---
title: रनवे
source_url: https://docs.openclaw.ai/hi/providers/runway
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw होस्टेड वीडियो जनरेशन के लिए एक बंडल किया हुआ `runway` प्रदाता शिप करता है। Plugin डिफ़ॉल्ट रूप से सक्षम होता है और `videoGenerationProviders` कॉन्ट्रैक्ट के विरुद्ध `runway` प्रदाता रजिस्टर करता है।

गुण | मान  
---|---  
प्रदाता आईडी | `runway`  
Plugin | बंडल किया हुआ, `enabledByDefault: true`  
प्रमाणीकरण env vars | `RUNWAYML_API_SECRET` (कैनोनिकल) या `RUNWAY_API_KEY`  
ऑनबोर्डिंग फ़्लैग | `--auth-choice runway-api-key`  
प्रत्यक्ष CLI फ़्लैग | `--runway-api-key <key>`  
API | Runway टास्क-आधारित वीडियो जनरेशन (`GET /v1/tasks/{id}` पोलिंग)  
डिफ़ॉल्ट मॉडल | `runway/gen4.5`  
  
## शुरू करना

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Set Runway as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Generate a video

एजेंट से वीडियो जनरेट करने के लिए कहें। Runway अपने आप उपयोग किया जाएगा।

## समर्थित मोड और मॉडल

प्रदाता तीन मोड में विभाजित सात Runway मॉडल उपलब्ध कराता है। वही मॉडल आईडी एक से अधिक मोड में काम कर सकती है (उदाहरण के लिए `gen4.5` टेक्स्ट-से-वीडियो और इमेज-से-वीडियो, दोनों के लिए काम करता है)।

मोड | मॉडल | संदर्भ इनपुट  
---|---|---  
टेक्स्ट-से-वीडियो | `gen4.5` (डिफ़ॉल्ट), `veo3.1`, `veo3.1_fast`, `veo3` | कोई नहीं  
इमेज-से-वीडियो | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 स्थानीय या रिमोट इमेज  
वीडियो-से-वीडियो | `gen4_aleph` | 1 स्थानीय या रिमोट वीडियो  
  
स्थानीय इमेज और वीडियो संदर्भ data URIs के माध्यम से समर्थित हैं।

आस्पेक्ट रेशियो | अनुमत मान  
---|---  
टेक्स्ट-से-वीडियो | `16:9`, `9:16`  
इमेज और वीडियो एडिट | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## कॉन्फ़िगरेशन

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## उन्नत कॉन्फ़िगरेशन

Environment variable aliases

OpenClaw `RUNWAYML_API_SECRET` (कैनोनिकल) और `RUNWAY_API_KEY`, दोनों को पहचानता है। इनमें से कोई भी वैरिएबल Runway प्रदाता को प्रमाणित करेगा।

Task polling

Runway टास्क-आधारित API का उपयोग करता है। जनरेशन अनुरोध सबमिट करने के बाद, OpenClaw वीडियो तैयार होने तक `GET /v1/tasks/{id}` पोल करता है। पोलिंग व्यवहार के लिए कोई अतिरिक्त कॉन्फ़िगरेशन आवश्यक नहीं है।

## संबंधित

[**Video generation** साझा टूल पैरामीटर, प्रदाता चयन, और async व्यवहार। ](</hi/tools/video-generation>) [**Configuration reference** वीडियो जनरेशन मॉडल सहित एजेंट डिफ़ॉल्ट सेटिंग्स। ](</hi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue