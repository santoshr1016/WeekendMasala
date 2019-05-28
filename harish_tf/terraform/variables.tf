variable "tf_s3_bucket" {
  type        = "string"
  default     = "skip-terraform"
  description = "S3 bucket where terraform state will be stored"
}

variable "tf_s3_region" {
  type        = "string"
  default     = "eu-west-1"
  description = "Region to find terraform state bucket"
}

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
      env_tag: (Required) The tag for the environment
      account_id: (Optional) The ID of the AWS account.;
  EOF
}

# rds

variable "rds_core_master" {
  type = "map"
  description = <<EOF
    create                              = (Optional) rds parameter creates database. Defaults: true
    create_free_space_alert             = (Optional) rds parameter free space alert. Defaults: true
    create_free_space_alarm             = (Optional) rds parameter free space alarm. Defaults: true
    create_cpu_alert                    = (Optional) rds parameter cpu alert. Defaults: true
    iam_database_authentication_enabled = (Optional) rds parameter iam database authentication enabled. Defaults: true
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

    min           - (Required) Minimum number of containers
    desired       - (Required) The desired number of containers
    max           - (Required) Maximum number of containers
    instance_type - (Required) Instance Type
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
