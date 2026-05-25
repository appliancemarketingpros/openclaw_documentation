---
title: پراکسی API Claude Max
source_url: https://docs.openclaw.ai/fa/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** یک ابزار جامعه‌محور است که اشتراک Claude Max/Pro شما را به‌صورت یک نقطه پایانی API سازگار با OpenAI ارائه می‌کند. این امکان را می‌دهد که از اشتراک خود با هر ابزاری که از قالب OpenAI API پشتیبانی می‌کند استفاده کنید.

## چرا از این استفاده کنیم؟

رویکرد | هزینه | مناسب برای  
---|---|---  
Anthropic API | پرداخت به‌ازای هر توکن (حدود $15/M ورودی، $75/M خروجی برای Opus) | برنامه‌های تولیدی، حجم بالا  
اشتراک Claude Max | $200/ماه ثابت | استفاده شخصی، توسعه، استفاده نامحدود  
  
اگر اشتراک Claude Max دارید و می‌خواهید از آن با ابزارهای سازگار با OpenAI استفاده کنید، این پروکسی ممکن است هزینه برخی گردش‌کارها را کاهش دهد. برای استفاده تولیدی، کلیدهای API همچنان مسیر روشن‌تری از نظر سیاست‌ها هستند.

## چگونه کار می‌کند

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (OpenAI format)              (converts format)      (uses your login)
[/code]

پروکسی:

  1. درخواست‌های قالب OpenAI را در `http://localhost:3456/v1/chat/completions` می‌پذیرد
  2. آن‌ها را به فرمان‌های Claude Code CLI تبدیل می‌کند
  3. پاسخ‌ها را در قالب OpenAI برمی‌گرداند (جریان‌دهی پشتیبانی می‌شود)


## شروع به کار

* ### Install the proxy

به Node.js 20+ و Claude Code CLI نیاز دارد.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Start the server

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Test the proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configure OpenClaw

OpenClaw را به‌عنوان یک نقطه پایانی سفارشی سازگار با OpenAI به پروکسی متصل کنید:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## کاتالوگ داخلی

شناسه مدل | نگاشت می‌شود به  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## پیکربندی پیشرفته

Proxy-style OpenAI-compatible notes

این مسیر از همان مسیر سازگار با OpenAI به سبک پروکسی استفاده می‌کند که سایر پشتیبان‌های سفارشی `/v1` استفاده می‌کنند:

  * شکل‌دهی درخواست مخصوص OpenAI بومی اعمال نمی‌شود
  * بدون `service_tier`، بدون `store` در Responses، بدون راهنمایی‌های prompt-cache، و بدون شکل‌دهی payload سازگار با استدلال OpenAI
  * هدرهای پنهان انتساب OpenClaw (`originator`، `version`، `User-Agent`) روی URL پروکسی تزریق نمی‌شوند

Auto-start on macOS with LaunchAgent

برای اجرای خودکار پروکسی یک LaunchAgent ایجاد کنید:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## پیوندها

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## یادداشت‌ها

  * این یک **ابزار جامعه‌محور** است و به‌صورت رسمی توسط Anthropic یا OpenClaw پشتیبانی نمی‌شود
  * به یک اشتراک فعال Claude Max/Pro با Claude Code CLI احراز هویت‌شده نیاز دارد
  * پروکسی به‌صورت محلی اجرا می‌شود و داده‌ها را به هیچ سرور شخص ثالثی ارسال نمی‌کند
  * پاسخ‌های جریانی به‌طور کامل پشتیبانی می‌شوند


## مرتبط

[**Anthropic provider** یکپارچه‌سازی بومی OpenClaw با Claude CLI یا کلیدهای API. ](</fa/providers/anthropic>) [**OpenAI provider** برای اشتراک‌های OpenAI/Codex. ](</fa/providers/openai>) [**Model selection** نمای کلی همه ارائه‌دهنده‌ها، ارجاع‌های مدل، و رفتار جایگزینی هنگام خرابی. ](</fa/concepts/model-providers>) [**Configuration** مرجع کامل پیکربندی. ](</fa/gateway/configuration>)

Was this useful?YesNo