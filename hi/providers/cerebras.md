---
title: Cerebras
source_url: https://docs.openclaw.ai/hi/providers/cerebras
scraped_at: 2026-06-29
---

ModelsProviders

[Cerebras](<https://www.cerebras.ai>) कस्टम इन्फ़रेंस हार्डवेयर पर उच्च-गति OpenAI-संगत इन्फ़रेंस प्रदान करता है। Cerebras प्रदाता Plugin में चार मॉडलों की स्थिर कैटलॉग शामिल है।

गुण | मान  
---|---  
प्रदाता id | `cerebras`  
Plugin | आधिकारिक बाहरी पैकेज  
Auth env var | `CEREBRAS_API_KEY`  
ऑनबोर्डिंग फ़्लैग | `--auth-choice cerebras-api-key`  
प्रत्यक्ष CLI फ़्लैग | `--cerebras-api-key <key>`  
API | OpenAI-संगत (`openai-completions`)  
बेस URL | `https://api.cerebras.ai/v1`  
डिफ़ॉल्ट मॉडल | `cerebras/zai-glm-4.7`  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway रीस्टार्ट करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/cerebras-provideropenclaw gateway restart
[/code]

## शुरुआत करना

* ### API कुंजी प्राप्त करें

[Cerebras Cloud Console](<https://cloud.cerebras.ai>) में API कुंजी बनाएं।

* ### ऑनबोर्डिंग चलाएं

ऑनबोर्डिंगCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

प्रत्यक्ष फ़्लैगCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

केवल EnvCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### सत्यापित करें कि मॉडल उपलब्ध हैं

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

सूची में सभी चार स्थिर मॉडल शामिल होने चाहिए। यदि `CEREBRAS_API_KEY` हल नहीं होता है, तो `openclaw models status --json` अनुपस्थित क्रेडेंशियल को `auth.unusableProfiles` के अंतर्गत रिपोर्ट करता है।

## नॉन-इंटरैक्टिव सेटअप

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## बिल्ट-इन कैटलॉग

OpenClaw एक स्थिर Cerebras कैटलॉग शिप करता है जो सार्वजनिक OpenAI-संगत एंडपॉइंट को मिरर करती है। सभी चार मॉडल 128k संदर्भ और 8,192 अधिकतम-आउटपुट टोकन साझा करते हैं।

मॉडल ref | नाम | रीजनिंग | नोट्स  
---|---|---|---  
`cerebras/zai-glm-4.7` | Z.ai GLM 4.7 | हाँ | डिफ़ॉल्ट मॉडल; प्रीव्यू रीजनिंग मॉडल  
`cerebras/gpt-oss-120b` | GPT OSS 120B | हाँ | प्रोडक्शन रीजनिंग मॉडल  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | नहीं | प्रीव्यू नॉन-रीजनिंग मॉडल  
`cerebras/llama3.1-8b` | Llama 3.1 8B | नहीं | प्रोडक्शन गति-केंद्रित मॉडल  
  
## मैनुअल कॉन्फ़िगरेशन

Plugin का सामान्यतः अर्थ है कि आपको केवल API कुंजी चाहिए। जब आप मॉडल मेटाडेटा ओवरराइड करना चाहते हैं या स्थिर कैटलॉग के विरुद्ध `mode: "merge"` में चलाना चाहते हैं, तो स्पष्ट `models.providers.cerebras` कॉन्फ़िगरेशन का उपयोग करें:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## संबंधित

[**मॉडल प्रदाता** प्रदाताओं, मॉडल refs, और failover व्यवहार का चयन। ](</hi/concepts/model-providers>) [**सोचने के मोड** दो रीजनिंग-सक्षम Cerebras मॉडलों के लिए रीजनिंग प्रयास स्तर। ](</hi/tools/thinking>) [**कॉन्फ़िगरेशन संदर्भ** Agent डिफ़ॉल्ट और मॉडल कॉन्फ़िगरेशन। ](</hi/gateway/config-agents#agent-defaults>) [**मॉडल FAQ** Auth profiles, मॉडल बदलना, और "no profile" त्रुटियों को हल करना। ](</hi/help/faq-models>)

Was this useful?YesNo

Open issue