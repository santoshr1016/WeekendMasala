module "vpc" {
  source = "git::ssh://git@bitbucket.org/skipthedishes/terraform.git?ref=v19.13.1//terraform/modules/core-vpc"

  name          = "inc2bator-core"
  env           = "${var.env}"
  resource_tags = "${local.resource_tags_api}"

  cidr_block    = "${var.vpc_cidr_block}"
  region        = "${local.region}"
  zone_id       = "${data.aws_route53_zone.skip_internal.zone_id}"

  azs                       = "${local.vpc_azs}"
  subnet_cidr_block         =  "${var.vpc_public_subnets}"
  private_subnet_cidr_block = "${var.vpc_private_subnets}"

  core_vpc_sg_rules_offices       = "${var.vpc_sg_rules_offices}"
  name_sg_override_offices        = "${lookup(var.vpc_sg_name_desc,"name_sg_override_offices","")}"
  description_sg_override_offices = "${lookup(var.vpc_sg_name_desc,"description_sg_override_offices","")}"

  core_vpc_sg_rules_individuals       = "${var.vpc_sg_rules_individuals}"
  name_sg_override_individuals        = "${lookup(var.vpc_sg_name_desc,"name_sg_override_individuals","")}"
  description_sg_override_individuals = "${lookup(var.vpc_sg_name_desc,"description_sg_override_individuals","")}"

  core_vpc_sg_rules_haproxy       = "${var.vpc_sg_rules_haproxy}"
  name_sg_override_haproxy        = "${lookup(var.vpc_sg_name_desc,"name_sg_override_haproxy","")}"
  description_sg_override_haproxy = "${lookup(var.vpc_sg_name_desc,"description_sg_override_haproxy","")}"

}