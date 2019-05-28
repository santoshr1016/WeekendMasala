tf_s3_region = "eu-west-1"

tf_s3_bucket = "skip-incubator-terraform-devops"

suffix = "priscilacarval"

key_name = "DevOpsInc2bator"

base_config = {
  env         = "alpha"
  account_id  = "888245128194"
  env_tag     = "alpha"
  env_type    = "alpha"
  region      = "eu-west-1"
}

# RDS
rds_core_master = {
  create_free_space_alert = "false"
  create_free_space_alarm = "false"
  create_cpu_alert = "false"
  create_burst_alarm = "false"
  create_burst_alert = "false"
  create_lag_alert = "false"
  create_lag_alarm = "false"
  create_replication_error_alarm = "false"
  create_disk_queue_depth_alert= "false"
  iam_database_authentication_enabled = "true"
}

# VPN
vpn_cidr_blocks = ["52.42.212.191/32", "10.210.0.0/16"]

# VPC

vpc_cidr_block = "192.168.0.0/16"

vpc_private_subnets = ["192.168.1.0/24", "192.168.11.0/24"]

vpc_public_subnets  = ["192.168.101.0/24", "192.168.111.0/24"]

# VPC - Security Group Configuration
vpc_sg_name_desc = {
  name_sg_override_offices     = "Inc2batorAlpha-Offices"
  name_sg_override_individuals = "Inc2batorAlpha-Individuals"
  name_sg_override_haproxy     = "core.haproxy"

  description_sg_override_individuals = "Individual access to the core vpc resources"
  description_sg_override_offices     = "Office access to the core vpc resources"
  description_sg_override_haproxy     = "Allows access to the core servers"
}

vpc_sg_rules_offices = [
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "192.168.0.0/16"
    from_port   = "0"
    to_port     = "65535"
    description = "Inc2bator"
  },
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "52.42.212.191/32"
    from_port   = "0"
    to_port     = "65535"
    description = "AWS VPN"
  },
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "10.210.0.0/16"
    from_port   = "0"
    to_port     = "65535"
    description = "AWS VPN Client"
  },
]

vpc_sg_rules_individuals = [
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "192.168.0.0/16"
    from_port   = "0"
    to_port     = "65535"
    description = "Inc2bator"
  }
]

vpc_sg_rules_haproxy = [
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "192.168.0.0/16"
    from_port   = "0"
    to_port     = "65535"
    description = "Inc2bator"
  }
]

# api_inc2bator

resource_tags_api = {
  "je:metadata:feature" = "api"
  "Name"                = "api-alpha"
  "port"                = "2727"
}

asg_api_inc2bator = {
  min           = 1
  desired       = 1
  max           = 2
  instance_type = "t3.micro"
}

service_api_inc2bator = {
  cpu           = 128
  memory        = 512
  task_count    = 1
  image_tag     = "latest"
  app_type      = "java"
}

# jslice_inc2bator

resource_tags_jslice = {
  "je:metadata:feature" = "jslice-priscilacarval"
  "Name"                = "jslice-alpha-priscilacarval"
  "port"                = "2828"
}

asg_jslice_inc2bator = {
  min           = 1
  desired       = 1
  max           = 2
  instance_type = "t3.micro"
}

service_jslice_inc2bator = {
  cpu           = 128
  memory        = 512
  task_count    = 1
  image_tag     = "latest"
  app_type      = "java"
}
