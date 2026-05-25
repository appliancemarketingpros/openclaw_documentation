---
title: Fireworks
source_url: https://docs.openclaw.ai/fa/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) مدل‌های open-weight و routed را از طریق API سازگار با OpenAI ارائه می‌کند. OpenClaw شامل یک Plugin ارائه‌دهنده Fireworks همراه است که با دو مدل Kimi از پیش فهرست‌شده عرضه می‌شود و در زمان اجرا هر مدل Fireworks یا شناسه router را می‌پذیرد.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `fireworks` (نام مستعار: `fireworks-ai`)  
Plugin | همراه، `enabledByDefault: true`  
متغیر محیطی احراز هویت | `FIREWORKS_API_KEY`  
فلگ راه‌اندازی اولیه | `--auth-choice fireworks-api-key`  
فلگ مستقیم CLI | `--fireworks-api-key <key>`  
API | سازگار با OpenAI (`openai-completions`)  
URL پایه | `https://api.fireworks.ai/inference/v1`  
مدل پیش‌فرض | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
نام مستعار پیش‌فرض | `Kimi K2.5 Turbo`  
  
## شروع به کار

* ### Set the Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

راه‌اندازی اولیه کلید را برای ارائه‌دهنده `fireworks` در پروفایل‌های احراز هویت شما ذخیره می‌کند و router مدل Kimi K2.5 Turbo **Fire Pass** را به‌عنوان مدل پیش‌فرض تنظیم می‌کند.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

فهرست باید شامل `Kimi K2.6` و `Kimi K2.5 Turbo (Fire Pass)` باشد. اگر `FIREWORKS_API_KEY` قابل حل نباشد، `openclaw models status --json` اعتبارنامه مفقود را زیر `auth.unusableProfiles` گزارش می‌کند.

## راه‌اندازی غیرتعاملی

برای نصب‌های اسکریپتی یا CI، همه چیز را در خط فرمان ارسال کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## فهرست داخلی

مرجع مدل | نام | ورودی | زمینه | حداکثر خروجی | تفکر  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | متن + تصویر | 262,144 | 262,144 | اجباراً خاموش  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | متن + تصویر | 256,000 | 256,000 | اجباراً خاموش (پیش‌فرض)  
  
## شناسه‌های مدل سفارشی Fireworks

OpenClaw هر مدل Fireworks یا شناسه router را در زمان اجرا می‌پذیرد. از شناسه دقیق نمایش‌داده‌شده توسط Fireworks استفاده کنید و پیشوند `fireworks/` را به آن اضافه کنید. حل پویای مدل، قالب Fire Pass را شبیه‌سازی می‌کند (ورودی متن + تصویر، API سازگار با OpenAI، هزینه پیش‌فرض صفر) و وقتی شناسه با الگوی Kimi مطابقت داشته باشد، تفکر را به‌صورت خودکار غیرفعال می‌کند.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

هر مرجع مدل Fireworks در OpenClaw با `fireworks/` شروع می‌شود و پس از آن شناسه دقیق یا مسیر router از پلتفرم Fireworks می‌آید. برای مثال:

  * مدل router: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * مدل مستقیم: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw هنگام ساخت درخواست API پیشوند `fireworks/` را حذف می‌کند و مسیر باقی‌مانده را به‌عنوان فیلد `model` سازگار با OpenAI به endpoint Fireworks می‌فرستد.

Why thinking is forced off for Kimi

اگر درخواست شامل پارامترهای `reasoning_*` باشد، Fireworks K2.6 خطای 400 برمی‌گرداند، حتی با اینکه Kimi از تفکر از طریق API خود Moonshot پشتیبانی می‌کند. سیاست همراه (`extensions/fireworks/thinking-policy.ts`) برای شناسه‌های مدل Kimi فقط سطح تفکر `off` را اعلام می‌کند، بنابراین سوییچ‌های دستی `/think` و سطح‌های سیاست ارائه‌دهنده با قرارداد زمان اجرا هم‌راستا می‌مانند.

برای استفاده سرتاسری از استدلال Kimi، [ارائه‌دهنده Moonshot](</fa/providers/moonshot>) را پیکربندی کنید و همان مدل را از طریق آن مسیریابی کنید.

Environment availability for the daemon

اگر Gateway به‌عنوان یک سرویس مدیریت‌شده اجرا شود (launchd، systemd، Docker)، کلید Fireworks باید برای همان فرایند قابل مشاهده باشد؛ نه فقط برای پوسته تعاملی شما.

در macOS، `openclaw gateway install` از قبل `~/.openclaw/.env` را به فایل محیط LaunchAgent متصل می‌کند. پس از چرخش کلید، نصب را دوباره اجرا کنید (یا `openclaw doctor --fix` را اجرا کنید).

## مرتبط

[**Model providers** انتخاب ارائه‌دهنده‌ها، مراجع مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**Thinking modes** سطح‌های `/think`، سیاست‌های ارائه‌دهنده، و مسیریابی مدل‌های دارای قابلیت استدلال. ](</fa/tools/thinking>) [**Moonshot** Kimi را با خروجی تفکر بومی از طریق API خود Moonshot اجرا کنید. ](</fa/providers/moonshot>) [**Troubleshooting** عیب‌یابی عمومی و پرسش‌های متداول. ](</fa/help/troubleshooting>)

Was this useful?YesNo