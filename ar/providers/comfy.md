---
title: ComfyUI
source_url: https://docs.openclaw.ai/ar/providers/comfy
scraped_at: 2026-05-25
---

يشحن OpenClaw Plugin مضمّنًا باسم `comfy` لتشغيلات ComfyUI المعتمدة على سير العمل. يعتمد Plugin بالكامل على سير العمل، لذلك لا يحاول OpenClaw مواءمة عناصر تحكم عامة مثل `size` أو `aspectRatio` أو `resolution` أو `durationSeconds` أو عناصر تحكم على نمط TTS مع الرسم البياني لديك.

الخاصية | التفاصيل  
---|---  
الموفّر | `comfy`  
النماذج | `comfy/workflow`  
الواجهات المشتركة | `image_generate`, `video_generate`, `music_generate`  
المصادقة | لا شيء لـ ComfyUI المحلي؛ أو `COMFY_API_KEY` أو `COMFY_CLOUD_API_KEY` لـ Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` وComfy Cloud `/api/*`  
  
## ما الذي يدعمه

  * إنشاء الصور من ملف JSON لسير العمل
  * تحرير الصور باستخدام صورة مرجعية واحدة مرفوعة
  * إنشاء الفيديو من ملف JSON لسير العمل
  * إنشاء الفيديو باستخدام صورة مرجعية واحدة مرفوعة
  * إنشاء الموسيقى أو الصوت عبر الأداة المشتركة `music_generate`
  * تنزيل المخرجات من Node مُعدّ أو من كل Nodes المخرجات المطابقة


## البدء

اختر بين تشغيل ComfyUI على جهازك أو استخدام Comfy Cloud.

### Local

**الأفضل لـ:** تشغيل مثيل ComfyUI الخاص بك على جهازك أو على شبكة LAN.

* ### تشغيل ComfyUI محليًا

تأكد من أن مثيل ComfyUI المحلي قيد التشغيل (القيمة الافتراضية هي `http://127.0.0.1:8188`).

* ### تحضير JSON الخاص بسير العمل

صدّر أو أنشئ ملف JSON لسير عمل ComfyUI. دوّن معرّفات Node الخاصة بعقدة إدخال الموجّه وعقدة الإخراج التي تريد أن يقرأ OpenClaw منها.

* ### إعداد الموفّر

اضبط `mode: "local"` ووجّه إلى ملف سير العمل. إليك مثالًا بسيطًا للصور:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### تعيين النموذج الافتراضي

وجّه OpenClaw إلى النموذج `comfy/workflow` للإمكانات التي قمت بإعدادها:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### التحقق

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**الأفضل لـ:** تشغيل سير العمل على Comfy Cloud من دون إدارة موارد GPU محلية.

* ### الحصول على مفتاح API

سجّل في [comfy.org](<https://comfy.org>) وأنشئ مفتاح API من لوحة حسابك.

* ### تعيين مفتاح API

وفّر المفتاح بإحدى الطرق التالية:

bashCopy code
[code]
    # متغير بيئة (مفضل)export COMFY_API_KEY="your-key" # متغير بيئة بديلexport COMFY_CLOUD_API_KEY="your-key" # أو مباشرة داخل الإعداداتopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### تحضير JSON الخاص بسير العمل

صدّر أو أنشئ ملف JSON لسير عمل ComfyUI. دوّن معرّفات Node الخاصة بعقدة إدخال الموجّه وعقدة الإخراج.

* ### إعداد الموفّر

اضبط `mode: "cloud"` ووجّه إلى ملف سير العمل:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### تعيين النموذج الافتراضي

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### التحقق

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## الإعدادات

يدعم comfy إعدادات اتصال مشتركة على المستوى الأعلى بالإضافة إلى أقسام سير عمل خاصة بكل قدرة (`image` و`video` و`music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### المفاتيح المشتركة

المفتاح | النوع | الوصف  
---|---|---  
`mode` | `"local"` or `"cloud"` | وضع الاتصال.  
`baseUrl` | string | القيمة الافتراضية هي `http://127.0.0.1:8188` للوضع المحلي أو `https://cloud.comfy.org` لوضع cloud.  
`apiKey` | string | مفتاح مضمن اختياري، بديل عن متغيرات البيئة `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | السماح باستخدام `baseUrl` خاص/على شبكة LAN في وضع cloud.  
  
### المفاتيح الخاصة بكل قدرة

تنطبق هذه المفاتيح داخل أقسام `image` أو `video` أو `music`:

المفتاح | مطلوب | الافتراضي | الوصف  
---|---|---|---  
`workflow` or `workflowPath` | نعم | \-- | مسار ملف JSON لسير عمل ComfyUI.  
`promptNodeId` | نعم | \-- | معرّف Node الذي يستقبل موجّه النص.  
`promptInputName` | لا | `"text"` | اسم الإدخال على Node الموجّه.  
`outputNodeId` | لا | \-- | معرّف Node الذي تُقرأ منه المخرجات. إذا تم حذفه، تُستخدم كل Nodes المخرجات المطابقة.  
`pollIntervalMs` | لا | \-- | فاصل الاستطلاع بالميلي ثانية لاكتمال المهمة.  
`timeoutMs` | لا | \-- | المهلة بالميلي ثانية لتشغيل سير العمل.  
  
يدعم قسما `image` و`video` أيضًا ما يلي:

المفتاح | مطلوب | الافتراضي | الوصف  
---|---|---|---  
`inputImageNodeId` | نعم (عند تمرير صورة مرجعية) | \-- | معرّف Node الذي يستقبل الصورة المرجعية المرفوعة.  
`inputImageInputName` | لا | `"image"` | اسم الإدخال على Node الصورة.  
  
## تفاصيل سير العمل

Image workflows

اضبط نموذج الصور الافتراضي على `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**مثال على التحرير باستخدام صورة مرجعية:**

لتمكين تحرير الصور باستخدام صورة مرجعية مرفوعة، أضف `inputImageNodeId` إلى إعدادات الصورة لديك:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video workflows

اضبط نموذج الفيديو الافتراضي على `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

تدعم سير عمل الفيديو في Comfy تحويل النص إلى فيديو وتحويل الصورة إلى فيديو عبر الرسم البياني المُعد.

Music workflows

يسجّل Plugin المضمّن موفّرًا لإنشاء الموسيقى من أجل مخرجات الصوت أو الموسيقى المعرّفة عبر سير العمل، ويتم عرضه عبر الأداة المشتركة `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

استخدم قسم إعدادات `music` للتوجيه إلى JSON الخاص بسير عمل الصوت وعقدة الإخراج.

Backward compatibility

ما زالت إعدادات الصور القديمة على المستوى الأعلى (من دون قسم `image` المتداخل) تعمل:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

يتعامل OpenClaw مع هذا الشكل القديم باعتباره إعدادات سير عمل الصور. لا تحتاج إلى الترحيل فورًا، لكن يُنصح باستخدام الأقسام المتداخلة `image` / `video` / `music` في الإعدادات الجديدة.

Live tests

توجد تغطية live اختيارية لـ Plugin المضمّن:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

يتخطى اختبار live الحالات الفردية للصور أو الفيديو أو الموسيقى ما لم يكن قسم سير عمل Comfy المطابق مُعدًا.

## ذو صلة

[**إنشاء الصور** إعدادات أداة إنشاء الصور وطريقة استخدامها. ](</ar/tools/image-generation>) [**إنشاء الفيديو** إعدادات أداة إنشاء الفيديو وطريقة استخدامها. ](</ar/tools/video-generation>) [**إنشاء الموسيقى** إعداد أداة إنشاء الموسيقى والصوت. ](</ar/tools/music-generation>) [**دليل الموفّرين** نظرة عامة على جميع الموفّرين ومراجع النماذج. ](</ar/providers>) [**مرجع الإعدادات** مرجع الإعدادات الكامل بما في ذلك الإعدادات الافتراضية للوكيل. ](</ar/gateway/config-agents#agent-defaults>)

Was this useful?YesNo