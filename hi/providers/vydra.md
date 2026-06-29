---
title: Vydra
source_url: https://docs.openclaw.ai/hi/providers/vydra
scraped_at: 2026-06-29
---

ModelsProviders

बंडल किया गया Vydra Plugin जोड़ता है:

  * `vydra/grok-imagine` के ज़रिए इमेज जनरेशन
  * `vydra/veo3` और `vydra/kling` के ज़रिए वीडियो जनरेशन
  * Vydra के ElevenLabs-समर्थित TTS रूट के ज़रिए स्पीच सिंथेसिस


OpenClaw तीनों क्षमताओं के लिए वही `VYDRA_API_KEY` उपयोग करता है।

गुण | मान  
---|---  
प्रदाता आईडी | `vydra`  
Plugin | बंडल किया गया, `enabledByDefault: true`  
ऑथ env var | `VYDRA_API_KEY`  
ऑनबोर्डिंग फ़्लैग | `--auth-choice vydra-api-key`  
डायरेक्ट CLI फ़्लैग | `--vydra-api-key <key>`  
कॉन्ट्रैक्ट | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
बेस URL | `https://www.vydra.ai/api/v1` (`www` होस्ट का उपयोग करें)  
  
## सेटअप

* ### इंटरैक्टिव ऑनबोर्डिंग चलाएँ

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

या env var सीधे सेट करें:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### डिफ़ॉल्ट क्षमता चुनें

नीचे दी गई क्षमताओं (इमेज, वीडियो, या स्पीच) में से एक या अधिक चुनें और मिलती-जुलती कॉन्फ़िगरेशन लागू करें।

## क्षमताएँ

इमेज जनरेशन

डिफ़ॉल्ट इमेज मॉडल:

  * `vydra/grok-imagine`


इसे डिफ़ॉल्ट इमेज प्रदाता के रूप में सेट करें:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

मौजूदा बंडल समर्थन केवल text-to-image है। Vydra के होस्ट किए गए edit routes दूरस्थ इमेज URL की अपेक्षा करते हैं, और OpenClaw अभी बंडल किए गए Plugin में Vydra-विशिष्ट upload bridge नहीं जोड़ता।

वीडियो जनरेशन

पंजीकृत वीडियो मॉडल:

  * text-to-video के लिए `vydra/veo3`
  * image-to-video के लिए `vydra/kling`


Vydra को डिफ़ॉल्ट वीडियो प्रदाता के रूप में सेट करें:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

नोट्स:

  * `vydra/veo3` केवल text-to-video के रूप में बंडल किया गया है।
  * `vydra/kling` को फ़िलहाल दूरस्थ इमेज URL संदर्भ की आवश्यकता होती है। स्थानीय फ़ाइल अपलोड शुरुआत में ही अस्वीकार कर दिए जाते हैं।
  * Vydra का मौजूदा `kling` HTTP रूट इस बारे में असंगत रहा है कि उसे `image_url` चाहिए या `video_url`; बंडल किया गया प्रदाता उसी दूरस्थ इमेज URL को दोनों फ़ील्ड में मैप करता है।
  * बंडल किया गया Plugin संयमित रहता है और aspect ratio, resolution, watermark, या generated audio जैसे undocumented style knobs आगे नहीं भेजता।

वीडियो लाइव टेस्ट

प्रदाता-विशिष्ट लाइव कवरेज:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

बंडल की गई Vydra लाइव फ़ाइल अब कवर करती है:

  * `vydra/veo3` text-to-video
  * दूरस्थ इमेज URL का उपयोग करके `vydra/kling` image-to-video


ज़रूरत होने पर दूरस्थ इमेज fixture को override करें:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

स्पीच सिंथेसिस

Vydra को स्पीच प्रदाता के रूप में सेट करें:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          speakerVoiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

डिफ़ॉल्ट:

  * मॉडल: `elevenlabs/tts`
  * वॉइस आईडी: `21m00Tcm4TlvDq8ikWAM`


बंडल किया गया Plugin फ़िलहाल एक known-good डिफ़ॉल्ट वॉइस उजागर करता है और MP3 ऑडियो फ़ाइलें लौटाता है।

## संबंधित

[**प्रदाता डायरेक्टरी** सभी उपलब्ध प्रदाताओं को ब्राउज़ करें। ](</hi/providers>) [**इमेज जनरेशन** साझा इमेज टूल पैरामीटर और प्रदाता चयन। ](</hi/tools/image-generation>) [**वीडियो जनरेशन** साझा वीडियो टूल पैरामीटर और प्रदाता चयन। ](</hi/tools/video-generation>) [**कॉन्फ़िगरेशन संदर्भ** एजेंट डिफ़ॉल्ट और मॉडल कॉन्फ़िगरेशन। ](</hi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue