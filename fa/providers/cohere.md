---
title: Cohere
source_url: https://docs.openclaw.ai/fa/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) استنتاج سازگار با OpenAI را از طریق API سازگاری خود فراهم می‌کند. OpenClaw در دوره انتقال به خارجی‌سازی، ارائه‌دهنده Cohere را همراه خود عرضه می‌کند و همچنین آن را به‌عنوان یک Plugin خارجی رسمی با کاتالوگ مدل Command A منتشر می‌کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `cohere`  
Plugin | همراه در دوره انتقال؛ بسته خارجی رسمی  
متغیر محیطی احراز هویت | `COHERE_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice cohere-api-key`  
پرچم مستقیم CLI | `--cohere-api-key <key>`  
API | سازگار با OpenAI (`openai-completions`)  
URL پایه | `https://api.cohere.ai/compatibility/v1`  
مدل پیش‌فرض | `cohere/command-a-03-2025`  
  
## شروع کنید

  1. Cohere در بسته‌های فعلی OpenClaw گنجانده شده است. اگر در دسترس نیست، بسته خارجی را نصب کنید و Gateway را دوباره راه‌اندازی کنید:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. یک کلید API برای Cohere ایجاد کنید.
  3. راه‌اندازی اولیه را اجرا کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. تأیید کنید که کاتالوگ در دسترس است:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

مدل پیش‌فرض فقط زمانی تنظیم می‌شود که هیچ مدل اصلی‌ای از قبل پیکربندی نشده باشد.

## راه‌اندازی فقط با محیط

`COHERE_API_KEY` را در اختیار فرایند Gateway قرار دهید، سپس مدل Cohere را انتخاب کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## مرتبط

  * [ارائه‌دهندگان مدل](</fa/concepts/model-providers>)
  * [CLI مدل‌ها](</fa/cli/models>)
  * [فهرست ارائه‌دهندگان](</fa/providers>)


Was this useful?YesNo

Open issue