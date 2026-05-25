---
title: Fal
source_url: https://docs.openclaw.ai/ar/providers/fal
scraped_at: 2026-05-25
---

OpenClaw يوفّر مزوّد `fal` مضمّنًا لإنشاء الصور والفيديوهات المستضاف.

الخاصية | القيمة  
---|---  
المزوّد | `fal`  
المصادقة | `FAL_KEY` (الأساسي؛ يعمل `FAL_API_KEY` أيضًا كبديل احتياطي)  
API | نقاط نهاية نماذج fal  
  
## بدء الاستخدام

* ### تعيين مفتاح API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### تعيين نموذج صور افتراضي

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## إنشاء الصور

يعتمد مزوّد إنشاء الصور `fal` المضمّن افتراضيًا على `fal/fal-ai/flux/dev`.

الإمكانية | القيمة  
---|---  
الحد الأقصى للصور | 4 لكل طلب  
وضع التحرير | Flux: صورة مرجعية واحدة؛ GPT Image 2: 10؛ Nano Banana 2: 14  
تجاوزات الحجم | مدعومة  
نسبة العرض إلى الارتفاع | مدعومة للإنشاء وتحرير GPT Image 2/Nano Banana 2  
الدقة | مدعومة  
تنسيق الإخراج | `png` أو `jpeg`  
  
استخدم `outputFormat: "png"` عندما تريد إخراج PNG. لا يعلن fal عن عنصر تحكم صريح للخلفية الشفافة في OpenClaw، لذلك يتم الإبلاغ عن `background: "transparent"` كتجاوز متجاهل لنماذج fal.

لاستخدام fal كمزوّد صور افتراضي:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## إنشاء الفيديو

يعتمد مزوّد إنشاء الفيديو `fal` المضمّن افتراضيًا على `fal/fal-ai/minimax/video-01-live`.

الإمكانية | القيمة  
---|---  
الأوضاع | نص إلى فيديو، مرجع صورة واحدة، مرجع Seedance إلى فيديو  
وقت التشغيل | تدفق إرسال/حالة/نتيجة مدعوم بقائمة انتظار للمهام طويلة التشغيل  
  
نماذج الفيديو المتاحة

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

مثال إعداد Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

مثال إعداد مرجع إلى فيديو في Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

يقبل المرجع إلى فيديو ما يصل إلى 9 صور، و3 فيديوهات، و3 مراجع صوتية عبر معاملات `video_generate` المشتركة `images` و`videos` و`audioRefs`، وبحد أقصى 12 ملفًا مرجعيًا إجمالًا.

مثال إعداد HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## ذات صلة

[**إنشاء الصور** معاملات أداة الصور المشتركة واختيار المزوّد. ](</ar/tools/image-generation>) [**إنشاء الفيديو** معاملات أداة الفيديو المشتركة واختيار المزوّد. ](</ar/tools/video-generation>) [**مرجع الإعدادات** افتراضيات الوكيل، بما في ذلك اختيار نماذج الصور والفيديو. ](</ar/gateway/config-agents#agent-defaults>)

Was this useful?YesNo