variable "gitlab_access_token" {
  type      = string
  sensitive = true
}

provider "gitlab" {
  token    = var.gitlab_access_token
  base_url = var.gitlab_api_url
}