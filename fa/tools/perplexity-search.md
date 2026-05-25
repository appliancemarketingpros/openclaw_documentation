---
title: جست‌وجوی Perplexity
source_url: https://docs.openclaw.ai/fa/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw از Perplexity Search API به‌عنوان ارائه‌دهنده‌ی `web_search` پشتیبانی می‌کند. این API نتایج ساختاریافته‌ای با فیلدهای `title`، `url` و `snippet` برمی‌گرداند.

برای سازگاری، OpenClaw از تنظیمات قدیمی Perplexity Sonar/OpenRouter نیز پشتیبانی می‌کند. اگر از `OPENROUTER_API_KEY`، یک کلید `sk-or-...` در `plugins.entries.perplexity.config.webSearch.apiKey` استفاده کنید، یا `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` را تنظیم کنید، ارائه‌دهنده به مسیر chat-completions تغییر می‌کند و به‌جای نتایج ساختاریافته‌ی Search API، پاسخ‌های تولیدشده با هوش مصنوعی همراه با ارجاع‌ها برمی‌گرداند.

## دریافت کلید API برای Perplexity

  1. در [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>) یک حساب Perplexity بسازید
  2. در داشبورد یک کلید API تولید کنید
  3. کلید را در پیکربندی ذخیره کنید یا `PERPLEXITY_API_KEY` را در محیط Gateway تنظیم کنید.


## سازگاری با OpenRouter

اگر از قبل از OpenRouter برای Perplexity Sonar استفاده می‌کردید، `provider: "perplexity"` را نگه دارید و `OPENROUTER_API_KEY` را در محیط Gateway تنظیم کنید، یا یک کلید `sk-or-...` را در `plugins.entries.perplexity.config.webSearch.apiKey` ذخیره کنید.

کنترل‌های اختیاری سازگاری:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## نمونه‌های پیکربندی

### Perplexity Search API بومی

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### سازگاری OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## محل تنظیم کلید

**از طریق پیکربندی:** دستور `openclaw configure --section web` را اجرا کنید. این دستور کلید را در `~/.openclaw/openclaw.json` زیر `plugins.entries.perplexity.config.webSearch.apiKey` ذخیره می‌کند. این فیلد اشیای SecretRef را نیز می‌پذیرد.

**از طریق محیط:** `PERPLEXITY_API_KEY` یا `OPENROUTER_API_KEY` را در محیط فرایند Gateway تنظیم کنید. برای نصب gateway، آن را در `~/.openclaw/.env` (یا محیط سرویس خودتان) قرار دهید. [متغیرهای محیطی](</fa/help/faq#env-vars-and-env-loading>) را ببینید.

اگر `provider: "perplexity"` پیکربندی شده باشد و SecretRef کلید Perplexity بدون جایگزین محیطی resolve نشده باشد، راه‌اندازی/بارگذاری مجدد سریعاً شکست می‌خورد.

## پارامترهای ابزار

این پارامترها برای مسیر بومی Perplexity Search API اعمال می‌شوند.

پرس‌وجوی جست‌وجو.

تعداد نتایجی که باید برگردانده شود (1-10).

کد کشور ISO دوحرفی (برای مثال `US`، `DE`).

کد زبان ISO 639-1 (برای مثال `en`، `de`، `fr`).

فیلتر زمانی - `day` برابر با ۲۴ ساعت است.

فقط نتایجی که پس از این تاریخ منتشر شده‌اند (`YYYY-MM-DD`).

فقط نتایجی که پیش از این تاریخ منتشر شده‌اند (`YYYY-MM-DD`).

آرایه‌ی allowlist/denylist دامنه‌ها (حداکثر 20).

بودجه‌ی کل محتوا (حداکثر 1000000).

محدودیت توکن برای هر صفحه.

برای مسیر سازگاری قدیمی Sonar/OpenRouter:

  * `query`، `count` و `freshness` پذیرفته می‌شوند
  * `count` در آنجا فقط برای سازگاری است؛ پاسخ همچنان یک پاسخ تولیدشده‌ی واحد همراه با ارجاع‌ها است، نه یک فهرست N-نتیجه‌ای
  * فیلترهای مخصوص Search API مانند `country`، `language`، `date_after`، `date_before`، `domain_filter`، `max_tokens` و `max_tokens_per_page` خطاهای صریح برمی‌گردانند


**نمونه‌ها:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### قواعد فیلتر دامنه

  * حداکثر 20 دامنه در هر فیلتر
  * امکان ترکیب allowlist و denylist در یک درخواست وجود ندارد
  * برای ورودی‌های denylist از پیشوند `-` استفاده کنید (برای مثال `["-reddit.com"]`)


## نکات

  * Perplexity Search API نتایج ساختاریافته‌ی جست‌وجوی وب را برمی‌گرداند (`title`، `url`، `snippet`)
  * OpenRouter یا `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` صریح، Perplexity را برای سازگاری دوباره به chat completions مربوط به Sonar تغییر می‌دهد
  * سازگاری Sonar/OpenRouter یک پاسخ تولیدشده‌ی واحد همراه با ارجاع‌ها برمی‌گرداند، نه ردیف‌های نتیجه‌ی ساختاریافته
  * نتایج به‌طور پیش‌فرض برای ۱۵ دقیقه کش می‌شوند (قابل پیکربندی از طریق `cacheTtlMinutes`)


## مرتبط

[**نمای کلی جست‌وجوی وب** همه‌ی ارائه‌دهنده‌ها و قواعد تشخیص خودکار. ](</fa/tools/web>) [**جست‌وجوی Brave** نتایج ساختاریافته با فیلترهای کشور و زبان. ](</fa/tools/brave-search>) [**جست‌وجوی Exa** جست‌وجوی عصبی همراه با استخراج محتوا. ](</fa/tools/exa-search>) [**مستندات Perplexity Search API** راه‌اندازی سریع و مرجع رسمی Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo