---
title: Gateway هوش مصنوعی Vercel
source_url: https://docs.openclaw.ai/fa/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) یک API یکپارچه فراهم می‌کند تا از طریق یک endpoint واحد به صدها مدل دسترسی داشته باشید.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `vercel-ai-gateway`  
احراز هویت | `AI_GATEWAY_API_KEY`  
API | سازگار با Anthropic Messages  
کاتالوگ مدل | کشف خودکار از طریق `/v1/models`  
  
## شروع به کار

* ### Set the API key

فرایند onboarding را اجرا کنید و گزینه احراز هویت AI Gateway را انتخاب کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Set a default model

مدل را به پیکربندی OpenClaw خود اضافه کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## نمونه غیرتعاملی

برای راه‌اندازی‌های اسکریپتی یا CI، همه مقادیر را در خط فرمان وارد کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## شکل کوتاه ID مدل

OpenClaw ارجاع‌های کوتاه مدل Vercel Claude را می‌پذیرد و هنگام اجرا آن‌ها را عادی‌سازی می‌کند:

ورودی کوتاه | ارجاع مدل عادی‌سازی‌شده  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## پیکربندی پیشرفته

Environment variable for daemon processes

اگر OpenClaw Gateway به‌صورت daemon اجرا می‌شود (launchd/systemd)، مطمئن شوید `AI_GATEWAY_API_KEY` برای آن فرایند در دسترس است.

Provider routing

Vercel AI Gateway درخواست‌ها را بر اساس پیشوند ارجاع مدل به ارائه‌دهنده بالادستی مسیریابی می‌کند. برای مثال، `vercel-ai-gateway/anthropic/claude-opus-4.6` از طریق Anthropic مسیریابی می‌شود، در حالی که `vercel-ai-gateway/openai/gpt-5.5` از طریق OpenAI و `vercel-ai-gateway/moonshotai/kimi-k2.6` از طریق MoonshotAI مسیریابی می‌شود. تنها `AI_GATEWAY_API_KEY` شما احراز هویت همه ارائه‌دهندگان بالادستی را مدیریت می‌کند.

Thinking levels

گزینه‌های `/think` زمانی که OpenClaw قرارداد ارائه‌دهنده بالادستی را می‌شناسد، از پیشوندهای مدل بالادستی مورد اعتماد پیروی می‌کنند. `vercel-ai-gateway/anthropic/...` از پروفایل تفکر Claude استفاده می‌کند، از جمله پیش‌فرض‌های تطبیقی برای مدل‌های Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`، `gpt-5.5`، و ارجاع‌های سبک Codex، `/think xhigh` را درست مانند ارائه‌دهندگان مستقیم OpenAI/OpenAI Codex ارائه می‌کنند. سایر ارجاع‌های namespaced سطح‌های عادی reasoning را حفظ می‌کنند، مگر اینکه metadata کاتالوگ آن‌ها موارد بیشتری اعلام کند.

## مرتبط

[**Model selection** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**Troubleshooting** عیب‌یابی عمومی و پرسش‌های متداول. ](</fa/help/troubleshooting>)

Was this useful?YesNo