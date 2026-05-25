---
title: Synthetisch
source_url: https://docs.openclaw.ai/nl/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) biedt Anthropic-compatibele eindpunten. OpenClaw registreert dit als de `synthetic`-provider en gebruikt de Anthropic Messages API.

Eigenschap | Waarde  
---|---  
Provider | `synthetic`  
Authenticatie | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Basis-URL | `https://api.synthetic.new/anthropic`  
  
## Aan de slag

* ### Een API-sleutel ophalen

Haal een `SYNTHETIC_API_KEY` op uit je Synthetic-account, of laat de onboardingwizard je erom vragen.

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Het standaardmodel verifiëren

Na onboarding wordt het standaardmodel ingesteld op:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Ingebouwde catalogus

Alle Synthetic-modellen gebruiken kosten `0` (invoer/uitvoer/cache).

Model-ID | Contextvenster | Max. tokens | Redeneren | Invoer  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | nee | tekst  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | ja | tekst  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | nee | tekst  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | nee | tekst  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | nee | tekst  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | nee | tekst  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | nee | tekst  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | nee | tekst  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | nee | tekst  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | nee | tekst  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | nee | tekst  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | ja | tekst + beeld  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | nee | tekst  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | nee | tekst  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | nee | tekst  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | nee | tekst + beeld  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | nee | tekst  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | nee | tekst  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | ja | tekst + beeld  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | nee | tekst  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | ja | tekst  
  
Toegestane modellenlijst

Als je een toegestane modellenlijst (`agents.defaults.models`) inschakelt, voeg dan elk Synthetic-model toe dat je wilt gebruiken. Modellen die niet in de toegestane lijst staan, worden verborgen voor de agent.

Basis-URL overschrijven

Als Synthetic het API-eindpunt wijzigt, overschrijf dan de basis-URL in je configuratie:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Onthoud dat OpenClaw automatisch `/v1` toevoegt.

## Gerelateerd

[**Modelselectie** Providerregels, modelverwijzingen en failovergedrag. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledig configuratieschema inclusief providerinstellingen. ](</nl/gateway/configuration-reference>) [**Synthetic** Synthetic-dashboard en API-documentatie. ](<https://synthetic.new>)

Was this useful?YesNo