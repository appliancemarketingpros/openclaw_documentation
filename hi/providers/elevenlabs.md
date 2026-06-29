---
title: ElevenLabs
source_url: https://docs.openclaw.ai/hi/providers/elevenlabs
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw टेक्स्ट-से-स्पीच के लिए ElevenLabs, Scribe v2 के साथ बैच स्पीच-से-टेक्स्ट, और Scribe v2 Realtime के साथ स्ट्रीमिंग STT का उपयोग करता है।

क्षमता | OpenClaw सतह | डिफ़ॉल्ट  
---|---|---  
टेक्स्ट-से-स्पीच | `messages.tts` / `talk` | `eleven_multilingual_v2`  
बैच स्पीच-से-टेक्स्ट | `tools.media.audio` | `scribe_v2`  
स्ट्रीमिंग स्पीच-से-टेक्स्ट | Voice Call स्ट्रीमिंग या Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## प्रमाणीकरण

पर्यावरण में `ELEVENLABS_API_KEY` सेट करें। मौजूदा ElevenLabs टूलिंग के साथ संगतता के लिए `XI_API_KEY` भी स्वीकार किया जाता है।

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## टेक्स्ट-से-स्पीच

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          speakerVoiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

ElevenLabs v3 TTS का उपयोग करने के लिए `modelId` को `eleven_v3` पर सेट करें। OpenClaw मौजूदा इंस्टॉल के लिए `eleven_multilingual_v2` को डिफ़ॉल्ट के रूप में रखता है।

जब ElevenLabs चयनित `voice.tts`/`messages.tts` प्रदाता होता है, तो Discord वॉयस चैनल ElevenLabs के स्ट्रीमिंग TTS एंडपॉइंट का उपयोग करते हैं। प्लेबैक OpenClaw के पूरी ऑडियो फ़ाइल को पहले डाउनलोड करके लिखने की प्रतीक्षा करने के बजाय लौटाई गई ऑडियो स्ट्रीम से शुरू होता है। `latencyTier` उन मॉडलों के लिए ElevenLabs के `optimize_streaming_latency` क्वेरी पैरामीटर से मैप होता है जो इसे स्वीकार करते हैं; OpenClaw `eleven_v3` के लिए वह पैरामीटर छोड़ देता है, क्योंकि वह इसे अस्वीकार करता है।

## स्पीच-से-टेक्स्ट

इनबाउंड ऑडियो अटैचमेंट और छोटे रिकॉर्ड किए गए वॉयस सेगमेंट के लिए Scribe v2 का उपयोग करें:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw `model_id: "scribe_v2"` के साथ multipart ऑडियो ElevenLabs `/v1/speech-to-text` पर भेजता है। मौजूद होने पर भाषा संकेत `language_code` से मैप होते हैं।

## स्ट्रीमिंग STT

बंडल किया गया `elevenlabs` Plugin, Voice Call और Google Meet एजेंट-मोड स्ट्रीमिंग ट्रांसक्रिप्शन के लिए Scribe v2 Realtime पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पाथ | डिफ़ॉल्ट  
---|---|---  
API कुंजी | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | `ELEVENLABS_API_KEY` / `XI_API_KEY` पर वापस जाता है  
मॉडल | `...elevenlabs.modelId` | `scribe_v2_realtime`  
ऑडियो फ़ॉर्मैट | `...elevenlabs.audioFormat` | `ulaw_8000`  
सैंपल दर | `...elevenlabs.sampleRate` | `8000`  
कमिट रणनीति | `...elevenlabs.commitStrategy` | `vad`  
भाषा | `...elevenlabs.languageCode` | (सेट नहीं)  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

Google Meet एजेंट मोड के लिए, `plugins.entries.google-meet.config.realtime.transcriptionProvider` को `"elevenlabs"` पर सेट करें और उसी प्रदाता ब्लॉक को `plugins.entries.google-meet.config.realtime.providers.elevenlabs` के अंतर्गत कॉन्फ़िगर करें।

## संबंधित

  * [टेक्स्ट-से-स्पीच](</hi/tools/tts>)
  * [Google Meet](</hi/plugins/google-meet>)
  * [मॉडल चयन](</hi/concepts/model-providers>)


Was this useful?YesNo

Open issue