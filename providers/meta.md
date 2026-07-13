---
title: Meta
source_url: https://docs.openclaw.ai/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

The **Meta API** uses the OpenAI-compatible **Responses API** (`POST /v1/responses`) for the `muse-spark-1.1` reasoning model. The provider ships as a bundled OpenClaw plugin.

Property | Value  
---|---  
Provider id | `meta`  
Plugin | bundled provider  
Auth env var | `MODEL_API_KEY`  
Onboarding flag | `--auth-choice meta-api-key`  
Direct CLI flag | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Base URL | `https://api.meta.ai/v1`  
Default model | `meta/muse-spark-1.1`  
Default reasoning | `high` (`reasoning.effort`)  
  
## Getting started

* ### Set the API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Lists the static `muse-spark-1.1` catalog entry. If `MODEL_API_KEY` is unresolved, `openclaw models status --json` reports the missing credential under `auth.unusableProfiles`.

## Non-interactive setup

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Built-in catalog

Model ref | Name | Reasoning | Context window | Max output  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | yes | 1,048,576 | 131,072  
  
Capabilities:

  * Text + image input
  * Tool calling and streaming
  * Reasoning effort: `minimal`, `low`, `medium`, `high`, `xhigh` (default: `high`)
  * Stateless encrypted reasoning replay (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Manual config

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Smoke test

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Live tests use `muse-spark-1.1` against `POST /v1/responses`.

## Related

[**Model providers** Choosing providers, model refs, and failover behavior. ](</concepts/model-providers>) [**Thinking modes** Reasoning effort levels for muse-spark-1.1. ](</tools/thinking>) [**Configuration reference** Agent defaults and model configuration. ](</gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue