---
title: Cerebras
source_url: https://docs.openclaw.ai/ar/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) توفّر استدلالًا عالي السرعة متوافقًا مع OpenAI على عتاد استدلال مخصّص. يتضمن OpenClaw Plugin مزوّد Cerebras مضمّنًا مع كتالوج ثابت من أربعة نماذج.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `cerebras`  
Plugin | مضمّن، `enabledByDefault: true`  
متغير بيئة المصادقة | `CEREBRAS_API_KEY`  
علامة الإعداد الأولي | `--auth-choice cerebras-api-key`  
علامة CLI مباشرة | `--cerebras-api-key <key>`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.cerebras.ai/v1`  
النموذج الافتراضي | `cerebras/zai-glm-4.7`  
  
## البدء

* ### الحصول على مفتاح API

أنشئ مفتاح API في [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### تشغيل الإعداد الأولي

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### التحقق من توفر النماذج

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

ينبغي أن تتضمن القائمة النماذج الأربعة المضمّنة كلها. إذا تعذّر حل `CEREBRAS_API_KEY`، فسيبلّغ `openclaw models status --json` عن بيانات الاعتماد المفقودة ضمن `auth.unusableProfiles`.

## إعداد غير تفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## الكتالوج المضمّن

يشحن OpenClaw كتالوج Cerebras ثابتًا يعكس نقطة النهاية العامة المتوافقة مع OpenAI. تشترك النماذج الأربعة كلها في سياق 128k و8,192 رمز إخراج كحد أقصى.

مرجع النموذج | الاسم | الاستدلال | ملاحظات  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | نعم | النموذج الافتراضي؛ نموذج استدلال للمعاينة  
`cerebras/gpt-oss-120b` | GPT OSS 120B | نعم | نموذج استدلال إنتاجي  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | لا | نموذج معاينة غير استدلالي  
`cerebras/llama3.1-8b` | Llama 3.1 8B | لا | نموذج إنتاجي يركز على السرعة  
  
## الإعداد اليدوي

يعني Plugin المضمّن عادةً أنك لا تحتاج إلا إلى مفتاح API. استخدم إعداد `models.providers.cerebras` الصريح عندما تريد تجاوز بيانات تعريف النموذج أو التشغيل في `mode: "merge"` مقابل الكتالوج الثابت:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## ذو صلة

[**مزوّدو النماذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**أوضاع التفكير** مستويات جهد الاستدلال لنموذجي Cerebras القادرين على الاستدلال. ](</ar/tools/thinking>) [**مرجع الإعداد** الإعدادات الافتراضية للوكلاء وإعدادات النماذج. ](</ar/gateway/config-agents#agent-defaults>) [**الأسئلة الشائعة حول النماذج** ملفات المصادقة الشخصية، وتبديل النماذج، وحل أخطاء "no profile". ](</ar/help/faq-models>)

Was this useful?YesNo