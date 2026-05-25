---
title: راه‌اندازی
source_url: https://docs.openclaw.ai/fa/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

پیکربندی پایه و فضای کاری عامل را مقداردهی اولیه کنید. با وجود هر پرچم راه‌اندازی اولیه، جادوگر را نیز اجرا می‌کند.

## گزینه‌ها

پرچم | توضیح  
---|---  
`--workspace <dir>` | دایرکتوری فضای کاری عامل (پیش‌فرض `~/.openclaw/workspace`؛ به‌صورت `agents.defaults.workspace` ذخیره می‌شود).  
`--wizard` | راه‌اندازی اولیه تعاملی را اجرا کنید.  
`--non-interactive` | راه‌اندازی اولیه را بدون اعلان‌ها اجرا کنید.  
`--mode <mode>` | حالت راه‌اندازی اولیه: `local` یا `remote`.  
`--import-from <provider>` | ارائه‌دهنده مهاجرت برای اجرا در طول راه‌اندازی اولیه.  
`--import-source <path>` | خانه عامل منبع برای `--import-from`.  
`--import-secrets` | رازهای پشتیبانی‌شده را در طول مهاجرت راه‌اندازی اولیه وارد کنید.  
`--remote-url <url>` | URL WebSocket مربوط به Gateway راه‌دور.  
`--remote-token <token>` | توکن Gateway راه‌دور (اختیاری).  
  
### راه‌اندازی خودکار جادوگر

`openclaw setup` وقتی هرکدام از این پرچم‌ها صراحتا وجود داشته باشند، حتی بدون `--wizard`، جادوگر را اجرا می‌کند:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## نمونه‌ها

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## نکته‌ها

  * `openclaw setup` ساده، پیکربندی و فضای کاری را بدون اجرای جریان کامل راه‌اندازی اولیه مقداردهی اولیه می‌کند.
  * پس از setup ساده، برای مسیر هدایت‌شده کامل `openclaw onboard`، برای تغییرات هدفمند `openclaw configure`، یا برای افزودن حساب‌های کانال `openclaw channels add` را اجرا کنید.
  * اگر وضعیت Hermes شناسایی شود، راه‌اندازی اولیه تعاملی می‌تواند مهاجرت را به‌صورت خودکار پیشنهاد کند. راه‌اندازی اولیه واردسازی به یک setup تازه نیاز دارد؛ برای طرح‌های اجرای آزمایشی، پشتیبان‌گیری‌ها و حالت بازنویسی خارج از راه‌اندازی اولیه، از [مهاجرت](</fa/cli/migrate>) استفاده کنید.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [راه‌اندازی اولیه (CLI)](</fa/start/wizard>)
  * [شروع به کار](</fa/start/getting-started>)
  * [نمای کلی نصب](</fa/install>)


Was this useful?YesNo