---
title: SenseAudio
source_url: https://docs.openclaw.ai/hi/providers/senseaudio
scraped_at: 2026-06-29
---

ModelsProviders

SenseAudio OpenClaw की साझा `tools.media.audio` पाइपलाइन के माध्यम से आने वाले ऑडियो और वॉइस-नोट अटैचमेंट को ट्रांसक्राइब कर सकता है। OpenClaw मल्टीपार्ट ऑडियो को OpenAI-संगत ट्रांसक्रिप्शन एंडपॉइंट पर पोस्ट करता है और लौटाए गए टेक्स्ट को `{{Transcript}}` के साथ एक `[Audio]` ब्लॉक के रूप में इंजेक्ट करता है।

प्रॉपर्टी | मान  
---|---  
प्रोवाइडर आईडी | `senseaudio`  
Plugin | बंडल किया गया, `enabledByDefault: true`  
कॉन्ट्रैक्ट | `mediaUnderstandingProviders` (ऑडियो)  
Auth env var | `SENSEAUDIO_API_KEY`  
डिफॉल्ट मॉडल | `senseaudio-asr-pro-1.5-260319`  
डिफॉल्ट URL | `https://api.senseaudio.cn/v1`  
वेबसाइट | [senseaudio.cn](<https://senseaudio.cn>)  
दस्तावेज़ | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## शुरू करना

* ### Set your API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Send a voice note

किसी भी कनेक्टेड चैनल के माध्यम से ऑडियो संदेश भेजें। OpenClaw ऑडियो को SenseAudio पर अपलोड करता है और जवाब पाइपलाइन में ट्रांसक्रिप्ट का उपयोग करता है।

## विकल्प

विकल्प | पाथ | विवरण  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR मॉडल आईडी  
`language` | `tools.media.audio.models[].language` | वैकल्पिक भाषा संकेत  
`prompt` | `tools.media.audio.prompt` | वैकल्पिक ट्रांसक्रिप्शन प्रॉम्प्ट  
`baseUrl` | `tools.media.audio.baseUrl` या मॉडल | OpenAI-संगत बेस को ओवरराइड करें  
`headers` | `tools.media.audio.request.headers` | अतिरिक्त रिक्वेस्ट हेडर  
  
## संबंधित

  * [मीडिया अंडरस्टैंडिंग (ऑडियो)](</hi/nodes/audio>)
  * [मॉडल प्रोवाइडर](</hi/concepts/model-providers>)


Was this useful?YesNo

Open issue