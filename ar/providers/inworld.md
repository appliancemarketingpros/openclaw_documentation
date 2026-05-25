---
title: Inworld
source_url: https://docs.openclaw.ai/ar/providers/inworld
scraped_at: 2026-05-25
---

Inworld هو مزوّد تحويل النص إلى كلام (TTS) بالبث. في OpenClaw، يقوم بتوليف صوت الردود الصادرة (MP3 افتراضيًا، وOGG_OPUS للملاحظات الصوتية) وصوت PCM لقنوات الاتصالات الهاتفية مثل المكالمة الصوتية.

ينشر OpenClaw إلى نقطة نهاية TTS بالبث الخاصة بـ Inworld، ويجمع مقاطع الصوت المرجعة بترميز base64 في مخزن مؤقت واحد، ثم يمرر النتيجة إلى مسار صوت الرد القياسي.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `inworld`  
Plugin | مضمن، `enabledByDefault: true`  
العقد | `speechProviders` (TTS فقط)  
متغير بيئة المصادقة | `INWORLD_API_KEY` (HTTP Basic، اعتماد لوحة المعلومات Base64)  
عنوان URL الأساسي | `https://api.inworld.ai`  
الصوت الافتراضي | `Sarah`  
النموذج الافتراضي | `inworld-tts-1.5-max`  
الإخراج | MP3 (افتراضي)، OGG_OPUS (ملاحظات صوتية)، PCM 22050 Hz (اتصالات هاتفية)  
الموقع الإلكتروني | [inworld.ai](<https://inworld.ai>)  
المستندات | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## البدء

* ### عيّن مفتاح API الخاص بك

انسخ الاعتماد من لوحة معلومات Inworld الخاصة بك (Workspace > API Keys) وعيّنه كمتغير بيئة. تُرسل القيمة كما هي كاعتماد HTTP Basic، لذلك لا ترمّزها بـ Base64 مرة أخرى ولا تحوّلها إلى رمز bearer.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### اختر Inworld في messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### أرسل رسالة

أرسل ردًا عبر أي قناة متصلة. يقوم OpenClaw بتوليف الصوت باستخدام Inworld ويسلّمه كـ MP3 (أو OGG_OPUS عندما تتوقع القناة ملاحظة صوتية).

## خيارات التكوين

الخيار | المسار | الوصف  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | اعتماد لوحة المعلومات Base64. يعود إلى `INWORLD_API_KEY` عند عدم ضبطه.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | تجاوز عنوان URL الأساسي لـ API الخاص بـ Inworld (الافتراضي `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | معرّف الصوت (الافتراضي `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | معرّف نموذج TTS (الافتراضي `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | درجة حرارة أخذ العينات `0..2` (اختياري).  
  
## ملاحظات

المصادقة

يستخدم Inworld مصادقة HTTP Basic بسلسلة اعتماد واحدة مرمّزة بـ Base64. انسخها كما هي من لوحة معلومات Inworld. يرسلها المزوّد كـ `Authorization: Basic <apiKey>` دون أي ترميز إضافي، لذلك لا ترمّزها بـ Base64 بنفسك ولا تمرر رمزًا بأسلوب bearer. راجع [ملاحظات مصادقة TTS](</ar/tools/tts#inworld-primary>) للاطلاع على التنبيه نفسه.

النماذج

معرّفات النماذج المدعومة: `inworld-tts-1.5-max` (افتراضي)، `inworld-tts-1.5-mini`، `inworld-tts-1-max`، `inworld-tts-1`.

مخرجات الصوت

تستخدم الردود MP3 افتراضيًا. عندما يكون هدف القناة هو `voice-note` يطلب OpenClaw من Inworld استخدام `OGG_OPUS` بحيث يُشغّل الصوت كفقاعة صوتية أصلية. يستخدم توليف الاتصالات الهاتفية `PCM` خامًا عند 22050 Hz لتغذية جسر الاتصالات الهاتفية.

نقاط النهاية المخصصة

تجاوز مضيف API باستخدام `messages.tts.providers.inworld.baseUrl`. تُزال الشرطات المائلة اللاحقة قبل إرسال الطلبات.

## ذات صلة

[**تحويل النص إلى كلام** نظرة عامة على TTS، والمزوّدون، وتكوين `messages.tts`. ](</ar/tools/tts>) [**التكوين** مرجع التكوين الكامل بما في ذلك إعدادات `messages.tts`. ](</ar/gateway/configuration>) [**المزوّدون** جميع مزوّدي OpenClaw المضمنين. ](</ar/providers>) [**استكشاف الأخطاء وإصلاحها** المشكلات الشائعة وخطوات التصحيح. ](</ar/help/troubleshooting>)

Was this useful?YesNo