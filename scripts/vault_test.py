import boto3

# Configurazione per LocalStack
ENDPOINT_URL = "http://localhost:4566"
REGION = "us-east-1"
BUCKET_NAME = "ai-vault-ghost-infra"
KEY_ALIAS = "alias/aegis-master-key"

# Inizializzazione client S3
s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name=REGION
)

def upload_encrypted_file():
    content = "Messaggio ultra-segreto criptato con KMS Aegis-Zero"
    print(f"--- Caricamento file nel bucket {BUCKET_NAME} ---")
    
    # Caricamento con specifica della chiave KMS
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key="top_secret.txt",
        Body=content,
        ServerSideEncryption="aws:kms",
        SSEKMSKeyId=KEY_ALIAS
    )
    print("✅ File caricato e criptato con successo!")

def download_and_read():
    print(f"--- Lettura file dal Vault ---")
    response = s3.get_object(Bucket=BUCKET_NAME, Key="top_secret.txt")
    data = response['Body'].read().decode('utf-8')
    print(f"🔓 Contenuto decriptato: {data}")

if __name__ == "__main__":
    upload_encrypted_file()
    download_and_read()