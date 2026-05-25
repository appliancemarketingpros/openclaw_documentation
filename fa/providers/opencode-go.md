---
title: OpenCode Go
source_url: https://docs.openclaw.ai/fa/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go کاتالوگ Go در [OpenCode](</fa/providers/opencode>) است. از همان `OPENCODE_API_KEY` کاتالوگ Zen استفاده می‌کند، اما شناسهٔ ارائه‌دهندهٔ زمان اجرا `opencode-go` را حفظ می‌کند تا مسیریابی بالادستیِ مختص هر مدل درست بماند.

ویژگی | مقدار  
---|---  
ارائه‌دهندهٔ زمان اجرا | `opencode-go`  
احراز هویت | `OPENCODE_API_KEY`  
راه‌اندازی والد | [OpenCode](</fa/providers/opencode>)  
  
## کاتالوگ داخلی

OpenClaw بیشتر ردیف‌های کاتالوگ Go را از رجیستری مدل Pi بسته‌بندی‌شده می‌گیرد و تا زمانی که رجیستری به‌روز شود، ردیف‌های فعلی بالادستی را تکمیل می‌کند. برای فهرست فعلی مدل‌ها، `openclaw models list --provider opencode-go` را اجرا کنید.

این ارائه‌دهنده شامل موارد زیر است:

ارجاع مدل | نام  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (محدودیت‌های 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## شروع به کار

### تعاملی

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### تنظیم یک مدل Go به‌عنوان پیش‌فرض

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### بررسی در دسترس بودن مدل‌ها

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### غیرتعاملی

* ### ارسال مستقیم کلید

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### بررسی در دسترس بودن مدل‌ها

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## نمونهٔ پیکربندی

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## پیکربندی پیشرفته

رفتار مسیریابی

وقتی ارجاع مدل از `opencode-go/...` استفاده کند، OpenClaw مسیریابی مختص هر مدل را به‌صورت خودکار مدیریت می‌کند. به پیکربندی اضافی برای ارائه‌دهنده نیازی نیست.

قرارداد ارجاع زمان اجرا

ارجاع‌های زمان اجرا صریح می‌مانند: `opencode/...` برای Zen، و `opencode-go/...` برای Go. این کار مسیریابی بالادستیِ مختص هر مدل را در هر دو کاتالوگ درست نگه می‌دارد.

اعتبارنامه‌های مشترک

همان `OPENCODE_API_KEY` توسط هر دو کاتالوگ Zen و Go استفاده می‌شود. وارد کردن کلید هنگام راه‌اندازی، اعتبارنامه‌ها را برای هر دو ارائه‌دهندهٔ زمان اجرا ذخیره می‌کند.

## مرتبط

[**OpenCode (والد)** راه‌اندازی مشترک، نمای کلی کاتالوگ، و یادداشت‌های پیشرفته. ](</fa/providers/opencode>) [**انتخاب مدل** انتخاب ارائه‌دهنده‌ها، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>)

Was this useful?YesNo