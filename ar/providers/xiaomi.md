---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/ar/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo هي منصة API لنماذج **MiMo**. يتضمن OpenClaw ‏Plugin مضمنا باسم `xiaomi` يسجل موفر محادثة متوافقا مع OpenAI وموفر كلام (TTS) مقابل `XIAOMI_API_KEY` نفسه.

الخاصية | القيمة  
---|---  
معرف الموفر | `xiaomi`  
Plugin | مضمن، `enabledByDefault: true`  
متغير بيئة المصادقة | `XIAOMI_API_KEY`  
علم الإعداد الأولي | `--auth-choice xiaomi-api-key`  
علم CLI المباشر | `--xiaomi-api-key <key>`  
العقود | إكمالات المحادثة + `speechProviders`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.xiaomimimo.com/v1`  
النموذج الافتراضي | `xiaomi/mimo-v2-flash`  
TTS الافتراضي | `mimo-v2.5-tts`، الصوت `mimo_default`  
  
## البدء

* ### احصل على مفتاح API

أنشئ مفتاح API في [وحدة تحكم Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### شغل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

أو مرر المفتاح مباشرة:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### تحقق من توفر النموذج

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## الفهرس المدمج

مرجع النموذج | الإدخال | السياق | الحد الأقصى للإخراج | الاستدلال | ملاحظات  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | نص | 262,144 | 8,192 | لا | النموذج الافتراضي  
`xiaomi/mimo-v2-pro` | نص | 1,048,576 | 32,000 | نعم | سياق كبير  
`xiaomi/mimo-v2-omni` | نص، صورة | 262,144 | 32,000 | نعم | متعدد الوسائط  
  
## تحويل النص إلى كلام

يسجل Plugin المضمن `xiaomi` أيضا Xiaomi MiMo كموفر كلام لـ `messages.tts`. يستدعي عقد TTS الخاص بإكمالات محادثة Xiaomi مع النص كرسالة `assistant` وإرشادات النمط الاختيارية كرسالة `user`.

الخاصية | القيمة  
---|---  
معرف TTS | `xiaomi` (الاسم المستعار `mimo`)  
المصادقة | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` مع `audio`  
الافتراضي | `mimo-v2.5-tts`، الصوت `mimo_default`  
الإخراج | MP3 افتراضيا؛ WAV عند تهيئته  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

تشمل الأصوات المدمجة المدعومة `mimo_default` و`default_zh` و`default_en` و`Mia` و`Chloe` و`Milo` و`Dean`. يدعم `mimo-v2-tts` حسابات MiMo TTS الأقدم؛ ويستخدم الافتراضي نموذج MiMo-V2.5 TTS الحالي. بالنسبة إلى أهداف الملاحظات الصوتية مثل Feishu وTelegram، يحول OpenClaw مخرجات Xiaomi إلى Opus بتردد 48kHz باستخدام `ffmpeg` قبل التسليم.

## مثال التهيئة

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

سلوك الحقن التلقائي

يتم حقن موفر `xiaomi` تلقائيا عند تعيين `XIAOMI_API_KEY` في بيئتك أو عند وجود ملف تعريف مصادقة. لا تحتاج إلى تهيئة الموفر يدويا إلا إذا أردت تجاوز بيانات تعريف النموذج أو عنوان URL الأساسي.

تفاصيل النموذج

  * **mimo-v2-flash** — خفيف وسريع، ومثالي لمهام النص العامة. لا يدعم الاستدلال.
  * **mimo-v2-pro** — يدعم الاستدلال مع نافذة سياق بحجم 1M من الرموز لأعباء عمل المستندات الطويلة.
  * **mimo-v2-omni** — نموذج متعدد الوسائط ممكّن للاستدلال يقبل إدخالات النص والصورة معا.

استكشاف الأخطاء وإصلاحها

  * إذا لم تظهر النماذج، فتأكد من أن `XIAOMI_API_KEY` معين وصالح.
  * عندما يعمل Gateway كخادم خلفي، تأكد من توفر المفتاح لتلك العملية (على سبيل المثال في `~/.openclaw/.env` أو عبر `env.shellEnv`).


## ذو صلة

[**اختيار النموذج** اختيار الموفرين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**مرجع التهيئة** مرجع تهيئة OpenClaw الكامل. ](</ar/gateway/configuration-reference>) [**وحدة تحكم Xiaomi MiMo** لوحة معلومات Xiaomi MiMo وإدارة مفاتيح API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo