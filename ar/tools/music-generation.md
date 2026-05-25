---
title: توليد الموسيقى
source_url: https://docs.openclaw.ai/ar/tools/music-generation
scraped_at: 2026-05-25
---

تتيح أداة `music_generate` للوكيل إنشاء موسيقى أو صوت عبر إمكانات توليد الموسيقى المشتركة مع المزوّدين المكوّنين — Google، MiniMax، وComfyUI المكوّن عبر سير العمل حاليًا.

بالنسبة لتشغيلات الوكيل المدعومة بجلسة، يبدأ OpenClaw توليد الموسيقى كمهمة خلفية، ويتتبعها في سجل المهام، ثم يوقظ الوكيل مرة أخرى عندما يكون المسار جاهزًا حتى يتمكن الوكيل من إخبار المستخدم وإرفاق الصوت النهائي. في محادثات المجموعات/القنوات التي تستخدم التسليم المرئي عبر أداة الرسائل فقط، يمرر الوكيل النتيجة عبر أداة الرسائل. إذا كتب وكيل الإكمال ردًا نهائيًا خاصًا فقط، يعود OpenClaw إلى إرسال مباشر عبر القناة مع الوسائط المولدة. تنبيه الإكمال يحذر الوكيل صراحة من أن الردود النهائية العادية تكون خاصة في تلك المسارات.

## البدء السريع

### Shared provider-backed

* ### Configure auth

عيّن مفتاح API لمزوّد واحد على الأقل — مثلًا `GEMINI_API_KEY` أو `MINIMAX_API_KEY`.

* ### Pick a default model (optional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Ask the agent

_"Generate an upbeat synthpop track about a night drive through a neon city."_

يستدعي الوكيل `music_generate` تلقائيًا. لا حاجة إلى إدراجه في قائمة السماح للأدوات.

بالنسبة للسياقات المتزامنة المباشرة دون تشغيل وكيل مدعوم بجلسة، تظل الأداة المضمّنة ترجع إلى التوليد المضمّن وتعيد مسار الوسائط النهائي في نتيجة الأداة.

### ComfyUI workflow

* ### Configure the workflow

كوّن `plugins.entries.comfy.config.music` باستخدام سير عمل JSON وعُقد المطالبة/الإخراج.

* ### Cloud auth (optional)

بالنسبة إلى Comfy Cloud، عيّن `COMFY_API_KEY` أو `COMFY_CLOUD_API_KEY`.

* ### Call the tool

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

أمثلة على المطالبات:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## المزوّدون المدعومون

المزوّد | النموذج الافتراضي | مدخلات مرجعية | عناصر التحكم المدعومة | المصادقة  
---|---|---|---|---  
ComfyUI | `workflow` | حتى صورة واحدة | موسيقى أو صوت معرّف بواسطة سير العمل | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | حتى 10 صور | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | لا شيء | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` أو MiniMax OAuth  
  
### مصفوفة الإمكانات

عقد الوضع الصريح الذي تستخدمه `music_generate` واختبارات العقد والفحص الحي المشترك:

المزوّد | `generate` | `edit` | حد التحرير | مسارات التشغيل الحي المشتركة  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | صورة واحدة | ليس ضمن الفحص المشترك؛ تغطيه `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 صور | `generate`, `edit`  
MiniMax | ✓ | — | لا شيء | `generate`  
  
استخدم `action: "list"` لفحص المزوّدين والنماذج المشتركة المتاحة وقت التشغيل:

textCopy code
[code]
    /tool music_generate action=list
[/code]

استخدم `action: "status"` لفحص مهمة الموسيقى النشطة المدعومة بجلسة:

textCopy code
[code]
    /tool music_generate action=status
[/code]

مثال توليد مباشر:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## معاملات الأداة

مطالبة توليد الموسيقى. مطلوبة لـ `action: "generate"`.

يعيد `"status"` مهمة الجلسة الحالية؛ ويفحص `"list"` المزوّدين.

تجاوز المزوّد/النموذج (مثل `google/lyria-3-pro-preview`, `comfy/workflow`).

