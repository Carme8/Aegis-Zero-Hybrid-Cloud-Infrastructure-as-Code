module "network" {
  source = "./modules/network"
}

module "data" {
  source = "./modules/data"
}

module "storage" {
  source      = "./modules/storage"
  bucket_name = "ai-vault-ghost-infra"
}

module "security" {
  source = "./modules/security"
}