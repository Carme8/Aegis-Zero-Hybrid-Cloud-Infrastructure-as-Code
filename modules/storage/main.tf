resource "aws_s3_bucket" "vault" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_server_side_encryption_configuration" "vault_encryption" {
  bucket = aws_s3_bucket.vault.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = "alias/aegis-master-key"
      sse_algorithm     = "aws:kms"
    }
  }
}

variable "bucket_name" {
  type = string
}