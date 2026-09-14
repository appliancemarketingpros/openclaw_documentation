---
title: OpenAI advanced configuration
source_url: https://docs.openclaw.ai/providers/openai/advanced
scraped_at: 2026-09-14
---

ModelsProviders

## GPT-5 prompt contribution

OpenClaw adds a shared GPT-5 prompt contribution to matching GPT-5-family OpenClaw-assembled prompts. The OpenAI plugin setting below controls the friendly style on OpenAI-family routes. Older GPT-4.x model ids do not match.

The native Codex app-server harness does not receive the persona/tool- discipline behavior contract or the friendly interaction-style overlay through developer instructions; native Codex keeps Codex-owned base, model, and project-doc behavior, and OpenClaw disables Codex's built-in personality for native threads so agent workspace personality files stay authoritative. OpenClaw contributes only runtime context to native Codex threads: channel delivery, OpenClaw dynamic tools, ACP delegation, workspace context, and OpenClaw skills. The heartbeat-guidance text from this same contribution is the one exception: native Codex heartbeat turns do get it, injected as dedicated collaboration instructions rather than through the shared prompt-contribution hook.

The GPT-5 contribution adds a tagged behavior contract for persona persistence, execution safety, tool discipline, output shape, completion checks, and verification on matching OpenClaw-assembled prompts. Channel- specific reply and silent-message behavior stays in the shared OpenClaw system prompt and outbound delivery policy. The friendly interaction-style layer is separate and configurable.

Value | Effect  
---|---  
`"friendly"` (default) | Enable the friendly interaction-style layer  
`"on"` | Alias for `"friendly"`  
`"off"` | Disable only the friendly style layer  
  
### Config

json5Copy code
[code]
    {  plugins: {    entries: {      openai: {        config: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set plugins.entries.openai.config.personality off
[/code]

## Advanced configuration

The `transport` and `serviceTier` examples below are authored embedded-provider request settings, so an otherwise eligible `auto` route stays on OpenClaw instead of selecting Codex implicitly. Valid `fastMode` / `fast_mode` values and valid cutoff keys are typed agent-runtime controls and do not select a runtime. Runtime-specific examples therefore pin `agentRuntime.id` explicitly. The native Codex app-server harness owns its transport and request settings. Authored embedded-provider settings can therefore select the declared OpenClaw fallback even with explicit `agentRuntime.id: "codex"`; see [Runtime selection](</concepts/agent-runtimes#runtime-selection>).

Transport (WebSocket vs SSE)

Direct API-key requests use SSE by default. Set `params.transport` when you want Responses WebSocket mode on an eligible official OpenAI endpoint.

Value | Behavior  
---|---  
`"sse"` (default) | Stream each request over SSE  
`"auto"` | Prefer a session-cached WebSocket, with pre-dispatch SSE fallback  
`"websocket-cached"` | Explicitly use the session-cached WebSocket path, with the same pre-dispatch SSE fallback  
`"websocket"` | Use a transient WebSocket for the request, with pre-dispatch SSE fallback  
  
Cached modes keep one eligible connection per session. When the prior request and response still match the current history, OpenClaw sends only the new input and references the prior response with `previous_response_id`. Otherwise it sends full history without that reference.

A setup or handshake failure before request dispatch falls back to SSE; it is not retried or reconnected first. After dispatch, failures with an unknown outcome remain replay-unsafe and fail closed. The explicit server rejections `previous_response_not_found` and `websocket_connection_limit_reached` are safe exceptions: OpenClaw closes the failed socket and retries that turn once over SSE with full history and no rejected `previous_response_id`.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          agentRuntime: { id: "openclaw" },          params: { transport: "auto" },        },      },    },  },}
[/code]

Related OpenAI docs:

  * [Responses API WebSocket mode](<https://developers.openai.com/api/docs/guides/websocket-mode>)
  * [Streaming API responses (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Fast mode

OpenClaw exposes a shared fast-mode toggle for `openai/*`:

  * **Chat/UI:** `/fast status|auto|on|off`
  * **Config:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Valid `params.fastMode` / `params.fast_mode` values and valid cutoff keys are typed runtime controls. They do not count as authored provider request params and do not select OpenClaw or Codex. The example below pins embedded OpenClaw because it describes a direct provider request.

When enabled on the embedded runtime, OpenClaw maps fast mode to OpenAI API Fast mode (formerly Priority processing) and sends `service_tier = "priority"`. Fast mode does not rewrite `reasoning` or `text.verbosity`. `fastMode: "auto"` starts new model calls fast until the auto cutoff, then starts later retry, fallback, tool-result, or continuation calls without fast mode. The cutoff defaults to 60 seconds; set `params.fastAutoOnSeconds` on the active model to change it.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          agentRuntime: { id: "openclaw" },          params: { fastMode: "auto", fastAutoOnSeconds: 30 },        },      },    },  },}
[/code]

