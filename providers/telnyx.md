---
title: Telnyx
source_url: https://docs.openclaw.ai/providers/telnyx
scraped_at: 2026-09-28
---

ModelsProviders

[Telnyx AI inference](<https://developers.telnyx.com/docs/inference/getting-started>) provides hosted, OpenAI-compatible access to open-weight models plus proxied frontier routes. The vendor-maintained external [`@telnyx/openclaw-provider`](<https://github.com/team-telnyx/openclaw-telnyx-provider>) plugin supplies the runtime; OpenClaw carries its catalog and onboarding metadata. Authenticated discovery follows the complete model set enabled for your Telnyx account, while the offline fallback contains the models available when that plugin release was built.

Property | Value  
---|---  
Provider id | `telnyx`  
Plugin | vendor-maintained external package (`@telnyx/openclaw-provider`)  
Auth env var | `TELNYX_API_KEY`  
Onboarding flag | `--auth-choice telnyx-api-key`  
Direct CLI flag | `--telnyx-api-key <key>`  
API | OpenAI-compatible (`openai-completions`)  
Base URL | `https://api.telnyx.com/v2/ai/openai`  
Default model | `telnyx/moonshotai/Kimi-K3`  
  
## Requirements

The catalog pin for `@telnyx/openclaw-provider@0.2.0` requires OpenClaw `2026.8.1` or newer. Upgrade OpenClaw before installing the plugin:

bashCopy code
[code]
    openclaw updateopenclaw --version
[/code]

## Install plugin

bashCopy code
[code]
    openclaw plugins install telnyxopenclaw gateway restart
[/code]

## Getting started

* ### Create a Telnyx account and API key

Create a key in the [Telnyx API keys portal](<https://portal.telnyx.com/#/app/api-keys>). Inference calls are usage-priced; see the [Telnyx inference docs](<https://developers.telnyx.com/docs/inference/getting-started>) for current models and rates.

* ### Run onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice telnyx-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice telnyx-api-key \--telnyx-api-key "$TELNYX_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TELNYX_API_KEY=...
[/code]

In an interactive run, pick the **Telnyx API key** choice. For non-interactive setup, read the [security guidance](</security>) first; `--accept-risk` acknowledges that setup can write credentials and daemon configuration without prompting.

* ### Verify the live catalog

bashCopy code
[code]
    openclaw models list --refresh --provider telnyx
[/code]

With usable auth, the plugin requests the authenticated `/models` endpoint and lists every model returned for the account. Without auth, it stays offline and uses the bundled fallback.

## Default model

`telnyx/moonshotai/Kimi-K3` is the default model. In OpenClaw it supports text and image input, tool calling, reasoning, a 1M-token context window, and up to 64k output tokens:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "telnyx/moonshotai/Kimi-K3" },    },  },}
[/code]

Use `/model telnyx/moonshotai/Kimi-K3` to switch an existing chat.

## Live model discovery

The plugin fetches the authenticated `/models` endpoint and caches the result for five minutes, then merges those rows over the bundled catalog. Newly launched Telnyx models appear automatically without waiting for a plugin release, including proxied frontier routes such as `telnyx/openai/gpt-5.x`, `telnyx/anthropic/claude-haiku-4-5`, and `telnyx/google/gemini-2.5-flash`.

## Bundled fallback catalog

The authenticated live catalog is authoritative. These rows keep setup and model selection useful before discovery succeeds:

Model ref | Input | Context | Max output  
---|---|---|---  
`telnyx/moonshotai/Kimi-K3` | text, image | 1M | 64k  
`telnyx/moonshotai/Kimi-K2.6` | text, image | 262k | 8k  
`telnyx/moonshotai/Kimi-K2.5` | text, image | 256k | 8k  
`telnyx/zai-org/GLM-5.2` | text | 1M | 131k  
`telnyx/zai-org/GLM-5.1-FP8` | text | 202k | 8k  
`telnyx/MiniMaxAI/MiniMax-M3-MXFP8` | text | 1M | 8k  
`telnyx/MiniMaxAI/MiniMax-M2.7` | text | 200k | 8k  
`telnyx/Qwen/Qwen3-235B-A22B` | text | 32k | 8k  
`telnyx/openai/gpt-5.4` | text | 400k | 8k  
`telnyx/openai/gpt-5.4-mini` | text | 400k | 8k  
`telnyx/openai/gpt-5.2` | text | 400k | 8k  
`telnyx/openai/gpt-5.1` | text | 400k | 8k  
`telnyx/openai/gpt-5` | text | 400k | 8k  
`telnyx/anthropic/claude-haiku-4-5` | text | 400k | 8k  
  
All bundled models support tool calling and reasoning. The `openai/*` and `anthropic/*` ids are Telnyx-proxied frontier routes; the rest are Telnyx-hosted open-weight models. Streaming usage is reported on the final chunk.

## Manual config

Most setups only need the API key. To pin the provider explicitly:

json5Copy code
[code]
    {  env: { vars: { TELNYX_API_KEY: "..." } },  agents: {    defaults: {      model: { primary: "telnyx/moonshotai/Kimi-K3" },    },  },  models: {    mode: "merge",    providers: {      telnyx: {        baseUrl: "https://api.telnyx.com/v2/ai/openai",        apiKey: "${TELNYX_API_KEY}",        api: "openai-completions",        models: [          {            id: "moonshotai/Kimi-K3",            name: "Kimi K3",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

## Related

[**Model providers** Choosing providers, model refs, and failover behavior. ](</concepts/model-providers>) [**Thinking modes** Select OpenClaw reasoning effort levels. ](</tools/thinking>) [**Models CLI** List, inspect, and select discovered models. ](</cli/models>) [**Models FAQ** Auth profiles and model-selection troubleshooting. ](</help/faq-models>)

Was this useful?YesNo

Open issue