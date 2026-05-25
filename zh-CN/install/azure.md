---
title: Azure
source_url: https://docs.openclaw.ai/zh-CN/install/azure
scraped_at: 2026-05-25
---

本指南将使用 Azure CLI 设置 Azure Linux VM，应用网络安全组 (NSG) 加固，配置 Azure Bastion 以进行 SSH 访问，并安装 OpenClaw。

## 你将完成

  * 使用 Azure CLI 创建 Azure 网络（VNet、子网、NSG）和计算资源
  * 应用网络安全组规则，使 VM SSH 仅允许来自 Azure Bastion
  * 使用 Azure Bastion 进行 SSH 访问（VM 上没有公共 IP）
  * 使用安装脚本安装 OpenClaw
  * 验证 Gateway 网关


## 你需要准备

  * 一个有权限创建计算和网络资源的 Azure 订阅
  * 已安装 Azure CLI（如有需要，请参阅 [Azure CLI 安装步骤](<https://learn.microsoft.com/cli/azure/install-azure-cli>)）
  * 一对 SSH 密钥（本指南会介绍如何生成）
  * 约 20-30 分钟


## 配置部署

* ### 登录 Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

`ssh` 扩展是 Azure Bastion 原生 SSH 隧道所必需的。

* ### 注册所需的资源提供程序（一次性）

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

验证注册状态。等待两者都显示 `Registered`。

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### 设置部署变量

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

调整名称和 CIDR 范围以适配你的环境。Bastion 子网必须至少为 `/26`。

* ### 选择 SSH 密钥

如果你已有公钥，请使用现有公钥：

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

如果你还没有 SSH 密钥，请生成一个：

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### 选择 VM 大小和 OS 磁盘大小

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

选择你的订阅和区域中可用的 VM 大小和 OS 磁盘大小：

  * 轻量使用时从较小规格开始，之后再扩容
  * 对于更重的自动化、更多渠道或更大的模型/工具工作负载，使用更多 vCPU/RAM/磁盘
  * 如果某个 VM 大小在你的区域或订阅配额中不可用，请选择最接近的可用 SKU


列出目标区域中可用的 VM 大小：

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

检查你当前的 vCPU 和磁盘使用量/配额：

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## 部署 Azure 资源

* ### 创建资源组

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### 创建网络安全组

创建 NSG 并添加规则，使只有 Bastion 子网可以通过 SSH 连接到 VM。

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

规则按优先级评估（数字越小越先执行）：Bastion 流量在 100 处被允许，随后所有其他 SSH 在 110 和 120 处被阻止。

* ### 创建虚拟网络和子网

使用 VM 子网（已附加 NSG）创建 VNet，然后添加 Bastion 子网。

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### 创建 VM

该 VM 没有公共 IP。SSH 访问完全通过 Azure Bastion 进行。

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` 会阻止分配公共 IP。`--nsg ""` 会跳过创建每个 NIC 级别的 NSG（子网级 NSG 负责安全）。

**可复现性：** 上面的命令对 Ubuntu 镜像使用 `latest`。如需固定特定版本，请列出可用版本并替换 `latest`：

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### 创建 Azure Bastion

Azure Bastion 提供托管 SSH 访问，让你无需暴露公共 IP 即可访问 VM。基于 CLI 的 `az network bastion ssh` 需要启用隧道的 Standard SKU。

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Bastion 预配通常需要 5-10 分钟，但在某些区域可能需要长达 15-30 分钟。

## 安装 OpenClaw

* ### 通过 Azure Bastion SSH 进入 VM

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### 安装 OpenClaw（在 VM shell 中）

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

如果尚未安装，安装程序会安装 Node LTS 和依赖项，安装 OpenClaw，并启动新手引导向导。详情请参阅 [安装](</zh-CN/install>)。

* ### 验证 Gateway 网关

新手引导完成后：

bashCopy code
[code]
    openclaw gateway status
[/code]

大多数企业 Azure 团队已经拥有 GitHub Copilot 许可证。如果你也是这种情况，建议在 OpenClaw 新手引导向导中选择 GitHub Copilot 提供商。请参阅 [GitHub Copilot 提供商](</zh-CN/providers/github-copilot>)。

## 成本注意事项

Azure Bastion Standard SKU 运行成本约为 **$140/月** ，VM (Standard_B2as_v2) 运行成本约为 **$55/月** 。

要降低成本：

  * 不使用时**取消分配 VM** （停止计算计费；磁盘费用仍会保留）。VM 被取消分配时，OpenClaw Gateway 网关将无法访问，请在需要重新上线时重启它：

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * 不需要时**删除 Bastion** ，需要 SSH 访问时再重新创建。Bastion 是最大的成本组成部分，预配只需几分钟。

  * 如果你只需要基于门户的 SSH，且不需要 CLI 隧道（`az network bastion ssh`），请**使用 Basic Bastion SKU** （约 $38/月）。


## 清理

要删除本指南创建的所有资源：

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

这会删除资源组及其中的所有内容（VM、VNet、NSG、Bastion、公共 IP）。

## 后续步骤

  * 设置消息渠道：[Channels](</zh-CN/channels>)
  * 将本地设备配对为节点：[Nodes](</zh-CN/nodes>)
  * 配置 Gateway 网关：[Gateway 配置](</zh-CN/gateway/configuration>)
  * 如需了解关于通过 GitHub Copilot 模型提供商在 Azure 上部署 OpenClaw 的更多详情：[在 Azure 上使用 GitHub Copilot 部署 OpenClaw](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## 相关内容

  * [安装概览](</zh-CN/install>)
  * [GCP](</zh-CN/install/gcp>)
  * [DigitalOcean](</zh-CN/install/digitalocean>)


Was this useful?YesNo