---
title: Ollama config recipes
source_url: https://docs.openclaw.ai/providers/ollama/recipes
scraped_at: 2026-09-14
---

ModelsProviders

## Common recipes

Replace model IDs with exact names from `ollama list` or `openclaw models list --provider ollama`.

Local model with auto-discovery

Ollama on the same machine as the Gateway, discovered automatically:

bashCopy code
[code]
    ollama serveollama pull gemma4export OLLAMA_API_KEY="ollama-local"openclaw models list --provider ollamaopenclaw models set ollama/gemma4
[/code]

Leave `models.providers.ollama` unset to use the default local endpoint, or configure a self-hosted endpoint with `models: []` to keep discovery eligible.

LAN Ollama host with manual models json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            reasoning: true,            input: ["text"],            contextTokens: 32768,            params: {              num_ctx: 32768,              thinking: false,              keep_alive: "15m",            },          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/qwen3.5:9b" },    },  },}
[/code]

`contextTokens` caps OpenClaw's active-input budget; `params.num_ctx` sets Ollama's request context. Keep them aligned when hardware cannot run the model's full advertised context.

Ollama Cloud only

No local daemon, hosted models directly:

bashCopy code
[code]
    export OLLAMA_API_KEY="your-ollama-api-key"
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/kimi-k2.5:cloud" },    },  },}
[/code]

For the dedicated `ollama-cloud` provider id instead of this shape, see [Ollama Cloud](</providers/ollama-cloud>).

Cloud plus local through a signed-in daemon bashCopy code
[code]
    ollama signinollama pull gemma4
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        models: [          { id: "gemma4", name: "gemma4", input: ["text"] },          { id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text", "image"] },        ],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama/gemma4",        fallbacks: ["ollama/kimi-k2.5:cloud"],      },    },  },}
[/code]

Multiple Ollama hosts

Custom provider IDs when running more than one Ollama server; each gets its own host, models, auth, and timeout.

json5Copy code
[code]
    {  models: {    providers: {      "ollama-fast": {        baseUrl: "http://mini.local:11434",        apiKey: "ollama-local",        api: "ollama",        models: [          { id: "gemma4", name: "gemma4", input: ["text"], contextTokens: 32768 },        ],      },      "ollama-large": {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 420,        maxTokens: 16384,        models: [          { id: "qwen3.5:27b", name: "qwen3.5:27b", input: ["text"], contextTokens: 131072 },        ],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama-fast/gemma4",        fallbacks: ["ollama-large/qwen3.5:27b"],      },    },  },}
[/code]

OpenClaw strips the active provider prefix (falling back to a bare `ollama/` prefix) before calling Ollama, so `ollama-large/qwen3.5:27b` reaches Ollama as `qwen3.5:27b`.

Small local model profile

Local Ollama models automatically use structured [Tool Search](</tools/tool-search>) when `tools.toolSearch` is unset. This keeps optional capabilities available while loading their schemas only when needed. Setup does not enable lean mode. App, interactive CLI, and non-interactive setup use a 32,768-token runtime context, or the model's native window if smaller. The advertised native window is retained separately; known cloud routes keep their hosted context. Large file reads use OpenClaw's context-based paging. The native adapter preserves those text pages and their continuation instructions; structured fallback data is bounded separately. Bound any explicit context override to what the host can support:

json5Copy code
[code]
    {  agents: {    entries: {      local: {        default: true,        model: { primary: "ollama/gemma4" },      },    },  },  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        models: [          {            id: "gemma4",            name: "gemma4",            input: ["text"],            contextTokens: 32768,            params: { num_ctx: 32768 },          },        ],      },    },  },}
[/code]

Explicit `tools.toolSearch` settings take precedence, including `false`. Tool Search does not change Ollama's context or thinking mode. Ollama thinking defaults to off; an explicit thinking setting can change that independently. If you previously enabled `localModelLean`, set it to `false` to restore optional tools while retaining automatic Tool Search.

Use `compat.supportsTools: false` only when the model or server reliably fails on tool schemas; it disables tool use entirely. For a deliberately narrower agent, prefer `tools.profile` or a per-agent tool policy.

### Model selection

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "ollama/gpt-oss:20b",        fallbacks: ["ollama/llama3.3", "ollama/qwen2.5-coder:32b"],      },    },  },}
[/code]

Custom provider ids work the same way: for a ref using the active provider prefix, such as `ollama-spark/qwen3:32b`, OpenClaw strips that prefix before calling Ollama, sending `qwen3:32b`.

For slow local models, prefer provider-scoped tuning before raising the whole agent runtime timeout:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

`timeoutSeconds` covers the model HTTP request: connection setup, headers, body streaming, and the total guarded-fetch abort. `params.keep_alive` is forwarded as top-level `keep_alive` on native `/api/chat` requests; set it per model when first-turn load time is the bottleneck.

### Quick verification

bashCopy code
[code]
    # Ollama daemon visible to this machinecurl http://127.0.0.1:11434/api/tags # OpenClaw catalog and selected modelopenclaw models list --provider ollamaopenclaw models status # Direct model smokeopenclaw infer model run \  --model ollama/gemma4 \  --prompt "Reply with exactly: ok"
[/code]

For remote hosts, replace `127.0.0.1` with the `baseUrl` host. If `curl` works but OpenClaw does not, check whether the Gateway runs on a different machine, container, or service account.

Was this useful?YesNo

Open issue