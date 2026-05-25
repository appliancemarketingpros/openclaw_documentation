---
title: Nodeها
source_url: https://docs.openclaw.ai/fa/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

گره‌های (دستگاه‌های) جفت‌شده را مدیریت کنید و قابلیت‌های گره را فراخوانی کنید.

مرتبط:

  * نمای کلی گره‌ها: [گره‌ها](</fa/nodes>)
  * دوربین: [گره‌های دوربین](</fa/nodes/camera>)
  * تصاویر: [گره‌های تصویر](</fa/nodes/images>)


گزینه‌های رایج:

  * `--url`، `--token`، `--timeout`، `--json`


## دستورهای رایج

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` جدول‌های در انتظار/جفت‌شده را چاپ می‌کند. ردیف‌های جفت‌شده شامل سن جدیدترین اتصال (آخرین اتصال) هستند. از `--connected` برای نمایش فقط گره‌های در حال حاضر متصل استفاده کنید. از `--last-connected <duration>` برای فیلتر کردن گره‌هایی استفاده کنید که در یک بازه زمانی متصل شده‌اند (مثلاً `24h`، `7d`). از `nodes remove --node <id|name|ip>` برای حذف رکورد قدیمی جفت‌سازی گره متعلق به Gateway استفاده کنید.

نکته تأیید:

  * `openclaw nodes pending` فقط به دامنه جفت‌سازی نیاز دارد.
  * `gateway.nodes.pairing.autoApproveCidrs` می‌تواند مرحله در انتظار را فقط برای جفت‌سازی دستگاه `role: node` که صراحتاً مورد اعتماد و برای نخستین بار است، رد کند. این گزینه به‌طور پیش‌فرض خاموش است و ارتقاها را تأیید نمی‌کند.
  * `openclaw nodes approve <requestId>` نیازمندی‌های دامنه اضافی را از درخواست در انتظار به ارث می‌برد: 
    * درخواست بدون دستور: فقط جفت‌سازی
    * دستورهای node غیر exec: جفت‌سازی + نوشتن
    * `system.run` / `system.run.prepare` / `system.which`: جفت‌سازی + مدیر


## فراخوانی

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

پرچم‌های فراخوانی:

  * `--params <json>`: رشته شیء JSON (پیش‌فرض `{}`).
  * `--invoke-timeout <ms>`: مهلت زمانی فراخوانی گره (پیش‌فرض `15000`).
  * `--idempotency-key <key>`: کلید اختیاری ایدمپوتنسی.
  * `system.run` و `system.run.prepare` اینجا مسدود شده‌اند؛ برای اجرای شل از ابزار `exec` با `host=node` استفاده کنید.


برای اجرای شل روی یک گره، به‌جای `openclaw nodes run` از ابزار `exec` با `host=node` استفاده کنید. CLI گره‌ها اکنون بر قابلیت‌ها متمرکز است: RPC مستقیم از طریق `nodes invoke`، به‌علاوه جفت‌سازی، دوربین، صفحه، مکان، Canvas، و اعلان‌ها. دستورهای Canvas توسط Plugin آزمایشی Canvas همراه پیاده‌سازی شده‌اند؛ هسته یک قلاب سازگاری نگه می‌دارد تا همچنان زیر `openclaw nodes canvas` باقی بمانند.

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [گره‌ها](</fa/nodes>)


Was this useful?YesNo