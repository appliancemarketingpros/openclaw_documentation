---
title: توکن‌جوس
source_url: https://docs.openclaw.ai/fa/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` یک Plugin بسته‌بندی‌شدهٔ اختیاری است که نتایج پرنویز ابزارهای `exec` و `bash` را پس از اجرای فرمان فشرده می‌کند.

این ابزار `tool_result` بازگردانده‌شده را تغییر می‌دهد، نه خود فرمان را. Tokenjuice ورودی پوسته را بازنویسی نمی‌کند، فرمان‌ها را دوباره اجرا نمی‌کند، و کدهای خروج را تغییر نمی‌دهد.

امروز این قابلیت برای اجراهای تعبیه‌شدهٔ PI و ابزارهای پویای OpenClaw در هارنس app-server متعلق به Codex اعمال می‌شود. Tokenjuice به میان‌افزار نتیجهٔ ابزار OpenClaw متصل می‌شود و خروجی را پیش از بازگشت به نشست فعال هارنس کوتاه می‌کند.

## فعال‌سازی Plugin

مسیر سریع:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

معادل آن:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw از پیش این Plugin را همراه خود ارائه می‌کند. مرحلهٔ جداگانه‌ای برای `plugins install` یا `tokenjuice install openclaw` وجود ندارد.

اگر ترجیح می‌دهید پیکربندی را مستقیماً ویرایش کنید:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## tokenjuice چه چیزی را تغییر می‌دهد

  * نتایج پرنویز `exec` و `bash` را پیش از بازگرداندن به نشست فشرده می‌کند.
  * اجرای اصلی فرمان را دست‌نخورده نگه می‌دارد.
  * خواندن دقیق محتوای فایل و فرمان‌های دیگری را که tokenjuice باید خام رها کند حفظ می‌کند.
  * اختیاری باقی می‌ماند: اگر خروجی واژه‌به‌واژه را همه‌جا می‌خواهید، Plugin را غیرفعال کنید.


## تأیید کارکرد آن

  1. Plugin را فعال کنید.
  2. نشستی را آغاز کنید که بتواند `exec` را فراخوانی کند.
  3. یک فرمان پرنویز مانند `git status` را اجرا کنید.
  4. بررسی کنید که نتیجهٔ ابزار بازگردانده‌شده کوتاه‌تر و ساختاریافته‌تر از خروجی خام پوسته باشد.


## غیرفعال‌سازی Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

یا:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## مرتبط

  * [ابزار Exec](</fa/tools/exec>)
  * [سطوح تفکر](</fa/tools/thinking>)
  * [موتور زمینه](</fa/concepts/context-engine>)


Was this useful?YesNo