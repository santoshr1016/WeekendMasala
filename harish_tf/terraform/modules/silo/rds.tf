module "rds_incubator_cluster" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/rds"

  name = "rds-${lookup(local.names, "full")}"

  env = "${var.env}"
  aws_account_id = "${local.account_id}"
  env_type = "${local.env_type}"
  r53_zone_id = "${data.aws_route53_zone.skip_internal.zone_id}"

  resource_tags = "${local.rds_tags}"
  sns_actions = "${local.sns_actions}"
  slow_log_arn = "${module.slow_logs_alerter.arn}"
  master = "${local.rds_core_master}"
  public_subnets = "${module.inc2bator_cluster.subnet_ids}"
}