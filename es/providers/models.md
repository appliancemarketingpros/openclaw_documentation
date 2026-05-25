---
title: Inicio rápido del proveedor de modelos
source_url: https://docs.openclaw.ai/es/providers/models
scraped_at: 2026-05-25
---

OpenClaw puede usar muchos proveedores de LLM. Elige uno, autentícate y luego configura el modelo predeterminado como `provider/model`.

## Inicio rápido (dos pasos)

  1. Autentícate con el proveedor (normalmente mediante `openclaw onboard`).
  2. Configura el modelo predeterminado:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Proveedores compatibles (conjunto inicial)

  * [Alibaba Model Studio](</es/providers/alibaba>)
  * [Amazon Bedrock](</es/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</es/providers/anthropic>)
  * [BytePlus (internacional)](</es/concepts/model-providers#byteplus-international>)
  * [Chutes](</es/providers/chutes>)
  * [ComfyUI](</es/providers/comfy>)
  * [Cloudflare AI Gateway](</es/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</es/providers/deepinfra>)
  * [fal](</es/providers/fal>)
  * [Fireworks](</es/providers/fireworks>)
  * [modelos GLM](</es/providers/glm>)
  * [MiniMax](</es/providers/minimax>)
  * [Mistral](</es/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</es/providers/moonshot>)
  * [OpenAI (API + Codex)](</es/providers/openai>)
  * [OpenCode (Zen + Go)](</es/providers/opencode>)
  * [OpenRouter](</es/providers/openrouter>)
  * [Qianfan](</es/providers/qianfan>)
  * [Qwen](</es/providers/qwen>)
  * [Runway](</es/providers/runway>)
  * [StepFun](</es/providers/stepfun>)
  * [Synthetic](</es/providers/synthetic>)
  * [Vercel AI Gateway](</es/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</es/providers/venice>)
  * [xAI](</es/providers/xai>)
  * [Z.AI](</es/providers/zai>)


## Variantes adicionales de proveedores incluidas

  * `anthropic-vertex` \- compatibilidad implícita de Anthropic en Google Vertex cuando las credenciales de Vertex están disponibles; no hay una opción de autenticación de incorporación separada
  * `copilot-proxy` \- puente local de VS Code Copilot Proxy; usa `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- flujo OAuth no oficial de Gemini CLI; requiere una instalación local de `gemini` (`brew install gemini-cli` o `npm install -g @google/gemini-cli`); modelo predeterminado `google-gemini-cli/gemini-3-flash-preview`; usa `openclaw onboard --auth-choice google-gemini-cli` o `openclaw models auth login --provider google-gemini-cli --set-default`


Para ver el catálogo completo de proveedores (xAI, Groq, Mistral, etc.) y la configuración avanzada, consulta [proveedores de modelos](</es/concepts/model-providers>).

## Relacionado

  * [Selección de modelo](</es/concepts/model-providers>)
  * [Conmutación por error de modelos](</es/concepts/model-failover>)
  * [CLI de modelos](</es/cli/models>)


Was this useful?YesNo