---
title: اكتشاف حلقة الأدوات
source_url: https://docs.openclaw.ai/ar/tools/loop-detection
scraped_at: 2026-05-25
---

لدى OpenClaw آليتا حماية متعاونتان لأنماط استدعاء الأدوات المتكررة:

  1. **اكتشاف الحلقات** (`tools.loopDetection.enabled`) — معطل افتراضيًا. يراقب سجل استدعاءات الأدوات المتحرك بحثًا عن الأنماط المتكررة وإعادات المحاولة لأدوات غير معروفة.
  2. **حارس ما بعد Compaction** (`tools.loopDetection.postCompactionGuard`) — مفعّل افتراضيًا ما لم تكن `tools.loopDetection.enabled` مضبوطة صراحةً على `false`. يتسلح بعد كل إعادة محاولة بعد Compaction ويجهض التشغيل عندما يصدر الوكيل الثلاثية نفسها `(tool, args, result)` ضمن النافذة.


تتم تهيئة كليهما ضمن كتلة `tools.loopDetection` نفسها، لكن حارس ما بعد Compaction يعمل كلما لم يكن المفتاح الرئيسي متوقفًا صراحةً. اضبط `tools.loopDetection.enabled: false` لإسكات السطحين كليهما.

## سبب وجود هذا

  * اكتشاف التسلسلات المتكررة التي لا تحقق تقدمًا.
  * اكتشاف حلقات عدم وجود نتائج عالية التكرار (الأداة نفسها، المدخلات نفسها، أخطاء متكررة).
  * اكتشاف أنماط استدعاءات متكررة محددة لأدوات polling معروفة.
  * منع دورات تجاوز السياق ثم Compaction ثم الحلقة نفسها من الاستمرار إلى أجل غير مسمى.


## كتلة التهيئة

الإعدادات الافتراضية العامة، مع عرض كل حقل موثق:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

تجاوز لكل وكيل (اختياري):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### سلوك الحقول

الحقل | الافتراضي | التأثير  
---|---|---  
`enabled` | `false` | المفتاح الرئيسي لكواشف السجل المتحرك. يؤدي ضبطه على `false` أيضًا إلى تعطيل حارس ما بعد Compaction.  
`historySize` | `30` | عدد استدعاءات الأدوات الحديثة المحتفظ بها للتحليل.  
`warningThreshold` | `10` | العتبة التي قبلها يُصنف النمط كتحذير فقط.  
`criticalThreshold` | `20` | عتبة حظر أنماط حلقات عدم التقدم المتكررة.  
`unknownToolThreshold` | `10` | حظر الاستدعاءات المتكررة إلى الأداة غير المتاحة نفسها بعد هذا العدد من الإخفاقات.  
`globalCircuitBreakerThreshold` | `30` | عتبة قاطع عدم التقدم العام عبر جميع الكواشف.  
`detectors.genericRepeat` | `true` | يحذر من أنماط تكرار الأداة نفسها + المعلمات نفسها، ويحظر عندما تعيد الاستدعاءات نفسها نتائج متطابقة أيضًا.  
`detectors.knownPollNoProgress` | `true` | يكتشف الأنماط المعروفة الشبيهة بـ polling دون تغير في الحالة.  
`detectors.pingPong` | `true` | يكتشف أنماط ping-pong المتناوبة.  
`postCompactionGuard.windowSize` | `3` | عدد استدعاءات الأدوات بعد Compaction التي يبقى الحارس خلالها مسلحًا، وعدد الثلاثيات المتطابقة الذي يجهض التشغيل.  
  
بالنسبة إلى `exec`، تقارن فحوص عدم التقدم نتائج الأوامر المستقرة وتتجاهل بيانات وقت التشغيل المتقلبة مثل المدة وPID ومعرّف الجلسة ودليل العمل. عندما يكون معرّف تشغيل متاحًا، يُقيّم سجل استدعاءات الأدوات الحديثة ضمن ذلك التشغيل فقط، بحيث لا ترث دورات Heartbeat المجدولة وعمليات التشغيل الجديدة أعداد حلقات قديمة من عمليات تشغيل سابقة.

