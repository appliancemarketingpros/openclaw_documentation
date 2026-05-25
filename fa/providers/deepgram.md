---
title: Deepgram
source_url: https://docs.openclaw.ai/fa/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram یک API تبدیل گفتار به متن است. در OpenClaw از آن برای رونویسی صوت/یادداشت صوتی ورودی از طریق `tools.media.audio` و برای STT پخش جریانی تماس صوتی از طریق `plugins.entries.voice-call.config.streaming` استفاده می‌شود.

برای رونویسی دسته‌ای، OpenClaw فایل صوتی کامل را در Deepgram بارگذاری می‌کند و متن رونویسی‌شده را به خط لوله پاسخ تزریق می‌کند (بلوک `{{Transcript}}` \+ `[Audio]`). برای پخش جریانی تماس صوتی، OpenClaw فریم‌های زنده G.711 u-law را از طریق نقطه پایانی WebSocket `listen` در Deepgram ارسال می‌کند و هم‌زمان با بازگشت آن‌ها از Deepgram، رونویسی‌های جزئی یا نهایی را منتشر می‌کند.

جزئیات | مقدار  
---|---  
وب‌سایت | [deepgram.com](<https://deepgram.com>)  
مستندات | [developers.deepgram.com](<https://developers.deepgram.com>)  
احراز هویت | `DEEPGRAM_API_KEY`  
مدل پیش‌فرض | `nova-3`  
  
## شروع به کار

* ### کلید API خود را تنظیم کنید

کلید API مربوط به Deepgram را به محیط اضافه کنید:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### ارائه‌دهنده صوت را فعال کنید

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### یک یادداشت صوتی ارسال کنید

یک پیام صوتی را از طریق هر کانال متصل ارسال کنید. OpenClaw آن را از طریق Deepgram رونویسی می‌کند و متن رونویسی‌شده را به خط لوله پاسخ تزریق می‌کند.

## گزینه‌های پیکربندی

گزینه | مسیر | توضیح  
---|---|---  
`model` | `tools.media.audio.models[].model` | شناسه مدل Deepgram (پیش‌فرض: `nova-3`)  
`language` | `tools.media.audio.models[].language` | راهنمای زبان (اختیاری)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | فعال‌سازی تشخیص زبان (اختیاری)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | فعال‌سازی نشانه‌گذاری (اختیاری)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | فعال‌سازی قالب‌بندی هوشمند (اختیاری)  
  
### با راهنمای زبان

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### با گزینه‌های Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT پخش جریانی تماس صوتی

Plugin همراه `deepgram` همچنین یک ارائه‌دهنده رونویسی بلادرنگ برای Plugin تماس صوتی ثبت می‌کند.

تنظیم | مسیر پیکربندی | پیش‌فرض  
---|---|---  
کلید API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | به `DEEPGRAM_API_KEY` بازمی‌گردد  
مدل | `...deepgram.model` | `nova-3`  
زبان | `...deepgram.language` | (تنظیم نشده)  
کدگذاری | `...deepgram.encoding` | `mulaw`  
نرخ نمونه‌برداری | `...deepgram.sampleRate` | `8000`  
نقطه‌گذاری پایانی | `...deepgram.endpointingMs` | `800`  
نتایج موقت | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## نکات

احراز هویت

احراز هویت از ترتیب استاندارد احراز هویت ارائه‌دهنده پیروی می‌کند. `DEEPGRAM_API_KEY` ساده‌ترین مسیر است.

پراکسی و نقاط پایانی سفارشی

هنگام استفاده از پراکسی، نقاط پایانی یا سرآیندها را با `tools.media.audio.baseUrl` و `tools.media.audio.headers` بازنویسی کنید.

رفتار خروجی

خروجی از همان قواعد صوتی سایر ارائه‌دهندگان پیروی می‌کند (سقف اندازه، مهلت‌های زمانی، تزریق رونویسی).

## مرتبط

[**ابزارهای رسانه** نمای کلی خط لوله پردازش صوت، تصویر و ویدئو. ](</fa/tools/media-overview>) [**پیکربندی** مرجع کامل پیکربندی، شامل تنظیمات ابزار رسانه. ](</fa/gateway/configuration>) [**عیب‌یابی** مشکلات رایج و مراحل اشکال‌زدایی. ](</fa/help/troubleshooting>) [**پرسش‌های متداول** پرسش‌های متداول درباره راه‌اندازی OpenClaw. ](</fa/help/faq>)

Was this useful?YesNo