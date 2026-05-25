---
title: جستجوی وب Ollama
source_url: https://docs.openclaw.ai/fa/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw از **Ollama Web Search** به‌عنوان یک ارائه‌دهندهٔ همراه `web_search` پشتیبانی می‌کند. این قابلیت از API جست‌وجوی وب Ollama استفاده می‌کند و نتایج ساختاریافته با عنوان‌ها، URLها و قطعه‌متن‌ها برمی‌گرداند.

برای Ollama محلی یا خودمیزبان، این راه‌اندازی به‌طور پیش‌فرض به کلید API نیاز ندارد. اما به این موارد نیاز دارد:

  * یک میزبان Ollama که از OpenClaw قابل دسترسی باشد
  * `ollama signin`


برای جست‌وجوی میزبانی‌شدهٔ مستقیم، URL پایهٔ ارائه‌دهندهٔ Ollama را روی `https://ollama.com` تنظیم کنید و یک `OLLAMA_API_KEY` واقعی ارائه دهید.

## راه‌اندازی

* ### شروع Ollama

مطمئن شوید Ollama نصب شده و در حال اجراست.

* ### ورود

اجرا کنید:

bashCopy code
[code]
    ollama signin
[/code]

* ### انتخاب Ollama Web Search

اجرا کنید:

bashCopy code
[code]
    openclaw configure --section web
[/code]

سپس **Ollama Web Search** را به‌عنوان ارائه‌دهنده انتخاب کنید.

اگر از قبل از Ollama برای مدل‌ها استفاده می‌کنید، Ollama Web Search از همان میزبان پیکربندی‌شده دوباره استفاده می‌کند.

## پیکربندی

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

بازنویسی اختیاری میزبان Ollama:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

اگر از قبل Ollama را به‌عنوان ارائه‌دهندهٔ مدل پیکربندی کرده‌اید، ارائه‌دهندهٔ جست‌وجوی وب می‌تواند به‌جای آن از همان میزبان دوباره استفاده کند:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

ارائه‌دهندهٔ مدل Ollama از `baseUrl` به‌عنوان کلید معیار استفاده می‌کند. ارائه‌دهندهٔ جست‌وجوی وب همچنین برای سازگاری با نمونه‌های پیکربندی به سبک OpenAI SDK، مقدار `baseURL` را در `models.providers.ollama` می‌پذیرد.

اگر هیچ URL پایهٔ صریحی برای Ollama تنظیم نشده باشد، OpenClaw از `http://127.0.0.1:11434` استفاده می‌کند.

اگر میزبان Ollama شما انتظار احراز هویت bearer داشته باشد، OpenClaw از `models.providers.ollama.apiKey` (یا احراز هویت ارائه‌دهندهٔ پشتیبانی‌شده با env متناظر) برای درخواست‌ها به آن میزبان پیکربندی‌شده دوباره استفاده می‌کند.

جست‌وجوی مستقیم میزبانی‌شدهٔ Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## نکته‌ها

  * برای این ارائه‌دهنده، هیچ فیلد کلید API مخصوص جست‌وجوی وب لازم نیست.
  * اگر میزبان Ollama با احراز هویت محافظت شده باشد، OpenClaw هنگام وجود کلید API عادی ارائه‌دهندهٔ Ollama از آن دوباره استفاده می‌کند.
  * اگر `baseUrl` برابر `https://ollama.com` باشد، OpenClaw مستقیماً `https://ollama.com/api/web_search` را فراخوانی می‌کند و کلید API پیکربندی‌شدهٔ Ollama را به‌عنوان احراز هویت bearer ارسال می‌کند.
  * اگر میزبان پیکربندی‌شده جست‌وجوی وب را ارائه نکند و `OLLAMA_API_KEY` تنظیم شده باشد، OpenClaw می‌تواند بدون ارسال آن کلید env به میزبان محلی، به `https://ollama.com/api/web_search` بازگردد.
  * OpenClaw هنگام راه‌اندازی هشدار می‌دهد اگر Ollama در دسترس نباشد یا ورود انجام نشده باشد، اما انتخاب را مسدود نمی‌کند.
  * شناسایی خودکار زمان اجرا می‌تواند وقتی هیچ ارائه‌دهندهٔ دارای اعتبارنامه با اولویت بالاتر پیکربندی نشده باشد، به Ollama Web Search بازگردد.
  * میزبان‌های daemon محلی Ollama از نقطهٔ پایانی پراکسی محلی `/api/experimental/web_search` استفاده می‌کنند که درخواست را امضا کرده و به Ollama Cloud بازارسال می‌کند.
  * میزبان‌های `https://ollama.com` مستقیماً از نقطهٔ پایانی میزبانی‌شدهٔ عمومی `/api/web_search` همراه با احراز هویت کلید API به‌صورت bearer استفاده می‌کنند.


## مرتبط

  * [نمای کلی جست‌وجوی وب](</fa/tools/web>) \-- همهٔ ارائه‌دهندگان و شناسایی خودکار
  * [Ollama](</fa/providers/ollama>) \-- راه‌اندازی مدل Ollama و حالت‌های ابری/محلی


Was this useful?YesNo