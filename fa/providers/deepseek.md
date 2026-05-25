---
title: DeepSeek
source_url: https://docs.openclaw.ai/fa/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) مدل‌های هوش مصنوعی قدرتمندی را با API سازگار با OpenAI ارائه می‌دهد.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `deepseek`  
احراز هویت | `DEEPSEEK_API_KEY`  
API | سازگار با OpenAI  
URL پایه | `https://api.deepseek.com`  
  
## شروع به کار

* ### دریافت کلید API

یک کلید API در [platform.deepseek.com](<https://platform.deepseek.com/api_keys>) بسازید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

این دستور کلید API شما را درخواست می‌کند و `deepseek/deepseek-v4-flash` را به‌عنوان مدل پیش‌فرض تنظیم می‌کند.

* ### تأیید در دسترس بودن مدل‌ها

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

برای بررسی کاتالوگ ایستای همراه، بدون نیاز به Gateway در حال اجرا، از این استفاده کنید:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

راه‌اندازی غیرتعاملی

برای نصب‌های اسکریپتی یا بدون رابط، همه پرچم‌ها را مستقیم ارسال کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## کاتالوگ داخلی

ارجاع مدل | نام | ورودی | زمینه | بیشینه خروجی | یادداشت‌ها  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | مدل پیش‌فرض؛ سطح V4 با قابلیت تفکر  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | سطح V4 با قابلیت تفکر  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | سطح بدون تفکر DeepSeek V3.2  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | سطح V3.2 با قابلیت استدلال  
  
## تفکر و ابزارها

نشست‌های تفکر DeepSeek V4 نسبت به بیشتر ارائه‌دهندگان سازگار با OpenAI قرارداد بازپخش سخت‌گیرانه‌تری دارند: پس از اینکه یک نوبت با تفکر فعال از ابزارها استفاده کند، DeepSeek انتظار دارد پیام‌های assistant بازپخش‌شده از آن نوبت، در درخواست‌های بعدی شامل `reasoning_content` باشند. OpenClaw این مورد را داخل Plugin مربوط به DeepSeek مدیریت می‌کند، بنابراین استفاده عادی چندنوبتی از ابزارها با `deepseek/deepseek-v4-flash` و `deepseek/deepseek-v4-pro` کار می‌کند.

اگر یک نشست موجود را از ارائه‌دهنده سازگار با OpenAI دیگری به یک مدل DeepSeek V4 تغییر دهید، نوبت‌های قدیمی‌تر فراخوانی ابزار توسط assistant ممکن است `reasoning_content` بومی DeepSeek را نداشته باشند. OpenClaw هنگام بازپخش پیام‌های assistant برای درخواست‌های تفکر DeepSeek V4، آن فیلد ازدست‌رفته را پر می‌کند تا ارائه‌دهنده بتواند تاریخچه را بدون نیاز به `/new` بپذیرد.

وقتی تفکر در OpenClaw غیرفعال باشد (از جمله انتخاب **None** در UI)، OpenClaw مقدار `thinking: { type: "disabled" }` را به DeepSeek می‌فرستد و `reasoning_content` بازپخش‌شده را از تاریخچه خروجی حذف می‌کند. این کار نشست‌های با تفکر غیرفعال را در مسیر بدون تفکر DeepSeek نگه می‌دارد.

برای مسیر سریع پیش‌فرض از `deepseek/deepseek-v4-flash` استفاده کنید. وقتی مدل V4 قوی‌تر را می‌خواهید و می‌توانید هزینه یا تأخیر بیشتر را بپذیرید، از `deepseek/deepseek-v4-pro` استفاده کنید.

## آزمون زنده

مجموعه مدل زنده مستقیم شامل DeepSeek V4 در مجموعه مدل‌های مدرن است. برای اجرای فقط بررسی‌های مدل مستقیم DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

این بررسی زنده تأیید می‌کند که هر دو مدل V4 می‌توانند تکمیل شوند و نوبت‌های بعدی تفکر/ابزار محموله بازپخشی را که DeepSeek نیاز دارد حفظ می‌کنند.

## نمونه پیکربندی

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** مرجع کامل پیکربندی برای agents، مدل‌ها، و ارائه‌دهندگان. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo