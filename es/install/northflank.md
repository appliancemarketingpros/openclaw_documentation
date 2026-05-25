---
title: Northflank
source_url: https://docs.openclaw.ai/es/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Implementa OpenClaw en Northflank con una plantilla de un clic y accede a él a través de la Control UI web. Esta es la ruta más fácil de "sin terminal en el servidor": Northflank ejecuta el Gateway por ti.

## Cómo empezar

  1. Haz clic en [Implementar OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) para abrir la plantilla.
  2. Crea una [cuenta en Northflank](<https://app.northflank.com/signup>) si todavía no tienes una.
  3. Haz clic en **Deploy OpenClaw now**.
  4. Establece la variable de entorno requerida: `OPENCLAW_GATEWAY_TOKEN` (usa un valor aleatorio fuerte).
  5. Haz clic en **Deploy stack** para compilar y ejecutar la plantilla de OpenClaw.
  6. Espera a que finalice la implementación y luego haz clic en **View resources**.
  7. Abre el servicio de OpenClaw.
  8. Abre la URL pública de OpenClaw en `/openclaw` y conéctate usando el secreto compartido configurado. Esta plantilla usa `OPENCLAW_GATEWAY_TOKEN` de forma predeterminada; si lo sustituyes por autenticación con contraseña, usa esa contraseña en su lugar.


## Qué obtienes

  * Gateway de OpenClaw alojado + Control UI
  * Almacenamiento persistente mediante Northflank Volume (`/data`) para que `openclaw.json`, `auth-profiles.json` por agente, el estado de canales/proveedores, las sesiones y el espacio de trabajo sobrevivan a las reimplementaciones


## Conectar un canal

Usa la Control UI en `/openclaw` o ejecuta `openclaw onboard` mediante SSH para obtener instrucciones de configuración de canales:

  * [Telegram](</es/channels/telegram>) (el más rápido: solo un token de bot)
  * [Discord](</es/channels/discord>)
  * [Todos los canales](</es/channels>)


## Siguientes pasos

  * Configura canales de mensajería: [Canales](</es/channels>)
  * Configura el Gateway: [Configuración del Gateway](</es/gateway/configuration>)
  * Mantén OpenClaw actualizado: [Actualización](</es/install/updating>)


Was this useful?YesNo