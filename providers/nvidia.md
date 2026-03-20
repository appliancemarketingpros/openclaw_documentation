---
title: NVIDIA
source_url: https://docs.openclaw.ai/providers/nvidia
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

NVIDIA

# 

​

NVIDIA

NVIDIA provides an OpenAI-compatible API at `https://integrate.api.nvidia.com/v1` for Nemotron and NeMo models. Authenticate with an API key from [NVIDIA NGC](<https://catalog.ngc.nvidia.com/>).

## 

​

CLI setup

Export the key once, then run onboarding and set an NVIDIA model:

Copy
[code]
    export NVIDIA_API_KEY="nvapi-..."
    openclaw onboard --auth-choice skip
    openclaw models set nvidia/nvidia/llama-3.1-nemotron-70b-instruct
    
[/code]

If you still pass `--token`, remember it lands in shell history and `ps` output; prefer the env var when possible.

## 

​

Config snippet

Copy
[code]
    {
      env: { NVIDIA_API_KEY: "nvapi-..." },
      models: {
        providers: {
          nvidia: {
            baseUrl: "https://integrate.api.nvidia.com/v1",
            api: "openai-completions",
          },
        },
      },
      agents: {
        defaults: {
          model: { primary: "nvidia/nvidia/llama-3.1-nemotron-70b-instruct" },
        },
      },
    }
    
[/code]

## 

​

Model IDs

  * `nvidia/llama-3.1-nemotron-70b-instruct` (default)
  * `meta/llama-3.3-70b-instruct`
  * `nvidia/mistral-nemo-minitron-8b-8k-instruct`


## 

​

Notes

  * OpenAI-compatible `/v1` endpoint; use an API key from NVIDIA NGC.
  * Provider auto-enables when `NVIDIA_API_KEY` is set; uses static defaults (131,072-token context window, 4,096 max tokens).


[Mistral](</providers/mistral>)[Ollama](</providers/ollama>)

⌘I