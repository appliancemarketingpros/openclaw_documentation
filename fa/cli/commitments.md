---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/fa/cli/commitments
scraped_at: 2026-05-25
---

تعهدات پیگیری استنباط‌شده را فهرست و مدیریت کنید.

تعهدات، حافظه‌های پیگیری کوتاه‌عمر و اختیاری هستند که از زمینهٔ گفت‌وگو ساخته می‌شوند. برای راهنمای مفهومی، [تعهدات استنباط‌شده](</fa/concepts/commitments>) را ببینید.

بدون زیر‌دستور، `openclaw commitments` تعهدات در انتظار را فهرست می‌کند.

## استفاده

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## گزینه‌ها

  * `--all`: به‌جای فقط تعهدات در انتظار، همهٔ وضعیت‌ها را نشان می‌دهد.
  * `--agent <id>`: به یک شناسهٔ عامل محدود می‌کند.
  * `--status <status>`: بر اساس وضعیت فیلتر می‌کند. مقادیر: `pending`، `sent`، `dismissed`، `snoozed`، یا `expired`.
  * `--json`: خروجی JSON قابل خواندن برای ماشین تولید می‌کند.


## نمونه‌ها

فهرست کردن تعهدات در انتظار:

bashCopy code
[code]
    openclaw commitments
[/code]

فهرست کردن هر تعهد ذخیره‌شده:

bashCopy code
[code]
    openclaw commitments --all
[/code]

محدود کردن به یک عامل:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

پیدا کردن تعهدات به تعویق افتاده:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

رد کردن یک یا چند تعهد:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

صدور به‌صورت JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## خروجی

خروجی متنی شامل موارد زیر است:

  * شناسهٔ تعهد
  * وضعیت
  * نوع
  * زودترین زمان سررسید
  * دامنه
  * متن پیشنهادی برای پیگیری


خروجی JSON همچنین مسیر ذخیره‌گاه تعهد و رکوردهای کامل ذخیره‌شده را شامل می‌شود.

## مرتبط

  * [تعهدات استنباط‌شده](</fa/concepts/commitments>)
  * [نمای کلی حافظه](</fa/concepts/memory>)
  * [Heartbeat](</fa/gateway/heartbeat>)
  * [کارهای زمان‌بندی‌شده](</fa/automation/cron-jobs>)


Was this useful?YesNo