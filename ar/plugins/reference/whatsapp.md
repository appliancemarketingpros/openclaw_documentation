---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/ar/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

يضيف سطح قناة WhatsApp لإرسال رسائل OpenClaw واستقبالها.

## التوزيع

  * الحزمة: `@openclaw/whatsapp`
  * مسار التثبيت: npm؛ ClawHub


## السطح

channels: whatsapp

## ملاحظة تثبيت Windows

على Windows، يحتاج WhatsApp Plugin إلى وجود Git في `PATH` أثناء تثبيت npm لأن إحدى تبعيات Baileys/libsignal الخاصة به تُجلب من عنوان URL خاص بـ git. ثبّت Git for Windows، ثم أعد تشغيل الصدفة وأعد تنفيذ التثبيت:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

يعمل Portable Git أيضًا إذا كان دليل `bin` الخاص به موجودًا في `PATH`.

## المستندات ذات الصلة

  * [whatsapp](</ar/channels/whatsapp>)


Was this useful?YesNo