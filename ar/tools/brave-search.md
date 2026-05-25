---
title: بحث Brave
source_url: https://docs.openclaw.ai/ar/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw يدعم Brave Search API كمزود `web_search`.

## الحصول على مفتاح API

  1. أنشئ حساب Brave Search API على <https://brave.com/search/api/>
  2. في لوحة التحكم، اختر خطة **Search** وأنشئ مفتاح API.
  3. خزّن المفتاح في الإعدادات أو اضبط `BRAVE_API_KEY` في بيئة Gateway.


## مثال الإعدادات

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

إعدادات بحث Brave الخاصة بالمزود أصبحت الآن ضمن `plugins.entries.brave.config.webSearch.*`. لا يزال `tools.web.search.apiKey` القديم يُحمّل عبر طبقة التوافق، لكنه لم يعد مسار الإعدادات المعتمد.

يتحكم `webSearch.mode` في نقل Brave:

  * `web` (الافتراضي): بحث ويب Brave عادي مع عناوين وروابط URL ومقتطفات
  * `llm-context`: Brave LLM Context API مع مقاطع نصية ومصادر مستخرجة مسبقًا للتأصيل


يمكن أن يشير `webSearch.baseUrl` بطلبات Brave إلى وكيل موثوق متوافق مع Brave أو gateway. يضيف OpenClaw المسار `/res/v1/web/search` أو `/res/v1/llm/context` إلى عنوان URL الأساسي المضبوط، ويحافظ على عنوان URL الأساسي في مفتاح التخزين المؤقت. يجب أن تستخدم نقاط النهاية العامة `https://`؛ ولا يُقبل `http://` إلا لمضيفي local loopback الموثوقين أو مضيفي وكلاء الشبكات الخاصة.

## معاملات الأداة

استعلام البحث.

عدد النتائج المراد إرجاعها (1–10).

رمز البلد وفق ISO من حرفين (مثل `US` و`DE`).

رمز لغة ISO 639-1 لنتائج البحث (مثل `en` و`de` و`fr`).

رمز لغة البحث في Brave (مثل `en` و`en-gb` و`zh-hans`).

رمز لغة ISO لعناصر واجهة المستخدم.

مرشح الوقت — `day` تعني 24 ساعة.

النتائج المنشورة بعد هذا التاريخ فقط (`YYYY-MM-DD`).

النتائج المنشورة قبل هذا التاريخ فقط (`YYYY-MM-DD`).

**أمثلة:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## ملاحظات

  * يستخدم OpenClaw خطة **Search** من Brave. إذا كان لديك اشتراك قديم (مثل الخطة Free الأصلية مع 2,000 استعلام/شهر)، فسيظل صالحًا لكنه لا يتضمن ميزات أحدث مثل LLM Context أو حدود معدلات أعلى.
  * تتضمن كل خطة من Brave **رصيدًا مجانيًا قدره $5/شهر** (يتجدد). تبلغ تكلفة خطة Search ‏$5 لكل 1,000 طلب، لذا يغطي الرصيد 1,000 استعلام/شهر. اضبط حد الاستخدام في لوحة تحكم Brave لتجنب الرسوم غير المتوقعة. راجع [بوابة Brave API](<https://brave.com/search/api/>) للاطلاع على الخطط الحالية.
  * تتضمن خطة Search نقطة نهاية LLM Context وحقوق استدلال الذكاء الاصطناعي. يتطلب تخزين النتائج لتدريب النماذج أو ضبطها خطة ذات حقوق تخزين صريحة. راجع [شروط خدمة](<https://api-dashboard.search.brave.com/terms-of-service>) Brave.
  * يعيد وضع `llm-context` إدخالات مصادر مؤصلة بدلًا من شكل مقتطفات بحث الويب العادي.
  * يدعم وضع `llm-context` النطاقات `freshness` والنطاقات المحددة بـ `date_after` \+ `date_before`. ولا يدعم `ui_lang`؛ ويتم رفض `date_before` بدون `date_after` لأن Brave يتطلب أن تتضمن نطاقات الحداثة المخصصة تاريخي بداية ونهاية.
  * يجب أن يتضمن `ui_lang` وسمًا فرعيًا للمنطقة مثل `en-US`.
  * تُخزّن النتائج مؤقتًا لمدة 15 دقيقة افتراضيًا (قابلة للضبط عبر `cacheTtlMinutes`).
  * تُضمّن قيم `webSearch.baseUrl` المخصصة في هوية ذاكرة التخزين المؤقت لـ Brave، بحيث لا تتصادم الاستجابات الخاصة بالوكيل.
  * فعّل علم التشخيصات `brave.http` لتسجيل عناوين URL/معاملات الاستعلام لطلبات Brave، وحالة الاستجابة/توقيتها، وأحداث إصابة/فوات/كتابة ذاكرة التخزين المؤقت للبحث أثناء استكشاف المشكلات وإصلاحها. لا يسجل العلم مفتاح API أو أجسام الاستجابات مطلقًا، لكن استعلامات البحث قد تكون حساسة.


## ذات صلة

  * [نظرة عامة على بحث الويب](</ar/tools/web>) \-- جميع المزودين والاكتشاف التلقائي
  * [بحث Perplexity](</ar/tools/perplexity-search>) \-- نتائج منظمة مع ترشيح النطاقات
  * [بحث Exa](</ar/tools/exa-search>) \-- بحث عصبي مع استخراج المحتوى


Was this useful?YesNo