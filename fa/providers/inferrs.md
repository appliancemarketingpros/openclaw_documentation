---
title: استنباط می‌کند
source_url: https://docs.openclaw.ai/fa/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) می‌تواند مدل‌های محلی را پشت یک API سازگار با OpenAI به نام `/v1` ارائه کند. OpenClaw از مسیر عمومی `openai-completions` با `inferrs` کار می‌کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `inferrs` (سفارشی؛ زیر `models.providers.inferrs` پیکربندی کنید)  
Plugin | هیچ‌کدام — `inferrs` یک provider plugin بسته‌بندی‌شده OpenClaw نیست  
متغیر محیط احراز هویت | اختیاری. اگر سرور inferrs شما احراز هویت نداشته باشد، هر مقداری کار می‌کند  
API | سازگار با OpenAI (`openai-completions`)  
URL پایه پیشنهادی | `http://127.0.0.1:8080/v1` (یا هر جایی که سرور inferrs شما قرار دارد)  
  
## شروع به کار

* ### اجرای inferrs با یک مدل

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### بررسی دسترس‌پذیر بودن سرور

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### افزودن ورودی provider برای OpenClaw

یک ورودی provider صریح اضافه کنید و مدل پیش‌فرض خود را به آن اشاره دهید. نمونه پیکربندی کامل را در پایین ببینید.

## نمونه پیکربندی کامل

این نمونه از Gemma 4 روی یک سرور محلی `inferrs` استفاده می‌کند.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## راه‌اندازی در زمان نیاز

Inferrs همچنین می‌تواند فقط زمانی توسط OpenClaw راه‌اندازی شود که یک مدل `inferrs/...` انتخاب شده باشد. `localService` را به همان ورودی provider اضافه کنید:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` باید مطلق باشد. روی میزبان Gateway از `which inferrs` استفاده کنید و آن مسیر را در پیکربندی قرار دهید. برای مرجع کامل فیلدها، [سرویس‌های مدل محلی](</fa/gateway/local-model-services>) را ببینید.

## پیکربندی پیشرفته

چرا requiresStringContent مهم است

برخی مسیرهای Chat Completions در `inferrs` فقط `messages[].content` رشته‌ای را می‌پذیرند، نه آرایه‌های ساختاریافته بخش‌های محتوا.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw پیش از ارسال درخواست، بخش‌های محتوای متنی خالص را به رشته‌های ساده تبدیل می‌کند.

نکته احتیاطی درباره Gemma و طرح‌واره ابزار

برخی ترکیب‌های فعلی `inferrs` \+ Gemma درخواست‌های مستقیم کوچک `/v1/chat/completions` را می‌پذیرند، اما همچنان در turnهای کامل agent-runtime OpenClaw شکست می‌خورند.

اگر چنین شد، ابتدا این را امتحان کنید:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

این کار سطح طرح‌واره ابزار OpenClaw را برای مدل غیرفعال می‌کند و می‌تواند فشار prompt را روی backendهای محلی سخت‌گیرتر کاهش دهد.

اگر درخواست‌های مستقیم بسیار کوچک همچنان کار می‌کنند اما turnهای عادی agent در OpenClaw داخل `inferrs` همچنان crash می‌کنند، مشکل باقی‌مانده معمولاً به رفتار مدل/سرور upstream مربوط است، نه لایه انتقال OpenClaw.

Smoke test دستی

پس از پیکربندی، هر دو لایه را آزمایش کنید:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

اگر فرمان اول کار کرد اما دومی شکست خورد، بخش عیب‌یابی زیر را بررسی کنید.

رفتار سبک proxy

با `inferrs` به‌عنوان یک backend سازگار با OpenAI به سبک proxy برای `/v1` رفتار می‌شود، نه یک endpoint بومی OpenAI.

  * شکل‌دهی درخواست مختص OpenAI بومی اینجا اعمال نمی‌شود
  * بدون `service_tier`، بدون Responses `store`، بدون راهنمایی‌های prompt-cache، و بدون شکل‌دهی payload سازگاری reasoning برای OpenAI
  * هدرهای انتساب پنهان OpenClaw (`originator`، `version`، `User-Agent`) روی URLهای پایه سفارشی `inferrs` تزریق نمی‌شوند


## عیب‌یابی

curl /v1/models شکست می‌خورد

`inferrs` اجرا نشده، در دسترس نیست، یا به host/port مورد انتظار bind نشده است. مطمئن شوید سرور راه‌اندازی شده و روی آدرسی که پیکربندی کرده‌اید در حال listen است.

messages[].content انتظار یک رشته دارد

در ورودی مدل `compat.requiresStringContent: true` را تنظیم کنید. برای جزئیات، بخش `requiresStringContent` در بالا را ببینید.

فراخوانی‌های مستقیم /v1/chat/completions موفق می‌شوند اما openclaw infer model run شکست می‌خورد

برای غیرفعال کردن سطح طرح‌واره ابزار، `compat.supportsTools: false` را تنظیم کنید. نکته احتیاطی طرح‌واره ابزار Gemma را در بالا ببینید.

inferrs همچنان در turnهای agent بزرگ‌تر crash می‌کند

اگر OpenClaw دیگر خطاهای schema دریافت نمی‌کند اما `inferrs` همچنان در turnهای agent بزرگ‌تر crash می‌کند، آن را محدودیت upstream در `inferrs` یا مدل در نظر بگیرید. فشار prompt را کاهش دهید یا به backend محلی یا مدل متفاوتی تغییر دهید.

## مرتبط

[**مدل‌های محلی** اجرای OpenClaw در برابر سرورهای مدل محلی. ](</fa/gateway/local-models>) [**سرویس‌های مدل محلی** راه‌اندازی سرورهای مدل محلی در زمان نیاز برای providerهای پیکربندی‌شده. ](</fa/gateway/local-model-services>) [**عیب‌یابی Gateway** اشکال‌زدایی backendهای محلی سازگار با OpenAI که probeها را با موفقیت می‌گذرانند اما اجرای agent در آن‌ها شکست می‌خورد. ](</fa/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**انتخاب مدل** نمای کلی همه providerها، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>)

Was this useful?YesNo