---
title: WhatsApp Plugin
source_url: https://docs.openclaw.ai/uk/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

Додає поверхню каналу WhatsApp для надсилання й отримання повідомлень OpenClaw.

## Розповсюдження

  * Package: `@openclaw/whatsapp`
  * Маршрут встановлення: npm; ClawHub


## Поверхня

channels: whatsapp

## Примітка щодо встановлення у Windows

У Windows Plugin WhatsApp потребує Git у `PATH` під час встановлення через npm, оскільки одну з його залежностей Baileys/libsignal отримують із git URL. Встановіть Git for Windows, потім перезапустіть оболонку й повторно запустіть встановлення:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git також працює, якщо його каталог `bin` є в `PATH`.

## Пов’язані документи

  * [whatsapp](</uk/channels/whatsapp>)


Was this useful?YesNo