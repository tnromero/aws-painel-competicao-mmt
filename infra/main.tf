terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket = "mmt-thiagoromero-terraform"
    key    = "terraform.tfstate"
    region = "us-east-2"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.aws_region
}
