---
title: NVIDIA
source_url: https://docs.openclaw.ai/ar/providers/nvidia
scraped_at: 2026-05-25
---

توفر NVIDIA واجهة API متوافقة مع OpenAI على `https://integrate.api.nvidia.com/v1` للنماذج المفتوحة مجانًا. صادِق باستخدام مفتاح API من [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## البدء

* ### Get your API key

أنشئ مفتاح API في [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Export the key and run onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Set an NVIDIA model

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

للإعداد غير التفاعلي، يمكنك أيضًا تمرير المفتاح مباشرةً:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## مثال على التكوين

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## الكتالوج المضمّن

مرجع النموذج | الاسم | السياق | أقصى مخرجات  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## التكوين المتقدم

Auto-enable behavior

يتم تفعيل المزوّد تلقائيًا عند ضبط متغير البيئة `NVIDIA_API_KEY`. لا يلزم أي تكوين صريح للمزوّد سوى المفتاح.

Catalog and pricing

الكتالوج المجمّع ثابت. تُضبط التكاليف افتراضيًا على `0` في المصدر لأن NVIDIA توفر حاليًا وصولًا مجانيًا إلى API للنماذج المدرجة.

OpenAI-compatible endpoint

تستخدم NVIDIA نقطة نهاية الإكمال القياسية `/v1`. يجب أن تعمل أي أدوات متوافقة مع OpenAI مباشرةً مع عنوان URL الأساسي من NVIDIA.

Slow custom provider responses

قد تستغرق بعض النماذج المخصصة المستضافة لدى NVIDIA وقتًا أطول من مراقب خمول النموذج الافتراضي قبل أن تصدر أول جزء من الاستجابة. بالنسبة إلى إدخالات مزوّد NVIDIA المخصصة، ارفع مهلة المزوّد بدلًا من رفع مهلة تشغيل الوكيل بالكامل:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## ذات صلة

[**Model selection** اختيار المزوّدين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Configuration reference** مرجع التكوين الكامل للوكلاء، والنماذج، والمزوّدين. ](</ar/gateway/configuration-reference>)

Was this useful?YesNo