---
title: Synthetic
source_url: https://docs.openclaw.ai/ar/providers/synthetic
scraped_at: 2026-05-25
---

[توفر Synthetic](<https://synthetic.new>) نقاط نهاية متوافقة مع Anthropic. يسجلها OpenClaw بوصفها الموفر `synthetic` ويستخدم Anthropic Messages API.

الخاصية | القيمة  
---|---  
الموفّر | `synthetic`  
المصادقة | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## البدء

* ### الحصول على مفتاح API

احصل على `SYNTHETIC_API_KEY` من حسابك في Synthetic، أو دع معالج onboarding يطلبه منك.

* ### تشغيل onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### التحقق من النموذج الافتراضي

بعد onboarding يتم ضبط النموذج الافتراضي على:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## مثال على الإعداد

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## الكتالوج المضمّن

تستخدم جميع نماذج Synthetic التكلفة `0` ‏(إدخال/إخراج/ذاكرة مؤقتة).

معرّف النموذج | نافذة السياق | الحد الأقصى للرموز | التفكير | الإدخال  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | لا | نص  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | نعم | نص  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | لا | نص  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | لا | نص  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | لا | نص  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | لا | نص  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | لا | نص  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | لا | نص  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | لا | نص  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | لا | نص  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | لا | نص  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | نعم | نص + صورة  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | لا | نص  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | لا | نص  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | لا | نص  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | لا | نص + صورة  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | لا | نص  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | لا | نص  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | نعم | نص + صورة  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | لا | نص  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | نعم | نص  
  
قائمة سماح النماذج

إذا قمت بتمكين قائمة سماح للنماذج (`agents.defaults.models`)، فأضف كل نموذج Synthetic تخطط لاستخدامه. سيتم إخفاء النماذج غير الموجودة في قائمة السماح عن الوكيل.

تجاوز Base URL

إذا غيّرت Synthetic نقطة نهاية API الخاصة بها، فجاوز base URL في إعداداتك:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

تذكّر أن OpenClaw يضيف `/v1` تلقائيًا.

## ذو صلة

[**اختيار النموذج** قواعد الموفّر ومراجع النماذج وسلوك failover. ](</ar/concepts/model-providers>) [**مرجع الإعدادات** مخطط الإعدادات الكامل بما في ذلك إعدادات الموفّر. ](</ar/gateway/configuration-reference>) [**Synthetic** لوحة تحكم Synthetic ووثائق API. ](<https://synthetic.new>)

Was this useful?YesNo