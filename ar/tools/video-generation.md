---
title: توليد الفيديو
source_url: https://docs.openclaw.ai/ar/tools/video-generation
scraped_at: 2026-05-25
---

تستطيع وكلاء OpenClaw إنشاء مقاطع فيديو من مطالبات نصية أو صور مرجعية أو مقاطع فيديو موجودة. تُدعَم ست عشرة واجهة خلفية لمزوّدين، ولكل منها خيارات نماذج وأنماط إدخال ومجموعات ميزات مختلفة. يختار الوكيل المزوّد المناسب تلقائيًا بناءً على إعداداتك ومفاتيح API المتاحة.

يتعامل OpenClaw مع إنشاء الفيديو على أنه ثلاثة أوضاع تشغيل:

  * `generate` \- طلبات تحويل النص إلى فيديو من دون وسائط مرجعية.
  * `imageToVideo` \- يتضمن الطلب صورة مرجعية واحدة أو أكثر.
  * `videoToVideo` \- يتضمن الطلب فيديو مرجعيًا واحدًا أو أكثر.


يمكن للمزوّدين دعم أي مجموعة فرعية من هذه الأوضاع. تتحقق الأداة من الوضع النشط قبل الإرسال وتعرض الأوضاع المدعومة في `action=list`.

## البدء السريع

* ### تكوين المصادقة

اضبط مفتاح API لأي مزوّد مدعوم:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### اختيار نموذج افتراضي (اختياري)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### اطلب من الوكيل

> أنشئ فيديو سينمائيًا مدته 5 ثوانٍ لكركند ودود يتزلج على الأمواج عند غروب الشمس.

يستدعي الوكيل `video_generate` تلقائيًا. لا حاجة إلى إدراج الأداة في قائمة السماح.

## كيفية عمل الإنشاء غير المتزامن

إنشاء الفيديو غير متزامن. عندما يستدعي الوكيل `video_generate` في جلسة:

  1. يرسل OpenClaw الطلب إلى المزوّد ويعيد معرّف مهمة فورًا.
  2. يعالج المزوّد المهمة في الخلفية (عادةً من 30 ثانية إلى عدة دقائق حسب المزوّد والدقة؛ وقد تعمل المزوّدات البطيئة المدعومة بطابور حتى المهلة المكوّنة).
  3. عندما يصبح الفيديو جاهزًا، يوقظ OpenClaw الجلسة نفسها بحدث إكمال داخلي.
  4. يخبر الوكيل المستخدم ويرفق الفيديو النهائي. في محادثات المجموعات/القنوات التي تستخدم تسليمًا مرئيًا مقتصرًا على أداة الرسائل، يمرر الوكيل النتيجة عبر أداة الرسائل بدل أن ينشرها OpenClaw مباشرة.


أثناء تنفيذ مهمة، تعيد استدعاءات `video_generate` المكررة في الجلسة نفسها حالة المهمة الحالية بدل بدء إنشاء آخر. استخدم `openclaw tasks list` أو `openclaw tasks show <taskId>` للتحقق من التقدم من CLI.

خارج عمليات تشغيل الوكيل المدعومة بجلسة (مثل الاستدعاءات المباشرة للأداة)، تعود الأداة إلى الإنشاء المضمن وتعيد مسار الوسائط النهائي في الدور نفسه.

تُحفَظ ملفات الفيديو المنشأة ضمن تخزين الوسائط المدار من OpenClaw عندما يعيد المزوّد بايتات. يتبع الحد الافتراضي لحفظ الفيديو المنشأ حد وسائط الفيديو، ويرفعه `agents.defaults.mediaMaxMb` لعمليات العرض الأكبر. عندما يعيد المزوّد أيضًا عنوان URL مستضافًا للمخرجات، يستطيع OpenClaw تسليم ذلك العنوان بدل فشل المهمة إذا رفض التخزين المحلي ملفًا يتجاوز الحجم المسموح.

### دورة حياة المهمة

