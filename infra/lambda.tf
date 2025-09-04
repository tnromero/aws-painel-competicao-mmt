# # Lambda Function
# resource "aws_lambda_function" "competition" {
#   filename         = "${path.module}/artifacts/competition.zip"
#   function_name    = "mmt-competition-lambda"
#   role             = aws_iam_role.lambda_exec.arn
#   handler          = "app.lambda_handler"
#   runtime          = "python3.12"
#   source_code_hash = filebase64sha256("${path.module}/artifacts/competition.zip")
#   depends_on       = [aws_iam_role_policy_attachment.lambda_basic]
# 
#   vpc_config {
#     subnet_ids         = [aws_subnet.main.id]
#     security_group_ids = [aws_security_group.lambda.id]
#   }
# }
