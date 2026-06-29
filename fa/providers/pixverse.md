---
title: PixVerse
source_url: https://docs.openclaw.ai/fa/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw، `pixverse` را به‌عنوان یک Plugin خارجی رسمی برای تولید ویدیوی میزبانی‌شده PixVerse ارائه می‌کند. این Plugin، ارائه‌دهنده `pixverse` را در برابر قرارداد `videoGenerationProviders` ثبت می‌کند.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `pixverse`  
بسته Plugin | `@openclaw/pixverse-provider`  
متغیر محیطی احراز هویت | `PIXVERSE_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice pixverse-api-key`  
پرچم مستقیم CLI | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (ارسال `video_id` همراه با نظرسنجی نتیجه)  
مدل پیش‌فرض | `pixverse/v6`  
منطقه پیش‌فرض API | بین‌المللی  
  
## شروع به کار

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

راهنمای مرحله‌ای پیش از نوشتن `region` و `baseUrl` در پیکربندی ارائه‌دهنده، می‌پرسد که از نقطه پایانی بین‌المللی (`https://app-api.pixverse.ai/openapi/v2`) یا نقطه پایانی چین (`https://app-api.pixverseai.cn/openapi/v2`) استفاده شود.

* ### Set PixVerse as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generate a video

از عامل بخواهید یک ویدیو تولید کند. PixVerse به‌صورت خودکار استفاده خواهد شد.

## حالت‌ها و مدل‌های پشتیبانی‌شده

ارائه‌دهنده، مدل‌های تولید PixVerse را از طریق ابزار ویدیوی مشترک OpenClaw در دسترس می‌گذارد.

حالت | مدل‌ها | ورودی مرجع  
---|---|---  
متن به ویدیو | `v6` (پیش‌فرض)، `c1` | هیچ‌کدام  
تصویر به ویدیو | `v6` (پیش‌فرض)، `c1` | 1 تصویر محلی یا راه دور  
  
ارجاع‌های تصویر محلی پیش از درخواست تصویر به ویدیو در PixVerse بارگذاری می‌شوند. URLهای تصویر راه دور از طریق نقطه پایانی بارگذاری تصویر PixVerse به‌صورت `image_url` عبور داده می‌شوند.

گزینه | مقدارهای پشتیبانی‌شده  
---|---  
مدت‌زمان | 1 تا 15 ثانیه  
وضوح | `360P`, `540P`, `720P`, `1080P`  
نسبت تصویر | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` برای متن به ویدیو  
صدای تولیدشده | `audio: true`  
  
## گزینه‌های ارائه‌دهنده

ارائه‌دهنده ویدیو این کلیدهای اختیاری اختصاصی ارائه‌دهنده را می‌پذیرد:

گزینه | نوع | اثر  
---|---|---  
`seed` | number | seed قطعی در صورت پشتیبانی  
`negativePrompt` / `negative_prompt` | string | اعلان منفی  
`quality` | string | کیفیت PixVerse مانند `720p`  
`motionMode` / `motion_mode` | string | حالت حرکت تصویر به ویدیو  
`cameraMovement` / `camera_movement` | string | پیش‌تنظیم حرکت دوربین PixVerse  
`templateId` / `template_id` | number | شناسه قالب فعال‌شده PixVerse  
  
## پیکربندی

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## پیکربندی پیشرفته

API region

OpenClaw به‌صورت پیش‌فرض از API بین‌المللی PixVerse استفاده می‌کند. هنگامی که کلید شما به منطقه پلتفرمی خاصی از PixVerse تعلق دارد، `models.providers.pixverse.region` را به‌صورت دستی تنظیم کنید، یا برای انتخاب آن در راهنمای مرحله‌ای راه‌اندازی از `openclaw onboard --auth-choice pixverse-api-key` استفاده کنید:

مقدار منطقه | URL پایه API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Custom base URL

`models.providers.pixverse.baseUrl` را فقط زمانی تنظیم کنید که مسیر‌دهی از طریق یک پراکسی سازگار و مورد اعتماد انجام می‌شود. `baseUrl` نسبت به `region` اولویت دارد.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Task polling

PixVerse از درخواست تولید، یک `video_id` برمی‌گرداند. OpenClaw تا زمانی که وظیفه موفق شود، شکست بخورد، یا مهلت آن تمام شود، از `/openapi/v2/video/result/{video_id}` نظرسنجی می‌کند.

## مرتبط

[**Video generation** پارامترهای ابزار مشترک، انتخاب ارائه‌دهنده، و رفتار ناهمگام. ](</fa/tools/video-generation>) [**Configuration reference** تنظیمات پیش‌فرض عامل، شامل مدل تولید ویدیو. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue