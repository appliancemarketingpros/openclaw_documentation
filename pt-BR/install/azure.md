---
title: Azure
source_url: https://docs.openclaw.ai/pt-BR/install/azure
scraped_at: 2026-05-25
---

Este guia configura uma VM Linux do Azure com a Azure CLI, aplica endurecimento de Network Security Group (NSG), configura o Azure Bastion para acesso SSH e instala o OpenClaw.

## O que você fará

  * Criar recursos de rede do Azure (VNet, sub-redes, NSG) e de computação com a Azure CLI
  * Aplicar regras de Network Security Group para que SSH na VM seja permitido apenas a partir do Azure Bastion
  * Usar o Azure Bastion para acesso SSH (sem IP público na VM)
  * Instalar o OpenClaw com o script de instalação
  * Verificar o Gateway


## O que você precisa

  * Uma assinatura do Azure com permissão para criar recursos de computação e rede
  * Azure CLI instalada (veja [etapas de instalação da Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>), se necessário)
  * Um par de chaves SSH (o guia aborda como gerar um, se necessário)
  * ~20-30 minutos


## Configurar a implantação

* ### Entrar na Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

A extensão `ssh` é necessária para tunelamento SSH nativo do Azure Bastion.

* ### Registrar os provedores de recursos necessários (uma vez)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Verifique o registro. Aguarde até que ambos mostrem `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Definir variáveis de implantação

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Ajuste nomes e intervalos CIDR para se adequarem ao seu ambiente. A sub-rede do Bastion deve ser pelo menos `/26`.

* ### Selecionar chave SSH

Use sua chave pública existente se você tiver uma:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Se você ainda não tem uma chave SSH, gere uma:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Selecionar tamanho da VM e tamanho do disco do SO

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Escolha um tamanho de VM e de disco do SO disponíveis em sua assinatura e região:

  * Comece menor para uso leve e aumente a escala depois
  * Use mais vCPU/RAM/disco para automações mais pesadas, mais canais ou cargas maiores de modelos/ferramentas
  * Se um tamanho de VM não estiver disponível em sua região ou cota da assinatura, escolha o SKU disponível mais próximo


Liste os tamanhos de VM disponíveis na sua região de destino:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Verifique seu uso/cota atual de vCPU e disco:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Implantar recursos do Azure

* ### Criar o grupo de recursos

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Criar o network security group

Crie o NSG e adicione regras para que apenas a sub-rede do Bastion possa fazer SSH na VM.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

As regras são avaliadas por prioridade (menor número primeiro): o tráfego do Bastion é permitido em 100, então todo o outro SSH é bloqueado em 110 e 120.

* ### Criar a rede virtual e as sub-redes

Crie a VNet com a sub-rede da VM (NSG anexado) e então adicione a sub-rede do Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Criar a VM

A VM não tem IP público. O acesso SSH é exclusivamente pelo Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` impede que um IP público seja atribuído. `--nsg ""` ignora a criação de um NSG por NIC (o NSG no nível da sub-rede cuida da segurança).

**Reprodutibilidade:** O comando acima usa `latest` para a imagem do Ubuntu. Para fixar uma versão específica, liste as versões disponíveis e substitua `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Criar o Azure Bastion

O Azure Bastion fornece acesso SSH gerenciado à VM sem expor um IP público. O SKU Standard com tunelamento é necessário para `az network bastion ssh` baseado na CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

O provisionamento do Bastion normalmente leva 5-10 minutos, mas pode levar até 15-30 minutos em algumas regiões.

## Instalar o OpenClaw

* ### Fazer SSH na VM pelo Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Instalar o OpenClaw (no shell da VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

O instalador instala o Node LTS e dependências se ainda não estiverem presentes, instala o OpenClaw e inicia o assistente de integração. Veja [Instalar](</pt-BR/install>) para detalhes.

* ### Verificar o Gateway

Depois que a integração for concluída:

bashCopy code
[code]
    openclaw gateway status
[/code]

A maioria das equipes empresariais do Azure já tem licenças do GitHub Copilot. Se esse for o seu caso, recomendamos escolher o provedor GitHub Copilot no assistente de integração do OpenClaw. Veja [provedor GitHub Copilot](</pt-BR/providers/github-copilot>).

## Considerações de custo

O SKU Azure Bastion Standard custa aproximadamente **$140/mês** e a VM (Standard_B2as_v2) custa aproximadamente **$55/mês**.

Para reduzir custos:

  * **Desaloque a VM** quando não estiver em uso (interrompe a cobrança de computação; as cobranças de disco permanecem). O OpenClaw Gateway não ficará acessível enquanto a VM estiver desalocada — reinicie-a quando precisar dela ativa novamente:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Exclua o Bastion quando não for necessário** e recrie-o quando precisar de acesso SSH. O Bastion é o maior componente de custo e leva apenas alguns minutos para ser provisionado.

  * **Use o SKU Basic Bastion** (~$38/mês) se você só precisar de SSH baseado no Portal e não exigir tunelamento pela CLI (`az network bastion ssh`).


## Limpeza

Para excluir todos os recursos criados por este guia:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Isso remove o grupo de recursos e tudo dentro dele (VM, VNet, NSG, Bastion, IP público).

## Próximos passos

  * Configure canais de mensagens: [Canais](</pt-BR/channels>)
  * Emparelhe dispositivos locais como Nodes: [Nodes](</pt-BR/nodes>)
  * Configure o Gateway: [Configuração do Gateway](</pt-BR/gateway/configuration>)
  * Para mais detalhes sobre a implantação do OpenClaw no Azure com o provedor de modelos GitHub Copilot: [OpenClaw no Azure com GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [GCP](</pt-BR/install/gcp>)
  * [DigitalOcean](</pt-BR/install/digitalocean>)


Was this useful?YesNo