## الإعداد الموصى به

  * للنماذج الأصغر، اضبط `enabled: true` واترك العتبات على قيمها الافتراضية. نادرًا ما تحتاج النماذج الرائدة إلى اكتشاف السجل المتحرك، ويمكنها إبقاء المفتاح الرئيسي على `false` مع الاستفادة من حارس ما بعد Compaction.
  * أبقِ العتبات مرتبة على النحو `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * إذا حدثت نتائج إيجابية كاذبة: 
    * ارفع `warningThreshold` و/أو `criticalThreshold`.
    * اختياريًا ارفع `globalCircuitBreakerThreshold`.
    * عطّل الكاشف المحدد الذي يسبب المشكلات فقط (`detectors.<name>: false`).
    * قلّل `historySize` لسياق تاريخي أقل صرامة.
  * لتعطيل كل شيء (بما في ذلك حارس ما بعد Compaction)، اضبط `tools.loopDetection.enabled: false` صراحةً.


## حارس ما بعد Compaction

عندما يكمل المشغّل إعادة محاولة Compaction بعد تجاوز السياق، يسلّح حارسًا قصير النافذة يراقب استدعاءات الأدوات القليلة التالية. إذا أصدر الوكيل الثلاثية نفسها `(toolName, argsHash, resultHash)` عدة مرات ضمن النافذة، يستنتج الحارس أن Compaction لم يكسر الحلقة ويجهض التشغيل بخطأ `compaction_loop_persisted`.

يُضبط الحارس عبر علم `tools.loopDetection.enabled` الرئيسي مع تفصيل واحد: يبقى **مفعّلًا عندما يكون العلم غير مضبوط أو`true`** ولا يتعطل إلا عندما يكون العلم `false` صراحةً. هذا مقصود. يوجد الحارس للخروج من حلقات Compaction التي كانت ستحرق رموزًا غير محدودة، لذا يحصل المستخدم بلا تهيئة على الحماية كذلك.

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * قيمة `windowSize` الأقل أكثر صرامة (محاولات أقل قبل الإجهاض).
  * قيمة `windowSize` الأعلى تمنح الوكيل محاولات تعافٍ أكثر.
  * لا يجهض الحارس أبدًا عندما تتغير النتائج، بل فقط عندما تكون النتائج متطابقة بايتًا عبر النافذة.
  * نطاقه ضيق عمدًا: لا يعمل إلا مباشرةً بعد إعادة محاولة Compaction.


## السجلات والسلوك المتوقع

عند اكتشاف حلقة، يبلغ OpenClaw عن حدث حلقة وإما يخفف دورة الأداة التالية أو يحظرها حسب الشدة. يحمي هذا المستخدمين من إنفاق الرموز المنفلت والتوقفات مع الحفاظ على وصول الأدوات الطبيعي.

  * تأتي التحذيرات أولًا.
  * يتبعها الكبح عندما تستمر الأنماط بعد عتبة التحذير.
  * تحظر العتبات الحرجة دورة الأداة التالية وتعرض سبب اكتشاف الحلقة بوضوح في سجل التشغيل.
  * يصدر حارس ما بعد Compaction أخطاء `compaction_loop_persisted` مع اسم الأداة المخالفة وعدد الاستدعاءات المتطابقة.


## ذات صلة

[**موافقات Exec** سياسة السماح/الرفض لتنفيذ shell. ](</ar/tools/exec-approvals>) [**مستويات التفكير** مستويات جهد الاستدلال وتفاعل سياسة المزوّد. ](</ar/tools/thinking>) [**الوكلاء الفرعيون** إنشاء وكلاء معزولين لحصر السلوك المنفلت. ](</ar/tools/subagents>) [**مرجع التهيئة** مخطط `tools.loopDetection` الكامل ودلالات الدمج. ](</ar/gateway/configuration-reference>)

Was this useful?YesNo