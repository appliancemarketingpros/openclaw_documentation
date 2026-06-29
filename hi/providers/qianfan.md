---
title: Qianfan
source_url: https://docs.openclaw.ai/hi/providers/qianfan
scraped_at: 2026-06-29
---

ModelsProviders

Qianfan Baidu का MaaS प्लेटफ़ॉर्म है, जो एक **एकीकृत API** प्रदान करता है जो अनुरोधों को एक ही endpoint और API key के पीछे कई मॉडलों तक रूट करता है। यह OpenAI-संगत है, इसलिए अधिकांश OpenAI SDKs केवल base URL बदलकर काम करते हैं।

गुण | मान  
---|---  
प्रदाता | `qianfan`  
प्रमाणीकरण | `QIANFAN_API_KEY`  
API | OpenAI-संगत  
Base URL | `https://qianfan.baidubce.com/v2`  
  
## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway रीस्टार्ट करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/qianfan-provideropenclaw gateway restart
[/code]

## शुरुआत करना

* ### Baidu Cloud खाता बनाएं

[Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) पर साइन अप या लॉग इन करें और सुनिश्चित करें कि आपके लिए Qianfan API access सक्षम है।

* ### API key जनरेट करें

एक नया application बनाएं या मौजूदा चुनें, फिर API key जनरेट करें। key का format `bce-v3/ALTAK-...` है।

* ### Onboarding चलाएं

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### सत्यापित करें कि मॉडल उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## अंतर्निहित catalog

Model ref | Input | Context | अधिकतम output | Reasoning | नोट्स  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | text | 98,304 | 32,768 | हां | डिफ़ॉल्ट मॉडल  
`qianfan/ernie-5.0-thinking-preview` | text, image | 119,000 | 64,000 | हां | Multimodal  
  
## Config उदाहरण

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport और संगतता

Qianfan OpenAI-संगत transport path के माध्यम से चलता है, native OpenAI request shaping के माध्यम से नहीं। इसका मतलब है कि standard OpenAI SDK सुविधाएं काम करती हैं, लेकिन provider-specific parameters forward नहीं किए जा सकते हैं।

Catalog और overrides

static catalog में वर्तमान में `deepseek-v3.2` और `ernie-5.0-thinking-preview` शामिल हैं। `models.providers.qianfan` जोड़ें या override करें केवल जब आपको custom base URL या model metadata चाहिए।

समस्या निवारण

  * सुनिश्चित करें कि आपकी API key `bce-v3/ALTAK-` से शुरू होती है और Baidu Cloud console में Qianfan API access सक्षम है।
  * यदि models सूचीबद्ध नहीं हैं, तो पुष्टि करें कि आपके account में Qianfan service सक्रिय है।
  * डिफ़ॉल्ट base URL `https://qianfan.baidubce.com/v2` है। इसे केवल तब बदलें जब आप custom endpoint या proxy का उपयोग करें।


## संबंधित

[**मॉडल चयन** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Configuration संदर्भ** पूरा OpenClaw configuration संदर्भ। ](</hi/gateway/configuration-reference>) [**Agent setup** agent defaults और model assignments configure करना। ](</hi/concepts/agent>) [**Qianfan API docs** आधिकारिक Qianfan API documentation। ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo

Open issue