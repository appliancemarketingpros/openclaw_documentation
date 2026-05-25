---
title: جستجوی Brave
source_url: https://docs.openclaw.ai/fa/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw از Brave Search API به‌عنوان ارائه‌دهندهٔ `web_search` پشتیبانی می‌کند.

## دریافت کلید API

  1. یک حساب Brave Search API در <https://brave.com/search/api/> بسازید
  2. در داشبورد، طرح **Search** را انتخاب کنید و یک کلید API بسازید.
  3. کلید را در پیکربندی ذخیره کنید یا `BRAVE_API_KEY` را در محیط Gateway تنظیم کنید.


## نمونهٔ پیکربندی

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

تنظیمات جست‌وجوی ویژهٔ ارائه‌دهندهٔ Brave اکنون زیر `plugins.entries.brave.config.webSearch.*` قرار دارند. `tools.web.search.apiKey` قدیمی همچنان از طریق شیم سازگاری بارگذاری می‌شود، اما دیگر مسیر پیکربندی معیار نیست.

`webSearch.mode` انتقال Brave را کنترل می‌کند:

  * `web` (پیش‌فرض): جست‌وجوی عادی وب Brave با عنوان‌ها، URLها و قطعه‌متن‌ها
  * `llm-context`: Brave LLM Context API با قطعه‌های متنی و منابع ازپیش‌استخراج‌شده برای اتکاپذیری


`webSearch.baseUrl` می‌تواند درخواست‌های Brave را به یک پراکسی یا Gateway سازگار با Brave و مورداعتماد هدایت کند. OpenClaw مسیر `/res/v1/web/search` یا `/res/v1/llm/context` را به URL پایهٔ پیکربندی‌شده اضافه می‌کند و URL پایه را در کلید کش نگه می‌دارد. نقاط پایانی عمومی باید از `https://` استفاده کنند؛ `http://` فقط برای میزبان‌های پراکسی loopback مورداعتماد یا شبکهٔ خصوصی پذیرفته می‌شود.

## پارامترهای ابزار

پرس‌وجوی جست‌وجو.

تعداد نتایجی که برگردانده می‌شود (۱ تا ۱۰).

کد کشور ISO دوحرفی (برای مثال `US`، `DE`).

کد زبان ISO 639-1 برای نتایج جست‌وجو (برای مثال `en`، `de`، `fr`).

کد زبان جست‌وجوی Brave (برای مثال `en`، `en-gb`، `zh-hans`).

کد زبان ISO برای عناصر UI.

فیلتر زمانی — `day` برابر با ۲۴ ساعت است.

فقط نتایجی که پس از این تاریخ منتشر شده‌اند (`YYYY-MM-DD`).

فقط نتایجی که پیش از این تاریخ منتشر شده‌اند (`YYYY-MM-DD`).

**نمونه‌ها:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## یادداشت‌ها

  * OpenClaw از طرح **Search** در Brave استفاده می‌کند. اگر اشتراک قدیمی دارید (برای مثال طرح Free اصلی با ۲٬۰۰۰ پرس‌وجو در ماه)، همچنان معتبر است، اما قابلیت‌های جدیدتر مانند LLM Context یا محدودیت‌های نرخ بالاتر را شامل نمی‌شود.
  * هر طرح Brave شامل **۵ دلار اعتبار رایگان ماهانه** (با تمدید دوره‌ای) است. طرح Search به‌ازای هر ۱٬۰۰۰ درخواست، ۵ دلار هزینه دارد، بنابراین این اعتبار ۱٬۰۰۰ پرس‌وجو در ماه را پوشش می‌دهد. برای جلوگیری از هزینه‌های غیرمنتظره، محدودیت مصرف خود را در داشبورد Brave تنظیم کنید. برای طرح‌های فعلی، [پورتال Brave API](<https://brave.com/search/api/>) را ببینید.
  * طرح Search شامل نقطهٔ پایانی LLM Context و حقوق استنتاج AI است. ذخیرهٔ نتایج برای آموزش یا تنظیم مدل‌ها به طرحی با حقوق صریح ذخیره‌سازی نیاز دارد. [شرایط خدمات](<https://api-dashboard.search.brave.com/terms-of-service>) Brave را ببینید.
  * حالت `llm-context` به‌جای قالب قطعه‌متن عادی جست‌وجوی وب، ورودی‌های منبع اتکاپذیر برمی‌گرداند.
  * حالت `llm-context` از `freshness` و بازه‌های محدود `date_after` \+ `date_before` پشتیبانی می‌کند. از `ui_lang` پشتیبانی نمی‌کند؛ `date_before` بدون `date_after` رد می‌شود، زیرا Brave الزام می‌کند بازه‌های freshness سفارشی هم تاریخ شروع و هم تاریخ پایان را داشته باشند.
  * `ui_lang` باید شامل یک زیرتگ منطقه مانند `en-US` باشد.
  * نتایج به‌طور پیش‌فرض به‌مدت ۱۵ دقیقه کش می‌شوند (از طریق `cacheTtlMinutes` قابل پیکربندی است).
  * مقدارهای سفارشی `webSearch.baseUrl` در هویت کش Brave گنجانده می‌شوند، بنابراین پاسخ‌های ویژهٔ پراکسی با هم تداخل پیدا نمی‌کنند.
  * برای ثبت URLها/پارامترهای پرس‌وجوی درخواست Brave، وضعیت/زمان‌بندی پاسخ، و رویدادهای برخورد/عدم‌برخورد/نوشتن کش جست‌وجو هنگام عیب‌یابی، پرچم عیب‌یابی `brave.http` را فعال کنید. این پرچم هرگز کلید API یا بدنهٔ پاسخ‌ها را ثبت نمی‌کند، اما پرس‌وجوهای جست‌وجو می‌توانند حساس باشند.


## مرتبط

  * [مرور کلی جست‌وجوی وب](</fa/tools/web>) \-- همهٔ ارائه‌دهندگان و تشخیص خودکار
  * [جست‌وجوی Perplexity](</fa/tools/perplexity-search>) \-- نتایج ساختاریافته با فیلترکردن دامنه
  * [جست‌وجوی Exa](</fa/tools/exa-search>) \-- جست‌وجوی عصبی با استخراج محتوا


Was this useful?YesNo