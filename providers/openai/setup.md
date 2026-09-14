---
title: OpenAI setup
source_url: https://docs.openclaw.ai/providers/openai/setup
scraped_at: 2026-09-14
---

ModelsProviders

## Getting started

### API key (OpenAI Platform)

**Best for:** direct API access and usage-based billing.

* ### Get your API key

Create or copy an API key from the [OpenAI Platform dashboard](<https://platform.openai.com/api-keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

Or pass the key directly:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### Route summary

Model ref | Runtime policy or route facts | Route | Auth  
---|---|---|---  
`openai/gpt-5.6` | unset/`auto`, exact official HTTPS native route, no request override | Codex may be selected | Ordered API-key auth profile  
`openai/gpt-5.6` | provider/model `agentRuntime.id: "openclaw"` | OpenClaw embedded runtime | Selected `openai` API-key profile  
`openai/gpt-5.5` | explicit provider/model `agentRuntime.id` | Selected agent runtime | Selected OpenAI API-key profile  
`openai/*` | authored Completions, custom, or request override | OpenClaw embedded runtime | Credential type remains unchanged  
`openai/*` | plaintext official HTTP endpoint | Rejected | Credential is not sent  
  
### Config example

json5Copy code
[code]
    {  env: { vars: { OPENAI_API_KEY: "example-openai-key-not-real" } },  agents: { defaults: { model: { primary: "openai/gpt-6-astra" } } },}
[/code]

The bare direct-API `gpt-5.6` alias is also accepted and resolves to the Sol tier. If this API organization does not expose GPT-5.6, set the primary to `openai/gpt-5.5` explicitly.

To try ChatGPT's current Instant model from the OpenAI API, set the model to `openai/chat-latest`:

json5Copy code
[code]
    {  env: { vars: { OPENAI_API_KEY: "example-openai-key-not-real" } },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` is a moving alias. Fresh OpenAI API-key setup instead uses `openai/gpt-6-astra`. The bare direct-API `openai/gpt-5.6` alias remains supported and resolves to Sol. Existing explicit primaries, including `openai/gpt-5.5`, remain unchanged. The `chat-latest` alias only accepts `medium` text verbosity; OpenClaw forces any other requested verbosity to `medium` for this model.

### Codex subscription

**Best for:** using your ChatGPT/Codex subscription with native Codex app-server execution instead of a separate API key. Codex cloud requires ChatGPT sign-in.

* ### Run Codex OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice openai
[/code]

Or run OAuth directly:

bashCopy code
[code]
    openclaw models auth login --provider openai
[/code]

For headless or callback-hostile setups, add `--device-code` to sign in with a ChatGPT device-code flow instead of the localhost browser callback:

bashCopy code
[code]
    openclaw models auth login --provider openai --device-code
[/code]

* ### Use the canonical OpenAI model route

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-6-astra
[/code]

No runtime config is required for this exact official HTTPS native route. It may select the Codex app-server runtime automatically, and OpenClaw installs or repairs the bundled Codex plugin when that runtime is chosen.

* ### Verify Codex auth is available

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

After the gateway is running, send `/codex status` or `/codex models` in chat to verify the native app-server runtime.

### Route summary

Model ref | Runtime policy or route facts | Route | Auth  
---|---|---|---  
`openai/gpt-6-astra` | unset/`auto`, exact official HTTPS native route, no request override | Codex may be selected | Codex sign-in, or an ordered `openai` auth profile  
`openai/gpt-5.6-terra` | unset/`auto`, exact official HTTPS native route, no request override | Codex may be selected | Codex sign-in when the catalog exposes Terra  
`openai/gpt-5.6-luna` | unset/`auto`, exact official HTTPS native route, no request override | Codex may be selected | Codex sign-in when the catalog exposes Luna  
`openai/gpt-6-astra` | provider/model `agentRuntime.id: "openclaw"` | OpenClaw embedded runtime, internal Codex-auth transport | Selected `openai` OAuth profile  
`openai/gpt-5.5` | explicit provider/model `agentRuntime.id` | Selected agent runtime | Selected OpenAI auth profile  
`openai/*` | authored Completions, custom, or request override | OpenClaw embedded runtime | Credential requirement remains route-specific  
`openai/*` | plaintext official HTTP endpoint | Rejected | Credential is not sent  
Legacy Codex GPT-5.5 ref | repaired by doctor | Rewritten to `openai/gpt-5.5` | Migrated OpenAI OAuth profile  
`codex-cli/gpt-5.5` | repaired by doctor | Rewritten to `openai/gpt-5.5` | Codex app-server auth  
  
### Config example

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-6-astra" },    },  },}
[/code]

With an API-key backup, keep the selected model under `openai/*` and put the auth order under `openai`. OpenClaw tries the subscription first, then the API key, while staying on the Codex harness:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-6-astra" },    },  },  auth: {    order: {      openai: [        "openai:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Check and recover Codex OAuth routing

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openaiopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

For a specific agent, add `--agent <id>`:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai
[/code]

If an older config still has legacy Codex GPT refs, or a stale OpenAI runtime session pin without explicit runtime config, repair it:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

If `models auth list --provider openai` shows no usable profile, sign in again:

bashCopy code
[code]
    openclaw models auth login --provider openaiopenclaw models status --probe --probe-provider openai
[/code]

Use `--profile-id` for multiple Codex OAuth logins in the same agent, then control them via auth ordering or `/model ...@<profileId> -s`:

bashCopy code
[code]
    openclaw models auth login --provider openai --profile-id openai:ritsukoopenclaw models auth login --provider openai --profile-id openai:lain
[/code]

Run `openclaw doctor --fix` to migrate older legacy OpenAI Codex prefix profile ids and order entries before relying on profile ordering.

### Status indicator

Chat `/status` shows which model runtime is active for the current session. The bundled Codex app-server harness appears as `Runtime: OpenAI Codex` when an eligible implicit route or explicit provider/model runtime policy selects it.

### Doctor warning

If legacy Codex model refs or stale OpenAI runtime pins remain in config or session state, `openclaw doctor --fix` rewrites them to `openai/*` with the Codex runtime unless OpenClaw is explicitly configured.

### Context window defaults and long-context opt-in

OpenClaw treats native model capacity and the active runtime budget as separate values:

  * `contextWindow` declares the model's native window.
  * `contextTokens` caps how much of that window OpenClaw uses for active input.


ChatGPT/Codex OAuth follows the live Codex account catalog. The current catalog commonly advertises a `272000` token active window for GPT-5.6. Direct API-key GPT-5.5 and GPT-5.6 models also default to `272000` `contextTokens`, even though the Platform API exposes a larger native window. This keeps the normal latency, quality, and cost profile consistent across auth modes. Override a direct model's active-input budget with `models.providers.openai.models[].contextTokens` on that exact model entry.

For direct API-key GPT-5.5 and GPT-5.6, OpenAI documents a `1050000` token provider window and `128000` maximum output tokens. Reserving the full output allowance gives the shared safe input budget used by both runtime recipes below:

textCopy code
[code]
    1050000 total - 128000 maximum output = 922000 safe active inputautomatic compaction threshold = 700000 active tokens
[/code]

`922000` is a derived operating budget, not a separate provider-published input limit. The two runtimes translate that budget differently: embedded OpenClaw sends Responses compaction controls, while native Codex owns its catalog window and automatic compaction. See the official [model comparison](<https://developers.openai.com/api/docs/models/compare>) and [GPT-5.5 model page](<https://developers.openai.com/api/docs/models/gpt-5.5>).

#### Embedded OpenClaw translation

This example pins the exact Sol model to the embedded OpenClaw runtime, enables OpenAI API Fast mode through the shared runtime control, and asks OpenAI Responses to compact at `700000` active tokens:

json5Copy code
[code]
    {  models: {    providers: {      openai: {        models: [          {            id: "gpt-5.6-sol",            name: "GPT-5.6 Sol",            contextWindow: 1050000,            contextTokens: 922000,            maxTokens: 128000,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.6-sol" },      models: {        "openai/gpt-5.6-sol": {          agentRuntime: { id: "openclaw" },          params: {            fastMode: true,            responsesServerCompaction: true,            responsesCompactThreshold: 700000,          },        },      },    },  },}
[/code]

OpenAI Responses automatic compaction emits an encrypted `compaction` output item. A stateless client carries the newest item into the next request and may drop every earlier input item. OpenClaw persists that item opaquely, fences reuse by route, session, and auth, replays it, prunes the replaced prefix, carries it through worker transcript commits, and removes it from display and diagnostics. Never print, log, or expose the encrypted content.

A process-owned isolated-Gateway run on OpenClaw 2026.8.1 verified this exact `openai/gpt-5.6-sol` configuration. Dense turns reached `295098`, `586562`, and `863664` prompt tokens. Turn three emitted and persisted a first-class server compaction item; the next request replayed that exact opaque item, pruned its prefix, and used `9602` prompt tokens. A deterministic long response produced `5480` output tokens, durable markers survived compaction and Gateway restart, restart latency was `12081` ms, every call reported `serviceTier: priority`, and the full suite took `220.03` seconds. These timings are observations, not service-level guarantees.

#### Native Codex translation

Keep the same OpenClaw model selection, but make Codex the explicit runtime and do not add Responses compaction params to this model entry:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "openai/gpt-5.6-sol" },      models: {        "openai/gpt-5.6-sol": {          agentRuntime: { id: "codex" },          params: { fastMode: true },        },      },    },  },}
[/code]

Codex must receive `922000` for both `context_window` and `max_context_window`, `700000` for `auto_compact_token_limit`, and matching app-server overrides with `model_auto_compact_token_limit_scope=total`. Codex then applies its 95% effective-window reserve, yielding `875900` active tokens. Configure an ordered OpenAI API-key profile and keep the default isolated agent-scoped Codex home. The complete catalog, app-server, auth, and restart recipe is in [Codex harness long context](</plugins/codex-harness/configuration#direct-api-long-context>).

These examples are two explicit runtime choices, not one auto-selecting configuration. The model-scoped `agentRuntime` and runtime-owned compaction settings must change together. OpenClaw can retain both choices only when their model refs or agent configurations are distinguishable; otherwise, switch the model runtime and its matching config as one atomic change. Then restart the Gateway and native Codex app-server, run `/model default -s`, and start a fresh chat. Existing native Codex threads retain the provider and model recorded when they were created.

### Catalog recovery

OpenClaw uses upstream Codex catalog metadata for `gpt-5.5` when it is present. If live Codex discovery omits the `gpt-5.5` row while the account is authenticated, OpenClaw synthesizes that OAuth model row so cron, sub-agent, and configured default-model runs do not fail with `Unknown model`.

Was this useful?YesNo

Open issue