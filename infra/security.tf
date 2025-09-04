# Security group para Lambda
resource "aws_security_group" "lambda" {
  name        = "${var.project_name}-${var.environment}-lambda-sg"
  description = "Allow Lambda outbound traffic"
  vpc_id      = aws_vpc.main.id
  tags = merge(var.default_tags, {
    Name = "${var.project_name}-${var.environment}-lambda-sg"
  })

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
