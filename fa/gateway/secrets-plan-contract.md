---
title: قرارداد برنامهٔ اعمال رازها
source_url: https://docs.openclaw.ai/fa/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

این صفحه قرارداد سخت‌گیرانه‌ای را تعریف می‌کند که توسط `openclaw secrets apply` اعمال می‌شود.

اگر یک هدف با این قواعد مطابقت نداشته باشد، apply پیش از تغییر پیکربندی شکست می‌خورد.

## شکل فایل طرح

`openclaw secrets apply --from <plan.json>` انتظار یک آرایه `targets` از اهداف طرح را دارد:

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## دامنه هدف پشتیبانی‌شده

اهداف طرح برای مسیرهای اعتبارنامه پشتیبانی‌شده در موارد زیر پذیرفته می‌شوند:

  * [سطح اعتبارنامه SecretRef](</fa/reference/secretref-credential-surface>)


## رفتار نوع هدف

قاعده کلی:

  * `target.type` باید شناخته‌شده باشد و باید با شکل نرمال‌شده `target.path` مطابقت داشته باشد.


نام‌های مستعار سازگاری همچنان برای طرح‌های موجود پذیرفته می‌شوند:

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## قواعد اعتبارسنجی مسیر

هر هدف با همه موارد زیر اعتبارسنجی می‌شود:

  * `type` باید یک نوع هدف شناخته‌شده باشد.
  * `path` باید یک مسیر نقطه‌ای غیرخالی باشد.
  * `pathSegments` می‌تواند حذف شود. اگر ارائه شود، باید دقیقاً به همان مسیر `path` نرمال شود.
  * بخش‌های ممنوعه رد می‌شوند: `__proto__`، `prototype`، `constructor`.
  * مسیر نرمال‌شده باید با شکل مسیر ثبت‌شده برای نوع هدف مطابقت داشته باشد.
  * اگر `providerId` یا `accountId` تنظیم شده باشد، باید با شناسه کدگذاری‌شده در مسیر مطابقت داشته باشد.
  * اهداف `auth-profiles.json` به `agentId` نیاز دارند.
  * هنگام ایجاد نگاشت جدید `auth-profiles.json`، `authProfileProvider` را شامل کنید.


## رفتار شکست

اگر اعتبارسنجی یک هدف شکست بخورد، apply با خطایی مانند این خارج می‌شود:

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

برای یک طرح نامعتبر هیچ نوشتنی ثبت نمی‌شود.

## رفتار رضایت ارائه‌دهنده exec

  * `--dry-run` به‌طور پیش‌فرض بررسی‌های exec SecretRef را رد می‌کند.
  * طرح‌هایی که شامل SecretRefها/ارائه‌دهندگان exec هستند، در حالت نوشتن رد می‌شوند مگر اینکه `--allow-exec` تنظیم شده باشد.
  * هنگام اعتبارسنجی/اعمال طرح‌های حاوی exec، در هر دو فرمان dry-run و نوشتن، `--allow-exec` را ارسال کنید.


## نکات دامنه زمان اجرا و ممیزی

  * ورودی‌های فقط-ارجاع `auth-profiles.json` (`keyRef`/`tokenRef`) در حل‌وفصل زمان اجرا و پوشش ممیزی گنجانده می‌شوند.
  * `secrets apply` اهداف پشتیبانی‌شده `openclaw.json`، اهداف پشتیبانی‌شده `auth-profiles.json` و اهداف پاک‌سازی اختیاری را می‌نویسد.


## بررسی‌های اپراتور

bashCopy code
[code]
    # Validate plan without writesopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # Then apply for realopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json # For exec-containing plans, opt in explicitly in both modesopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

اگر apply با پیام مسیر هدف نامعتبر شکست خورد، طرح را با `openclaw secrets configure` دوباره تولید کنید یا مسیر هدف را به یکی از شکل‌های پشتیبانی‌شده بالا اصلاح کنید.

## مستندات مرتبط

  * [مدیریت اسرار](</fa/gateway/secrets>)
  * [CLI `secrets`](</fa/cli/secrets>)
  * [سطح اعتبارنامه SecretRef](</fa/reference/secretref-credential-surface>)
  * [مرجع پیکربندی](</fa/gateway/configuration-reference>)


Was this useful?YesNo