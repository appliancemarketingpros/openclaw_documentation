---
title: Arcee AI
source_url: https://docs.openclaw.ai/fa/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) دسترسی به خانواده Trinity از مدل‌های ترکیب متخصصان را از طریق رابط برنامه‌نویسی کاربردی سازگار با OpenAI فراهم می‌کند. همه مدل‌های Trinity تحت مجوز Apache 2.0 منتشر شده‌اند.

مدل‌های Arcee AI را می‌توان مستقیما از طریق پلتفرم Arcee یا از طریق [OpenRouter](</fa/providers/openrouter>) در دسترس داشت.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `arcee`  
احراز هویت | `ARCEEAI_API_KEY` (مستقیم) یا `OPENROUTER_API_KEY` (از طریق OpenRouter)  
رابط برنامه‌نویسی کاربردی | سازگار با OpenAI  
URL پایه | `https://api.arcee.ai/api/v1` (مستقیم) یا `https://openrouter.ai/api/v1` (OpenRouter)  
  
## شروع کار

### مستقیم (پلتفرم Arcee)

* ### دریافت کلید رابط برنامه‌نویسی کاربردی

در [Arcee AI](<https://chat.arcee.ai/>) یک کلید رابط برنامه‌نویسی کاربردی ایجاد کنید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### تنظیم مدل پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### از طریق OpenRouter

* ### دریافت کلید رابط برنامه‌نویسی کاربردی

در [OpenRouter](<https://openrouter.ai/keys>) یک کلید رابط برنامه‌نویسی کاربردی ایجاد کنید.

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### تنظیم مدل پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

همان ارجاع‌های مدل برای هر دو راه‌اندازی مستقیم و OpenRouter کار می‌کنند (برای مثال `arcee/trinity-large-thinking`).

## راه‌اندازی غیرتعاملی

### مستقیم (پلتفرم Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### از طریق OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## کاتالوگ داخلی

OpenClaw در حال حاضر این کاتالوگ Arcee همراه را ارائه می‌کند:

ارجاع مدل | نام | ورودی | زمینه | هزینه (ورودی/خروجی به ازای هر 1M) | یادداشت‌ها  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | متن | 256K | $0.25 / $0.90 | مدل پیش‌فرض؛ استدلال فعال است  
`arcee/trinity-large-preview` | Trinity Large Preview | متن | 128K | $0.25 / $1.00 | چندمنظوره؛ 400B پارامتر، 13B فعال  
`arcee/trinity-mini` | Trinity Mini 26B | متن | 128K | $0.045 / $0.15 | سریع و مقرون‌به‌صرفه؛ فراخوانی تابع  
  
## قابلیت‌های پشتیبانی‌شده

قابلیت | پشتیبانی‌شده  
---|---  
استریمینگ | بله  
استفاده از ابزار / فراخوانی تابع | بله (Trinity Mini، Trinity Large Preview)  
خروجی ساخت‌یافته (حالت JSON و طرح‌واره JSON) | بله  
تفکر گسترده | بله (Trinity Large Thinking؛ ابزارها غیرفعال‌اند)  
  
نکته محیطی

اگر Gateway به صورت daemon (launchd/systemd) اجرا می‌شود، مطمئن شوید `ARCEEAI_API_KEY` (یا `OPENROUTER_API_KEY`) برای آن فرایند در دسترس است (برای مثال، در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

مسیریابی OpenRouter

هنگام استفاده از مدل‌های Arcee از طریق OpenRouter، همان ارجاع‌های مدل `arcee/*` اعمال می‌شوند. OpenClaw مسیریابی را بر اساس انتخاب احراز هویت شما به‌صورت شفاف مدیریت می‌کند. برای جزئیات پیکربندی مخصوص OpenRouter، [مستندات ارائه‌دهنده OpenRouter](</fa/providers/openrouter>) را ببینید.

## مرتبط

[**OpenRouter** به مدل‌های Arcee و بسیاری مدل‌های دیگر از طریق یک کلید رابط برنامه‌نویسی کاربردی واحد دسترسی پیدا کنید. ](</fa/providers/openrouter>) [**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>)

Was this useful?YesNo