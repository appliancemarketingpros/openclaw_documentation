---
title: SGLang
source_url: https://docs.openclaw.ai/fa/providers/sglang
scraped_at: 2026-05-25
---

SGLang مدل‌های open-weight را از طریق یک API HTTP سازگار با OpenAI ارائه می‌کند. OpenClaw با استفاده از خانوادهٔ ارائه‌دهندهٔ `openai-completions` و با کشف خودکار مدل‌های موجود به SGLang متصل می‌شود.

ویژگی | مقدار  
---|---  
شناسهٔ ارائه‌دهنده | `sglang`  
Plugin | همراه، `enabledByDefault: true`  
متغیر محیطی احراز هویت | `SGLANG_API_KEY` (اگر سرور احراز هویت ندارد، هر مقدار غیرخالی)  
پرچم راه‌اندازی اولیه | `--auth-choice sglang`  
API | سازگار با OpenAI (`openai-completions`)  
URL پایهٔ پیش‌فرض | `http://127.0.0.1:30000/v1`  
جای‌نگهدار مدل پیش‌فرض | `sglang/Qwen/Qwen3-8B`  
مصرف Streaming | بله (`supportsStreamingUsage: true`)  
قیمت‌گذاری | به‌عنوان external-free علامت‌گذاری شده است (`modelPricing.external: false`)  
  
OpenClaw همچنین وقتی با `SGLANG_API_KEY` اعلام آمادگی می‌کنید، مدل‌های موجود را از SGLang **به‌صورت خودکار کشف می‌کند**. وقتی یک URL پایهٔ سفارشی برای SGLang نیز پیکربندی می‌کنید، از `sglang/*` در `agents.defaults.models` استفاده کنید تا کشف مدل پویا بماند. بخش کشف مدل (ارائه‌دهندهٔ ضمنی) را در پایین ببینید.

## شروع کار

* ### SGLang را شروع کنید

SGLang را با یک سرور سازگار با OpenAI اجرا کنید. URL پایهٔ شما باید نقاط پایانی `/v1` را در دسترس قرار دهد (برای مثال `/v1/models` و `/v1/chat/completions`). SGLang معمولاً روی این نشانی اجرا می‌شود:

  * `http://127.0.0.1:30000/v1`


* ### یک کلید API تنظیم کنید

اگر روی سرور شما احراز هویت پیکربندی نشده باشد، هر مقداری کار می‌کند:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### راه‌اندازی اولیه را اجرا کنید یا مستقیماً یک مدل تنظیم کنید

bashCopy code
[code]
    openclaw onboard
[/code]

یا مدل را به‌صورت دستی پیکربندی کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## کشف مدل (ارائه‌دهندهٔ ضمنی)

وقتی `SGLANG_API_KEY` تنظیم شده باشد (یا یک پروفایل احراز هویت وجود داشته باشد) و شما `models.providers.sglang` را تعریف **نکرده باشید** ، OpenClaw این مورد را پرس‌وجو می‌کند:

  * `GET http://127.0.0.1:30000/v1/models`


و شناسه‌های بازگردانده‌شده را به ورودی‌های مدل تبدیل می‌کند.

## پیکربندی صریح (مدل‌های دستی)

در این موارد از پیکربندی صریح استفاده کنید:

  * SGLang روی میزبان/درگاه متفاوتی اجرا می‌شود.
  * می‌خواهید مقادیر `contextWindow`/`maxTokens` را ثابت کنید.
  * سرور شما به یک کلید API واقعی نیاز دارد (یا می‌خواهید سرآیندها را کنترل کنید).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## پیکربندی پیشرفته

رفتار سبک پروکسی

SGLang به‌عنوان یک backend سازگار با OpenAI و سبک پروکسی برای `/v1` در نظر گرفته می‌شود، نه یک نقطهٔ پایانی بومی OpenAI.

رفتار | SGLang  
---|---  
شکل‌دهی درخواست فقط مخصوص OpenAI | اعمال نمی‌شود  
`service_tier`، Responses `store`، راهنمایی‌های prompt-cache | ارسال نمی‌شود  
شکل‌دهی payload سازگار با reasoning | اعمال نمی‌شود  
سرآیندهای انتساب پنهان (`originator`، `version`، `User-Agent`) | روی URLهای پایهٔ سفارشی SGLang تزریق نمی‌شود  
عیب‌یابی

**سرور در دسترس نیست**

بررسی کنید سرور در حال اجراست و پاسخ می‌دهد:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**خطاهای احراز هویت**

اگر درخواست‌ها با خطاهای احراز هویت ناموفق می‌شوند، یک `SGLANG_API_KEY` واقعی تنظیم کنید که با پیکربندی سرور شما مطابقت داشته باشد، یا ارائه‌دهنده را صراحتاً زیر `models.providers.sglang` پیکربندی کنید.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهنده‌ها، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** طرح‌وارهٔ کامل پیکربندی شامل ورودی‌های ارائه‌دهنده. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo