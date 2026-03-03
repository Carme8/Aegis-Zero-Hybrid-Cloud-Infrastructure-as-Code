resource "aws_dynamodb_table" "metadata" {
  name           = "ghost-infra-metadata"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

} 
