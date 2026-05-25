---
title: پرچم‌های عیب‌یابی
source_url: https://docs.openclaw.ai/fa/diagnostics/flags
scraped_at: 2026-05-25
---

پرچم‌های عیب‌یابی به شما امکان می‌دهند لاگ‌های اشکال‌زدایی هدفمند را بدون فعال کردن لاگ‌گیری تفصیلی در همه‌جا فعال کنید. پرچم‌ها اختیاری‌اند و مگر اینکه یک زیرسامانه آن‌ها را بررسی کند، اثری ندارند.

## نحوه کار

  * پرچم‌ها رشته هستند (بدون حساسیت به بزرگی/کوچکی حروف).
  * می‌توانید پرچم‌ها را در پیکربندی یا از طریق یک بازنویسی env فعال کنید.
  * وایلدکارت‌ها پشتیبانی می‌شوند: 
    * `telegram.*` با `telegram.http` مطابقت دارد
    * `*` همه پرچم‌ها را فعال می‌کند


## فعال‌سازی از طریق پیکربندی

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

چند پرچم:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

پس از تغییر پرچم‌ها، Gateway را بازراه‌اندازی کنید.

## بازنویسی env (موردی)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

غیرفعال کردن همه پرچم‌ها:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## مصنوع‌های Timeline

پرچم `timeline` رویدادهای زمان‌بندی ساختاریافته راه‌اندازی و زمان اجرا را برای هارنس‌های QA خارجی می‌نویسد:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

همچنین می‌توانید آن را در پیکربندی فعال کنید:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

مسیر فایل timeline همچنان از `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH` می‌آید. وقتی `timeline` فقط از طریق پیکربندی فعال شده باشد، نخستین spanهای بارگذاری پیکربندی منتشر نمی‌شوند، چون OpenClaw هنوز پیکربندی را نخوانده است؛ spanهای بعدی راه‌اندازی از پرچم پیکربندی استفاده می‌کنند.

`OPENCLAW_DIAGNOSTICS=1`، `OPENCLAW_DIAGNOSTICS=all`، و `OPENCLAW_DIAGNOSTICS=*` نیز timeline را فعال می‌کنند، چون همه پرچم‌های عیب‌یابی را فعال می‌کنند. وقتی فقط مصنوع زمان‌بندی JSONL را می‌خواهید، `timeline` را ترجیح دهید.

رکوردهای Timeline از پوشش `openclaw.diagnostics.v1` استفاده می‌کنند. رویدادها می‌توانند شامل شناسه‌های پردازه، نام فازها، نام spanها، مدت‌زمان‌ها، شناسه‌های Plugin، تعداد وابستگی‌ها، نمونه‌های تاخیر حلقه رویداد، نام عملیات provider، وضعیت خروج فرایند فرزند، و نام‌ها/پیام‌های خطای راه‌اندازی باشند. فایل‌های timeline را به‌عنوان مصنوع‌های عیب‌یابی محلی در نظر بگیرید؛ پیش از اشتراک‌گذاری خارج از دستگاهتان آن‌ها را بازبینی کنید.

## محل لاگ‌ها

پرچم‌ها لاگ‌ها را در فایل لاگ عیب‌یابی استاندارد منتشر می‌کنند. به‌طور پیش‌فرض:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

اگر `logging.file` را تنظیم کرده‌اید، به‌جای آن از همان مسیر استفاده کنید. لاگ‌ها JSONL هستند (یک شیء JSON در هر خط). ویرایش اطلاعات حساس همچنان بر اساس `logging.redactSensitive` اعمال می‌شود.

## استخراج لاگ‌ها

جدیدترین فایل لاگ را انتخاب کنید:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

فیلتر کردن عیب‌یابی HTTP مربوط به Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

فیلتر کردن عیب‌یابی HTTP مربوط به Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

یا هنگام بازتولید مشکل، tail کنید:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

برای Gatewayهای راه دور، می‌توانید از `openclaw logs --follow` نیز استفاده کنید (به [/cli/logs](</fa/cli/logs>) مراجعه کنید).

## نکات

  * اگر `logging.level` بالاتر از `warn` تنظیم شده باشد، ممکن است این لاگ‌ها سرکوب شوند. مقدار پیش‌فرض `info` مناسب است.
  * `brave.http` نشانی‌های URL/پارامترهای query درخواست Brave Search، وضعیت/زمان‌بندی پاسخ، و رویدادهای برخورد/عدم برخورد/نوشتن cache را لاگ می‌کند. کلیدهای API یا بدنه پاسخ را لاگ نمی‌کند، اما queryهای جست‌وجو می‌توانند حساس باشند.
  * فعال گذاشتن پرچم‌ها ایمن است؛ آن‌ها فقط حجم لاگ را برای زیرسامانه مشخص تحت تاثیر قرار می‌دهند.
  * برای تغییر مقصدهای لاگ، سطح‌ها، و ویرایش اطلاعات حساس از [/logging](</fa/logging>) استفاده کنید.


## مرتبط

  * [عیب‌یابی Gateway](</fa/gateway/diagnostics>)
  * [رفع اشکال Gateway](</fa/gateway/troubleshooting>)


Was this useful?YesNo