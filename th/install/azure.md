---
title: Azure
source_url: https://docs.openclaw.ai/th/install/azure
scraped_at: 2026-05-25
---

คู่มือนี้ตั้งค่า Azure Linux VM ด้วย Azure CLI, ใช้การเสริมความปลอดภัยของ Network Security Group (NSG), กำหนดค่า Azure Bastion สำหรับการเข้าถึง SSH และติดตั้ง OpenClaw

## สิ่งที่คุณจะทำ

  * สร้างเครือข่าย Azure (VNet, ซับเน็ต, NSG) และทรัพยากรคอมพิวต์ด้วย Azure CLI
  * ใช้กฎ Network Security Group เพื่อให้ VM SSH อนุญาตเฉพาะจาก Azure Bastion เท่านั้น
  * ใช้ Azure Bastion สำหรับการเข้าถึง SSH (ไม่มี IP สาธารณะบน VM)
  * ติดตั้ง OpenClaw ด้วยสคริปต์ตัวติดตั้ง
  * ตรวจสอบ Gateway


## สิ่งที่คุณต้องมี

  * การสมัครใช้งาน Azure ที่มีสิทธิ์สร้างทรัพยากรคอมพิวต์และเครือข่าย
  * ติดตั้ง Azure CLI แล้ว (ดู [ขั้นตอนการติดตั้ง Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>) หากจำเป็น)
  * คู่คีย์ SSH (คู่มือนี้ครอบคลุมการสร้างคีย์หากจำเป็น)
  * ประมาณ 20-30 นาที


## กำหนดค่าการปรับใช้

* ### ลงชื่อเข้าใช้ Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

ต้องใช้ส่วนขยาย `ssh` สำหรับการทำ SSH tunneling แบบ native ของ Azure Bastion

* ### ลงทะเบียนผู้ให้บริการทรัพยากรที่จำเป็น (ครั้งเดียว)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

ตรวจสอบการลงทะเบียน รอจนกว่าทั้งสองรายการจะแสดง `Registered`

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### ตั้งค่าตัวแปรการปรับใช้

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

ปรับชื่อและช่วง CIDR ให้เหมาะกับสภาพแวดล้อมของคุณ ซับเน็ต Bastion ต้องมีขนาดอย่างน้อย `/26`

* ### เลือกคีย์ SSH

ใช้คีย์สาธารณะที่มีอยู่ของคุณ หากคุณมีอยู่แล้ว:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

หากคุณยังไม่มีคีย์ SSH ให้สร้างคีย์ใหม่:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### เลือกขนาด VM และขนาดดิสก์ OS

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

เลือกขนาด VM และขนาดดิสก์ OS ที่พร้อมใช้งานในการสมัครใช้งานและภูมิภาคของคุณ:

  * เริ่มจากขนาดเล็กกว่าสำหรับการใช้งานเบา แล้วค่อยขยายภายหลัง
  * ใช้ vCPU/RAM/ดิสก์มากขึ้นสำหรับระบบอัตโนมัติที่หนักขึ้น ช่องทางมากขึ้น หรือเวิร์กโหลดโมเดล/เครื่องมือที่ใหญ่ขึ้น
  * หากขนาด VM ไม่พร้อมใช้งานในภูมิภาคหรือโควตาการสมัครใช้งานของคุณ ให้เลือก SKU ที่ใกล้เคียงที่สุดที่พร้อมใช้งาน


แสดงรายการขนาด VM ที่พร้อมใช้งานในภูมิภาคเป้าหมายของคุณ:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

ตรวจสอบการใช้งาน/โควตา vCPU และดิสก์ปัจจุบันของคุณ:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## ปรับใช้ทรัพยากร Azure

* ### สร้างกลุ่มทรัพยากร

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### สร้างกลุ่มความปลอดภัยเครือข่าย

สร้าง NSG และเพิ่มกฎเพื่อให้เฉพาะซับเน็ต Bastion เท่านั้นที่สามารถ SSH เข้า VM ได้

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

กฎจะถูกประเมินตามลำดับความสำคัญ (ตัวเลขต่ำสุดก่อน): อนุญาตทราฟฟิก Bastion ที่ 100 จากนั้นบล็อก SSH อื่นทั้งหมดที่ 110 และ 120

* ### สร้างเครือข่ายเสมือนและซับเน็ต

สร้าง VNet พร้อมซับเน็ต VM (แนบ NSG) จากนั้นเพิ่มซับเน็ต Bastion

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### สร้าง VM

