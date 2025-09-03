terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_dynamodb_table" "entities" {
  name         = "mmt-entities"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pk"
  range_key    = "sk"

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }
}

resource "aws_sqs_queue" "events" {
  name = "mmt-events.fifo"
  fifo_queue = true
}

resource "aws_iam_role" "lambda_exec" {
  name = "mmt-lambda-exec-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_policy" "lambda_ddb_sqs_policy" {
  name        = "mmt-lambda-ddb-sqs"
  description = "Allow Lambdas to access DynamoDB and SQS"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "dynamodb:PutItem",
          "dynamodb:GetItem",
          "dynamodb:Query",
          "dynamodb:UpdateItem",
          "dynamodb:Scan"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "sqs:SendMessage",
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_extra" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda_ddb_sqs_policy.arn
}

# Lambda function for 'competition' service - expects artifact at infra/artifacts/competition.zip
resource "aws_lambda_function" "competition" {
  filename         = "${path.module}/artifacts/competition.zip"
  function_name    = "mmt-competition-lambda"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "app.lambda_handler"
  runtime          = "python3.11"
  source_code_hash = filebase64sha256("${path.module}/artifacts/competition.zip")
  depends_on       = [aws_iam_role_policy_attachment.lambda_basic]
}

# Note: More services can be added analogously (modalities, teams, athletes, scoring)

output "dynamodb_table_name" {
  value = aws_dynamodb_table.entities.name
}

output "sqs_queue_url" {
  value = aws_sqs_queue.events.id
}

output "competition_lambda_arn" {
  value = aws_lambda_function.competition.arn
}
