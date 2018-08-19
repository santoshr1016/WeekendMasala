provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "rsk-test-bucket"
}

resource "aws_iam_user" "santosh" {
  name = "rsk-santosh"
}

# Understand it as
# 1. Load the Policy file
# 2. Fill the placeholders / variables in the file using the "vars" snippet

data "template_file" "bucket_policy" {
  template = "${file("policy.json")}"

  vars {
    bucket_arn = "${aws_s3_bucket.my_bucket.arn}"
  }
}

# Loading the "data" which has got all placeholders filled using the "rendered"
resource "aws_iam_user_policy" "my_policy" {
  name = "my-policy"
  user = "${aws_iam_user.santosh.name}"
  policy = "${data.template_file.bucket_policy.rendered}"
}

output "policy" {
  value = "${aws_iam_user_policy.my_policy.policy}"
}