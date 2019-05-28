locals {

  env = "${lookup(var.base_config, "env")}"
  region  = "${lookup(var.base_config, "region")}"
  env_type = "${lookup(var.base_config, "env_type")}"
  account_id = "${lookup(var.base_config, "account_id")}"

  names = {
    short = "ecs-${var.suffix}"
    full  = "ecs-inc2btr-${var.suffix}"
  }

  _resource_tags = {
    "je:metadata:dept"    = "skip"
    "je:metadata:env"     = "${var.env}"
    "je:metadata:envtype" = "dev"
    "je:metadata:owners"  = "incubator-${var.suffix}"
    "je:metadata:silo"    = "inc2bator"
    "je:metadata:tenant"  = "all"
    "je:metadata:tier"    = "5"
    "Terraform"           = "True"
  }

  # load balance
  lb_config = {
    is_api = "true"
    is_shared_alb = "true"
    dns_name = "${module.inc2bator_cluster.alb_dns}"
    zone_id = "${module.inc2bator_cluster.alb_zone_id}"
    arn = "${module.inc2bator_cluster.alb_arn}"
    arn_suffix = "${module.inc2bator_cluster.alb_arn_suffix}"
    listener_arn = "${module.inc2bator_cluster.alb_listener_arn}"
    sg_id = "${module.inc2bator_cluster.alb_sg_id}"
    r53_hosted_zone_id = "${data.aws_route53_zone.skip_internal.zone_id}"
    subnet_ids = "${join(",",module.inc2bator_cluster.subnet_ids)}"
  }

  # cluster
  cluster_config = {
    arn = "${module.inc2bator_cluster.cluster_arn}"
    vpc_id = "${module.inc2bator_cluster.vpc_id}"
    subnet_ids = "${module.inc2bator_cluster.subnet_ids}"
    instance_sg_id = "${module.inc2bator_cluster.instance_sg_id}"
  }

  cluster = {
    "je:metadata:feature" = "cluster-${var.suffix}"
    "Name"                = "cluster-${var.env}-${var.suffix}"
    "Environment"         = "${var.env}"
  }

  cluster_tags = "${merge(local._resource_tags, local.cluster)}"

  # alert

  sns_actions = "${module.alert_system.alert_system_arns}"

  alert_system = {
    "send_to_slack" = "false"
    "ssm_hook_id"   = "/global/slack/skipthedishesteam/hook_id_priscilacarval"
    "s3_bucket"     = "${var.tf_s3_bucket}"
    "je:metadata:envtype" = "alpha"
    "je:metadata:tenant"  = "na"
  }

  slow_logs_tags_defaults = {
    "je:metadata:feature" = "slow_logs_alerter"
    "je:metadata:tier"    = "5"
  }

  slow_logs_tags = "${merge(local._resource_tags, local.slow_logs_tags_defaults)}"

  # rds
  rds = {
    "je:metadata:feature" = "rds-${var.suffix}"
    "Name"                = "rds-${var.env}-${var.suffix}"
    "Environment"         = "${var.env}"
  }

  rds_tags = "${merge(local._resource_tags, local.rds)}"

  rds_core_master_defaults = {
    create                              = "true"
    multi_az                            = "${local.env_type != "dev" ? "true" : "false"}"
    skip_final_snapshot                 = "${local.env_type != "prod" ? "true" : "false"}"
    create_free_space_alert             = "true"
    create_free_space_alarm             = "true"
    create_cpu_alert                    = "true"
    iam_database_authentication_enabled = "true"
  }

  rds_core_master = "${merge(local.rds_core_master_defaults, var.rds_core_master)}"

  # service api
  api_name = "${var.resource_tags_api["je:metadata:feature"]}-${var.env}-${var.suffix}"

  resource_tags_api = "${merge(local._resource_tags, var.resource_tags_api, map("Name", local.api_name))}"

  service_cfg_api = {
    name = "${local.api_name}"
    port = "${var.resource_tags_api["port"]}"
  }

  service_config_api = "${merge(local.service_cfg_api, var.service_api_inc2bator)}"

  task_cfg_api = {
    task_policies = "${module.task_policy_api.policy}"
  }

  task_config_api = "${merge(var.service_api_inc2bator, local.task_cfg_api)}"

  # service jslice
  jslice_name = "${var.resource_tags_jslice["je:metadata:feature"]}-${var.env}-${var.suffix}"

  resource_tags_jslice = "${merge(local._resource_tags, var.resource_tags_jslice, map("Name", local.jslice_name))}"

  service_cfg_jslice = {
    name = "${local.jslice_name}"
    port = "${var.resource_tags_jslice["port"]}"
  }

  service_config_jslice = "${merge(local.service_cfg_jslice, var.service_jslice_inc2bator)}"

  task_cfg_jslice = {
    task_policies = "${module.task_policy_jslice.policy}"
  }

  task_config_jslice = "${merge(var.service_api_inc2bator, local.task_cfg_jslice)}"

  #vpc

  admin_vpc = {
    enable_nat_gateway   = "true"
    enable_dns_support   = "true"
    enable_dns_hostnames = "true"
    availability_zone = "a"
  }

  vpc_azs = ["${local.region}a", "${local.region}b", "${local.region}c"]
}

