---
title: Particle
source_url: https://docs.openclaw.ai/providers/particle
scraped_at: 2026-11-02
---

ModelsProviders

[Particle](<https://particle.ai>) serves Particle-1 through an OpenAI-compatible Chat Completions API.

Property | Value  
---|---  
Provider | `particle`  
Plugin | `@openclaw/particle-provider`  
API key environment variable | `PARTICLE_API_KEY`  
Base URL | `https://api.particle.ai/v1`  
API | `openai-completions`  
Default model | `particle/particle-ai/particle-1`  
  
## Setup

  1. Create an API key at [platform.particle.ai](<https://platform.particle.ai>). Inference requires the key's `inference` scope and a positive credit balance unless Particle grants the key free access.

  2. Install the provider plugin:

bashCopy code
[code]openclaw plugins install @openclaw/particle-provider
[/code]

  3. Run onboarding:

bashCopy code
[code]openclaw onboard --auth-choice particle-api-key
[/code]


For non-interactive setup with a key already in the environment:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk --skip-health \  --auth-choice particle-api-key \  --particle-api-key "$PARTICLE_API_KEY"
[/code]

Make the environment variable available to the Gateway process, not just your interactive shell. See [Environment variables](</help/environment>).

Verify configuration and select the model:

bashCopy code
[code]
    openclaw models list --provider particleopenclaw models set particle/particle-ai/particle-1
[/code]

## Particle-1

The catalog uses the ID Particle lists and returns, `particle-ai/particle-1`. The short alias `particle-1` is accepted wherever you type a model.

  * Text and image input; text output, reasoning, and function tool calling.
  * 1,048,576-token context window; up to 131,072 output tokens. Particle defaults to 32,000 output tokens when a client does not send a limit; OpenClaw sends its own output limit.
  * Standard prices: $0.25 input, $0.03 cached input, and $1.00 output per million tokens. Reasoning tokens count as output tokens. These are catalog estimates, not a live billing report.


Limits and prices were checked against Particle's [model catalog](<https://docs.particle.ai/models>) and [billing documentation](<https://docs.particle.ai/usage-billing>) on October 29, 2026.

## Reasoning and caching

Particle-1 defaults to high reasoning. OpenClaw exposes `off`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`:

  * `off` sends `reasoning_effort: "none"`.
  * `minimal` and `low` select low effort.
  * `medium`, `high`, and `xhigh` select high effort.
  * `max` selects max effort.


See [Thinking levels](</tools/thinking>) and Particle's [reasoning controls](<https://docs.particle.ai/reasoning>).

The plugin enables the standard conversation `prompt_cache_key` for cache routing. Particle does not document a client-selectable cache-retention duration.

## Supported API surface

Particle accepts JSON mode, but does **not** advertise schema-guaranteed structured output. Do not rely on strict JSON Schema enforcement.

Official references: [Quickstart](<https://docs.particle.ai/quickstart>), [Authentication](<https://docs.particle.ai/authentication>), [Chat Completions](<https://docs.particle.ai/chat-completions>).

Was this useful?YesNo

Open issue