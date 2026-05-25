---
title: Chutes
source_url: https://docs.openclaw.ai/fa/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) کاتالوگ‌های مدل متن‌باز را از طریق یک API سازگار با OpenAI ارائه می‌کند. OpenClaw هم از احراز هویت OAuth در مرورگر و هم از احراز هویت مستقیم با کلید API برای ارائه‌دهنده همراه `chutes` پشتیبانی می‌کند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `chutes`  
API | سازگار با OpenAI  
URL پایه | `https://llm.chutes.ai/v1`  
احراز هویت | OAuth یا کلید API (پایین را ببینید)  
  
## شروع به کار

### OAuth

* ### Run the OAuth onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw جریان مرورگر را به‌صورت محلی اجرا می‌کند، یا روی میزبان‌های راه‌دور/بدون رابط گرافیکی یک URL + جریان جای‌گذاری تغییرمسیر نشان می‌دهد. توکن‌های OAuth از طریق پروفایل‌های احراز هویت OpenClaw به‌صورت خودکار تازه‌سازی می‌شوند.

* ### Verify the default model

پس از راه‌اندازی اولیه، مدل پیش‌فرض روی `chutes/zai-org/GLM-4.7-TEE` تنظیم می‌شود و کاتالوگ همراه Chutes ثبت می‌شود.

### API key

* ### Get an API key

یک کلید در [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>) بسازید.

* ### Run the API key onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verify the default model

پس از راه‌اندازی اولیه، مدل پیش‌فرض روی `chutes/zai-org/GLM-4.7-TEE` تنظیم می‌شود و کاتالوگ همراه Chutes ثبت می‌شود.

## رفتار کشف

وقتی احراز هویت Chutes در دسترس باشد، OpenClaw کاتالوگ Chutes را با همان اعتبارنامه پرس‌وجو می‌کند و از مدل‌های کشف‌شده استفاده می‌کند. اگر کشف ناموفق باشد، OpenClaw به یک کاتالوگ ایستای همراه بازمی‌گردد تا راه‌اندازی اولیه و شروع به کار همچنان کار کنند.

## نام‌های مستعار پیش‌فرض

OpenClaw سه نام مستعار کاربردی برای کاتالوگ همراه Chutes ثبت می‌کند:

نام مستعار | مدل هدف  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## کاتالوگ آغازین داخلی

کاتالوگ پشتیبان همراه شامل ارجاع‌های فعلی Chutes است:

ارجاع مدل  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## نمونه پیکربندی

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

می‌توانید جریان OAuth را با متغیرهای محیطی اختیاری سفارشی کنید:

متغیر | هدف  
---|---  
`CHUTES_CLIENT_ID` | شناسه کلاینت OAuth سفارشی  
`CHUTES_CLIENT_SECRET` | راز کلاینت OAuth سفارشی  
`CHUTES_OAUTH_REDIRECT_URI` | URI تغییرمسیر سفارشی  
`CHUTES_OAUTH_SCOPES` | دامنه‌های OAuth سفارشی  
  
برای نیازمندی‌های برنامه تغییرمسیر و راهنما، [مستندات OAuth Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>) را ببینید.

Notes

  * کشف با کلید API و OAuth هر دو از همان شناسه ارائه‌دهنده `chutes` استفاده می‌کنند.
  * مدل‌های Chutes با قالب `chutes/<model-id>` ثبت می‌شوند.
  * اگر کشف هنگام شروع به کار ناموفق باشد، کاتالوگ ایستای همراه به‌صورت خودکار استفاده می‌شود.


## مرتبط

[**Model selection** قواعد ارائه‌دهنده، ارجاع‌های مدل، و رفتار جابه‌جایی هنگام خرابی. ](</fa/concepts/model-providers>) [**Configuration reference** طرح‌واره کامل پیکربندی شامل تنظیمات ارائه‌دهنده. ](</fa/gateway/configuration-reference>) [**Chutes** داشبورد و مستندات API برای Chutes. ](<https://chutes.ai>) [**Chutes API keys** کلیدهای API برای Chutes را بسازید و مدیریت کنید. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo