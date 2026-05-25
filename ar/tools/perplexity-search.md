---
title: بحث Perplexity
source_url: https://docs.openclaw.ai/ar/tools/perplexity-search
scraped_at: 2026-05-25
---

يدعم OpenClaw واجهة Perplexity Search API كموفّر `web_search`. تُرجع نتائج منظّمة تحتوي على حقول `title` و`url` و`snippet`.

للتوافق، يدعم OpenClaw أيضًا إعدادات Perplexity Sonar/OpenRouter القديمة. إذا كنت تستخدم `OPENROUTER_API_KEY`، أو مفتاحًا يبدأ بـ `sk-or-...` في `plugins.entries.perplexity.config.webSearch.apiKey`، أو ضبطت `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`، فسينتقل الموفّر إلى مسار إكمالات الدردشة ويُرجع إجابات مولّدة بالذكاء الاصطناعي مع اقتباسات بدلًا من نتائج Search API المنظّمة.

## الحصول على مفتاح Perplexity API

  1. أنشئ حساب Perplexity على [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. أنشئ مفتاح API في لوحة التحكم
  3. خزّن المفتاح في الإعدادات أو اضبط `PERPLEXITY_API_KEY` في بيئة Gateway.


## التوافق مع OpenRouter

إذا كنت تستخدم OpenRouter بالفعل مع Perplexity Sonar، فأبقِ `provider: "perplexity"` واضبط `OPENROUTER_API_KEY` في بيئة Gateway، أو خزّن مفتاحًا يبدأ بـ `sk-or-...` في `plugins.entries.perplexity.config.webSearch.apiKey`.

عناصر تحكم التوافق الاختيارية:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## أمثلة الإعدادات

### واجهة Perplexity Search API الأصلية

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### توافق OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## أين تضبط المفتاح

**عبر الإعدادات:** شغّل `openclaw configure --section web`. يخزّن المفتاح في `~/.openclaw/openclaw.json` تحت `plugins.entries.perplexity.config.webSearch.apiKey`. يقبل هذا الحقل أيضًا كائنات SecretRef.

**عبر البيئة:** اضبط `PERPLEXITY_API_KEY` أو `OPENROUTER_API_KEY` في بيئة عملية Gateway. لتثبيت Gateway، ضعه في `~/.openclaw/.env` (أو بيئة خدمتك). راجع [متغيرات البيئة](</ar/help/faq#env-vars-and-env-loading>).

إذا تم تكوين `provider: "perplexity"` وكان SecretRef لمفتاح Perplexity غير قابل للحل ولا يوجد بديل من البيئة، يفشل بدء التشغيل/إعادة التحميل بسرعة.

## معاملات الأداة

تنطبق هذه المعاملات على مسار Perplexity Search API الأصلي.

استعلام البحث.

عدد النتائج المطلوب إرجاعها (1-10).

رمز البلد ISO المكوّن من حرفين (مثل `US`، `DE`).

رمز اللغة ISO 639-1 (مثل `en`، `de`، `fr`).

مرشح الوقت - `day` يعني 24 ساعة.

النتائج المنشورة بعد هذا التاريخ فقط (`YYYY-MM-DD`).

النتائج المنشورة قبل هذا التاريخ فقط (`YYYY-MM-DD`).

مصفوفة قائمة السماح/قائمة الحظر للنطاقات (الحد الأقصى 20).

إجمالي ميزانية المحتوى (الحد الأقصى 1000000).

حد الرموز لكل صفحة.

بالنسبة إلى مسار توافق Sonar/OpenRouter القديم:

  * يتم قبول `query` و`count` و`freshness`
  * `count` مخصص للتوافق فقط هناك؛ تظل الاستجابة إجابة واحدة مولّدة مع اقتباسات بدلًا من قائمة من N نتيجة
  * مرشحات Search API فقط مثل `country` و`language` و`date_after` و`date_before` و`domain_filter` و`max_tokens` و`max_tokens_per_page` تُرجع أخطاء صريحة


**أمثلة:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### قواعد مرشح النطاق

  * 20 نطاقًا كحد أقصى لكل مرشح
  * لا يمكن مزج قائمة السماح وقائمة الحظر في الطلب نفسه
  * استخدم البادئة `-` لإدخالات قائمة الحظر (مثل `["-reddit.com"]`)


## ملاحظات

  * تُرجع Perplexity Search API نتائج بحث ويب منظّمة (`title`، `url`، `snippet`)
  * يؤدي OpenRouter أو تحديد `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` صراحةً إلى إعادة Perplexity إلى إكمالات دردشة Sonar للتوافق
  * يُرجع توافق Sonar/OpenRouter إجابة واحدة مولّدة مع اقتباسات، وليس صفوف نتائج منظّمة
  * تُخزّن النتائج مؤقتًا لمدة 15 دقيقة افتراضيًا (قابل للتكوين عبر `cacheTtlMinutes`)


## ذات صلة

[**نظرة عامة على بحث الويب** جميع الموفّرين وقواعد الاكتشاف التلقائي. ](</ar/tools/web>) [**بحث Brave** نتائج منظّمة مع مرشحات البلد واللغة. ](</ar/tools/brave-search>) [**بحث Exa** بحث عصبي مع استخراج المحتوى. ](</ar/tools/exa-search>) [**وثائق Perplexity Search API** دليل البدء السريع والمرجع الرسميان لـ Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo