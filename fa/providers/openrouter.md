---
title: OpenRouter
source_url: https://docs.openclaw.ai/fa/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter یک **API یکپارچه** فراهم می‌کند که درخواست‌ها را از طریق یک endpoint و کلید API واحد به مدل‌های زیادی هدایت می‌کند. این API با OpenAI سازگار است، بنابراین بیشتر SDKهای OpenAI با تغییر base URL کار می‌کنند.

## شروع کار

* ### دریافت کلید API

یک کلید API در [openrouter.ai/keys](<https://openrouter.ai/keys>) بسازید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (اختیاری) تغییر به یک مدل مشخص

راه‌اندازی اولیه به‌صورت پیش‌فرض از `openrouter/auto` استفاده می‌کند. بعدا یک مدل مشخص انتخاب کنید:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## نمونه پیکربندی

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## ارجاع‌های مدل

نمونه‌های fallback همراه:

ارجاع مدل | یادداشت‌ها  
---|---  
`openrouter/auto` | مسیریابی خودکار OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 از طریق MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 از طریق MoonshotAI  
  
## تولید تصویر

OpenRouter می‌تواند پشتوانه ابزار `image_generate` نیز باشد. از یک مدل تصویر OpenRouter زیر `agents.defaults.imageGenerationModel` استفاده کنید:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw درخواست‌های تصویر را با `modalities: ["image", "text"]` به API تصویر chat completions در OpenRouter ارسال می‌کند. مدل‌های تصویر Gemini اشاره‌های پشتیبانی‌شده `aspectRatio` و `resolution` را از طریق `image_config` در OpenRouter دریافت می‌کنند. برای مدل‌های تصویر کندتر OpenRouter از `agents.defaults.imageGenerationModel.timeoutMs` استفاده کنید؛ پارامتر `timeoutMs` هر فراخوانی در ابزار `image_generate` همچنان اولویت دارد.

## تولید ویدیو

OpenRouter می‌تواند از طریق API ناهمگام `/videos` خود پشتوانه ابزار `video_generate` نیز باشد. از یک مدل ویدیوی OpenRouter زیر `agents.defaults.videoGenerationModel` استفاده کنید:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw کارهای متن‌به‌ویدیو و تصویر‌به‌ویدیو را به OpenRouter ارسال می‌کند، `polling_url` بازگردانده‌شده را polling می‌کند و ویدیوی کامل‌شده را از `unsigned_urls` در OpenRouter یا endpoint مستندشده محتوای کار دانلود می‌کند. تصاویر مرجع به‌صورت پیش‌فرض به‌عنوان تصاویر فریم اول/آخر ارسال می‌شوند؛ تصاویر برچسب‌خورده با `reference_image` به‌عنوان ارجاع‌های ورودی OpenRouter ارسال می‌شوند. پیش‌فرض همراه `google/veo-3.1-fast` مدت‌زمان‌های 4/6/8 ثانیه‌ای پشتیبانی‌شده فعلی، وضوح‌های `720P`/`1080P` و نسبت‌های تصویر `16:9`/`9:16` را اعلام می‌کند. ویدیو‌به‌ویدیو برای OpenRouter ثبت نشده است، چون API بالادستی تولید ویدیو در حال حاضر متن و ارجاع‌های تصویر را می‌پذیرد.

## متن به گفتار

OpenRouter می‌تواند از طریق endpoint سازگار با OpenAI خود، یعنی `/audio/speech`، به‌عنوان ارائه‌دهنده TTS نیز استفاده شود.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

اگر `messages.tts.providers.openrouter.apiKey` حذف شود، TTS ابتدا از `models.providers.openrouter.apiKey` و سپس از `OPENROUTER_API_KEY` دوباره استفاده می‌کند.

## گفتار به متن (صدای ورودی)

OpenRouter می‌تواند پیوست‌های صوتی/voice ورودی را از طریق مسیر مشترک `tools.media.audio` و با استفاده از endpoint مربوط به STT خود (`/audio/transcriptions`) رونویسی کند. این برای هر channel plugin که voice/audio ورودی را به پیش‌پرواز درک رسانه ارسال می‌کند اعمال می‌شود.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw درخواست‌های STT برای OpenRouter را به‌صورت JSON با صدای base64 زیر `input_audio` ارسال می‌کند (قرارداد STT در OpenRouter)، نه به‌صورت بارگذاری فرم multipart مربوط به OpenAI.

## احراز هویت و headerها

OpenRouter در پشت صحنه از یک توکن Bearer با کلید API شما استفاده می‌کند.

در درخواست‌های واقعی OpenRouter (`https://openrouter.ai/api/v1`)، OpenClaw همچنین headerهای مستندشده انتساب برنامه در OpenRouter را اضافه می‌کند:

Header | مقدار  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## پیکربندی پیشرفته

کش‌کردن پاسخ

کش‌کردن پاسخ در OpenRouter اختیاری و نیازمند فعال‌سازی است. آن را برای هر مدل OpenRouter با پارامترهای مدل فعال کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw مقدار `X-OpenRouter-Cache: true` و، در صورت پیکربندی، `X-OpenRouter-Cache-TTL` را ارسال می‌کند. `responseCacheClear: true` برای درخواست فعلی یک تازه‌سازی اجباری انجام می‌دهد و پاسخ جایگزین را ذخیره می‌کند. نام‌های مستعار snake_case (`response_cache`، `response_cache_ttl_seconds` و `response_cache_clear`) نیز پذیرفته می‌شوند.

این مورد از کش‌کردن prompt در ارائه‌دهنده و از نشانگرهای Anthropic `cache_control` در OpenRouter جدا است. فقط روی مسیرهای تاییدشده `openrouter.ai` اعمال می‌شود، نه base URLهای proxy سفارشی.

نشانگرهای cache مربوط به Anthropic

در مسیرهای تاییدشده OpenRouter، ارجاع‌های مدل Anthropic نشانگرهای اختصاصی OpenRouter مربوط به Anthropic `cache_control` را که OpenClaw برای استفاده بهتر دوباره از prompt-cache در بلوک‌های prompt سیستم/توسعه‌دهنده استفاده می‌کند، نگه می‌دارند.

prefill استدلال Anthropic

در مسیرهای تاییدشده OpenRouter، ارجاع‌های مدل Anthropic که reasoning برای آن‌ها فعال است، turnهای پایانی prefill دستیار را پیش از رسیدن درخواست به OpenRouter حذف می‌کنند؛ مطابق با الزام Anthropic که گفتگوهای reasoning باید با یک turn کاربر پایان یابند.

تزریق thinking / reasoning

در مسیرهای پشتیبانی‌شده غیر از `auto`، OpenClaw سطح thinking انتخاب‌شده را به payloadهای reasoning مربوط به proxy در OpenRouter نگاشت می‌کند. اشاره‌های مدل پشتیبانی‌نشده و `openrouter/auto` آن تزریق reasoning را رد می‌کنند. Hunter Alpha نیز برای ارجاع‌های مدل پیکربندی‌شده قدیمی، proxy reasoning را رد می‌کند، چون OpenRouter ممکن است برای آن مسیر بازنشسته متن پاسخ نهایی را در فیلدهای reasoning برگرداند.

بازپخش reasoning در DeepSeek V4

در مسیرهای تاییدشده OpenRouter، `openrouter/deepseek/deepseek-v4-flash` و `openrouter/deepseek/deepseek-v4-pro` مقدار گمشده `reasoning_content` را در turnهای بازپخش‌شده دستیار پر می‌کنند تا گفتگوهای thinking/tool شکل پیگیری لازم DeepSeek V4 را حفظ کنند. OpenClaw مقادیر پشتیبانی‌شده OpenRouter برای `reasoning_effort` را برای این مسیرها ارسال می‌کند؛ `xhigh` بالاترین سطح اعلام‌شده است و overrideهای قدیمی `max` به `xhigh` نگاشت می‌شوند.

شکل‌دهی درخواست فقط مخصوص OpenAI

OpenRouter همچنان از مسیر سازگار با OpenAI به سبک proxy عبور می‌کند، بنابراین شکل‌دهی درخواست فقط مخصوص OpenAI مانند `serviceTier`، مقدار `store` در Responses، payloadهای سازگار با reasoning در OpenAI و اشاره‌های prompt-cache ارسال نمی‌شوند.

مسیرهای متکی بر Gemini

ارجاع‌های OpenRouter متکی بر Gemini روی مسیر proxy-Gemini باقی می‌مانند: OpenClaw پاک‌سازی thought-signature مربوط به Gemini را در آنجا حفظ می‌کند، اما اعتبارسنجی بازپخش native Gemini یا بازنویسی‌های bootstrap را فعال نمی‌کند.

فراداده مسیریابی ارائه‌دهنده

اگر مسیریابی ارائه‌دهنده OpenRouter را زیر پارامترهای مدل ارسال کنید، OpenClaw آن را پیش از اجرای wrapperهای stream مشترک، به‌عنوان فراداده مسیریابی OpenRouter forward می‌کند.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** مرجع کامل پیکربندی برای agentها، مدل‌ها و ارائه‌دهندگان. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo