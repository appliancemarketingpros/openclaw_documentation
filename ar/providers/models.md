---
title: بدء سريع لموفّر النماذج
source_url: https://docs.openclaw.ai/ar/providers/models
scraped_at: 2026-05-25
---

يمكن لـ OpenClaw استخدام العديد من مزوّدي LLM. اختر واحدًا، ثم صادق، ثم اضبط النموذج الافتراضي بصيغة `provider/model`.

## البدء السريع (خطوتان)

  1. صادق مع المزوّد (عادةً عبر `openclaw onboard`).
  2. اضبط النموذج الافتراضي:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## المزوّدون المدعومون (مجموعة البداية)

  * [Alibaba Model Studio](</ar/providers/alibaba>)
  * [Amazon Bedrock](</ar/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</ar/providers/anthropic>)
  * [BytePlus (دولي)](</ar/concepts/model-providers#byteplus-international>)
  * [Chutes](</ar/providers/chutes>)
  * [ComfyUI](</ar/providers/comfy>)
  * [Cloudflare AI Gateway](</ar/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</ar/providers/deepinfra>)
  * [fal](</ar/providers/fal>)
  * [Fireworks](</ar/providers/fireworks>)
  * [نماذج GLM](</ar/providers/glm>)
  * [MiniMax](</ar/providers/minimax>)
  * [Mistral](</ar/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</ar/providers/moonshot>)
  * [OpenAI (API + Codex)](</ar/providers/openai>)
  * [OpenCode (Zen + Go)](</ar/providers/opencode>)
  * [OpenRouter](</ar/providers/openrouter>)
  * [Qianfan](</ar/providers/qianfan>)
  * [Qwen](</ar/providers/qwen>)
  * [Runway](</ar/providers/runway>)
  * [StepFun](</ar/providers/stepfun>)
  * [Synthetic](</ar/providers/synthetic>)
  * [Vercel AI Gateway](</ar/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</ar/providers/venice>)
  * [xAI](</ar/providers/xai>)
  * [Z.AI](</ar/providers/zai>)


## صيغ إضافية مجمّعة للمزوّدين

  * `anthropic-vertex` \- دعم Anthropic الضمني على Google Vertex عند توفر بيانات اعتماد Vertex؛ لا يوجد اختيار مصادقة إعداد أولي منفصل
  * `copilot-proxy` \- جسر محلي إلى VS Code Copilot Proxy؛ استخدم `openclaw onboard --auth-choice copilot-proxy`
  * `google-gemini-cli` \- تدفق OAuth غير رسمي لـ Gemini CLI؛ يتطلب تثبيت `gemini` محليًا (`brew install gemini-cli` أو `npm install -g @google/gemini-cli`)؛ النموذج الافتراضي `google-gemini-cli/gemini-3-flash-preview`؛ استخدم `openclaw onboard --auth-choice google-gemini-cli` أو `openclaw models auth login --provider google-gemini-cli --set-default`


للاطلاع على كتالوج المزوّدين الكامل (xAI وGroq وMistral وغيرها) والإعدادات المتقدمة، راجع [مزوّدي النماذج](</ar/concepts/model-providers>).

## ذات صلة

  * [اختيار النموذج](</ar/concepts/model-providers>)
  * [تجاوز فشل النموذج](</ar/concepts/model-failover>)
  * [Models CLI](</ar/cli/models>)


Was this useful?YesNo