variable "gitlab_access_token" {
  type      = string
  sensitive = true
}

provider "gitlab" {
  token    = var.gitlab_access_token
  base_url = "${CI_SERVER_URL}/api/v4"
}

resource "gitlab_cluster_agent" "gke_agent" {
  project = var.project_id
  name    = "gke-agent"
}

resource "gitlab_cluster_agent_token" "agent_token" {
  project  = var.project_id
  agent_id = gitlab_cluster_agent.gke_agent.agent_id
  name     = "terraform-generated-token"
}

output "agent_token" {
  value     = gitlab_cluster_agent_token.agent_token.token
  sensitive = true
}