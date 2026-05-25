---
title: Azure
source_url: https://docs.openclaw.ai/fr/install/azure
scraped_at: 2026-05-25
---

Ce guide configure une VM Linux Azure avec l’Azure CLI, applique un durcissement du groupe de sécurité réseau (NSG), configure Azure Bastion pour l’accès SSH et installe OpenClaw.

## Ce que vous allez faire

  * Créer les ressources réseau Azure (VNet, sous-réseaux, NSG) et de calcul avec l’Azure CLI
  * Appliquer des règles de groupe de sécurité réseau afin que le SSH de la VM ne soit autorisé que depuis Azure Bastion
  * Utiliser Azure Bastion pour l’accès SSH (aucune IP publique sur la VM)
  * Installer OpenClaw avec le script d’installation
  * Vérifier le Gateway


## Ce qu’il vous faut

  * Un abonnement Azure avec l’autorisation de créer des ressources de calcul et réseau
  * Azure CLI installé (voir les [étapes d’installation d’Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>) si nécessaire)
  * Une paire de clés SSH (le guide explique comment en générer une si nécessaire)
  * ~20 à 30 minutes


## Configurer le déploiement

* ### Se connecter à Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

L’extension `ssh` est requise pour le tunneling SSH natif d’Azure Bastion.

* ### Enregistrer les fournisseurs de ressources requis (une seule fois)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Vérifiez l’enregistrement. Attendez que les deux affichent `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Définir les variables de déploiement

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Ajustez les noms et plages CIDR à votre environnement. Le sous-réseau Bastion doit être au minimum en `/26`.

* ### Sélectionner la clé SSH

Utilisez votre clé publique existante si vous en avez une :

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Si vous n’avez pas encore de clé SSH, générez-en une :

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Sélectionner la taille de VM et la taille du disque du système d’exploitation

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Choisissez une taille de VM et une taille de disque du système d’exploitation disponibles dans votre abonnement et votre région :

  * Commencez plus petit pour une utilisation légère, puis augmentez l’échelle plus tard
  * Utilisez davantage de vCPU/RAM/disque pour une automatisation plus lourde, plus de canaux ou des charges de travail de modèles/outils plus importantes
  * Si une taille de VM n’est pas disponible dans votre région ou dans le quota de votre abonnement, choisissez la référence SKU disponible la plus proche


Listez les tailles de VM disponibles dans votre région cible :

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Vérifiez votre utilisation/quota actuel de vCPU et de disque :

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Déployer les ressources Azure

* ### Créer le groupe de ressources

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Créer le groupe de sécurité réseau

Créez le NSG et ajoutez des règles afin que seul le sous-réseau Bastion puisse se connecter en SSH à la VM.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Les règles sont évaluées par priorité (le plus petit nombre en premier) : le trafic Bastion est autorisé à 100, puis tout autre SSH est bloqué à 110 et 120.

* ### Créer le réseau virtuel et les sous-réseaux

Créez le VNet avec le sous-réseau de la VM (NSG attaché), puis ajoutez le sous-réseau Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Créer la VM

La VM n’a pas d’IP publique. L’accès SSH se fait exclusivement via Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` empêche l’attribution d’une IP publique. `--nsg ""` évite de créer un NSG par carte réseau (le NSG au niveau du sous-réseau gère la sécurité).

**Reproductibilité :** La commande ci-dessus utilise `latest` pour l’image Ubuntu. Pour épingler une version spécifique, listez les versions disponibles et remplacez `latest` :

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Créer Azure Bastion

Azure Bastion fournit un accès SSH géré à la VM sans exposer d’IP publique. La référence SKU Standard avec tunneling est requise pour `az network bastion ssh` basé sur la CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Le provisionnement de Bastion prend généralement 5 à 10 minutes, mais peut prendre jusqu’à 15 à 30 minutes dans certaines régions.

## Installer OpenClaw

* ### Se connecter en SSH à la VM via Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Installer OpenClaw (dans le shell de la VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

L’installateur installe Node LTS et les dépendances si elles ne sont pas déjà présentes, installe OpenClaw et lance l’assistant d’intégration. Consultez [Installer](</fr/install>) pour plus de détails.

* ### Vérifier le Gateway

Une fois l’intégration terminée :

bashCopy code
[code]
    openclaw gateway status
[/code]

La plupart des équipes Azure en entreprise disposent déjà de licences GitHub Copilot. Si c’est votre cas, nous recommandons de choisir le fournisseur GitHub Copilot dans l’assistant d’intégration d’OpenClaw. Consultez [Fournisseur GitHub Copilot](</fr/providers/github-copilot>).

## Considérations de coût

La référence SKU Azure Bastion Standard coûte environ **140 $US/mois** et la VM (Standard_B2as_v2) coûte environ **55 $US/mois**.

Pour réduire les coûts :

  * **Désallouez la VM** lorsqu’elle n’est pas utilisée (cela arrête la facturation du calcul ; les frais de disque restent applicables). Le Gateway OpenClaw ne sera pas joignable pendant que la VM est désallouée — redémarrez-la lorsque vous devez de nouveau la rendre active :

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Supprimez Bastion lorsqu’il n’est pas nécessaire** et recréez-le lorsque vous avez besoin de l’accès SSH. Bastion est le composant le plus coûteux et son provisionnement ne prend que quelques minutes.

  * **Utilisez la référence SKU Bastion Basic** (~38 $US/mois) si vous avez seulement besoin d’un SSH basé sur le portail et n’avez pas besoin du tunneling CLI (`az network bastion ssh`).


## Nettoyage

Pour supprimer toutes les ressources créées par ce guide :

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Cela supprime le groupe de ressources et tout ce qu’il contient (VM, VNet, NSG, Bastion, IP publique).

## Étapes suivantes

  * Configurer les canaux de messagerie : [Canaux](</fr/channels>)
  * Associer des appareils locaux comme nœuds : [Nœuds](</fr/nodes>)
  * Configurer le Gateway : [Configuration du Gateway](</fr/gateway/configuration>)
  * Pour plus de détails sur le déploiement d’OpenClaw Azure avec le fournisseur de modèles GitHub Copilot : [OpenClaw sur Azure avec GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [GCP](</fr/install/gcp>)
  * [DigitalOcean](</fr/install/digitalocean>)


Was this useful?YesNo