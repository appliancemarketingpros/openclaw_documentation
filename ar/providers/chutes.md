---
title: Chutes
source_url: https://docs.openclaw.ai/ar/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) تتيح كتالوجات النماذج مفتوحة المصدر عبر واجهة API متوافقة مع OpenAI. يدعم OpenClaw كلاً من OAuth عبر المتصفح والمصادقة المباشرة بمفتاح API لموفر `chutes` المضمن.

الخاصية | القيمة  
---|---  
الموفر | `chutes`  
API | متوافقة مع OpenAI  
عنوان URL الأساسي | `https://llm.chutes.ai/v1`  
المصادقة | OAuth أو مفتاح API (انظر أدناه)  
  
## البدء

### OAuth

* ### Run the OAuth onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

يشغّل OpenClaw تدفق المتصفح محلياً، أو يعرض عنوان URL + تدفق لصق إعادة التوجيه على المضيفات البعيدة/دون واجهة رسومية. تُحدَّث رموز OAuth تلقائياً عبر ملفات تعريف مصادقة OpenClaw.

* ### Verify the default model

بعد الإعداد، يُضبط النموذج الافتراضي على `chutes/zai-org/GLM-4.7-TEE` ويُسجَّل كتالوج Chutes المضمن.

### API key

* ### Get an API key

أنشئ مفتاحاً في [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Run the API key onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verify the default model

بعد الإعداد، يُضبط النموذج الافتراضي على `chutes/zai-org/GLM-4.7-TEE` ويُسجَّل كتالوج Chutes المضمن.

## سلوك الاكتشاف

عندما تكون مصادقة Chutes متاحة، يستعلم OpenClaw عن كتالوج Chutes باستخدام بيانات الاعتماد تلك ويستخدم النماذج المكتشفة. إذا فشل الاكتشاف، يعود OpenClaw إلى كتالوج ثابت مضمن كي يستمر الإعداد وبدء التشغيل في العمل.

## الأسماء المستعارة الافتراضية

يسجّل OpenClaw ثلاثة أسماء مستعارة ملائمة لكتالوج Chutes المضمن:

الاسم المستعار | النموذج الهدف  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## كتالوج البدء المدمج

يتضمن كتالوج الرجوع المضمن مراجع Chutes الحالية:

مرجع النموذج  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## مثال التكوين

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

يمكنك تخصيص تدفق OAuth باستخدام متغيرات بيئة اختيارية:

المتغير | الغرض  
---|---  
`CHUTES_CLIENT_ID` | معرّف عميل OAuth مخصص  
`CHUTES_CLIENT_SECRET` | سر عميل OAuth مخصص  
`CHUTES_OAUTH_REDIRECT_URI` | URI إعادة توجيه مخصص  
`CHUTES_OAUTH_SCOPES` | نطاقات OAuth مخصصة  
  
راجع [وثائق Chutes OAuth](<https://chutes.ai/docs/sign-in-with-chutes/overview>) لمعرفة متطلبات تطبيق إعادة التوجيه والحصول على المساعدة.

Notes

  * يستخدم كل من اكتشاف مفتاح API وOAuth معرّف موفر `chutes` نفسه.
  * تُسجَّل نماذج Chutes بصيغة `chutes/<model-id>`.
  * إذا فشل الاكتشاف عند بدء التشغيل، يُستخدم الكتالوج الثابت المضمن تلقائياً.


## ذات صلة

[**Model selection** قواعد الموفرين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Configuration reference** مخطط التكوين الكامل بما في ذلك إعدادات الموفر. ](</ar/gateway/configuration-reference>) [**Chutes** لوحة تحكم Chutes ووثائق API. ](<https://chutes.ai>) [**Chutes API keys** أنشئ مفاتيح API الخاصة بـ Chutes وأدرها. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo