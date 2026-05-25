---
title: RPC-адаптери
source_url: https://docs.openclaw.ai/uk/reference/rpc
scraped_at: 2026-05-25
---

OpenClaw інтегрує зовнішні CLI через JSON-RPC. Сьогодні використовуються два шаблони.

## Шаблон A: HTTP-демон (signal-cli)

  * `signal-cli` працює як демон із JSON-RPC через HTTP.
  * Потік подій — SSE (`/api/v1/events`).
  * Перевірка стану: `/api/v1/check`.
  * OpenClaw керує життєвим циклом, коли `channels.signal.autoStart=true`.


Див. [Signal](</uk/channels/signal>) для налаштування та кінцевих точок.

## Шаблон B: дочірній процес stdio (imsg)

  * OpenClaw запускає `imsg rpc` як дочірній процес для [iMessage](</uk/channels/imessage>).
  * JSON-RPC передається рядками через stdin/stdout (один JSON-об’єкт на рядок).
  * Порт TCP не потрібен, демон не потрібен.


Використовувані основні методи:

  * `watch.subscribe` → сповіщення (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (перевірка/діагностика)


Див. [iMessage](</uk/channels/imessage>) для застарілого налаштування та адресації (переважно `chat_id`).

## Рекомендації щодо адаптерів

  * Gateway керує процесом (запуск/зупинка прив’язані до життєвого циклу провайдера).
  * Забезпечуйте стійкість RPC-клієнтів: тайм-аути, перезапуск після завершення.
  * Віддавайте перевагу стабільним ідентифікаторам (наприклад, `chat_id`) замість рядків для відображення.


## Пов’язане

  * [Протокол Gateway](</uk/gateway/protocol>)


Was this useful?YesNo