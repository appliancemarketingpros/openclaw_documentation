---
title: Inworld
source_url: https://docs.openclaw.ai/hi/providers/inworld
scraped_at: 2026-06-29
---

ModelsProviders

Inworld एक स्ट्रीमिंग टेक्स्ट-टू-स्पीच (TTS) प्रदाता है। OpenClaw में यह आउटबाउंड उत्तर ऑडियो (डिफ़ॉल्ट रूप से MP3, वॉइस नोट्स के लिए OGG_OPUS) और Voice Call जैसे टेलीफोनी चैनलों के लिए PCM ऑडियो सिंथेसाइज़ करता है।

OpenClaw Inworld के स्ट्रीमिंग TTS एंडपॉइंट पर पोस्ट करता है, लौटाए गए base64 ऑडियो चंक्स को एक ही बफ़र में जोड़ता है, और परिणाम को मानक उत्तर-ऑडियो पाइपलाइन को सौंपता है।

गुण | मान  
---|---  
प्रदाता id | `inworld`  
Plugin | आधिकारिक बाहरी पैकेज  
अनुबंध | `speechProviders` (केवल TTS)  
Auth env var | `INWORLD_API_KEY` (HTTP Basic, Base64 डैशबोर्ड क्रेडेंशियल)  
बेस URL | `https://api.inworld.ai`  
डिफ़ॉल्ट वॉइस | `Sarah`  
डिफ़ॉल्ट मॉडल | `inworld-tts-1.5-max`  
आउटपुट | MP3 (डिफ़ॉल्ट), OGG_OPUS (वॉइस नोट्स), PCM 22050 Hz (टेलीफोनी)  
वेबसाइट | [inworld.ai](<https://inworld.ai>)  
Docs | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway पुनः आरंभ करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/inworld-speechopenclaw gateway restart
[/code]

## शुरू करना

* ### अपनी API key सेट करें

अपने Inworld डैशबोर्ड (Workspace > API Keys) से क्रेडेंशियल कॉपी करें और उसे env var के रूप में सेट करें। मान HTTP Basic क्रेडेंशियल के रूप में जस का तस भेजा जाता है, इसलिए इसे फिर से Base64-encode न करें या इसे bearer token में परिवर्तित न करें।

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### messages.tts में Inworld चुनें

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          speakerVoiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### संदेश भेजें

किसी भी कनेक्टेड चैनल के माध्यम से उत्तर भेजें। OpenClaw Inworld के साथ ऑडियो सिंथेसाइज़ करता है और उसे MP3 के रूप में डिलीवर करता है (या जब चैनल वॉइस नोट की अपेक्षा करता है तब OGG_OPUS के रूप में)।

## कॉन्फ़िगरेशन विकल्प

विकल्प | पाथ | विवरण  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64 डैशबोर्ड क्रेडेंशियल। `INWORLD_API_KEY` पर फ़ॉलबैक करता है।  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Inworld API बेस URL ओवरराइड करें (डिफ़ॉल्ट `https://api.inworld.ai`)।  
`speakerVoiceId` | `messages.tts.providers.inworld.speakerVoiceId` | वॉइस आइडेंटिफ़ायर (डिफ़ॉल्ट `Sarah`)।  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS मॉडल id (डिफ़ॉल्ट `inworld-tts-1.5-max`)।  
`temperature` | `messages.tts.providers.inworld.temperature` | सैंपलिंग तापमान `0..2` (वैकल्पिक)।  
  
## नोट्स

प्रमाणीकरण

Inworld एकल Base64-encoded क्रेडेंशियल स्ट्रिंग के साथ HTTP Basic auth का उपयोग करता है। इसे Inworld डैशबोर्ड से जस का तस कॉपी करें। प्रदाता इसे बिना किसी और एन्कोडिंग के `Authorization: Basic <apiKey>` के रूप में भेजता है, इसलिए इसे स्वयं Base64-encode न करें और bearer-style token पास न करें। इसी कॉलआउट के लिए [TTS auth notes](</hi/tools/tts#inworld-primary>) देखें।

मॉडल

समर्थित मॉडल ids: `inworld-tts-1.5-max` (डिफ़ॉल्ट), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`।

ऑडियो आउटपुट

उत्तर डिफ़ॉल्ट रूप से MP3 का उपयोग करते हैं। जब चैनल लक्ष्य `voice-note` होता है, OpenClaw Inworld से `OGG_OPUS` मांगता है ताकि ऑडियो मूल वॉइस बबल की तरह चले। टेलीफोनी सिंथेसिस टेलीफोनी ब्रिज को फ़ीड करने के लिए 22050 Hz पर raw `PCM` का उपयोग करता है।

कस्टम एंडपॉइंट्स

API होस्ट को `messages.tts.providers.inworld.baseUrl` से ओवरराइड करें। अनुरोध भेजे जाने से पहले trailing slashes हटा दिए जाते हैं।

## संबंधित

[**टेक्स्ट-टू-स्पीच** TTS अवलोकन, प्रदाता, और `messages.tts` कॉन्फ़िगरेशन। ](</hi/tools/tts>) [**कॉन्फ़िगरेशन** `messages.tts` सेटिंग्स सहित पूरा कॉन्फ़िगरेशन संदर्भ। ](</hi/gateway/configuration>) [**प्रदाता** सभी समर्थित OpenClaw प्रदाता। ](</hi/providers>) [**समस्या निवारण** सामान्य समस्याएं और डिबगिंग चरण। ](</hi/help/troubleshooting>)

Was this useful?YesNo

Open issue