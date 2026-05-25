---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/fa/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway یک **API یکپارچه** ارائه می‌کند که درخواست‌ها را به مدل‌های متعدد پشت یک نقطه پایانی و کلید API واحد هدایت می‌کند. این API با OpenAI سازگار است، بنابراین بیشتر SDKهای OpenAI با تغییر Base URL کار می‌کنند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `kilocode`  
احراز هویت | `KILOCODE_API_KEY`  
API | سازگار با OpenAI  
Base URL | `https://api.kilo.ai/api/gateway/`  
  
## شروع به کار

* ### ایجاد حساب

به [app.kilo.ai](<https://app.kilo.ai>) بروید، وارد شوید یا یک حساب ایجاد کنید، سپس به API Keys بروید و یک کلید جدید بسازید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

یا متغیر محیطی را مستقیم تنظیم کنید:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### بررسی کنید که مدل در دسترس است

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## مدل پیش‌فرض

مدل پیش‌فرض `kilocode/kilo/auto` است؛ یک مدل مسیریابی هوشمند متعلق به ارائه‌دهنده که توسط Kilo Gateway مدیریت می‌شود.

## کاتالوگ داخلی

OpenClaw هنگام شروع، مدل‌های در دسترس را به‌صورت پویا از Kilo Gateway کشف می‌کند. از `/models kilocode` استفاده کنید تا فهرست کامل مدل‌های در دسترس با حساب خود را ببینید.

هر مدلی که روی Gateway در دسترس باشد می‌تواند با پیشوند `kilocode/` استفاده شود:

ref مدل | یادداشت‌ها  
---|---  
`kilocode/kilo/auto` | پیش‌فرض — مسیریابی هوشمند  
`kilocode/anthropic/claude-sonnet-4` | Anthropic از طریق Kilo  
`kilocode/openai/gpt-5.5` | OpenAI از طریق Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google از طریق Kilo  
...و بسیاری موارد دیگر | برای فهرست کردن همه از `/models kilocode` استفاده کنید  
  
## نمونه پیکربندی

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

انتقال و سازگاری

Kilo Gateway در منبع به‌عنوان سازگار با OpenRouter مستند شده است، بنابراین به‌جای شکل‌دهی بومی درخواست OpenAI، روی مسیر سازگار با OpenAI به سبک پراکسی باقی می‌ماند.

  * refهای Kilo مبتنی بر Gemini روی مسیر proxy-Gemini باقی می‌مانند، بنابراین OpenClaw پاک‌سازی thought-signature مربوط به Gemini را در آنجا حفظ می‌کند، بدون اینکه اعتبارسنجی replay بومی Gemini یا بازنویسی‌های bootstrap را فعال کند.
  * Kilo Gateway در پشت صحنه از توکن Bearer همراه با کلید API شما استفاده می‌کند.

پوشش‌دهندهٔ جریان و reasoning

پوشش‌دهندهٔ جریان مشترک Kilo سربرگ برنامهٔ ارائه‌دهنده را اضافه می‌کند و payloadهای reasoning پراکسی را برای refهای مدل مشخص پشتیبانی‌شده نرمال‌سازی می‌کند.

عیب‌یابی

  * اگر کشف مدل هنگام شروع شکست بخورد، OpenClaw به کاتالوگ ایستای بسته‌بندی‌شده که شامل `kilocode/kilo/auto` است fallback می‌کند.
  * تأیید کنید کلید API شما معتبر است و حساب Kilo شما مدل‌های موردنظر را فعال دارد.
  * وقتی Gateway به‌صورت daemon اجرا می‌شود، مطمئن شوید `KILOCODE_API_KEY` برای آن فرایند در دسترس است (برای مثال در `~/.openclaw/.env` یا از طریق `env.shellEnv`).


## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، refهای مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** مرجع کامل پیکربندی OpenClaw. ](</fa/gateway/configuration-reference>) [**Kilo Gateway** داشبورد Kilo Gateway، کلیدهای API، و مدیریت حساب. ](<https://app.kilo.ai>)

Was this useful?YesNo