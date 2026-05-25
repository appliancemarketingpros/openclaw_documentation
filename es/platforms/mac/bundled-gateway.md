---
title: Gateway en macOS
source_url: https://docs.openclaw.ai/es/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app ya no incluye Node/Bun ni el entorno de ejecución de Gateway. La app de macOS espera una instalación **externa** de la CLI `openclaw`, no inicia Gateway como proceso hijo y administra un servicio launchd por usuario para mantener Gateway en ejecución (o se conecta a un Gateway local existente si ya hay uno en ejecución).

## Instala la CLI (obligatorio para el modo local)

Node 24 es el entorno de ejecución predeterminado en Mac. Node 22 LTS, actualmente `22.16+`, sigue funcionando por compatibilidad. Luego instala `openclaw` globalmente:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

El botón **Instalar CLI** de la app de macOS ejecuta el mismo flujo de instalación global que la app usa internamente: prefiere npm primero, luego pnpm y luego bun si es el único gestor de paquetes detectado. Node sigue siendo el entorno de ejecución recomendado para Gateway.

## Launchd (Gateway como LaunchAgent)

Etiqueta:

  * `ai.openclaw.gateway` (o `ai.openclaw.<profile>`; el legado `com.openclaw.*` puede permanecer)


Ubicación del plist (por usuario):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (o `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Administrador:

  * La app de macOS es propietaria de la instalación/actualización de LaunchAgent en modo Local.
  * La CLI también puede instalarlo: `openclaw gateway install`.


Comportamiento:

  * "OpenClaw activo" habilita/deshabilita LaunchAgent.
  * Salir de la app **no** detiene el gateway (launchd lo mantiene activo).
  * Si ya hay un Gateway en ejecución en el puerto configurado, la app se conecta a él en lugar de iniciar uno nuevo.


Registro:

  * stdout/err de launchd: `/tmp/openclaw/openclaw-gateway.log`


## Compatibilidad de versiones

La app de macOS comprueba la versión de gateway con respecto a su propia versión. Si son incompatibles, actualiza la CLI global para que coincida con la versión de la app.

## Comprobación rápida

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Luego:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Relacionado

  * [app de macOS](</es/platforms/macos>)
  * [runbook de Gateway](</es/gateway>)


Was this useful?YesNo