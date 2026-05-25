---
title: Cerebras
source_url: https://docs.openclaw.ai/fa/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) استنتاج پرسرعت سازگار با OpenAI را روی سخت‌افزار استنتاج سفارشی ارائه می‌دهد. OpenClaw یک Plugin ارائه‌دهندهٔ Cerebras همراه دارد که شامل یک کاتالوگ ثابت چهارمدلی است.

ویژگی | مقدار  
---|---  
شناسهٔ ارائه‌دهنده | `cerebras`  
Plugin | همراه، `enabledByDefault: true`  
متغیر محیطی احراز هویت | `CEREBRAS_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice cerebras-api-key`  
پرچم مستقیم CLI | `--cerebras-api-key <key>`  
API | سازگار با OpenAI (`openai-completions`)  
URL پایه | `https://api.cerebras.ai/v1`  
مدل پیش‌فرض | `cerebras/zai-glm-4.7`  
  
## شروع به کار

* ### دریافت کلید API

یک کلید API در [Cerebras Cloud Console](<https://cloud.cerebras.ai>) ایجاد کنید.

* ### اجرای راه‌اندازی اولیه

راه‌اندازی اولیهCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

پرچم مستقیمCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

فقط محیطCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### تأیید در دسترس بودن مدل‌ها

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

این فهرست باید هر چهار مدل همراه را شامل شود. اگر `CEREBRAS_API_KEY` قابل حل نباشد، `openclaw models status --json` اعتبارنامهٔ گمشده را زیر `auth.unusableProfiles` گزارش می‌کند.

## راه‌اندازی غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## کاتالوگ داخلی

OpenClaw یک کاتالوگ ثابت Cerebras ارائه می‌کند که با نقطهٔ پایانی عمومی سازگار با OpenAI همخوان است. هر چهار مدل، زمینهٔ 128k و حداکثر 8,192 توکن خروجی دارند.

ارجاع مدل | نام | استدلال | یادداشت‌ها  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | بله | مدل پیش‌فرض؛ مدل استدلال پیش‌نمایش  
`cerebras/gpt-oss-120b` | GPT OSS 120B | بله | مدل استدلال تولیدی  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | خیر | مدل غیر استدلالی پیش‌نمایش  
`cerebras/llama3.1-8b` | Llama 3.1 8B | خیر | مدل تولیدی متمرکز بر سرعت  
  
## پیکربندی دستی

Plugin همراه معمولاً یعنی فقط به کلید API نیاز دارید. وقتی می‌خواهید فرادادهٔ مدل را بازنویسی کنید یا در برابر کاتالوگ ثابت با `mode: "merge"` اجرا کنید، از پیکربندی صریح `models.providers.cerebras` استفاده کنید:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## مرتبط

[**ارائه‌دهندگان مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**حالت‌های تفکر** سطوح تلاش استدلال برای دو مدل Cerebras دارای قابلیت استدلال. ](</fa/tools/thinking>) [**مرجع پیکربندی** پیش‌فرض‌های عامل و پیکربندی مدل. ](</fa/gateway/config-agents#agent-defaults>) [**پرسش‌های متداول مدل‌ها** پروفایل‌های احراز هویت، تغییر مدل‌ها، و رفع خطاهای «no profile». ](</fa/help/faq-models>)

Was this useful?YesNo