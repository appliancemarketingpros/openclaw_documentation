---
title: Azure
source_url: https://docs.openclaw.ai/uk/install/azure
scraped_at: 2026-05-25
---

Цей посібник налаштовує Linux VM Azure за допомогою Azure CLI, застосовує посилення Network Security Group (NSG), налаштовує Azure Bastion для доступу SSH і встановлює OpenClaw.

## Що ви зробите

  * Створите мережеві ресурси Azure (VNet, підмережі, NSG) та обчислювальні ресурси за допомогою Azure CLI
  * Застосуєте правила Network Security Group, щоб SSH до VM був дозволений лише з Azure Bastion
  * Використаєте Azure Bastion для доступу SSH (без публічної IP-адреси на VM)
  * Встановите OpenClaw за допомогою інсталяційного скрипта
  * Перевірите Gateway


## Що вам потрібно

  * Підписка Azure з дозволом створювати обчислювальні та мережеві ресурси
  * Установлений Azure CLI (за потреби див. [кроки встановлення Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>))
  * Пара ключів SSH (посібник описує, як згенерувати її за потреби)
  * ~20-30 хвилин


## Налаштування розгортання

* ### Sign in to Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

Розширення `ssh` потрібне для нативного тунелювання SSH через Azure Bastion.

* ### Register required resource providers (one-time)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Перевірте реєстрацію. Зачекайте, доки обидва покажуть `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Set deployment variables

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Налаштуйте імена та діапазони CIDR відповідно до вашого середовища. Підмережа Bastion має бути щонайменше `/26`.

* ### Select SSH key

Використайте наявний публічний ключ, якщо він у вас є:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Якщо у вас ще немає ключа SSH, згенеруйте його:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Select VM size and OS disk size

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Виберіть розмір VM і розмір диска ОС, доступні у вашій підписці та регіоні:

  * Почніть з меншого розміру для легкого використання й масштабуйте пізніше
  * Використовуйте більше vCPU/RAM/диска для інтенсивнішої автоматизації, більшої кількості каналів або більших навантажень моделей/інструментів
  * Якщо розмір VM недоступний у вашому регіоні або квоті підписки, виберіть найближчий доступний SKU


Перелічіть розміри VM, доступні у вашому цільовому регіоні:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Перевірте поточне використання та квоту vCPU і дисків:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Розгортання ресурсів Azure

* ### Create the resource group

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Create the network security group

Створіть NSG і додайте правила, щоб лише підмережа Bastion могла підключатися до VM через SSH.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Правила оцінюються за пріоритетом (спочатку найменше число): трафік Bastion дозволено з пріоритетом 100, а потім увесь інший SSH блокується з пріоритетами 110 і 120.

* ### Create the virtual network and subnets

Створіть VNet з підмережею VM (із підключеним NSG), а потім додайте підмережу Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Створіть VM

VM не має публічної IP-адреси. Доступ SSH здійснюється виключно через Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` запобігає призначенню публічної IP-адреси. `--nsg ""` пропускає створення NSG для окремого NIC (безпеку забезпечує NSG на рівні підмережі).

**Відтворюваність:** Наведена вище команда використовує `latest` для образу Ubuntu. Щоб закріпити конкретну версію, виведіть список доступних версій і замініть `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Створіть Azure Bastion

Azure Bastion забезпечує керований SSH-доступ до VM без відкриття публічної IP-адреси. Для CLI-команди `az network bastion ssh` потрібен SKU Standard із тунелюванням.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Підготовка Bastion зазвичай займає 5-10 хвилин, але в деяких регіонах може тривати до 15-30 хвилин.

## Установіть OpenClaw

* ### Увійдіть до VM через Azure Bastion за допомогою SSH

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Установіть OpenClaw (в оболонці VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

Інсталятор установлює Node LTS і залежності, якщо їх ще немає, установлює OpenClaw і запускає майстер початкового налаштування. Докладніше див. [Установлення](</uk/install>).

* ### Перевірте Gateway

Після завершення початкового налаштування:

bashCopy code
[code]
    openclaw gateway status
[/code]

Більшість корпоративних команд Azure вже мають ліцензії GitHub Copilot. Якщо це ваш випадок, рекомендуємо вибрати провайдера GitHub Copilot у майстрі початкового налаштування OpenClaw. Див. [провайдер GitHub Copilot](</uk/providers/github-copilot>).

## Міркування щодо вартості

Azure Bastion Standard SKU коштує приблизно **$140/місяць** , а VM (Standard_B2as_v2) коштує приблизно **$55/місяць**.

Щоб зменшити витрати:

  * **Звільняйте VM** коли вона не використовується (це зупиняє оплату обчислень; плата за диск залишається). OpenClaw Gateway буде недоступний, доки VM звільнено — перезапустіть її, коли вона знову потрібна в роботі:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Видаляйте Bastion, коли він не потрібен** , і створюйте його знову, коли потрібен SSH-доступ. Bastion є найбільшою складовою витрат, і його розгортання займає лише кілька хвилин.

  * **Використовуйте Basic Bastion SKU** (~$38/місяць), якщо вам потрібен лише SSH через Portal і не потрібне тунелювання CLI (`az network bastion ssh`).


## Очищення

Щоб видалити всі ресурси, створені за цим посібником:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Це видаляє групу ресурсів і все в ній (VM, VNet, NSG, Bastion, публічну IP-адресу).

## Наступні кроки

  * Налаштуйте канали обміну повідомленнями: [Канали](</uk/channels>)
  * Спарюйте локальні пристрої як вузли: [Вузли](</uk/nodes>)
  * Налаштуйте Gateway: [Конфігурація Gateway](</uk/gateway/configuration>)
  * Докладніше про розгортання OpenClaw в Azure з провайдером моделі GitHub Copilot: [OpenClaw в Azure з GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [GCP](</uk/install/gcp>)
  * [DigitalOcean](</uk/install/digitalocean>)


Was this useful?YesNo