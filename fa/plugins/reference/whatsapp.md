---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/fa/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

سطح کانال WhatsApp را برای ارسال و دریافت پیام‌های OpenClaw اضافه می‌کند.

## توزیع

  * بسته: `@openclaw/whatsapp`
  * مسیر نصب: npm؛ ClawHub


## سطح

channels: whatsapp

## نکته نصب در Windows

در Windows، Plugin WhatsApp هنگام نصب npm به Git در `PATH` نیاز دارد، زیرا یکی از وابستگی‌های Baileys/libsignal آن از یک URL مربوط به git دریافت می‌شود. Git for Windows را نصب کنید، سپس shell را دوباره راه‌اندازی کنید و نصب را دوباره اجرا کنید:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git نیز در صورتی کار می‌کند که دایرکتوری `bin` آن در `PATH` باشد.

## مستندات مرتبط

  * [whatsapp](</fa/channels/whatsapp>)


Was this useful?YesNo