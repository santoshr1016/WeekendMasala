provider "aws" {
  region = "us-east-1"
}

locals {
  prefix = "rsk-test-first"
}

resource "aws_s3_bucket" "rsk_bucket" {
  bucket = "${local.prefix}-bucket"
}