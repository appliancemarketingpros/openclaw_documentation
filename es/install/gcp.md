---
title: GCP
source_url: https://docs.openclaw.ai/es/install/gcp
scraped_at: 2026-05-25
---

Ejecuta un Gateway de OpenClaw persistente en una VM de GCP Compute Engine usando Docker, con estado duradero, binarios integrados y comportamiento de reinicio seguro.

Si quieres "OpenClaw 24/7 por ~$5-12/mes", esta es una configuración fiable en Google Cloud. Los precios varían según el tipo de máquina y la región; elige la VM más pequeña que se ajuste a tu carga de trabajo y aumenta la escala si encuentras OOMs.

## ¿Qué estamos haciendo (en términos simples)?

  * Crear un proyecto de GCP y habilitar la facturación
  * Crear una VM de Compute Engine
  * Instalar Docker (entorno de ejecución de aplicación aislado)
  * Iniciar el Gateway de OpenClaw en Docker
  * Persistir `~/.openclaw` \+ `~/.openclaw/workspace` en el host (sobrevive a reinicios/reconstrucciones)
  * Acceder a la Control UI desde tu portátil mediante un túnel SSH


Ese estado montado de `~/.openclaw` incluye `openclaw.json`, por agente `agents/<agentId>/agent/auth-profiles.json` y `.env`.

Se puede acceder al Gateway mediante:

  * Reenvío de puertos SSH desde tu portátil
  * Exposición directa del puerto si gestionas el firewall y los tokens por tu cuenta


Esta guía usa Debian en GCP Compute Engine. Ubuntu también funciona; asigna los paquetes según corresponda. Para el flujo genérico de Docker, consulta [Docker](</es/install/docker>).

* * *

## Ruta rápida (operadores con experiencia)

  1. Crea un proyecto de GCP + habilita la API de Compute Engine
  2. Crea una VM de Compute Engine (e2-small, Debian 12, 20GB)
  3. Accede por SSH a la VM
  4. Instala Docker
  5. Clona el repositorio de OpenClaw
  6. Crea directorios persistentes en el host
  7. Configura `.env` y `docker-compose.yml`
  8. Integra los binarios requeridos, compila e inicia


* * *

## Lo que necesitas

  * Cuenta de GCP (apta para el nivel gratuito con e2-micro)
  * CLI de gcloud instalada (o usar Cloud Console)
  * Acceso SSH desde tu portátil
  * Comodidad básica con SSH + copiar/pegar
  * ~20-30 minutos
  * Docker y Docker Compose
  * Credenciales de autenticación del modelo
  * Credenciales opcionales de proveedores 
    * QR de WhatsApp
    * Token de bot de Telegram
    * OAuth de Gmail


* * *

* ### Install gcloud CLI (or use Console)

**Opción A: CLI de gcloud** (recomendada para automatización)

Instala desde <https://cloud.google.com/sdk/docs/install>

Inicializa y autentícate:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Opción B: Cloud Console**

Todos los pasos se pueden realizar mediante la interfaz web en <https://console.cloud.google.com>

* ### Create a GCP project

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Habilita la facturación en <https://console.cloud.google.com/billing> (requerida para Compute Engine).

Habilita la API de Compute Engine:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. Ve a IAM y administración > Crear proyecto
  2. Asígnale un nombre y créalo
  3. Habilita la facturación para el proyecto
  4. Navega a APIs y servicios > Habilitar APIs > busca "Compute Engine API" > Habilitar


* ### Create the VM

**Tipos de máquina:**

