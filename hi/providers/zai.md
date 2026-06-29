---
title: Z.AI
source_url: https://docs.openclaw.ai/hi/providers/zai
scraped_at: 2026-06-29
---

ModelsProviders

Z.AI **GLM** मॉडल के लिए API प्लेटफ़ॉर्म है। यह GLM के लिए REST APIs प्रदान करता है और प्रमाणीकरण के लिए API keys का उपयोग करता है। अपनी API key Z.AI console में बनाएं। OpenClaw, Z.AI API key के साथ `zai` provider का उपयोग करता है।

गुण | मान  
---|---  
Provider | `zai`  
Package | `@openclaw/zai-provider`  
Auth | `ZAI_API_KEY` (लेगेसी उपनाम: `Z_AI_API_KEY`)  
API | Z.AI Chat Completions (Bearer प्रमाणीकरण)  
  
## GLM मॉडल

GLM एक मॉडल परिवार है, अलग provider नहीं। OpenClaw में, GLM मॉडल `zai/glm-5.2` जैसे refs का उपयोग करते हैं: provider `zai`, model id `glm-5.2`.

## शुरू करना

पहले provider plugin इंस्टॉल करें:

bashCopy code
[code]
    openclaw plugins install @openclaw/zai-provider
[/code]

### Auto-detect endpoint

**इनके लिए सर्वश्रेष्ठ:** अधिकांश उपयोगकर्ता। OpenClaw आपकी API key के साथ समर्थित Z.AI endpoints की जांच करता है और सही base URL अपने-आप लागू करता है।

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Explicit regional endpoint

**इनके लिए सर्वश्रेष्ठ:** वे उपयोगकर्ता जो किसी विशिष्ट Coding Plan या सामान्य API surface को बाध्य करना चाहते हैं।

* ### Pick the right onboarding choice

bashCopy code
[code]
    # Coding Plan Global (Coding Plan उपयोगकर्ताओं के लिए अनुशंसित)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (चीन क्षेत्र)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (चीन क्षेत्र)openclaw onboard --auth-choice zai-cn
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## कॉन्फ़िगरेशन उदाहरण

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  models: {    providers: {      zai: {        // GLM-5.2 Coding Plan endpoint का उपयोग करता है।        baseUrl: "https://api.z.ai/api/coding/paas/v4",      },    },  },  agents: { defaults: { model: { primary: "zai/glm-5.2" } } },}
[/code]

## बिल्ट-इन कैटलॉग

`zai` provider plugin अपना कैटलॉग plugin manifest में भेजता है, इसलिए read-only listing provider runtime लोड किए बिना ज्ञात GLM पंक्तियां दिखा सकती है:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

manifest-समर्थित कैटलॉग में वर्तमान में शामिल हैं:

Model ref | टिप्पणियां  
---|---  
`zai/glm-5.2` | Coding Plan डिफ़ॉल्ट; 1M context  
`zai/glm-5.1` | General API डिफ़ॉल्ट  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## उन्नत कॉन्फ़िगरेशन

Forward-resolving unknown GLM-5 models

अज्ञात `glm-5*` ids तब भी provider path पर forward-resolve होते हैं, जब id मौजूदा GLM-5 family shape से मेल खाता है, तो `glm-4.7` template से provider-owned metadata synthesize करके।

Tool-call streaming

Z.AI tool-call streaming के लिए `tool_stream` डिफ़ॉल्ट रूप से सक्षम है। इसे अक्षम करने के लिए:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking and preserved thinking

Z.AI thinking OpenClaw के `/think` controls का पालन करता है। thinking बंद होने पर, OpenClaw `thinking: { type: "disabled" }` भेजता है, ताकि ऐसे responses से बचा जा सके जो visible text से पहले `reasoning_content` पर output budget खर्च करते हैं।

Preserved thinking opt-in है क्योंकि Z.AI को पूरा historical `reasoning_content` replay करना होता है, जिससे prompt tokens बढ़ते हैं। इसे प्रति model सक्षम करें:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.2": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

सक्षम होने और thinking on होने पर, OpenClaw `thinking: { type: "enabled", clear_thinking: false }` भेजता है और उसी OpenAI-compatible transcript के लिए पहले का `reasoning_content` replay करता है।

उन्नत उपयोगकर्ता अब भी exact provider payload को `params.extra_body.thinking` से override कर सकते हैं।

Image understanding

Z.AI plugin image understanding register करता है।

गुण | मान  
---|---  
Model | `glm-4.6v`  
  
Image understanding configured Z.AI auth से अपने-आप resolve होता है — किसी अतिरिक्त config की आवश्यकता नहीं है।

Auth details

  * Z.AI आपकी API key के साथ Bearer auth का उपयोग करता है।
  * `zai-api-key` onboarding choice आपकी key के साथ समर्थित endpoints probe करके मेल खाने वाला Z.AI endpoint अपने-आप पहचानता है।
  * जब आप किसी विशिष्ट API surface को बाध्य करना चाहते हों, तो स्पष्ट क्षेत्रीय विकल्पों (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) का उपयोग करें।
  * लेगेसी env var `Z_AI_API_KEY` अब भी स्वीकार किया जाता है; अगर `ZAI_API_KEY` unset है, तो OpenClaw startup पर इसे `ZAI_API_KEY` में copy करता है।


## संबंधित

[**Model selection** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Configuration reference** पूरा OpenClaw config schema, जिसमें provider और model settings शामिल हैं। ](</hi/gateway/configuration-reference>)

Was this useful?YesNo

Open issue