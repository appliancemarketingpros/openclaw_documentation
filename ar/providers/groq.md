---
title: Groq
source_url: https://docs.openclaw.ai/ar/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) يوفر استدلالًا فائق السرعة على نماذج مفتوحة الأوزان (Llama وGemma وKimi وQwen وGPT OSS والمزيد) باستخدام عتاد LPU مخصص. يتضمن OpenClaw Plugin مدمجًا لـ Groq يسجل كلًا من مزود دردشة متوافق مع OpenAI ومزود فهم وسائط صوتية.

الخاصية | القيمة  
---|---  
معرف المزود | `groq`  
Plugin | مدمج، `enabledByDefault: true`  
متغير بيئة المصادقة | `GROQ_API_KEY`  
علم الإعداد الأولي | `--auth-choice groq-api-key`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.groq.com/openai/v1`  
نسخ الصوت | `whisper-large-v3-turbo` (الافتراضي)  
الإعداد الافتراضي المقترح للدردشة | `groq/llama-3.3-70b-versatile`  
  
## البدء

* ### احصل على مفتاح API

أنشئ مفتاح API في [console.groq.com/keys](<https://console.groq.com/keys>).

* ### عيّن مفتاح API

الإعداد الأوليCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

البيئة فقطCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### عيّن نموذجًا افتراضيًا

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### تحقق من إمكانية الوصول إلى الكتالوج

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### مثال ملف الإعدادات

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## الكتالوج المدمج

يشحن OpenClaw كتالوج Groq مدعومًا بملف manifest يتضمن إدخالات استدلالية وغير استدلالية. شغّل `openclaw models list --provider groq` للاطلاع على الصفوف المدمجة في الإصدار المثبت لديك، أو راجع [console.groq.com/docs/models](<https://console.groq.com/docs/models>) للاطلاع على قائمة Groq المعتمدة.

مرجع النموذج | الاسم | الاستدلال | الإدخال | السياق  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | لا | نص | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | لا | نص | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | لا | نص + صورة | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | لا | نص + صورة | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | لا | نص | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | لا | نص | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | لا | نص | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | لا | نص | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | لا | نص | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | لا | نص | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | نعم | نص | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | نعم | نص | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | نعم | نص | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | نعم | نص | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | نعم | نص | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | نعم | نص | 131,072  
`groq/groq/compound` | Compound | نعم | نص | 131,072  
`groq/groq/compound-mini` | Compound Mini | نعم | نص | 131,072  
  
## نماذج الاستدلال

يربط OpenClaw مستويات `/think` المشتركة بقيم `reasoning_effort` الخاصة بنماذج Groq:

  * بالنسبة إلى `qwen/qwen3-32b`، يرسل التفكير المعطل `none` ويرسل التفكير المفعّل `default`.
  * بالنسبة إلى نماذج استدلال Groq GPT OSS (`openai/gpt-oss-*`)، يرسل OpenClaw `low` أو `medium` أو `high` بناءً على مستوى `/think`. عند تعطيل التفكير، لا يرسل `reasoning_effort` لأن هذه النماذج لا تدعم قيمة معطلة.
  * تستخدم DeepSeek R1 Distill وQwen QwQ وCompound سطح الاستدلال الأصلي في Groq؛ يتحكم `/think` في الظهور، لكن النموذج يستدل دائمًا.


راجع [أوضاع التفكير](</ar/tools/thinking>) لمعرفة مستويات `/think` المشتركة وكيف يترجمها OpenClaw لكل مزود.

## نسخ الصوت

يسجل Plugin Groq المدمج أيضًا **مزود فهم وسائط صوتية** بحيث يمكن نسخ الرسائل الصوتية عبر سطح `tools.media.audio` المشترك.

الخاصية | القيمة  
---|---  
مسار الإعداد المشترك | `tools.media.audio`  
عنوان URL الأساسي الافتراضي | `https://api.groq.com/openai/v1`  
النموذج الافتراضي | `whisper-large-v3-turbo`  
الأولوية التلقائية | 20  
نقطة نهاية API | متوافقة مع OpenAI `/audio/transcriptions`  
  
لجعل Groq الواجهة الخلفية الافتراضية للصوت:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

توفر البيئة للبرنامج الخفي

إذا كان Gateway يعمل كخدمة مُدارة (launchd أو systemd أو Docker)، فيجب أن يكون `GROQ_API_KEY` مرئيًا لتلك العملية، وليس فقط للصدفة التفاعلية لديك.

معرفات نماذج Groq المخصصة

يقبل OpenClaw أي معرف نموذج Groq في وقت التشغيل. استخدم المعرف الدقيق الذي يعرضه Groq وأضف إليه البادئة `groq/`. يغطي الكتالوج المدمج الحالات الشائعة؛ أما المعرفات غير الموجودة في الكتالوج فتستخدم قالب OpenAI المتوافق الافتراضي.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## ذات صلة

[**مزودو النماذج** اختيار المزودين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**أوضاع التفكير** مستويات جهد الاستدلال وتفاعل سياسة المزود. ](</ar/tools/thinking>) [**مرجع الإعدادات** مخطط الإعدادات الكامل، بما في ذلك إعدادات المزود والصوت. ](</ar/gateway/configuration-reference>) [**Groq Console** لوحة معلومات Groq ووثائق API والتسعير. ](<https://console.groq.com>)

Was this useful?YesNo