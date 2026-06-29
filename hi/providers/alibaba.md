---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/hi/providers/alibaba
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw एक bundled `alibaba` Plugin भेजता है, जो Alibaba Model Studio (DashScope का अंतरराष्ट्रीय नाम) पर Wan मॉडल के लिए वीडियो-जनरेशन प्रदाता रजिस्टर करता है। Plugin डिफ़ॉल्ट रूप से सक्षम है; आपको केवल API key सेट करनी होती है।

प्रॉपर्टी | मान  
---|---  
प्रदाता id | `alibaba`  
Plugin | bundled, `enabledByDefault: true`  
Auth env vars | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (पहला मिलान जीतेगा)  
ऑनबोर्डिंग फ़्लैग | `--auth-choice alibaba-model-studio-api-key`  
डायरेक्ट CLI फ़्लैग | `--alibaba-model-studio-api-key <key>`  
डिफ़ॉल्ट मॉडल | `alibaba/wan2.6-t2v`  
डिफ़ॉल्ट बेस URL | `https://dashscope-intl.aliyuncs.com`  
  
## शुरू करना

* ### API key सेट करें

कुंजी को `alibaba` प्रदाता के साथ संग्रहीत करने के लिए ऑनबोर्डिंग का उपयोग करें:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

या install/onboarding के दौरान सीधे कुंजी पास करें:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

या Gateway शुरू करने से पहले स्वीकार किए गए env vars में से कोई भी निर्यात करें:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### डिफ़ॉल्ट वीडियो मॉडल सेट करें

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### सत्यापित करें कि प्रदाता कॉन्फ़िगर है

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

सूची में सभी पाँच bundled Wan मॉडल शामिल होने चाहिए। यदि `MODELSTUDIO_API_KEY` हल नहीं होता है, तो `openclaw models status --json` अनुपस्थित credential को `auth.unusableProfiles` के अंतर्गत रिपोर्ट करता है।

## अंतर्निहित Wan मॉडल

मॉडल ref | मोड  
---|---  
`alibaba/wan2.6-t2v` | टेक्स्ट-से-वीडियो (डिफ़ॉल्ट)  
`alibaba/wan2.6-i2v` | इमेज-से-वीडियो  
`alibaba/wan2.6-r2v` | रेफ़रेंस-से-वीडियो  
`alibaba/wan2.6-r2v-flash` | रेफ़रेंस-से-वीडियो (तेज़)  
`alibaba/wan2.7-r2v` | रेफ़रेंस-से-वीडियो  
  
## क्षमताएँ और सीमाएँ

bundled प्रदाता DashScope के Wan वीडियो API caps को mirror करता है। तीनों मोड समान प्रति-request वीडियो संख्या और अवधि cap साझा करते हैं; केवल इनपुट आकार अलग होता है।

मोड | अधिकतम आउटपुट वीडियो | अधिकतम इनपुट इमेज | अधिकतम इनपुट वीडियो | अधिकतम अवधि | समर्थित controls  
---|---|---|---|---|---  
टेक्स्ट-से-वीडियो | 1 | लागू नहीं | लागू नहीं | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
इमेज-से-वीडियो | 1 | 1 | लागू नहीं | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
रेफ़रेंस-से-वीडियो | 1 | लागू नहीं | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
जब कोई request `durationSeconds` छोड़ देता है, तो प्रदाता DashScope का स्वीकार्य डिफ़ॉल्ट **5 सेकंड** भेजता है। 10 s तक बढ़ाने के लिए [वीडियो जनरेशन टूल](</hi/tools/video-generation>) पर `durationSeconds` स्पष्ट रूप से सेट करें।

## उन्नत कॉन्फ़िगरेशन

DashScope base URL override करें

प्रदाता डिफ़ॉल्ट रूप से अंतरराष्ट्रीय DashScope endpoint का उपयोग करता है। China-region endpoint को target करने के लिए, सेट करें:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

प्रदाता AIGC task URLs बनाने से पहले trailing slashes हटा देता है।

Auth env प्राथमिकता

OpenClaw Alibaba API key को environment variables से इस क्रम में हल करता है, पहला non-empty मान लेते हुए:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


कॉन्फ़िगर की गई `auth.profiles` प्रविष्टियाँ (`openclaw models auth login` के माध्यम से सेट) env-var resolution को override करती हैं। profile rotation, cooldown, और override mechanics के लिए [models FAQ में Auth profiles](</hi/help/faq-models#what-is-an-auth-profile>) देखें।

Qwen Plugin से संबंध

दोनों bundled plugins DashScope से बात करते हैं और overlapping API keys स्वीकार करते हैं। उपयोग करें:

  * इस पेज पर दस्तावेज़ किए गए समर्पित Wan वीडियो प्रदाता को चलाने के लिए `alibaba/wan*.*` ids।
  * Qwen chat, embedding, और media understanding के लिए `qwen/*` ids ([Qwen](</hi/providers/qwen>) देखें)।


`MODELSTUDIO_API_KEY` एक बार सेट करने से दोनों plugins authenticate हो जाते हैं क्योंकि auth env var list जानबूझकर overlap करती है; आपको प्रत्येक Plugin को अलग से onboard करने की आवश्यकता नहीं है।

## संबंधित

[**वीडियो जनरेशन** साझा वीडियो टूल parameters और प्रदाता selection। ](</hi/tools/video-generation>) [**Qwen** उसी DashScope auth पर Qwen chat, embedding, और media-understanding setup। ](</hi/providers/qwen>) [**कॉन्फ़िगरेशन संदर्भ** Agent defaults और मॉडल कॉन्फ़िगरेशन। ](</hi/gateway/config-agents#agent-defaults>) [**Models FAQ** Auth profiles, models बदलना, और "no profile" errors हल करना। ](</hi/help/faq-models>)

Was this useful?YesNo

Open issue