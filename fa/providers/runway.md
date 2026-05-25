---
title: باند پرواز
source_url: https://docs.openclaw.ai/fa/providers/runway
scraped_at: 2026-05-25
---

OpenClaw یک ارائه‌دهنده‌ی bundled با نام `runway` برای تولید ویدیوی میزبانی‌شده ارائه می‌کند. این Plugin به‌طور پیش‌فرض فعال است و ارائه‌دهنده‌ی `runway` را برای قرارداد `videoGenerationProviders` ثبت می‌کند.

ویژگی | مقدار  
---|---  
شناسه‌ی ارائه‌دهنده | `runway`  
Plugin | bundled، `enabledByDefault: true`  
متغیرهای محیطی احراز هویت | `RUNWAYML_API_SECRET` (canonical) یا `RUNWAY_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice runway-api-key`  
پرچم مستقیم CLI | `--runway-api-key <key>`  
API | تولید ویدیوی وظیفه‌محور Runway (نظرسنجی `GET /v1/tasks/{id}`)  
مدل پیش‌فرض | `runway/gen4.5`  
  
## شروع به کار

* ### تنظیم کلید API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### تنظیم Runway به‌عنوان ارائه‌دهنده‌ی پیش‌فرض ویدیو

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### تولید یک ویدیو

از عامل بخواهید یک ویدیو تولید کند. Runway به‌طور خودکار استفاده خواهد شد.

## حالت‌ها و مدل‌های پشتیبانی‌شده

این ارائه‌دهنده هفت مدل Runway را در سه حالت ارائه می‌کند. یک شناسه‌ی مدل می‌تواند بیش از یک حالت را پوشش دهد (برای مثال `gen4.5` هم برای متن‌به‌ویدیو و هم برای تصویر‌به‌ویدیو کار می‌کند).

حالت | مدل‌ها | ورودی مرجع  
---|---|---  
متن‌به‌ویدیو | `gen4.5` (پیش‌فرض)، `veo3.1`، `veo3.1_fast`، `veo3` | ندارد  
تصویر‌به‌ویدیو | `gen4.5`، `gen4_turbo`، `gen3a_turbo`، `veo3.1`، `veo3.1_fast`، `veo3` | ۱ تصویر محلی یا راه‌دور  
ویدیو‌به‌ویدیو | `gen4_aleph` | ۱ ویدیوی محلی یا راه‌دور  
  
ارجاع‌های تصویر و ویدیوی محلی از طریق URIهای داده پشتیبانی می‌شوند.

نسبت‌های تصویر | مقادیر مجاز  
---|---  
متن‌به‌ویدیو | `16:9`، `9:16`  
ویرایش‌های تصویر و ویدیو | `1:1`، `16:9`، `9:16`، `3:4`، `4:3`، `21:9`  
  
## پیکربندی

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## پیکربندی پیشرفته

نام‌های مستعار متغیر محیطی

OpenClaw هر دو `RUNWAYML_API_SECRET` (canonical) و `RUNWAY_API_KEY` را می‌شناسد. هر یک از این متغیرها ارائه‌دهنده‌ی Runway را احراز هویت می‌کند.

نظرسنجی وظیفه

Runway از یک API وظیفه‌محور استفاده می‌کند. پس از ارسال درخواست تولید، OpenClaw تا آماده شدن ویدیو، `GET /v1/tasks/{id}` را نظرسنجی می‌کند. برای رفتار نظرسنجی به پیکربندی اضافی نیاز نیست.

## مرتبط

[**تولید ویدیو** پارامترهای ابزار مشترک، انتخاب ارائه‌دهنده، و رفتار ناهمگام. ](</fa/tools/video-generation>) [**مرجع پیکربندی** تنظیمات پیش‌فرض عامل، از جمله مدل تولید ویدیو. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo