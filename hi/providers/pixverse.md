---
title: PixVerse
source_url: https://docs.openclaw.ai/hi/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw होस्टेड PixVerse वीडियो जनरेशन के लिए आधिकारिक बाहरी Plugin के रूप में `pixverse` प्रदान करता है। Plugin `videoGenerationProviders` कॉन्ट्रैक्ट के विरुद्ध `pixverse` प्रदाता रजिस्टर करता है।

गुण | मान  
---|---  
प्रदाता id | `pixverse`  
Plugin पैकेज | `@openclaw/pixverse-provider`  
Auth env var | `PIXVERSE_API_KEY`  
ऑनबोर्डिंग फ्लैग | `--auth-choice pixverse-api-key`  
डायरेक्ट CLI फ्लैग | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (`video_id` सबमिशन और परिणाम पोलिंग)  
डिफॉल्ट मॉडल | `pixverse/v6`  
डिफॉल्ट API क्षेत्र | अंतरराष्ट्रीय  
  
## शुरू करना

* ### Plugin इंस्टॉल करें

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### API key सेट करें

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

विजार्ड `region` और `baseUrl` को प्रदाता कॉन्फिग में लिखने से पहले पूछता है कि अंतरराष्ट्रीय एंडपॉइंट (`https://app-api.pixverse.ai/openapi/v2`) या CN एंडपॉइंट (`https://app-api.pixverseai.cn/openapi/v2`) का उपयोग करना है।

* ### PixVerse को डिफॉल्ट वीडियो प्रदाता के रूप में सेट करें

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### वीडियो जनरेट करें

एजेंट से वीडियो जनरेट करने के लिए कहें। PixVerse अपने आप उपयोग किया जाएगा।

## समर्थित मोड और मॉडल

प्रदाता OpenClaw के साझा वीडियो टूल के माध्यम से PixVerse जनरेशन मॉडल उपलब्ध कराता है।

मोड | मॉडल | संदर्भ इनपुट  
---|---|---  
टेक्स्ट-से-वीडियो | `v6` (डिफॉल्ट), `c1` | कोई नहीं  
इमेज-से-वीडियो | `v6` (डिफॉल्ट), `c1` | 1 स्थानीय या रिमोट इमेज  
  
इमेज-से-वीडियो अनुरोध से पहले स्थानीय इमेज संदर्भ PixVerse पर अपलोड किए जाते हैं। रिमोट इमेज URL को PixVerse इमेज अपलोड एंडपॉइंट से `image_url` के रूप में पास किया जाता है।

विकल्प | समर्थित मान  
---|---  
अवधि | 1-15 सेकंड  
रिजॉल्यूशन | `360P`, `540P`, `720P`, `1080P`  
आस्पेक्ट रेशियो | टेक्स्ट-से-वीडियो के लिए `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9`  
जनरेटेड ऑडियो | `audio: true`  
  
## प्रदाता विकल्प

वीडियो प्रदाता ये वैकल्पिक प्रदाता-विशिष्ट कुंजियां स्वीकार करता है:

विकल्प | प्रकार | प्रभाव  
---|---|---  
`seed` | number | समर्थित होने पर नियतात्मक seed  
`negativePrompt` / `negative_prompt` | string | Negative prompt  
`quality` | string | PixVerse गुणवत्ता, जैसे `720p`  
`motionMode` / `motion_mode` | string | इमेज-से-वीडियो मोशन मोड  
`cameraMovement` / `camera_movement` | string | PixVerse कैमरा मूवमेंट प्रीसेट  
`templateId` / `template_id` | number | सक्रिय PixVerse template id  
  
## कॉन्फिगरेशन

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## उन्नत कॉन्फिगरेशन

API क्षेत्र

OpenClaw डिफॉल्ट रूप से अंतरराष्ट्रीय PixVerse API का उपयोग करता है। जब आपकी key किसी विशिष्ट PixVerse प्लेटफॉर्म क्षेत्र से संबंधित हो, तो `models.providers.pixverse.region` मैन्युअल रूप से सेट करें, या सेटअप विजार्ड में एक चुनने के लिए `openclaw onboard --auth-choice pixverse-api-key` का उपयोग करें:

क्षेत्र मान | PixVerse API बेस URL  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

कस्टम बेस URL

भरोसेमंद संगत प्रॉक्सी के माध्यम से रूट करते समय ही `models.providers.pixverse.baseUrl` सेट करें। `baseUrl` को `region` पर प्राथमिकता मिलती है।

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

कार्य पोलिंग

PixVerse जनरेशन अनुरोध से एक `video_id` लौटाता है। OpenClaw `/openapi/v2/video/result/{video_id}` को तब तक poll करता है जब तक कार्य सफल नहीं हो जाता, विफल नहीं हो जाता, या समय समाप्त नहीं हो जाता।

## संबंधित

[**वीडियो जनरेशन** साझा टूल पैरामीटर, प्रदाता चयन, और async व्यवहार। ](</hi/tools/video-generation>) [**कॉन्फिगरेशन संदर्भ** वीडियो जनरेशन मॉडल सहित एजेंट डिफॉल्ट सेटिंग्स। ](</hi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue