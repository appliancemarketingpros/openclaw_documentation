---
title: پوشه
source_url: https://docs.openclaw.ai/fa/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

جست‌وجوهای دایرکتوری برای کانال‌هایی که از آن پشتیبانی می‌کنند (مخاطبان/همتاها، گروه‌ها، و «من»).

## پرچم‌های رایج

  * `--channel <name>`: شناسه/نام مستعار کانال (وقتی چند کانال پیکربندی شده باشند الزامی است؛ وقتی فقط یک کانال پیکربندی شده باشد خودکار است)
  * `--account <id>`: شناسه حساب (پیش‌فرض: پیش‌فرض کانال)
  * `--json`: خروجی JSON


## نکات

  * `directory` برای کمک به یافتن شناسه‌هایی است که می‌توانید در فرمان‌های دیگر جای‌گذاری کنید (به‌ویژه `openclaw message send --target ...`).
  * برای بسیاری از کانال‌ها، نتایج به‌جای دایرکتوری زنده ارائه‌دهنده، مبتنی بر پیکربندی هستند (فهرست‌های مجاز / گروه‌های پیکربندی‌شده).
  * Pluginهای کانال نصب‌شده همچنان می‌توانند پشتیبانی از دایرکتوری را حذف کنند؛ در این حالت، فرمان به‌جای نصب دوباره Plugin، عملیات دایرکتوری پشتیبانی‌نشده را گزارش می‌کند.
  * خروجی پیش‌فرض `id` (و گاهی `name`) است که با یک تب جدا شده‌اند؛ برای اسکریپت‌نویسی از `--json` استفاده کنید.


## استفاده از نتایج با `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## قالب‌های شناسه (بر اساس کانال)

  * WhatsApp: `+15551234567` (DM)، `1234567890-1234567890@g.us` (گروه)، `120363123456789@newsletter` (هدف خروجی Channel/Newsletter)
  * Telegram: `@username` یا شناسه عددی گفت‌وگو؛ گروه‌ها شناسه‌های عددی هستند
  * Slack: `user:U…` و `channel:C…`
  * Discord: `user:<id>` و `channel:<id>`
  * Matrix (Plugin): `user:@user:server`، `room:!roomId:server`، یا `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` و `conversation:<id>`
  * Zalo (Plugin): شناسه کاربر (Bot API)
  * Zalo Personal / `zalouser` (Plugin): شناسه رشته گفت‌وگو (DM/گروه) از `zca` (`me`، `friend list`، `group list`)


## خود («من»)

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## همتاها (مخاطبان/کاربران)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## گروه‌ها

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)


Was this useful?YesNo