---
title: Railway
source_url: https://docs.openclaw.ai/es/install/railway
scraped_at: 2026-05-25
---

# Railway

Despliega OpenClaw en Railway con una plantilla de un clic y accede a él a través de la Control UI web. Esta es la ruta más fácil de “sin terminal en el servidor”: Railway ejecuta el Gateway por ti.

## Lista rápida de comprobación (usuarios nuevos)

  1. Haz clic en **Deploy on Railway** (abajo).
  2. Añade un **Volume** montado en `/data`.
  3. Establece las **Variables** requeridas (al menos `OPENCLAW_GATEWAY_PORT` y `OPENCLAW_GATEWAY_TOKEN`).
  4. Habilita **HTTP Proxy** en el puerto `8080`.
  5. Abre `https://<your-railway-domain>/openclaw` y conéctate usando el secreto compartido configurado. Esta plantilla usa `OPENCLAW_GATEWAY_TOKEN` de forma predeterminada; si lo sustituyes por autenticación con contraseña, usa esa contraseña en su lugar.


## Despliegue con un clic

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Después del despliegue, encuentra tu URL pública en **Railway → tu servicio → Settings → Domains**.

Railway hará una de estas dos cosas:

  * te dará un dominio generado (a menudo `https://<something>.up.railway.app`), o
  * usará tu dominio personalizado si has añadido uno.


Luego abre:

  * `https://<your-railway-domain>/openclaw` — Control UI


## Qué obtienes

  * Gateway de OpenClaw alojado + Control UI
  * Almacenamiento persistente mediante Railway Volume (`/data`) para que `openclaw.json`, `auth-profiles.json` por agente, el estado de canales/proveedores, las sesiones y el espacio de trabajo sobrevivan a los redespliegues


## Ajustes obligatorios de Railway

### Redes públicas

Habilita **HTTP Proxy** para el servicio.

  * Puerto: `8080`


### Volume (obligatorio)

Adjunta un volumen montado en:

  * `/data`


### Variables

Establece estas variables en el servicio:

  * `OPENCLAW_GATEWAY_PORT=8080` (obligatorio: debe coincidir con el puerto de Redes públicas)
  * `OPENCLAW_GATEWAY_TOKEN` (obligatorio; trátalo como un secreto de administrador)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (recomendado)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (recomendado)


## Conectar un canal

Usa la Control UI en `/openclaw` o ejecuta `openclaw onboard` mediante el shell de Railway para ver instrucciones de configuración de canales:

  * [Telegram](</es/channels/telegram>) (el más rápido: solo un token de bot)
  * [Discord](</es/channels/discord>)
  * [Todos los canales](</es/channels>)


## Copias de seguridad y migración

Exporta tu estado, configuración, perfiles de autenticación y espacio de trabajo:

bashCopy code
[code]
    openclaw backup create
[/code]

Esto crea un archivo portátil de copia de seguridad con el estado de OpenClaw más cualquier espacio de trabajo configurado. Consulta [Backup](</es/cli/backup>) para más detalles.

## Siguientes pasos

  * Configura canales de mensajería: [Canales](</es/channels>)
  * Configura el Gateway: [Configuración del Gateway](</es/gateway/configuration>)
  * Mantén OpenClaw actualizado: [Actualización](</es/install/updating>)


Was this useful?YesNo