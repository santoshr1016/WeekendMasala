provider "aws" {
  region  = "eu-west-1"
  version = "2.6.0"
}

terraform {
  backend "s3" {}
}

variable "suffix" {
  type = "string"
}
