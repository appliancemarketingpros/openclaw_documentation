---
title: شروع سریع ارائه‌دهندهٔ مدل
source_url: https://docs.openclaw.ai/fa/providers/models
scraped_at: 2026-05-25
---

OpenClaw می‌تواند از بسیاری از ارائه‌دهندگان LLM استفاده کند. یکی را انتخاب کنید، احراز هویت کنید، سپس مدل پیش‌فرض را به صورت `provider/model` تنظیم کنید.

## شروع سریع (دو مرحله)

  1. با ارائه‌دهنده احراز هویت کنید (معمولاً از طریق `openclaw onboard`).
  2. مدل پیش‌فرض را تنظیم کنید:

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

## ارائه‌دهندگان پشتیبانی‌شده (مجموعه آغازین)

  * [Alibaba Model Studio](</fa/providers/alibaba>)
  * [Amazon Bedrock](</fa/providers/bedrock>)
  * [Anthropic (API + Claude CLI)](</fa/providers/anthropic>)
  * [BytePlus (بین‌المللی)](</fa/concepts/model-providers#byteplus-international>)
  * [Chutes](</fa/providers/chutes>)
  * [ComfyUI](</fa/providers/comfy>)
  * [Cloudflare AI Gateway](</fa/providers/cloudflare-ai-gateway>)
  * [DeepInfra](</fa/providers/deepinfra>)
  * [fal](</fa/providers/fal>)
  * [Fireworks](</fa/providers/fireworks>)
  * [مدل‌های GLM](</fa/providers/glm>)
  * [MiniMax](</fa/providers/minimax>)
  * [Mistral](</fa/providers/mistral>)
  * [Moonshot AI (Kimi + Kimi Coding)](</fa/providers/moonshot>)
  * [OpenAI (API + Codex)](</fa/providers/openai>)
  * [OpenCode (Zen + Go)](</fa/providers/opencode>)
  * [OpenRouter](</fa/providers/openrouter>)
  * [Qianfan](</fa/providers/qianfan>)
  * [Qwen](</fa/providers/qwen>)
  * [Runway](</fa/providers/runway>)
  * [StepFun](</fa/providers/stepfun>)
  * [Synthetic](</fa/providers/synthetic>)
  * [Vercel AI Gateway](</fa/providers/vercel-ai-gateway>)
  * [Venice (Venice AI)](</fa/providers/venice>)
  * [xAI](</fa/providers/xai>)
  * [Z.AI](</fa/providers/zai>)


## گونه‌های اضافی ارائه‌دهنده‌های همراه

  * `anthropic-vertex` \- پشتیبانی ضمنی از Anthropic روی Google Vertex زمانی که اعتبارنامه‌های Vertex در دسترس باشند؛ گزینه احراز هویت جداگانه‌ای برای راه‌اندازی اولیه ندارد
  * `copilot-proxy` \- پل محلی VS Code Copilot Proxy؛ از `openclaw onboard --auth-choice copilot-proxy` استفاده کنید
  * `google-gemini-cli` \- جریان غیررسمی OAuth برای Gemini CLI؛ به نصب محلی `gemini` نیاز دارد (`brew install gemini-cli` یا `npm install -g @google/gemini-cli`)؛ مدل پیش‌فرض `google-gemini-cli/gemini-3-flash-preview`؛ از `openclaw onboard --auth-choice google-gemini-cli` یا `openclaw models auth login --provider google-gemini-cli --set-default` استفاده کنید


برای کاتالوگ کامل ارائه‌دهندگان (xAI، Groq، Mistral و غیره) و پیکربندی پیشرفته، [ارائه‌دهندگان مدل](</fa/concepts/model-providers>) را ببینید.

## مرتبط

  * [انتخاب مدل](</fa/concepts/model-providers>)
  * [failover مدل](</fa/concepts/model-failover>)
  * [CLI مدل‌ها](</fa/cli/models>)


Was this useful?YesNo