كلمات اختيارية عندما يدعم المزوّد إدخال كلمات صريحًا.

اطلب إخراجًا آليًا فقط عندما يدعمه المزوّد.

مسار أو URL لصورة مرجعية واحدة.

صور مرجعية متعددة (حتى 10 لدى المزوّدين الداعمين).

المدة المستهدفة بالثواني عندما يدعم المزوّد تلميحات المدة.

تلميح تنسيق الإخراج عندما يدعمه المزوّد.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg مهلة طلب المزوّد الاختيارية بالمللي ثانية. عند حذفها، يستخدم OpenClaw `agents.defaults.musicGenerationModel.timeoutMs` إذا كان مكوّنًا. تُرفع القيم الأقل من 10000ms إلى 10000ms ويُبلّغ عنها في نتيجة الأداة. OPENCLAW_DOCS_MARKER:paramClose:

## السلوك غير المتزامن

يعمل توليد الموسيقى المدعوم بجلسة كمهمة خلفية:

  * **مهمة خلفية:** تنشئ `music_generate` مهمة خلفية، وتعيد استجابة بدء/مهمة فورًا، وتنشر المسار النهائي لاحقًا في رسالة متابعة من الوكيل.
  * **منع التكرار:** بينما تكون المهمة `queued` أو `running`، تعيد استدعاءات `music_generate` اللاحقة في الجلسة نفسها حالة المهمة بدلًا من بدء توليد آخر. استخدم `action: "status"` للتحقق صراحة.
  * **بحث الحالة:** يفحص `openclaw tasks list` أو `openclaw tasks show <taskId>` حالات الانتظار والتشغيل والحالات النهائية.
  * **تنبيه الإكمال:** يحقن OpenClaw حدث إكمال داخليًا مرة أخرى في الجلسة نفسها حتى يستطيع النموذج كتابة المتابعة الظاهرة للمستخدم بنفسه.
  * **تلميح المطالبة:** تحصل أدوار المستخدم/الأدوار اليدوية اللاحقة في الجلسة نفسها على تلميح تشغيل صغير عندما تكون مهمة موسيقى قيد التنفيذ بالفعل، حتى لا يستدعي النموذج `music_generate` مرة أخرى دون داع.
  * **رجوع دون جلسة:** تعمل السياقات المباشرة/المحلية دون جلسة وكيل حقيقية بشكل مضمّن وتعيد نتيجة الصوت النهائية في الدور نفسه.


### دورة حياة المهمة

الحالة | المعنى  
---|---  
`queued` | أُنشئت المهمة وتنتظر قبول المزوّد لها.  
`running` | يعالجها المزوّد (عادة من 30 ثانية إلى 3 دقائق حسب المزوّد والمدة).  
`succeeded` | المسار جاهز؛ يستيقظ الوكيل وينشره في المحادثة.  
`failed` | خطأ من المزوّد أو انتهاء مهلة؛ يستيقظ الوكيل مع تفاصيل الخطأ.  
  
تحقق من الحالة من CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## التكوين

### اختيار النموذج

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### ترتيب اختيار المزوّد

يحاول OpenClaw المزوّدين بهذا الترتيب:

  1. معامل `model` من استدعاء الأداة (إذا حدده الوكيل).
  2. `musicGenerationModel.primary` من التكوين.
  3. `musicGenerationModel.fallbacks` بالترتيب.
  4. الاكتشاف التلقائي باستخدام افتراضيات المزوّد المدعومة بالمصادقة فقط: 
     * المزوّد الافتراضي الحالي أولًا؛
     * بقية مزوّدي توليد الموسيقى المسجلين بترتيب معرّف المزوّد.


إذا فشل مزوّد، تتم تجربة المرشح التالي تلقائيًا. إذا فشل الجميع، يتضمن الخطأ تفاصيل من كل محاولة.

عيّن `agents.defaults.mediaGenerationAutoProviderFallback: false` لاستخدام إدخالات `model` و`primary` و`fallbacks` الصريحة فقط.

## ملاحظات المزوّدين

