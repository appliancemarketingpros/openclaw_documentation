---
title: SGLang
source_url: https://docs.openclaw.ai/ar/providers/sglang
scraped_at: 2026-05-25
---

توفّر SGLang النماذج مفتوحة الأوزان عبر واجهة API HTTP متوافقة مع OpenAI. يتصل OpenClaw بـ SGLang باستخدام عائلة المزوّد `openai-completions` مع الاكتشاف التلقائي للنماذج المتاحة.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `sglang`  
Plugin | مضمّن، `enabledByDefault: true`  
متغيّر بيئة المصادقة | `SGLANG_API_KEY` (أي قيمة غير فارغة إذا لم تكن لدى الخادم مصادقة)  
علم التهيئة الأولية | `--auth-choice sglang`  
API | متوافقة مع OpenAI (`openai-completions`)  
عنوان URL الأساسي الافتراضي | `http://127.0.0.1:30000/v1`  
العنصر النائب الافتراضي للنموذج | `sglang/Qwen/Qwen3-8B`  
استخدام البث | نعم (`supportsStreamingUsage: true`)  
التسعير | موسوم كخارجي مجاني (`modelPricing.external: false`)  
  
يقوم OpenClaw أيضًا **بالاكتشاف التلقائي** للنماذج المتاحة من SGLang عندما تختار ذلك باستخدام `SGLANG_API_KEY`. استخدم `sglang/*` في `agents.defaults.models` لإبقاء الاكتشاف ديناميكيًا عندما تضبط أيضًا عنوان URL أساسيًا مخصصًا لـ SGLang. راجع اكتشاف النموذج (مزوّد ضمني) أدناه.

## البدء

* ### ابدأ SGLang

شغّل SGLang مع خادم متوافق مع OpenAI. يجب أن يوفّر عنوان URL الأساسي لديك نقاط نهاية `/v1` (على سبيل المثال `/v1/models` و`/v1/chat/completions`). تعمل SGLang عادةً على:

  * `http://127.0.0.1:30000/v1`


* ### عيّن مفتاح API

تعمل أي قيمة إذا لم تكن المصادقة مضبوطة على خادمك:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### شغّل التهيئة الأولية أو عيّن نموذجًا مباشرة

bashCopy code
[code]
    openclaw onboard
[/code]

أو اضبط النموذج يدويًا:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## اكتشاف النموذج (مزوّد ضمني)

عند تعيين `SGLANG_API_KEY` (أو وجود ملف تعريف مصادقة) و**عدم** تعريف `models.providers.sglang`، سيستعلم OpenClaw عن:

  * `GET http://127.0.0.1:30000/v1/models`


ويحوّل المعرّفات المُعادة إلى إدخالات نماذج.

## الضبط الصريح (نماذج يدوية)

استخدم الضبط الصريح عندما:

  * تعمل SGLang على مضيف/منفذ مختلف.
  * تريد تثبيت قيم `contextWindow`/`maxTokens`.
  * يتطلب خادمك مفتاح API حقيقيًا (أو تريد التحكم في الرؤوس).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## الضبط المتقدم

سلوك بنمط الوكيل

تُعامل SGLang كواجهة خلفية `/v1` متوافقة مع OpenAI بنمط الوكيل، وليست نقطة نهاية OpenAI أصلية.

السلوك | SGLang  
---|---  
تشكيل الطلبات الخاص بـ OpenAI فقط | غير مطبّق  
`service_tier`، و`store` في Responses، وتلميحات ذاكرة التخزين المؤقت للمطالبات | لا تُرسل  
تشكيل حمولة توافق الاستدلال | غير مطبّق  
رؤوس الإسناد المخفية (`originator`، `version`، `User-Agent`) | لا تُحقن في عناوين URL الأساسية المخصصة لـ SGLang  
استكشاف الأخطاء وإصلاحها

**يتعذر الوصول إلى الخادم**

تحقق من أن الخادم يعمل ويستجيب:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**أخطاء المصادقة**

إذا فشلت الطلبات بسبب أخطاء مصادقة، فعيّن `SGLANG_API_KEY` حقيقيًا يطابق ضبط خادمك، أو اضبط المزوّد صراحةً ضمن `models.providers.sglang`.

## ذات صلة

[**اختيار النموذج** اختيار المزوّدين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**مرجع الضبط** مخطط الضبط الكامل بما في ذلك إدخالات المزوّدين. ](</ar/gateway/configuration-reference>)

Was this useful?YesNo