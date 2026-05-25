---
title: Azure Speech
source_url: https://docs.openclaw.ai/ar/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech هو مزوّد تحويل النص إلى كلام ضمن Azure AI Speech. وفي OpenClaw يقوم بتوليف الصوت الصادر للردود بصيغة MP3 افتراضيًا، وبصيغة Ogg/Opus أصلية للملاحظات الصوتية، وبصوت mulaw بتردد 8 kHz لقنوات الاتصالات الهاتفية مثل Voice Call.

يستخدم OpenClaw واجهة Azure Speech REST API مباشرةً مع SSML ويرسل تنسيق الإخراج المملوك للمزوّد عبر `X-Microsoft-OutputFormat`.

التفصيل | القيمة  
---|---  
الموقع الإلكتروني | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
الوثائق | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
المصادقة | `AZURE_SPEECH_KEY` بالإضافة إلى `AZURE_SPEECH_REGION`  
الصوت الافتراضي | `en-US-JennyNeural`  
إخراج الملف الافتراضي | `audio-24khz-48kbitrate-mono-mp3`  
ملف الملاحظة الصوتية الافتراضي | `ogg-24khz-16bit-mono-opus`  
  
## البدء

* ### أنشئ مورد Azure Speech

في بوابة Azure، أنشئ مورد Speech. انسخ **KEY 1** من Resource Management > Keys and Endpoint، وانسخ موقع المورد مثل `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### حدد Azure Speech في messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### أرسل رسالة

أرسل ردًا عبر أي قناة متصلة. سيقوم OpenClaw بتوليف الصوت باستخدام Azure Speech وتسليم MP3 للصوت القياسي، أو Ogg/Opus عندما تتوقع القناة ملاحظة صوتية.

## خيارات التكوين

الخيار | المسار | الوصف  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | مفتاح مورد Azure Speech. ويعود إلى `AZURE_SPEECH_KEY` أو `AZURE_SPEECH_API_KEY` أو `SPEECH_KEY`.  
`region` | `messages.tts.providers.azure-speech.region` | منطقة مورد Azure Speech. ويعود إلى `AZURE_SPEECH_REGION` أو `SPEECH_REGION`.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | تجاوز اختياري لنقطة نهاية/عنوان URL الأساسي لـ Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | تجاوز اختياري لعنوان URL الأساسي لـ Azure Speech.  
`voice` | `messages.tts.providers.azure-speech.voice` | قيمة ShortName للصوت في Azure (الافتراضي `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | رمز لغة SSML ‏(الافتراضي `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | تنسيق إخراج ملف الصوت (الافتراضي `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | تنسيق إخراج الملاحظة الصوتية (الافتراضي `ogg-24khz-16bit-mono-opus`).  
  
## ملاحظات

المصادقة

يستخدم Azure Speech مفتاح مورد Speech، وليس مفتاح Azure OpenAI. يتم إرسال المفتاح على هيئة `Ocp-Apim-Subscription-Key`؛ ويشتق OpenClaw العنوان `https://<region>.tts.speech.microsoft.com` من `region` ما لم توفر `endpoint` أو `baseUrl`.

أسماء الأصوات

استخدم قيمة `ShortName` الخاصة بالصوت في Azure Speech، مثل `en-US-JennyNeural`. ويمكن للمزوّد المضمن عرض الأصوات عبر مورد Speech نفسه ويصفّي الأصوات المعلّمة على أنها deprecated أو retired.

مخرجات الصوت

يقبل Azure تنسيقات إخراج مثل `audio-24khz-48kbitrate-mono-mp3`، و`ogg-24khz-16bit-mono-opus`، و`riff-24khz-16bit-mono-pcm`. ويطلب OpenClaw Ogg/Opus لأهداف `voice-note` حتى تتمكن القنوات من إرسال فقاعات صوتية أصلية من دون تحويل إضافي من MP3.

الاسم البديل

تُقبل `azure` كاسم بديل للمزوّد من أجل PRs الحالية وتكوينات المستخدمين، لكن يجب أن تستخدم التكوينات الجديدة `azure-speech` لتجنب الالتباس مع مزوّدي نماذج Azure OpenAI.

## ذو صلة

[**تحويل النص إلى كلام** نظرة عامة على TTS، والمزوّدين، وتكوين `messages.tts`. ](</ar/tools/tts>) [**التكوين** المرجع الكامل للتكوين بما في ذلك إعدادات `messages.tts`. ](</ar/gateway/configuration>) [**المزوّدون** جميع مزوّدي OpenClaw المضمنين. ](</ar/providers>) [**استكشاف الأخطاء وإصلاحها** المشكلات الشائعة وخطوات تصحيح الأخطاء. ](</ar/help/troubleshooting>)

Was this useful?YesNo