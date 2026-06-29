---
title: ارائه‌دهنده‌ی llama.cpp
source_url: https://docs.openclaw.ai/fa/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` Plugin رسمی ارائه‌دهندهٔ خارجی برای تعبیه‌های GGUF محلی است. این Plugin مالک وابستگی runtime یعنی `node-llama-cpp` است که توسط `memorySearch.provider: "local"` استفاده می‌شود.

پیش از استفاده از تعبیه‌های حافظهٔ محلی، آن را نصب کنید:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

بستهٔ اصلی npm مربوط به `openclaw` شامل `node-llama-cpp` نیست. نگه داشتن وابستگی بومی در این Plugin باعث می‌شود به‌روزرسانی‌های عادی npm برای OpenClaw یک runtime نصب‌شده به‌صورت دستی را داخل پوشهٔ بستهٔ OpenClaw حذف نکنند.

## پیکربندی

ارائه‌دهندهٔ جست‌وجوی حافظه را روی `local` تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

مدل پیش‌فرض `embeddinggemma-300m-qat-Q8_0.gguf` است. همچنین می‌توانید `local.modelPath` را به یک فایل `.gguf` محلی اشاره دهید.

## Runtime بومی

برای روان‌ترین مسیر نصب بومی، از Node 24 استفاده کنید. checkoutهای سورس که از pnpm استفاده می‌کنند ممکن است لازم باشد وابستگی بومی را تأیید و بازسازی کنند:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

برای تعبیه‌های محلی با اصطکاک کمتر، به‌جای آن از یک ارائه‌دهندهٔ سرویس محلی مانند Ollama یا LM Studio استفاده کنید.

Was this useful?YesNo

Open issue