Fast mode is premium-priced and model-specific. GPT-5.6 Sol API Fast mode currently costs 2× Standard token pricing, with long-context multipliers stacking as described in [context window defaults and long-context opt-in](</providers/openai/setup#context-window-defaults-and-long-context-opt-in>). ChatGPT/Codex-credit Fast mode is a separate billing system: GPT-5.6 and GPT-5.5 currently consume 2.5× Standard credits, while API-key Codex runs use API token pricing. See [Fast mode](<https://openai.com/api-priority-processing/>), [API pricing](<https://developers.openai.com/api/docs/pricing>), and [Codex speed](<https://learn.chatgpt.com/docs/agent-configuration/speed>).

OpenAI API Fast mode with service_tier

OpenAI now calls this API product Fast mode; it was formerly Priority processing. OpenClaw sends the wire value `service_tier = "priority"`. Set an explicit tier per model on the embedded OpenClaw runtime:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          agentRuntime: { id: "openclaw" },          params: { serviceTier: "priority" },        },      },    },  },}
[/code]

Supported values: `auto`, `default`, `flex`, `priority`.

Server-side compaction (Responses API)

For store-capable direct OpenAI Responses models (`openai/*` resolved to `api.openai.com`), the OpenAI plugin's OpenClaw stream wrapper auto-enables server-side compaction:

  * Forces `store: true` (unless model compat sets `supportsStore: false`)
  * Injects `context_management: [{ type: "compaction", compact_threshold: ... }]`
  * Default `compact_threshold`: 70% of `contextWindow` (or `80000` when unavailable)


The same resolved route and effective threshold gate the client preflight, so OpenClaw does not delay local compaction unless the transport will inject `context_management`. ChatGPT OAuth, custom proxies, and routes with `compat.supportsStore: false` are not store-capable and therefore ignore these server-compaction controls. This applies to the built-in OpenClaw runtime path and to OpenAI provider hooks used by embedded runs. The native Codex app-server harness manages its own context through Codex and is not affected by this setting.

OpenAI emits the compacted state as an encrypted `compaction` output item. Keep that item opaque. For stateless continuation, carry the newest item forward and drop the earlier input prefix it replaces. OpenClaw does this automatically: it persists and replays the item only for the matching route, session, and auth identity, preserves it across worker transcript commits, and filters it from user-visible history and diagnostics. Never display or log the encrypted content.

### Enable explicitly

Useful for store-capable endpoints like Azure OpenAI Responses. Setting this to `true` does not override endpoint or `supportsStore` capability:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Custom threshold

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Disable

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Strict-agentic GPT mode

For `openai` provider GPT-5-family models run through OpenClaw's embedded runtime, OpenClaw already defaults to a stricter execution contract called `strict-agentic`. It auto-activates whenever the resolved provider is `openai` and the model id matches the GPT-5 family, unless config explicitly opts back out:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedAgent: { executionContract: "default" },    },  },}
[/code]

Setting `"strict-agentic"` explicitly is a no-op on a supported lane (it is already the default) and inert on unsupported provider/model pairs.

With `strict-agentic` active, OpenClaw:

  * Makes `progress_card` available for substantial work unless `tools.updatePlan` disables it
  * Retries structurally empty or reasoning-only turns with a visible-answer continuation
  * Uses explicit harness plan events when the selected harness provides them


OpenClaw does not classify assistant prose to decide whether a turn is a plan, progress update, or final answer.

Native vs OpenAI-compatible routes

OpenClaw treats direct OpenAI, Codex, and Azure OpenAI endpoints differently from generic OpenAI-compatible `/v1` proxies:

**Native routes** (`openai/*`, Azure OpenAI):

  * Keep `reasoning: { effort: "none" }` only for models that support the OpenAI `none` effort
  * Omit disabled reasoning for models or proxies that reject `reasoning.effort: "none"`
  * Default tool schemas to strict mode
  * Attach hidden attribution headers on verified native hosts only (Azure OpenAI does not get these headers, even though it is a native route)
  * Keep OpenAI-only request shaping (`service_tier`, `store`, reasoning-compat, prompt-cache hints)


**Proxy/compatible routes:**

  * Use looser compat behavior
  * Strip Completions `store` from non-native `openai-completions` payloads
  * Accept advanced `params.extra_body`/`params.extraBody` pass-through JSON for OpenAI-compatible Completions proxies
  * Accept `params.chat_template_kwargs` for OpenAI-compatible Completions proxies such as vLLM
  * Do not force strict tool schemas or native-only headers


If a usable tool schema is incompatible with requested strict mode, the request uses `strict: false`. Debug logs report the downgrade under `openai-transport`, with a bounded sample of incompatible tools. Built-in and managed Responses requests share duplicate suppression for the same model and schemas.

Was this useful?YesNo

Open issue