ComfyUI

مدفوع بسير العمل ويعتمد على الرسم البياني المكوّن إضافة إلى ربط العُقد لحقول المطالبة/الإخراج. يندمج Plugin `comfy` المضمّن مع أداة `music_generate` المشتركة عبر سجل مزوّدي توليد الموسيقى.

Google (Lyria 3)

يستخدم توليد Lyria 3 الدفعي. يدعم التدفق المضمّن الحالي المطالبة، ونص الكلمات الاختياري، والصور المرجعية الاختيارية.

MiniMax

يستخدم نقطة نهاية `music_generation` الدُفعية. يدعم المطالبة والكلمات الاختيارية ووضع الآلات وتوجيه المدة وإخراج mp3 عبر مصادقة مفتاح API `minimax` أو OAuth `minimax-portal`.

## اختيار المسار الصحيح

  * **مدعوم بمزوّد مشترك** عندما تريد اختيار النموذج، وتجاوز فشل المزوّد، وتدفق المهمة/الحالة غير المتزامن المضمّن.
  * **مسار Plugin (ComfyUI)** عندما تحتاج إلى رسم بياني مخصص لسير العمل أو مزوّد ليس جزءًا من إمكانية الموسيقى المضمّنة المشتركة.


إذا كنت تصحح سلوكًا خاصًا بـ ComfyUI، فراجع [ComfyUI](</ar/providers/comfy>). إذا كنت تصحح سلوكًا مشتركًا للمزوّد، فابدأ بـ [Google (Gemini)](</ar/providers/google>) أو [MiniMax](</ar/providers/minimax>).

## أوضاع إمكانات المزوّد

يدعم عقد توليد الموسيقى المشترك تصريحات وضع صريحة:

  * `generate` للتوليد من مطالبة فقط.
  * `edit` عندما يتضمن الطلب صورة مرجعية واحدة أو أكثر.


ينبغي لتطبيقات المزوّد الجديدة تفضيل كتل الأوضاع الصريحة:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

الحقول المسطحة القديمة مثل `maxInputImages` و`supportsLyrics` و `supportsFormat` **ليست** كافية للإعلان عن دعم التحرير. ينبغي للمزوّدين التصريح بـ `generate` و`edit` صراحة حتى تستطيع الاختبارات الحية واختبارات العقد وأداة `music_generate` المشتركة التحقق من دعم الوضع بشكل حتمي.

## الاختبارات الحية

تغطية حية اختيارية للمزوّدين المضمّنين المشتركين:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

غلاف المستودع:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

يحمّل هذا الملف الحي متغيرات بيئة المزوّد الناقصة من `~/.profile`، ويفضّل مفاتيح API الحية/من البيئة على ملفات تعريف المصادقة المخزنة افتراضيًا، ويشغّل تغطية كل من `generate` و`edit` المعلنة عندما يفعّل المزوّد وضع التحرير. التغطية حاليًا:

  * `google`: `generate` بالإضافة إلى `edit`
  * `minimax`: `generate` فقط
  * `comfy`: تغطية حية منفصلة لـ Comfy، وليست ضمن المسح المشترك للمزوّدين


فعّل اختياريًا التغطية الحية لمسار الموسيقى المضمّن في ComfyUI:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

يغطي ملف Comfy الحي أيضًا سير عمل الصور والفيديو في comfy عندما تكون تلك الأقسام مهيأة.

## ذات صلة

  * [مهام الخلفية](</ar/automation/tasks>) — تتبّع المهام لتشغيلات `music_generate` المنفصلة
  * [ComfyUI](</ar/providers/comfy>)
  * [مرجع التهيئة](</ar/gateway/config-agents#agent-defaults>) — تهيئة `musicGenerationModel`
  * [Google (Gemini)](</ar/providers/google>)
  * [MiniMax](</ar/providers/minimax>)
  * [النماذج](</ar/concepts/models>) — تهيئة النماذج والتبديل عند الفشل
  * [نظرة عامة على الأدوات](</ar/tools>)


Was this useful?YesNo