VM ไม่มี IP สาธารณะ การเข้าถึง SSH ทำผ่าน Azure Bastion เท่านั้น

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` ป้องกันไม่ให้มีการกำหนด IP สาธารณะ `--nsg ""` ข้ามการสร้าง NSG ต่อ NIC (NSG ระดับซับเน็ตจัดการความปลอดภัย)

**ความสามารถในการทำซ้ำ:** คำสั่งด้านบนใช้ `latest` สำหรับอิมเมจ Ubuntu หากต้องการตรึงเวอร์ชันเฉพาะ ให้แสดงรายการเวอร์ชันที่พร้อมใช้งานและแทนที่ `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### สร้าง Azure Bastion

Azure Bastion ให้การเข้าถึง SSH ที่จัดการแล้วไปยัง VM โดยไม่เปิดเผย IP สาธารณะ ต้องใช้ Standard SKU พร้อม tunneling สำหรับ `az network bastion ssh` ที่ใช้ CLI

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

โดยทั่วไป การจัดเตรียม Bastion ใช้เวลา 5-10 นาที แต่อาจใช้เวลาถึง 15-30 นาทีในบางภูมิภาค

## ติดตั้ง OpenClaw

* ### SSH เข้า VM ผ่าน Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### ติดตั้ง OpenClaw (ในเชลล์ VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

ตัวติดตั้งจะติดตั้ง Node LTS และการพึ่งพาหากยังไม่มีอยู่ ติดตั้ง OpenClaw และเปิดตัวช่วยสร้างการเริ่มใช้งาน ดูรายละเอียดที่ [ติดตั้ง](</th/install>)

* ### ตรวจสอบ Gateway

หลังจากการเริ่มใช้งานเสร็จสมบูรณ์:

bashCopy code
[code]
    openclaw gateway status
[/code]

ทีม Azure ระดับองค์กรส่วนใหญ่มีไลเซนส์ GitHub Copilot อยู่แล้ว หากเป็นกรณีของคุณ เราแนะนำให้เลือกผู้ให้บริการ GitHub Copilot ในตัวช่วยสร้างการเริ่มใช้งาน OpenClaw ดู [ผู้ให้บริการ GitHub Copilot](</th/providers/github-copilot>)

## ข้อควรพิจารณาด้านค่าใช้จ่าย

Azure Bastion Standard SKU มีค่าใช้จ่ายประมาณ **$140/เดือน** และ VM (Standard_B2as_v2) มีค่าใช้จ่ายประมาณ **$55/เดือน**

เพื่อลดค่าใช้จ่าย:

  * **ยกเลิกการจัดสรร VM** เมื่อไม่ได้ใช้งาน (หยุดการคิดค่าคอมพิวต์; ค่าดิสก์ยังคงอยู่) OpenClaw Gateway จะไม่สามารถเข้าถึงได้ขณะที่ VM ถูกยกเลิกการจัดสรร — เริ่มใหม่เมื่อคุณต้องการให้พร้อมใช้งานอีกครั้ง:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **ลบ Bastion เมื่อไม่จำเป็น** และสร้างใหม่เมื่อคุณต้องการการเข้าถึง SSH Bastion เป็นองค์ประกอบต้นทุนที่ใหญ่ที่สุดและใช้เวลาเพียงไม่กี่นาทีในการจัดเตรียม

  * **ใช้ Basic Bastion SKU** (~$38/เดือน) หากคุณต้องการเฉพาะ SSH ผ่าน Portal และไม่ต้องใช้ CLI tunneling (`az network bastion ssh`)


## การล้างข้อมูล

เพื่อลบทรัพยากรทั้งหมดที่สร้างโดยคู่มือนี้:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

การดำเนินการนี้จะลบกลุ่มทรัพยากรและทุกอย่างภายในนั้น (VM, VNet, NSG, Bastion, IP สาธารณะ)

## ขั้นตอนถัดไป

  * ตั้งค่าช่องทางข้อความ: [ช่องทาง](</th/channels>)
  * จับคู่อุปกรณ์ภายในเครื่องเป็น Node: [Node](</th/nodes>)
  * กำหนดค่า Gateway: [การกำหนดค่า Gateway](</th/gateway/configuration>)
  * สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับการปรับใช้ OpenClaw บน Azure ด้วยผู้ให้บริการโมเดล GitHub Copilot: [OpenClaw บน Azure พร้อม GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## ที่เกี่ยวข้อง

  * [ภาพรวมการติดตั้ง](</th/install>)
  * [GCP](</th/install/gcp>)
  * [DigitalOcean](</th/install/digitalocean>)


Was this useful?YesNo