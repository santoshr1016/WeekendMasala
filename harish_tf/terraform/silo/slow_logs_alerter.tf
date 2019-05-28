module "slow_logs_alerter" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/apps/slow-logs-alerter"

  enable = "false"
  base_config = "${var.base_config}"
  tags        = "${local.slow_logs_tags}"
  s3_bucket = "${var.tf_s3_bucket}"
}