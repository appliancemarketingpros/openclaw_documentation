---
title: Together AI
source_url: https://docs.openclaw.ai/fa/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) دسترسی به مدل‌های متن‌باز پیشرو، از جمله Llama، DeepSeek، Kimi و موارد دیگر را از طریق یک API یکپارچه فراهم می‌کند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `together`  
احراز هویت | `TOGETHER_API_KEY`  
API | سازگار با OpenAI  
URL پایه | `https://api.together.xyz/v1`  
  
## شروع به کار

* ### دریافت کلید API

یک کلید API در [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>) ایجاد کنید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### تنظیم مدل پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### نمونه غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## کاتالوگ داخلی

OpenClaw این کاتالوگ همراه Together را عرضه می‌کند:

ارجاع مدل | نام | ورودی | زمینه | یادداشت‌ها  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | متن، تصویر | 262,144 | مدل پیش‌فرض؛ استدلال فعال است  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | متن | 202,752 | مدل متن عمومی  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | متن | 131,072 | مدل دستورالعمل سریع  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | متن، تصویر | 10,000,000 | چندوجهی  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | متن، تصویر | 20,000,000 | چندوجهی  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | متن | 131,072 | مدل متن عمومی  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | متن | 131,072 | مدل استدلال  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | متن | 262,144 | مدل متن ثانویه Kimi  
  
## تولید ویدئو

Plugin همراه `together` همچنین تولید ویدئو را از طریق ابزار مشترک `video_generate` ثبت می‌کند.

ویژگی | مقدار  
---|---  
مدل ویدئوی پیش‌فرض | `together/Wan-AI/Wan2.2-T2V-A14B`  
حالت‌ها | متن به ویدئو، ارجاع تک‌تصویر  
پارامترهای پشتیبانی‌شده | `aspectRatio`, `resolution`  
  
برای استفاده از Together به‌عنوان ارائه‌دهنده پیش‌فرض ویدئو:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

یادداشت محیط

اگر Gateway به‌صورت daemon اجرا می‌شود (launchd/systemd)، مطمئن شوید `TOGETHER_API_KEY` برای آن فرایند در دسترس است (برای مثال، در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

عیب‌یابی

  * بررسی کنید کلید شما کار می‌کند: `openclaw models list --provider together`
  * اگر مدل‌ها نمایش داده نمی‌شوند، تأیید کنید کلید API در محیط درست برای فرایند Gateway شما تنظیم شده است.
  * ارجاع‌های مدل از قالب `together/<model-id>` استفاده می‌کنند.


## مرتبط

[**انتخاب مدل** قوانین ارائه‌دهنده، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**تولید ویدئو** پارامترهای ابزار مشترک تولید ویدئو و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**مرجع پیکربندی** طرحواره کامل پیکربندی، شامل تنظیمات ارائه‌دهنده. ](</fa/gateway/configuration-reference>) [**Together AI** داشبورد Together AI، مستندات API و قیمت‌گذاری. ](<https://together.ai>)

Was this useful?YesNo