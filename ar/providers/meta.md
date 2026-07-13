---
title: بيانات وصفية
source_url: https://docs.openclaw.ai/ar/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

تستخدم **واجهة Meta API** واجهة **Responses API** المتوافقة مع OpenAI ‏(`POST /v1/responses`) لنموذج الاستدلال `muse-spark-1.1`. يُشحن المزوّد في صورة Plugin مضمن في OpenClaw.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `meta`  
Plugin | مزوّد مضمن  
متغير بيئة المصادقة | `MODEL_API_KEY`  
علامة الإعداد الأولي | `--auth-choice meta-api-key`  
علامة CLI المباشرة | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
عنوان URL الأساسي | `https://api.meta.ai/v1`  
النموذج الافتراضي | `meta/muse-spark-1.1`  
الاستدلال الافتراضي | `high` (`reasoning.effort`)  
  
## بدء الاستخدام

* ### تعيين مفتاح API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### التحقق من توفر النماذج

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

يسرد إدخال الكتالوج الثابت `muse-spark-1.1`. إذا تعذر تحديد قيمة `MODEL_API_KEY`، يُبلغ `openclaw models status --json` عن بيانات الاعتماد المفقودة ضمن `auth.unusableProfiles`.

## الإعداد غير التفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## الكتالوج المدمج

مرجع النموذج | الاسم | الاستدلال | نافذة السياق | الحد الأقصى للمخرجات  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | نعم | 1,048,576 | 131,072  
  
الإمكانات:

  * إدخال النصوص والصور
  * استدعاء الأدوات والبث
  * جهد الاستدلال: `minimal`، و`low`، و`medium`، و`high`، و`xhigh` (الافتراضي: `high`)
  * إعادة تشغيل الاستدلال المشفر من دون حالة (`store: false`, `include: ["reasoning.encrypted_content"]`)


## الضبط اليدوي

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## اختبار التحقق السريع

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

تستخدم الاختبارات المباشرة `muse-spark-1.1` مع `POST /v1/responses`.

## ذو صلة

[**مزوّدو النماذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الأعطال. ](</ar/concepts/model-providers>) [**أوضاع التفكير** مستويات جهد الاستدلال للنموذج muse-spark-1.1. ](</ar/tools/thinking>) [**مرجع الضبط** الإعدادات الافتراضية للوكيل وضبط النماذج. ](</ar/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue