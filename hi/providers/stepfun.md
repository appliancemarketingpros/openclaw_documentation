---
title: StepFun
source_url: https://docs.openclaw.ai/hi/providers/stepfun
scraped_at: 2026-06-29
---

ModelsProviders

StepFun प्रदाता Plugin दो प्रदाता ids का समर्थन करता है:

  * मानक endpoint के लिए `stepfun`
  * Step Plan endpoint के लिए `stepfun-plan`


## Plugin इंस्टॉल करें

आधिकारिक Plugin इंस्टॉल करें, फिर Gateway पुनः प्रारंभ करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/stepfun-provideropenclaw gateway restart
[/code]

## क्षेत्र और endpoint का अवलोकन

Endpoint | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Auth env var: `STEPFUN_API_KEY`

## अंतर्निहित catalog

Standard (`stepfun`):

Model ref | Context | Max output | Notes  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | डिफ़ॉल्ट मानक model  
  
Step Plan (`stepfun-plan`):

Model ref | Context | Max output | Notes  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | डिफ़ॉल्ट Step Plan model  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | अतिरिक्त Step Plan model  
  
## शुरू करना

अपना प्रदाता surface चुनें और setup steps का पालन करें।

### Standard

**इसके लिए सर्वोत्तम:** मानक StepFun endpoint के माध्यम से सामान्य-उद्देश्य उपयोग।

* ### Choose your endpoint region

Auth choice | Endpoint | Region  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | International  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

या China endpoint के लिए:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Model refs

  * डिफ़ॉल्ट model: `stepfun/step-3.5-flash`


### Step Plan

**इसके लिए सर्वोत्तम:** Step Plan reasoning endpoint।

* ### Choose your endpoint region

Auth choice | Endpoint | Region  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | International  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

या China endpoint के लिए:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Model refs

  * डिफ़ॉल्ट model: `stepfun-plan/step-3.5-flash`
  * वैकल्पिक model: `stepfun-plan/step-3.5-flash-2603`


## उन्नत configuration

Full config: Standard provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Full config: Step Plan provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notes

  * प्रदाता एक आधिकारिक external package है; setup से पहले इसे इंस्टॉल करें।
  * `step-3.5-flash-2603` वर्तमान में केवल `stepfun-plan` पर उपलब्ध है।
  * एक single auth flow `stepfun` और `stepfun-plan` दोनों के लिए region-matched profiles लिखता है, इसलिए दोनों surfaces को साथ में discover किया जा सकता है।
  * models का निरीक्षण करने या switch करने के लिए `openclaw models list` और `openclaw models set <provider/model>` का उपयोग करें।


## संबंधित

[**Model selection** सभी प्रदाताओं, model refs, और failover behavior का अवलोकन। ](</hi/concepts/model-providers>) [**Configuration reference** प्रदाताओं, models, और plugins के लिए पूरा config schema। ](</hi/gateway/configuration-reference>) [**Model selection** models कैसे चुनें और configure करें। ](</hi/concepts/models>) [**StepFun Platform** StepFun API key management और documentation। ](<https://platform.stepfun.com>)

Was this useful?YesNo

Open issue