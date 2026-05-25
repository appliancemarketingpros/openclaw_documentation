---
title: Deepgram
source_url: https://docs.openclaw.ai/ar/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram هي واجهة API لتحويل الكلام إلى نص. وفي OpenClaw تُستخدم لنسخ الصوت/الملاحظات الصوتية الواردة عبر `tools.media.audio`، وللنسخ المتدفق في Voice Call عبر `plugins.entries.voice-call.config.streaming`.

في النسخ الدفعي، يرفع OpenClaw ملف الصوت كاملًا إلى Deepgram ويحقن النص المنسوخ في مسار الرد (`{{Transcript}}` \+ كتلة `[Audio]`). أما في النسخ المتدفق لـ Voice Call، فيمرّر OpenClaw إطارات G.711 u-law الحية عبر نقطة نهاية WebSocket ‏`listen` الخاصة بـ Deepgram ويصدر نصوصًا جزئية أو نهائية عندما تعيدها Deepgram.

التفصيل | القيمة  
---|---  
الموقع | [deepgram.com](<https://deepgram.com>)  
المستندات | [developers.deepgram.com](<https://developers.deepgram.com>)  
المصادقة | `DEEPGRAM_API_KEY`  
النموذج الافتراضي | `nova-3`  
  
## البدء

* ### عيّن مفتاح API الخاص بك

أضف مفتاح Deepgram API إلى البيئة:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### فعّل موفّر الصوت

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### أرسل ملاحظة صوتية

أرسل رسالة صوتية عبر أي قناة متصلة. سيقوم OpenClaw بنسخها عبر Deepgram وحقن النص في مسار الرد.

## خيارات التهيئة

الخيار | المسار | الوصف  
---|---|---  
`model` | `tools.media.audio.models[].model` | معرّف نموذج Deepgram (الافتراضي: `nova-3`)  
`language` | `tools.media.audio.models[].language` | تلميح اللغة (اختياري)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | تمكين اكتشاف اللغة (اختياري)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | تمكين علامات الترقيم (اختياري)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | تمكين التنسيق الذكي (اختياري)  
  
### مع تلميح اللغة

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### مع خيارات Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## النسخ المتدفق في Voice Call

تسجّل Plugin المجمّعة `deepgram` أيضًا موفّر نسخ فوري لـ Plugin الخاصة بـ Voice Call.

الإعداد | مسار التهيئة | الافتراضي  
---|---|---  
مفتاح API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | يعود إلى `DEEPGRAM_API_KEY`  
النموذج | `...deepgram.model` | `nova-3`  
اللغة | `...deepgram.language` | (غير معيّنة)  
الترميز | `...deepgram.encoding` | `mulaw`  
معدل العينة | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
النتائج المرحلية | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## ملاحظات

المصادقة

تتبع المصادقة ترتيب auth القياسي الخاص بالموفّر. ويُعد `DEEPGRAM_API_KEY` أبسط مسار.

Proxy ونقاط النهاية المخصصة

تجاوز نقاط النهاية أو الرؤوس باستخدام `tools.media.audio.baseUrl` و `tools.media.audio.headers` عند استخدام proxy.

سلوك الإخراج

يتبع الإخراج قواعد الصوت نفسها كما في الموفّرين الآخرين (حدود الحجم، والمهلات، وحقن النص المنسوخ).

## ذو صلة

[**أدوات الوسائط** نظرة عامة على خط معالجة الصوت والصور والفيديو. ](</ar/tools/media-overview>) [**التهيئة** مرجع التهيئة الكامل بما في ذلك إعدادات أداة الوسائط. ](</ar/gateway/configuration>) [**استكشاف الأخطاء وإصلاحها** المشكلات الشائعة وخطوات تصحيح الأخطاء. ](</ar/help/troubleshooting>) [**الأسئلة الشائعة** الأسئلة المتكررة حول إعداد OpenClaw. ](</ar/help/faq>)

Was this useful?YesNo