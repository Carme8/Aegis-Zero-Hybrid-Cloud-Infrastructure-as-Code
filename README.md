# 🛡️ Aegis-Zero: Hybrid Cloud Infrastructure-as-Code
<p align="center">
  <img src="https://img.shields.io/badge/Terraform-1.5+-623CE4?style=for-the-badge&logo=terraform&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/LocalStack-Pro--Grade-00C9FF?style=for-the-badge&logo=docker&logoColor=white" />
</p>

## 🎯 Perché questo progetto? (The Vision)
In un panorama dove i costi cloud fuori controllo e la sicurezza dei dati sono le sfide n.1 per i CTO, **Aegis-Zero** dimostra come ingegnerizzare un'infrastruttura **Enterprise-Grade** con un approccio "Security-First" e "Zero-Cost".

Il progetto implementa un caveau digitale (S3 Vault) protetto da chiavi crittografiche asimmetriche (KMS), testato interamente in un ambiente cloud ibrido locale per eliminare le spese di sviluppo.

---

## 💰 Cost Breakdown: Il Linguaggio dei Manager
Perché un'azienda dovrebbe adottare questo approccio? Ecco il confronto tra lo sviluppo tradizionale su AWS e l'approccio Aegis-Zero:

| Servizio AWS | Costo Stimato (Dev/Test Mensile) | Costo Aegis-Zero | Risparmio |
| :--- | :--- | :--- | :--- |
| **KMS** (Key Management) | $5.00 + API calls | **$0.00** | 100% |
| **S3 Storage** (Standard) | $20.00 - $50.00 | **$0.00** | 100% |
| **DynamoDB** (Provisioned) | $15.00+ | **$0.00** | 100% |
| **Data Transfer** | Variabile | **$0.00** | 100% |
| **TOTALE** | **~$80.00 / mese** | **$0.00** | **$960 / Anno** |

---

## 🏗️ Architettura del Sistema
L'infrastruttura è modulare, scalabile e pronta per il "Lift & Shift" verso la produzione reale.



* **Network Layer**: VPC isolata con subnet dedicate (simulata).
* **Security Layer**: Chiavi KMS personalizzate con policy di rotazione (simulata).
* **Storage Layer**: S3 Bucket con crittografia *Server-Side* forzata.
* **Compute Simulation**: Script Python (Boto3) che agisce come un microservizio per validare il flusso dei dati.

---

## 🛠️ Infrastructure Validation & Deployment Logs

#### 1. Infrastructure Deployment Terraform ![Terraform](https://img.shields.io/badge/Terraform-1.5+-623CE4?style=for-the-badge&logo=terraform&logoColor=white)

<img width="625" height="913" alt="infrastructure_apply png" src="https://github.com/user-attachments/assets/b7927203-c09a-46b1-b1e8-23395187a1eb" />

#### 2. Security & Encryption Validation

<img width="701" height="131" alt="vault_encryption_test" src="https://github.com/user-attachments/assets/3be3e108-17bb-4c54-8a24-3a83f4be16a3" />

#### 3. Cloud Services Status LocalStack ![LocalStack](https://img.shields.io/badge/LocalStack-Pro--Grade-00C9FF?style=for-the-badge&logo=docker&logoColor=white)

<img width="1919" height="1031" alt="cloud_dashboard" src="https://github.com/user-attachments/assets/03551dce-c03e-436c-81fb-27793156d6d8" />


#### 4. S3 Vault & Docker Orchestration ![LocalStack](https://img.shields.io/badge/LocalStack-Pro--Grade-00C9FF?style=for-the-badge&logo=docker&logoColor=white)  ![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<img width="1919" height="381" alt="s3_bucket_detail" src="https://github.com/user-attachments/assets/a1832805-f9a7-4611-80a8-950208244028" />

<img width="1918" height="1029" alt="docker_orchestration" src="https://github.com/user-attachments/assets/a071a709-ea81-455f-8201-35f8c47c256c" />

---

## 🚀 Come Replicare l'Ambiente

Segui questa procedura guidata per distribuire l'intera infrastruttura **Aegis-Zero** sul tuo sistema locale in meno di 2 minuti.

### 1. Prerequisiti
Assicurati di avere installato:
* **Docker & Docker Compose**
* **Terraform** (v1.5+)
* **Python 3.10+** (con libreria `boto3`)

### 2. Setup dell'Ambiente Cloud (Docker)
Avvia il container **Aegis_Cloud** (basato su LocalStack). Questo comando prepara gli endpoint AWS emulati (S3, KMS, DynamoDB) all'interno di un network isolato.
```bash
docker-compose up -d


Inizializza i plugin e i moduli necessari
terraform init

Crea le risorse AWS simulate (VPC, S3 Vault, KMS Key)
terraform apply -auto-approve

Validazione del Vault (Python)
python scripts/vault_test.py

Per spegnere l'ambiente
docker-compose down
