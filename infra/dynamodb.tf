resource "aws_dynamodb_table" "mmt" {
  name         = "mmt-${var.environment}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PK"
  range_key    = "SK"
  region       = "${var.aws_region}"

  attribute {
    name = "PK"
    type = "S"
  }

  attribute {
    name = "SK"
    type = "S"
  }

  tags = merge(var.default_tags, {
      name = "mmt-${var.environment}"
    })
}