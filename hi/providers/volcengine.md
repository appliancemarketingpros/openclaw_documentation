---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/hi/providers/volcengine
scraped_at: 2026-06-29
---

ModelsProviders

Volcengine प्रदाता Doubao मॉडलों और Volcano Engine पर होस्ट किए गए तृतीय-पक्ष मॉडलों तक पहुंच देता है, जिसमें सामान्य और कोडिंग वर्कलोड के लिए अलग-अलग एंडपॉइंट होते हैं। वही bundled plugin Volcengine Speech को TTS प्रदाता के रूप में भी रजिस्टर कर सकता है।

विवरण | मान  
---|---  
प्रदाता | `volcengine` (सामान्य + TTS) + `volcengine-plan` (कोडिंग)  
मॉडल auth | `VOLCANO_ENGINE_API_KEY`  
TTS auth | `VOLCENGINE_TTS_API_KEY` या `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | OpenAI-संगत मॉडल, BytePlus Seed Speech TTS  
  
## शुरू करना

* ### API key सेट करें

इंटरैक्टिव ऑनबोर्डिंग चलाएं:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

यह एक ही API key से सामान्य (`volcengine`) और कोडिंग (`volcengine-plan`) दोनों प्रदाताओं को रजिस्टर करता है।

* ### डिफ़ॉल्ट मॉडल सेट करें

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### पुष्टि करें कि मॉडल उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## प्रदाता और एंडपॉइंट

प्रदाता | एंडपॉइंट | उपयोग का मामला  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | सामान्य मॉडल  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | कोडिंग मॉडल  
  
## बिल्ट-इन कैटलॉग

### सामान्य (volcengine)

मॉडल ref | नाम | इनपुट | संदर्भ  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | टेक्स्ट, इमेज | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | टेक्स्ट, इमेज | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | टेक्स्ट, इमेज | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | टेक्स्ट, इमेज | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | टेक्स्ट, इमेज | 128,000  
  
### कोडिंग (volcengine-plan)

मॉडल ref | नाम | इनपुट | संदर्भ  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | टेक्स्ट | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | टेक्स्ट | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | टेक्स्ट | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | टेक्स्ट | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | टेक्स्ट | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | टेक्स्ट | 256,000  
  
## टेक्स्ट-टू-स्पीच

Volcengine TTS BytePlus Seed Speech HTTP API का उपयोग करता है और OpenAI-संगत Doubao मॉडल API key से अलग कॉन्फ़िगर किया जाता है। BytePlus console में, Seed Speech > Settings > API Keys खोलें और API key कॉपी करें, फिर सेट करें:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

फिर इसे `openclaw.json` में सक्षम करें:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

वॉइस-नोट लक्ष्यों के लिए, OpenClaw Volcengine से प्रदाता-नेटिव `ogg_opus` मांगता है। सामान्य ऑडियो अटैचमेंट के लिए, यह `mp3` मांगता है। प्रदाता aliases `bytedance` और `doubao` भी उसी speech प्रदाता पर resolve होते हैं।

डिफ़ॉल्ट resource id `seed-tts-1.0` है क्योंकि डिफ़ॉल्ट प्रोजेक्ट में नए बनाए गए Seed Speech API keys को BytePlus यही देता है। अगर आपके प्रोजेक्ट के पास TTS 2.0 entitlement है, तो `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0` सेट करें।

पुराने Speech Console applications के लिए legacy AppID/token auth समर्थित रहता है:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## उन्नत कॉन्फ़िगरेशन

ऑनबोर्डिंग के बाद डिफ़ॉल्ट मॉडल

`openclaw onboard --auth-choice volcengine-api-key` वर्तमान में `volcengine-plan/ark-code-latest` को डिफ़ॉल्ट मॉडल के रूप में सेट करता है, साथ ही सामान्य `volcengine` कैटलॉग भी रजिस्टर करता है।

मॉडल picker fallback व्यवहार

ऑनबोर्डिंग/कॉन्फ़िगर मॉडल चयन के दौरान, Volcengine auth choice `volcengine/*` और `volcengine-plan/*` दोनों rows को प्राथमिकता देता है। अगर वे मॉडल अभी तक loaded नहीं हैं, तो OpenClaw खाली provider-scoped picker दिखाने के बजाय unfiltered catalog पर fallback करता है।

daemon प्रक्रियाओं के लिए environment variables

अगर Gateway daemon (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि मॉडल और TTS env vars जैसे `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID`, और `VOLCENGINE_TTS_TOKEN` उस प्रक्रिया के लिए उपलब्ध हैं (उदाहरण के लिए, `~/.openclaw/.env` में या `env.shellEnv` के माध्यम से)।

## संबंधित

[**मॉडल चयन** प्रदाताओं, मॉडल refs, और failover behavior को चुनना। ](</hi/concepts/model-providers>) [**कॉन्फ़िगरेशन** agents, मॉडल, और प्रदाताओं के लिए पूरा config reference। ](</hi/gateway/configuration>) [**समस्या निवारण** सामान्य समस्याएं और debugging steps। ](</hi/help/troubleshooting>) [**FAQ** OpenClaw setup के बारे में अक्सर पूछे जाने वाले प्रश्न। ](</hi/help/faq>)

Was this useful?YesNo

Open issue