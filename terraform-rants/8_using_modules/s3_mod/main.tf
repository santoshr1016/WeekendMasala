resource "aws_s3_bucket" "my_bucket_rsant" {
  bucket = "${var.bucket_name}"

  versioning {
    enabled = "${var.versioning}"
  }
}