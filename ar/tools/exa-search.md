---
title: بحث Exa
source_url: https://docs.openclaw.ai/ar/tools/exa-search
scraped_at: 2026-05-25
---

يدعم OpenClaw ‏[Exa AI](<https://exa.ai/>) كموفر `web_search`. يوفّر Exa أوضاع بحث عصبية، وبالكلمات المفتاحية، وهجينة مع استخراج محتوى مدمج (تمييزات، ونص، وملخصات).

## الحصول على مفتاح API

* ### إنشاء حساب

سجّل في [exa.ai](<https://exa.ai/>) وأنشئ مفتاح API من لوحة التحكم لديك.

* ### تخزين المفتاح

اضبط `EXA_API_KEY` في بيئة Gateway، أو اضبطه عبر:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## الإعدادات

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**بديل البيئة:** اضبط `EXA_API_KEY` في بيئة Gateway. لتثبيت gateway، ضعه في `~/.openclaw/.env`.

## تجاوز عنوان URL الأساسي

اضبط `plugins.entries.exa.config.webSearch.baseUrl` عندما ينبغي أن تمر طلبات بحث Exa عبر وكيل متوافق أو نقطة نهاية Exa بديلة. يقوم OpenClaw بتطبيع المضيفات العارية عبر إضافة `https://` في البداية، ويضيف `/search` إلا إذا كان المسار ينتهي بها بالفعل. تُضمَّن نقطة النهاية المحلولة في مفتاح ذاكرة التخزين المؤقت للبحث، لذلك لا تتم مشاركة النتائج من نقاط نهاية Exa المختلفة.

## معلمات الأداة

استعلام البحث.

النتائج المراد إرجاعها (1–100).

وضع البحث.

مرشح الوقت.

النتائج بعد هذا التاريخ (`YYYY-MM-DD`).

النتائج قبل هذا التاريخ (`YYYY-MM-DD`).

خيارات استخراج المحتوى (انظر أدناه).

### استخراج المحتوى

يمكن لـ Exa إرجاع المحتوى المستخرج إلى جانب نتائج البحث. مرّر كائن `contents` للتفعيل:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

خيار المحتوى | النوع | الوصف  
---|---|---  
`text` | `boolean | { maxCharacters }` | استخراج نص الصفحة الكامل  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | استخراج الجمل الرئيسية  
`summary` | `boolean | { query }` | ملخص مولّد بالذكاء الاصطناعي  
  
### أوضاع البحث

الوضع | الوصف  
---|---  
`auto` | يختار Exa أفضل وضع (الافتراضي)  
`neural` | بحث دلالي/قائم على المعنى  
`fast` | بحث سريع بالكلمات المفتاحية  
`deep` | بحث عميق وشامل  
`deep-reasoning` | بحث عميق مع استدلال  
`instant` | أسرع النتائج  
  
## ملاحظات

  * إذا لم يتم توفير خيار `contents`، يستخدم Exa افتراضيًا `{ highlights: true }` بحيث تتضمن النتائج مقتطفات من الجمل الرئيسية
  * تحتفظ النتائج بحقلي `highlightScores` و`summary` من استجابة API الخاصة بـ Exa عند توفرهما
  * تُستخلص أوصاف النتائج من التمييزات أولًا، ثم الملخص، ثم النص الكامل — أيها كان متوفرًا
  * لا يمكن الجمع بين `freshness` و`date_after`/`date_before` — استخدم وضع ترشيح زمني واحد
  * يمكن إرجاع ما يصل إلى 100 نتيجة لكل استعلام (وفقًا لحدود نوع البحث في Exa)
  * تُخزّن النتائج مؤقتًا لمدة 15 دقيقة افتراضيًا (قابلة للضبط عبر `cacheTtlMinutes`)
  * Exa تكامل API رسمي مع استجابات JSON منظّمة


## ذات صلة

  * [نظرة عامة على بحث الويب](</ar/tools/web>) \-- جميع الموفرين والاكتشاف التلقائي
  * [Brave Search](</ar/tools/brave-search>) \-- نتائج منظّمة مع مرشحات البلد/اللغة
  * [Perplexity Search](</ar/tools/perplexity-search>) \-- نتائج منظّمة مع ترشيح النطاقات


Was this useful?YesNo