---
title: بحث Gemini
source_url: https://docs.openclaw.ai/ar/tools/gemini-search
scraped_at: 2026-05-25
---

يدعم OpenClaw نماذج Gemini مع [إسناد Google Search](<https://ai.google.dev/gemini-api/docs/grounding>) المدمج، الذي يعيد إجابات مولّدة بالذكاء الاصطناعي ومدعومة بنتائج Google Search الحية مع استشهادات.

## احصل على مفتاح API

* ### Create a key

انتقل إلى [Google AI Studio](<https://aistudio.google.com/apikey>) وأنشئ مفتاح API.

* ### Store the key

اضبط `GEMINI_API_KEY` في بيئة Gateway، أو أعد استخدام `models.providers.google.apiKey`، أو كوّن مفتاح بحث ويب مخصصًا عبر:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## التكوين

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // optional; falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash", // default          },        },      },    },  },  tools: {    web: {      search: {        provider: "gemini",      },    },  },}
[/code]

**أسبقية بيانات الاعتماد:** يستخدم بحث الويب في Gemini `plugins.entries.google.config.webSearch.apiKey` أولًا، ثم `GEMINI_API_KEY`، ثم `models.providers.google.apiKey`. بالنسبة إلى عناوين URL الأساسية، تكون الأولوية لـ `plugins.entries.google.config.webSearch.baseUrl` المخصص قبل `models.providers.google.baseUrl`.

بالنسبة إلى تثبيت Gateway، ضع مفاتيح البيئة في `~/.openclaw/.env`.

## كيف يعمل

بخلاف موفري البحث التقليديين الذين يعيدون قائمة بالروابط والمقتطفات، يستخدم Gemini إسناد Google Search لإنتاج إجابات مولّدة بالذكاء الاصطناعي مع استشهادات مضمنة. تتضمن النتائج كلًا من الإجابة المولّدة وعناوين URL للمصادر.

  * تُحل عناوين URL للاستشهادات من إسناد Gemini تلقائيًا من عناوين URL لإعادة التوجيه من Google إلى عناوين URL مباشرة.
  * يستخدم حل إعادة التوجيه مسار حارس SSRF (HEAD + فحوصات إعادة التوجيه + التحقق من http/https) قبل إعادة عنوان URL النهائي للاستشهاد.
  * يستخدم حل إعادة التوجيه إعدادات SSRF الافتراضية الصارمة، لذلك تُحظر عمليات إعادة التوجيه إلى أهداف خاصة/داخلية.


## المعاملات المدعومة

يدعم بحث Gemini كلًا من `query` و`freshness` و`date_after` و`date_before`.

يُقبل `count` للتوافق مع `web_search` المشترك، لكن إسناد Gemini لا يزال يعيد إجابة واحدة مولّدة مع استشهادات بدلًا من قائمة نتائج بعدد N.

يقبل `freshness` القيم `day` و`week` و`month` و`year`، والاختصارات المشتركة `pd` و`pw` و`pm` و`py`. يحوّل OpenClaw هذه القيم، أو نطاقًا صريحًا من `date_after`/`date_before`، إلى `timeRangeFilter` الخاص بإسناد Gemini Google Search. لا تُدعم `country` و`language` و`domain_filter`.

## اختيار النموذج

النموذج الافتراضي هو `gemini-2.5-flash` (سريع وفعّال من حيث التكلفة). يمكن استخدام أي نموذج Gemini يدعم الإسناد عبر `plugins.entries.google.config.webSearch.model`.

## تجاوزات عنوان URL الأساسي

اضبط `plugins.entries.google.config.webSearch.baseUrl` عندما يلزم توجيه بحث الويب في Gemini عبر وكيل للمشغّل أو نقطة نهاية مخصصة متوافقة مع Gemini. إذا لم يُضبط ذلك، يعيد بحث الويب في Gemini استخدام `models.providers.google.baseUrl`. تُطبّع قيمة `https://generativelanguage.googleapis.com` الصريحة إلى `https://generativelanguage.googleapis.com/v1beta`؛ وتُبقى مسارات الوكيل المخصصة كما قُدمت بعد إزالة الشرطات المائلة اللاحقة.

## ذو صلة

  * [نظرة عامة على بحث الويب](</ar/tools/web>) \-- جميع الموفّرين والاكتشاف التلقائي
  * [Brave Search](</ar/tools/brave-search>) \-- نتائج منظمة مع مقتطفات
  * [Perplexity Search](</ar/tools/perplexity-search>) \-- نتائج منظمة + استخراج المحتوى


Was this useful?YesNo