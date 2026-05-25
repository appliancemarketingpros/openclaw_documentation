---
title: Azure
source_url: https://docs.openclaw.ai/tr/install/azure
scraped_at: 2026-05-25
---

Bu kılavuz, Azure CLI ile bir Azure Linux VM kurar, Network Security Group (NSG) sıkılaştırması uygular, SSH erişimi için Azure Bastion yapılandırır ve OpenClaw yükler.

## Yapacaklarınız

  * Azure CLI ile Azure ağını (VNet, alt ağlar, NSG) ve işlem kaynaklarını oluşturma
  * VM SSH erişimine yalnızca Azure Bastion üzerinden izin verilecek şekilde Network Security Group kurallarını uygulama
  * SSH erişimi için Azure Bastion kullanma (VM üzerinde genel IP yok)
  * Yükleyici betiğiyle OpenClaw yükleme
  * Gateway’i doğrulama


## Gerekenler

  * İşlem ve ağ kaynakları oluşturma iznine sahip bir Azure aboneliği
  * Azure CLI yüklü (gerekirse [Azure CLI yükleme adımlarına](<https://learn.microsoft.com/cli/azure/install-azure-cli>) bakın)
  * Bir SSH anahtar çifti (gerekirse kılavuz bir tane oluşturmayı kapsar)
  * ~20-30 dakika


## Dağıtımı yapılandırma

* ### Azure CLI’da oturum açın

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

`ssh` uzantısı, Azure Bastion yerel SSH tünellemesi için gereklidir.

* ### Gerekli kaynak sağlayıcılarını kaydedin (bir kerelik)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Kaydı doğrulayın. İkisi de `Registered` gösterene kadar bekleyin.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Dağıtım değişkenlerini ayarlayın

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Adları ve CIDR aralıklarını ortamınıza uyacak şekilde ayarlayın. Bastion alt ağı en az `/26` olmalıdır.

* ### SSH anahtarı seçin

Varsa mevcut genel anahtarınızı kullanın:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Henüz bir SSH anahtarınız yoksa bir tane oluşturun:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### VM boyutunu ve OS disk boyutunu seçin

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Aboneliğinizde ve bölgenizde kullanılabilir bir VM boyutu ve OS disk boyutu seçin:

  * Hafif kullanım için daha küçük başlayın ve daha sonra ölçek büyütün
  * Daha ağır otomasyon, daha fazla kanal veya daha büyük model/araç iş yükleri için daha fazla vCPU/RAM/disk kullanın
  * Bir VM boyutu bölgenizde veya abonelik kotanızda kullanılamıyorsa, kullanılabilir en yakın SKU’yu seçin


Hedef bölgenizde kullanılabilir VM boyutlarını listeleyin:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Geçerli vCPU ve disk kullanımınızı/kotanızı kontrol edin:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Azure kaynaklarını dağıtma

* ### Kaynak grubunu oluşturun

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Network Security Group oluşturun

NSG’yi oluşturun ve yalnızca Bastion alt ağının VM’ye SSH ile bağlanabilmesi için kurallar ekleyin.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Kurallar önceliğe göre değerlendirilir (en düşük sayı önce): Bastion trafiğine 100’de izin verilir, ardından diğer tüm SSH erişimi 110 ve 120’de engellenir.

* ### Sanal ağı ve alt ağları oluşturun

VM alt ağıyla (NSG bağlı) VNet’i oluşturun, ardından Bastion alt ağını ekleyin.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### VM’yi oluşturun

VM’nin genel IP’si yoktur. SSH erişimi yalnızca Azure Bastion üzerinden yapılır.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` genel IP atanmasını engeller. `--nsg ""` NIC başına NSG oluşturmayı atlar (güvenliği alt ağ düzeyindeki NSG sağlar).

**Yeniden üretilebilirlik:** Yukarıdaki komut, Ubuntu imajı için `latest` kullanır. Belirli bir sürümü sabitlemek için kullanılabilir sürümleri listeleyin ve `latest` değerini değiştirin:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Azure Bastion oluşturun

Azure Bastion, genel IP açığa çıkarmadan VM’ye yönetilen SSH erişimi sağlar. CLI tabanlı `az network bastion ssh` için tünelleme özellikli Standard SKU gereklidir.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Bastion hazırlama genellikle 5-10 dakika sürer, ancak bazı bölgelerde 15-30 dakikaya kadar sürebilir.

## OpenClaw yükleme

* ### Azure Bastion üzerinden VM’ye SSH ile bağlanın

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### OpenClaw yükleyin (VM kabuğunda)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

Yükleyici, henüz mevcut değilse Node LTS ve bağımlılıkları yükler, OpenClaw’u yükler ve ilk kurulum sihirbazını başlatır. Ayrıntılar için [Yükleme](</tr/install>) bölümüne bakın.

* ### Gateway’i doğrulayın

İlk kurulum tamamlandıktan sonra:

bashCopy code
[code]
    openclaw gateway status
[/code]

Çoğu kurumsal Azure ekibinin zaten GitHub Copilot lisansları vardır. Durumunuz buysa, OpenClaw ilk kurulum sihirbazında GitHub Copilot sağlayıcısını seçmenizi öneririz. [GitHub Copilot sağlayıcısı](</tr/providers/github-copilot>) bölümüne bakın.

## Maliyet değerlendirmeleri

Azure Bastion Standard SKU yaklaşık **$140/ay** , VM (Standard_B2as_v2) ise yaklaşık **$55/ay** maliyetle çalışır.

Maliyetleri azaltmak için:

  * **VM’yi ayırın** kullanılmadığında (işlem faturalandırmasını durdurur; disk ücretleri devam eder). VM ayrılmış durumdayken OpenClaw Gateway’e erişilemez; tekrar canlı ihtiyacınız olduğunda yeniden başlatın:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Gerekmediğinde Bastion’ı silin** ve SSH erişimine ihtiyacınız olduğunda yeniden oluşturun. Bastion en büyük maliyet bileşenidir ve hazırlanması yalnızca birkaç dakika sürer.

  * Yalnızca Portal tabanlı SSH gerekiyorsa ve CLI tünellemesi (`az network bastion ssh`) gerekmiyorsa **Basic Bastion SKU’yu** (~$38/ay) kullanın.


## Temizleme

Bu kılavuz tarafından oluşturulan tüm kaynakları silmek için:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Bu işlem kaynak grubunu ve içindeki her şeyi (VM, VNet, NSG, Bastion, genel IP) kaldırır.

## Sonraki adımlar

  * Mesajlaşma kanallarını ayarlayın: [Kanallar](</tr/channels>)
  * Yerel cihazları Node olarak eşleyin: [Nodes](</tr/nodes>)
  * Gateway’i yapılandırın: [Gateway yapılandırması](</tr/gateway/configuration>)
  * GitHub Copilot model sağlayıcısıyla OpenClaw Azure dağıtımı hakkında daha fazla ayrıntı için: [GitHub Copilot ile Azure üzerinde OpenClaw](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## İlgili

  * [Yüklemeye genel bakış](</tr/install>)
  * [GCP](</tr/install/gcp>)
  * [DigitalOcean](</tr/install/digitalocean>)


Was this useful?YesNo