الحالة | المعنى  
---|---  
`queued` | أُنشئت المهمة، وتنتظر قبول المزوّد لها.  
`running` | يعالجها المزوّد (عادةً من 30 ثانية إلى عدة دقائق حسب المزوّد والدقة).  
`succeeded` | الفيديو جاهز؛ يستيقظ الوكيل وينشره في المحادثة.  
`failed` | خطأ من المزوّد أو انتهاء المهلة؛ يستيقظ الوكيل مع تفاصيل الخطأ.  
  
تحقق من الحالة من CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

إذا كانت مهمة فيديو بالفعل في حالة `queued` أو `running` للجلسة الحالية، فإن `video_generate` يعيد حالة المهمة الموجودة بدل بدء مهمة جديدة. استخدم `action: "status"` للتحقق صراحةً من دون تشغيل إنشاء جديد.

## المزوّدون المدعومون

المزوّد | النموذج الافتراضي | النص | مرجع الصورة | مرجع الفيديو | المصادقة  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | نعم (عنوان URL بعيد) | نعم (عنوان URL بعيد) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | ما يصل إلى صورتين (نماذج I2V فقط؛ الإطار الأول + الأخير) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | ما يصل إلى صورتين (الإطار الأول + الأخير عبر الدور) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | ما يصل إلى 9 صور مرجعية | ما يصل إلى 3 مقاطع فيديو | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | صورة واحدة | - | `COMFY_API_KEY` أو `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | صورة واحدة؛ ما يصل إلى 9 مع تحويل Seedance من مرجع إلى فيديو | ما يصل إلى 3 مقاطع فيديو مع تحويل Seedance من مرجع إلى فيديو | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | صورة واحدة | فيديو واحد | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | صورة واحدة | - | `MINIMAX_API_KEY` أو MiniMax OAuth  
OpenAI | `sora-2` | ✓ | صورة واحدة | فيديو واحد | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | ما يصل إلى 4 صور (الإطار الأول/الأخير أو مراجع) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | نعم (عنوان URL بعيد) | نعم (عنوان URL بعيد) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | صورة واحدة | فيديو واحد | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | صورة واحدة | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | صورة واحدة (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | صورة إطار أول واحدة أو ما يصل إلى 7 `reference_image`s | فيديو واحد | `XAI_API_KEY`  
  
تقبل بعض المزوّدات متغيرات بيئة إضافية أو بديلة لمفتاح API. راجع صفحات المزوّدين الفردية للتفاصيل.

شغّل `video_generate action=list` لفحص المزوّدين والنماذج وأوضاع التشغيل المتاحة وقت التشغيل.

### مصفوفة القدرات

عقد الوضع الصريح الذي تستخدمه `video_generate` واختبارات العقد والمسح الحي المشترك:

المزوّد | `generate` | `imageToVideo` | `videoToVideo` | المسارات الحية المشتركة اليوم  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يتم تخطي `videoToVideo` لأن هذا المزوّد يحتاج إلى عناوين URL بعيدة لفيديوهات `http(s)`  
BytePlus | ✓ | ✓ | - | `generate`، `imageToVideo`  
ComfyUI | ✓ | ✓ | - | ليس ضمن المسح المشترك؛ توجد التغطية الخاصة بسير العمل مع اختبارات Comfy  
DeepInfra | ✓ | - | - | `generate`؛ مخططات فيديو DeepInfra الأصلية هي تحويل نص إلى فيديو في العقد المضمن  
fal | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ `videoToVideo` فقط عند استخدام تحويل Seedance من مرجع إلى فيديو  
Google | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يتم تخطي `videoToVideo` المشترك لأن مسح Gemini/Veo الحالي المدعوم بالمخزن المؤقت لا يقبل ذلك الإدخال  
MiniMax | ✓ | ✓ | - | `generate`، `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يتم تخطي `videoToVideo` المشترك لأن مسار المؤسسة/الإدخال هذا يحتاج حاليًا إلى وصول inpaint/remix من جهة المزوّد  
OpenRouter | ✓ | ✓ | - | `generate`، `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يتم تخطي `videoToVideo` لأن هذا المزوّد يحتاج إلى عناوين URL بعيدة لفيديوهات `http(s)`  
Runway | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يعمل `videoToVideo` فقط عندما يكون النموذج المحدد هو `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`، `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`؛ يتم تخطي `imageToVideo` المشترك لأن `veo3` المضمن نصي فقط و`kling` المضمن يتطلب عنوان URL بعيدًا لصورة  
xAI | ✓ | ✓ | ✓ | `generate`، `imageToVideo`؛ يتم تخطي `videoToVideo` لأن هذا المزوّد يحتاج حاليًا إلى عنوان URL بعيد لملف MP4  
  
## معلمات الأداة

### مطلوبة

وصف نصي للفيديو المراد إنشاؤه. مطلوب لـ `action: "generate"`.

### إدخالات المحتوى

تلميحات أدوار اختيارية لكل موضع، بالتوازي مع قائمة الصور المجمّعة. القيم القياسية: `first_frame`، `last_frame`، `reference_image`.

تلميحات أدوار اختيارية لكل موضع، بالتوازي مع قائمة الفيديوهات المجمّعة. القيمة القياسية: `reference_video`.

صوت مرجعي واحد (مسار أو URL). يُستخدم لموسيقى الخلفية أو كمرجع صوتي عندما يدعم المزوّد إدخالات الصوت.

تلميحات أدوار اختيارية لكل موضع، بالتوازي مع قائمة الصوت المجمّعة. القيمة القياسية: `reference_audio`.

### عناصر التحكم في النمط

تلميح نسبة العرض إلى الارتفاع مثل `1:1` أو `16:9` أو `9:16` أو `adaptive` أو قيمة خاصة بالمزوّد. يطبّع OpenClaw القيم غير المدعومة أو يتجاهلها حسب المزوّد.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI تلميح الدقة مثل `480P` أو `720P` أو `768P` أو `1080P` أو `4K` أو قيمة خاصة بالمزوّد. يطبّع OpenClaw القيم غير المدعومة أو يتجاهلها حسب المزوّد. OPENCLAW_DOCS_MARKER:paramClose:

المدة المستهدفة بالثواني (تُقرَّب إلى أقرب قيمة يدعمها المزوّد).

تفعيل الصوت المولّد في المخرجات عند دعمه. يختلف عن `audioRef*` (الإدخالات).

`adaptive` قيمة دالة خاصة بالمزوّد: تُمرَّر كما هي إلى المزوّدات التي تعلن `adaptive` ضمن قدراتها (مثل BytePlus Seedance التي تستخدمها لاكتشاف النسبة تلقائيا من أبعاد صورة الإدخال). المزوّدات التي لا تعلنها تعرض القيمة عبر `details.ignoredOverrides` في نتيجة الأداة حتى يكون الإسقاط مرئيا.

### متقدم

يعيد `"status"` مهمة الجلسة الحالية؛ ويفحص `"list"` المزوّدات.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci تجاوز المزوّد/النموذج (مثل `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg مهلة اختيارية لعملية المزوّد بالمللي ثانية. عند حذفها، يستخدم OpenClaw `agents.defaults.videoGenerationModel.timeoutMs` إذا كان مكوّنا. OPENCLAW_DOCS_MARKER:paramClose:

