---
title: Gateway هوش مصنوعی Cloudflare
source_url: https://docs.openclaw.ai/fa/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway در برابر APIهای ارائه‌دهنده قرار می‌گیرد و به شما امکان می‌دهد تحلیل، کش و کنترل‌ها را اضافه کنید. برای Anthropic، OpenClaw از Anthropic Messages API از طریق نقطه پایانی Gateway شما استفاده می‌کند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `cloudflare-ai-gateway`  
URL پایه | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
مدل پیش‌فرض | `cloudflare-ai-gateway/claude-sonnet-4-6`  
کلید API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (کلید API ارائه‌دهنده شما برای درخواست‌ها از طریق Gateway)  
  
وقتی thinking برای مدل‌های Anthropic Messages فعال باشد، OpenClaw نوبت‌های assistant prefill انتهایی را پیش از ارسال payload از طریق Cloudflare AI Gateway حذف می‌کند. Anthropic پاسخ‌های ازپیش‌پرشده را با extended thinking رد می‌کند، در حالی که prefill عادی بدون thinking همچنان در دسترس می‌ماند.

## شروع به کار

* ### تنظیم کلید API ارائه‌دهنده و جزئیات Gateway

onboarding را اجرا کنید و گزینه احراز هویت Cloudflare AI Gateway را انتخاب کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

این کار شناسه حساب، شناسه Gateway و کلید API شما را درخواست می‌کند.

* ### تنظیم یک مدل پیش‌فرض

مدل را به پیکربندی OpenClaw خود اضافه کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### تأیید در دسترس بودن مدل

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## نمونه غیرتعاملی

برای راه‌اندازی‌های اسکریپتی یا CI، همه مقادیر را در خط فرمان وارد کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## پیکربندی پیشرفته

Gatewayهای احراز هویت‌شده

اگر احراز هویت Gateway را در Cloudflare فعال کرده‌اید، سرآیند `cf-aig-authorization` را اضافه کنید. این مورد **علاوه بر** کلید API ارائه‌دهنده شما است.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

یادداشت محیط

اگر Gateway به‌صورت daemon (launchd/systemd) اجرا می‌شود، مطمئن شوید `CLOUDFLARE_AI_GATEWAY_API_KEY` برای آن فرایند در دسترس است.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهنده‌ها، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**عیب‌یابی** عیب‌یابی عمومی و پرسش‌های متداول. ](</fa/help/troubleshooting>)

Was this useful?YesNo