provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "rsk_bucket" {
  bucket = "rsk-s3-bucket"
}

