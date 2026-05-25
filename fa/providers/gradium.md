---
title: Gradium
source_url: https://docs.openclaw.ai/fa/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) یک ارائه‌دهنده متن‌به‌گفتار همراه برای OpenClaw است. این Plugin می‌تواند پاسخ‌های صوتی معمولی (WAV)، خروجی Opus سازگار با یادداشت صوتی، و صدای 8 kHz u-law را برای سطوح تلفنی تولید کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `gradium`  
احراز هویت | `GRADIUM_API_KEY` یا پیکربندی `apiKey`  
نشانی پایه | `https://api.gradium.ai` (پیش‌فرض)  
صدای پیش‌فرض | `Emma` (`YTpq7expH9539ERJ`)  
  
## راه‌اندازی

یک کلید API برای Gradium بسازید، سپس آن را با یک متغیر محیطی یا کلید پیکربندی در اختیار OpenClaw قرار دهید.

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Config key

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

این Plugin ابتدا `apiKey` حل‌شده را بررسی می‌کند و در صورت نبود آن، به متغیر محیطی `GRADIUM_API_KEY` برمی‌گردد.

## پیکربندی

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

کلید | نوع | توضیح  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | کلید API حل‌شده. از `${ENV}` و ارجاع‌های محرمانه پشتیبانی می‌کند.  
`messages.tts.providers.gradium.baseUrl` | string | مبدا API را بازنویسی می‌کند. اسلش‌های انتهایی حذف می‌شوند. مقدار پیش‌فرض `https://api.gradium.ai` است.  
`messages.tts.providers.gradium.voiceId` | string | شناسه صدای پیش‌فرض که وقتی بازنویسی دستوری وجود ندارد استفاده می‌شود.  
  
قالب صدای خروجی به‌صورت خودکار توسط runtime بر اساس سطح مقصد انتخاب می‌شود و از `openclaw.json` قابل پیکربندی نیست. بخش خروجی را در ادامه ببینید.

## صداها

نام | شناسه صدا  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
صدای پیش‌فرض: Emma.

### بازنویسی صدا برای هر پیام

وقتی سیاست گفتار فعال اجازه بازنویسی صدا را می‌دهد، می‌توانید با استفاده از یک توکن دستوری، صداها را به‌صورت درون‌خطی تغییر دهید. همه این‌ها به همان بازنویسی `voiceId` حل می‌شوند:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

اگر سیاست گفتار بازنویسی صدا را غیرفعال کرده باشد، دستور مصرف می‌شود اما نادیده گرفته می‌شود.

## خروجی

runtime قالب خروجی را از سطح مقصد انتخاب می‌کند. این ارائه‌دهنده در حال حاضر قالب‌های دیگری تولید نمی‌کند.

مقصد | قالب | پسوند فایل | نرخ نمونه‌برداری | پرچم سازگار با صدا  
---|---|---|---|---  
صدای استاندارد | `wav` | `.wav` | ارائه‌دهنده | خیر  
یادداشت صوتی | `opus` | `.opus` | ارائه‌دهنده | بله  
تلفنی | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## ترتیب انتخاب خودکار

در میان ارائه‌دهندگان TTS پیکربندی‌شده، ترتیب انتخاب خودکار Gradium برابر با `30` است. برای اینکه ببینید OpenClaw وقتی `messages.tts.provider` ثابت نشده باشد چگونه ارائه‌دهنده فعال را انتخاب می‌کند، [متن‌به‌گفتار](</fa/tools/tts>) را ببینید.

## مرتبط

  * [متن‌به‌گفتار](</fa/tools/tts>)
  * [نمای کلی رسانه](</fa/tools/media-overview>)


Was this useful?YesNo