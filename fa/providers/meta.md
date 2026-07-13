---
title: فراداده
source_url: https://docs.openclaw.ai/fa/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** برای مدل استدلالی `muse-spark-1.1` از **Responses API** سازگار با OpenAI (`POST /v1/responses`) استفاده می‌کند. ارائه‌دهنده به‌صورت یک Plugin همراه OpenClaw عرضه می‌شود.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `meta`  
Plugin | ارائه‌دهنده همراه  
متغیر محیطی احراز هویت | `MODEL_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice meta-api-key`  
پرچم مستقیم CLI | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
نشانی پایه | `https://api.meta.ai/v1`  
مدل پیش‌فرض | `meta/muse-spark-1.1`  
استدلال پیش‌فرض | `high` (`reasoning.effort`)  
  
## شروع به کار

* ### تنظیم کلید API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### بررسی دردسترس‌بودن مدل‌ها

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

مدخل ایستای `muse-spark-1.1` را در فهرست مدل‌ها نمایش می‌دهد. اگر `MODEL_API_KEY` قابل تشخیص نباشد، `openclaw models status --json` اعتبارنامه مفقود را در `auth.unusableProfiles` گزارش می‌کند.

## راه‌اندازی غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## فهرست داخلی

مرجع مدل | نام | استدلال | پنجره زمینه | حداکثر خروجی  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | بله | 1,048,576 | 131,072  
  
قابلیت‌ها:

  * ورودی متن و تصویر
  * فراخوانی ابزار و پخش جریانی
  * میزان تلاش استدلالی: `minimal`، `low`، `medium`، `high`، `xhigh` (پیش‌فرض: `high`)
  * بازپخش استدلال رمزگذاری‌شده بدون حالت (`store: false`، `include: ["reasoning.encrypted_content"]`)


## پیکربندی دستی

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## آزمون دود

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

آزمون‌های زنده، `muse-spark-1.1` را در برابر `POST /v1/responses` اجرا می‌کنند.

## مطالب مرتبط

[**ارائه‌دهندگان مدل** انتخاب ارائه‌دهندگان، مراجع مدل و رفتار جایگزینی هنگام خرابی. ](</fa/concepts/model-providers>) [**حالت‌های تفکر** سطوح تلاش استدلالی برای muse-spark-1.1. ](</fa/tools/thinking>) [**مرجع پیکربندی** تنظیمات پیش‌فرض عامل و پیکربندی مدل. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue