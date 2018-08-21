# We have defined our modules in s3_mod folder and we gonna use them here.

provider "aws" {
  region = "us-east-1"
}

module "versioned_bucket" {
  source = "./s3_mod"
  bucket_name = "rsk-versioned-bucket"
  versioning = true
}

module "normal_bucket" {
  source = "./s3_mod"
  bucket_name = "rsk-normal-bucket"
}


output "versioned_bucket_name" {
  value = "${module.versioned_bucket.s3_bucket_arn}"
}

output "normal_bucket_name" {
  value = "${module.normal_bucket.s3_bucket_arn}"
}