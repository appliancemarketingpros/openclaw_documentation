---
title: PixVerse
source_url: https://docs.openclaw.ai/ar/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

يوفّر OpenClaw `pixverse` بصفته Plugin خارجيًا رسميًا لتوليد فيديو PixVerse المستضاف. يسجّل Plugin مزوّد `pixverse` مقابل عقد `videoGenerationProviders`.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `pixverse`  
حزمة Plugin | `@openclaw/pixverse-provider`  
متغير بيئة المصادقة | `PIXVERSE_API_KEY`  
علم التهيئة | `--auth-choice pixverse-api-key`  
علم CLI المباشر | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (إرسال `video_id` مع استطلاع النتائج)  
النموذج الافتراضي | `pixverse/v6`  
منطقة API الافتراضية | دولية  
  
## البدء

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

يسأل المعالج هل تريد استخدام نقطة النهاية الدولية (`https://app-api.pixverse.ai/openapi/v2`) أم نقطة نهاية CN (`https://app-api.pixverseai.cn/openapi/v2`) قبل كتابة `region` و `baseUrl` في إعدادات المزوّد.

* ### Set PixVerse as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generate a video

اطلب من الوكيل توليد فيديو. سيُستخدم PixVerse تلقائيًا.

## الأوضاع والنماذج المدعومة

يعرض المزوّد نماذج توليد PixVerse عبر أداة الفيديو المشتركة في OpenClaw.

الوضع | النماذج | إدخال مرجعي  
---|---|---  
تحويل النص إلى فيديو | `v6` (افتراضي)، `c1` | لا شيء  
تحويل الصورة إلى فيديو | `v6` (افتراضي)، `c1` | صورة محلية أو بعيدة واحدة  
  
تُرفع مراجع الصور المحلية إلى PixVerse قبل طلب تحويل الصورة إلى فيديو. تُمرّر عناوين URL للصور البعيدة عبر نقطة نهاية رفع الصور في PixVerse باسم `image_url`.

الخيار | القيم المدعومة  
---|---  
المدة | 1-15 ثانية  
الدقة | `360P`, `540P`, `720P`, `1080P`  
نسبة العرض إلى الارتفاع | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` لتحويل النص إلى فيديو  
الصوت المولّد | `audio: true`  
  
## خيارات المزوّد

يقبل مزوّد الفيديو هذه المفاتيح الاختيارية الخاصة بالمزوّد:

الخيار | النوع | التأثير  
---|---|---  
`seed` | number | بذرة حتمية عند دعمها  
`negativePrompt` / `negative_prompt` | string | موجّه سلبي  
`quality` | string | جودة PixVerse مثل `720p`  
`motionMode` / `motion_mode` | string | وضع حركة تحويل الصورة إلى فيديو  
`cameraMovement` / `camera_movement` | string | إعداد مسبق لحركة كاميرا PixVerse  
`templateId` / `template_id` | number | معرّف قالب PixVerse مفعّل  
  
## الإعدادات

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## الإعدادات المتقدمة

API region

يستخدم OpenClaw افتراضيًا PixVerse API الدولي. عيّن `models.providers.pixverse.region` يدويًا عندما ينتمي مفتاحك إلى منطقة منصة PixVerse محددة، أو استخدم `openclaw onboard --auth-choice pixverse-api-key` لاختيار منطقة في معالج الإعداد:

قيمة المنطقة | عنوان URL الأساسي لـ PixVerse API  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Custom base URL

عيّن `models.providers.pixverse.baseUrl` فقط عند التوجيه عبر وكيل موثوق ومتوافق. تكون لـ `baseUrl` أسبقية على `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Task polling

يعيد PixVerse قيمة `video_id` من طلب التوليد. يستطلع OpenClaw `/openapi/v2/video/result/{video_id}` حتى تنجح المهمة أو تفشل أو تنتهي مهلتها.

## ذات صلة

[**Video generation** معلمات الأداة المشتركة، واختيار المزوّد، والسلوك غير المتزامن. ](</ar/tools/video-generation>) [**Configuration reference** إعدادات الوكيل الافتراضية، بما في ذلك نموذج توليد الفيديو. ](</ar/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue