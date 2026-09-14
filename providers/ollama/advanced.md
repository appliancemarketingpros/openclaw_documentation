---
title: Ollama advanced configuration
source_url: https://docs.openclaw.ai/providers/ollama/advanced
scraped_at: 2026-09-14
---

ModelsProviders

## Advanced configuration

Legacy OpenAI-compatible mode

Set `api: "openai-completions"` explicitly for a proxy behind `/v1/chat/completions`:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: true, // default: true        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

This mode may not support streaming and tool calling simultaneously; you may need `params: { streaming: false }` on the model.

OpenClaw injects `options.num_ctx` by default in this mode so Ollama does not silently fall back to a 4096-token context. If your proxy rejects unknown `options` fields, disable it:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: false,        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Context windows

For auto-discovered models, OpenClaw uses the context window `/api/show` reports, including larger `PARAMETER num_ctx` values from custom Modelfiles; otherwise it falls back to OpenClaw's default Ollama context window.

Per-model `contextWindow` declares native window metadata, and per-model `contextTokens` caps active input. Provider-level `maxTokens` remains an output-token default; a model entry can override it. Native `/api/chat` requests set `options.num_ctx` from a positive `params.num_ctx` first, then from the effective model `contextTokens` when present. Local discovery normally caps `contextTokens` at 32,768 (or the model's smaller native window), so OpenClaw can override a smaller Modelfile context even without an explicit `params.num_ctx`. Invalid, zero, negative, or non-finite `params.num_ctx` values are ignored. Only when neither value is available does Ollama choose its own model, Modelfile, `OLLAMA_CONTEXT_LENGTH`, or VRAM-based default; the native adapter does not fall back directly to the advertised `contextWindow`. After upgrading an older configuration, run `openclaw doctor --fix`. Doctor preserves current `contextTokens` caps without creating a stronger model or provider `num_ctx` pin; uncapped legacy native entries still migrate their older context budgets. Existing explicit `params.num_ctx` values remain authoritative, including pins an older Doctor already wrote. Review or remove an oversized existing pin to let `contextTokens` drive the request again. Use `params.num_ctx` to override the native request context explicitly. The OpenAI-compatible adapter still injects `options.num_ctx` by default from `params.num_ctx`, then the matching model entry's `contextTokens` or `contextWindow`; disable with `injectNumCtxForOpenAICompat: false` if the upstream rejects `options`.

Native model entries also accept common Ollama runtime options under `params`, forwarded as native `/api/chat` `options`: `num_keep`, `seed`, `num_predict`, `top_k`, `top_p`, `min_p`, `typical_p`, `repeat_last_n`, `temperature`, `repeat_penalty`, `presence_penalty`, `frequency_penalty`, `stop`, `num_batch`, `num_gpu`, `main_gpu`, `use_mmap`, and `num_thread`. Runtime sampling controls (`temperature`, `topP`, `frequencyPenalty`, `presencePenalty`, and `seed`) override the matching model defaults, including explicit zero values. The Gateway's Chat Completions API maps `top_p`, `frequency_penalty`, and `presence_penalty` to these controls. With `temperature: 0`, OpenClaw still normalizes `top_p` to `1` for greedy sampling after applying overrides. A few keys (`format`, `keep_alive`, `truncate`, `shift`) are forwarded as top-level request fields instead of nested `options`. Local native chat requests default to `truncate: false` and `shift: false`, so supporting servers reject overflowing input instead of silently dropping history. OpenClaw then attempts compaction and retries, or reports the failure. Generation that fills the window can still produce a labeled partial reply. This behavior is verified with Ollama 0.33.3; older servers may ignore the fields. Explicit per-model values override these defaults. Hosted models and the OpenAI-compatible endpoint keep their existing behavior. OpenClaw only forwards these Ollama request keys, so runtime-only params such as `streaming` are never sent to Ollama. Use `params.think` (or `params.thinking`) to set top-level `think`; `false` disables API-level thinking for Qwen-style thinking models.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        models: [          {            id: "llama3.3",            contextWindow: 131072,            contextTokens: 32768,            maxTokens: 65536,            params: {              num_ctx: 32768,              temperature: 0.7,              top_p: 0.9,              thinking: false,            },          }        ]      }    }  }}
[/code]

Per-model `agents.defaults.models["ollama/<model>"].params.num_ctx` also works; the explicit provider model entry wins if both are set.

Thinking control

Native local Ollama compaction summaries default to thinking off. This keeps summarization from using its default three-minute request window for reasoning; Qwen3.5 treats `low` as thinking enabled rather than a reduced thinking budget. An explicit `agents.defaults.compaction.thinkingLevel` overrides this preference. Existing per-model `params.think`/`params.thinking` settings keep their normal precedence. Hosted routes keep their compaction defaults.

OpenClaw forwards thinking as Ollama expects it: top-level `think`, not `options.think`. Auto-discovered models whose `/api/show` reports a `thinking` capability expose `/think low`, `/think medium`, `/think high`, and `/think max`; non-thinking models expose only `/think off`.

When replaying an assistant message, native requests retain its available reasoning in Ollama's separate `thinking` field alongside text and tool calls. This lets tool follow-ups reuse reasoning retained by the session's history policy without mixing it into visible answer text.

bashCopy code
[code]
    openclaw agent --model ollama/gemma4 --thinking offopenclaw agent --model ollama/gemma4 --thinking low
[/code]

Or set a model default:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "ollama/gemma4": {          params: { thinking: "low" },        },      },    },  },}
[/code]

