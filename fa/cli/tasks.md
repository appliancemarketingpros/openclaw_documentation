---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/fa/cli/tasks
scraped_at: 2026-05-25
---

وظایف پس‌زمینهٔ پایدار و وضعیت Task Flow را بررسی کنید. بدون زیرفرمان، `openclaw tasks` معادل `openclaw tasks list` است.

برای چرخهٔ حیات و مدل تحویل، [وظایف پس‌زمینه](</fa/automation/tasks>) را ببینید.

## استفاده

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## گزینه‌های ریشه

  * `--json`: خروجی JSON.
  * `--runtime <name>`: فیلتر بر اساس نوع: `subagent`، `acp`، `cron`، یا `cli`.
  * `--status <name>`: فیلتر بر اساس وضعیت: `queued`، `running`، `succeeded`، `failed`، `timed_out`، `cancelled`، یا `lost`.


## زیرفرمان‌ها

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

وظایف پس‌زمینهٔ ردیابی‌شده را از جدیدترین به قدیمی‌ترین فهرست می‌کند.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

یک وظیفه را بر اساس شناسهٔ وظیفه، شناسهٔ اجرا، یا کلید نشست نشان می‌دهد.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

سیاست اعلان را برای یک وظیفهٔ در حال اجرا تغییر می‌دهد.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

یک وظیفهٔ پس‌زمینهٔ در حال اجرا را لغو می‌کند.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

رکوردهای وظیفه و Task Flow را که کهنه، گم‌شده، دارای تحویل ناموفق، یا به‌شکلی دیگر ناسازگار هستند آشکار می‌کند. وظایف گم‌شده‌ای که تا `cleanupAfter` نگه داشته می‌شوند هشدار هستند؛ وظایف گم‌شدهٔ منقضی‌شده یا بدون مهر زمانی خطا هستند.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

همگام‌سازی وظیفه و Task Flow، ثبت مهر زمانی پاک‌سازی، هرس‌کردن، و پاک‌سازی رجیستری نشست اجرای Cron کهنه را پیش‌نمایش یا اعمال می‌کند. برای وظایف Cron، پیش از علامت‌گذاری یک وظیفهٔ فعال قدیمی به‌عنوان `lost`، همگام‌سازی از گزارش‌های اجرای ماندگار/وضعیت کار استفاده می‌کند؛ بنابراین اجراهای Cron تکمیل‌شده صرفاً به‌دلیل از بین رفتن وضعیت زمان اجرای درون‌حافظه‌ای Gateway به خطاهای حسابرسی کاذب تبدیل نمی‌شوند. حسابرسی آفلاین CLI برای مجموعهٔ کارهای فعال Cron محلیِ فرایند Gateway مرجع قطعی نیست. وظایف CLI دارای شناسهٔ اجرا/شناسهٔ منبع زمانی به‌عنوان `lost` علامت‌گذاری می‌شوند که زمینهٔ اجرای زندهٔ Gateway آن‌ها از بین رفته باشد، حتی اگر یک ردیف نشست فرزند قدیمی باقی مانده باشد. هنگام اعمال، نگه‌داری همچنین ردیف‌های رجیستری نشست `cron:<jobId>:run:<uuid>` قدیمی‌تر از ۷ روز را هرس می‌کند، در حالی که کارهای Cron در حال اجرا را حفظ می‌کند و ردیف‌های نشست غیر Cron را دست‌نخورده می‌گذارد.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

وضعیت پایدار Task Flow را زیر دفترکل وظیفه بررسی یا لغو می‌کند.

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [وظایف پس‌زمینه](</fa/automation/tasks>)


Was this useful?YesNo