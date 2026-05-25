---
title: جلب الويب
source_url: https://docs.openclaw.ai/ar/tools/web-fetch
scraped_at: 2026-05-25
---

تُجري أداة `web_fetch` طلب HTTP GET عاديًا وتستخرج المحتوى المقروء (من HTML إلى Markdown أو نص). وهي **لا** تنفّذ JavaScript.

للمواقع المعتمدة بكثافة على JS أو الصفحات المحمية بتسجيل الدخول، استخدم [متصفح الويب](</ar/tools/browser>) بدلًا منها.

## البدء السريع

تكون `web_fetch` **مفعّلة افتراضيًا** \-- لا حاجة إلى أي إعداد. يمكن للوكيل استدعاؤها فورًا:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## معاملات الأداة

عنوان URL المطلوب جلبه. `http(s)` فقط.

تنسيق الإخراج بعد استخراج المحتوى الرئيسي.

اقتطاع الإخراج إلى هذا العدد من الأحرف.

## كيف تعمل

* ### الجلب

ترسل طلب HTTP GET مع User-Agent شبيه بـ Chrome وترويسة `Accept-Language`. تحظر أسماء المضيفين الخاصة/الداخلية وتعيد فحص عمليات إعادة التوجيه.

* ### الاستخراج

تشغّل Readability (استخراج المحتوى الرئيسي) على استجابة HTML.

* ### الخيار الاحتياطي (اختياري)

إذا فشل Readability وكان Firecrawl مضبوطًا، تعيد المحاولة عبر Firecrawl API مع وضع تجاوز البوتات.

* ### ذاكرة التخزين المؤقت

تُخزّن النتائج مؤقتًا لمدة 15 دقيقة (قابلة للضبط) لتقليل عمليات الجلب المتكررة لعنوان URL نفسه.

## الإعداد

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## الخيار الاحتياطي Firecrawl

إذا فشل استخراج Readability، يمكن لـ `web_fetch` الرجوع إلى [Firecrawl](</ar/tools/firecrawl>) لتجاوز البوتات وتحسين الاستخراج:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

يدعم `plugins.entries.firecrawl.config.webFetch.apiKey` كائنات SecretRef. تُرحَّل إعدادات `tools.web.fetch.firecrawl.*` القديمة تلقائيًا بواسطة `openclaw doctor --fix`.

سلوك وقت التشغيل الحالي:

  * يحدد `tools.web.fetch.provider` موفر خيار الجلب الاحتياطي صراحةً.
  * إذا حُذف `provider`، يكتشف OpenClaw تلقائيًا أول موفر web-fetch جاهز من بيانات الاعتماد المتاحة. يمكن لـ `web_fetch` غير المعزول استخدام Plugins المثبتة التي تعلن `contracts.webFetchProviders` وتُسجّل موفرًا مطابقًا في وقت التشغيل. حاليًا الموفر المضمّن هو Firecrawl.
  * تبقى استدعاءات `web_fetch` المعزولة مقتصرة على الموفرين المضمّنين.
  * إذا كان Readability معطلًا، يتخطى `web_fetch` مباشرةً إلى الخيار الاحتياطي للموفر المحدد. إذا لم يتوفر أي موفر، فإنه يفشل بشكل مغلق.


## وكيل البيئة الموثوق

إذا كان النشر لديك يتطلب مرور `web_fetch` عبر وكيل HTTP(S) صادر موثوق، فاضبط `tools.web.fetch.useTrustedEnvProxy: true`.

في هذا الوضع، يظل OpenClaw يطبّق فحوصات SSRF المستندة إلى اسم المضيف قبل إرسال الطلب، لكنه يتيح للوكيل حل DNS بدلًا من إجراء تثبيت DNS محلي. فعّل ذلك فقط عندما يكون الوكيل خاضعًا لتحكم المشغّل ويفرض سياسة الصادر بعد حل DNS.

## الحدود والسلامة

  * يُقيّد `maxChars` إلى `tools.web.fetch.maxCharsCap`
  * يُحدّ جسم الاستجابة عند `maxResponseBytes` قبل التحليل؛ وتُقتطع الاستجابات كبيرة الحجم مع تحذير
  * تُحظر أسماء المضيفين الخاصة/الداخلية
  * يُعد `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` و `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` تفعيلين اختياريين ضيقين لمكدسات وكلاء fake-IP الموثوقة؛ اتركهما غير مضبوطين ما لم يكن وكيلك يمتلك تلك النطاقات الاصطناعية ويفرض سياسة وجهته الخاصة
  * تُفحص عمليات إعادة التوجيه وتُحد بواسطة `maxRedirects`
  * يُعد `useTrustedEnvProxy` تفعيلًا اختياريًا صريحًا ويجب ألا يُمكّن إلا للوكلاء الخاضعين لتحكم المشغّل الذين لا يزالون يفرضون سياسة الصادر بعد حل DNS
  * `web_fetch` جهدها الأفضل -- بعض المواقع تحتاج إلى [متصفح الويب](</ar/tools/browser>)


## ملفات تعريف الأدوات

إذا كنت تستخدم ملفات تعريف الأدوات أو قوائم السماح، فأضف `web_fetch` أو `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## ذات صلة

  * [بحث الويب](</ar/tools/web>) \-- ابحث في الويب باستخدام موفرين متعددين
  * [متصفح الويب](</ar/tools/browser>) \-- أتمتة متصفح كاملة للمواقع المعتمدة بكثافة على JS
  * [Firecrawl](</ar/tools/firecrawl>) \-- أدوات البحث والكشط من Firecrawl


Was this useful?YesNo