---
title: Azure
source_url: https://docs.openclaw.ai/nl/install/azure
scraped_at: 2026-05-25
---

Deze gids stelt een Azure Linux-VM in met de Azure CLI, past verharding van Network Security Group (NSG) toe, configureert Azure Bastion voor SSH-toegang en installeert OpenClaw.

## Wat je gaat doen

  * Azure-netwerken (VNet, subnetten, NSG) en compute-resources maken met de Azure CLI
  * Network Security Group-regels toepassen zodat VM-SSH alleen is toegestaan vanaf Azure Bastion
  * Azure Bastion gebruiken voor SSH-toegang (geen openbaar IP-adres op de VM)
  * OpenClaw installeren met het installatiescript
  * De Gateway verifiëren


## Wat je nodig hebt

  * Een Azure-abonnement met toestemming om compute- en netwerkresources te maken
  * Azure CLI geïnstalleerd (zie indien nodig [installatiestappen voor Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>))
  * Een SSH-sleutelpaar (de gids behandelt hoe je er zo nodig een genereert)
  * ~20-30 minuten


## Implementatie configureren

* ### Aanmelden bij Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

De `ssh`-extensie is vereist voor native SSH-tunneling via Azure Bastion.

* ### Vereiste resourceproviders registreren (eenmalig)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Controleer de registratie. Wacht tot beide `Registered` tonen.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Implementatievariabelen instellen

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Pas namen en CIDR-bereiken aan je omgeving aan. Het Bastion-subnet moet minimaal `/26` zijn.

* ### SSH-sleutel selecteren

Gebruik je bestaande openbare sleutel als je er een hebt:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Als je nog geen SSH-sleutel hebt, genereer er dan een:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### VM-grootte en grootte van de OS-schijf selecteren

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Kies een VM-grootte en OS-schijfgrootte die beschikbaar zijn in je abonnement en regio:

  * Begin kleiner voor licht gebruik en schaal later op
  * Gebruik meer vCPU/RAM/schijf voor zwaardere automatisering, meer kanalen of grotere model-/toolworkloads
  * Als een VM-grootte niet beschikbaar is in je regio of abonnementsquotum, kies dan de dichtstbijzijnde beschikbare SKU


Toon VM-groottes die beschikbaar zijn in je doelregio:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Controleer je huidige vCPU- en schijfgebruik/quotum:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Azure-resources implementeren

* ### De resourcegroep maken

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### De network security group maken

Maak de NSG en voeg regels toe zodat alleen het Bastion-subnet via SSH verbinding kan maken met de VM.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

De regels worden geëvalueerd op prioriteit (laagste nummer eerst): Bastion-verkeer wordt toegestaan op 100, daarna wordt alle andere SSH geblokkeerd op 110 en 120.

* ### Het virtuele netwerk en de subnetten maken

Maak het VNet met het VM-subnet (NSG gekoppeld) en voeg daarna het Bastion-subnet toe.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### De VM maken

De VM heeft geen openbaar IP-adres. SSH-toegang verloopt uitsluitend via Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` voorkomt dat er een openbaar IP-adres wordt toegewezen. `--nsg ""` slaat het maken van een NSG per NIC over (de NSG op subnetniveau regelt de beveiliging).

**Reproduceerbaarheid:** De bovenstaande opdracht gebruikt `latest` voor de Ubuntu-image. Om een specifieke versie vast te pinnen, toon je beschikbare versies en vervang je `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Azure Bastion maken

Azure Bastion biedt beheerde SSH-toegang tot de VM zonder een openbaar IP-adres bloot te stellen. Standard SKU met tunneling is vereist voor CLI-gebaseerde `az network bastion ssh`.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Het inrichten van Bastion duurt doorgaans 5-10 minuten, maar kan in sommige regio's tot 15-30 minuten duren.

## OpenClaw installeren

* ### Via Azure Bastion met SSH verbinden met de VM

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### OpenClaw installeren (in de VM-shell)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

Het installatieprogramma installeert Node LTS en afhankelijkheden als die nog niet aanwezig zijn, installeert OpenClaw en start de onboardingwizard. Zie [Installeren](</nl/install>) voor details.

* ### De Gateway verifiëren

Nadat onboarding is voltooid:

bashCopy code
[code]
    openclaw gateway status
[/code]

De meeste Azure-teams in ondernemingen hebben al GitHub Copilot-licenties. Als dat voor jou geldt, raden we aan de GitHub Copilot-provider te kiezen in de OpenClaw-onboardingwizard. Zie [GitHub Copilot-provider](</nl/providers/github-copilot>).

## Kostenoverwegingen

Azure Bastion Standard SKU kost ongeveer **$140/maand** en de VM (Standard_B2as_v2) kost ongeveer **$55/maand**.

Om kosten te verlagen:

  * **Deallocate de VM** wanneer die niet in gebruik is (stopt compute-facturering; schijfkosten blijven bestaan). De OpenClaw Gateway is niet bereikbaar terwijl de VM is gedealloceerd — start deze opnieuw wanneer je hem weer live nodig hebt:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Verwijder Bastion wanneer dit niet nodig is** en maak het opnieuw wanneer je SSH-toegang nodig hebt. Bastion is de grootste kostencomponent en het inrichten duurt slechts enkele minuten.

  * **Gebruik de Basic Bastion SKU** (~$38/maand) als je alleen Portal-gebaseerde SSH nodig hebt en geen CLI-tunneling (`az network bastion ssh`) vereist.


## Opschonen

Om alle resources te verwijderen die door deze gids zijn gemaakt:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Dit verwijdert de resourcegroep en alles daarin (VM, VNet, NSG, Bastion, openbaar IP-adres).

## Volgende stappen

  * Stel berichtkanalen in: [Kanalen](</nl/channels>)
  * Koppel lokale apparaten als Nodes: [Nodes](</nl/nodes>)
  * Configureer de Gateway: [Gateway-configuratie](</nl/gateway/configuration>)
  * Voor meer details over OpenClaw Azure-implementatie met de GitHub Copilot-modelprovider: [OpenClaw op Azure met GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [GCP](</nl/install/gcp>)
  * [DigitalOcean](</nl/install/digitalocean>)


Was this useful?YesNo