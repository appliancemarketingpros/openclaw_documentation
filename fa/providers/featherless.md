---
title: Featherless AI
source_url: https://docs.openclaw.ai/fa/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) مدل‌های باز را از طریق یک API سازگار با OpenAI ارائه می‌کند. OpenClaw، ‏Featherless را به‌عنوان Plugin رسمی ارائه‌دهندهٔ خارجی نصب می‌کند و ضمن کوچک نگه‌داشتن فهرست داخلی، شناسه‌های دقیق مدل را هنگام اجرا از Featherless می‌پذیرد.

ویژگی | مقدار  
---|---  
شناسهٔ ارائه‌دهنده | `featherless`  
بسته | `@openclaw/featherless-provider`  
متغیر محیطی احراز هویت | `FEATHERLESS_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice featherless-api-key`  
پرچم مستقیم CLI | `--featherless-api-key <key>`  
API | سازگار با OpenAI (`openai-completions`)  
نشانی پایه | `https://api.featherless.ai/v1`  
مدل پیش‌فرض | `featherless/Qwen/Qwen3-32B`  
  
## راه‌اندازی

Plugin را نصب و Gateway را بازراه‌اندازی کنید:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

راه‌اندازی اولیه را اجرا کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

برای راه‌اندازی غیرتعاملی:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

یا کلید را در دسترس فرایند Gateway قرار دهید:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

ارائه‌دهنده را تأیید کنید:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## مدل پیش‌فرض

این Plugin از `Qwen/Qwen3-32B` به‌عنوان مدل پیش‌فرض راه‌اندازی استفاده می‌کند، زیرا مستندات Featherless فراخوانی بومی ابزار را برای خانوادهٔ Qwen 3 ذکر می‌کنند. OpenClaw پنجرهٔ بافت ۳۲٬۷۶۸ توکنی، محدودیت محافظه‌کارانهٔ خروجی ۴٬۰۹۶ توکنی و کنترل‌های تفکر الگوی گفت‌وگوی Qwen را برای آن پیکربندی می‌کند.

فیلدهای هزینه در فهرست صفر هستند، زیرا Featherless از چندین شیوهٔ صورت‌حساب پشتیبانی می‌کند و OpenClaw نرخ‌های مختص طرح حساب یا قیمت‌گذاری هر درخواست را در خود جای نمی‌دهد.

## سایر مدل‌های Featherless

شناسهٔ دقیق مدل Featherless را پس از پیشوند ارائه‌دهندهٔ `featherless/` استفاده کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw عمداً نمایهٔ عمومی کامل مدل‌های Featherless را در انتخابگر کپی نمی‌کند. این نمایه بزرگ است و فرادادهٔ ساخت‌یافتهٔ کافی برای طبقه‌بندی ایمن همهٔ مدل‌های متن، بینایی، تعبیه‌سازی و استدلال ارائه نمی‌کند. بنابراین، شناسه‌های ناشناخته با پیش‌فرض‌های محافظه‌کارانهٔ فقط‌متنی و بدون استدلال تفکیک می‌شوند: پنجرهٔ بافت ۴٬۰۹۶ توکنی و محدودیت خروجی ۱٬۰۲۴ توکنی.

اگر مدلی به فرادادهٔ متفاوتی نیاز دارد، یک ورودی صریح برای مدل ارائه‌دهنده اضافه کنید:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

پیش از افزودن فرادادهٔ سفارشی، فهرست مدل‌های Featherless را برای بررسی موجودبودن کنونی مدل و برچسب‌های قابلیت آن بررسی کنید.

## عیب‌یابی

  * `401` یا `403`: تأیید کنید که `FEATHERLESS_API_KEY` برای فرایند Gateway قابل مشاهده است، یا راه‌اندازی اولیه را دوباره اجرا کنید.
  * مدل ناشناخته: پس از پیشوند `featherless/`، شناسهٔ دقیق و حساس به بزرگی و کوچکی حروف را از Featherless استفاده کنید.
  * فراخوانی‌های ابزار به‌صورت متن بازگردانده می‌شوند: خانوادهٔ مدلی را انتخاب کنید که Featherless فراخوانی بومی تابع را برای آن مستند کرده است، مانند Qwen 3.
  * Gateway مدیریت‌شده نمی‌تواند کلید را ببیند: آن را در `~/.openclaw/.env` یا منبع محیطی دیگری که سرویس بارگیری می‌کند قرار دهید، سپس Gateway را بازراه‌اندازی کنید.


## مرتبط

  * [ارائه‌دهندگان مدل](</fa/concepts/model-providers>)
  * [همهٔ ارائه‌دهندگان](</fa/providers>)
  * [حالت‌های تفکر](</fa/tools/thinking>)


Was this useful?YesNo

Open issue