خيارات خاصة بالمزوّد ككائن JSON (مثل `{"seed": 42, "draft": true}`). المزوّدات التي تعلن مخططا ذا أنواع تتحقق من المفاتيح والأنواع؛ وتتسبب المفاتيح غير المعروفة أو حالات عدم التطابق في تخطي المرشح أثناء الرجوع الاحتياطي. المزوّدات التي لا تعلن مخططا تتلقى الخيارات كما هي. شغّل `video_generate action=list` لمعرفة ما يقبله كل مزوّد.

تحدد إدخالات المراجع وضع التشغيل:

  * لا توجد وسائط مرجعية → `generate`
  * أي مرجع صورة → `imageToVideo`
  * أي مرجع فيديو → `videoToVideo`
  * إدخالات الصوت المرجعية **لا** تغيّر الوضع المحسوم؛ فهي تُطبّق فوق أي وضع تختاره مراجع الصور/الفيديو، ولا تعمل إلا مع المزوّدات التي تعلن `maxInputAudios`.


ليست مراجع الصور والفيديو المختلطة سطح قدرات مشتركا مستقرا. فضّل نوع مرجع واحدا لكل طلب.

#### الرجوع الاحتياطي والخيارات ذات الأنواع

تُطبَّق بعض فحوصات القدرات في طبقة الرجوع الاحتياطي بدلا من حد الأداة، لذلك يمكن لطلب يتجاوز حدود المزوّد الأساسي أن يعمل مع مزوّد احتياطي قادر:

  * يُتخطى المرشح النشط الذي لا يعلن `maxInputAudios` (أو يعلن `0`) عندما يحتوي الطلب على مراجع صوتية؛ ثم يُجرَّب المرشح التالي.
  * إذا كان `maxDurationSeconds` للمرشح النشط أدنى من `durationSeconds` المطلوبة ولا توجد قائمة `supportedDurationSeconds` معلنة → يُتخطى.
  * إذا احتوى الطلب على `providerOptions` وكان المرشح النشط يعلن صراحة مخطط `providerOptions` ذا أنواع → يُتخطى إذا كانت المفاتيح المقدمة غير موجودة في المخطط أو كانت أنواع القيم غير مطابقة. المزوّدات التي لا تملك مخططا معلنا تتلقى الخيارات كما هي (تمرير متوافق مع الإصدارات السابقة). يمكن للمزوّد تعطيل جميع خيارات المزوّد عبر إعلان مخطط فارغ (`capabilities.providerOptions: {}`)، مما يسبب التخطي نفسه كعدم تطابق النوع.


