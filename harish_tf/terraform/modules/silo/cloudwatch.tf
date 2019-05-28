locals {
  slack_hook_id = "/global/slack/skipthedishesteam/hook_id"
}

module "ecs_to_slack_eu_west_1" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/apps/ecs-to-slack"

  region      = "eu-west-1"
  ssm_hook_id = "${local.slack_hook_id}"
}