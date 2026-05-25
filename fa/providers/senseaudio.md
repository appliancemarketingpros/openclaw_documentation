---
title: SenseAudio
source_url: https://docs.openclaw.ai/fa/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio می‌تواند پیوست‌های صوتی و یادداشت‌های صوتی ورودی را از طریق خط لوله مشترک `tools.media.audio` در OpenClaw رونویسی کند. OpenClaw صوت چندبخشی را به نقطه پایانی رونویسی سازگار با OpenAI ارسال می‌کند و متن برگشتی را به‌صورت `{{Transcript}}` به‌همراه یک بلوک `[Audio]` تزریق می‌کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `senseaudio`  
Plugin | همراه، `enabledByDefault: true`  
قرارداد | `mediaUnderstandingProviders` (صوت)  
متغیر محیطی احراز هویت | `SENSEAUDIO_API_KEY`  
مدل پیش‌فرض | `senseaudio-asr-pro-1.5-260319`  
URL پیش‌فرض | `https://api.senseaudio.cn/v1`  
وب‌سایت | [senseaudio.cn](<https://senseaudio.cn>)  
مستندات | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## شروع به کار

* ### کلید API خود را تنظیم کنید

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### ارائه‌دهنده صوتی را فعال کنید

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### یک یادداشت صوتی ارسال کنید

یک پیام صوتی را از طریق هر کانال متصل ارسال کنید. OpenClaw صوت را در SenseAudio بارگذاری می‌کند و از رونویسی در خط لوله پاسخ استفاده می‌کند.

## گزینه‌ها

گزینه | مسیر | توضیح  
---|---|---  
`model` | `tools.media.audio.models[].model` | شناسه مدل ASR در SenseAudio  
`language` | `tools.media.audio.models[].language` | راهنمای اختیاری زبان  
`prompt` | `tools.media.audio.prompt` | اعلان اختیاری رونویسی  
`baseUrl` | `tools.media.audio.baseUrl` یا مدل | بازنویسی پایه سازگار با OpenAI  
`headers` | `tools.media.audio.request.headers` | سرآیندهای اضافی درخواست  
  
## مرتبط

  * [درک رسانه (صوت)](</fa/nodes/audio>)
  * [ارائه‌دهندگان مدل](</fa/concepts/model-providers>)


Was this useful?YesNo