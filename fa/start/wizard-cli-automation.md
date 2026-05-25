---
title: خودکارسازی CLI
source_url: https://docs.openclaw.ai/fa/start/wizard-cli-automation
scraped_at: 2026-05-25
---

از `--non-interactive` برای خودکارسازی `openclaw onboard` استفاده کنید.

## نمونه پایه غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

برای دریافت خلاصه‌ای قابل خواندن توسط ماشین، `--json` را اضافه کنید.

وقتی خودکارسازی شما فایل‌های workspace را از پیش مقداردهی می‌کند و نمی‌خواهد onboarding فایل‌های bootstrap پیش‌فرض را ایجاد کند، از `--skip-bootstrap` استفاده کنید.

برای ذخیره refهای مبتنی بر env در auth profileها به‌جای مقدارهای plaintext، از `--secret-input-mode ref` استفاده کنید. انتخاب تعاملی بین refهای env و refهای پیکربندی‌شده provider (`file` یا `exec`) در جریان onboarding در دسترس است.

در حالت غیرتعاملی `ref`، متغیرهای env مربوط به provider باید در محیط فرایند تنظیم شده باشند. ارسال flagهای کلید inline بدون متغیر env متناظر اکنون سریعاً با خطا متوقف می‌شود.

مثال:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## نمونه‌های ویژه provider

نمونه کلید API Anthropic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

برای catalog مربوط به Go، به `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` تغییر دهید.

نمونه Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

نمونه provider سفارشی bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` اختیاری است. اگر حذف شود، onboarding مقدار `CUSTOM_API_KEY` را بررسی می‌کند. OpenClaw شناسه‌های رایج مدل vision را به‌طور خودکار دارای قابلیت تصویر علامت‌گذاری می‌کند. برای شناسه‌های vision سفارشی ناشناخته، `--custom-image-input` را اضافه کنید، یا برای اجبار metadata فقط‌متنی از `--custom-text-input` استفاده کنید.

گونه ref-mode:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

در این حالت، onboarding مقدار `apiKey` را به‌صورت `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }` ذخیره می‌کند.

setup-token مربوط به Anthropic همچنان به‌عنوان یک مسیر token پشتیبانی‌شده برای onboarding در دسترس است، اما OpenClaw اکنون در صورت در دسترس بودن، استفاده دوباره از Claude CLI را ترجیح می‌دهد. برای production، کلید API Anthropic را ترجیح دهید.

## افزودن agent دیگر

برای ایجاد agent جداگانه با workspace، sessionها و auth profileهای خودش، از `openclaw agents add <name>` استفاده کنید. اجرا بدون `--workspace`، wizard را راه‌اندازی می‌کند.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

مواردی که تنظیم می‌کند:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


نکات:

  * workspaceهای پیش‌فرض از `~/.openclaw/workspace-<agentId>` پیروی می‌کنند.
  * برای مسیریابی پیام‌های ورودی، `bindings` را اضافه کنید (wizard می‌تواند این کار را انجام دهد).
  * flagهای غیرتعاملی: `--model`، `--agent-dir`، `--bind`، `--non-interactive`.


## مستندات مرتبط

  * هاب onboarding: [Onboarding (CLI)](</fa/start/wizard>)
  * مرجع کامل: [مرجع راه‌اندازی CLI](</fa/start/wizard-cli-reference>)
  * مرجع دستور: [`openclaw onboard`](</fa/cli/onboard>)


Was this useful?YesNo