Tipo | Especificaciones | Costo | Notas  
---|---|---|---  
e2-medium | 2 vCPU, 4GB RAM | ~$25/mes | Más fiable para compilaciones locales de Docker  
e2-small | 2 vCPU, 2GB RAM | ~$12/mes | Mínimo recomendado para compilación de Docker  
e2-micro | 2 vCPU (compartidas), 1GB RAM | Apto para nivel gratuito | A menudo falla con OOM en compilación de Docker (salida 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. Ve a Compute Engine > Instancias de VM > Crear instancia
  2. Nombre: `openclaw-gateway`
  3. Región: `us-central1`, Zona: `us-central1-a`
  4. Tipo de máquina: `e2-small`
  5. Disco de arranque: Debian 12, 20GB
  6. Crear


* ### SSH into the VM

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

Haz clic en el botón "SSH" junto a tu VM en el panel de Compute Engine.

Nota: la propagación de claves SSH puede tardar 1-2 minutos después de crear la VM. Si se rechaza la conexión, espera y vuelve a intentarlo.

* ### Install Docker (on the VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Cierra sesión y vuelve a entrar para que el cambio de grupo surta efecto:

bashCopy code
[code]
    exit
[/code]

Luego vuelve a acceder por SSH:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

Verifica:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone the OpenClaw repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Esta guía asume que compilarás una imagen personalizada para garantizar la persistencia de binarios.

* ### Create persistent host directories

Los contenedores Docker son efímeros. Todo el estado de larga duración debe vivir en el host.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Configure environment variables

Crea `.env` en la raíz del repositorio.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Define `OPENCLAW_GATEWAY_TOKEN` cuando quieras gestionar el token estable del gateway mediante `.env`; de lo contrario, configura `gateway.auth.token` antes de depender de clientes entre reinicios. Si no existe ninguna de las dos fuentes, OpenClaw usa un token solo en tiempo de ejecución para ese inicio. Genera una contraseña para el keyring y pégala en `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**No confirmes este archivo en el repositorio.**

Este archivo `.env` es para variables de entorno de contenedor/tiempo de ejecución como `OPENCLAW_GATEWAY_TOKEN`. La autenticación OAuth/API-key almacenada de proveedores vive en el archivo montado `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Docker Compose configuration

Crea o actualiza `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` es solo para comodidad durante el arranque inicial, no reemplaza una configuración adecuada del gateway. Aun así, configura la autenticación (`gateway.auth.token` o contraseña) y usa ajustes de enlace seguros para tu despliegue.

* ### Shared Docker VM runtime steps

Usa la guía compartida de entorno de ejecución para el flujo común de host Docker:

  * [Integrar los binarios requeridos en la imagen](</es/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Compilar e iniciar](</es/install/docker-vm-runtime#build-and-launch>)
  * [Qué persiste dónde](</es/install/docker-vm-runtime#what-persists-where>)
  * [Actualizaciones](</es/install/docker-vm-runtime#updates>)


* ### GCP-specific launch notes

En GCP, si la compilación falla con `Killed` o `exit code 137` durante `pnpm install --frozen-lockfile`, la VM se quedó sin memoria. Usa `e2-small` como mínimo, o `e2-medium` para primeras compilaciones más fiables.

Al enlazar a LAN (`OPENCLAW_GATEWAY_BIND=lan`), configura un origen de navegador de confianza antes de continuar:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Si cambiaste el puerto del gateway, reemplaza `18789` por tu puerto configurado.

* ### Access from your laptop

Crea un túnel SSH para reenviar el puerto del Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Ábrelo en tu navegador:

`http://127.0.0.1:18789/`

Vuelve a imprimir un enlace limpio al panel:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Si la interfaz solicita autenticación de secreto compartido, pega el token o la contraseña configurados en los ajustes de Control UI. Este flujo de Docker escribe un token por defecto; si cambias la configuración del contenedor a autenticación por contraseña, usa esa contraseña en su lugar.

Si Control UI muestra `unauthorized` o `disconnected (1008): pairing required`, aprueba el dispositivo del navegador:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

¿Necesitas de nuevo la referencia de persistencia compartida y actualización? Consulta [Entorno de ejecución de VM Docker](</es/install/docker-vm-runtime#what-persists-where>) y [actualizaciones del entorno de ejecución de VM Docker](</es/install/docker-vm-runtime#updates>).

* * *

## Solución de problemas

**Conexión SSH rechazada**

La propagación de claves SSH puede tardar 1-2 minutos después de crear la VM. Espera y vuelve a intentarlo.

**Problemas con OS Login**

Comprueba tu perfil de OS Login:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Asegúrate de que tu cuenta tenga los permisos de IAM requeridos (Compute OS Login o Compute OS Admin Login).

**Sin memoria (OOM)**

Si la compilación de Docker falla con `Killed` y `exit code 137`, la VM fue terminada por OOM. Actualiza a e2-small (mínimo) o e2-medium (recomendado para compilaciones locales fiables):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Cuentas de servicio (práctica recomendada de seguridad)

Para uso personal, tu cuenta de usuario predeterminada funciona bien.

Para automatización o pipelines de CI/CD, crea una cuenta de servicio dedicada con permisos mínimos:

  1. Crea una cuenta de servicio:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Concede el rol de administrador de instancias de Compute (o un rol personalizado más restringido):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Evita usar el rol de propietario para automatización. Usa el principio de privilegio mínimo.

Consulta <https://cloud.google.com/iam/docs/understanding-roles> para ver detalles de los roles de IAM.

* * *

## Próximos pasos

  * Configura canales de mensajería: [Canales](</es/channels>)
  * Empareja dispositivos locales como nodos: [Nodos](</es/nodes>)
  * Configura el Gateway: [Configuración del Gateway](</es/gateway/configuration>)


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Azure](</es/install/azure>)
  * [Alojamiento VPS](</es/vps>)


Was this useful?YesNo