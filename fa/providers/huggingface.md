---
title: Hugging Face (استنتاج)
source_url: https://docs.openclaw.ai/fa/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) تکمیل‌های گفت‌وگوی سازگار با OpenAI را از طریق یک API مسیریاب واحد ارائه می‌کند. با یک توکن به مدل‌های زیادی (DeepSeek، Llama و موارد بیشتر) دسترسی می‌گیرید. OpenClaw از **نقطه پایانی سازگار با OpenAI** استفاده می‌کند (فقط تکمیل‌های گفت‌وگو)؛ برای تبدیل متن به تصویر، embeddings یا گفتار، مستقیماً از [کلاینت‌های استنتاج HF](<https://huggingface.co/docs/api-inference/quicktour>) استفاده کنید.

  * ارائه‌دهنده: `huggingface`
  * احراز هویت: `HUGGINGFACE_HUB_TOKEN` یا `HF_TOKEN` (توکن دقیق با **Make calls to Inference Providers**)
  * API: سازگار با OpenAI (`https://router.huggingface.co/v1`)
  * صورت‌حساب: یک توکن HF؛ [قیمت‌گذاری](<https://huggingface.co/docs/inference-providers/pricing>) نرخ‌های ارائه‌دهنده را همراه با یک سطح رایگان دنبال می‌کند.


## شروع به کار

* ### ایجاد یک توکن دقیق

به [توکن‌های تنظیمات Hugging Face](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) بروید و یک توکن دقیق جدید بسازید.

* ### اجرای راه‌اندازی اولیه

در فهرست کشویی ارائه‌دهنده، **Hugging Face** را انتخاب کنید، سپس هنگام درخواست، کلید API خود را وارد کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### انتخاب یک مدل پیش‌فرض

در فهرست کشویی **مدل پیش‌فرض Hugging Face** ، مدل مورد نظر خود را انتخاب کنید. وقتی توکن معتبر دارید، فهرست از Inference API بارگذاری می‌شود؛ در غیر این صورت یک فهرست داخلی نمایش داده می‌شود. انتخاب شما به‌عنوان مدل پیش‌فرض ذخیره می‌شود.

همچنین می‌توانید بعداً مدل پیش‌فرض را در پیکربندی تنظیم یا تغییر دهید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### بررسی در دسترس بودن مدل

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### راه‌اندازی غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

این کار `huggingface/deepseek-ai/DeepSeek-R1` را به‌عنوان مدل پیش‌فرض تنظیم می‌کند.

## شناسه‌های مدل

ارجاع‌های مدل از قالب `huggingface/<org>/<model>` استفاده می‌کنند (شناسه‌های سبک Hub). فهرست زیر از **GET** `https://router.huggingface.co/v1/models` گرفته شده است؛ کاتالوگ شما ممکن است موارد بیشتری داشته باشد.

مدل | ارجاع (با پیشوند `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## پیکربندی پیشرفته

کشف مدل و فهرست کشویی راه‌اندازی اولیه

OpenClaw مدل‌ها را با فراخوانی مستقیم **نقطه پایانی Inference** کشف می‌کند:

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(اختیاری: برای دریافت فهرست کامل، `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` یا `$HF_TOKEN` را ارسال کنید؛ برخی نقاط پایانی بدون احراز هویت زیرمجموعه‌ای را برمی‌گردانند.) پاسخ به سبک OpenAI است: `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

وقتی یک کلید API مربوط به Hugging Face را پیکربندی می‌کنید (از طریق راه‌اندازی اولیه، `HUGGINGFACE_HUB_TOKEN` یا `HF_TOKEN`)، OpenClaw از این GET برای کشف مدل‌های تکمیل گفت‌وگوی موجود استفاده می‌کند. هنگام **راه‌اندازی تعاملی** ، پس از وارد کردن توکن، یک فهرست کشویی **مدل پیش‌فرض Hugging Face** می‌بینید که از آن فهرست پر شده است (یا اگر درخواست ناموفق باشد، از کاتالوگ داخلی). در زمان اجرا (برای نمونه، هنگام شروع Gateway)، وقتی کلید موجود باشد، OpenClaw دوباره **GET** `https://router.huggingface.co/v1/models` را برای تازه‌سازی کاتالوگ فراخوانی می‌کند. این فهرست با یک کاتالوگ داخلی ادغام می‌شود (برای فراداده‌هایی مانند پنجره زمینه و هزینه). اگر درخواست ناموفق باشد یا هیچ کلیدی تنظیم نشده باشد، فقط از کاتالوگ داخلی استفاده می‌شود.

نام‌های مدل، نام‌های مستعار و پسوندهای سیاست

  * **نام از API:** وقتی API یکی از `name`، `title` یا `display_name` را برمی‌گرداند، نام نمایشی مدل از **GET /v1/models** تکمیل می‌شود؛ در غیر این صورت از شناسه مدل ساخته می‌شود (برای نمونه `deepseek-ai/DeepSeek-R1` به "DeepSeek R1" تبدیل می‌شود).
  * **بازنویسی نام نمایشی:** می‌توانید برای هر مدل در پیکربندی یک برچسب سفارشی تنظیم کنید تا در CLI و UI همان‌طور که می‌خواهید نمایش داده شود:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **پسوندهای سیاست:** مستندات و راهنماهای داخلی Hugging Face در OpenClaw در حال حاضر این دو پسوند را به‌عنوان گونه‌های سیاست داخلی در نظر می‌گیرند:

    * **`:fastest`** — بالاترین توان عملیاتی.
    * **`:cheapest`** — کمترین هزینه به ازای هر توکن خروجی.

می‌توانید این موارد را به‌عنوان ورودی‌های جداگانه در `models.providers.huggingface.models` اضافه کنید یا `model.primary` را همراه با پسوند تنظیم کنید. همچنین می‌توانید ترتیب ارائه‌دهنده پیش‌فرض خود را در [تنظیمات Inference Provider](<https://hf.co/settings/inference-providers>) تنظیم کنید (بدون پسوند = استفاده از همان ترتیب).

  * **ادغام پیکربندی:** ورودی‌های موجود در `models.providers.huggingface.models` (برای نمونه در `models.json`) هنگام ادغام پیکربندی حفظ می‌شوند. بنابراین هر `name`، `alias` یا گزینه مدل سفارشی که آنجا تنظیم کرده باشید حفظ می‌شود.


محیط و راه‌اندازی daemon

اگر Gateway به‌صورت daemon اجرا می‌شود (launchd/systemd)، مطمئن شوید `HUGGINGFACE_HUB_TOKEN` یا `HF_TOKEN` برای آن فرایند در دسترس است (برای نمونه در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

پیکربندی: DeepSeek R1 با جایگزین Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

پیکربندی: Qwen با گونه‌های ارزان‌ترین و سریع‌ترین json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

پیکربندی: DeepSeek + Llama + GPT-OSS با نام‌های مستعار json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

پیکربندی: چند Qwen و DeepSeek با پسوندهای سیاست json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## مرتبط

[**انتخاب مدل** نمای کلی همه ارائه‌دهندگان، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**انتخاب مدل** نحوه انتخاب و پیکربندی مدل‌ها. ](</fa/concepts/models>) [**مستندات Inference Providers** مستندات رسمی Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**پیکربندی** مرجع کامل پیکربندی. ](</fa/gateway/configuration>)

Was this useful?YesNo