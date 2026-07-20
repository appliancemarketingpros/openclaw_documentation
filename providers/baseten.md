---
title: Baseten
source_url: https://docs.openclaw.ai/providers/baseten
scraped_at: 2026-07-20
---

Get started

[Baseten Model APIs](<https://docs.baseten.co/inference/model-apis/overview>) provide hosted, OpenAI-compatible access to frontier models. The official external plugin uses authenticated discovery, so OpenClaw follows the complete model set enabled for your Baseten account. Its offline fallback contains every Model API available when this OpenClaw release was built.

Property | Value  
---|---  
Provider id | `baseten`  
Plugin | official external package (`@openclaw/baseten-provider`)  
Auth env var | `BASETEN_API_KEY`  
Onboarding flag | `--auth-choice baseten-api-key`  
Direct CLI flag | `--baseten-api-key <key>`  
API | OpenAI-compatible (`openai-completions`)  
Base URL | `https://inference.baseten.co/v1`  
Default model | `baseten/thinkingmachines/inkling`  
  
## Install plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/baseten-provideropenclaw gateway restart
[/code]

## Getting started

* ### Create a Baseten account and API key

Baseten's Basic plan has no monthly platform fee; Model API calls are usage-priced. Create a key in [Baseten API key settings](<https://app.baseten.co/settings/api_keys>) and check current rates on the [pricing page](<https://www.baseten.co/pricing>).

* ### Run onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice baseten-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice baseten-api-key \--baseten-api-key "$BASETEN_API_KEY"
[/code]

Env onlyCopy code
[code]
    export BASETEN_API_KEY=...
[/code]

* ### Verify the live catalog

bashCopy code
[code]
    openclaw models list --provider baseten
[/code]

With usable auth, the plugin requests `GET /v1/models` and lists every model returned for the account. Without auth, it stays offline and uses the bundled fallback.

## Inkling

[Thinking Machines Lab's Inkling](<https://thinkingmachines.ai/news/introducing-inkling/>) is the default model. In OpenClaw it supports text and image input, tool calling, structured tool schemas, configurable reasoning effort, a 1.048M-token context window, and up to 32k output tokens:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },}
[/code]

Use `/model baseten/thinkingmachines/inkling` to switch an existing chat.

## Bundled fallback catalog

The authenticated live catalog is authoritative. These rows keep setup and model selection useful before discovery succeeds:

Model ref | Input | Context | Max output  
---|---|---|---  
`baseten/deepseek-ai/DeepSeek-V4-Pro` | text | 262k | 262k  
`baseten/zai-org/GLM-4.7` | text | 200k | 200k  
`baseten/zai-org/GLM-5` | text | 202k | 202k  
`baseten/zai-org/GLM-5.1` | text | 202k | 202k  
`baseten/zai-org/GLM-5.2` | text | 202k | 202k  
`baseten/thinkingmachines/inkling` | text, image | 1.048M | 32k  
`baseten/moonshotai/Kimi-K2.5` | text, image | 262k | 262k  
`baseten/moonshotai/Kimi-K2.6` | text, image | 262k | 262k  
`baseten/moonshotai/Kimi-K2.7-Code` | text, image | 262k | 262k  
`baseten/nvidia/Nemotron-120B-A12B` | text | 202k | 202k  
`baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | text | 202k | 202k  
`baseten/openai/gpt-oss-120b` | text | 128k | 128k  
  
All bundled models support tool calling and reasoning. OpenClaw maps its thinking levels to models with native `reasoning_effort`. Baseten's opt-in GLM, Kimi, and Nemotron models default to thinking off; most expose a binary off/on control, while GLM 5.2 exposes off, high, and max. OpenClaw sends these choices through Baseten's `chat_template_args.enable_thinking` control and, for GLM 5.2, the validated top-level `reasoning_effort` parameter.

## Manual config

Most setups only need the API key. To pin the provider explicitly:

json5Copy code
[code]
    {  env: { BASETEN_API_KEY: "..." },  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },  models: {    mode: "merge",    providers: {      baseten: {        baseUrl: "https://inference.baseten.co/v1",        apiKey: "${BASETEN_API_KEY}",        api: "openai-completions",        models: [          {            id: "thinkingmachines/inkling",            name: "Inkling",            reasoning: true,            input: ["text", "image"],            contextWindow: 1048000,            maxTokens: 32000,            compat: {              supportsStore: false,              supportsDeveloperRole: false,              supportsUsageInStreaming: true,              supportsStrictMode: true,              supportsTools: true,              supportsReasoningEffort: true,              supportedReasoningEfforts: ["none", "minimal", "low", "medium", "high", "xhigh"],              reasoningEffortMap: {                off: "none",                none: "none",                adaptive: "xhigh",                max: "xhigh",              },              maxTokensField: "max_tokens",            },          },        ],      },    },  },}
[/code]

## Related

[**Model providers** Choosing providers, model refs, and failover behavior. ](</concepts/model-providers>) [**Thinking modes** Select OpenClaw reasoning effort levels. ](</tools/thinking>) [**Models CLI** List, inspect, and select discovered models. ](</cli/models>) [**Models FAQ** Auth profiles and model-selection troubleshooting. ](</help/faq-models>)

Was this useful?YesNo

Open issue