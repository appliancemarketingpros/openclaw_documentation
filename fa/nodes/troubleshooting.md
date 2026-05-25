---
title: عیب‌یابی Node
source_url: https://docs.openclaw.ai/fa/nodes/troubleshooting
scraped_at: 2026-05-25
---

از این صفحه زمانی استفاده کنید که یک گره در وضعیت دیده می‌شود اما ابزارهای گره با شکست مواجه می‌شوند.

## زنجیره فرمان‌ها

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

سپس بررسی‌های اختصاصی گره را اجرا کنید:

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>
[/code]

نشانه‌های سالم:

  * گره برای نقش `node` متصل و جفت‌سازی شده است.
  * `nodes describe` قابلیتی را که فراخوانی می‌کنید شامل می‌شود.
  * تأییدیه‌های اجرا حالت/فهرست مجاز مورد انتظار را نشان می‌دهند.


## الزامات پیش‌زمینه

`canvas.*`، `camera.*`، و `screen.*` فقط روی گره‌های iOS/Android در پیش‌زمینه در دسترس هستند.

بررسی و رفع سریع:

bashCopy code
[code]
    openclaw nodes describe --node <idOrNameOrIp>openclaw nodes canvas snapshot --node <idOrNameOrIp>openclaw logs --follow
[/code]

اگر `NODE_BACKGROUND_UNAVAILABLE` را دیدید، برنامه گره را به پیش‌زمینه بیاورید و دوباره تلاش کنید.

## ماتریس مجوزها

قابلیت | iOS | Android | برنامه گره macOS | کد خطای معمول  
---|---|---|---|---  
`camera.snap`, `camera.clip` | دوربین (+ میکروفون برای صدای کلیپ) | دوربین (+ میکروفون برای صدای کلیپ) | دوربین (+ میکروفون برای صدای کلیپ) | `*_PERMISSION_REQUIRED`  
`screen.record` | ضبط صفحه (+ میکروفون اختیاری) | اعلان ضبط صفحه (+ میکروفون اختیاری) | ضبط صفحه | `*_PERMISSION_REQUIRED`  
`location.get` | هنگام استفاده یا همیشه (بسته به حالت) | مکان پیش‌زمینه/پس‌زمینه بر اساس حالت | مجوز مکان | `LOCATION_PERMISSION_REQUIRED`  
`system.run` | ناموجود (مسیر میزبان گره) | ناموجود (مسیر میزبان گره) | تأییدیه‌های اجرا الزامی است | `SYSTEM_RUN_DENIED`  
  
## جفت‌سازی در برابر تأییدیه‌ها

این‌ها دروازه‌های متفاوتی هستند:

  1. **جفت‌سازی دستگاه** : آیا این گره می‌تواند به Gateway متصل شود؟
  2. **سیاست فرمان گره Gateway** : آیا شناسه فرمان RPC توسط `gateway.nodes.allowCommands` / `denyCommands` و پیش‌فرض‌های پلتفرم مجاز است؟
  3. **تأییدیه‌های اجرا** : آیا این گره می‌تواند یک فرمان شل مشخص را به‌صورت محلی اجرا کند؟


بررسی‌های سریع:

bashCopy code
[code]
    openclaw devices listopenclaw nodes statusopenclaw approvals get --node <idOrNameOrIp>openclaw approvals allowlist add --node <idOrNameOrIp> "/usr/bin/uname"
[/code]

اگر جفت‌سازی وجود ندارد، ابتدا دستگاه گره را تأیید کنید. اگر `nodes describe` فرمانی را ندارد، سیاست فرمان گره Gateway را بررسی کنید و همچنین بررسی کنید آیا گره هنگام اتصال واقعاً آن فرمان را اعلام کرده است یا نه. اگر جفت‌سازی درست است اما `system.run` شکست می‌خورد، تأییدیه‌ها/فهرست مجاز اجرای آن گره را اصلاح کنید.

جفت‌سازی گره یک دروازه هویت/اعتماد است، نه سطح تأیید برای هر فرمان. برای `system.run`، سیاست هر گره در فایل تأییدیه‌های اجرای همان گره قرار دارد (`openclaw approvals get --node ...`)، نه در رکورد جفت‌سازی Gateway.

برای اجراهای `host=node` که بر تأییدیه تکیه دارند، Gateway همچنین اجرا را به `systemRunPlan` متعارف آماده‌شده متصل می‌کند. اگر فراخواننده‌ای بعدی فرمان/cwd یا فراداده نشست را پیش از ارسال اجرای تأییدشده تغییر دهد، Gateway به‌جای اعتماد به محموله ویرایش‌شده، اجرا را به‌عنوان عدم تطابق تأییدیه رد می‌کند.

## کدهای خطای رایج گره

  * `NODE_BACKGROUND_UNAVAILABLE` → برنامه در پس‌زمینه است؛ آن را به پیش‌زمینه بیاورید.
  * `CAMERA_DISABLED` → کلید دوربین در تنظیمات گره غیرفعال است.
  * `*_PERMISSION_REQUIRED` → مجوز سیستم‌عامل وجود ندارد/رد شده است.
  * `LOCATION_DISABLED` → حالت مکان خاموش است.
  * `LOCATION_PERMISSION_REQUIRED` → حالت مکان درخواست‌شده اعطا نشده است.
  * `LOCATION_BACKGROUND_UNAVAILABLE` → برنامه در پس‌زمینه است اما فقط مجوز «هنگام استفاده» وجود دارد.
  * `SYSTEM_RUN_DENIED: approval required` → درخواست اجرا به تأیید صریح نیاز دارد.
  * `SYSTEM_RUN_DENIED: allowlist miss` → فرمان توسط حالت فهرست مجاز مسدود شده است. روی میزبان‌های گره Windows، شکل‌های پوشش شل مانند `cmd.exe /c ...` در حالت فهرست مجاز به‌عنوان موارد خارج از فهرست مجاز در نظر گرفته می‌شوند، مگر اینکه از طریق جریان پرسش تأیید شده باشند.


## چرخه بازیابی سریع

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --follow
[/code]

اگر هنوز گیر کرده‌اید:

  * جفت‌سازی دستگاه را دوباره تأیید کنید.
  * برنامه گره را دوباره باز کنید (پیش‌زمینه).
  * مجوزهای سیستم‌عامل را دوباره اعطا کنید.
  * سیاست تأیید اجرای فرمان را دوباره ایجاد/تنظیم کنید.


## مرتبط

  * [نمای کلی گره‌ها](</fa/nodes>)
  * [گره‌های دوربین](</fa/nodes/camera>)
  * [فرمان مکان](</fa/nodes/location-command>)
  * [تأییدیه‌های اجرا](</fa/tools/exec-approvals>)
  * [جفت‌سازی Gateway](</fa/gateway/pairing>)
  * [عیب‌یابی Gateway](</fa/gateway/troubleshooting>)
  * [عیب‌یابی کانال](</fa/channels/troubleshooting>)


Was this useful?YesNo