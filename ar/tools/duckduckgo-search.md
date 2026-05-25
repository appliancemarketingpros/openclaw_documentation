---
title: بحث DuckDuckGo
source_url: https://docs.openclaw.ai/ar/tools/duckduckgo-search
scraped_at: 2026-05-25
---

يدعم OpenClaw DuckDuckGo بوصفه مزوّد `web_search` **بلا مفتاح**. لا يلزم أي مفتاح API أو حساب.

## الإعداد

لا حاجة إلى مفتاح API - فقط اضبط DuckDuckGo كمزوّدك:

* ### التكوين

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## التكوين

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

إعدادات اختيارية على مستوى Plugin للمنطقة وSafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## معاملات الأداة

استعلام البحث.

النتائج المطلوب إرجاعها (1-10).

رمز منطقة DuckDuckGo (مثل `us-en`، `uk-en`، `de-de`).

مستوى SafeSearch.

يمكن أيضًا ضبط المنطقة وSafeSearch في تكوين Plugin (انظر أعلاه) - معاملات الأداة تتجاوز قيم التكوين لكل استعلام.

## ملاحظات

  * **لا يوجد مفتاح API** \- يعمل مباشرة، بدون أي تكوين
  * **تجريبي** \- يجمع النتائج من صفحات بحث HTML غير المعتمدة على JavaScript في DuckDuckGo، وليس من API أو SDK رسمي
  * **خطر تحدّي البوتات** \- قد يعرض DuckDuckGo اختبارات CAPTCHA أو يحظر الطلبات عند الاستخدام الكثيف أو الآلي
  * **تحليل HTML** \- تعتمد النتائج على بنية الصفحة، والتي يمكن أن تتغيّر بدون إشعار
  * **ترتيب الاكتشاف التلقائي** \- DuckDuckGo هو أول بديل بلا مفتاح (الترتيب 100) في الاكتشاف التلقائي. تعمل المزوّدات المدعومة بواجهة API ذات المفاتيح المكوّنة أولًا، ثم Ollama Web Search (الترتيب 110)، ثم SearXNG (الترتيب 200)
  * **SafeSearch افتراضيًا moderate** عندما لا يكون مكوّنًا


## ذو صلة

  * [نظرة عامة على Web Search](</ar/tools/web>) \-- جميع المزوّدات والاكتشاف التلقائي
  * [Brave Search](</ar/tools/brave-search>) \-- نتائج منظمة مع طبقة مجانية
  * [Exa Search](</ar/tools/exa-search>) \-- بحث عصبي مع استخراج المحتوى


Was this useful?YesNo