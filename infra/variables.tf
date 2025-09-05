variable "environment" {
  description = "Ambiente de implantação (dev, prod, etc.)"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Nome do projeto"
  type        = string
  default     = "mmt"
}

variable "subnet_cidr_block" {
  description = "Bloco CIDR da Subnet"
  type        = string
}

variable "vpc_cidr_block" {
  description = "Bloco CIDR da VPC"
  type        = string
}

variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
}

# variable "artifacts_path" {
#   description = "Path where lambda artifacts (zip) will be placed. Relative to infra module"
#   type        = string
# }

# Tags padrão para todos os recursos
variable "default_tags" {
  description = "Tags padrão para todos os recursos AWS"
  type        = map(string)
}

variable "account_id" {
  description = "AWS Account ID"
  type        = string
}