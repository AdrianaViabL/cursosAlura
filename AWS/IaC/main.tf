terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "default"
  region = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-094125af156557ca2"
  instance_type = "t2.micro"
  key_name = "iac-teste"
  user_data = <<-EOF
                 #!/bin/bash - codigo bash a ser executado
                 # esse codigo vai: criar um arquivo index.html com um codigo html dentro na pasta home/ubuntu 
                 # Obs.: o parametro user_data so executa na CRIAÇÃO da instancia, qualquer alteração futura não será vista dentro da instancia
                 # para isso deve-se (nesse caso) excluir essa instancia (terraform destroy) e criar ele novamente
                 echo "<h1>Feito com Terraform</h1>" > index.html
                 #nohup busybox httpd -f -p 8080 &
                 EOF
  user_data_replace_on_change = true
  tags = {
    Name = "Second instance"
  }
}