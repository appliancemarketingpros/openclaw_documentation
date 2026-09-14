---
title: Ollama node-local inference
source_url: https://docs.openclaw.ai/providers/ollama/node-local-inference
scraped_at: 2026-09-14
---

ModelsProviders

## Node-local inference

Agents can delegate a short task to an Ollama model on a paired desktop or server node. The prompt and response cross the existing authenticated Gateway/node connection; the request runs on the node's own loopback Ollama endpoint (`http://127.0.0.1:11434`).

* ### Start Ollama on the node

bashCopy code
[code]
    ollama pull qwen3:0.6bollama list
[/code]

* ### Connect the node host

bashCopy code
[code]
    openclaw node run \  --host <gateway-host> \  --port 18789 \  --display-name "Local inference"
[/code]

Approve the device and its node commands on the Gateway host, then verify:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <deviceRequestId>openclaw nodes pendingopenclaw nodes approve <nodeRequestId>openclaw nodes status --connected
[/code]

A first connection, or an upgrade that adds Ollama commands, can trigger node-command approval. If the node connects without advertising `ollama.models` and `ollama.chat`, check `openclaw nodes pending` again.

* ### Use it from an agent

The bundled Ollama plugin exposes the `node_inference` tool. Agents call `action: "discover"` first, then `action: "run"` with a node and model from that result (`run` can omit the node when exactly one capable node is connected). For example: "Discover the Ollama models on my nodes, then use the fastest loaded model to summarize this text."

Discovery reads `/api/tags`, checks `/api/show` capabilities, and uses `/api/ps` when available to rank already-loaded models first. It returns only local models Ollama reports as chat-capable (`completion` capability) — Ollama Cloud rows and embedding-only models are excluded. Each run disables model thinking and defaults output to 512 tokens (hard cap 8192) unless the tool call requests a different `maxTokens`; some models (for example GPT-OSS) do not support disabling thinking and may still emit reasoning tokens.

To keep Ollama running on a node without exposing it to agents:

bashCopy code
[code]
    openclaw config set plugins.entries.ollama.config.nodeInference.enabled false
[/code]

Restart the node (`openclaw node restart`, or stop/rerun `openclaw node run` for a foreground session). The node stops advertising `ollama.models` and `ollama.chat`; Ollama itself and the Gateway's Ollama provider are unaffected. Set the value back to `true` and restart to re-enable; a changed command surface may need `openclaw nodes pending` approval again after reconnect.

Verify the node commands directly, without an agent turn:

bashCopy code
[code]
    openclaw nodes invoke \  --node "Local inference" \  --command ollama.models \  --params '{}' \  --invoke-timeout 90000 \  --timeout 100000 openclaw nodes invoke \  --node "Local inference" \  --command ollama.chat \  --params '{"model":"qwen3:0.6b","prompt":"Reply with exactly: pong","maxTokens":32,"timeoutMs":120000}' \  --invoke-timeout 130000 \  --timeout 140000
[/code]

`--invoke-timeout` bounds how long the node has to run the command; `--timeout` bounds the overall Gateway call and should be larger.

Node-local inference always uses the node's own loopback endpoint — it does not reuse a configured remote/cloud `models.providers.ollama.baseUrl`. The node commands are available by default on macOS, Linux, and Windows node hosts and remain subject to normal node pairing/command policy.

Was this useful?YesNo

Open issue