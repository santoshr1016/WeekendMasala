locals {


}

module "silo" {
  source = "../modules/silo"

  suffix = "${var.suffix}"
  key_name = "${var.key_name}"
  base_config = "${var.base_config}"
  env = "${var.base_config["env"]}"
  instance_profile_name = "${module.aws_iam_instance_profile.ecs_app_instance_profile_name}"

  # RDS
  rds_core_master = "${var.rds_core_master}"
  tf_s3_bucket = "${var.tf_s3_bucket}"

  # VPN
  vpn_cidr_blocks = "${var.vpn_cidr_blocks}"

  # VPC
  vpc_cidr_block = "${var.vpc_cidr_block}"
  vpc_public_subnets = "${var.vpc_public_subnets}"
  vpc_private_subnets = "${var.vpc_private_subnets}"

  # VPC - Security Group Configuration

  vpc_sg_name_desc = "${var.vpc_sg_name_desc}"
  vpc_sg_rules_haproxy = "${var.vpc_sg_rules_haproxy}"
  vpc_sg_rules_offices = "${var.vpc_sg_rules_offices}"
  vpc_sg_rules_individuals = "${var.vpc_sg_rules_individuals}"

  # api_inc2bator
  resource_tags_api = "${var.resource_tags_api}"
  asg_api_inc2bator = "${var.asg_api_inc2bator}"
  service_api_inc2bator = "${var.service_api_inc2bator}"

  # jslice_inc2bator
  resource_tags_jslice = "${var.resource_tags_jslice}"
  asg_jslice_inc2bator = "${var.asg_jslice_inc2bator}"
  service_jslice_inc2bator = "${var.service_jslice_inc2bator}"

}
