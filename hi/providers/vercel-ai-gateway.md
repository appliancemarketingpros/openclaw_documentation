---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/hi/providers/vercel-ai-gateway
scraped_at: 2026-06-29
---

ModelsProviders

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) एक एकीकृत API प्रदान करता है, जिससे एक ही endpoint के माध्यम से सैकड़ों models तक पहुंचा जा सकता है।

गुण | मान  
---|---  
Provider | `vercel-ai-gateway`  
Package | `@openclaw/vercel-ai-gateway-provider`  
Auth | `AI_GATEWAY_API_KEY`  
API | Anthropic Messages संगत  
Model catalog | `/v1/models` के माध्यम से स्वतः खोजा गया  
  
## शुरू करना

* ### Plugin इंस्टॉल करें

bashCopy code
[code]
    openclaw plugins install @openclaw/vercel-ai-gateway-provider
[/code]

* ### API key सेट करें

onboarding चलाएं और AI Gateway auth विकल्प चुनें:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### डिफ़ॉल्ट model सेट करें

model को अपने OpenClaw config में जोड़ें:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### सत्यापित करें कि model उपलब्ध है

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Non-interactive उदाहरण

स्क्रिप्टेड या CI सेटअप के लिए, सभी मान command line पर पास करें:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Model ID shorthand

OpenClaw Vercel Claude shorthand model refs स्वीकार करता है और उन्हें runtime पर normalize करता है:

Shorthand input | Normalized model ref  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## उन्नत configuration

daemon प्रक्रियाओं के लिए environment variable

यदि OpenClaw Gateway daemon (launchd/systemd) के रूप में चलता है, तो सुनिश्चित करें कि `AI_GATEWAY_API_KEY` उस process के लिए उपलब्ध है।

Provider routing

Vercel AI Gateway model ref prefix के आधार पर requests को upstream provider तक route करता है। उदाहरण के लिए, `vercel-ai-gateway/anthropic/claude-opus-4.6` Anthropic के माध्यम से route होता है, जबकि `vercel-ai-gateway/openai/gpt-5.5` OpenAI के माध्यम से route होता है और `vercel-ai-gateway/moonshotai/kimi-k2.6` MoonshotAI के माध्यम से route होता है। आपकी एकल `AI_GATEWAY_API_KEY` सभी upstream providers के लिए authentication संभालती है।

Thinking levels

जब OpenClaw upstream provider contract जानता है, तो `/think` विकल्प भरोसेमंद upstream model prefixes का पालन करते हैं। `vercel-ai-gateway/anthropic/...` Claude thinking profile का उपयोग करता है, जिसमें Claude 4.6 models के लिए adaptive defaults शामिल हैं। `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5`, और Codex-style refs सीधे OpenAI/OpenAI Codex providers की तरह `/think xhigh` उपलब्ध कराते हैं। अन्य namespaced refs सामान्य reasoning levels बनाए रखते हैं, जब तक कि उनका catalog metadata अधिक घोषित न करे।

## संबंधित

[**Model चयन** providers, model refs, और failover behavior चुनना। ](</hi/concepts/model-providers>) [**Troubleshooting** सामान्य troubleshooting और FAQ। ](</hi/help/troubleshooting>)

Was this useful?YesNo

Open issue