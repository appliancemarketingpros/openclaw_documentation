---
title: Краткое руководство по поставщику моделей
source_url: https://docs.openclaw.ai/ru/providers/models
scraped_at: 2026-06-29
---

ModelsOverview

OpenClaw может использовать множество провайдеров LLM. Выберите одного, выполните аутентификацию, затем задайте модель по умолчанию как `provider/model`.

## Быстрый старт (два шага)

  1. Выполните аутентификацию у провайдера (обычно через `openclaw onboard`).
  2. Задайте модель по умолчанию:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## Поддерживаемые провайдеры (начальный набор)

  * [Alibaba Model Studio](</ru/providers/alibaba>)
  * [Amazon Bedrock](</ru/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</ru/providers/anthropic>)
  * [BytePlus (International)](</ru/concepts/model-providers#byteplus-international>)
  * [Chutes](</ru/providers/chutes>)
  * [Cohere](</ru/providers/cohere>)
  * [ComfyUI](</ru/providers/comfy>)
  * [Cloudflare AI Gateway](</ru/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</ru/providers/deepinfra>)
  * [fal](</ru/providers/fal>)
  * [Fireworks](</ru/providers/fireworks>)
  * [MiniMax](</ru/providers/minimax>)
  * [Mistral](</ru/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</ru/providers/moonshot>)
  * [OpenAI (API + Codex)](</ru/providers/openai>)
  * [OpenCode (Zen + Go)](</ru/providers/opencode>)
  * [OpenRouter](</ru/providers/openrouter>)
  * [Qianfan](</ru/providers/qianfan>)
  * [Qwen](</ru/providers/qwen>)
  * [Runway](</ru/providers/runway>)
  * [StepFun](</ru/providers/stepfun>)
  * [Synthetic](</ru/providers/synthetic>)
  * [Vercel AI Gateway](</ru/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</ru/providers/venice>)
  * [xAI](</ru/providers/xai>)
  * [Z.AI (GLM)](</ru/providers/zai>)


## Дополнительные варианты провайдеров

  * `anthropic-vertex` \- установите `@openclaw/anthropic-vertex-provider` для неявной поддержки Anthropic в Google Vertex, когда доступны учетные данные Vertex; отдельный вариант аутентификации при онбординге не требуется
  * `copilot-proxy` \- локальный мост VS Code Copilot Proxy; используйте `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- неофициальный OAuth-поток Gemini CLI; требует локальной установки `gemini` (`brew install gemini-cli` или `npm install -g @google/gemini-cli`); модель по умолчанию `google-gemini-cli/gemini-3-flash-preview`; используйте `openclaw onboard --auth-choice google-gemini-cli` или `openclaw models auth login --provider google-gemini-cli --set-default`


Полный каталог провайдеров (xAI, Groq, Mistral и т. д.) и расширенную конфигурацию см. в разделе [Провайдеры моделей](</ru/concepts/model-providers>).

## Связанные материалы

  * [Выбор модели](</ru/concepts/model-providers>)
  * [Резервное переключение моделей](</ru/concepts/model-failover>)
  * [CLI моделей](</ru/cli/models>)


Was this useful?YesNo

Open issue