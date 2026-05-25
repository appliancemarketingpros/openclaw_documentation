---
title: چیان‌فان
source_url: https://docs.openclaw.ai/fa/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan پلتفرم MaaS شرکت Baidu است که یک **API یکپارچه** فراهم می‌کند و درخواست‌ها را پشت یک نقطه پایانی و کلید API واحد به مدل‌های بسیاری هدایت می‌کند. این پلتفرم با OpenAI سازگار است، بنابراین بیشتر SDKهای OpenAI با تغییر URL پایه کار می‌کنند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `qianfan`  
احراز هویت | `QIANFAN_API_KEY`  
API | سازگار با OpenAI  
URL پایه | `https://qianfan.baidubce.com/v2`  
  
## شروع کار

* ### Create a Baidu Cloud account

در [کنسول Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) ثبت‌نام کنید یا وارد شوید و مطمئن شوید دسترسی Qianfan API برای شما فعال است.

* ### Generate an API key

یک برنامه جدید بسازید یا یک برنامه موجود را انتخاب کنید، سپس یک کلید API تولید کنید. قالب کلید `bce-v3/ALTAK-...` است.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## کاتالوگ داخلی

ارجاع مدل | ورودی | زمینه | بیشینه خروجی | استدلال | یادداشت‌ها  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | متن | 98,304 | 32,768 | بله | مدل پیش‌فرض  
`qianfan/ernie-5.0-thinking-preview` | متن، تصویر | 119,000 | 64,000 | بله | چندوجهی  
  
## نمونه پیکربندی

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport and compatibility

Qianfan از مسیر انتقال سازگار با OpenAI اجرا می‌شود، نه قالب‌دهی درخواست بومی OpenAI. یعنی قابلیت‌های استاندارد SDKهای OpenAI کار می‌کنند، اما ممکن است پارامترهای اختصاصی ارائه‌دهنده ارسال نشوند.

Catalog and overrides

کاتالوگ داخلی در حال حاضر شامل `deepseek-v3.2` و `ernie-5.0-thinking-preview` است. فقط زمانی `models.providers.qianfan` را اضافه یا بازنویسی کنید که به URL پایه سفارشی یا فراداده مدل نیاز داشته باشید.

Troubleshooting

  * مطمئن شوید کلید API شما با `bce-v3/ALTAK-` شروع می‌شود و دسترسی Qianfan API در کنسول Baidu Cloud برای آن فعال است.
  * اگر مدل‌ها فهرست نمی‌شوند، تأیید کنید سرویس Qianfan برای حساب شما فعال شده است.
  * URL پایه پیش‌فرض `https://qianfan.baidubce.com/v2` است. فقط زمانی آن را تغییر دهید که از نقطه پایانی یا پراکسی سفارشی استفاده می‌کنید.


## مرتبط

[**Model selection** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**Configuration reference** مرجع کامل پیکربندی OpenClaw. ](</fa/gateway/configuration-reference>) [**Agent setup** پیکربندی پیش‌فرض‌های agent و انتساب‌های مدل. ](</fa/concepts/agent>) [**Qianfan API docs** مستندات رسمی Qianfan API. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo