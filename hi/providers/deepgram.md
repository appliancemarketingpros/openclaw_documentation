---
title: Deepgram
source_url: https://docs.openclaw.ai/hi/providers/deepgram
scraped_at: 2026-06-29
---

ModelsProviders

Deepgram एक speech-to-text API है। OpenClaw में इसका उपयोग `tools.media.audio` के माध्यम से आने वाले ऑडियो/voice-note ट्रांसक्रिप्शन और `plugins.entries.voice-call.config.streaming` के माध्यम से Voice Call स्ट्रीमिंग STT के लिए किया जाता है।

बैच ट्रांसक्रिप्शन के लिए, OpenClaw पूरी ऑडियो फ़ाइल को Deepgram पर अपलोड करता है और ट्रांसक्रिप्ट को उत्तर पाइपलाइन (`{{Transcript}}` \+ `[Audio]` ब्लॉक) में इंजेक्ट करता है। Voice Call स्ट्रीमिंग के लिए, OpenClaw लाइव G.711 u-law फ़्रेम को Deepgram के WebSocket `listen` endpoint पर फ़ॉरवर्ड करता है और Deepgram द्वारा लौटाए जाने पर आंशिक या अंतिम ट्रांसक्रिप्ट उत्सर्जित करता है।

विवरण | मान  
---|---  
वेबसाइट | [deepgram.com](<https://deepgram.com>)  
दस्तावेज़ | [developers.deepgram.com](<https://developers.deepgram.com>)  
प्रमाणीकरण | `DEEPGRAM_API_KEY`  
डिफ़ॉल्ट मॉडल | `nova-3`  
  
## शुरू करना

* ### Set your API key

अपनी Deepgram API key को environment में जोड़ें:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Send a voice note

किसी भी जुड़े हुए channel के माध्यम से एक ऑडियो संदेश भेजें। OpenClaw इसे Deepgram के माध्यम से ट्रांसक्राइब करता है और ट्रांसक्रिप्ट को उत्तर पाइपलाइन में इंजेक्ट करता है।

## कॉन्फ़िगरेशन विकल्प

विकल्प | पथ | विवरण  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram model id (डिफ़ॉल्ट: `nova-3`)  
`language` | `tools.media.audio.models[].language` | भाषा संकेत (वैकल्पिक)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | भाषा पहचान सक्षम करें (वैकल्पिक)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | विराम चिह्न सक्षम करें (वैकल्पिक)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | smart formatting सक्षम करें (वैकल्पिक)  
  
### With language hint

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### With Deepgram options

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call स्ट्रीमिंग STT

बंडल किया गया `deepgram` Plugin, Voice Call Plugin के लिए एक realtime transcription provider भी पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पथ | डिफ़ॉल्ट  
---|---|---  
API key | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | `DEEPGRAM_API_KEY` पर fallback करता है  
मॉडल | `...deepgram.model` | `nova-3`  
भाषा | `...deepgram.language` | (सेट नहीं)  
एन्कोडिंग | `...deepgram.encoding` | `mulaw`  
सैंपल दर | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Interim results | `...deepgram.interimResults` | `true`  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## नोट्स

Authentication

प्रमाणीकरण मानक provider auth order का पालन करता है। `DEEPGRAM_API_KEY` सबसे सरल path है।

Proxy and custom endpoints

proxy का उपयोग करते समय `tools.media.audio.baseUrl` और `tools.media.audio.headers` के साथ endpoints या headers को override करें।

Output behavior

आउटपुट अन्य providers जैसे ही audio rules का पालन करता है (size caps, timeouts, transcript injection)।

## संबंधित

[**Media tools** ऑडियो, इमेज, और वीडियो प्रोसेसिंग पाइपलाइन का अवलोकन। ](</hi/tools/media-overview>) [**Configuration** media tool settings सहित पूरा config reference। ](</hi/gateway/configuration>) [**Troubleshooting** सामान्य समस्याएँ और debugging steps। ](</hi/help/troubleshooting>) [**FAQ** OpenClaw setup के बारे में अक्सर पूछे जाने वाले प्रश्न। ](</hi/help/faq>)

Was this useful?YesNo

Open issue