---
title: مهايئات RPC
source_url: https://docs.openclaw.ai/ar/reference/rpc
scraped_at: 2026-05-25
---

يدمج OpenClaw أدوات CLI خارجية عبر JSON-RPC. يُستخدم نمطان حاليًا.

## النمط A: خدمة HTTP خفية (signal-cli)

  * يعمل `signal-cli` كخدمة خفية مع JSON-RPC عبر HTTP.
  * تدفق الأحداث هو SSE (`/api/v1/events`).
  * فحص الصحة: `/api/v1/check`.
  * يتحكم OpenClaw في دورة الحياة عندما تكون `channels.signal.autoStart=true`.


راجع [Signal](</ar/channels/signal>) للإعداد ونقاط النهاية.

## النمط B: عملية فرعية عبر stdio (imsg)

  * يشغّل OpenClaw الأمر `imsg rpc` كعملية فرعية لـ [iMessage](</ar/channels/imessage>).
  * يكون JSON-RPC محددًا بالأسطر عبر stdin/stdout (كائن JSON واحد لكل سطر).
  * لا يلزم منفذ TCP ولا خدمة خفية.


الطرق الأساسية المستخدمة:

  * `watch.subscribe` → إشعارات (`method: "message"`)
  * `watch.unsubscribe`
  * `send`
  * `chats.list` (فحص/تشخيصات)


راجع [iMessage](</ar/channels/imessage>) للإعداد القديم والعنونة (يُفضّل `chat_id`).

## إرشادات المحوّل

  * يتحكم Gateway في العملية (يرتبط البدء/الإيقاف بدورة حياة المزوّد).
  * اجعل عملاء RPC قادرين على الصمود: مهلات، وإعادة تشغيل عند الخروج.
  * فضّل المعرّفات المستقرة (مثل `chat_id`) على سلاسل العرض.


## ذو صلة

  * [بروتوكول Gateway](</ar/gateway/protocol>)


Was this useful?YesNo