---
title: NVIDIA
source_url: https://docs.openclaw.ai/fa/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA یک API سازگار با OpenAI در `https://integrate.api.nvidia.com/v1` برای مدل‌های باز به‌صورت رایگان ارائه می‌دهد. با یک کلید API از [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) احراز هویت کنید.

## شروع به کار

* ### کلید API خود را دریافت کنید

یک کلید API در [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) بسازید.

* ### کلید را export کنید و راه‌اندازی اولیه را اجرا کنید

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### یک مدل NVIDIA تنظیم کنید

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

برای راه‌اندازی غیرتعاملی، می‌توانید کلید را مستقیماً هم ارسال کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## نمونهٔ پیکربندی

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## کاتالوگ داخلی

مرجع مدل | نام | بافت | بیشینهٔ خروجی  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## پیکربندی پیشرفته

رفتار فعال‌سازی خودکار

وقتی متغیر محیطی `NVIDIA_API_KEY` تنظیم شده باشد، ارائه‌دهنده به‌صورت خودکار فعال می‌شود. فراتر از کلید، هیچ پیکربندی صریحی برای ارائه‌دهنده لازم نیست.

کاتالوگ و قیمت‌گذاری

کاتالوگ همراه، ایستا است. از آنجا که NVIDIA در حال حاضر برای مدل‌های فهرست‌شده دسترسی رایگان به API ارائه می‌دهد، هزینه‌ها در منبع به‌صورت پیش‌فرض `0` هستند.

نقطهٔ پایانی سازگار با OpenAI

NVIDIA از نقطهٔ پایانی استاندارد تکمیل‌های `/v1` استفاده می‌کند. هر ابزار سازگار با OpenAI باید با URL پایهٔ NVIDIA بدون نیاز به تنظیمات اضافی کار کند.

پاسخ‌های کند ارائه‌دهندهٔ سفارشی

برخی مدل‌های سفارشی میزبانی‌شده توسط NVIDIA ممکن است پیش از انتشار نخستین قطعهٔ پاسخ، بیش از watchdog پیش‌فرض بیکاری مدل زمان ببرند. برای ورودی‌های ارائه‌دهندهٔ سفارشی NVIDIA، به‌جای افزایش timeout کل زمان اجرای عامل، timeout ارائه‌دهنده را افزایش دهید:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، مراجع مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** مرجع کامل پیکربندی برای عامل‌ها، مدل‌ها، و ارائه‌دهندگان. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo