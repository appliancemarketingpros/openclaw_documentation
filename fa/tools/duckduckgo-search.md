---
title: جست‌وجوی DuckDuckGo
source_url: https://docs.openclaw.ai/fa/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw از DuckDuckGo به‌عنوان ارائه‌دهنده‌ی `web_search` **بدون کلید** پشتیبانی می‌کند. هیچ کلید API یا حسابی لازم نیست.

## راه‌اندازی

هیچ کلید API لازم نیست؛ فقط DuckDuckGo را به‌عنوان ارائه‌دهنده‌ی خود تنظیم کنید:

* ### پیکربندی

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## پیکربندی

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

تنظیمات اختیاری در سطح Plugin برای منطقه و SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## پارامترهای ابزار

پرس‌وجوی جست‌وجو.

نتایجی که باید برگردانده شوند (۱ تا ۱۰).

کد منطقه‌ی DuckDuckGo (مثلاً `us-en`، `uk-en`، `de-de`).

سطح SafeSearch.

منطقه و SafeSearch را می‌توان در پیکربندی Plugin نیز تنظیم کرد (بالا را ببینید)؛ پارامترهای ابزار در هر پرس‌وجو مقادیر پیکربندی را بازنویسی می‌کنند.

## یادداشت‌ها

  * **بدون کلید API** ؛ بلافاصله و بدون هیچ پیکربندی کار می‌کند
  * **آزمایشی** ؛ نتایج را از صفحه‌های جست‌وجوی HTML غیرجاوااسکریپتی DuckDuckGo گردآوری می‌کند، نه از یک API یا SDK رسمی
  * **ریسک چالش ربات** ؛ DuckDuckGo ممکن است CAPTCHA ارائه کند یا در استفاده‌ی سنگین یا خودکار درخواست‌ها را مسدود کند
  * **تجزیه‌ی HTML** ؛ نتایج به ساختار صفحه وابسته‌اند، که ممکن است بدون اطلاع تغییر کند
  * **ترتیب تشخیص خودکار** ؛ DuckDuckGo نخستین جایگزین بدون کلید در تشخیص خودکار است (ترتیب ۱۰۰). ارائه‌دهنده‌های مبتنی بر API که کلیدهای پیکربندی‌شده دارند ابتدا اجرا می‌شوند، سپس Ollama Web Search (ترتیب ۱۱۰)، سپس SearXNG (ترتیب ۲۰۰)
  * **SafeSearch در صورت پیکربندی‌نشدن، به‌طور پیش‌فرض روی moderate است**


## مرتبط

  * [نمای کلی جست‌وجوی وب](</fa/tools/web>) \-- همه‌ی ارائه‌دهنده‌ها و تشخیص خودکار
  * [Brave Search](</fa/tools/brave-search>) \-- نتایج ساختاریافته با رده‌ی رایگان
  * [Exa Search](</fa/tools/exa-search>) \-- جست‌وجوی عصبی همراه با استخراج محتوا


Was this useful?YesNo