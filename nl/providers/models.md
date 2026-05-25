---
title: Snelstartgids voor modelproviders
source_url: https://docs.openclaw.ai/nl/providers/models
scraped_at: 2026-05-25
---

OpenClaw kan veel LLM-providers gebruiken. Kies er één, authenticeer en stel vervolgens het standaardmodel in als `provider/model`.

## Snelstart (twee stappen)

  1. Authenticeer bij de provider (meestal via `openclaw onboard`).
  2. Stel het standaardmodel in:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Ondersteunde providers (startset)

  * [Alibaba Model Studio](</nl/providers/alibaba>)
  * [Amazon Bedrock](</nl/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</nl/providers/anthropic>)
  * [BytePlus (Internationaal)](</nl/concepts/model-providers#byteplus-international>)
  * [Chutes](</nl/providers/chutes>)
  * [ComfyUI](</nl/providers/comfy>)
  * [Cloudflare AI Gateway](</nl/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</nl/providers/deepinfra>)
  * [fal](</nl/providers/fal>)
  * [Fireworks](</nl/providers/fireworks>)
  * [GLM-modellen](</nl/providers/glm>)
  * [MiniMax](</nl/providers/minimax>)
  * [Mistral](</nl/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</nl/providers/moonshot>)
  * [OpenAI (API + Codex)](</nl/providers/openai>)
  * [OpenCode (Zen + Go)](</nl/providers/opencode>)
  * [OpenRouter](</nl/providers/openrouter>)
  * [Qianfan](</nl/providers/qianfan>)
  * [Qwen](</nl/providers/qwen>)
  * [Runway](</nl/providers/runway>)
  * [StepFun](</nl/providers/stepfun>)
  * [Synthetic](</nl/providers/synthetic>)
  * [Vercel AI Gateway](</nl/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</nl/providers/venice>)
  * [xAI](</nl/providers/xai>)
  * [Z.AI](</nl/providers/zai>)


## Aanvullende gebundelde providervarianten

  * `anthropic-vertex` \- impliciete Anthropic op Google Vertex-ondersteuning wanneer Vertex-referenties beschikbaar zijn; geen afzonderlijke authenticatiekeuze voor onboarding
  * `copilot-proxy` \- lokale VS Code Copilot Proxy-brug; gebruik `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- onofficiële Gemini CLI OAuth-flow; vereist een lokale `gemini`-installatie (`brew install gemini-cli` of `npm install -g @google/gemini-cli`); standaardmodel `google-gemini-cli/gemini-3-flash-preview`; gebruik `openclaw onboard --auth-choice google-gemini-cli` of `openclaw models auth login --provider google-gemini-cli --set-default`


Voor de volledige providercatalogus (xAI, Groq, Mistral, enzovoort) en geavanceerde configuratie, zie [Modelproviders](</nl/concepts/model-providers>).

## Gerelateerd

  * [Modelselectie](</nl/concepts/model-providers>)
  * [Modelfailover](</nl/concepts/model-failover>)
  * [Modellen-CLI](</nl/cli/models>)


Was this useful?YesNo