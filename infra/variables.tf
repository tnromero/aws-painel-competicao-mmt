variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "artifacts_path" {
  description = "Path where lambda artifacts (zip) will be placed. Relative to infra module"
  type        = string
  default     = "${path.module}/artifacts"
}
