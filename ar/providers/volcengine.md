---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/ar/providers/volcengine
scraped_at: 2026-05-25
---

يوفّر مزوّد Volcengine إمكانية الوصول إلى نماذج Doubao والنماذج التابعة لجهات خارجية المستضافة على Volcano Engine، مع نقاط نهاية منفصلة لأعباء العمل العامة وأعباء عمل البرمجة. ويمكن لـ Plugin المضمّن نفسه أيضًا تسجيل Volcengine Speech كمزوّد TTS.

التفاصيل | القيمة  
---|---  
المزوّدات | `volcengine` (عام + TTS) + `volcengine-plan` (للبرمجة)  
مصادقة النموذج | `VOLCANO_ENGINE_API_KEY`  
مصادقة TTS | `VOLCENGINE_TTS_API_KEY` أو `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | نماذج متوافقة مع OpenAI، وBytePlus Seed Speech TTS  
  
## البدء

* ### تعيين مفتاح API

شغّل الإعداد التفاعلي:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

يسجّل هذا كِلَا المزوّدين العام (`volcengine`) ومزوّد البرمجة (`volcengine-plan`) باستخدام مفتاح API واحد.

* ### تعيين نموذج افتراضي

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### التحقق من توفر النموذج

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## المزوّدات ونقاط النهاية

المزوّد | نقطة النهاية | حالة الاستخدام  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | النماذج العامة  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | نماذج البرمجة  
  
## الفهرس المضمّن

### عام (volcengine)

مرجع النموذج | الاسم | الإدخال | السياق  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | نص، صورة | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | نص، صورة | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | نص، صورة | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | نص، صورة | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | نص، صورة | 128,000  
  
### للبرمجة (volcengine-plan)

مرجع النموذج | الاسم | الإدخال | السياق  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | نص | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | نص | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | نص | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | نص | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | نص | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | نص | 256,000  
  
## تحويل النص إلى كلام

يستخدم Volcengine TTS واجهة BytePlus Seed Speech HTTP API، ويتم إعداده بشكل منفصل عن مفتاح API الخاص بنماذج Doubao المتوافقة مع OpenAI. في وحدة تحكم BytePlus، افتح Seed Speech > Settings > API Keys وانسخ مفتاح API، ثم عيّن:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

ثم فعّله في `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

بالنسبة إلى أهداف الملاحظات الصوتية، يطلب OpenClaw من Volcengine تنسيق `ogg_opus` الأصلي الخاص بالمزوّد. وبالنسبة إلى مرفقات الصوت العادية، يطلب تنسيق `mp3`. كما تُحل الأسماء البديلة للمزوّد `bytedance` و`doubao` إلى مزوّد الكلام نفسه.

المعرّف الافتراضي للمورد هو `seed-tts-1.0` لأن هذا هو المورد الذي تمنحه BytePlus لمفاتيح API الجديدة الخاصة بـ Seed Speech في المشروع الافتراضي. إذا كان مشروعك يملك صلاحية TTS 2.0، فعيّن `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

لا يزال دعم المصادقة القديمة باستخدام AppID/الرمز متاحًا لتطبيقات Speech Console الأقدم:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## الإعدادات المتقدمة

النموذج الافتراضي بعد الإعداد

يعيّن `openclaw onboard --auth-choice volcengine-api-key` حاليًا `volcengine-plan/ark-code-latest` كنموذج افتراضي، مع تسجيل الفهرس العام `volcengine` أيضًا.

سلوك الرجوع في منتقي النموذج

أثناء الإعداد أو اختيار النموذج في التهيئة، يفضّل خيار مصادقة Volcengine الصفوف `volcengine/*` و`volcengine-plan/*` معًا. وإذا لم تكن هذه النماذج محمّلة بعد، فسيرجع OpenClaw إلى الفهرس غير المصفّى بدلًا من عرض منتقي فارغ مقيّد بنطاق المزوّد.

متغيرات البيئة لعمليات daemon

إذا كانت Gateway تعمل كعملية daemon (‏launchd/systemd)، فتأكد من أن متغيرات البيئة الخاصة بالنموذج وTTS مثل `VOLCANO_ENGINE_API_KEY` و`VOLCENGINE_TTS_API_KEY`، و`BYTEPLUS_SEED_SPEECH_API_KEY`، و`VOLCENGINE_TTS_APPID`، و `VOLCENGINE_TTS_TOKEN` متاحة لتلك العملية (على سبيل المثال، في `~/.openclaw/.env` أو عبر `env.shellEnv`).

## ذو صلة

[**اختيار النموذج** اختيار المزوّدات، ومراجع النماذج، وسلوك التجاوز عند الفشل. ](</ar/concepts/model-providers>) [**الإعدادات** المرجع الكامل لإعدادات الوكلاء، والنماذج، والمزوّدات. ](</ar/gateway/configuration>) [**استكشاف الأخطاء وإصلاحها** المشكلات الشائعة وخطوات التصحيح. ](</ar/help/troubleshooting>) [**الأسئلة الشائعة** الأسئلة الشائعة حول إعداد OpenClaw. ](</ar/help/faq>)

Was this useful?YesNo