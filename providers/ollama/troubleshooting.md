---
title: Ollama troubleshooting
source_url: https://docs.openclaw.ai/providers/ollama/troubleshooting
scraped_at: 2026-09-14
---

ModelsProviders

## Troubleshooting

WSL2 crash loop (repeated reboots)

On WSL2 with NVIDIA/CUDA, the official Ollama Linux installer creates an `ollama.service` systemd unit with `Restart=always`. If that service autostarts and loads a GPU-backed model during WSL2 boot, Ollama can pin host memory while loading; Hyper-V memory reclaim cannot always reclaim those pages, so Windows can terminate the WSL2 VM, systemd restarts Ollama, and the loop repeats.

Evidence: repeated WSL2 reboots/terminations, high CPU in `app.slice` or `ollama.service` right after WSL2 startup, and SIGTERM from systemd rather than the Linux OOM killer.

OpenClaw logs a startup warning when it detects WSL2, `ollama.service` enabled with `Restart=always`, and visible CUDA markers.

Mitigation:

bashCopy code
[code]
    sudo systemctl disable ollama
[/code]

On the Windows side, add this to `%USERPROFILE%\.wslconfig`, then run `wsl --shutdown`:

iniCopy code
[code]
    [experimental]autoMemoryReclaim=disabled
[/code]

Or shorten keep-alive / start Ollama manually only when needed:

bashCopy code
[code]
    export OLLAMA_KEEP_ALIVE=5mollama serve
[/code]

See [ollama/ollama#11317](<https://github.com/ollama/ollama/issues/11317>).

Ollama not detected

Confirm Ollama is running and is in the agent's model scope. For ambient localhost discovery, set `OLLAMA_API_KEY` (or an auth profile). A nonempty manual model list skips discovery; an explicit self-hosted endpoint with `models: []` does not:

bashCopy code
[code]
    ollama servecurl http://localhost:11434/api/tags
[/code]

No models available

Pull the model locally, or define it explicitly in `models.providers.ollama`:

bashCopy code
[code]
    ollama list  # See what's installedollama pull gemma4ollama pull gpt-oss:20bollama pull llama3.3     # Or another model
[/code]

Connection refused bashCopy code
[code]
    # Check if Ollama is runningps aux | grep ollama # Or restart Ollamaollama serve
[/code]

Remote host works with curl but not OpenClaw

Verify from the same machine and runtime that runs the Gateway:

bashCopy code
[code]
    openclaw gateway status --deepcurl http://ollama-host:11434/api/tags
[/code]

Common causes:

  * `baseUrl` points at `localhost`, but the Gateway runs in Docker or on another host.
  * The URL uses `/v1`, selecting OpenAI-compatible behavior instead of native Ollama.
  * The remote host needs firewall or LAN binding changes.
  * The model is on your laptop's daemon but not the remote one.

Model outputs tool JSON as text

Usually the provider is in OpenAI-compatible mode, or the model cannot handle tool schemas. Prefer native mode:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",        api: "ollama",      },    },  },}
[/code]

If a small local model still fails on tool schemas, set `compat.supportsTools: false` on that model entry and retest.

Kimi or GLM returns garbled symbols

Hosted Kimi/GLM responses that are long, non-linguistic symbol runs are treated as a failed provider call rather than a successful reply, so normal retry/fallback/error handling takes over instead of persisting corrupted text into the session.

If it recurs, capture the model name, the current session file, and whether the run used `Cloud + Local` or `Cloud only`, then try a fresh session and a fallback model:

bashCopy code
[code]
    openclaw infer model run --model ollama/kimi-k2.5:cloud --prompt "Reply with exactly: ok" --jsonopenclaw models set ollama/gemma4
[/code]

Cold local model times out

Large local models can need a long first load. Scope the timeout to the Ollama provider and optionally keep the model loaded between turns:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

If the host itself is slow to accept connections, `timeoutSeconds` also extends the guarded connect timeout for this provider.

Large-context model is too slow or runs out of memory

Many models advertise contexts larger than your hardware can run comfortably. Native requests forward the effective `contextTokens` unless `params.num_ctx` overrides it. Cap both OpenClaw's budget and Ollama's request context for predictable first-token latency:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            contextTokens: 32768,            params: { num_ctx: 32768, thinking: false },          },        ],      },    },  },}
[/code]

Lower the model entry's `contextTokens` if OpenClaw sends too much prompt. Lower `params.num_ctx` if Ollama's runtime context is too large for the machine. Lower `maxTokens` if generation runs too long.

Was this useful?YesNo

Open issue