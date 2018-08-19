locals {
  name = "Santosh"
}

output "name_local" {
  value = "${local.name}"
}