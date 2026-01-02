variable "gitlab_access_token" {
  type      = string
  sensitive = true
}

provider "gitlab" {
  token    = var.gitlab_access_token
  base_url = var.gitlab_api_url
}

resource "gitlab_cluster_agent" "gke_agent" {
  project = "24379"
  name    = "gke-agent"
}

resource "gitlab_cluster_agent_token" "agent_token" {
  project  = "24379"
  agent_id = gitlab_cluster_agent.gke_agent.agent_id
  name     = "terraform-generated-token"
}

output "agent_token" {
  value     = gitlab_cluster_agent_token.agent_token.token
  sensitive = true
}