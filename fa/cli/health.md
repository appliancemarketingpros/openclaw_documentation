---
title: سلامت
source_url: https://docs.openclaw.ai/fa/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

وضعیت سلامت را از Gateway در حال اجرا دریافت کنید.

## گزینه‌ها

پرچم | پیش‌فرض | توضیح  
---|---|---  
`--json` | `false` | به‌جای متن، JSON قابل‌خواندن توسط ماشین چاپ کنید.  
`--timeout <ms>` | `10000` | مهلت اتصال برحسب میلی‌ثانیه.  
`--verbose` | `false` | ثبت گزارش مفصل. یک بررسی زنده را اجباری می‌کند و خروجی هر عامل را گسترش می‌دهد.  
`--debug` | `false` | نام مستعار برای `--verbose`.  
  
نمونه‌ها:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

نکته‌ها:

  * دستور پیش‌فرض `openclaw health` از Gateway در حال اجرا، نمای وضعیت سلامت آن را درخواست می‌کند. وقتی Gateway از قبل یک نمای کش‌شده تازه داشته باشد، می‌تواند همان payload کش‌شده را برگرداند و در پس‌زمینه تازه‌سازی کند.
  * `--verbose` یک بررسی زنده را اجباری می‌کند، جزئیات اتصال Gateway را چاپ می‌کند، و خروجی قابل‌خواندن برای انسان را در همه حساب‌ها و عامل‌های پیکربندی‌شده گسترش می‌دهد.
  * وقتی چند عامل پیکربندی شده باشند، خروجی شامل مخزن‌های نشست برای هر عامل است.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [وضعیت سلامت Gateway](</fa/gateway/health>)


Was this useful?YesNo