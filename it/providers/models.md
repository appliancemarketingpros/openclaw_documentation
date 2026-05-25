---
title: Guida rapida al fornitore di modelli
source_url: https://docs.openclaw.ai/it/providers/models
scraped_at: 2026-05-25
---

OpenClaw può usare molti provider LLM. Scegline uno, autenticati, quindi imposta il modello predefinito come `provider/model`.

## Avvio rapido (due passaggi)

  1. Autenticati con il provider (di solito tramite `openclaw onboard`).
  2. Imposta il modello predefinito:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Provider supportati (set iniziale)

  * [Alibaba Model Studio](</it/providers/alibaba>)
  * [Amazon Bedrock](</it/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</it/providers/anthropic>)
  * [BytePlus (International)](</it/concepts/model-providers#byteplus-international>)
  * [Chutes](</it/providers/chutes>)
  * [ComfyUI](</it/providers/comfy>)
  * [Cloudflare AI Gateway](</it/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</it/providers/deepinfra>)
  * [fal](</it/providers/fal>)
  * [Fireworks](</it/providers/fireworks>)
  * [modelli GLM](</it/providers/glm>)
  * [MiniMax](</it/providers/minimax>)
  * [Mistral](</it/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</it/providers/moonshot>)
  * [OpenAI (API + Codex)](</it/providers/openai>)
  * [OpenCode (Zen + Go)](</it/providers/opencode>)
  * [OpenRouter](</it/providers/openrouter>)
  * [Qianfan](</it/providers/qianfan>)
  * [Qwen](</it/providers/qwen>)
  * [Runway](</it/providers/runway>)
  * [StepFun](</it/providers/stepfun>)
  * [Synthetic](</it/providers/synthetic>)
  * [Vercel AI Gateway](</it/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</it/providers/venice>)
  * [xAI](</it/providers/xai>)
  * [Z.AI](</it/providers/zai>)


## Varianti aggiuntive di provider incluse

  * `anthropic-vertex` \- supporto implicito Anthropic su Google Vertex quando sono disponibili le credenziali Vertex; nessuna scelta di autenticazione di onboarding separata
  * `copilot-proxy` \- bridge locale VS Code Copilot Proxy; usa `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- flusso OAuth non ufficiale di Gemini CLI; richiede un'installazione locale di `gemini` (`brew install gemini-cli` o `npm install -g @google/gemini-cli`); modello predefinito `google-gemini-cli/gemini-3-flash-preview`; usa `openclaw onboard --auth-choice google-gemini-cli` o `openclaw models auth login --provider google-gemini-cli --set-default`


Per il catalogo completo dei provider (xAI, Groq, Mistral, ecc.) e la configurazione avanzata, consulta [Provider di modelli](</it/concepts/model-providers>).

## Correlati

  * [Selezione del modello](</it/concepts/model-providers>)
  * [Failover del modello](</it/concepts/model-failover>)
  * [CLI dei modelli](</it/cli/models>)


Was this useful?YesNo