---
title: Z.AI
source_url: https://docs.openclaw.ai/ar/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) هي منصة API لنماذج **GLM**. توفر REST APIs لـ GLM وتستخدم مفاتيح API للمصادقة. أنشئ مفتاح API الخاص بك في وحدة تحكم [Z.AI](<http://Z.AI>). يستخدم OpenClaw موفر `zai` مع مفتاح [Z.AI](<http://Z.AI>) API.

  * الموفر: `zai`
  * المصادقة: `ZAI_API_KEY`
  * API: إكمالات الدردشة في [Z.AI](<http://Z.AI>) (مصادقة Bearer)


## البدء

### Auto-detect endpoint

**الأفضل لـ:** معظم المستخدمين. يكتشف OpenClaw نقطة نهاية [Z.AI](<http://Z.AI>) المطابقة من المفتاح ويطبق عنوان URL الأساسي الصحيح تلقائيا.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Explicit regional endpoint

**الأفضل لـ:** المستخدمين الذين يريدون فرض خطة ترميز محددة أو سطح API عام.

* ### Pick the right onboarding choice

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## الكتالوج المضمن

يشحن OpenClaw كتالوج موفر `zai` المضمن في بيان Plugin، لذا يمكن أن يعرض السرد للقراءة فقط صفوف GLM المعروفة دون تحميل وقت تشغيل الموفر:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

يتضمن الكتالوج المدعوم بالبيان حاليا:

مرجع النموذج | ملاحظات  
---|---  
`zai/glm-5.1` | النموذج الافتراضي  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## الإعداد المتقدم

Forward-resolving unknown GLM-5 models

لا تزال معرفات `glm-5*` غير المعروفة تحل إلى الأمام على مسار الموفر المضمن عبر إنشاء بيانات وصفية مملوكة للموفر من قالب `glm-4.7` عندما يطابق المعرف شكل عائلة GLM-5 الحالي.

Tool-call streaming

يتم تمكين `tool_stream` افتراضيا لبث استدعاءات الأدوات في [Z.AI](<http://Z.AI>). لتعطيله:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking and preserved thinking

يتبع التفكير في [Z.AI](<http://Z.AI>) عناصر تحكم `/think` في OpenClaw. عند إيقاف التفكير، يرسل OpenClaw القيمة `thinking: { type: "disabled" }` لتجنب الاستجابات التي تستهلك ميزانية الإخراج في `reasoning_content` قبل النص المرئي.

التفكير المحفوظ اختياري لأن [Z.AI](<http://Z.AI>) يتطلب إعادة تشغيل `reasoning_content` التاريخي بالكامل، مما يزيد رموز المطالبة. فعله لكل نموذج:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

عند تمكينه وتشغيل التفكير، يرسل OpenClaw `thinking: { type: "enabled", clear_thinking: false }` ويعيد تشغيل `reasoning_content` السابق للنص الحواري نفسه المتوافق مع OpenAI.

لا يزال بإمكان المستخدمين المتقدمين تجاوز حمولة الموفر الدقيقة باستخدام `params.extra_body.thinking`.

Image understanding

يسجل Plugin [Z.AI](<http://Z.AI>) المضمن فهم الصور.

الخاصية | القيمة  
---|---  
النموذج | `glm-4.6v`  
  
يتم حل فهم الصور تلقائيا من مصادقة [Z.AI](<http://Z.AI>) المكونة، ولا حاجة إلى إعدادات إضافية.

Auth details

  * تستخدم [Z.AI](<http://Z.AI>) مصادقة Bearer مع مفتاح API الخاص بك.
  * يكتشف اختيار الإعداد الأولي `zai-api-key` نقطة نهاية [Z.AI](<http://Z.AI>) المطابقة تلقائيا من بادئة المفتاح.
  * استخدم الاختيارات الإقليمية الصريحة (`zai-coding-global` و`zai-coding-cn` و`zai-global` و`zai-cn`) عندما تريد فرض سطح API محدد.


## ذات صلة

[**GLM model family** نظرة عامة على عائلة نماذج GLM. ](</ar/providers/glm>) [**Model selection** اختيار الموفرين ومراجع النماذج وسلوك الانتقال عند الفشل. ](</ar/concepts/model-providers>)

Was this useful?YesNo