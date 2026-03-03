#!/bin/bash
set -e
echo "🛡️  Inizializzazione Aegis-Zero..."
docker-compose up -d
sleep 5
k3d cluster create aegis-cluster -p "8080:80@loadbalancer" --wait || echo "Cluster già presente."
terraform init && terraform apply -auto-approve
kubectl apply -f k8s/app-deploy.yaml
echo "✅ Sistema pronto su http://localhost:8080"