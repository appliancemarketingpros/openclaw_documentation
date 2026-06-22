---
title: Cohere
source_url: https://docs.openclaw.ai/providers/cohere
scraped_at: 2026-06-22
---

ModelsProviders

[Cohere](<https://cohere.com>) provides OpenAI-compatible inference through its Compatibility API. OpenClaw ships the Cohere provider during its externalization transition and also publishes it as an official external plugin with the Command A model catalog.

Property | Value  
---|---  
Provider id | `cohere`  
Plugin | bundled during transition; official external package  
Auth env var | `COHERE_API_KEY`  
Onboarding flag | `--auth-choice cohere-api-key`  
Direct CLI flag | `--cohere-api-key <key>`  
API | OpenAI-compatible (`openai-completions`)  
Base URL | `https://api.cohere.ai/compatibility/v1`  
Default model | `cohere/command-a-03-2025`  
  
## Get started

  1. Cohere is included in current OpenClaw packages. If it is unavailable, install the external package and restart the Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Create a Cohere API key.
  3. Run onboarding:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Confirm the catalog is available:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

The default model is set only when no primary model is already configured.

## Environment-only setup

Make `COHERE_API_KEY` available to the Gateway process, then select the Cohere model:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Related

  * [Model providers](</concepts/model-providers>)
  * [Models CLI](</cli/models>)
  * [Provider directory](</providers>)


Was this useful?YesNo

Open issue