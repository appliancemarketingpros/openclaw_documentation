---
title: بازنشانی
source_url: https://docs.openclaw.ai/fa/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

پیکربندی/وضعیت محلی را بازنشانی کنید (CLI نصب‌شده باقی می‌ماند).

گزینه‌ها:

  * `--scope <scope>`: `config`، `config+creds+sessions`، یا `full`
  * `--yes`: پیام‌های تأیید را رد کنید
  * `--non-interactive`: پیام‌ها را غیرفعال کنید؛ به `--scope` و `--yes` نیاز دارد
  * `--dry-run`: اقدام‌ها را بدون حذف فایل‌ها چاپ کنید


مثال‌ها:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

نکات:

  * اگر پیش از حذف وضعیت محلی یک نماگرفت قابل‌بازیابی می‌خواهید، ابتدا `openclaw backup create` را اجرا کنید.
  * اگر `--scope` را حذف کنید، `openclaw reset` از یک پیام تعاملی برای انتخاب آنچه باید حذف شود استفاده می‌کند.
  * `--non-interactive` فقط زمانی معتبر است که هر دو `--scope` و `--yes` تنظیم شده باشند.


## مرتبط

  * [مرجع CLI](</fa/cli>)


Was this useful?YesNo