---
title: Início rápido do provedor de modelo
source_url: https://docs.openclaw.ai/pt-BR/providers/models
scraped_at: 2026-05-25
---

OpenClaw pode usar muitos provedores de LLM. Escolha um, autentique-se e então defina o modelo padrão como `provider/model`.

## Início rápido (duas etapas)

  1. Autentique-se com o provedor (geralmente via `openclaw onboard`).
  2. Defina o modelo padrão:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Provedores compatíveis (conjunto inicial)

  * [Alibaba Model Studio](</pt-BR/providers/alibaba>)
  * [Amazon Bedrock](</pt-BR/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</pt-BR/providers/anthropic>)
  * [BytePlus (International)](</pt-BR/concepts/model-providers#byteplus-international>)
  * [Chutes](</pt-BR/providers/chutes>)
  * [ComfyUI](</pt-BR/providers/comfy>)
  * [Cloudflare AI Gateway](</pt-BR/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</pt-BR/providers/deepinfra>)
  * [fal](</pt-BR/providers/fal>)
  * [Fireworks](</pt-BR/providers/fireworks>)
  * [modelos GLM](</pt-BR/providers/glm>)
  * [MiniMax](</pt-BR/providers/minimax>)
  * [Mistral](</pt-BR/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</pt-BR/providers/moonshot>)
  * [OpenAI (API + Codex)](</pt-BR/providers/openai>)
  * [OpenCode (Zen + Go)](</pt-BR/providers/opencode>)
  * [OpenRouter](</pt-BR/providers/openrouter>)
  * [Qianfan](</pt-BR/providers/qianfan>)
  * [Qwen](</pt-BR/providers/qwen>)
  * [Runway](</pt-BR/providers/runway>)
  * [StepFun](</pt-BR/providers/stepfun>)
  * [Synthetic](</pt-BR/providers/synthetic>)
  * [Vercel AI Gateway](</pt-BR/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</pt-BR/providers/venice>)
  * [xAI](</pt-BR/providers/xai>)
  * [Z.AI](</pt-BR/providers/zai>)


## Variantes adicionais de provedores incluídas

  * `anthropic-vertex` \- suporte implícito ao Anthropic no Google Vertex quando as credenciais do Vertex estão disponíveis; sem opção separada de autenticação no onboarding
  * `copilot-proxy` \- ponte local do VS Code Copilot Proxy; use `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- fluxo OAuth não oficial da Gemini CLI; requer uma instalação local de `gemini` (`brew install gemini-cli` ou `npm install -g @google/gemini-cli`); modelo padrão `google-gemini-cli/gemini-3-flash-preview`; use `openclaw onboard --auth-choice google-gemini-cli` ou `openclaw models auth login --provider google-gemini-cli --set-default`


Para o catálogo completo de provedores (xAI, Groq, Mistral etc.) e configuração avançada, consulte [Provedores de modelos](</pt-BR/concepts/model-providers>).

## Relacionados

  * [Seleção de modelos](</pt-BR/concepts/model-providers>)
  * [Failover de modelos](</pt-BR/concepts/model-failover>)
  * [CLI de modelos](</pt-BR/cli/models>)


Was this useful?YesNo