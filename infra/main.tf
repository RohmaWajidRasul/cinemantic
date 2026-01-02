# --- 1. Provider Configuration ---

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
    gitlab = {
      source  = "gitlabhq/gitlab"
      version = "~> 16.0"
    }
  }
  backend "http" {}
}

provider "google" {
  project = var.project_id
  region  = var.region
}
provider "google-beta" {
  project = var.project_id
  region  = var.region
}

data "google_client_config" "default" {}

provider "kubernetes" {
  host                   = "https://${google_container_cluster.primary.endpoint}"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(google_container_cluster.primary.master_auth[0].cluster_ca_certificate)
}



# --- 2. Networking (VPC and Private Service Connection) ---

resource "google_compute_network" "vpc_network" {
  name                    = var.network_name
  auto_create_subnetworks = false
}

# Reserve a private IP range for the Cloud SQL instance
resource "google_compute_global_address" "private_ip_range" {
  name          = "google-managed-services-range"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.vpc_network.id
}

# Create the private connection for Google services
resource "google_service_networking_connection" "private_vpc_connection" {
  service                  = "servicenetworking.googleapis.com"
  network                  = google_compute_network.vpc_network.id
  reserved_peering_ranges  = [google_compute_global_address.private_ip_range.name]
  depends_on               = [google_compute_global_address.private_ip_range]
}

# Create subnet for GKE
resource "google_compute_subnetwork" "subnet" {
  name          = "${var.network_name}-subnet"
  region        = var.region
  network       = google_compute_network.vpc_network.id
  ip_cidr_range = "10.10.0.0/24"

  secondary_ip_range {
    range_name    = "k8s-pod-range"
    ip_cidr_range = "10.48.0.0/14"
  }
  secondary_ip_range {
    range_name    = "k8s-service-range"
    ip_cidr_range = "10.52.0.0/20"
  }
}

# Create a Cloud Router (NAT needs this to function)
resource "google_compute_router" "router" {
  name    = "nat-router"
  network = google_compute_network.vpc_network.name
  region  = var.region
}

# Create the Cloud NAT gateway
resource "google_compute_nat" "nat_gateway" {
  name                               = "main-nat-gateway"
  router                             = google_compute_router.router.name
  region                             = var.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"

  log_config {
    enable = true
    filter = "ERRORS_ONLY"
  }
}



# --- 3. Cloud SQL Instance (PostgreSQL with pgvector) ---

resource "google_sql_database_instance" "postgres_instance" {
  database_version = "POSTGRES_15"
  name             = "cinemantic-db"
  region           = var.region
  settings {
    tier = "db-custom-4-8192" # 4 vCPU, 8GB RAM
    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.vpc_network.id
    }
    disk_type = "PD_SSD"
    disk_size = 50
  }
  deletion_protection = false
  depends_on          = [google_service_networking_connection.private_vpc_connection]
}

resource "google_sql_database" "database" {
  instance = google_sql_database_instance.postgres_instance.name
  name     = "cinemantic_db"
}

resource "google_sql_user" "user" {
  instance = google_sql_database_instance.postgres_instance.name
  name     = var.db_user
  password = var.db_password
}



# --- 4. GKE Cluster Definition ---

resource "google_container_cluster" "primary" {
  name                     = "cinemantic-cluster"
  location                 = var.zone
  initial_node_count       = 1
  network                  = google_compute_network.vpc_network.id
  subnetwork               = google_compute_subnetwork.subnet.id
  remove_default_node_pool = true

  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }

  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }

  ip_allocation_policy {
    cluster_secondary_range_name  = "k8s-pod-range"
    services_secondary_range_name = "k8s-service-range"
  }

  deletion_protection = false
  
  depends_on = [google_service_networking_connection.private_vpc_connection]
}



# --- 5. Google Cloud Storage ---

# Create the GCS Bucket for storing model artifacts
resource "google_storage_bucket" "models_bucket" {
  name                        = "cinemantic-models-${var.project_id}"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
}



# --- 6. GKE Node Pools ---

# Standard Pool
resource "google_container_node_pool" "standard_pool" {
  cluster    = google_container_cluster.primary.name
  location   = var.zone
  name       = "standard-pool"
  node_count = 1

  autoscaling {
    min_node_count = 1
    max_node_count = 1
  }

  node_config {
    machine_type = "e2-highcpu-4"
    oauth_scopes = ["cloud-platform"]
    disk_size_gb = 50
    disk_type = "pd-ssd"
  }
}



# --- 7. IAM and Workload Identity Binding ---

resource "google_service_account" "cloudsql_sa" {
  account_id   = var.cloudsql_sa_id
  display_name = "GSA for Django Cloud SQL Access"
}

resource "google_project_iam_member" "cloudsql_client_binding" {
  project = var.project_id
  role    = "roles/cloudsql.client"
  member  = "serviceAccount:${google_service_account.cloudsql_sa.email}"
}

resource "google_project_iam_member" "gcs_viewer_binding" {
  project = var.project_id
  role    = "roles/storage.objectAdmin"
  member  = "serviceAccount:${google_service_account.cloudsql_sa.email}"
}

resource "google_service_account_iam_member" "workload_identity_binding" {
  service_account_id = google_service_account.cloudsql_sa.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "serviceAccount:${var.project_id}.svc.id.goog[default/app-sa]"

  depends_on = [
    google_container_cluster.primary
  ]
}

resource "kubernetes_role" "deployment_restarter" {
  metadata {
    name = "deployment-restarter"
    namespace = "default"
  }

  rule {
    api_groups = ["apps"]
    resources  = ["deployments"]
    verbs      = ["get", "patch"]
  }
}

resource "kubernetes_role_binding" "app_sa_restarter_binding" {
  metadata {
    name = "app-sa-restarter-binding"
    namespace = "default"
  }

  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = kubernetes_role.deployment_restarter.metadata[0].name
  }

  subject {
    kind      = "ServiceAccount"
    name      = "app-sa" # Must match the SA name in the K8s manifest
    namespace = "default"
  }
}

resource "google_compute_global_address" "ingress_ip" {
  name = "movie-recs-ip"
}