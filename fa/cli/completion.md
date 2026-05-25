---
title: تکمیل
source_url: https://docs.openclaw.ai/fa/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

اسکریپت‌های تکمیل پوسته را تولید کنید و در صورت تمایل آن‌ها را در نمایه پوسته خود نصب کنید.

## نحوه استفاده

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## گزینه‌ها

  * `-s, --shell <shell>`: پوسته هدف (`zsh`، `bash`، `powershell`، `fish`؛ پیش‌فرض: `zsh`)
  * `-i, --install`: نصب تکمیل با افزودن یک خط منبع به نمایه پوسته شما
  * `--write-state`: نوشتن اسکریپت(های) تکمیل در `$OPENCLAW_STATE_DIR/completions` بدون چاپ در خروجی استاندارد
  * `-y, --yes`: رد کردن اعلان‌های تأیید نصب


## یادداشت‌ها

  * `--install` یک بلوک کوچک «OpenClaw Completion» را در نمایه پوسته شما می‌نویسد و آن را به اسکریپت کش‌شده اشاره می‌دهد.
  * بدون `--install` یا `--write-state`، فرمان اسکریپت را در خروجی استاندارد چاپ می‌کند.
  * تولید تکمیل، درخت‌های فرمان را پیشاپیش بارگذاری می‌کند تا زیرفرمان‌های تودرتو نیز شامل شوند.


## مرتبط

  * [مرجع CLI](</fa/cli>)


Was this useful?YesNo