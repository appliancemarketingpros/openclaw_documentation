---
title: Mistral
source_url: https://docs.openclaw.ai/hi/providers/mistral
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw में एक बंडल किया गया Mistral Plugin शामिल है, जो चार अनुबंध पंजीकृत करता है: चैट पूर्णताएं, मीडिया समझ (Voxtral बैच ट्रांसक्रिप्शन), Voice Call के लिए रीयलटाइम STT (Voxtral Realtime), और मेमोरी एम्बेडिंग्स (`mistral-embed`).

गुण | मान  
---|---  
प्रदाता id | `mistral`  
Plugin | बंडल किया गया, `enabledByDefault: true`  
Auth env var | `MISTRAL_API_KEY`  
ऑनबोर्डिंग फ्लैग | `--auth-choice mistral-api-key`  
सीधा CLI फ्लैग | `--mistral-api-key <key>`  
API | OpenAI-संगत (`openai-completions`)  
बेस URL | `https://api.mistral.ai/v1`  
डिफ़ॉल्ट मॉडल | `mistral/mistral-large-latest`  
एम्बेडिंग मॉडल | `mistral-embed`  
Voxtral बैच | `voxtral-mini-latest` (ऑडियो ट्रांसक्रिप्शन)  
Voxtral रीयलटाइम | `voxtral-mini-transcribe-realtime-2602`  
  
## शुरू करना

* ### अपनी API कुंजी प्राप्त करें

[Mistral Console](<https://console.mistral.ai/>) में एक API कुंजी बनाएं।

* ### ऑनबोर्डिंग चलाएं

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

या कुंजी सीधे पास करें:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### डिफ़ॉल्ट मॉडल सेट करें

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### सत्यापित करें कि मॉडल उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## अंतर्निहित LLM कैटलॉग

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) बंडल किए गए कैटलॉग में वर्तमान मिश्रित Medium मॉडल है: 128B डेंस वेट्स, टेक्स्ट और इमेज इनपुट, 256K कॉन्टेक्स्ट, फ़ंक्शन कॉलिंग, संरचित आउटपुट, कोडिंग, और Chat Completions API के ज़रिए समायोज्य रीज़निंग। जब आप डिफ़ॉल्ट `mistral/mistral-large-latest` के बजाय Mistral का नया एकीकृत एजेंटिक/कोडिंग मॉडल चाहते हैं, तो `mistral/mistral-medium-3-5` का उपयोग करें।

OpenClaw वर्तमान में यह बंडल किया गया Mistral कैटलॉग शिप करता है:

मॉडल ref | इनपुट | कॉन्टेक्स्ट | अधिकतम आउटपुट | नोट्स  
---|---|---|---|---  
`mistral/mistral-large-latest` | टेक्स्ट, इमेज | 262,144 | 16,384 | डिफ़ॉल्ट मॉडल  
`mistral/mistral-medium-2508` | टेक्स्ट, इमेज | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | टेक्स्ट, इमेज | 262,144 | 8,192 | Mistral Medium 3.5; समायोज्य रीज़निंग  
`mistral/mistral-small-latest` | टेक्स्ट, इमेज | 128,000 | 16,384 | Mistral Small 4; API `reasoning_effort` के ज़रिए समायोज्य रीज़निंग  
`mistral/pixtral-large-latest` | टेक्स्ट, इमेज | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | टेक्स्ट | 256,000 | 4,096 | कोडिंग  
`mistral/devstral-medium-latest` | टेक्स्ट | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | टेक्स्ट | 128,000 | 40,000 | रीज़निंग-सक्षम  
  
ऑनबोर्डिंग के बाद, Gateway शुरू किए बिना Medium 3.5 का स्मोक-टेस्ट करें:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

कॉन्फ़िग बदलने से पहले बंडल किए गए कैटलॉग की पंक्ति ब्राउज़ करने के लिए:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## ऑडियो ट्रांसक्रिप्शन (Voxtral)

मीडिया समझ पाइपलाइन के ज़रिए बैच ऑडियो ट्रांसक्रिप्शन के लिए Voxtral का उपयोग करें।

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Voice Call स्ट्रीमिंग STT

बंडल किया गया `mistral` Plugin Voxtral Realtime को Voice Call स्ट्रीमिंग STT प्रदाता के रूप में पंजीकृत करता है।

सेटिंग | कॉन्फ़िग पथ | डिफ़ॉल्ट  
---|---|---  
API कुंजी | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | `MISTRAL_API_KEY` पर फ़ॉलबैक करता है  
मॉडल | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
एन्कोडिंग | `...mistral.encoding` | `pcm_mulaw`  
सैंपल रेट | `...mistral.sampleRate` | `8000`  
लक्ष्य विलंब | `...mistral.targetStreamingDelayMs` | `800`  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## उन्नत कॉन्फ़िगरेशन

समायोज्य रीज़निंग

`mistral/mistral-small-latest` (Mistral Small 4) और `mistral/mistral-medium-3-5`, Chat Completions API पर `reasoning_effort` के ज़रिए [समायोज्य रीज़निंग](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) का समर्थन करते हैं (`none` आउटपुट में अतिरिक्त सोच को न्यूनतम करता है; `high` अंतिम उत्तर से पहले पूर्ण सोच ट्रेस दिखाता है)। Mistral Medium 3.5 एजेंटिक और कोड उपयोग मामलों के लिए `reasoning_effort="high"` की अनुशंसा करता है।

OpenClaw सेशन **सोच** स्तर को Mistral के API पर मैप करता है:

OpenClaw सोच स्तर | Mistral `reasoning_effort`  
---|---  
**बंद** / **न्यूनतम** | `none`  
**कम** / **मध्यम** / **उच्च** / **xhigh** / **अनुकूली** / **अधिकतम** | `high`  
  
Medium 3.5 रीज़निंग के लिए मॉडल-स्कोप्ड कॉन्फ़िग का उदाहरण:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

मेमोरी एम्बेडिंग्स

Mistral `/v1/embeddings` के ज़रिए मेमोरी एम्बेडिंग्स सर्व कर सकता है (डिफ़ॉल्ट मॉडल: `mistral-embed`)।

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth और बेस URL

  * Mistral auth `MISTRAL_API_KEY` (Bearer header) का उपयोग करता है।
  * प्रदाता बेस URL डिफ़ॉल्ट रूप से `https://api.mistral.ai/v1` होता है और मानक OpenAI-संगत चैट-कम्प्लीशन्स अनुरोध आकार स्वीकार करता है।
  * ऑनबोर्डिंग डिफ़ॉल्ट मॉडल `mistral/mistral-large-latest` है।
  * `models.providers.mistral.baseUrl` के तहत बेस URL को केवल तभी ओवरराइड करें जब Mistral स्पष्ट रूप से आपकी ज़रूरत का क्षेत्रीय endpoint प्रकाशित करे।


## संबंधित

[**मॉडल चयन** प्रदाताओं, मॉडल refs, और failover व्यवहार का चयन। ](</hi/concepts/model-providers>) [**मीडिया समझ** ऑडियो ट्रांसक्रिप्शन सेटअप और प्रदाता चयन। ](</hi/nodes/media-understanding>)

Was this useful?YesNo

Open issue