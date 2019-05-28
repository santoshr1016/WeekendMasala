key_name = "DevOpsInc2bator"
region = "eu-west-1"
suffix = "harishpal"
base_config = {
   env        = "alpha"
   account_id = "888245128194"
   env_tag    = "alpha"
   env_type   = "alpha"
 }
tf_s3_region = "eu-west-1"
tf_s3_bucket = "skip-incubator-terraform-devops"
# VPN
vpn_cidr_blocks = ["52.42.212.191/32", "10.210.0.0/16"]
VPC
vpc_cidr_block = "192.168.25.0/24"
vpc_public_subnets  = ["192.168.25.0/26", "192.168.25.64/26"]

vpc_private_subnets = ["192.168.25.128/26", "192.168.25.192/26"]
vpc_sg_name_desc = {
  name_sg_override_offices     = "Inc2batorAlpha-Offices"
  name_sg_override_individuals = "Inc2batorAlpha-Individuals"
  name_sg_override_haproxy     = "Inc2batorAlpha-Haproxy"

  description_sg_override_individuals = "Individual access to the core vpc resources"
  description_sg_override_offices     = "Office access to the core vpc resources"
  description_sg_override_haproxy     = "Allows access to the core servers"
vpc_sg_rules_offices = [
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "192.168.25.0/24"
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
    cidr        = "192.168.24.0/24"
    from_port   = "0"
    to_port     = "65535"
    description = "Inc2bator"
  }
]

vpc_sg_rules_haproxy = [
  {
    type        = "ingress"
    protocol    = "all"
    cidr        = "192.168.24.0/24"
    from_port   = "0"
    to_port     = "65535"
    description = "Inc2bator"
  }
]

# cluster
asg_cluster_inc2bator = {
   min           = 1
   desired       = 1
   max           = 2
   instance_type = "t3.micro"
 }
 
# api

resource_tags_api = {
  "je:metadata:feature" = "api"
  "Name"                = "api"
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
 }
 
# jslice

asg_jslice_inc2bator = {
  min           = 1
  desired       = 1
  max           = 2
  instance_type = "t3.micro"
}
