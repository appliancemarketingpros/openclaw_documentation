---
title: Azure
source_url: https://docs.openclaw.ai/es/install/azure
scraped_at: 2026-05-25
---

Esta guía configura una VM de Linux de Azure con la CLI de Azure, aplica endurecimiento de Network Security Group (NSG), configura Azure Bastion para acceso SSH e instala OpenClaw.

## Qué harás

  * Crear recursos de red de Azure (VNet, subredes, NSG) y recursos de cómputo con la CLI de Azure
  * Aplicar reglas de Network Security Group para que el SSH de la VM solo se permita desde Azure Bastion
  * Usar Azure Bastion para acceso SSH (sin IP pública en la VM)
  * Instalar OpenClaw con el script de instalación
  * Verificar el Gateway


## Qué necesitas

  * Una suscripción de Azure con permiso para crear recursos de cómputo y red
  * CLI de Azure instalada (consulta los [pasos de instalación de la CLI de Azure](<https://learn.microsoft.com/cli/azure/install-azure-cli>) si es necesario)
  * Un par de claves SSH (la guía cubre cómo generar uno si es necesario)
  * ~20-30 minutos


## Configurar la implementación

* ### Iniciar sesión en la CLI de Azure

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

La extensión `ssh` es necesaria para el túnel SSH nativo de Azure Bastion.

* ### Registrar los proveedores de recursos necesarios (una vez)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Verifica el registro. Espera hasta que ambos muestren `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Establecer variables de implementación

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Ajusta los nombres y rangos CIDR para que se adapten a tu entorno. La subred de Bastion debe ser al menos `/26`.

* ### Seleccionar clave SSH

Usa tu clave pública existente si tienes una:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Si aún no tienes una clave SSH, genera una:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Seleccionar tamaño de VM y tamaño del disco del SO

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Elige un tamaño de VM y un tamaño de disco del SO disponibles en tu suscripción y región:

  * Comienza con algo más pequeño para uso ligero y escala más adelante
  * Usa más vCPU/RAM/disco para automatización más pesada, más canales o cargas de trabajo de modelos/herramientas más grandes
  * Si un tamaño de VM no está disponible en tu región o cuota de suscripción, elige el SKU disponible más cercano


Lista los tamaños de VM disponibles en tu región de destino:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Comprueba tu uso/cuota actual de vCPU y disco:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Implementar recursos de Azure

* ### Crear el grupo de recursos

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Crear el grupo de seguridad de red

Crea el NSG y agrega reglas para que solo la subred de Bastion pueda hacer SSH a la VM.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Las reglas se evalúan por prioridad (primero el número más bajo): el tráfico de Bastion se permite en 100 y luego todo el resto del SSH se bloquea en 110 y 120.

* ### Crear la red virtual y las subredes

Crea la VNet con la subred de la VM (con el NSG asociado) y luego agrega la subred de Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Crear la VM

La VM no tiene IP pública. El acceso SSH se realiza exclusivamente mediante Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` evita que se asigne una IP pública. `--nsg ""` omite la creación de un NSG por NIC (el NSG a nivel de subred gestiona la seguridad).

**Reproducibilidad:** El comando anterior usa `latest` para la imagen de Ubuntu. Para fijar una versión específica, lista las versiones disponibles y sustituye `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Crear Azure Bastion

Azure Bastion proporciona acceso SSH administrado a la VM sin exponer una IP pública. Se requiere el SKU Standard con tunelización para `az network bastion ssh` basado en CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

El aprovisionamiento de Bastion suele tardar 5-10 minutos, pero puede tardar hasta 15-30 minutos en algunas regiones.

## Instalar OpenClaw

* ### Conectarse por SSH a la VM mediante Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Instalar OpenClaw (en la shell de la VM)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

El instalador instala Node LTS y las dependencias si aún no están presentes, instala OpenClaw e inicia el asistente de incorporación. Consulta [Instalar](</es/install>) para obtener más detalles.

* ### Verificar el Gateway

Después de completar la incorporación:

bashCopy code
[code]
    openclaw gateway status
[/code]

La mayoría de los equipos empresariales de Azure ya tienen licencias de GitHub Copilot. Si ese es tu caso, recomendamos elegir el proveedor GitHub Copilot en el asistente de incorporación de OpenClaw. Consulta [Proveedor GitHub Copilot](</es/providers/github-copilot>).

## Consideraciones de costo

El SKU Standard de Azure Bastion cuesta aproximadamente **$140/mes** y la VM (Standard_B2as_v2) cuesta aproximadamente **$55/mes**.

Para reducir costos:

  * **Desasigna la VM** cuando no esté en uso (detiene la facturación de cómputo; los cargos de disco permanecen). El Gateway de OpenClaw no estará accesible mientras la VM esté desasignada; reiníciala cuando necesites que vuelva a estar activa:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Elimina Bastion cuando no sea necesario** y recréalo cuando necesites acceso SSH. Bastion es el componente de mayor costo y tarda solo unos minutos en aprovisionarse.

  * **Usa el SKU Basic de Bastion** (~$38/mes) si solo necesitas SSH basado en el Portal y no requieres tunelización por CLI (`az network bastion ssh`).


## Limpieza

Para eliminar todos los recursos creados por esta guía:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Esto elimina el grupo de recursos y todo lo que contiene (VM, VNet, NSG, Bastion, IP pública).

## Pasos siguientes

  * Configura canales de mensajería: [Canales](</es/channels>)
  * Empareja dispositivos locales como nodos: [Nodos](</es/nodes>)
  * Configura el Gateway: [Configuración del Gateway](</es/gateway/configuration>)
  * Para obtener más detalles sobre la implementación de OpenClaw en Azure con el proveedor de modelos GitHub Copilot: [OpenClaw en Azure con GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [GCP](</es/install/gcp>)
  * [DigitalOcean](</es/install/digitalocean>)


Was this useful?YesNo