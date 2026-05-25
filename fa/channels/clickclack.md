---
title: کلیک‌کلاک
source_url: https://docs.openclaw.ai/fa/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack، OpenClaw را از طریق توکن‌های بات درجه‌یک ClickClack به یک فضای کاری خودمیزبان ClickClack متصل می‌کند.

وقتی می‌خواهید یک عامل OpenClaw به‌عنوان کاربر بات ClickClack ظاهر شود، از این استفاده کنید. ClickClack از بات‌های سرویس مستقل و بات‌های متعلق به کاربر پشتیبانی می‌کند؛ بات‌های متعلق به کاربر یک `owner_user_id` نگه می‌دارند و فقط دامنه‌های توکنی را دریافت می‌کنند که شما اعطا می‌کنید.

## راه‌اندازی سریع

یک توکن بات در ClickClack ایجاد کنید:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

برای بات متعلق به کاربر، `--owner <user_id>` را اضافه کنید.

OpenClaw را پیکربندی کنید:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

سپس اجرا کنید:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## چند بات

هر حساب اتصال بی‌درنگ ClickClack خودش را باز می‌کند و از توکن بات خودش استفاده می‌کند.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` برای پاسخ‌های کوتاه بات مستقیماً از `api.runtime.llm.complete` استفاده می‌کند. وقتی یک حساب `agentId` را تنظیم می‌کند، OpenClaw به بیت اعتماد صریح `plugins.entries.clickclack.llm.allowAgentIdOverride` نیاز دارد تا Plugin بتواند تکمیل‌ها را برای آن عامل بات اجرا کند. اگر فقط از مسیر عامل پیش‌فرض استفاده می‌کنید، آن را خاموش نگه دارید.

## هدف‌ها

  * `channel:<name-or-id>` به یک کانال فضای کاری ارسال می‌کند. هدف‌های بدون پیشوند به‌طور پیش‌فرض `channel:` هستند.
  * `dm:<user_id>` یک گفت‌وگوی مستقیم با آن کاربر ایجاد می‌کند یا از گفت‌وگوی موجود استفاده می‌کند.
  * `thread:<message_id>` در یک رشته موجود پاسخ می‌دهد.


نمونه‌ها:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## مجوزها

دامنه‌های توکن ClickClack توسط API ClickClack اعمال می‌شوند.

  * `bot:read`: خواندن داده‌های فضای کاری/کانال/پیام/رشته/DM/بی‌درنگ/نمایه.
  * `bot:write`: `bot:read` به‌همراه پیام‌های کانال، پاسخ‌های رشته، DMها و بارگذاری‌ها.
  * `bot:admin`: `bot:write` به‌همراه ایجاد کانال.


OpenClaw برای گفت‌وگوی عادی عامل فقط به `bot:write` نیاز دارد.

## عیب‌یابی

  * `ClickClack is not configured`: مقدار `channels.clickclack.token` یا `CLICKCLACK_BOT_TOKEN` را تنظیم کنید.
  * `workspace not found`: مقدار `workspace` را به شناسه یا slug فضای کاری که ClickClack برمی‌گرداند تنظیم کنید.
  * پاسخی از ورودی‌ها نمی‌آید: تأیید کنید توکن دسترسی خواندن بی‌درنگ دارد و بات به پیام‌های خودش پاسخ نمی‌دهد.
  * ارسال‌های کانال ناموفق‌اند: بررسی کنید بات عضو فضای کاری است و `bot:write` دارد.


Was this useful?YesNo