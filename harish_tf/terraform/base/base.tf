data "aws_iam_policy_document" "instance_profile" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]

    effect = "Allow"

    principals {
      identifiers = ["ec2.amazonaws.com"]
      type = "Service"
    }
  }
}

resource "aws_iam_role" "app_instance" {
  name = "ecs-cluster-instance-role-${var.suffix}"

  assume_role_policy = "${data.aws_iam_policy_document.instance_profile.json}"
}

resource "aws_iam_instance_profile" "app_instance" {
  name = "ecs-cluster-instance-profile-${var.suffix}"

  role = "${aws_iam_role.app_instance.name}"
}

resource "aws_iam_role_policy" "app_instance" {
  name = "ecs-cluster-instance-policy-${var.suffix}"
  role = "${aws_iam_role.app_instance.name}"

  policy = "${data.aws_iam_policy_document.instance_role.json}"
}

resource "aws_iam_role_policy_attachment" "app_instance" {
  role       = "${aws_iam_role.app_instance.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}



data "aws_iam_policy_document" "service_assume_role" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]

    effect = "Allow"

    principals {
      identifiers = ["ecs.amazonaws.com"]
      type = "Service"
    }
  }
}

resource "aws_iam_role" "ecs_service" {
  name = "ecs-cluster-service-role-${var.suffix}"

  assume_role_policy = "${data.aws_iam_policy_document.service_assume_role.json}"
}

resource "aws_iam_role_policy" "ecs_service" {
  name = "ecs-cluster-service-policy"
  role = "${aws_iam_role.ecs_service.name}"

  policy = "${data.aws_iam_policy_document.service_role.json}"
}

data "aws_iam_policy_document" "service_role" {
  statement {
    actions = [
      "elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
      "elasticloadbalancing:DeregisterTargets",
      "elasticloadbalancing:Describe*",
      "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
      "elasticloadbalancing:RegisterTargets",
      "ec2:Describe*",
      "ec2:AuthorizeSecurityGroupIngress"
    ]

    effect = "Allow"

    resources = [
      "*"
    ]
  }
}


data "aws_iam_policy_document" "instance_role" {
  statement {
    actions = [
      "ecs:StartTask"
    ]

    effect = "Allow"

    resources = [
      "*"
    ]
  }
}

resource "aws_ssm_parameter" "slack_hook_id" {
  name = "/global/slack/skipthedishesteam/hook_id_${var.suffix}"
  type = "String"
  value = "changeme"
}
