---
title: مدرج
source_url: https://docs.openclaw.ai/ar/providers/runway
scraped_at: 2026-05-25
---

يأتي OpenClaw مع مزوّد `runway` مضمّن لإنشاء الفيديو المستضاف. يكون Plugin ممكّنًا افتراضيًا ويسجّل مزوّد `runway` مقابل عقد `videoGenerationProviders`.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `runway`  
Plugin | مضمّن، `enabledByDefault: true`  
متغيرات بيئة المصادقة | `RUNWAYML_API_SECRET` (الأساسي) أو `RUNWAY_API_KEY`  
علم الإعداد الأولي | `--auth-choice runway-api-key`  
علم CLI المباشر | `--runway-api-key <key>`  
API | إنشاء الفيديو القائم على مهام Runway (استطلاع `GET /v1/tasks/{id}`)  
النموذج الافتراضي | `runway/gen4.5`  
  
## البدء

* ### اضبط مفتاح API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### عيّن Runway كمزوّد الفيديو الافتراضي

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### أنشئ فيديو

اطلب من الوكيل إنشاء فيديو. سيُستخدم Runway تلقائيًا.

## الأوضاع والنماذج المدعومة

يوفّر المزوّد سبعة نماذج من Runway موزّعة على ثلاثة أوضاع. يمكن لمعرّف النموذج نفسه أن يخدم أكثر من وضع واحد (على سبيل المثال يعمل `gen4.5` لكل من تحويل النص إلى فيديو وتحويل الصورة إلى فيديو).

الوضع | النماذج | إدخال مرجعي  
---|---|---  
تحويل النص إلى فيديو | `gen4.5` (الافتراضي)، `veo3.1`، `veo3.1_fast`، `veo3` | لا يوجد  
تحويل الصورة إلى فيديو | `gen4.5`، `gen4_turbo`، `gen3a_turbo`، `veo3.1`، `veo3.1_fast`، `veo3` | صورة محلية أو بعيدة واحدة  
تحويل الفيديو إلى فيديو | `gen4_aleph` | فيديو محلي أو بعيد واحد  
  
تُدعم مراجع الصور والفيديو المحلية عبر عناوين URI للبيانات.

نسب العرض إلى الارتفاع | القيم المسموح بها  
---|---  
تحويل النص إلى فيديو | `16:9`، `9:16`  
تعديلات الصور والفيديو | `1:1`، `16:9`، `9:16`، `3:4`، `4:3`، `21:9`  
  
## الإعدادات

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## الإعدادات المتقدمة

الأسماء البديلة لمتغيرات البيئة

يتعرف OpenClaw على كل من `RUNWAYML_API_SECRET` (الأساسي) و`RUNWAY_API_KEY`. سيصادق أي من المتغيرين مزوّد Runway.

استطلاع المهام

يستخدم Runway واجهة API قائمة على المهام. بعد إرسال طلب إنشاء، يستطلع OpenClaw `GET /v1/tasks/{id}` إلى أن يصبح الفيديو جاهزًا. لا يلزم أي إعداد إضافي لسلوك الاستطلاع.

## ذو صلة

[**إنشاء الفيديو** معلمات الأداة المشتركة، واختيار المزوّد، والسلوك غير المتزامن. ](</ar/tools/video-generation>) [**مرجع الإعدادات** إعدادات الوكيل الافتراضية، بما في ذلك نموذج إنشاء الفيديو. ](</ar/gateway/config-agents#agent-defaults>)

Was this useful?YesNo