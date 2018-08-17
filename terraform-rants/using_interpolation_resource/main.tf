provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "rsk_bucket" {
  bucket = "rsk-s3-bucket"
}

resource "aws_iam_policy" "rsk_bucket_policy" {
  name = "rsk-s3-bucket-policy"

  # Interpolation for s3
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action":
      [
        "s3:ListBucket"
      ],
      "Effect": "Allow",
        "Resource":
        [
          "${aws_s3_bucket.rsk_bucket.arn}"
        ]
    }
  ]
}
POLICY
}