---
title: سامانه
source_url: https://docs.openclaw.ai/fa/cli/system
scraped_at: 2026-05-25
---

# `openclaw system`

ابزارهای کمکی سطح سیستم برای Gateway: در صف گذاشتن رویدادهای سیستمی، کنترل Heartbeatها، و مشاهده حضور.

همه زیر‌فرمان‌های `system` از Gateway RPC استفاده می‌کنند و پرچم‌های مشترک کلاینت را می‌پذیرند:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## فرمان‌های رایج

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

به‌طور پیش‌فرض، یک رویداد سیستمی را در نشست **اصلی** در صف قرار می‌دهد. Heartbeat بعدی آن را به‌صورت یک خط `System:` در اعلان تزریق می‌کند. برای اجرای فوری Heartbeat از `--mode now` استفاده کنید؛ `next-heartbeat` تا تیک زمان‌بندی‌شده بعدی منتظر می‌ماند.

برای هدف گرفتن یک نشست مشخص، `--session-key` را ارسال کنید (برای مثال برای بازگرداندن تکمیل یک وظیفه ناهمگام به کانالی که آن را شروع کرده است).

> **استثنای زمان‌بندی با`--session-key`:** وقتی `--session-key` ارائه شود، `--mode next-heartbeat` به‌جای انتظار برای تیک زمان‌بندی‌شده بعدی، به یک بیدارباش هدفمند فوری تبدیل می‌شود. بیدارباش‌های هدفمند از نیت Heartbeat `immediate` استفاده می‌کنند تا از دروازه هنوز-موعد-نرسیده اجراکننده عبور کنند؛ در غیر این صورت یک بیدارباش با نیت `event` به تعویق می‌افتاد (و عملاً حذف می‌شد). اگر تحویل با تأخیر می‌خواهید، `--session-key` را حذف کنید تا رویداد روی نشست اصلی قرار بگیرد و با Heartbeat منظم بعدی همراه شود.

پرچم‌ها:

  * `--text <text>`: متن رویداد سیستمی الزامی.
  * `--mode <mode>`: `now` یا `next-heartbeat` (پیش‌فرض).
  * `--session-key <sessionKey>`: اختیاری؛ یک نشست عامل مشخص را به‌جای نشست اصلی عامل هدف می‌گیرد. کلیدهایی که متعلق به عامل حل‌شده نباشند به نشست اصلی عامل بازمی‌گردند.
  * `--json`: خروجی قابل‌خواندن توسط ماشین.
  * `--url`، `--token`، `--timeout`، `--expect-final`: پرچم‌های مشترک Gateway RPC.


## `system heartbeat last|enable|disable`

کنترل‌های Heartbeat:

  * `last`: آخرین رویداد Heartbeat را نشان می‌دهد.
  * `enable`: Heartbeatها را دوباره روشن می‌کند (اگر غیرفعال شده بودند از این استفاده کنید).
  * `disable`: Heartbeatها را موقتاً متوقف می‌کند.


پرچم‌ها:

  * `--json`: خروجی قابل‌خواندن توسط ماشین.
  * `--url`، `--token`، `--timeout`، `--expect-final`: پرچم‌های مشترک Gateway RPC.


## `system presence`

ورودی‌های حضور سیستمی فعلی را که Gateway از آن‌ها آگاه است فهرست می‌کند (گره‌ها، نمونه‌ها، و خطوط وضعیت مشابه).

پرچم‌ها:

  * `--json`: خروجی قابل‌خواندن توسط ماشین.
  * `--url`، `--token`، `--timeout`، `--expect-final`: پرچم‌های مشترک Gateway RPC.


## نکته‌ها

  * به یک Gateway در حال اجرا نیاز دارد که از طریق پیکربندی فعلی شما قابل دسترسی باشد (محلی یا راه‌دور).
  * رویدادهای سیستمی گذرا هستند و در راه‌اندازی‌های مجدد پایدار نمی‌مانند.


## مرتبط

  * [مرجع CLI](</fa/cli>)


Was this useful?YesNo