يُسجَّل أول سبب تخطٍّ في الطلب عند `warn` حتى يرى المشغّلون متى تم تجاوز مزوّدهم الأساسي؛ وتسجّل أسباب التخطي اللاحقة عند `debug` لإبقاء سلاسل الرجوع الاحتياطي الطويلة هادئة. إذا تم تخطي كل المرشحين، يتضمن الخطأ المجمّع سبب التخطي لكل منهم.

## الإجراءات

الإجراء | ما يفعله  
---|---  
`generate` | الافتراضي. ينشئ فيديو من المطالبة المعطاة وإدخالات المراجع الاختيارية.  
`status` | يتحقق من حالة مهمة الفيديو قيد التنفيذ للجلسة الحالية دون بدء توليد آخر.  
`list` | يعرض المزوّدات والنماذج المتاحة وقدراتها.  
  
## اختيار النموذج

يحل OpenClaw النموذج بهذا الترتيب:

  1. **معلمة الأداة`model`** \- إذا حدد الوكيل واحدة في الاستدعاء.
  2. **`videoGenerationModel.primary`** من الإعدادات.
  3. **`videoGenerationModel.fallbacks`** بالترتيب.
  4. **الاكتشاف التلقائي** \- المزوّدات التي لديها مصادقة صالحة، بدءا من المزوّد الافتراضي الحالي، ثم بقية المزوّدات بالترتيب الأبجدي.


إذا فشل مزوّد، يُجرَّب المرشح التالي تلقائيا. إذا فشل جميع المرشحين، يتضمن الخطأ تفاصيل من كل محاولة.

اضبط `agents.defaults.mediaGenerationAutoProviderFallback: false` لاستخدام إدخالات `model` و`primary` و`fallbacks` الصريحة فقط.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## ملاحظات المزوّدين

Alibaba

يستخدم نقطة النهاية غير المتزامنة في DashScope / Model Studio. يجب أن تكون الصور والفيديوهات المرجعية عناوين URL بعيدة بصيغة `http(s)`.

BytePlus (1.0)

معرّف المزوّد: `byteplus`.

النماذج: `seedance-1-0-pro-250528` (الافتراضي)، `seedance-1-0-pro-t2v-250528`، `seedance-1-0-pro-fast-251015`، `seedance-1-0-lite-t2v-250428`، `seedance-1-0-lite-i2v-250428`.

نماذج T2V (`*-t2v-*`) لا تقبل إدخالات الصور؛ تدعم نماذج I2V والنماذج العامة `*-pro-*` صورة مرجعية واحدة (الإطار الأول). مرّر الصورة موضعيا أو اضبط `role: "first_frame"`. تُبدَّل معرّفات نماذج T2V تلقائيا إلى متغير I2V المقابل عند تقديم صورة.

مفاتيح `providerOptions` المدعومة: `seed` (رقم)، `draft` (منطقي - يفرض 480p)، `camera_fixed` (منطقي).

