---
title: Ollama Cloud
source_url: https://docs.openclaw.ai/fa/providers/ollama-cloud
scraped_at: 2026-06-29
---

ModelsProviders

Ollama Cloud، API مدل میزبانی‌شده Ollama است. این به OpenClaw امکان می‌دهد مدل‌های میزبانی‌شده Ollama را مستقیماً فراخوانی کند، بدون نصب سرور محلی Ollama یا وارد کردن برنامه محلی Ollama به حالت ابری. از شناسه ارائه‌دهنده `ollama-cloud` و ارجاع‌های مدل مانند `ollama-cloud/kimi-k2.6` استفاده کنید.

این صفحه برای مسیریابی مستقیم فقط ابری است. ارائه‌دهنده از سبک بومی `/api/chat` در Ollama استفاده می‌کند، نه مسیر سازگار با OpenAI یعنی `/v1`. OpenClaw آن را به‌عنوان یک شناسه ارائه‌دهنده جداگانه ثبت می‌کند تا اعتبارنامه‌های فقط ابری، کشف زنده کاتالوگ، و انتخاب مدل با میزبان محلی `ollama` مخلوط نشوند.

وقتی مسیریابی فقط ابری می‌خواهید از این صفحه استفاده کنید. برای Ollama محلی، مسیریابی ترکیبی ابری-به‌علاوه-محلی، embeddings، و جزئیات میزبان سفارشی، به [Ollama](</fa/providers/ollama>) مراجعه کنید.

## راه‌اندازی

یک کلید API برای Ollama Cloud در [ollama.com/settings/keys](<https://ollama.com/settings/keys>) بسازید، سپس اجرا کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice ollama-cloud
[/code]

یا تنظیم کنید:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret
[/code]

## پیش‌فرض‌ها

  * ارائه‌دهنده: `ollama-cloud`
  * URL پایه: `https://ollama.com`
  * متغیر محیطی: `OLLAMA_API_KEY`
  * سبک API: بومی Ollama `/api/chat`
  * مدل نمونه: `ollama-cloud/kimi-k2.6`


## چه زمانی Ollama Cloud را انتخاب کنید

  * مدل‌های میزبانی‌شده Ollama را بدون اجرای محلی `ollama serve` می‌خواهید.
  * همان شکل API گفت‌وگوی بومی Ollama را می‌خواهید که OpenClaw برای Ollama محلی استفاده می‌کند، اما به `https://ollama.com` اشاره کند.
  * یک مسیر ابری ساده برای مدل‌هایی می‌خواهید که از قبل در کاتالوگ میزبانی‌شده Ollama هستند.
  * به دریافت مدل محلی، کنترل GPU محلی، یا استنتاج فقط LAN نیاز ندارید.


وقتی مسیریابی فقط محلی یا ابری-به‌علاوه-محلی از طریق میزبان Ollama واردشده می‌خواهید، به‌جای آن از [Ollama](</fa/providers/ollama>) استفاده کنید. وقتی به معناشناسی `/v1/chat/completions` یا ویژگی‌های سازگار با OpenAI و ویژه ارائه‌دهنده نیاز دارید، به‌جای آن از یک ارائه‌دهنده سازگار با OpenAI استفاده کنید.

## مدل‌ها

OpenClaw مدل‌های Ollama Cloud را از کاتالوگ زنده میزبانی‌شده کشف می‌کند. شناسه‌های میزبانی‌شده رایج شامل این‌ها هستند:

  * `ollama-cloud/gpt-oss:20b`
  * `ollama-cloud/kimi-k2.6`
  * `ollama-cloud/deepseek-v4-flash`
  * `ollama-cloud/minimax-m2.7`
  * `ollama-cloud/glm-5`


از شناسه مدلی از کاتالوگ میزبانی‌شده فعلی خود استفاده کنید:

bashCopy code
[code]
    openclaw models list --provider ollama-cloudopenclaw models set ollama-cloud/kimi-k2.6
[/code]

شناسه‌های مدل، شناسه‌های کاتالوگ ابری هستند، نه نام‌های دریافت محلی. اگر نام مدلی در یک میزبان محلی Ollama کار می‌کند اما در کاتالوگ میزبانی‌شده وجود ندارد، به‌جای آن از ارائه‌دهنده `ollama` با همان میزبان محلی استفاده کنید.

## آزمون زنده

برای آزمون‌های سریع کلید API در Ollama Cloud، آزمون زنده Ollama را به نقطه پایانی میزبانی‌شده اشاره دهید و مدلی از کاتالوگ فعلی خود انتخاب کنید:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_OLLAMA=1 \OPENCLAW_LIVE_OLLAMA_BASE_URL=https://ollama.com \OPENCLAW_LIVE_OLLAMA_MODEL=kimi-k2.6 \OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=1 \pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

آزمون سریع ابری متن، stream بومی، و جست‌وجوی وب را اجرا می‌کند. به‌طور پیش‌فرض embeddings را برای `https://ollama.com` رد می‌کند، زیرا کلیدهای API Ollama Cloud ممکن است مجوز `/api/embed` را ندهند.

## عیب‌یابی

  * خطاهای `Set OLLAMA_API_KEY`: یک کلید API ابری واقعی ارائه کنید. نشانگر محلی `ollama-local` فقط برای میزبان‌های محلی یا خصوصی Ollama است.
  * خطاهای مدل ناشناخته: `openclaw models list --provider ollama-cloud` را اجرا کنید و شناسه مدل میزبانی‌شده را دقیقاً کپی کنید.
  * مشکلات tool-call یا JSON خام روی میزبان‌های سفارشی Ollama: بررسی کنید که به‌اشتباه از URL سازگار با OpenAI یعنی `/v1` استفاده نکرده باشید. مسیرهای Ollama باید از URL پایه بومی بدون پسوند `/v1` استفاده کنند.


## مرتبط

  * [Ollama](</fa/providers/ollama>)
  * [ارائه‌دهندگان مدل](</fa/concepts/model-providers>)
  * [همه ارائه‌دهندگان](</fa/providers>)


Was this useful?YesNo

Open issue