---
title: Adaptery RPC
source_url: https://docs.openclaw.ai/pl/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw integruje zewnętrzne CLI przez JSON-RPC. Obecnie używane są dwa wzorce.

## Wzorzec A: demon HTTP (signal-cli)

  * `signal-cli` działa jako demon z JSON-RPC przez HTTP.
  * Strumień zdarzeń to SSE (`/api/v1/events`).
  * Sonda kondycji: `/api/v1/check`.
  * OpenClaw zarządza cyklem życia, gdy `channels.signal.autoStart=true`.


Zobacz [Signal](</pl/channels/signal>), aby poznać konfigurację i punkty końcowe.

## Wzorzec B: proces potomny stdio (imsg)

  * OpenClaw uruchamia `imsg rpc` jako proces potomny dla [iMessage](</pl/channels/imessage>).
  * JSON-RPC jest rozdzielany wierszami przez stdin/stdout (jeden obiekt JSON na wiersz).
  * Nie jest wymagany port TCP ani demon.


Używane metody bazowe:

  * `watch.subscribe` → powiadomienia (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (sonda/diagnostyka)


Zobacz [iMessage](</pl/channels/imessage>), aby poznać starszą konfigurację i adresowanie (preferowane `chat_id`).

## Wytyczne dotyczące adapterów

  * Gateway zarządza procesem (uruchamianie/zatrzymywanie powiązane z cyklem życia dostawcy).
  * Dbaj o odporność klientów RPC: limity czasu, ponowne uruchamianie po zakończeniu.
  * Preferuj stabilne identyfikatory (np. `chat_id`) zamiast ciągów wyświetlanych.


## Powiązane

  * [Protokół Gateway](</pl/gateway/protocol>)


Was this useful?YesNo