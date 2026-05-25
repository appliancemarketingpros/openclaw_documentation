---
title: Fal
source_url: https://docs.openclaw.ai/fa/providers/fal
scraped_at: 2026-05-25
---

OpenClaw یک ارائه‌دهنده همراه `fal` برای تولید تصویر و ویدئوی میزبانی‌شده ارائه می‌کند.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `fal`  
احراز هویت | `FAL_KEY` (اصلی؛ `FAL_API_KEY` نیز به‌عنوان fallback کار می‌کند)  
API | نقاط پایانی مدل fal  
  
## شروع به کار

* ### تنظیم کلید API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### تنظیم مدل تصویر پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## تولید تصویر

ارائه‌دهنده همراه تولید تصویر `fal` به‌صورت پیش‌فرض از `fal/fal-ai/flux/dev` استفاده می‌کند.

قابلیت | مقدار  
---|---  
حداکثر تصاویر | 4 در هر درخواست  
حالت ویرایش | Flux: 1 تصویر مرجع؛ GPT Image 2: 10؛ Nano Banana 2: 14  
بازنویسی اندازه | پشتیبانی می‌شود  
نسبت ابعاد | برای تولید و ویرایش GPT Image 2/Nano Banana 2 پشتیبانی می‌شود  
وضوح | پشتیبانی می‌شود  
قالب خروجی | `png` یا `jpeg`  
  
وقتی خروجی PNG می‌خواهید، از `outputFormat: "png"` استفاده کنید. fal در OpenClaw کنترل صریحی برای پس‌زمینه شفاف اعلام نمی‌کند، بنابراین `background: "transparent"` برای مدل‌های fal به‌عنوان یک بازنویسی نادیده‌گرفته‌شده گزارش می‌شود.

برای استفاده از fal به‌عنوان ارائه‌دهنده تصویر پیش‌فرض:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## تولید ویدئو

ارائه‌دهنده همراه تولید ویدئوی `fal` به‌صورت پیش‌فرض از `fal/fal-ai/minimax/video-01-live` استفاده می‌کند.

قابلیت | مقدار  
---|---  
حالت‌ها | متن-به-ویدئو، مرجع تک‌تصویری، مرجع-به-ویدئو Seedance  
زمان اجرا | جریان ارسال/وضعیت/نتیجه مبتنی بر صف برای کارهای طولانی‌مدت  
  
مدل‌های ویدئوی موجود

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

نمونه پیکربندی Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

نمونه پیکربندی مرجع-به-ویدئو Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

مرجع-به-ویدئو تا 9 تصویر، 3 ویدئو و 3 مرجع صوتی را از طریق پارامترهای مشترک `video_generate` یعنی `images`، `videos` و `audioRefs` می‌پذیرد، با حداکثر 12 فایل مرجع در مجموع.

نمونه پیکربندی HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## مرتبط

[**تولید تصویر** پارامترهای ابزار تصویر مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/image-generation>) [**تولید ویدئو** پارامترهای ابزار ویدئوی مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**مرجع پیکربندی** پیش‌فرض‌های عامل، شامل انتخاب مدل تصویر و ویدئو. ](</fa/gateway/config-agents#agent-defaults>)

Was this useful?YesNo