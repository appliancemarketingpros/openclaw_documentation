---
title: Azure
source_url: https://docs.openclaw.ai/hi/install/azure
scraped_at: 2026-06-29
---

InstallHosting

यह मार्गदर्शिका Azure CLI के साथ Azure Linux VM सेट अप करती है, Network Security Group (NSG) हार्डनिंग लागू करती है, SSH पहुंच के लिए Azure Bastion कॉन्फ़िगर करती है, और OpenClaw इंस्टॉल करती है।

## आप क्या करेंगे

  * Azure CLI के साथ Azure नेटवर्किंग (VNet, सबनेट, NSG) और कंप्यूट संसाधन बनाना
  * Network Security Group नियम लागू करना ताकि VM SSH केवल Azure Bastion से अनुमति पाए
  * SSH पहुंच के लिए Azure Bastion का उपयोग करना (VM पर कोई सार्वजनिक IP नहीं)
  * इंस्टॉलर स्क्रिप्ट के साथ OpenClaw इंस्टॉल करना
  * Gateway सत्यापित करना


## आपको क्या चाहिए

  * कंप्यूट और नेटवर्क संसाधन बनाने की अनुमति वाली Azure सदस्यता
  * Azure CLI इंस्टॉल किया हुआ (ज़रूरत हो तो [Azure CLI इंस्टॉल चरण](<https://learn.microsoft.com/cli/azure/install-azure-cli>) देखें)
  * एक SSH कुंजी युग्म (ज़रूरत होने पर यह मार्गदर्शिका उसे जनरेट करना कवर करती है)
  * ~20-30 मिनट


## डिप्लॉयमेंट कॉन्फ़िगर करें

* ### Azure CLI में साइन इन करें

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

Azure Bastion नेटिव SSH टनलिंग के लिए `ssh` एक्सटेंशन आवश्यक है।

* ### आवश्यक संसाधन प्रदाताओं को रजिस्टर करें (एक बार)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

रजिस्ट्रेशन सत्यापित करें। दोनों में `Registered` दिखने तक प्रतीक्षा करें।

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### डिप्लॉयमेंट वेरिएबल सेट करें

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

अपने परिवेश के अनुसार नाम और CIDR रेंज समायोजित करें। Bastion सबनेट कम से कम `/26` होना चाहिए।

* ### SSH कुंजी चुनें

यदि आपके पास मौजूदा सार्वजनिक कुंजी है, तो उसका उपयोग करें:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

यदि आपके पास अभी SSH कुंजी नहीं है, तो एक जनरेट करें:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### VM आकार और OS डिस्क आकार चुनें

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

अपनी सदस्यता और क्षेत्र में उपलब्ध VM आकार और OS डिस्क आकार चुनें:

  * हल्के उपयोग के लिए छोटे आकार से शुरू करें और बाद में स्केल अप करें
  * भारी ऑटोमेशन, अधिक चैनल, या बड़े मॉडल/टूल वर्कलोड के लिए अधिक vCPU/RAM/डिस्क का उपयोग करें
  * यदि कोई VM आकार आपके क्षेत्र या सदस्यता कोटा में उपलब्ध नहीं है, तो निकटतम उपलब्ध SKU चुनें


अपने लक्ष्य क्षेत्र में उपलब्ध VM आकारों की सूची देखें:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

अपना वर्तमान vCPU और डिस्क उपयोग/कोटा जांचें:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Azure संसाधन डिप्लॉय करें

* ### संसाधन समूह बनाएं

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### नेटवर्क सुरक्षा समूह बनाएं

NSG बनाएं और नियम जोड़ें ताकि केवल Bastion सबनेट VM में SSH कर सके।

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

नियमों का मूल्यांकन प्राथमिकता के अनुसार किया जाता है (सबसे कम संख्या पहले): Bastion ट्रैफ़िक को 100 पर अनुमति मिलती है, फिर बाकी सभी SSH को 110 और 120 पर ब्लॉक किया जाता है।

* ### वर्चुअल नेटवर्क और सबनेट बनाएं

VM सबनेट (NSG संलग्न) के साथ VNet बनाएं, फिर Bastion सबनेट जोड़ें।

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### VM बनाएं

VM में कोई सार्वजनिक IP नहीं है। SSH पहुंच विशेष रूप से Azure Bastion के माध्यम से है।

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` सार्वजनिक IP असाइन होने से रोकता है। `--nsg ""` प्रति-NIC NSG बनाने को छोड़ देता है (सबनेट-स्तर का NSG सुरक्षा संभालता है)।

**पुनरुत्पादकता:** ऊपर दिया गया कमांड Ubuntu इमेज के लिए `latest` का उपयोग करता है। किसी विशिष्ट संस्करण को पिन करने के लिए, उपलब्ध संस्करणों की सूची देखें और `latest` बदलें:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Azure Bastion बनाएं

Azure Bastion सार्वजनिक IP उजागर किए बिना VM तक प्रबंधित SSH पहुंच प्रदान करता है। CLI-आधारित `az network bastion ssh` के लिए टनलिंग वाला Standard SKU आवश्यक है।

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Bastion प्रोविजनिंग में आम तौर पर 5-10 मिनट लगते हैं, लेकिन कुछ क्षेत्रों में 15-30 मिनट तक लग सकते हैं।

## OpenClaw इंस्टॉल करें

* ### Azure Bastion के माध्यम से VM में SSH करें

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### OpenClaw इंस्टॉल करें (VM शेल में)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

इंस्टॉलर Node LTS और निर्भरताएं इंस्टॉल करता है यदि वे पहले से मौजूद नहीं हैं, OpenClaw इंस्टॉल करता है, और ऑनबोर्डिंग विज़ार्ड लॉन्च करता है। विवरण के लिए [इंस्टॉल](</hi/install>) देखें।

* ### Gateway सत्यापित करें

ऑनबोर्डिंग पूरी होने के बाद:

bashCopy code
[code]
    openclaw gateway status
[/code]

अधिकांश एंटरप्राइज़ Azure टीमों के पास पहले से GitHub Copilot लाइसेंस होते हैं। यदि आपके मामले में ऐसा है, तो हम OpenClaw ऑनबोर्डिंग विज़ार्ड में GitHub Copilot प्रदाता चुनने की अनुशंसा करते हैं। [GitHub Copilot प्रदाता](</hi/providers/github-copilot>) देखें।

## लागत संबंधी विचार

Azure Bastion Standard SKU लगभग **$140/माह** चलता है और VM (Standard_B2as_v2) लगभग **$55/माह** चलता है।

लागत कम करने के लिए:

  * **VM को डिअलोकेट करें** जब उपयोग में न हो (कंप्यूट बिलिंग रुकती है; डिस्क शुल्क बने रहते हैं)। VM डिअलोकेट होने पर OpenClaw Gateway पहुंच योग्य नहीं होगा — जब आपको इसे फिर से लाइव चाहिए, तो इसे पुनः प्रारंभ करें:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Bastion की आवश्यकता न होने पर उसे हटाएं** और SSH पहुंच की आवश्यकता होने पर फिर से बनाएं। Bastion सबसे बड़ा लागत घटक है और इसे प्रोविजन करने में केवल कुछ मिनट लगते हैं।

  * यदि आपको केवल Portal-आधारित SSH चाहिए और CLI टनलिंग (`az network bastion ssh`) की आवश्यकता नहीं है, तो **Basic Bastion SKU** (~$38/माह) का उपयोग करें।


## क्लीनअप

इस मार्गदर्शिका द्वारा बनाए गए सभी संसाधन हटाने के लिए:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

यह संसाधन समूह और उसके अंदर की हर चीज़ (VM, VNet, NSG, Bastion, सार्वजनिक IP) हटा देता है।

## अगले चरण

  * मैसेजिंग चैनल सेट अप करें: [चैनल](</hi/channels>)
  * स्थानीय डिवाइसों को नोड के रूप में पेयर करें: [नोड](</hi/nodes>)
  * Gateway कॉन्फ़िगर करें: [Gateway कॉन्फ़िगरेशन](</hi/gateway/configuration>)
  * GitHub Copilot मॉडल प्रदाता के साथ OpenClaw Azure डिप्लॉयमेंट पर अधिक जानकारी के लिए: [GitHub Copilot के साथ Azure पर OpenClaw](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>)
  * [GCP](</hi/install/gcp>)
  * [DigitalOcean](</hi/install/digitalocean>)


Was this useful?YesNo

Open issue