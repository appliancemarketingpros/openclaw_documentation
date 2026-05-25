---
title: محرك السياق
source_url: https://docs.openclaw.ai/ar/concepts/context-engine
scraped_at: 2026-05-25
---

يعالج **محرك السياق** كيفية بناء OpenClaw لسياق النموذج لكل تشغيل: أي الرسائل يجب تضمينها، وكيفية تلخيص السجل الأقدم، وكيفية إدارة السياق عبر حدود الوكلاء الفرعيين.

يأتي OpenClaw مع محرك `legacy` مدمج ويستخدمه افتراضيا - ولا يحتاج معظم المستخدمين إلى تغيير ذلك أبدا. ثبّت محرك Plugin وحدده فقط عندما تريد سلوكا مختلفا في التجميع أو Compaction أو الاستدعاء عبر الجلسات.

## البدء السريع

* ### تحقق من المحرك النشط

bashCopy code
[code]
    openclaw doctor# or inspect config directly:cat ~/.openclaw/openclaw.json | jq '.plugins.slots.contextEngine'
[/code]

* ### ثبّت محرك Plugin

تثبت Plugins محرك السياق مثل أي Plugin آخر في OpenClaw.

### من npm

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### من مسار محلي

bashCopy code
[code]
    openclaw plugins install -l ./my-context-engine
[/code]

* ### فعّل المحرك وحدده

json5Copy code
[code]
    // openclaw.json{  plugins: {    slots: {      contextEngine: "lossless-claw", // must match the plugin's registered engine id    },    entries: {      "lossless-claw": {        enabled: true,        // Plugin-specific config goes here (see the plugin's docs)      },    },  },}
[/code]

أعد تشغيل Gateway بعد التثبيت والتهيئة.

* ### الرجوع إلى legacy (اختياري)

اضبط `contextEngine` على `"legacy"` (أو أزل المفتاح بالكامل - `"legacy"` هو الافتراضي).

## كيف يعمل

في كل مرة يشغّل فيها OpenClaw موجها للنموذج، يشارك محرك السياق في أربع نقاط من دورة الحياة:

1\. الاستيعاب

يستدعى عند إضافة رسالة جديدة إلى الجلسة. يستطيع المحرك تخزين الرسالة أو فهرستها في مخزن البيانات الخاص به.

2\. التجميع

يستدعى قبل كل تشغيل للنموذج. يعيد المحرك مجموعة مرتبة من الرسائل (و`systemPromptAddition` اختياريا) تناسب ميزانية الرموز.

3\. Compact

يستدعى عندما تمتلئ نافذة السياق، أو عندما يشغّل المستخدم `/compact`. يلخص المحرك السجل الأقدم لتحرير مساحة.

4\. بعد الدور

يستدعى بعد اكتمال التشغيل. يستطيع المحرك حفظ الحالة، أو تشغيل Compaction في الخلفية، أو تحديث الفهارس.

بالنسبة إلى حزمة Codex غير ACP المضمنة، يطبق OpenClaw دورة الحياة نفسها من خلال إسقاط السياق المجمع في تعليمات مطور Codex وموجه الدور الحالي. لا يزال Codex يملك سجل السلسلة الأصلي والضاغط الأصلي الخاصين به.

### دورة حياة الوكيل الفرعي (اختيارية)

يستدعي OpenClaw خطافي دورة حياة اختياريين للوكلاء الفرعيين:

جهّز حالة السياق المشتركة قبل بدء تشغيل تابع. يتلقى الخطاف مفاتيح جلسة الأصل/التابع، و`contextMode` (`isolated` أو `fork`)، ومعرفات/ملفات النصوص المتاحة، وTTL اختياريا. إذا أعاد مقبض تراجع، يستدعيه OpenClaw عندما يفشل الإنشاء بعد نجاح التحضير.

نظّف عند اكتمال جلسة وكيل فرعي أو كنسها.

### إضافة موجه النظام

يمكن لطريقة `assemble` إرجاع سلسلة `systemPromptAddition`. يضيف OpenClaw هذه السلسلة في بداية موجه النظام للتشغيل. يتيح ذلك للمحركات حقن إرشادات استدعاء ديناميكية، أو تعليمات استرجاع، أو تلميحات واعية بالسياق من دون الحاجة إلى ملفات مساحة عمل ثابتة.

## محرك legacy

يحافظ محرك `legacy` المدمج على السلوك الأصلي لـ OpenClaw:

  * **الاستيعاب** : لا عملية (يتولى مدير الجلسات حفظ الرسائل مباشرة).
  * **التجميع** : تمرير مباشر (يتولى مسار التعقيم → التحقق → الحد الحالي في وقت التشغيل تجميع السياق).
  * **Compact** : يفوض إلى Compaction التلخيص المدمج، الذي ينشئ ملخصا واحدا للرسائل الأقدم ويبقي الرسائل الحديثة كما هي.
  * **بعد الدور** : لا عملية.