Per-model `params.think`/`params.thinking` can disable or force API thinking for a specific model. OpenClaw preserves that explicit config when the active run only has the implicit `off` default; a non-off runtime command such as `/think medium` still overrides it. A truthy thinking request is never sent to a model explicitly marked `reasoning: false`; a `think: false` request is always sent regardless.

Reasoning models

Models named `deepseek-r1`, `reasoning`, `reason`, or `think` are treated as reasoning-capable by default — no extra config needed:

bashCopy code
[code]
    ollama pull deepseek-r1:32b
[/code]

Model costs

Ollama runs locally and is free, so all model costs are `0` for both auto-discovered and manually defined models.

Memory embeddings

The bundled Ollama plugin registers a memory embedding provider for [memory search](</concepts/memory>). It uses the configured Ollama base URL and API key, calls `/api/embed`, and batches multiple memory chunks into one `input` request when possible.

When `proxy.enabled=true`, embedding requests to the exact host-local loopback origin derived from the configured `baseUrl` use OpenClaw's guarded direct path instead of the managed forward proxy. The configured hostname must itself be `localhost` or a loopback IP literal — DNS names that merely resolve to loopback still use the managed proxy path. LAN, tailnet, private-network, and public Ollama hosts always stay on the managed proxy path, and redirects to another host/port do not inherit trust. `proxy.loopbackMode: "proxy"` routes loopback traffic through the proxy anyway; `proxy.loopbackMode: "block"` denies it before connecting — see [Managed proxy](</security/network-proxy#gateway-loopback-mode>).

Property | Value  
---|---  
Default model | `nomic-embed-text`  
Auto-pull | Yes, if not present locally  
Embedding concurrency | Provider-owned; no memory-search tuning key is required  
  
Query-time embeddings use retrieval prefixes for models that require or recommend them: `nomic-embed-text`, `qwen3-embedding`, and `mxbai-embed-large`. Document batches stay raw, so existing indexes need no format migration.

Embedding concurrency and batching behavior are owned by the Ollama memory provider. For a remote embedding host, use the supported `remote.baseUrl` and `remote.apiKey` fields to keep auth scoped to that host:

json5Copy code
[code]
    {  memory: {    search: {      provider: "ollama",      model: "nomic-embed-text",      remote: {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",      },    },  },}
[/code]

Streaming configuration

Ollama uses the **native API** (`/api/chat`) by default, which supports streaming and tool calling together — no special config needed.

For native requests, thinking control is forwarded directly: `/think off` and `openclaw agent --thinking off` send top-level `think: false` unless an explicit `params.think`/`params.thinking` is configured; `/think low|medium|high` send the matching effort string. Verified full-effort Ollama Cloud families such as GLM 5.2 and DeepSeek V4 also send native `think: "max"` for `/think max`; other models and local servers keep the compatible `think: "high"` mapping.

Was this useful?YesNo

Open issue