variable "env" {}

variable "suffix" {
  type        = "string"
  description = "The suffix of the incubatee"
}

variable "key_name" {
  type        = "string"
  description = "Name of the SSH Key"
}

variable "base_config" {
  type = "map"

  description = <<EOF
      env: (Required) The env of the resources.
      account_id: (Optional) The ID of the AWS account. Default: "162884609747";
  EOF
}

variable "instance_profile_name" {
  type = "string"

  description = "The instance profile name"
}

# S3
variable "tf_s3_bucket" {
  type        = "string"
  description = "S3 bucket where terraform state will be stored"
}

# rds

variable "rds_core_master" {
  type = "map"
  description = <<EOF
    Variables for the Master Instance:

    create : (Optional) Create database? Type: Boolean. Default: "true".
    create_free_space_alert: (Optional) Create RDS CloudWatch free space alert when space below 20%. Default: "true".
    create_free_space_alarm: (Optional) Create RDS CloudWatch free space alarm when space below 10%. Default: "true".
    create_cpu_alert: (Optional) Create RDS CloudWatch cpu alert when maximum up to 50% or Defined. Default: "true".
    iam_database_authentication_enabled: (Optional) Enable IAM Authentication. Type: Boolean. Default: "true".
 EOF
}

# vpn
variable "vpn_cidr_blocks" {
  type        = "list"
  description = "CIDR for VPN Server and VPN Client"
}

# vpc

variable "vpc_cidr_block" {
  type = "string"
  default = "192.168.0.0/16"
  description = "The range of id that should be used into vpc"
}

variable "vpc_public_subnets" {
  type = "list"
}

variable "vpc_private_subnets" {
  type = "list"
}

# VPC - Security Group Configuration

variable "vpc_sg_name_desc" {
  type        = "map"
  description = "Map contain name and description of security groups"
}

variable "vpc_sg_rules_offices" {
  type        = "list"
  description = "Security group ingress ips, description and ports"
}

variable "vpc_sg_rules_individuals" {
  default = []
  type        = "list"
  description = "Security group ingress ips, description and ports"
}

variable "vpc_sg_rules_haproxy" {
  type        = "list"
  description = "Security group ingress ips, description and ports"
}

# api_inc2bator

variable "resource_tags_api" {
  type = "map"

  description = <<EOF
    Tags for asset tracking, triage, and cost allocation
        je:metadata:feature - (Required) - Application name
  EOF
}

variable "asg_api_inc2bator" {
  type        = "map"
  description = <<EOF
    Map of variables for API Inc2Bator Auto Scaling Group

    min           - (Required) Minimum number of containers
    desired       - (Required) The desired number of containers
    max           - (Required) Maximum number of containers
    instance_type - (Required) Instance Type
  EOF
}

