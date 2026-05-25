---
title: حذف نصب
source_url: https://docs.openclaw.ai/fa/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

سرویس Gateway و داده‌های محلی را حذف نصب کنید (CLI باقی می‌ماند).

گزینه‌ها:

  * `--service`: سرویس Gateway را حذف کنید
  * `--state`: وضعیت و پیکربندی را حذف کنید
  * `--workspace`: دایرکتوری‌های فضای کاری را حذف کنید
  * `--app`: برنامه macOS را حذف کنید
  * `--all`: سرویس، وضعیت، فضای کاری و برنامه را حذف کنید
  * `--yes`: اعلان‌های تأیید را رد کنید
  * `--non-interactive`: اعلان‌ها را غیرفعال کنید؛ به `--yes` نیاز دارد
  * `--dry-run`: کنش‌ها را بدون حذف فایل‌ها چاپ کنید


نمونه‌ها:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

نکته‌ها:

  * اگر پیش از حذف وضعیت یا فضاهای کاری، یک اسنپ‌شات قابل بازیابی می‌خواهید، ابتدا `openclaw backup create` را اجرا کنید.
  * `--all` میانبری برای حذف هم‌زمان سرویس، وضعیت، فضای کاری و برنامه است.
  * `--non-interactive` به `--yes` نیاز دارد.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [حذف نصب](</fa/install/uninstall>)


Was this useful?YesNo