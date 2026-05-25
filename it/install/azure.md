---
title: Azure
source_url: https://docs.openclaw.ai/it/install/azure
scraped_at: 2026-05-25
---

Questa guida configura una VM Linux di Azure con Azure CLI, applica l'irrobustimento del Network Security Group (NSG), configura Azure Bastion per l'accesso SSH e installa OpenClaw.

## Cosa farai

  * Creare risorse di rete Azure (VNet, subnet, NSG) e risorse di calcolo con Azure CLI
  * Applicare regole del Network Security Group affinché l'SSH della VM sia consentito solo da Azure Bastion
  * Usare Azure Bastion per l'accesso SSH (nessun IP pubblico sulla VM)
  * Installare OpenClaw con lo script di installazione
  * Verificare il Gateway


## Cosa ti serve

  * Una sottoscrizione Azure con autorizzazione a creare risorse di calcolo e di rete
  * Azure CLI installata (vedi [passaggi di installazione di Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>) se necessario)
  * Una coppia di chiavi SSH (la guida spiega come generarne una se necessario)
  * ~20-30 minuti


## Configurare il deployment

* ### Accedi ad Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

L'estensione `ssh` è necessaria per il tunneling SSH nativo di Azure Bastion.

* ### Registra i provider di risorse necessari (una tantum)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Verifica la registrazione. Attendi finché entrambi mostrano `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Imposta le variabili di deployment

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Adatta nomi e intervalli CIDR al tuo ambiente. La subnet Bastion deve essere almeno `/26`.

* ### Seleziona la chiave SSH

Usa la tua chiave pubblica esistente, se ne hai una:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Se non hai ancora una chiave SSH, generane una:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Seleziona le dimensioni della VM e la dimensione del disco del sistema operativo

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Scegli una dimensione della VM e una dimensione del disco del sistema operativo disponibili nella tua sottoscrizione e area:

  * Inizia con dimensioni più piccole per un utilizzo leggero e aumenta in seguito
  * Usa più vCPU/RAM/disco per automazioni più pesanti, più canali o carichi di lavoro di modelli/strumenti più grandi
  * Se una dimensione della VM non è disponibile nella tua area o nella quota della sottoscrizione, scegli lo SKU disponibile più vicino


Elenca le dimensioni delle VM disponibili nell'area di destinazione:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Controlla l'utilizzo e la quota correnti di vCPU e disco:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Distribuire le risorse Azure

* ### Crea il gruppo di risorse

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Crea il gruppo di sicurezza di rete

Crea l'NSG e aggiungi regole in modo che solo la subnet Bastion possa accedere alla VM via SSH.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Le regole vengono valutate in base alla priorità (prima il numero più basso): il traffico Bastion è consentito a 100, quindi tutto l'altro SSH viene bloccato a 110 e 120.

* ### Crea la rete virtuale e le subnet

Crea la VNet con la subnet della VM (NSG collegato), quindi aggiungi la subnet Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Crea la VM

La VM non ha IP pubblico. L'accesso SSH avviene esclusivamente tramite Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` impedisce l'assegnazione di un IP pubblico. `--nsg ""` evita la creazione di un NSG per NIC (la sicurezza è gestita dall'NSG a livello di subnet).

**Riproducibilità:** il comando sopra usa `latest` per l'immagine Ubuntu. Per fissare una versione specifica, elenca le versioni disponibili e sostituisci `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Crea Azure Bastion

Azure Bastion fornisce accesso SSH gestito alla VM senza esporre un IP pubblico. Lo SKU Standard con tunneling è necessario per `az network bastion ssh` basato su CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Il provisioning di Bastion richiede in genere 5-10 minuti, ma in alcune aree può richiedere fino a 15-30 minuti.

## Installare OpenClaw

* ### Accedi alla VM via SSH tramite Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Installa OpenClaw (nella shell della VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

Il programma di installazione installa Node LTS e le dipendenze se non sono già presenti, installa OpenClaw e avvia la procedura guidata di onboarding. Vedi [Installazione](</it/install>) per i dettagli.

* ### Verifica il Gateway

Al termine dell'onboarding:

bashCopy code
[code]
    openclaw gateway status
[/code]

La maggior parte dei team Azure aziendali dispone già di licenze GitHub Copilot. Se questo è il tuo caso, consigliamo di scegliere il provider GitHub Copilot nella procedura guidata di onboarding di OpenClaw. Vedi [provider GitHub Copilot](</it/providers/github-copilot>).

## Considerazioni sui costi

Lo SKU Standard di Azure Bastion costa circa **$140/mese** e la VM (Standard_B2as_v2) costa circa **$55/mese**.

Per ridurre i costi:

  * **Dealloca la VM** quando non è in uso (interrompe la fatturazione del calcolo; i costi del disco restano). Il Gateway OpenClaw non sarà raggiungibile mentre la VM è deallocata: riavviala quando devi renderla nuovamente attiva:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Elimina Bastion quando non serve** e ricrealo quando hai bisogno dell'accesso SSH. Bastion è la componente di costo maggiore e richiede solo pochi minuti per il provisioning.

  * **Usa lo SKU Basic di Bastion** (~$38/mese) se ti serve solo l'SSH basato sul Portale e non hai bisogno del tunneling CLI (`az network bastion ssh`).


## Pulizia

Per eliminare tutte le risorse create da questa guida:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Questo rimuove il gruppo di risorse e tutto ciò che contiene (VM, VNet, NSG, Bastion, IP pubblico).

## Passaggi successivi

  * Configura i canali di messaggistica: [Canali](</it/channels>)
  * Associa i dispositivi locali come nodi: [Nodi](</it/nodes>)
  * Configura il Gateway: [configurazione del Gateway](</it/gateway/configuration>)
  * Per maggiori dettagli sul deployment di OpenClaw in Azure con il provider di modelli GitHub Copilot: [OpenClaw su Azure con GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [GCP](</it/install/gcp>)
  * [DigitalOcean](</it/install/digitalocean>)


Was this useful?YesNo