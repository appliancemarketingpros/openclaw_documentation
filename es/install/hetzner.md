---
title: Hetzner
source_url: https://docs.openclaw.ai/es/install/hetzner
scraped_at: 2026-05-25
---

## Objetivo

Ejecutar un OpenClaw Gateway persistente en un VPS de Hetzner usando Docker, con estado duradero, binarios integrados y comportamiento de reinicio seguro.

Si quieres "OpenClaw 24/7 por ~$5", esta es la configuración fiable más sencilla. Los precios de Hetzner cambian; elige el VPS Debian/Ubuntu más pequeño y escala si encuentras errores de falta de memoria.

Recordatorio del modelo de seguridad:

  * Los agentes compartidos por la empresa están bien cuando todos están dentro del mismo límite de confianza y el entorno de ejecución es solo empresarial.
  * Mantén una separación estricta: VPS/runtime dedicado + cuentas dedicadas; no perfiles personales de Apple/Google/navegador/gestor de contraseñas en ese host.
  * Si los usuarios son adversarios entre sí, sepáralos por Gateway/host/usuario del sistema operativo.


Consulta [Seguridad](</es/gateway/security>) y [Alojamiento de VPS](</es/vps>).

## ¿Qué estamos haciendo (en términos simples)?

  * Alquilar un pequeño servidor Linux (VPS de Hetzner)
  * Instalar Docker (runtime de app aislado)
  * Iniciar el OpenClaw Gateway en Docker
  * Persistir `~/.openclaw` \+ `~/.openclaw/workspace` en el host (sobrevive a reinicios/recompilaciones)
  * Acceder a la interfaz de control desde tu portátil mediante un túnel SSH


Ese estado montado de `~/.openclaw` incluye `openclaw.json`, por agente `agents/<agentId>/agent/auth-profiles.json` y `.env`.

Se puede acceder al Gateway mediante:

  * Reenvío de puertos SSH desde tu portátil
  * Exposición directa de puertos si gestionas tú mismo el firewall y los tokens


Esta guía presupone Ubuntu o Debian en Hetzner.  
Si estás en otro VPS Linux, adapta los paquetes según corresponda. Para el flujo genérico de Docker, consulta [Docker](</es/install/docker>).

* * *

## Ruta rápida (operadores con experiencia)

  1. Aprovisionar el VPS de Hetzner
  2. Instalar Docker
  3. Clonar el repositorio de OpenClaw
  4. Crear directorios persistentes en el host
  5. Configurar `.env` y `docker-compose.yml`
  6. Integrar los binarios requeridos en la imagen
  7. `docker compose up -d`
  8. Verificar la persistencia y el acceso al Gateway


* * *

## Qué necesitas

  * VPS de Hetzner con acceso root
  * Acceso SSH desde tu portátil
  * Comodidad básica con SSH + copiar/pegar
  * ~20 minutos
  * Docker y Docker Compose
  * Credenciales de autenticación del modelo
  * Credenciales opcionales de proveedores 
    * QR de WhatsApp
    * Token de bot de Telegram
    * OAuth de Gmail


* * *

* ### Aprovisionar el VPS

Crea un VPS Ubuntu o Debian en Hetzner.

Conéctate como root:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Esta guía presupone que el VPS es con estado. No lo trates como infraestructura desechable.

* ### Instalar Docker (en el VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Verifica:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clonar el repositorio de OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Esta guía presupone que compilarás una imagen personalizada para garantizar la persistencia de los binarios.

* ### Crear directorios persistentes en el host

Los contenedores Docker son efímeros. Todo estado de larga duración debe vivir en el host.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configurar variables de entorno

Crea `.env` en la raíz del repositorio.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Define `OPENCLAW_GATEWAY_TOKEN` cuando quieras gestionar el token estable del gateway mediante `.env`; de lo contrario, configura `gateway.auth.token` antes de depender de clientes entre reinicios. Si ninguna de las dos fuentes existe, OpenClaw usa un token solo de runtime para ese arranque. Genera una contraseña de llavero y pégala en `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**No confirmes este archivo en git.**

Este archivo `.env` es para env de contenedor/runtime, como `OPENCLAW_GATEWAY_TOKEN`. La autenticación OAuth/clave API de proveedores almacenada vive en el archivo montado `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Configuración de Docker Compose

Crea o actualiza `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` es solo para facilitar el arranque inicial, no sustituye una configuración de Gateway adecuada. Aun así, configura la autenticación (`gateway.auth.token` o contraseña) y usa ajustes de enlace seguros para tu despliegue.

* ### Pasos compartidos del runtime de VM Docker

Usa la guía de runtime compartido para el flujo común de host Docker:

  * [Integrar los binarios requeridos en la imagen](</es/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Compilar y lanzar](</es/install/docker-vm-runtime#build-and-launch>)
  * [Qué persiste y dónde](</es/install/docker-vm-runtime#what-persists-where>)
  * [Actualizaciones](</es/install/docker-vm-runtime#updates>)


* ### Acceso específico de Hetzner

Después de los pasos compartidos de compilación y lanzamiento, completa la siguiente configuración para abrir el túnel:

**Requisito previo:** Asegúrate de que la configuración de sshd de tu VPS permite el reenvío TCP. Si has reforzado tu configuración de SSH, revisa `/etc/ssh/sshd_config` y define:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` permite reenvíos locales `ssh -L` desde tu portátil y bloquea reenvíos remotos desde el servidor. Configurarlo en `no` hará que el túnel falle con: `channel 3: open failed: administratively prohibited: open failed`

Después de confirmar que el reenvío TCP está habilitado, reinicia el servicio SSH (`systemctl restart ssh`) y ejecuta el túnel desde tu portátil:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Abre:

`http://127.0.0.1:18789/`

Pega el secreto compartido configurado. Esta guía usa el token del gateway de forma predeterminada; si cambiaste a autenticación por contraseña, usa esa contraseña en su lugar.

El mapa de persistencia compartido está en [Runtime de VM Docker](</es/install/docker-vm-runtime#what-persists-where>).

## Infraestructura como código (Terraform)

Para equipos que prefieren flujos de trabajo de infraestructura como código, una configuración de Terraform mantenida por la comunidad proporciona:

  * Configuración modular de Terraform con gestión de estado remoto
  * Aprovisionamiento automatizado mediante cloud-init
  * Scripts de despliegue (bootstrap, despliegue, copia de seguridad/restauración)
  * Refuerzo de seguridad (firewall, UFW, acceso solo por SSH)
  * Configuración de túnel SSH para acceso al gateway


**Repositorios:**

  * Infraestructura: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Configuración de Docker: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Este enfoque complementa la configuración de Docker anterior con despliegues reproducibles, infraestructura versionada y recuperación automatizada ante desastres.

## Siguientes pasos

  * Configurar canales de mensajería: [Canales](</es/channels>)
  * Configurar el Gateway: [Configuración de Gateway](</es/gateway/configuration>)
  * Mantener OpenClaw actualizado: [Actualización](</es/install/updating>)


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Fly.io](</es/install/fly>)
  * [Docker](</es/install/docker>)
  * [Alojamiento de VPS](</es/vps>)


Was this useful?YesNo