BytePlus Seedance 1.5

يتطلب Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). معرّف المزوّد: `byteplus-seedance15`. النموذج: `seedance-1-5-pro-251215`.

يستخدم API الموحّد `content[]`. يدعم ما يصل إلى صورتَي إدخال (`first_frame` \+ `last_frame`). يجب أن تكون جميع الإدخالات عناوين URL بعيدة بصيغة `https://`. اضبط `role: "first_frame"` / `"last_frame"` على كل صورة، أو مرّر الصور موضعيا.

يكتشف `aspectRatio: "adaptive"` النسبة تلقائيا من صورة الإدخال. يطابق `audio: true` إلى `generate_audio`. تُمرَّر `providerOptions.seed` (رقم).

BytePlus Seedance 2.0

يتطلب Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). معرّف المزوّد: `byteplus-seedance2`. النماذج: `dreamina-seedance-2-0-260128`، `dreamina-seedance-2-0-fast-260128`.

يستخدم API الموحّد `content[]`. يدعم حتى 9 صور مرجعية، و3 فيديوهات مرجعية، و3 ملفات صوت مرجعية. يجب أن تكون جميع الإدخالات عناوين URL بعيدة بصيغة `https://`. اضبط `role` على كل أصل - القيم المدعومة: `"first_frame"`، `"last_frame"`، `"reference_image"`، `"reference_video"`، `"reference_audio"`.

يكتشف `aspectRatio: "adaptive"` النسبة تلقائيا من صورة الإدخال. يطابق `audio: true` إلى `generate_audio`. تُمرَّر `providerOptions.seed` (رقم).

ComfyUI

تنفيذ محلي أو سحابي موجّه بسير العمل. يدعم تحويل النص إلى فيديو وتحويل الصورة إلى فيديو عبر الرسم البياني المُكوَّن.

fal

يستخدم تدفقًا مدعومًا بطابور للمهام طويلة التشغيل. ينتظر OpenClaw حتى 20 دقيقة افتراضيًا قبل اعتبار مهمة طابور fal قيد التقدّم منتهية المهلة. تقبل معظم نماذج فيديو fal مرجع صورة واحدًا. تقبل نماذج Seedance 2.0 لتحويل المرجع إلى فيديو حتى 9 صور، و3 فيديوهات، و3 مراجع صوتية، وبحد أقصى 12 ملف مرجعي إجمالًا.

Google (Gemini / Veo)

يدعم مرجع صورة واحدًا أو مرجع فيديو واحدًا. تُتجاهل طلبات الصوت المُولَّد مع تحذير في مسار Gemini API لأن تلك الواجهة ترفض معامل `generateAudio` لإنشاء فيديو Veo الحالي.

MiniMax

مرجع صورة واحد فقط. يقبل MiniMax دقّتي `768P` و`1080P`؛ وتُطبَّع الطلبات مثل `720P` إلى أقرب قيمة مدعومة قبل الإرسال.

OpenAI

يُمرَّر تجاوز `size` فقط. تُتجاهل تجاوزات النمط الأخرى (`aspectRatio`، `resolution`، `audio`، `watermark`) مع تحذير.

OpenRouter

يستخدم واجهة `/videos` غير المتزامنة من OpenRouter. يرسل OpenClaw المهمة، ويستطلع `polling_url`، وينزّل إما `unsigned_urls` أو نقطة نهاية محتوى المهمة الموثقة. يعلن الافتراضي المضمّن `google/veo-3.1-fast` عن مدد 4/6/8 ثوانٍ، ودقّات `720P`/`1080P`، ونِسب عرض إلى ارتفاع `16:9`/`9:16`.

Qwen

نفس خلفية DashScope مثل Alibaba. يجب أن تكون مُدخلات المراجع عناوين URL بعيدة من نوع `http(s)`؛ وتُرفض الملفات المحلية مسبقًا.

Runway

يدعم الملفات المحلية عبر عناوين URI للبيانات. يتطلب تحويل الفيديو إلى فيديو `runway/gen4_aleph`. تعرض عمليات النص فقط نسبتي العرض إلى الارتفاع `16:9` و`9:16`.

