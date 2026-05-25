---
title: Tavily
source_url: https://docs.openclaw.ai/fa/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) یک API جست‌وجو است که برای برنامه‌های AI طراحی شده است. OpenClaw آن را به دو روش ارائه می‌کند:

  * به‌عنوان ارائه‌دهنده‌ی `web_search` برای ابزار جست‌وجوی عمومی
  * به‌عنوان ابزارهای صریح Plugin: ‏`tavily_search` و `tavily_extract`


Tavily نتایج ساختاریافته‌ای برمی‌گرداند که برای مصرف LLM بهینه شده‌اند و عمق جست‌وجوی قابل پیکربندی، فیلتر موضوع، فیلترهای دامنه، خلاصه پاسخ‌های تولیدشده با AI، و استخراج محتوا از URLها (از جمله صفحه‌های رندرشده با JavaScript) را پشتیبانی می‌کنند.

ویژگی | مقدار  
---|---  
شناسه Plugin | `tavily`  
احراز هویت | `TAVILY_API_KEY` یا پیکربندی `apiKey`  
URL پایه | `https://api.tavily.com` (پیش‌فرض)  
ابزارهای همراه | `tavily_search`, `tavily_extract`  
  
## شروع به کار

* ### دریافت یک کلید API

در [tavily.com](<https://tavily.com>) یک حساب Tavily بسازید، سپس در داشبورد یک کلید API ایجاد کنید.

* ### پیکربندی Plugin و ارائه‌دهنده

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### بررسی اجرای جست‌وجو

از هر agent یک `web_search` اجرا کنید، یا مستقیما `tavily_search` را فراخوانی کنید.

## مرجع ابزار

### `tavily_search`

وقتی به کنترل‌های جست‌وجوی اختصاصی Tavily به‌جای `web_search` عمومی نیاز دارید، از این استفاده کنید.

پارامتر | نوع | محدودیت‌ها / پیش‌فرض | توضیح  
---|---|---|---  
`query` | string | الزامی | رشته پرس‌وجوی جست‌وجو. کمتر از 400 نویسه نگه دارید.  
`search_depth` | enum | `basic` (پیش‌فرض), `advanced` | `advanced` کندتر است اما ارتباط بالاتری دارد.  
`topic` | enum | `general` (پیش‌فرض), `news`, `finance` | فیلتر بر اساس خانواده موضوع.  
`max_results` | integer | 1-20 | تعداد نتایج.  
`include_answer` | boolean | پیش‌فرض `false` | شامل‌کردن خلاصه پاسخ تولیدشده با AI توسط Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | فیلتر نتایج بر اساس تازگی.  
`include_domains` | string array | (هیچ‌کدام) | فقط نتایج این دامنه‌ها را شامل شود.  
`exclude_domains` | string array | (هیچ‌کدام) | نتایج این دامنه‌ها حذف شود.  
  
موازنه عمق جست‌وجو:

عمق | سرعت | ارتباط | بهترین کاربرد  
---|---|---|---  
`basic` | سریع‌تر | بالا | پرس‌وجوهای عمومی (پیش‌فرض).  
`advanced` | کندتر | بالاترین | پژوهش دقیق و حقیقت‌یابی.  
  
### `tavily_extract`

از این برای استخراج محتوای تمیز از یک یا چند URL استفاده کنید. صفحه‌های رندرشده با JavaScript را مدیریت می‌کند و برای استخراج هدفمند، قطعه‌بندی متمرکز بر پرس‌وجو را پشتیبانی می‌کند.

پارامتر | نوع | محدودیت‌ها / پیش‌فرض | توضیح  
---|---|---|---  
`urls` | string array | الزامی، 1-20 | URLهایی که محتوا از آن‌ها استخراج می‌شود.  
`query` | string | (اختیاری) | رتبه‌بندی دوباره قطعه‌های استخراج‌شده بر اساس ارتباط با این پرس‌وجو.  
`extract_depth` | enum | `basic` (پیش‌فرض), `advanced` | از `advanced` برای صفحه‌های سنگین از نظر JS، SPAها، یا جدول‌های پویا استفاده کنید.  
`chunks_per_source` | integer | 1-5؛ **به`query` نیاز دارد** | قطعه‌های برگشتی به‌ازای هر URL. اگر بدون `query` تنظیم شود خطا می‌دهد.  
`include_images` | boolean | پیش‌فرض `false` | شامل‌کردن URLهای تصویر در نتایج.  
  
موازنه عمق استخراج:

عمق | زمان استفاده  
---|---  
`basic` | صفحه‌های ساده. ابتدا این را امتحان کنید.  
`advanced` | SPAهای رندرشده با JS، محتوای پویا، جدول‌ها.  
  
## انتخاب ابزار مناسب

نیاز | ابزار  
---|---  
جست‌وجوی سریع وب، بدون گزینه‌های ویژه | `web_search`  
جست‌وجو با عمق، موضوع، پاسخ‌های AI | `tavily_search`  
استخراج محتوا از URLهای مشخص | `tavily_extract`  
  
## پیکربندی پیشرفته

ترتیب یافتن کلید API

کلاینت Tavily کلید API خود را به این ترتیب جست‌وجو می‌کند:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (حل‌شده از طریق SecretRefs).
  2. `TAVILY_API_KEY` از محیط gateway.


اگر هیچ‌کدام وجود نداشته باشد، `tavily_extract` خطای راه‌اندازی ایجاد می‌کند.

URL پایه سفارشی

اگر Tavily را از طریق یک proxy در جلو قرار می‌دهید، `plugins.entries.tavily.config.webSearch.baseUrl` را بازنویسی کنید. مقدار پیش‌فرض `https://api.tavily.com` است.

`chunks_per_source` به `query` نیاز دارد

`tavily_extract` فراخوانی‌هایی را که `chunks_per_source` را بدون `query` ارسال می‌کنند رد می‌کند. Tavily قطعه‌ها را بر اساس ارتباط با پرس‌وجو رتبه‌بندی می‌کند، بنابراین این پارامتر بدون آن بی‌معنا است.

## مرتبط

[**نمای کلی جست‌وجوی وب** همه ارائه‌دهنده‌ها و قواعد تشخیص خودکار. ](</fa/tools/web>) [**Firecrawl** جست‌وجو به‌همراه scraping با استخراج محتوا. ](</fa/tools/firecrawl>) [**جست‌وجوی Exa** جست‌وجوی عصبی با استخراج محتوا. ](</fa/tools/exa-search>) [**پیکربندی** schema کامل پیکربندی برای ورودی‌های Plugin و مسیریابی ابزار. ](</fa/gateway/configuration>)

Was this useful?YesNo