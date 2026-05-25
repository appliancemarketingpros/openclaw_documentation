---
title: مصنوعی
source_url: https://docs.openclaw.ai/fa/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) نقاط پایانی سازگار با Anthropic را ارائه می‌کند. OpenClaw آن را به‌عنوان ارائه‌دهنده `synthetic` ثبت می‌کند و از API پیام‌های Anthropic استفاده می‌کند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `synthetic`  
احراز هویت | `SYNTHETIC_API_KEY`  
API | پیام‌های Anthropic  
نشانی پایه | `https://api.synthetic.new/anthropic`  
  
## شروع کار

* ### دریافت کلید API

یک `SYNTHETIC_API_KEY` از حساب Synthetic خود دریافت کنید، یا اجازه دهید راهنمای شروع به کار از شما آن را بخواهد.

* ### اجرای شروع به کار

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### تأیید مدل پیش‌فرض

پس از شروع به کار، مدل پیش‌فرض روی این مقدار تنظیم می‌شود:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## نمونه پیکربندی

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## کاتالوگ داخلی

همه مدل‌های Synthetic از هزینه `0` استفاده می‌کنند (ورودی/خروجی/کش).

شناسه مدل | پنجره زمینه | حداکثر توکن‌ها | استدلال | ورودی  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | خیر | متن  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | بله | متن  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | خیر | متن  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | خیر | متن  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | خیر | متن  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | خیر | متن  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | خیر | متن  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | خیر | متن  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | خیر | متن  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | خیر | متن  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | خیر | متن  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | بله | متن + تصویر  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | خیر | متن  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | خیر | متن  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | خیر | متن  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | خیر | متن + تصویر  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | خیر | متن  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | خیر | متن  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | بله | متن + تصویر  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | خیر | متن  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | بله | متن  
  
فهرست مجاز مدل‌ها

اگر فهرست مجاز مدل‌ها (`agents.defaults.models`) را فعال کنید، هر مدل Synthetic را که قصد استفاده از آن را دارید اضافه کنید. مدل‌هایی که در فهرست مجاز نیستند از agent پنهان خواهند شد.

بازنویسی نشانی پایه

اگر Synthetic نقطه پایانی API خود را تغییر داد، نشانی پایه را در پیکربندی خود بازنویسی کنید:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

به یاد داشته باشید که OpenClaw به‌طور خودکار `/v1` را اضافه می‌کند.

## مرتبط

[**انتخاب مدل** قواعد ارائه‌دهنده، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** طرح‌واره کامل پیکربندی شامل تنظیمات ارائه‌دهنده. ](</fa/gateway/configuration-reference>) [**Synthetic** داشبورد Synthetic و مستندات API. ](<https://synthetic.new>)

Was this useful?YesNo