Together

مرجع صورة واحد فقط.

Vydra

يستخدم `https://www.vydra.ai/api/v1` مباشرة لتجنّب عمليات إعادة التوجيه التي تُسقط المصادقة. يُضمَّن `veo3` كتحويل نص إلى فيديو فقط؛ ويتطلب `kling` عنوان URL بعيدًا لصورة.

xAI

يدعم تحويل النص إلى فيديو، وتحويل صورة الإطار الأول الفردية إلى فيديو، وما يصل إلى 7 مُدخلات `reference_image` عبر `reference_images` في xAI، وتدفقات تحرير/تمديد الفيديو البعيد.

## أوضاع قدرات المزوّد

يدعم عقد إنشاء الفيديو المشترك قدرات خاصة بكل وضع بدلًا من حدود إجمالية مسطحة فقط. يجب أن تفضّل تطبيقات المزوّد الجديدة كتل الأوضاع الصريحة:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

الحقول الإجمالية المسطحة مثل `maxInputImages` و`maxInputVideos` **ليست** كافية للإعلان عن دعم وضع التحويل. يجب أن يعلن المزوّدون عن `generate` و`imageToVideo` و`videoToVideo` صراحةً كي تتمكن الاختبارات الحية، واختبارات العقد، وأداة `video_generate` المشتركة من التحقق من دعم الوضع بصورة حتمية.

عندما يتمتع نموذج واحد لدى مزوّد بدعم أوسع لمُدخلات المراجع من البقية، استخدم `maxInputImagesByModel` أو `maxInputVideosByModel` أو `maxInputAudiosByModel` بدلًا من رفع الحد على مستوى الوضع.

## الاختبارات الحية

تغطية حية اختيارية للمزوّدين المشتركين المضمّنين:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

مغلّف المستودع:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

يحمّل هذا الملف الحي متغيرات بيئة المزوّد الناقصة من `~/.profile`، ويفضّل مفاتيح API الحية/من البيئة على ملفات تعريف المصادقة المخزنة افتراضيًا، ويشغّل اختبار دخان آمنًا للإصدار افتراضيًا:

  * `generate` لكل مزوّد غير FAL في المسح.
  * مطالبة جراد بحر مدتها ثانية واحدة.
  * حد العمليات لكل مزوّد من `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (`180000` افتراضيًا).


FAL اختياري لأن زمن انتظار الطابور من جهة المزوّد قد يهيمن على وقت الإصدار:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

عيّن `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` لتشغيل أوضاع التحويل المعلنة أيضًا التي يستطيع المسح المشترك ممارستها بأمان باستخدام وسائط محلية:

  * `imageToVideo` عندما تكون `capabilities.imageToVideo.enabled`.
  * `videoToVideo` عندما تكون `capabilities.videoToVideo.enabled` ويقبل المزوّد/النموذج إدخال فيديو محلي مدعومًا بالمخزن المؤقت في المسح المشترك.


اليوم يغطي مسار `videoToVideo` الحي المشترك `runway` فقط عندما تحدد `runway/gen4_aleph`.

## التكوين

عيّن نموذج إنشاء الفيديو الافتراضي في تكوين OpenClaw لديك:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

أو عبر CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## ذات صلة

  * [Alibaba Model Studio](</ar/providers/alibaba>)
  * [المهام الخلفية](</ar/automation/tasks>) \- تتبع المهام لإنشاء الفيديو غير المتزامن
  * [BytePlus](</ar/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</ar/providers/comfy>)
  * [مرجع التكوين](</ar/gateway/config-agents#agent-defaults>)
  * [fal](</ar/providers/fal>)
  * [Google (Gemini)](</ar/providers/google>)
  * [MiniMax](</ar/providers/minimax>)
  * [النماذج](</ar/concepts/models>)
  * [OpenAI](</ar/providers/openai>)
  * [Qwen](</ar/providers/qwen>)
  * [Runway](</ar/providers/runway>)
  * [Together AI](</ar/providers/together>)
  * [نظرة عامة على الأدوات](</ar/tools>)
  * [Vydra](</ar/providers/vydra>)
  * [xAI](</ar/providers/xai>)


Was this useful?YesNo