---
title: Azure
source_url: https://docs.openclaw.ai/zh-TW/install/azure
scraped_at: 2026-05-25
---

本指南會使用 Azure CLI 設定 Azure Linux VM、套用 Network Security Group (NSG) 強化、設定 Azure Bastion 以便 SSH 存取，並安裝 OpenClaw。

## 你將執行的事項

  * 使用 Azure CLI 建立 Azure 網路（VNet、子網路、NSG）與運算資源
  * 套用 Network Security Group 規則，讓 VM SSH 只允許從 Azure Bastion 存取
  * 使用 Azure Bastion 進行 SSH 存取（VM 不使用公用 IP）
  * 使用安裝程式指令碼安裝 OpenClaw
  * 驗證 Gateway


## 你需要準備的項目

  * 具備建立運算與網路資源權限的 Azure 訂閱
  * 已安裝 Azure CLI（如有需要，請參閱 [Azure CLI 安裝步驟](<https://learn.microsoft.com/cli/azure/install-azure-cli>)）
  * SSH 金鑰組（本指南會涵蓋在需要時產生金鑰）
  * 約 20-30 分鐘


## 設定部署

* ### 登入 Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

Azure Bastion 原生 SSH 通道需要 `ssh` 擴充功能。

* ### 註冊必要的資源提供者（一次性）

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

驗證註冊狀態。等待兩者都顯示 `Registered`。

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### 設定部署變數

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

請調整名稱與 CIDR 範圍，以符合你的環境。Bastion 子網路至少必須是 `/26`。

* ### 選取 SSH 金鑰

如果你已有公開金鑰，請使用現有公開金鑰：

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

如果你還沒有 SSH 金鑰，請產生一組：

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### 選取 VM 大小與 OS 磁碟大小

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

選擇你的訂閱與區域中可用的 VM 大小與 OS 磁碟大小：

  * 輕量使用可先從較小規格開始，之後再擴充
  * 如需較重的自動化、更多通道，或較大的模型/工具工作負載，請使用更多 vCPU/RAM/磁碟
  * 如果你的區域或訂閱配額無法使用某個 VM 大小，請選擇最接近的可用 SKU


列出目標區域中可用的 VM 大小：

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

檢查目前的 vCPU 與磁碟使用量/配額：

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## 部署 Azure 資源

* ### 建立資源群組

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### 建立 Network Security Group

建立 NSG 並新增規則，讓只有 Bastion 子網路可以透過 SSH 連入 VM。

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

規則會依優先順序評估（數字越小越先）：Bastion 流量在 100 被允許，接著所有其他 SSH 會在 110 與 120 被封鎖。

* ### 建立虛擬網路與子網路

使用 VM 子網路（已附加 NSG）建立 VNet，然後新增 Bastion 子網路。

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### 建立 VM

VM 沒有公用 IP。SSH 存取完全透過 Azure Bastion 進行。

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` 可防止指派公用 IP。`--nsg ""` 會略過建立每張 NIC 專用的 NSG（由子網路層級的 NSG 處理安全性）。

**可重現性：** 上方命令使用 `latest` 作為 Ubuntu 映像。若要釘選特定版本，請列出可用版本並取代 `latest`：

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### 建立 Azure Bastion

Azure Bastion 提供受控 SSH 存取，無需將 VM 暴露在公用 IP 上。使用 CLI 型 `az network bastion ssh` 時，需要支援通道的 Standard SKU。

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Bastion 佈建通常需要 5-10 分鐘，但在某些區域可能需要最多 15-30 分鐘。

## 安裝 OpenClaw

* ### 透過 Azure Bastion SSH 連入 VM

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### 安裝 OpenClaw（在 VM shell 中）

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

安裝程式會安裝 Node LTS 與相依套件（如果尚未存在）、安裝 OpenClaw，並啟動上線精靈。詳情請參閱 [安裝](</zh-TW/install>)。

* ### 驗證 Gateway

上線完成後：

bashCopy code
[code]
    openclaw gateway status
[/code]

多數企業 Azure 團隊已經擁有 GitHub Copilot 授權。如果你也是這種情況，建議在 OpenClaw 上線精靈中選擇 GitHub Copilot 提供者。請參閱 [GitHub Copilot 提供者](</zh-TW/providers/github-copilot>)。

## 成本考量

Azure Bastion Standard SKU 約為 **$140/月** ，VM (Standard_B2as_v2) 約為 **$55/月** 。

若要降低成本：

  * **不使用時解除配置 VM** （停止運算計費；磁碟費用仍會保留）。VM 解除配置期間將無法連線到 OpenClaw Gateway — 需要再次上線時請重新啟動：

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **不需要時刪除 Bastion** ，並在需要 SSH 存取時重新建立。Bastion 是最大的成本項目，而且只需要幾分鐘即可佈建。

  * 如果你只需要透過 Portal 使用 SSH，且不需要 CLI 通道 (`az network bastion ssh`)，請**使用 Basic Bastion SKU** （約 $38/月）。


## 清理

若要刪除本指南建立的所有資源：

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

這會移除資源群組及其中所有內容（VM、VNet、NSG、Bastion、公用 IP）。

## 後續步驟

  * 設定訊息通道：[通道](</zh-TW/channels>)
  * 將本機裝置配對為 Node：[Node](</zh-TW/nodes>)
  * 設定 Gateway：[Gateway 設定](</zh-TW/gateway/configuration>)
  * 如需更多關於使用 GitHub Copilot 模型提供者在 Azure 上部署 OpenClaw 的詳細資訊：[Azure 上搭配 GitHub Copilot 的 OpenClaw](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## 相關

  * [安裝概觀](</zh-TW/install>)
  * [GCP](</zh-TW/install/gcp>)
  * [DigitalOcean](</zh-TW/install/digitalocean>)


Was this useful?YesNo