variable "service_api_inc2bator" {
  type        = "map"
  description = <<EOF
    Map of variables for API Inc2bator Service

    cpu: (Required) The number of CPU units that the each task reserves.
    memory: (Required) The number of memory units that the each task reserves.
    image_name: (Optional) The image name used as the name of the ECR repo. Default: "var.name-var.base_config.env".
    image_tag: (Required) The image tag used for the task definition.
    app_type: (Required) The App Type of the task that is running. Generally `java`, `python`, `node`, `ebs` or `kitt`.
    use_new_relic: (Optional) Boolean used to enable New Relic in the task definition. Default: "false".
    use_appdynamics (Optional) Boolean used to enable AppDynamics in the task definition. Default: "false".
    dedicated (Optional) Boolean used to determine if the task is dedicated or not on the task definition. Default: "false".
    load_balancer (Optional) String used to set the load balancer env var on the task defnition. Default: "".
    volume_name (Optional) The volume name to use on the task defnition. Default: "".
    volume_path (Optional) The volume path to use on the task defnition. Default: "".
    task_policies (Optional) A "|" delimited list of policy strings to attach to the task role. Default: "".
    awslogs_datetime_format (Optional) The awslogs-datetime-format used in the task definition. Default: "%Y-%m-%dT%H:%M:%S%LZ".
    name_suffix: (Optional) The name suffix to pass in the environment variables of the task definition. Default: "".
    custom_vpn_ingress_rules: (Optional) Set to "true" if you want to define your own VPN ingress rules on aws_security_group.task. Only relevant when service_config.is_fargate is "true". Default: "false"
    custom_task_egress_rules: (Optional) Set to "true" if you want to define your own egress rules on aws_security_group.task. Only relevant when service_config.is_fargate is "true". Default: "false"
    role_name: (Optional) Overrides task`s role_name. Default: name-env-task.
  EOF
}

# jslice_inc2bator

variable "resource_tags_jslice" {
  type = "map"

  description = <<EOF
    Tags for asset tracking, triage, and cost allocation
        je:metadata:feature - (Required) - Application name
  EOF
}

variable "asg_jslice_inc2bator" {
  type        = "map"
  description = <<EOF
    Map of variables for API Inc2Bator Auto Scaling Group

    min           - (Required) Minimum number of containers
    desired       - (Required) The desired number of containers
    max           - (Required) Maximum number of containers
    instance_type - (Required) Instance Type
  EOF
}

variable "service_jslice_inc2bator" {
  type        = "map"
  description = <<EOF
    Map of variables for API Inc2bator Service

    cpu: (Required) The number of CPU units that the each task reserves.
    memory: (Required) The number of memory units that the each task reserves.
    image_name: (Optional) The image name used as the name of the ECR repo. Default: "var.name-var.base_config.env".
    image_tag: (Required) The image tag used for the task definition.
    app_type: (Required) The App Type of the task that is running. Generally `java`, `python`, `node`, `ebs` or `kitt`.
    use_new_relic: (Optional) Boolean used to enable New Relic in the task definition. Default: "false".
    use_appdynamics (Optional) Boolean used to enable AppDynamics in the task definition. Default: "false".
    dedicated (Optional) Boolean used to determine if the task is dedicated or not on the task definition. Default: "false".
    load_balancer (Optional) String used to set the load balancer env var on the task defnition. Default: "".
    volume_name (Optional) The volume name to use on the task defnition. Default: "".
    volume_path (Optional) The volume path to use on the task defnition. Default: "".
    task_policies (Optional) A "|" delimited list of policy strings to attach to the task role. Default: "".
    awslogs_datetime_format (Optional) The awslogs-datetime-format used in the task definition. Default: "%Y-%m-%dT%H:%M:%S%LZ".
    name_suffix: (Optional) The name suffix to pass in the environment variables of the task definition. Default: "".
    custom_vpn_ingress_rules: (Optional) Set to "true" if you want to define your own VPN ingress rules on aws_security_group.task. Only relevant when service_config.is_fargate is "true". Default: "false"
    custom_task_egress_rules: (Optional) Set to "true" if you want to define your own egress rules on aws_security_group.task. Only relevant when service_config.is_fargate is "true". Default: "false"
    role_name: (Optional) Overrides task`s role_name. Default: name-env-task.
  EOF
}
