---
title: جفت‌سازی
source_url: https://docs.openclaw.ai/fa/cli/pairing
scraped_at: 2026-05-25
---

# `openclaw pairing`

درخواست‌های جفت‌سازی پیام مستقیم را تأیید یا بررسی کنید (برای کانال‌هایی که از جفت‌سازی پشتیبانی می‌کنند).

مرتبط:

  * جریان جفت‌سازی: [جفت‌سازی](</fa/channels/pairing>)


## دستورها

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing list --channel telegram --account workopenclaw pairing list telegram --json openclaw pairing approve <code>openclaw pairing approve telegram <code>openclaw pairing approve --channel telegram --account work <code> --notify
[/code]

## `pairing list`

درخواست‌های جفت‌سازی در انتظار را برای یک کانال فهرست کنید.

گزینه‌ها:

  * `[channel]`: شناسه موقعیتی کانال
  * `--channel <channel>`: شناسه صریح کانال
  * `--account <accountId>`: شناسه حساب برای کانال‌های چندحسابی
  * `--json`: خروجی قابل خواندن برای ماشین


نکته‌ها:

  * اگر چند کانال دارای قابلیت جفت‌سازی پیکربندی شده باشند، باید کانالی را یا به‌صورت موقعیتی یا با `--channel` ارائه کنید.
  * کانال‌های افزونه مجاز هستند، به شرطی که شناسه کانال معتبر باشد.


## `pairing approve`

یک کد جفت‌سازی در انتظار را تأیید کنید و به آن فرستنده اجازه دهید.

نحوه استفاده:

  * `openclaw pairing approve <channel> <code>`
  * `openclaw pairing approve --channel <channel> <code>`
  * `openclaw pairing approve <code>` هنگامی که دقیقاً یک کانال دارای قابلیت جفت‌سازی پیکربندی شده باشد


گزینه‌ها:

  * `--channel <channel>`: شناسه صریح کانال
  * `--account <accountId>`: شناسه حساب برای کانال‌های چندحسابی
  * `--notify`: ارسال تأییدیه به درخواست‌کننده در همان کانال


راه‌اندازی اولیه مالک:

  * اگر هنگام تأیید یک کد جفت‌سازی، `commands.ownerAllowFrom` خالی باشد، OpenClaw فرستنده تأییدشده را نیز به‌عنوان مالک دستور ثبت می‌کند، با استفاده از یک ورودی دارای دامنه کانال مانند `telegram:123456789`.
  * این کار فقط اولین مالک را راه‌اندازی اولیه می‌کند. تأییدهای بعدی جفت‌سازی، `commands.ownerAllowFrom` را جایگزین یا گسترش نمی‌دهند.
  * مالک دستور، حساب اپراتور انسانی است که اجازه دارد دستورهای مخصوص مالک را اجرا کند و اقدامات خطرناکی مانند `/diagnostics`، `/export-trajectory`، `/config` و تأییدهای اجرا را تأیید کند.


## نکته‌ها

  * ورودی کانال: آن را به‌صورت موقعیتی (`pairing list telegram`) یا با `--channel <channel>` ارسال کنید.
  * `pairing list` از `--account <accountId>` برای کانال‌های چندحسابی پشتیبانی می‌کند.
  * `pairing approve` از `--account <accountId>` و `--notify` پشتیبانی می‌کند.
  * اگر فقط یک کانال دارای قابلیت جفت‌سازی پیکربندی شده باشد، `pairing approve <code>` مجاز است.
  * اگر پیش از وجود این راه‌اندازی اولیه، فرستنده‌ای را تأیید کرده‌اید، `openclaw doctor` را اجرا کنید؛ وقتی هیچ مالک دستوری پیکربندی نشده باشد هشدار می‌دهد و دستور `openclaw config set commands.ownerAllowFrom ...` را برای رفع آن نشان می‌دهد.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [جفت‌سازی کانال](</fa/channels/pairing>)


Was this useful?YesNo