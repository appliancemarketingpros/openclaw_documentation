---
title: RPC-адаптеры
source_url: https://docs.openclaw.ai/ru/reference/rpc
scraped_at: 2026-06-29
---

ReferenceRPC and API

OpenClaw интегрирует внешние CLI через JSON-RPC. Сегодня используются два шаблона.

## Шаблон A: HTTP-демон (signal-cli)

  * `signal-cli` запускается как демон с JSON-RPC поверх HTTP.
  * Поток событий — SSE (`/api/v1/events`).
  * Проверка работоспособности: `/api/v1/check`.
  * OpenClaw управляет жизненным циклом, когда `channels.signal.autoStart=true`.


См. [Signal](</ru/channels/signal>) для настройки и эндпоинтов.

## Шаблон B: дочерний процесс stdio (imsg)

  * OpenClaw запускает `imsg rpc` как дочерний процесс для [iMessage](</ru/channels/imessage>).
  * JSON-RPC передается построчно через stdin/stdout (по одному JSON-объекту на строку).
  * TCP-порт не нужен, демон не требуется.


Используемые основные методы:

  * `watch.subscribe` → уведомления (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (проверка/диагностика)


См. [iMessage](</ru/channels/imessage>) для устаревшей настройки и адресации (предпочтительно `chat_id`).

## Рекомендации по адаптерам

  * Gateway владеет процессом (запуск/остановка привязаны к жизненному циклу провайдера).
  * Делайте RPC-клиенты устойчивыми: тайм-ауты, перезапуск при завершении.
  * Предпочитайте стабильные идентификаторы (например, `chat_id`) отображаемым строкам.


## Связанное

  * [Протокол Gateway](</ru/gateway/protocol>)


Was this useful?YesNo

Open issue