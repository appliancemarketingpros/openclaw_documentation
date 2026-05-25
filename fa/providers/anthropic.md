---
title: Anthropic
source_url: https://docs.openclaw.ai/fa/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic خانواده مدل‌های **Claude** را می‌سازد. OpenClaw از دو مسیر احراز هویت پشتیبانی می‌کند:

  * **کلید API** — دسترسی مستقیم به API شرکت Anthropic با صورت‌حساب مبتنی بر مصرف (مدل‌های `anthropic/*`)
  * **Claude CLI** — استفاده مجدد از ورود موجود Claude CLI روی همان میزبان


## شروع به کار

### کلید API

**بهترین گزینه برای:** دسترسی استاندارد API و صورت‌حساب مبتنی بر مصرف.

* ### کلید API خود را دریافت کنید

یک کلید API در [کنسول Anthropic](<https://console.anthropic.com/>) بسازید.

* ### راه‌اندازی اولیه را اجرا کنید

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

یا کلید را مستقیما ارسال کنید:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### در دسترس بودن مدل را بررسی کنید

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### نمونه پیکربندی

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**بهترین گزینه برای:** استفاده مجدد از ورود موجود Claude CLI بدون کلید API جداگانه.

* ### مطمئن شوید Claude CLI نصب شده و وارد شده است

با این دستور بررسی کنید:

bashCopy code
[code]
    claude --version
[/code]

* ### راه‌اندازی اولیه را اجرا کنید

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw اعتبارنامه‌های موجود Claude CLI را شناسایی کرده و دوباره استفاده می‌کند.

* ### در دسترس بودن مدل را بررسی کنید

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### نمونه پیکربندی

ارجاع مدل متعارف Anthropic به‌همراه بازنویسی زمان اجرای CLI را ترجیح دهید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

ارجاع‌های مدل قدیمی `claude-cli/claude-opus-4-7` همچنان برای سازگاری کار می‌کنند، اما پیکربندی جدید باید انتخاب ارائه‌دهنده/مدل را به‌صورت `anthropic/*` نگه دارد و backend اجرا را در سیاست زمان اجرای ارائه‌دهنده/مدل قرار دهد.

## پیش‌فرض‌های تفکر (Claude 4.6)

مدل‌های Claude 4.6 وقتی سطح تفکر صریحی تنظیم نشده باشد، در OpenClaw به‌طور پیش‌فرض از تفکر `adaptive` استفاده می‌کنند.

برای هر پیام با `/think:<level>` یا در پارامترهای مدل بازنویسی کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## کش کردن پرامپت

OpenClaw از قابلیت کش کردن پرامپت Anthropic برای احراز هویت با کلید API پشتیبانی می‌کند.

مقدار | مدت نگهداری کش | توضیح  
---|---|---  
`"short"` (پیش‌فرض) | 5 دقیقه | به‌طور خودکار برای احراز هویت با کلید API اعمال می‌شود  
`"long"` | 1 ساعت | کش طولانی‌تر  
`"none"` | بدون کش | غیرفعال کردن کش کردن پرامپت  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

بازنویسی‌های کش برای هر عامل

از پارامترهای سطح مدل به‌عنوان مبنا استفاده کنید، سپس عامل‌های مشخص را از طریق `agents.list[].params` بازنویسی کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

ترتیب ادغام پیکربندی:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (مطابق با `id`، بازنویسی بر اساس کلید)


این امکان را می‌دهد که یک عامل کش طولانی‌مدت را نگه دارد، در حالی که عامل دیگری روی همان مدل، کش را برای ترافیک جهشی/کم‌استفاده مجدد غیرفعال کند.

نکات Bedrock Claude

  * مدل‌های Anthropic Claude روی Bedrock (`amazon-bedrock/*anthropic.claude*`) هنگام پیکربندی، عبور مستقیم `cacheRetention` را می‌پذیرند.
  * مدل‌های غیر Anthropic در Bedrock در زمان اجرا به `cacheRetention: "none"` مجبور می‌شوند.
  * پیش‌فرض‌های هوشمند کلید API همچنین وقتی مقدار صریحی تنظیم نشده باشد، برای ارجاع‌های Claude-on-Bedrock مقدار `cacheRetention: "short"` را مقداردهی اولیه می‌کنند.


## پیکربندی پیشرفته

حالت سریع

کلید مشترک `/fast` در OpenClaw از ترافیک مستقیم Anthropic (کلید API و OAuth به `api.anthropic.com`) پشتیبانی می‌کند.

دستور | نگاشت به  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

درک رسانه (تصویر و PDF)

Plugin بسته‌بندی‌شده Anthropic، درک تصویر و PDF را ثبت می‌کند. OpenClaw قابلیت‌های رسانه را به‌طور خودکار از احراز هویت پیکربندی‌شده Anthropic حل می‌کند؛ نیازی به پیکربندی اضافی نیست.

ویژگی | مقدار  
---|---  
مدل پیش‌فرض | `claude-opus-4-7`  
ورودی پشتیبانی‌شده | تصاویر، اسناد PDF  
  
وقتی تصویر یا PDF به یک مکالمه پیوست می‌شود، OpenClaw آن را به‌طور خودکار از طریق ارائه‌دهنده درک رسانه Anthropic مسیریابی می‌کند.

پنجره زمینه 1M (بتا)

پنجره زمینه 1M شرکت Anthropic پشت دروازه بتا است. آن را برای هر مدل فعال کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw این را در درخواست‌ها به `anthropic-beta: context-1m-2025-08-07` نگاشت می‌کند.

`params.context1m: true` همچنین برای backend مربوط به Claude CLI (`claude-cli/*`) برای مدل‌های واجد شرایط Opus و Sonnet اعمال می‌شود و پنجره زمینه زمان اجرا را برای آن نشست‌های CLI گسترش می‌دهد تا با رفتار API مستقیم مطابقت داشته باشد.

زمینه 1M در Claude Opus 4.7

`anthropic/claude-opus-4.7` و گونه `claude-cli` آن به‌طور پیش‌فرض پنجره زمینه 1M دارند؛ نیازی به `params.context1m: true` نیست.

## عیب‌یابی

خطاهای 401 / توکن ناگهان نامعتبر شد

احراز هویت توکنی Anthropic منقضی می‌شود و می‌تواند لغو شود. برای راه‌اندازی‌های جدید، به‌جای آن از کلید API شرکت Anthropic استفاده کنید.

هیچ کلید API برای ارائه‌دهنده "anthropic" پیدا نشد

احراز هویت Anthropic **برای هر عامل جداگانه است** — عامل‌های جدید کلیدهای عامل اصلی را به ارث نمی‌برند. راه‌اندازی اولیه را برای آن عامل دوباره اجرا کنید (یا یک کلید API روی میزبان Gateway پیکربندی کنید)، سپس با `openclaw models status` بررسی کنید.

هیچ اعتبارنامه‌ای برای پروفایل "anthropic:default" پیدا نشد

`openclaw models status` را اجرا کنید تا ببینید کدام پروفایل احراز هویت فعال است. راه‌اندازی اولیه را دوباره اجرا کنید، یا یک کلید API برای مسیر آن پروفایل پیکربندی کنید.

هیچ پروفایل احراز هویتی در دسترس نیست (همه در دوره انتظار هستند)

`openclaw models status --json` را برای `auth.unusableProfiles` بررسی کنید. دوره‌های انتظار محدودیت نرخ Anthropic می‌توانند در سطح مدل باشند، بنابراین ممکن است یک مدل خواهر Anthropic همچنان قابل استفاده باشد. یک پروفایل Anthropic دیگر اضافه کنید یا تا پایان دوره انتظار صبر کنید.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهنده‌ها، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**backendهای CLI** جزئیات راه‌اندازی backend مربوط به Claude CLI و زمان اجرا. ](</fa/gateway/cli-backends>) [**کش کردن پرامپت** نحوه کار کش کردن پرامپت در میان ارائه‌دهنده‌ها. ](</fa/reference/prompt-caching>) [**OAuth و احراز هویت** جزئیات احراز هویت و قواعد استفاده مجدد از اعتبارنامه. ](</fa/gateway/authentication>)

Was this useful?YesNo