لا يسجل محرك legacy أدوات ولا يوفر `systemPromptAddition`.

عندما لا يتم تعيين `plugins.slots.contextEngine` (أو يتم تعيينه إلى `"legacy"`)، يستخدم هذا المحرك تلقائيا.

## محركات Plugin

يمكن لـ Plugin تسجيل محرك سياق باستخدام واجهة برمجة تطبيقات Plugin:

tsCopy code
[code]
     export default function register(api) {  api.registerContextEngine("my-engine", (ctx) => ({    info: {      id: "my-engine",      name: "My Context Engine",      ownsCompaction: true,    },     async ingest({ sessionId, message, isHeartbeat }) {      // Store the message in your data store      return { ingested: true };    },     async assemble({ sessionId, messages, tokenBudget, availableTools, citationsMode }) {      // Return messages that fit the budget      return {        messages: buildContext(messages, tokenBudget),        estimatedTokens: countTokens(messages),        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },     async compact({ sessionId, force }) {      // Summarize older context      return { ok: true, compacted: true };    },  }));}
[/code]

يتضمن المصنع `ctx` قيما اختيارية هي `config` و`agentDir` و`workspaceDir` حتى تتمكن Plugins من تهيئة حالة لكل وكيل أو لكل مساحة عمل قبل تشغيل أول خطاف من دورة الحياة.

ثم فعّله في الإعدادات:

json5Copy code
[code]
    {  plugins: {    slots: {      contextEngine: "my-engine",    },    entries: {      "my-engine": {        enabled: true,      },    },  },}
[/code]

### واجهة ContextEngine

الأعضاء المطلوبة:

العضو | النوع | الغرض  
---|---|---  
`info` | خاصية | معرف المحرك، واسمه، وإصداره، وما إذا كان يملك Compaction  
`ingest(params)` | طريقة | تخزين رسالة واحدة  
`assemble(params)` | طريقة | بناء سياق لتشغيل نموذج (يعيد `AssembleResult`)  
`compact(params)` | طريقة | تلخيص/تقليل السياق  
  
يعيد `assemble` قيمة `AssembleResult` تحتوي على:

الرسائل المرتبة لإرسالها إلى النموذج.

تقدير المحرك لإجمالي الرموز في السياق المجمع. يستخدم OpenClaw هذا لاتخاذ قرارات عتبة Compaction ولتقارير التشخيص.

يضاف إلى بداية موجه النظام.

يتحكم في تقدير الرموز الذي يستخدمه المشغّل لفحوصات تجاوز السعة الاستباقية. القيمة الافتراضية هي `"assembled"`، ما يعني أن تقدير الموجه المجمع فقط هو الذي يفحص - وهذا مناسب للمحركات التي تعيد سياقا نافذيا مكتفيا بذاته. اضبطه على `"preassembly_may_overflow"` فقط عندما يمكن للعرض المجمع لديك إخفاء خطر تجاوز السعة في النص الأساسي؛ حينها يأخذ المشغّل الحد الأقصى بين التقدير المجمع وتقدير سجل الجلسة قبل التجميع (غير النافذي) عند تقرير ما إذا كان ينبغي إجراء Compaction استباقيا. في كلتا الحالتين، الرسائل التي تعيدها هي ما يراه النموذج فعلا - لا يؤثر `promptAuthority` إلا في الفحص المسبق.

يعيد `compact` قيمة `CompactResult`. عندما يدوّر Compaction النص النشط، يحدد `result.sessionId` و`result.sessionFile` جلسة الخلف التي يجب أن تستخدمها المحاولة التالية أو الدور التالي.

الأعضاء الاختيارية:

العضو | النوع | الغرض  
---|---|---  
`bootstrap(params)` | طريقة | تهيئة حالة المحرك لجلسة. يستدعى مرة واحدة عندما يرى المحرك جلسة لأول مرة (مثلا، استيراد السجل).  
`ingestBatch(params)` | طريقة | استيعاب دور مكتمل كدفعة. يستدعى بعد اكتمال التشغيل، مع كل رسائل ذلك الدور دفعة واحدة.  
`afterTurn(params)` | طريقة | عمل دورة الحياة بعد التشغيل (حفظ الحالة، تشغيل Compaction في الخلفية).  
`prepareSubagentSpawn(params)` | طريقة | إعداد حالة مشتركة لجلسة تابعة قبل أن تبدأ.  
`onSubagentEnded(params)` | طريقة | التنظيف بعد انتهاء وكيل فرعي.  
`dispose()` | طريقة | تحرير الموارد. يستدعى أثناء إيقاف Gateway أو إعادة تحميل Plugin - وليس لكل جلسة.  
  
### ownsCompaction

يتحكم `ownsCompaction` فيما إذا كان Compaction التلقائي المدمج داخل محاولة Pi يبقى مفعلا للتشغيل:

ownsCompaction: true

يملك المحرك سلوك Compaction. يعطل OpenClaw Compaction التلقائي المدمج في Pi لذلك التشغيل، ويكون تنفيذ `compact()` في المحرك مسؤولا عن `/compact`، وCompaction استعادة تجاوز السعة، وأي Compaction استباقي يريد تنفيذه في `afterTurn()`. قد يظل OpenClaw يشغّل أداة الحماية من تجاوز السعة قبل الموجه؛ وعندما تتوقع أن النص الكامل سيتجاوز السعة، يستدعي مسار الاسترداد `compact()` الخاص بالمحرك النشط قبل إرسال موجه آخر.

ownsCompaction: false أو غير معين

قد يظل Compaction التلقائي المدمج في Pi يعمل أثناء تنفيذ الموجه، لكن طريقة `compact()` الخاصة بالمحرك النشط تظل تستدعى من أجل `/compact` واستعادة تجاوز السعة.

يعني ذلك أن هناك نمطين صالحين لـ Plugin:

### وضع الامتلاك

نفّذ خوارزمية Compaction الخاصة بك واضبط `ownsCompaction: true`.

### وضع التفويض

اضبط `ownsCompaction: false` واجعل `compact()` يستدعي `delegateCompactionToRuntime(...)` من `openclaw/plugin-sdk/core` لاستخدام سلوك Compaction المدمج في OpenClaw.

إن `compact()` الذي لا يفعل شيئا غير آمن لمحرك نشط غير مالك، لأنه يعطل مسار `/compact` وCompaction استعادة تجاوز السعة الطبيعيين لفتحة ذلك المحرك.

## مرجع الإعدادات

json5Copy code
[code]
    {  plugins: {    slots: {      // Select the active context engine. Default: "legacy".      // Set to a plugin id to use a plugin engine.      contextEngine: "legacy",    },  },}
[/code]

## العلاقة بـ Compaction والذاكرة

Compaction

Compaction هي إحدى مسؤوليات محرك السياق. يفوض المحرك القديم إلى التلخيص المدمج في OpenClaw. يمكن لمحركات Plugin تنفيذ أي استراتيجية Compaction (ملخصات DAG، واسترجاع المتجهات، وما إلى ذلك).

Memory plugins

تكون Plugins الذاكرة (`plugins.slots.memory`) منفصلة عن محركات السياق. توفر Plugins الذاكرة البحث/الاسترجاع؛ وتتحكم محركات السياق في ما يراه النموذج. يمكنها العمل معًا - فقد يستخدم محرك السياق بيانات Plugin الذاكرة أثناء التجميع. يجب أن تفضل محركات Plugin التي تريد مسار مطالبة الذاكرة النشطة استخدام `buildMemorySystemPromptAddition(...)` من `openclaw/plugin-sdk/core`، الذي يحول أقسام مطالبة الذاكرة النشطة إلى `systemPromptAddition` جاهز للإضافة في البداية. إذا احتاج محرك إلى تحكم أدنى مستوى، فلا يزال بإمكانه سحب الأسطر الخام من `openclaw/plugin-sdk/memory-host-core` عبر `buildActiveMemoryPromptSection(...)`.

Session pruning

لا يزال تشذيب نتائج الأدوات القديمة في الذاكرة يعمل بغض النظر عن محرك السياق النشط.

## نصائح

  * استخدم `openclaw doctor` للتحقق من أن محركك يُحمَّل بشكل صحيح.
  * عند تبديل المحركات، تواصل الجلسات الحالية العمل بسجلها الحالي. يتولى المحرك الجديد التشغيل في الجولات المستقبلية.
  * تُسجل أخطاء المحرك وتظهر في التشخيصات. إذا فشل محرك Plugin في التسجيل أو تعذّر حل معرف المحرك المحدد، لا يعود OpenClaw تلقائيًا إلى البديل؛ تفشل الجولات حتى تصلح Plugin أو تعيد تبديل `plugins.slots.contextEngine` إلى `"legacy"`.
  * لأغراض التطوير، استخدم `openclaw plugins install -l ./my-engine` لربط دليل Plugin محلي دون نسخه.


## ذات صلة

  * [Compaction](</ar/concepts/compaction>) \- تلخيص المحادثات الطويلة
  * [السياق](</ar/concepts/context>) \- كيفية بناء السياق لجولات الوكيل
  * [بنية Plugin](</ar/plugins/architecture>) \- تسجيل Plugins محرك السياق
  * [بيان Plugin](</ar/plugins/manifest>) \- حقول بيان Plugin
  * [Plugins](</ar/tools/plugin>) \- نظرة عامة على Plugin


Was this useful?YesNo