# 🛡️ Aegis-Zero: Ghost Infra
### Hybrid Cloud Infrastructure-as-Code (IaC)

Un'infrastruttura cloud modulare e sicura interamente riproducibile in locale. Progettata per simulare un ambiente AWS reale, focalizzandosi sulla protezione dei dati e sulla crittografia KMS.

## 🏗️ Architettura del Progetto
Il progetto è strutturato in moduli Terraform riutilizzabili:
* **Network**: VPC e configurazione di rete isolata.
* **Storage (S3)**: Bucket per il "Vault" dei dati sensibili.
* **Security (KMS)**: Gestione delle chiavi crittografiche per la protezione dei dati.
* **Data (DynamoDB)**: Database NoSQL per i metadati.



## 🛠️ Tech Stack
* **Infrastructure**: Terraform
* **Cloud Emulation**: LocalStack (Docker)
* **Security**: AWS KMS (Key Management Service)
* **Testing**: Python (Boto3)

## 🚀 Come testare l'infrastruttura
1. **Avvia l'ambiente**: `docker-compose up -d`
2. **Inizializza**: `terraform init`
3. **Applica**: `terraform apply -auto-approve`
4. **Verifica Crittografia**: Esegui `python scripts/vault_test.py` per testare l'upload criptato nel Vault.

## 📑 Note Tecniche
Ho risolto le limitazioni di rete locali su Windows configurando il provider AWS con `s3_use_path_style = true`, garantendo l'interoperabilità corretta con gli endpoint di LocalStack.
