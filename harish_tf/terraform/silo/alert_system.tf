module "alert_system" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/apps/alert-system"

  aws_account_id = "${local.account_id}"

  env            = "${local.env}"
  alert_system   = "${local.alert_system}"
}