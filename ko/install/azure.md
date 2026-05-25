---
title: Azure
source_url: https://docs.openclaw.ai/ko/install/azure
scraped_at: 2026-05-25
---

이 가이드는 Azure CLI로 Azure Linux VM을 설정하고, Network Security Group(NSG) 강화를 적용하며, SSH 액세스를 위해 Azure Bastion을 구성하고, OpenClaw를 설치합니다.

## 수행할 작업

  * Azure CLI로 Azure 네트워킹(VNet, 서브넷, NSG) 및 컴퓨팅 리소스 생성
  * VM SSH가 Azure Bastion에서만 허용되도록 Network Security Group 규칙 적용
  * SSH 액세스에 Azure Bastion 사용(VM에 공용 IP 없음)
  * 설치 스크립트로 OpenClaw 설치
  * Gateway 확인


## 필요한 것

  * 컴퓨팅 및 네트워크 리소스를 생성할 권한이 있는 Azure 구독
  * Azure CLI 설치됨(필요한 경우 [Azure CLI 설치 단계](<https://learn.microsoft.com/cli/azure/install-azure-cli>) 참조)
  * SSH 키 쌍(필요한 경우 이 가이드에서 생성 방법을 다룹니다)
  * 약 20~30분


## 배포 구성

* ### Azure CLI에 로그인

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

Azure Bastion 네이티브 SSH 터널링에는 `ssh` 확장이 필요합니다.

* ### 필수 리소스 공급자 등록(1회)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

등록을 확인합니다. 둘 다 `Registered`로 표시될 때까지 기다립니다.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### 배포 변수 설정

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

환경에 맞게 이름과 CIDR 범위를 조정하세요. Bastion 서브넷은 최소 `/26`이어야 합니다.

* ### SSH 키 선택

기존 공개 키가 있으면 사용합니다.

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

아직 SSH 키가 없으면 하나 생성합니다.

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### VM 크기 및 OS 디스크 크기 선택

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

구독과 지역에서 사용할 수 있는 VM 크기와 OS 디스크 크기를 선택하세요.

  * 가벼운 사용에는 더 작은 크기로 시작하고 나중에 확장하세요
  * 더 무거운 자동화, 더 많은 채널, 또는 더 큰 모델/도구 워크로드에는 더 많은 vCPU/RAM/디스크를 사용하세요
  * 지역 또는 구독 할당량에서 VM 크기를 사용할 수 없는 경우 사용 가능한 가장 가까운 SKU를 선택하세요


대상 지역에서 사용할 수 있는 VM 크기를 나열합니다.

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

현재 vCPU 및 디스크 사용량/할당량을 확인합니다.

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Azure 리소스 배포

* ### 리소스 그룹 생성

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Network Security Group 생성

NSG를 생성하고 Bastion 서브넷만 VM에 SSH로 접속할 수 있도록 규칙을 추가합니다.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

규칙은 우선순위(가장 낮은 숫자부터)로 평가됩니다. Bastion 트래픽은 100에서 허용되고, 이후 다른 모든 SSH는 110 및 120에서 차단됩니다.

* ### 가상 네트워크 및 서브넷 생성

VM 서브넷(NSG 연결됨)이 포함된 VNet을 생성한 다음 Bastion 서브넷을 추가합니다.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### VM 생성

VM에는 공용 IP가 없습니다. SSH 액세스는 Azure Bastion을 통해서만 이루어집니다.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""`는 공용 IP가 할당되지 않도록 합니다. `--nsg ""`는 NIC별 NSG 생성을 건너뜁니다(서브넷 수준 NSG가 보안을 처리합니다).

**재현성:** 위 명령은 Ubuntu 이미지에 `latest`를 사용합니다. 특정 버전으로 고정하려면 사용 가능한 버전을 나열하고 `latest`를 바꾸세요.

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Azure Bastion 생성

Azure Bastion은 공용 IP를 노출하지 않고 VM에 관리형 SSH 액세스를 제공합니다. CLI 기반 `az network bastion ssh`에는 터널링이 활성화된 Standard SKU가 필요합니다.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Bastion 프로비저닝은 일반적으로 5~10분이 걸리지만, 일부 지역에서는 최대 15~30분이 걸릴 수 있습니다.

## OpenClaw 설치

* ### Azure Bastion을 통해 VM에 SSH 접속

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### OpenClaw 설치(VM 셸에서)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

설치 프로그램은 아직 없는 경우 Node LTS와 종속성을 설치하고, OpenClaw를 설치한 뒤 온보딩 마법사를 실행합니다. 자세한 내용은 [설치](</ko/install>)를 참조하세요.

* ### Gateway 확인

온보딩이 완료된 후:

bashCopy code
[code]
    openclaw gateway status
[/code]

대부분의 엔터프라이즈 Azure 팀은 이미 GitHub Copilot 라이선스를 보유하고 있습니다. 이에 해당하는 경우 OpenClaw 온보딩 마법사에서 GitHub Copilot 공급자를 선택하는 것을 권장합니다. [GitHub Copilot 공급자](</ko/providers/github-copilot>)를 참조하세요.

## 비용 고려 사항

Azure Bastion Standard SKU는 대략 **월 $140** , VM(Standard_B2as_v2)은 대략 **월 $55** 입니다.

비용을 줄이려면:

  * 사용하지 않을 때 **VM 할당을 해제** 하세요(컴퓨팅 과금이 중지되며, 디스크 요금은 계속 발생합니다). VM 할당이 해제되어 있는 동안에는 OpenClaw Gateway에 연결할 수 없습니다. 다시 라이브 상태가 필요할 때 재시작하세요.

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **필요하지 않을 때 Bastion을 삭제** 하고 SSH 액세스가 필요할 때 다시 생성하세요. Bastion은 가장 큰 비용 요소이며, 프로비저닝에는 몇 분만 걸립니다.

  * Portal 기반 SSH만 필요하고 CLI 터널링(`az network bastion ssh`)이 필요하지 않다면 **Basic Bastion SKU**(월 약 $38)를 사용하세요.


## 정리

이 가이드에서 생성한 모든 리소스를 삭제하려면:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

이 명령은 리소스 그룹과 그 안의 모든 항목(VM, VNet, NSG, Bastion, 공용 IP)을 제거합니다.

## 다음 단계

  * 메시징 채널 설정: [채널](</ko/channels>)
  * 로컬 기기를 Node로 페어링: [Nodes](</ko/nodes>)
  * Gateway 구성: [Gateway 구성](</ko/gateway/configuration>)
  * GitHub Copilot 모델 공급자를 사용하는 OpenClaw Azure 배포에 대한 자세한 내용: [GitHub Copilot을 사용하는 Azure의 OpenClaw](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## 관련 항목

  * [설치 개요](</ko/install>)
  * [GCP](</ko/install/gcp>)
  * [DigitalOcean](</ko/install/digitalocean>)


Was this useful?YesNo