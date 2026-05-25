---
title: OpenCode
source_url: https://docs.openclaw.ai/fa/providers/opencode
scraped_at: 2026-05-25
---

OpenCode دو کاتالوگ میزبانی‌شده را در OpenClaw ارائه می‌کند:

کاتالوگ | پیشوند | ارائه‌دهنده زمان اجرا  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
هر دو کاتالوگ از یک کلید API یکسان OpenCode استفاده می‌کنند. OpenClaw شناسه‌های ارائه‌دهنده زمان اجرا را جدا نگه می‌دارد تا مسیریابی بالادستی برای هر مدل درست باقی بماند، اما راه‌اندازی اولیه و مستندات آن‌ها را به‌عنوان یک راه‌اندازی OpenCode واحد در نظر می‌گیرند.

## شروع به کار

### Zen catalog

**بهترین برای:** پراکسی چندمدلی گزینش‌شده OpenCode (Claude، GPT، Gemini).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

یا کلید را مستقیماً وارد کنید:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Zen model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**بهترین برای:** مجموعه Kimi، GLM و MiniMax میزبانی‌شده در OpenCode.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

یا کلید را مستقیماً وارد کنید:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Go model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## نمونه پیکربندی

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## کاتالوگ‌های داخلی

### Zen

ویژگی | مقدار  
---|---  
ارائه‌دهنده زمان اجرا | `opencode`  
مدل‌های نمونه | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

ویژگی | مقدار  
---|---  
ارائه‌دهنده زمان اجرا | `opencode-go`  
مدل‌های نمونه | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## پیکربندی پیشرفته

API key aliases

`OPENCODE_ZEN_API_KEY` نیز به‌عنوان نام مستعار برای `OPENCODE_API_KEY` پشتیبانی می‌شود.

Shared credentials

وارد کردن یک کلید OpenCode در زمان راه‌اندازی، اعتبارنامه‌ها را برای هر دو ارائه‌دهنده زمان اجرا ذخیره می‌کند. لازم نیست هر کاتالوگ را جداگانه راه‌اندازی کنید.

Billing and dashboard

وارد OpenCode می‌شوید، جزئیات صورت‌حساب را اضافه می‌کنید و کلید API خود را کپی می‌کنید. صورت‌حساب و دسترس‌پذیری کاتالوگ از داشبورد OpenCode مدیریت می‌شوند.

Gemini replay behavior

ارجاع‌های OpenCode مبتنی بر Gemini روی مسیر proxy-Gemini باقی می‌مانند، بنابراین OpenClaw پاک‌سازی امضای فکری Gemini را در همان‌جا نگه می‌دارد، بدون اینکه اعتبارسنجی بازپخش بومی Gemini یا بازنویسی‌های راه‌انداز را فعال کند.

Non-Gemini replay behavior

ارجاع‌های OpenCode غیر Gemini سیاست بازپخش حداقلی سازگار با OpenAI را حفظ می‌کنند.

## مرتبط

[**Model selection** انتخاب ارائه‌دهندگان، ارجاع‌های مدل و رفتار جایگزینی. ](</fa/concepts/model-providers>) [**Configuration reference** مرجع کامل پیکربندی برای عامل‌ها، مدل‌ها و ارائه‌دهندگان. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo