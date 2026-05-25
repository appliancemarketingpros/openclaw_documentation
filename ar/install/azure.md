---
title: Azure
source_url: https://docs.openclaw.ai/ar/install/azure
scraped_at: 2026-05-25
---

يعد هذا الدليل جهاز Azure Linux VM باستخدام Azure CLI، ويطبق تقوية Network Security Group (NSG)، ويهيئ Azure Bastion للوصول عبر SSH، ويثبت OpenClaw.

## ما ستفعله

  * إنشاء موارد الشبكات في Azure (VNet، والشبكات الفرعية، وNSG) وموارد الحوسبة باستخدام Azure CLI
  * تطبيق قواعد Network Security Group بحيث يسمح بالوصول إلى VM عبر SSH من Azure Bastion فقط
  * استخدام Azure Bastion للوصول عبر SSH (من دون عنوان IP عام على VM)
  * تثبيت OpenClaw باستخدام سكربت التثبيت
  * التحقق من Gateway


## ما تحتاج إليه

  * اشتراك Azure مع صلاحية إنشاء موارد الحوسبة والشبكات
  * تثبيت Azure CLI (راجع [خطوات تثبيت Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>) عند الحاجة)
  * زوج مفاتيح SSH (يغطي الدليل إنشاء واحد عند الحاجة)
  * نحو 20-30 دقيقة


## تهيئة النشر

* ### تسجيل الدخول إلى Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

يلزم ملحق `ssh` لأنفاق SSH الأصلية عبر Azure Bastion.

* ### تسجيل موفري الموارد المطلوبين (مرة واحدة)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

تحقق من التسجيل. انتظر حتى يعرض كلاهما `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### تعيين متغيرات النشر

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

عدل الأسماء ونطاقات CIDR بما يناسب بيئتك. يجب أن تكون شبكة Bastion الفرعية على الأقل `/26`.

* ### اختيار مفتاح SSH

استخدم مفتاحك العام الحالي إذا كان لديك واحد:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

إذا لم يكن لديك مفتاح SSH بعد، فأنشئ واحدا:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### اختيار حجم VM وحجم قرص نظام التشغيل

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

اختر حجم VM وحجم قرص نظام تشغيل متاحين في اشتراكك ومنطقتك:

  * ابدأ بحجم أصغر للاستخدام الخفيف، ثم وسع لاحقا
  * استخدم مزيدا من vCPU/RAM/القرص للأتمتة الأثقل، أو المزيد من القنوات، أو أحمال عمل النماذج/الأدوات الأكبر
  * إذا كان حجم VM غير متاح في منطقتك أو حصة اشتراكك، فاختر أقرب SKU متاح


اعرض أحجام VM المتاحة في منطقتك المستهدفة:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

تحقق من استخدامك/حصتك الحالية من vCPU والقرص:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## نشر موارد Azure

* ### إنشاء مجموعة الموارد

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### إنشاء مجموعة أمان الشبكة

أنشئ NSG وأضف قواعد بحيث لا تتمكن إلا شبكة Bastion الفرعية من الوصول إلى VM عبر SSH.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

تقيم القواعد حسب الأولوية (أقل رقم أولا): يسمح بحركة Bastion عند 100، ثم يحظر كل SSH الآخر عند 110 و120.

* ### إنشاء الشبكة الافتراضية والشبكات الفرعية

أنشئ VNet مع شبكة VM الفرعية (مع ربط NSG)، ثم أضف شبكة Bastion الفرعية.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### إنشاء VM

لا يحتوي VM على عنوان IP عام. الوصول عبر SSH يتم حصريا من خلال Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

يمنع `--public-ip-address ""` تعيين عنوان IP عام. يتخطى `--nsg ""` إنشاء NSG لكل NIC (يتولى NSG على مستوى الشبكة الفرعية الأمان).

**قابلية إعادة الإنتاج:** يستخدم الأمر أعلاه `latest` لصورة Ubuntu. لتثبيت إصدار محدد، اعرض الإصدارات المتاحة واستبدل `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### إنشاء Azure Bastion

يوفر Azure Bastion وصول SSH مدارا إلى VM من دون تعريض عنوان IP عام. يلزم Standard SKU مع تمكين الأنفاق لاستخدام `az network bastion ssh` المستند إلى CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

يستغرق توفير Bastion عادة 5-10 دقائق، لكنه قد يستغرق حتى 15-30 دقيقة في بعض المناطق.

## تثبيت OpenClaw

* ### الوصول إلى VM عبر SSH من خلال Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### تثبيت OpenClaw (داخل shell الخاص بـ VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

يثبت المثبت Node LTS والتبعيات إذا لم تكن موجودة بالفعل، ويثبت OpenClaw، ويشغل معالج الإعداد الأولي. راجع [التثبيت](</ar/install>) للحصول على التفاصيل.

* ### التحقق من Gateway

بعد اكتمال الإعداد الأولي:

bashCopy code
[code]
    openclaw gateway status
[/code]

لدى معظم فرق Azure المؤسسية تراخيص GitHub Copilot بالفعل. إذا كان هذا هو حالك، نوصي باختيار موفر GitHub Copilot في معالج الإعداد الأولي في OpenClaw. راجع [موفر GitHub Copilot](</ar/providers/github-copilot>).

## اعتبارات التكلفة

يعمل Azure Bastion Standard SKU بتكلفة تقارب **$140/شهريا** ويعمل VM (Standard_B2as_v2) بتكلفة تقارب **$55/شهريا**.

لتقليل التكاليف:

  * **إلغاء تخصيص VM** عند عدم استخدامه (يوقف فوترة الحوسبة؛ تبقى رسوم القرص). لن يكون OpenClaw Gateway قابلا للوصول أثناء إلغاء تخصيص VM — أعد تشغيله عندما تحتاج إلى تشغيله مباشرة مرة أخرى:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **احذف Bastion عندما لا تحتاج إليه** وأعد إنشاءه عندما تحتاج إلى وصول SSH. Bastion هو أكبر مكون تكلفة ولا يستغرق توفيره إلا بضع دقائق.

  * **استخدم Basic Bastion SKU** (~$38/شهريا) إذا كنت تحتاج فقط إلى SSH المستند إلى Portal ولا تحتاج إلى أنفاق CLI (`az network bastion ssh`).


## التنظيف

لحذف جميع الموارد التي أنشأها هذا الدليل:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

يزيل هذا مجموعة الموارد وكل ما بداخلها (VM، وVNet، وNSG، وBastion، وعنوان IP العام).

## الخطوات التالية

  * إعداد قنوات المراسلة: [القنوات](</ar/channels>)
  * إقران الأجهزة المحلية كعقد: [العقد](</ar/nodes>)
  * تهيئة Gateway: [تهيئة Gateway](</ar/gateway/configuration>)
  * لمزيد من التفاصيل حول نشر OpenClaw على Azure باستخدام موفر نموذج GitHub Copilot: [OpenClaw على Azure مع GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## ذو صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [GCP](</ar/install/gcp>)
  * [DigitalOcean](</ar/install/digitalocean>)


Was this useful?YesNo