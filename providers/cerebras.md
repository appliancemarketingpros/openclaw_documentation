---
title: Cerebras
source_url: https://docs.openclaw.ai/providers/cerebras
scraped_at: 2026-05-04
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

Cerebras

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

[Cerebras](<https://www.cerebras.ai>) provides high-speed OpenAI-compatible inference.

Property| Value  
---|---  
Provider| `cerebras`  
Auth| `CEREBRAS_API_KEY`  
API| OpenAI-compatible  
Base URL| `https://api.cerebras.ai/v1`  
  
## 

​

Getting Started

1

Get an API key

Create an API key in the [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

2

Run onboarding
[code]
    openclaw onboard --auth-choice cerebras-api-key
    
[/code]

3

Verify models are available
[code]
    openclaw models list --provider cerebras
    
[/code]

### 

​

Non-Interactive Setup
[code] 
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice cerebras-api-key \
      --cerebras-api-key "$CEREBRAS_API_KEY"
    
[/code]

## 

​

Built-In Catalog

OpenClaw ships a static Cerebras catalog for the public OpenAI-compatible endpoint:

Model ref| Name| Notes  
---|---|---  
`cerebras/zai-glm-4.7`| Z.ai GLM 4.7| Default model; preview reasoning model  
`cerebras/gpt-oss-120b`| GPT OSS 120B| Production reasoning model  
`cerebras/qwen-3-235b-a22b-instruct-2507`| Qwen 3 235B Instruct| Preview non-reasoning model  
`cerebras/llama3.1-8b`| Llama 3.1 8B| Production speed-focused model  
  
Cerebras marks `zai-glm-4.7` and `qwen-3-235b-a22b-instruct-2507` as preview models, and `llama3.1-8b` / `qwen-3-235b-a22b-instruct-2507` are documented for deprecation on May 27, 2026. Check Cerebras’ supported-models page before relying on them for production.

## 

​

Manual Config

The bundled plugin usually means you only need the API key. Use explicit `models.providers.cerebras` config when you want to override model metadata:
[code] 
    {
      env: { CEREBRAS_API_KEY: "sk-..." },
      agents: {
        defaults: {
          model: { primary: "cerebras/zai-glm-4.7" },
        },
      },
      models: {
        mode: "merge",
        providers: {
          cerebras: {
            baseUrl: "https://api.cerebras.ai/v1",
            apiKey: "${CEREBRAS_API_KEY}",
            api: "openai-completions",
            models: [
              { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },
              { id: "gpt-oss-120b", name: "GPT OSS 120B" },
            ],
          },
        },
      },
    }
    
[/code]

If the Gateway runs as a daemon (launchd/systemd), make sure `CEREBRAS_API_KEY` is available to that process, for example in `~/.openclaw/.env` or through `env.shellEnv`.

[Azure Speech](</providers/azure-speech>)[Chutes](</providers/chutes>)

⌘I