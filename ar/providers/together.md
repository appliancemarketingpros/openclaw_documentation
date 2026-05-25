---
title: Together AI
source_url: https://docs.openclaw.ai/ar/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) يوفّر وصولًا إلى نماذج مفتوحة المصدر رائدة، بما في ذلك Llama وDeepSeek وKimi والمزيد، عبر API موحّد.

الخاصية | القيمة  
---|---  
المزوّد | `together`  
المصادقة | `TOGETHER_API_KEY`  
API | متوافق مع OpenAI  
عنوان URL الأساسي | `https://api.together.xyz/v1`  
  
## البدء

* ### احصل على مفتاح API

أنشئ مفتاح API في [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### عيّن نموذجًا افتراضيًا

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### مثال غير تفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## الكتالوج المضمّن

يشحن OpenClaw كتالوج Together المضمّن هذا:

مرجع النموذج | الاسم | الإدخال | السياق | الملاحظات  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | نص، صورة | 262,144 | النموذج الافتراضي؛ الاستدلال مفعّل  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | نص | 202,752 | نموذج نصوص عام الغرض  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | نص | 131,072 | نموذج تعليمات سريع  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | نص، صورة | 10,000,000 | متعدد الوسائط  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | نص، صورة | 20,000,000 | متعدد الوسائط  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | نص | 131,072 | نموذج نصوص عام  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | نص | 131,072 | نموذج استدلال  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | نص | 262,144 | نموذج نصوص Kimi ثانوي  
  
## إنشاء الفيديو

يسجّل Plugin `together` المضمّن أيضًا إنشاء الفيديو من خلال أداة `video_generate` المشتركة.

الخاصية | القيمة  
---|---  
نموذج الفيديو الافتراضي | `together/Wan-AI/Wan2.2-T2V-A14B`  
الأوضاع | تحويل النص إلى فيديو، مرجع صورة واحدة  
المعلمات المدعومة | `aspectRatio`, `resolution`  
  
لاستخدام Together كمزوّد الفيديو الافتراضي:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

ملاحظة حول البيئة

إذا كان Gateway يعمل كبرنامج خفي (launchd/systemd)، فتأكد من إتاحة `TOGETHER_API_KEY` لتلك العملية (على سبيل المثال، في `~/.openclaw/.env` أو عبر `env.shellEnv`).

استكشاف الأخطاء وإصلاحها

  * تحقق من أن مفتاحك يعمل: `openclaw models list --provider together`
  * إذا لم تظهر النماذج، فتأكد من ضبط مفتاح API في البيئة الصحيحة لعملية Gateway لديك.
  * تستخدم مراجع النماذج الصيغة `together/<model-id>`.


## ذات صلة

[**اختيار النموذج** قواعد المزوّد، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**إنشاء الفيديو** معلمات أداة إنشاء الفيديو المشتركة واختيار المزوّد. ](</ar/tools/video-generation>) [**مرجع الإعدادات** مخطط الإعدادات الكامل، بما في ذلك إعدادات المزوّد. ](</ar/gateway/configuration-reference>) [**Together AI** لوحة تحكم Together AI، ووثائق API، والأسعار. ](<https://together.ai>)

Was this useful?YesNo