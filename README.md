# 🛡️ Aegis-Zero: Hybrid Cloud Infrastructure-as-Code

<p align="center">
  <img src="https://img.shields.io/badge/Terraform-1.5+-623CE4?style=for-the-badge&logo=terraform&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/LocalStack-Pro--Grade-00C9FF?style=for-the-badge&logo=localstack&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

## 🎯 Strategic Rationale & Business Value
In un mercato dove i costi cloud e la protezione dei dati sensibili sono priorità assolute, **Aegis-Zero** dimostra come ingegnerizzare un'infrastruttura **Enterprise-Grade** con un approccio **Security-First** e **Zero-Cost**. 

Questo progetto implementa un caveau digitale (**S3 Vault**) protetto da crittografia hardware-based (**AWS KMS**), orchestrato interamente via Terraform e validato in un ambiente cloud ibrido locale per eliminare le spese di sviluppo e testing.

---

## 🏗️ Architettura & Flusso Logico

L'infrastruttura segue i principi del **AWS Well-Architected Framework**:

1.  **Provisioning (IaC)**: Utilizzo di moduli Terraform per la creazione atomica di VPC, S3 e KMS con policy "Least Privilege".
2.  **Encryption Pipeline**: Lo script di validazione simula un microservizio che richiede una *Data Key* a KMS per cifrare i dati prima dell'upload (SSE-KMS).
3.  **Audit & Persistence**: Tracking sistematico delle operazioni su DynamoDB per garantire la tracciabilità totale (Audit Log).
4.  **Local Emulation**: Stack AWS completo riprodotto via **LocalStack**, permettendo test d'integrazione a latenza zero.

---

## 💰 FinOps: Cost Breakdown
L'approccio "Shift-Left" di Aegis-Zero permette un risparmio immediato durante le fasi di Dev/Test.

| Servizio AWS | Costo Stimato (Mensile) | Costo Aegis-Zero | Risparmio |
| :--- | :--- | :--- | :--- |
| **KMS** (Key Management) | $5.00 + API calls | **$0.00** | 100% |
| **S3 Storage** (Standard) | $25.00+ | **$0.00** | 100% |
| **DynamoDB** (WCU/RCU) | $15.00+ | **$0.00** | 100% |
| **TOTALE** | **~$80.00 / mese** | **$0.00** | **~$960 / Anno** |

---

## 🛠️ Infrastructure Validation

### 1. Terraform Deployment Logs
Validazione della creazione delle risorse e coerenza degli stati tra i vari provider.

<img width="600" alt="terraform_apply" src="https://github.com/user-attachments/assets/b7927203-c09a-46b1-b1e8-23395187a1eb" />

### 2. Security Handshake (KMS + S3)
Prova tecnica di cifratura: il dato viene reso illeggibile senza l'autorizzazione crittografica corretta.

<img width="600" alt="vault_test" src="https://github.com/user-attachments/assets/3be3e108-17bb-4c54-8a24-3a83f4be16a3" />

### 3. Service Health Dashboard
Monitoraggio degli endpoint locali e dello stato operativo dei container.

<img width="800" alt="cloud_dashboard" src="https://github.com/user-attachments/assets/03551dce-c03e-436c-81fb-27793156d6d8" />

---

## 🚀 Come Replicare l'Ambiente

### 1. Prerequisiti
* Docker & Docker Compose
* Terraform (v1.5+)
* Python 3.10+ (libreria `boto3`)

### 2. Setup Cloud (Docker)
Avvia LocalStack per emulare l'ambiente AWS:
```bash
Setup Cloud
docker-compose up -d

Inizializza i plugin e i moduli necessari
terraform init

Crea le risorse AWS simulate (VPC, S3 Vault, KMS Key)
terraform apply -auto-approve

Esegue lo script dalla cartella dedicata
python scripts/vault_test.py

Distrugge le risorse gestite da Terraform
terraform destroy -auto-approve

Spegne i container Docker
docker-compose down
```
Aegis-Zero © 2026
