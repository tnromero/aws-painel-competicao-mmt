# Lambda Function
resource "aws_lambda_function" "lambda_athlete" {
	filename         = "${path.module}/artifacts/athlete.zip"
	function_name    = "mmt-athlete-lambda"
	role             = "arn:aws:iam::${var.account_id}:role/role-mmt-execution-lambda"
	handler          = "mmt.athlete.athlete_lambda_function.lambda_handler"
	runtime          = "python3.12"
	source_code_hash = filebase64sha256("${path.module}/artifacts/athlete.zip")
	
	vpc_config {
		subnet_ids         = [aws_subnet.main.id]
		security_group_ids = [aws_security_group.lambda.id]
	}
	tags = merge(var.default_tags, {
		Name = "mmt-athlete-lambda"
	})
}
