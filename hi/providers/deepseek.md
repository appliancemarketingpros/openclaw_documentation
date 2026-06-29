---
title: DeepSeek
source_url: https://docs.openclaw.ai/hi/providers/deepseek
scraped_at: 2026-06-29
---

ModelsProviders

[DeepSeek](<https://www.deepseek.com>) OpenAI-संगत API के साथ शक्तिशाली AI मॉडल प्रदान करता है।

गुण | मान  
---|---  
प्रदाता | `deepseek`  
प्रमाणीकरण | `DEEPSEEK_API_KEY`  
API | OpenAI-संगत  
बेस URL | `https://api.deepseek.com`  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway रीस्टार्ट करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/deepseek-provideropenclaw gateway restart
[/code]

## शुरुआत करना

* ### Get your API key

[platform.deepseek.com](<https://platform.deepseek.com/api_keys>) पर API कुंजी बनाएं।

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

यह आपकी API कुंजी मांगेगा और `deepseek/deepseek-v4-flash` को डिफ़ॉल्ट मॉडल के रूप में सेट करेगा।

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

चल रहे Gateway की आवश्यकता के बिना Plugin के स्थिर कैटलॉग का निरीक्षण करने के लिए, इसका उपयोग करें:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Non-interactive setup

स्क्रिप्टेड या हेडलेस इंस्टॉलेशन के लिए, सभी फ़्लैग सीधे पास करें:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## अंतर्निहित कैटलॉग

मॉडल रेफ़ | नाम | इनपुट | Context | अधिकतम आउटपुट | नोट्स  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | पाठ | 1,000,000 | 384,000 | डिफ़ॉल्ट मॉडल; V4 thinking-सक्षम सतह  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | पाठ | 1,000,000 | 384,000 | V4 thinking-सक्षम सतह  
`deepseek/deepseek-chat` | DeepSeek Chat | पाठ | 131,072 | 8,192 | DeepSeek V3.2 non-thinking सतह  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | पाठ | 131,072 | 65,536 | Reasoning-सक्षम V3.2 सतह  
  
## Thinking और tools

DeepSeek V4 thinking सेशन का replay contract अधिकांश OpenAI-संगत प्रदाताओं की तुलना में अधिक सख्त है: thinking-सक्षम टर्न द्वारा tools का उपयोग करने के बाद, DeepSeek अपेक्षा करता है कि उस टर्न से फिर से चलाए गए assistant संदेशों में फ़ॉलो-अप अनुरोधों पर `reasoning_content` शामिल हो। OpenClaw इसे DeepSeek Plugin के भीतर संभालता है, इसलिए सामान्य multi-turn tool उपयोग `deepseek/deepseek-v4-flash` और `deepseek/deepseek-v4-pro` के साथ काम करता है।

यदि आप किसी मौजूदा सेशन को किसी अन्य OpenAI-संगत प्रदाता से DeepSeek V4 मॉडल पर स्विच करते हैं, तो पुराने assistant tool-call टर्न में मूल DeepSeek `reasoning_content` नहीं हो सकता। OpenClaw DeepSeek V4 thinking अनुरोधों के लिए फिर से चलाए गए assistant संदेशों में उस अनुपलब्ध फ़ील्ड को भरता है, ताकि प्रदाता `/new` की आवश्यकता के बिना इतिहास स्वीकार कर सके।

जब OpenClaw में thinking अक्षम होती है (UI **कोई नहीं** चयन सहित), OpenClaw DeepSeek को `thinking: { type: "disabled" }` भेजता है और outgoing history से फिर से चलाए गए `reasoning_content` को हटा देता है। इससे disabled-thinking सेशन non-thinking DeepSeek पथ पर बने रहते हैं।

डिफ़ॉल्ट तेज़ पथ के लिए `deepseek/deepseek-v4-flash` का उपयोग करें। जब आपको अधिक शक्तिशाली V4 मॉडल चाहिए और आप अधिक लागत या latency स्वीकार कर सकते हैं, तो `deepseek/deepseek-v4-pro` का उपयोग करें।

## लाइव परीक्षण

प्रत्यक्ष लाइव मॉडल suite में आधुनिक मॉडल सेट में DeepSeek V4 शामिल है। केवल DeepSeek V4 direct-model checks चलाने के लिए:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

वह लाइव जांच सत्यापित करती है कि दोनों V4 मॉडल complete कर सकते हैं और thinking/tool फ़ॉलो-अप टर्न उस replay payload को संरक्षित रखते हैं जिसकी DeepSeek को आवश्यकता होती है।

## Config उदाहरण

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## संबंधित

[**Model selection** प्रदाता, मॉडल रेफ़ और failover व्यवहार चुनना। ](</hi/concepts/model-providers>) [**Configuration reference** agents, models और providers के लिए पूरा config संदर्भ। ](</hi/gateway/configuration-reference>)

Was this useful?YesNo

Open issue