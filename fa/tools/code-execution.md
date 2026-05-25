---
title: اجرای کد
source_url: https://docs.openclaw.ai/fa/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` تحلیل Python راه دور و سندباکس‌شده را روی Responses API شرکت xAI اجرا می‌کند. این ابزار توسط Plugin همراه `xai` (زیر قرارداد `tools`) ثبت می‌شود و به همان نقطه پایانی `https://api.x.ai/v1/responses` ارسال می‌کند که `x_search` از آن استفاده می‌کند.

ویژگی | مقدار  
---|---  
نام ابزار | `code_execution`  
Plugin ارائه‌دهنده | `xai` (همراه، `enabledByDefault: true`)  
احراز هویت | پروفایل احراز هویت xAI، `XAI_API_KEY`، یا `plugins.entries.xai.config.webSearch.apiKey`  
مدل پیش‌فرض | `grok-4-1-fast`  
مهلت زمانی پیش‌فرض | ۳۰ ثانیه  
`maxTurns` پیش‌فرض | تنظیم‌نشده (xAI محدودیت داخلی خودش را اعمال می‌کند)  
  
این با [`exec`](</fa/tools/exec>) محلی تفاوت دارد:

  * `exec` فرمان‌های shell را روی ماشین شما یا node جفت‌شده اجرا می‌کند.
  * `code_execution`، Python را در sandbox راه دور xAI اجرا می‌کند.


از `code_execution` برای این موارد استفاده کنید:

  * محاسبات.
  * جدول‌بندی.
  * آمار سریع.
  * تحلیل به سبک نمودار.
  * تحلیل داده‌های بازگردانده‌شده توسط `x_search` یا `web_search`.


وقتی به فایل‌های محلی، shell، repo یا دستگاه‌های جفت‌شده نیاز دارید از آن استفاده **نکنید**. برای این کار از [`exec`](</fa/tools/exec>) استفاده کنید.

## راه‌اندازی

* ### یک کلید API برای xAI ارائه کنید

برای `code_execution` و `x_search`، فرمان `openclaw onboard --auth-choice xai-api-key` را اجرا کنید، یا `XAI_API_KEY` را تنظیم کنید / کلید را زیر Plugin xAI پیکربندی کنید وقتی می‌خواهید جست‌وجوی وب Grok نیز از همان اعتبارنامه استفاده کند:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

یا از طریق پیکربندی:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### code_execution را فعال و تنظیم کنید

این ابزار با `plugins.entries.xai.config.codeExecution.enabled` کنترل می‌شود. پیش‌فرض خاموش است.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Gateway را راه‌اندازی مجدد کنید

bashCopy code
[code]
    openclaw gateway restart
[/code]

پس از اینکه Plugin xAI دوباره با `enabled: true` ثبت شد، `code_execution` در فهرست ابزارهای agent ظاهر می‌شود.

## نحوه استفاده از آن

طبیعی درخواست کنید و هدف تحلیل را صریح بیان کنید:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

این ابزار در داخل فقط یک پارامتر `task` می‌گیرد، بنابراین agent باید درخواست کامل تحلیل و هر داده درون‌خطی را در یک prompt ارسال کند.

## خطاها

وقتی ابزار بدون احراز هویت اجرا شود، یک خطای ساختاریافته `missing_xai_api_key` برمی‌گرداند که به گزینه‌های auth-profile، متغیر محیطی و پیکربندی اشاره می‌کند. خطا JSON است، نه یک استثنای پرتاب‌شده، بنابراین agent می‌تواند خودش آن را اصلاح کند:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## محدودیت‌ها

  * این اجرای راه دور xAI است، نه اجرای فرایند محلی.
  * نتایج را تحلیل زودگذر در نظر بگیرید، نه یک جلسه notebook پایدار.
  * دسترسی به فایل‌های محلی یا workspace خود را فرض نکنید.
  * برای داده‌های تازه X، ابتدا از [`x_search`](</fa/tools/web#x_search>) استفاده کنید و نتیجه را به `code_execution` لوله کنید.


## مرتبط

[**ابزار Exec** اجرای shell محلی روی ماشین شما یا node جفت‌شده. ](</fa/tools/exec>) [**تأییدهای Exec** سیاست مجاز/غیرمجاز برای اجرای shell. ](</fa/tools/exec-approvals>) [**ابزارهای وب** `web_search`، `x_search` و `web_fetch`. ](</fa/tools/web>) [**ارائه‌دهنده xAI** مدل‌های Grok، جست‌وجوی وب/X، و پیکربندی اجرای کد. ](</fa/providers/xai>)

Was this useful?YesNo