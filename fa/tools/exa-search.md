---
title: جستجوی Exa
source_url: https://docs.openclaw.ai/fa/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw از [Exa AI](<https://exa.ai/>) به‌عنوان ارائه‌دهنده `web_search` پشتیبانی می‌کند. Exa حالت‌های جست‌وجوی عصبی، کلیدواژه‌ای و ترکیبی را همراه با استخراج محتوای داخلی (برجسته‌سازی‌ها، متن، خلاصه‌ها) ارائه می‌دهد.

## دریافت کلید API

* ### Create an account

در [exa.ai](<https://exa.ai/>) ثبت‌نام کنید و از داشبورد خود یک کلید API تولید کنید.

* ### Store the key

`EXA_API_KEY` را در محیط Gateway تنظیم کنید، یا از طریق این دستور پیکربندی کنید:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## پیکربندی

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**جایگزین محیطی:** `EXA_API_KEY` را در محیط Gateway تنظیم کنید. برای نصب gateway، آن را در `~/.openclaw/.env` قرار دهید.

## بازنویسی URL پایه

وقتی درخواست‌های جست‌وجوی Exa باید از طریق یک پروکسی سازگار یا endpoint جایگزین Exa عبور کنند، `plugins.entries.exa.config.webSearch.baseUrl` را تنظیم کنید. OpenClaw میزبان‌های خام را با افزودن `https://` به ابتدای آن‌ها عادی‌سازی می‌کند و `/search` را اضافه می‌کند مگر اینکه مسیر از قبل به آن ختم شده باشد. endpoint نهایی در کلید cache جست‌وجو گنجانده می‌شود، بنابراین نتایج endpointهای مختلف Exa با هم به اشتراک گذاشته نمی‌شوند.

## پارامترهای ابزار

عبارت جست‌وجو.

نتایج برای بازگرداندن (1–100).

حالت جست‌وجو.

فیلتر زمانی.

نتایج پس از این تاریخ (`YYYY-MM-DD`).

نتایج پیش از این تاریخ (`YYYY-MM-DD`).

گزینه‌های استخراج محتوا (پایین را ببینید).

### استخراج محتوا

Exa می‌تواند محتوای استخراج‌شده را در کنار نتایج جست‌وجو بازگرداند. برای فعال‌سازی، یک شیء `contents` ارسال کنید:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

گزینه Contents | نوع | توضیح  
---|---|---  
`text` | `boolean | { maxCharacters }` | استخراج متن کامل صفحه  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | استخراج جمله‌های کلیدی  
`summary` | `boolean | { query }` | خلاصه تولیدشده با هوش مصنوعی  
  
### حالت‌های جست‌وجو

حالت | توضیح  
---|---  
`auto` | Exa بهترین حالت را انتخاب می‌کند (پیش‌فرض)  
`neural` | جست‌وجوی معنایی/مبتنی بر معنا  
`fast` | جست‌وجوی سریع کلیدواژه‌ای  
`deep` | جست‌وجوی عمیق و کامل  
`deep-reasoning` | جست‌وجوی عمیق با استدلال  
`instant` | سریع‌ترین نتایج  
  
## نکات

  * اگر هیچ گزینه `contents` ارائه نشود، Exa به‌صورت پیش‌فرض از `{ highlights: true }` استفاده می‌کند تا نتایج شامل گزیده‌هایی از جمله‌های کلیدی باشند
  * نتایج، فیلدهای `highlightScores` و `summary` را از پاسخ API مربوط به Exa، در صورت موجود بودن، حفظ می‌کنند
  * توضیحات نتیجه ابتدا از برجسته‌سازی‌ها، سپس از خلاصه، و سپس از متن کامل استخراج می‌شوند — هرکدام که موجود باشد
  * `freshness` و `date_after`/`date_before` را نمی‌توان با هم ترکیب کرد — از یک حالت فیلتر زمانی استفاده کنید
  * در هر query می‌توان تا 100 نتیجه بازگرداند (با رعایت محدودیت‌های نوع جست‌وجوی Exa)
  * نتایج به‌صورت پیش‌فرض برای 15 دقیقه cache می‌شوند (قابل پیکربندی از طریق `cacheTtlMinutes`)
  * Exa یک یکپارچه‌سازی رسمی API با پاسخ‌های JSON ساختاریافته است


## مرتبط

  * [نمای کلی Web Search](</fa/tools/web>) \-- همه ارائه‌دهندگان و تشخیص خودکار
  * [Brave Search](</fa/tools/brave-search>) \-- نتایج ساختاریافته با فیلترهای کشور/زبان
  * [Perplexity Search](</fa/tools/perplexity-search>) \-- نتایج ساختاریافته با فیلتر دامنه


Was this useful?YesNo