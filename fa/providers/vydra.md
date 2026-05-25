---
title: Vydra
source_url: https://docs.openclaw.ai/fa/providers/vydra
scraped_at: 2026-05-25
---

Plugin همراه Vydra این موارد را اضافه می‌کند:

  * تولید تصویر از طریق `vydra/grok-imagine`
  * تولید ویدیو از طریق `vydra/veo3` و `vydra/kling`
  * سنتز گفتار از طریق مسیر TTS مبتنی بر ElevenLabs در Vydra


OpenClaw برای هر سه قابلیت از همان `VYDRA_API_KEY` استفاده می‌کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `vydra`  
Plugin | همراه، `enabledByDefault: true`  
متغیر محیطی احراز هویت | `VYDRA_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice vydra-api-key`  
پرچم مستقیم CLI | `--vydra-api-key <key>`  
قراردادها | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL پایه | `https://www.vydra.ai/api/v1` (از میزبان `www` استفاده کنید)  
  
## راه‌اندازی

* ### اجرای راه‌اندازی اولیه تعاملی

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

یا متغیر محیطی را مستقیما تنظیم کنید:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### انتخاب یک قابلیت پیش‌فرض

یک یا چند قابلیت زیر را انتخاب کنید (تصویر، ویدیو، یا گفتار) و پیکربندی متناظر را اعمال کنید.

## قابلیت‌ها

تولید تصویر

مدل تصویر پیش‌فرض:

  * `vydra/grok-imagine`


آن را به‌عنوان ارائه‌دهنده تصویر پیش‌فرض تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

پشتیبانی همراه فعلی فقط متن به تصویر است. مسیرهای ویرایش میزبانی‌شده Vydra انتظار URLهای تصویر راه‌دور را دارند، و OpenClaw هنوز در Plugin همراه پل آپلود اختصاصی Vydra اضافه نمی‌کند.

تولید ویدیو

مدل‌های ویدیوی ثبت‌شده:

  * `vydra/veo3` برای متن به ویدیو
  * `vydra/kling` برای تصویر به ویدیو


Vydra را به‌عنوان ارائه‌دهنده ویدیوی پیش‌فرض تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

نکات:

  * `vydra/veo3` فقط به‌عنوان متن به ویدیو همراه شده است.
  * `vydra/kling` در حال حاضر به ارجاع URL تصویر راه‌دور نیاز دارد. آپلود فایل‌های محلی از ابتدا رد می‌شود.
  * مسیر HTTP فعلی `kling` در Vydra درباره اینکه به `image_url` نیاز دارد یا `video_url` ناسازگار بوده است؛ ارائه‌دهنده همراه همان URL تصویر راه‌دور را به هر دو فیلد نگاشت می‌کند.
  * Plugin همراه محافظه‌کار می‌ماند و کنترل‌های سبک مستندنشده مانند نسبت تصویر، وضوح، واترمارک، یا صدای تولیدشده را ارسال نمی‌کند.

تست‌های زنده ویدیو

پوشش زنده اختصاصی ارائه‌دهنده:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

فایل زنده همراه Vydra اکنون این موارد را پوشش می‌دهد:

  * `vydra/veo3` متن به ویدیو
  * `vydra/kling` تصویر به ویدیو با استفاده از URL تصویر راه‌دور


در صورت نیاز، fixture تصویر راه‌دور را بازنویسی کنید:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

سنتز گفتار

Vydra را به‌عنوان ارائه‌دهنده گفتار تنظیم کنید:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

پیش‌فرض‌ها:

  * مدل: `elevenlabs/tts`
  * شناسه صدا: `21m00Tcm4TlvDq8ikWAM`


Plugin همراه در حال حاضر یک صدای پیش‌فرض شناخته‌شده و مطمئن را ارائه می‌کند و فایل‌های صوتی MP3 برمی‌گرداند.

## مرتبط

[**فهرست ارائه‌دهندگان** همه ارائه‌دهندگان موجود را مرور کنید. ](</fa/providers>) [**تولید تصویر** پارامترهای مشترک ابزار تصویر و انتخاب ارائه‌دهنده. ](</fa/tools/image-generation>) [**تولید ویدیو** پارامترهای مشترک ابزار ویدیو و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**مرجع پیکربندی** پیش‌فرض‌های Agent و پیکربندی مدل. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo