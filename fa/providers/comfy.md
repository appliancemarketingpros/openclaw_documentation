---
title: ComfyUI
source_url: https://docs.openclaw.ai/fa/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw یک Plugin همراه با نام `comfy` برای اجرای ComfyUI مبتنی بر گردش کار ارائه می‌کند. این Plugin کاملاً مبتنی بر گردش کار است، بنابراین OpenClaw تلاش نمی‌کند کنترل‌های عمومی `size`، `aspectRatio`، `resolution`، `durationSeconds` یا کنترل‌های سبک TTS را به گراف شما نگاشت کند.

ویژگی | جزئیات  
---|---  
ارائه‌دهنده | `comfy`  
مدل‌ها | `comfy/workflow`  
سطح‌های مشترک | `image_generate`، `video_generate`، `music_generate`  
احراز هویت | برای ComfyUI محلی هیچ موردی نیست؛ `COMFY_API_KEY` یا `COMFY_CLOUD_API_KEY` برای Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` و Comfy Cloud `/api/*`  
  
## چه چیزهایی پشتیبانی می‌شود

  * تولید تصویر از یک JSON گردش کار
  * ویرایش تصویر با 1 تصویر مرجع بارگذاری‌شده
  * تولید ویدیو از یک JSON گردش کار
  * تولید ویدیو با 1 تصویر مرجع بارگذاری‌شده
  * تولید موسیقی یا صدا از طریق ابزار مشترک `music_generate`
  * دانلود خروجی از یک گره پیکربندی‌شده یا همه گره‌های خروجی منطبق


## شروع به کار

بین اجرای ComfyUI روی دستگاه خودتان یا استفاده از Comfy Cloud یکی را انتخاب کنید.

### محلی

**بهترین برای:** اجرای نمونه ComfyUI خودتان روی دستگاه یا LAN خودتان.

* ### ComfyUI را به‌صورت محلی شروع کنید

مطمئن شوید نمونه ComfyUI محلی شما در حال اجراست (پیش‌فرض `http://127.0.0.1:8188` است).

* ### JSON گردش کار خود را آماده کنید

یک فایل JSON گردش کار ComfyUI صادر یا ایجاد کنید. شناسه‌های گره را برای گره ورودی پرامپت و گره خروجی‌ای که می‌خواهید OpenClaw از آن بخواند یادداشت کنید.

* ### ارائه‌دهنده را پیکربندی کنید

`mode: "local"` را تنظیم کنید و به فایل گردش کار خود اشاره کنید. این یک نمونه حداقلی تصویر است:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### مدل پیش‌فرض را تنظیم کنید

OpenClaw را برای قابلیتی که پیکربندی کرده‌اید به مدل `comfy/workflow` اشاره دهید:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### راستی‌آزمایی کنید

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**بهترین برای:** اجرای گردش‌های کار روی Comfy Cloud بدون مدیریت منابع GPU محلی.

* ### یک کلید API دریافت کنید

در [comfy.org](<https://comfy.org>) ثبت‌نام کنید و از داشبورد حساب خود یک کلید API بسازید.

* ### کلید API را تنظیم کنید

کلید خود را از طریق یکی از این روش‌ها ارائه کنید:

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### JSON گردش کار خود را آماده کنید

یک فایل JSON گردش کار ComfyUI صادر یا ایجاد کنید. شناسه‌های گره را برای گره ورودی پرامپت و گره خروجی یادداشت کنید.

* ### ارائه‌دهنده را پیکربندی کنید

`mode: "cloud"` را تنظیم کنید و به فایل گردش کار خود اشاره کنید:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### مدل پیش‌فرض را تنظیم کنید

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### راستی‌آزمایی کنید

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## پیکربندی

Comfy از تنظیمات اتصال مشترک سطح بالا به‌همراه بخش‌های گردش کار به‌ازای هر قابلیت (`image`، `video`، `music`) پشتیبانی می‌کند:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### کلیدهای مشترک

کلید | نوع | توضیح  
---|---|---  
`mode` | `"local"` یا `"cloud"` | حالت اتصال.  
`baseUrl` | string | برای محلی به‌صورت پیش‌فرض `http://127.0.0.1:8188` و برای ابر `https://cloud.comfy.org` است.  
`apiKey` | string | کلید درون‌خطی اختیاری، جایگزین متغیرهای محیطی `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | اجازه دادن به یک `baseUrl` خصوصی/LAN در حالت ابری.  
  
### کلیدهای هر قابلیت

این کلیدها داخل بخش‌های `image`، `video` یا `music` اعمال می‌شوند:

کلید | ضروری | پیش‌فرض | توضیح  
---|---|---|---  
`workflow` یا `workflowPath` | بله | \-- | مسیر فایل JSON گردش کار ComfyUI.  
`promptNodeId` | بله | \-- | شناسه گرهی که پرامپت متنی را دریافت می‌کند.  
`promptInputName` | خیر | `"text"` | نام ورودی روی گره پرامپت.  
`outputNodeId` | خیر | \-- | شناسه گرهی که خروجی از آن خوانده می‌شود. اگر حذف شود، همه گره‌های خروجی منطبق استفاده می‌شوند.  
`pollIntervalMs` | خیر | \-- | فاصله polling بر حسب میلی‌ثانیه برای تکمیل کار.  
`timeoutMs` | خیر | \-- | مهلت زمانی بر حسب میلی‌ثانیه برای اجرای گردش کار.  
  
بخش‌های `image` و `video` همچنین پشتیبانی می‌کنند از:

کلید | ضروری | پیش‌فرض | توضیح  
---|---|---|---  
`inputImageNodeId` | بله (هنگام ارسال یک تصویر مرجع) | \-- | شناسه گرهی که تصویر مرجع بارگذاری‌شده را دریافت می‌کند.  
`inputImageInputName` | خیر | `"image"` | نام ورودی روی گره تصویر.  
  
## جزئیات گردش کار

گردش‌های کار تصویر

مدل تصویر پیش‌فرض را روی `comfy/workflow` تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**نمونه ویرایش با تصویر مرجع:**

برای فعال کردن ویرایش تصویر با یک تصویر مرجع بارگذاری‌شده، `inputImageNodeId` را به پیکربندی تصویر خود اضافه کنید:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

گردش‌های کار ویدیو

مدل ویدیوی پیش‌فرض را روی `comfy/workflow` تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

گردش‌های کار ویدیوی Comfy از متن‌به‌ویدیو و تصویر‌به‌ویدیو از طریق گراف پیکربندی‌شده پشتیبانی می‌کنند.

گردش‌های کار موسیقی

Plugin همراه، یک ارائه‌دهنده تولید موسیقی را برای خروجی‌های صوتی یا موسیقی تعریف‌شده با گردش کار ثبت می‌کند که از طریق ابزار مشترک `music_generate` در دسترس قرار می‌گیرد:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

از بخش پیکربندی `music` برای اشاره به JSON گردش کار صوتی و گره خروجی خود استفاده کنید.

سازگاری روبه‌عقب

پیکربندی تصویر سطح بالای موجود (بدون بخش تودرتوی `image`) همچنان کار می‌کند:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw آن شکل قدیمی را به‌عنوان پیکربندی گردش کار تصویر در نظر می‌گیرد. لازم نیست فوراً مهاجرت کنید، اما بخش‌های تودرتوی `image` / `video` / `music` برای راه‌اندازی‌های جدید توصیه می‌شوند.

آزمون‌های زنده

پوشش زنده اختیاری برای Plugin همراه وجود دارد:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

آزمون زنده موارد جداگانه تصویر، ویدیو یا موسیقی را رد می‌کند مگر اینکه بخش گردش کار Comfy متناظر پیکربندی شده باشد.

## مرتبط

[**تولید تصویر** پیکربندی و استفاده از ابزار تولید تصویر. ](</fa/tools/image-generation>) [**تولید ویدیو** پیکربندی و استفاده از ابزار تولید ویدیو. ](</fa/tools/video-generation>) [**تولید موسیقی** راه‌اندازی ابزار تولید موسیقی و صدا. ](</fa/tools/music-generation>) [**فهرست ارائه‌دهنده‌ها** نمای کلی همه ارائه‌دهنده‌ها و ارجاع‌های مدل. ](</fa/providers>) [**مرجع پیکربندی** مرجع کامل پیکربندی، شامل پیش‌فرض‌های عامل. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo