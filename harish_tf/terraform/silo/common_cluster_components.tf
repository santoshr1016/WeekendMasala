module "aws_iam_instance_profile" {
  source = "../../base"
  suffix = "api-${var.suffix}"
}

data "aws_route53_zone" "skip_internal" {
  zone_id = "Z3BISK0SREYAQN"
}

data "template_file" "cadvisor" {
  template = "${file("${path.module}/files/cadvisor.json")}"
}

resource "aws_ecs_task_definition" "cadvisor" {
  family                = "cadvisor"
  container_definitions = "${data.template_file.cadvisor.rendered}"

  volume {
    name      = "root"
    host_path = "/"
  }

  volume {
    name      = "var_run"
    host_path = "/var/run"
  }

  volume {
    name      = "sys"
    host_path = "/sys"
  }

  volume {
    name      = "var_lib_docker"
    host_path = "/var/lib/docker/"
  }

  volume {
    name      = "cgroup"
    host_path = "/sys/fs/cgroup"
  }
}
