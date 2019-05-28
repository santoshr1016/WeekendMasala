module "api_service" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/modules_tf.git?ref=v5.1.0//modules/ecs-service"

  cluster_config = "${local.cluster_config}"
  base_config = "${var.base_config}"
  task_config = "${local.task_config_api}"
  lb_config = "${local.lb_config}"
  service_config = "${local.service_config_api}"
  resource_tags = "${local.resource_tags_api}"
}

module "task_policy_api" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/communications/policy"

  name = "api_service-${var.suffix}"
  env = "${var.env}"

}

module "jslice_service" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/modules_tf.git?ref=v5.1.0//modules/ecs-service"

  cluster_config = "${local.cluster_config}"
  base_config = "${var.base_config}"
  task_config = "${local.task_config_jslice}"
  lb_config = "${local.lb_config}"
  service_config = "${local.service_config_jslice}"
  resource_tags = "${local.resource_tags_jslice}"
}

module "task_policy_jslice" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/communications/policy"

  name = "jslice_service-${var.suffix}"
  env = "${var.env}"

}

