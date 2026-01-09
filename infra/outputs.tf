output "region" {
  value = var.region
}

output "zone" {
  value = var.zone
}

output "cluster_name" {
  value = google_container_cluster.primary.name
  description = "Name of the GKE cluster."
}

output "cluster_ca_certificate" {
  value     = google_container_cluster.primary.master_auth[0].cluster_ca_certificate
  sensitive = true
  description = "Public certificate of the cluster (needed for TLS connection)."
}

output "cloud_sql_instance_connection_name" {
  value = google_sql_database_instance.postgres_instance.connection_name
  description = "Connection string for the Cloud SQL instance."
}

output "cloudsql_gsa_email" {
  value = google_service_account.cloudsql_sa.email
  description = "Email of the GSA to bind to the K8s Service Account."
}

output "model_bucket_name" {
  value       = google_storage_bucket.models_bucket.name
  description = "Name of the GCS bucket for model artifacts."
}

output "ingress_ip_name" {
  value = google_compute_global_address.ingress_ip.name
  description = "Name of the static IP for the Ingress."
}

output "ingress_ip_address" {
  value = google_compute_global_address.ingress_ip.address
  description = "The external IP address of the Ingress."
}