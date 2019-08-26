resource "aws_instance" "sample_instance" {
  ami = "ami-XXXXX"
  instance_type = "t2.micro"

  tags {
    Name = "Sample instance"
  }
}