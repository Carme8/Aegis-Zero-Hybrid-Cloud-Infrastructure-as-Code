resource "aws_kms_key" "aegis_key" {
  description             = "Chiave Master per Aegis-Zero"
  deletion_window_in_days = 7
  enable_key_rotation     = true
}

resource "aws_kms_alias" "aegis_key_alias" {
  name          = "alias/aegis-master-key"
  target_key_id = aws_kms_key.aegis_key.key_id
}

output "key_arn" {
  value = aws_kms_key.aegis_key.arn
}