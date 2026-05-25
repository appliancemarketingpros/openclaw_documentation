---
title: SenseAudio
source_url: https://docs.openclaw.ai/ar/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio يمكنه نسخ مرفقات الصوت الواردة والملاحظات الصوتية عبر مسار `tools.media.audio` المشترك في OpenClaw. يرسل OpenClaw الصوت متعدد الأجزاء إلى نقطة نهاية النسخ المتوافقة مع OpenAI ويحقن النص المُعاد في صورة `{{Transcript}}` إضافةً إلى كتلة `[Audio]`.

الخاصية | القيمة  
---|---  
معرّف المزوّد | `senseaudio`  
Plugin | مضمّن، `enabledByDefault: true`  
العقد | `mediaUnderstandingProviders` (الصوت)  
متغير بيئة المصادقة | `SENSEAUDIO_API_KEY`  
النموذج الافتراضي | `senseaudio-asr-pro-1.5-260319`  
عنوان URL الافتراضي | `https://api.senseaudio.cn/v1`  
الموقع الإلكتروني | [senseaudio.cn](<https://senseaudio.cn>)  
الوثائق | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## بدء الاستخدام

* ### عيّن مفتاح API الخاص بك

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### فعّل مزوّد الصوت

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### أرسل ملاحظة صوتية

أرسل رسالة صوتية عبر أي قناة متصلة. يرفع OpenClaw الصوت إلى SenseAudio ويستخدم النص المنسوخ في مسار الرد.

## الخيارات

الخيار | المسار | الوصف  
---|---|---  
`model` | `tools.media.audio.models[].model` | معرّف نموذج ASR في SenseAudio  
`language` | `tools.media.audio.models[].language` | تلميح لغة اختياري  
`prompt` | `tools.media.audio.prompt` | موجّه نسخ اختياري  
`baseUrl` | `tools.media.audio.baseUrl` أو النموذج | تجاوز الأساس المتوافق مع OpenAI  
`headers` | `tools.media.audio.request.headers` | ترويسات طلب إضافية  
  
## ذو صلة

  * [فهم الوسائط (الصوت)](</ar/nodes/audio>)
  * [مزوّدو النماذج](</ar/concepts/model-providers>)


Was this useful?YesNo