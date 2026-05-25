---
title: Gradium
source_url: https://docs.openclaw.ai/ar/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) هو مزوّد مضمّن لتحويل النص إلى كلام في OpenClaw. يمكن لـ Plugin إنشاء ردود صوتية عادية (WAV)، ومخرجات Opus متوافقة مع الملاحظات الصوتية، وصوت u-law بتردد 8 kHz لواجهات الاتصالات الهاتفية.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `gradium`  
المصادقة | `GRADIUM_API_KEY` أو config `apiKey`  
عنوان URL الأساسي | `https://api.gradium.ai` (افتراضي)  
الصوت الافتراضي | `Emma` (`YTpq7expH9539ERJ`)  
  
## الإعداد

أنشئ مفتاح Gradium API، ثم أتحه لـ OpenClaw إما عبر متغيّر بيئة أو مفتاح config.

### متغيّر البيئة

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### مفتاح config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

يتحقق Plugin أولاً من `apiKey` بعد حله، ثم يعود إلى متغيّر البيئة `GRADIUM_API_KEY`.

## الإعدادات

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

المفتاح | النوع | الوصف  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | مفتاح API بعد حله. يدعم `${ENV}` ومراجع الأسرار.  
`messages.tts.providers.gradium.baseUrl` | string | يتجاوز أصل API. تُزال الشرطات المائلة اللاحقة. الإعداد الافتراضي هو `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | معرّف الصوت الافتراضي المستخدم عند عدم وجود تجاوز عبر توجيه.  
  
يُحدَّد تنسيق الصوت الناتج تلقائياً بواسطة وقت التشغيل بناءً على الواجهة المستهدفة، ولا يمكن ضبطه من `openclaw.json`. راجع المخرجات أدناه.

## الأصوات

الاسم | معرّف الصوت  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
الصوت الافتراضي: Emma.

### تجاوز الصوت لكل رسالة

عندما تسمح سياسة الكلام النشطة بتجاوزات الصوت، يمكنك تبديل الأصوات ضمن السطر باستخدام رمز توجيه. تُحل كل هذه إلى تجاوز `voiceId` نفسه:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

إذا عطّلت سياسة الكلام تجاوزات الصوت، فسيُستهلك التوجيه لكن يُتجاهل.

## المخرجات

يختار وقت التشغيل تنسيق المخرجات من الواجهة المستهدفة. لا ينشئ المزوّد تنسيقات أخرى حالياً.

الهدف | التنسيق | امتداد الملف | معدّل العينة | علامة التوافق مع الصوت  
---|---|---|---|---  
صوت قياسي | `wav` | `.wav` | provider | لا  
ملاحظة صوتية | `opus` | `.opus` | provider | نعم  
اتصالات هاتفية | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## ترتيب الاختيار التلقائي

ضمن مزوّدي TTS المهيأين، يكون ترتيب الاختيار التلقائي لـ Gradium هو `30`. راجع [تحويل النص إلى كلام](</ar/tools/tts>) لمعرفة كيفية اختيار OpenClaw للمزوّد النشط عندما لا يكون `messages.tts.provider` مثبتاً.

## ذو صلة

  * [تحويل النص إلى كلام](</ar/tools/tts>)
  * [نظرة عامة على الوسائط](</ar/tools/media-overview>)


Was this useful?YesNo