provider "aws" {
  region  = "eu-west-1"
  version = "2.6.0"
}

terraform {
  backend "s3" {}
}

data "terraform_remote_state" "base_state" {
  backend = "s3"

  config {
    bucket = "${var.tf_s3_bucket}"
    region = "${var.tf_s3_region}"
    key    = "tf-state/base-${var.suffix}.tfstate"
  }
}

module "aws_iam_instance_profile" {
  source = "../base"
  suffix = "${var.suffix}"
}
