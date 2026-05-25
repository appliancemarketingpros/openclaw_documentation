---
title: Adaptadores RPC
source_url: https://docs.openclaw.ai/pt-BR/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw integra CLIs externas via JSON-RPC. Dois padrões são usados hoje.

## Padrão A: daemon HTTP (signal-cli)

  * `signal-cli` é executado como um daemon com JSON-RPC sobre HTTP.
  * O fluxo de eventos é SSE (`/api/v1/events`).
  * Sonda de integridade: `/api/v1/check`.
  * OpenClaw controla o ciclo de vida quando `channels.signal.autoStart=true`.


Consulte [Signal](</pt-BR/channels/signal>) para configuração e endpoints.

## Padrão B: processo filho stdio (imsg)

  * OpenClaw inicia `imsg rpc` como um processo filho para [iMessage](</pt-BR/channels/imessage>).
  * JSON-RPC é delimitado por linhas sobre stdin/stdout (um objeto JSON por linha).
  * Sem porta TCP, sem daemon necessário.


Métodos principais usados:

  * `watch.subscribe` → notificações (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (sonda/diagnósticos)


Consulte [iMessage](</pt-BR/channels/imessage>) para configuração legada e endereçamento (`chat_id` preferencial).

## Diretrizes para adaptadores

  * Gateway controla o processo (início/parada vinculados ao ciclo de vida do provedor).
  * Mantenha os clientes RPC resilientes: timeouts, reiniciar ao sair.
  * Prefira IDs estáveis (por exemplo, `chat_id`) a strings de exibição.


## Relacionado

  * [Protocolo do Gateway](</pt-BR/gateway/protocol>)


Was this useful?YesNo