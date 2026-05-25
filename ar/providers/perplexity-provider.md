---
title: Perplexity
source_url: https://docs.openclaw.ai/ar/providers/perplexity-provider
scraped_at: 2026-05-25
---

يوفر Plugin Perplexity إمكانات بحث الويب من خلال Perplexity Search API أو Perplexity Sonar عبر OpenRouter.

الخاصية | القيمة  
---|---  
النوع | مزوّد بحث ويب (وليس مزوّد نماذج)  
المصادقة | `PERPLEXITY_API_KEY` (مباشر) أو `OPENROUTER_API_KEY` (عبر OpenRouter)  
مسار التهيئة | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## البدء

* ### تعيين مفتاح API

شغّل تدفق تهيئة بحث الويب التفاعلي:

bashCopy code
[code]
    openclaw configure --section web
[/code]

أو عيّن المفتاح مباشرةً:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### بدء البحث

سيستخدم الوكيل Perplexity تلقائيًا لعمليات بحث الويب بمجرد تهيئة المفتاح. لا يلزم اتخاذ أي خطوات إضافية.

## أوضاع البحث

يحدد Plugin وسيلة النقل تلقائيًا بناءً على بادئة مفتاح API:

### واجهة API الأصلية من Perplexity (pplx-)

عندما يبدأ مفتاحك بـ `pplx-`، يستخدم OpenClaw واجهة Perplexity Search API الأصلية. تُرجع وسيلة النقل هذه نتائج منظّمة وتدعم مرشحات النطاق واللغة والتاريخ (راجع خيارات التصفية أدناه).

### OpenRouter / Sonar (sk-or-)

عندما يبدأ مفتاحك بـ `sk-or-`، يوجّه OpenClaw الطلبات عبر OpenRouter باستخدام نموذج Perplexity Sonar. تُرجع وسيلة النقل هذه إجابات مركّبة بالذكاء الاصطناعي مع استشهادات.

بادئة المفتاح | وسيلة النقل | الميزات  
---|---|---  
`pplx-` | واجهة Perplexity Search API الأصلية | نتائج منظّمة، مرشحات النطاق/اللغة/التاريخ  
`sk-or-` | OpenRouter (Sonar) | إجابات مركّبة بالذكاء الاصطناعي مع استشهادات  
  
## تصفية API الأصلية

عند استخدام واجهة Perplexity API الأصلية، تدعم عمليات البحث المرشحات التالية:

المرشح | الوصف | المثال  
---|---|---  
البلد | رمز بلد مكوّن من حرفين | `us`, `de`, `jp`  
اللغة | رمز لغة ISO 639-1 | `en`, `fr`, `zh`  
النطاق الزمني | نافذة الحداثة | `day`, `week`, `month`, `year`  
مرشحات النطاق | قائمة سماح أو قائمة حظر (بحد أقصى 20 نطاقًا) | `example.com`  
ميزانية المحتوى | حدود الرموز لكل استجابة / لكل صفحة | `max_tokens`, `max_tokens_per_page`  
  
## التهيئة المتقدمة

متغير البيئة لعمليات الخدمة الخلفية

إذا كان OpenClaw Gateway يعمل كخدمة خلفية (launchd/systemd)، فتأكد من توفر `PERPLEXITY_API_KEY` لتلك العملية.

إعداد وكيل OpenRouter

إذا كنت تفضّل توجيه عمليات بحث Perplexity عبر OpenRouter، فعيّن `OPENROUTER_API_KEY` (بالبادئة `sk-or-`) بدلًا من مفتاح Perplexity الأصلي. سيكتشف OpenClaw البادئة ويتحول إلى وسيلة نقل Sonar تلقائيًا.

## ذو صلة

[**أداة بحث Perplexity** كيف يستدعي الوكيل عمليات بحث Perplexity ويفسّر النتائج. ](</ar/tools/perplexity-search>) [**مرجع التهيئة** مرجع التهيئة الكامل، بما في ذلك إدخالات Plugin. ](</ar/gateway/configuration-reference>)

Was this useful?YesNo