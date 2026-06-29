---
title: कृत्रिम
source_url: https://docs.openclaw.ai/hi/providers/synthetic
scraped_at: 2026-06-29
---

ModelsProviders

[Synthetic](<https://synthetic.new>) Anthropic-संगत एंडपॉइंट्स उपलब्ध कराता है। OpenClaw इसे `synthetic` provider के रूप में पंजीकृत करता है और Anthropic Messages API का उपयोग करता है।

गुण | मान  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
बेस URL | `https://api.synthetic.new/anthropic`  
  
## शुरू करना

* ### API कुंजी प्राप्त करें

अपने Synthetic खाते से `SYNTHETIC_API_KEY` प्राप्त करें, या ऑनबोर्डिंग विज़ार्ड को आपसे एक कुंजी मांगने दें।

* ### ऑनबोर्डिंग चलाएं

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### डिफ़ॉल्ट मॉडल सत्यापित करें

ऑनबोर्डिंग के बाद डिफ़ॉल्ट मॉडल इस पर सेट होता है:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## कॉन्फ़िग उदाहरण

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## अंतर्निहित कैटलॉग

सभी Synthetic मॉडल लागत `0` (इनपुट/आउटपुट/कैश) का उपयोग करते हैं।

मॉडल ID | संदर्भ विंडो | अधिकतम टोकन | रीजनिंग | इनपुट  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | नहीं | टेक्स्ट  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | हाँ | टेक्स्ट  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | नहीं | टेक्स्ट  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | नहीं | टेक्स्ट  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | नहीं | टेक्स्ट  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | नहीं | टेक्स्ट  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | हाँ | टेक्स्ट + छवि  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | नहीं | टेक्स्ट  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | नहीं | टेक्स्ट  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | नहीं | टेक्स्ट + छवि  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | नहीं | टेक्स्ट  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | नहीं | टेक्स्ट  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | हाँ | टेक्स्ट + छवि  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | नहीं | टेक्स्ट  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | हाँ | टेक्स्ट  
  
मॉडल allowlist

अगर आप मॉडल allowlist (`agents.defaults.models`) सक्षम करते हैं, तो वह हर Synthetic मॉडल जोड़ें जिसे आप उपयोग करने की योजना बनाते हैं। allowlist में नहीं मौजूद मॉडल agent से छिपा दिए जाएंगे।

बेस URL ओवरराइड

अगर Synthetic अपना API एंडपॉइंट बदलता है, तो अपने कॉन्फ़िग में बेस URL ओवरराइड करें:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

याद रखें कि OpenClaw अपने आप `/v1` जोड़ता है।

## संबंधित

[**मॉडल चयन** Provider नियम, मॉडल refs, और failover व्यवहार। ](</hi/concepts/model-providers>) [**कॉन्फ़िगरेशन संदर्भ** provider सेटिंग्स सहित पूरा कॉन्फ़िग schema। ](</hi/gateway/configuration-reference>) [**Synthetic** Synthetic डैशबोर्ड और API दस्तावेज़। ](<https://synthetic.new>)

Was this useful?YesNo

Open issue