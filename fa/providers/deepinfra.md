---
title: DeepInfra
source_url: https://docs.openclaw.ai/fa/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra یک **API یکپارچه** ارائه می‌دهد که درخواست‌ها را پشت یک نقطه پایانی و کلید API واحد، به محبوب‌ترین مدل‌های متن‌باز و پیشرو هدایت می‌کند. با OpenAI سازگار است، بنابراین بیشتر SDKهای OpenAI با تغییر نشانی پایه کار می‌کنند.

## دریافت کلید API

  1. به <https://deepinfra.com/> بروید
  2. وارد شوید یا یک حساب بسازید
  3. به Dashboard / Keys بروید و یک کلید API جدید بسازید یا از کلید خودکار ساخته‌شده استفاده کنید


## راه‌اندازی CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

یا متغیر محیطی را تنظیم کنید:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## قطعه پیکربندی

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## سطوح پشتیبانی‌شده OpenClaw

Plugin همراه، همه سطوح DeepInfra را که با قراردادهای فعلی ارائه‌دهنده OpenClaw مطابقت دارند ثبت می‌کند:

سطح | مدل پیش‌فرض | پیکربندی/ابزار OpenClaw  
---|---|---  
ارائه‌دهنده چت / مدل | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
تولید/ویرایش تصویر | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
درک رسانه | `moonshotai/Kimi-K2.5` برای تصاویر | درک تصویر ورودی  
گفتار به متن | `openai/whisper-large-v3-turbo` | رونویسی صوت ورودی  
متن به گفتار | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
تولید ویدیو | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
embeddingهای حافظه | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra همچنین بازرتبه‌بندی، دسته‌بندی، تشخیص شیء و انواع مدل بومی دیگر را نیز ارائه می‌کند. OpenClaw در حال حاضر برای این دسته‌ها قراردادهای ارائه‌دهنده سطح اول ندارد، بنابراین این Plugin هنوز آن‌ها را ثبت نمی‌کند.

## مدل‌های موجود

OpenClaw هنگام راه‌اندازی، مدل‌های موجود DeepInfra را به‌صورت پویا کشف می‌کند. برای دیدن فهرست کامل مدل‌های موجود، از `/models deepinfra` استفاده کنید.

هر مدلی که در [DeepInfra.com](<https://deepinfra.com/>) موجود باشد می‌تواند با پیشوند `deepinfra/` استفاده شود:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## نکته‌ها

  * ارجاع‌های مدل به شکل `deepinfra/<provider>/<model>` هستند (برای مثال، `deepinfra/Qwen/Qwen3-Max`).
  * مدل پیش‌فرض: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * نشانی پایه: `https://api.deepinfra.com/v1/openai`
  * تولید ویدیوی بومی از `https://api.deepinfra.com/v1/inference/<model>` استفاده می‌کند.


## مرتبط

  * [ارائه‌دهندگان مدل](</fa/concepts/model-providers>)
  * [همه ارائه‌دهندگان](</fa/providers>)


Was this useful?YesNo