---
title: Fireworks
source_url: https://docs.openclaw.ai/ar/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) تتيح نماذج مفتوحة الأوزان ونماذج موجّهة عبر API متوافق مع OpenAI. يتضمن OpenClaw Plugin مزود Fireworks مضمّنا يأتي مع نموذجي Kimi مفهرسين مسبقا ويقبل أي معرّف نموذج أو موجّه من Fireworks في وقت التشغيل.

الخاصية | القيمة  
---|---  
معرّف المزود | `fireworks` (الاسم البديل: `fireworks-ai`)  
Plugin | مضمّن، `enabledByDefault: true`  
متغير بيئة المصادقة | `FIREWORKS_API_KEY`  
علم الإعداد الأولي | `--auth-choice fireworks-api-key`  
علم CLI مباشر | `--fireworks-api-key <key>`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.fireworks.ai/inference/v1`  
النموذج الافتراضي | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
الاسم البديل الافتراضي | `Kimi K2.5 Turbo`  
  
## البدء

* ### Set the Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

يخزن الإعداد الأولي المفتاح مقابل مزود `fireworks` في ملفات تعريف المصادقة لديك ويعيّن موجّه Kimi K2.5 Turbo **Fire Pass** كنموذج افتراضي.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

يجب أن تتضمن القائمة `Kimi K2.6` و`Kimi K2.5 Turbo (Fire Pass)`. إذا لم يتم حل `FIREWORKS_API_KEY`، فسيبلغ `openclaw models status --json` عن بيانات الاعتماد المفقودة ضمن `auth.unusableProfiles`.

## الإعداد غير التفاعلي

لعمليات التثبيت النصية أو تثبيت CI، مرّر كل شيء في سطر الأوامر:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## الفهرس المضمّن

مرجع النموذج | الاسم | الإدخال | السياق | أقصى إخراج | التفكير  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | نص + صورة | 262,144 | 262,144 | مفروض إيقافه  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | نص + صورة | 256,000 | 256,000 | مفروض إيقافه (افتراضي)  
  
## معرّفات نماذج Fireworks المخصصة

يقبل OpenClaw أي معرّف نموذج أو موجّه من Fireworks في وقت التشغيل. استخدم المعرّف الدقيق الذي تعرضه Fireworks وأضف إليه البادئة `fireworks/`. ينسخ الحل الديناميكي قالب Fire Pass (إدخال نص + صورة، API متوافق مع OpenAI، تكلفة افتراضية صفر) ويعطّل التفكير تلقائيا عندما يطابق المعرّف نمط Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

يبدأ كل مرجع نموذج Fireworks في OpenClaw بـ `fireworks/` متبوعا بالمعرّف الدقيق أو مسار الموجّه من منصة Fireworks. على سبيل المثال:

  * نموذج موجّه: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * نموذج مباشر: `fireworks/accounts/fireworks/models/<model-name>`


يزيل OpenClaw بادئة `fireworks/` عند إنشاء طلب API ويرسل المسار المتبقي إلى نقطة نهاية Fireworks بوصفه حقل `model` المتوافق مع OpenAI.

Why thinking is forced off for Kimi

يعيد Fireworks K2.6 الرمز 400 إذا حمل الطلب معاملات `reasoning_*` على الرغم من أن Kimi يدعم التفكير عبر API الخاص بـ Moonshot. لا تعلن السياسة المضمّنة (`extensions/fireworks/thinking-policy.ts`) إلا مستوى التفكير `off` لمعرّفات نماذج Kimi، لذلك تظل تبديلات `/think` اليدوية وأسطح سياسة المزود متوافقة مع عقد وقت التشغيل.

لاستخدام استدلال Kimi من البداية إلى النهاية، اضبط [مزود Moonshot](</ar/providers/moonshot>) ووجّه النموذج نفسه عبره.

Environment availability for the daemon

إذا كان Gateway يعمل كخدمة مدارة (launchd، systemd، Docker)، فيجب أن يكون مفتاح Fireworks مرئيا لتلك العملية، وليس فقط لصدفتك التفاعلية.

على macOS، يقوم `openclaw gateway install` بالفعل بتوصيل `~/.openclaw/.env` بملف بيئة LaunchAgent. أعد تشغيل التثبيت (أو `openclaw doctor --fix`) بعد تدوير المفتاح.

## ذو صلة

[**Model providers** اختيار المزودين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Thinking modes** مستويات `/think` وسياسات المزودين وتوجيه النماذج القادرة على الاستدلال. ](</ar/tools/thinking>) [**Moonshot** شغّل Kimi مع مخرجات التفكير الأصلية عبر API الخاص بـ Moonshot. ](</ar/providers/moonshot>) [**Troubleshooting** استكشاف الأخطاء وإصلاحها العام والأسئلة الشائعة. ](</ar/help/troubleshooting>)

Was this useful?YesNo