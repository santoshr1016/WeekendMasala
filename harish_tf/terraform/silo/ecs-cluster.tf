module "inc2bator_cluster" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/ecs-cluster"

  env               = "${var.env}"
  key_name          = "${var.key_name}"

  iam_role          = "${var.instance_profile_name}"

  asg_min           = "${lookup(var.asg_api_inc2bator, "min")}"
  asg_desired       = "${lookup(var.asg_api_inc2bator, "desired")}"
  asg_max           = "${lookup(var.asg_api_inc2bator, "max")}"
  instance_type     = "${lookup(var.asg_api_inc2bator, "instance_type")}"

  stack_name        = "${lookup(local.names, "full")}-${var.env}"
  stack_name_short  = "${lookup(local.names, "short")}-${var.env}"

  resource_tags     = "${local.cluster_tags}"

  vpc_subnet_ids    = "${module.vpc.subnet_ids}"
  cluster_vpc_id    = "${module.vpc.vpc_id}"
  admin_subnet      = "${module.vpc.private_subnet_ids[0]}"

  cadvisor_revision = "${aws_ecs_task_definition.cadvisor.revision}"
  cadvisor_family   = "${aws_ecs_task_definition.cadvisor.family}"

  base_config       = "${var.base_config}"

  vpn_cidr_blocks   = "${var.vpn_cidr_blocks}"

}