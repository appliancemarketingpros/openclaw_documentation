---
title: Adaptadores RPC
source_url: https://docs.openclaw.ai/es/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw integra CLI externas mediante JSON-RPC. Hoy se utilizan dos patrones.

## Patrón A: demonio HTTP (signal-cli)

  * `signal-cli` se ejecuta como demonio con JSON-RPC sobre HTTP.
  * El flujo de eventos es SSE (`/api/v1/events`).
  * Sondeo de estado: `/api/v1/check`.
  * OpenClaw controla el ciclo de vida cuando `channels.signal.autoStart=true`.


Consulta [Signal](</es/channels/signal>) para la configuración y los puntos de conexión.

## Patrón B: proceso hijo stdio (imsg)

  * OpenClaw genera `imsg rpc` como proceso hijo para [iMessage](</es/channels/imessage>).
  * JSON-RPC está delimitado por líneas sobre stdin/stdout (un objeto JSON por línea).
  * No se requiere puerto TCP ni demonio.


Métodos principales utilizados:

  * `watch.subscribe` → notificaciones (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (sondeo/diagnóstico)


Consulta [iMessage](</es/channels/imessage>) para la configuración heredada y el direccionamiento (`chat_id` preferido).

## Directrices para adaptadores

  * Gateway controla el proceso (inicio/detención vinculados al ciclo de vida del proveedor).
  * Mantén resilientes los clientes RPC: tiempos de espera, reinicio al salir.
  * Prefiere IDs estables (por ejemplo, `chat_id`) en lugar de cadenas de visualización.


## Relacionado

  * [Protocolo de Gateway](</es/gateway/protocol>)


Was this useful?YesNo