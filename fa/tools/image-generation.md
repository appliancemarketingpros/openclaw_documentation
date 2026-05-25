---
title: تولید تصویر
source_url: https://docs.openclaw.ai/fa/tools/image-generation
scraped_at: 2026-05-25
---

ابزار `image_generate` به عامل امکان می‌دهد با استفاده از ارائه‌دهندگان پیکربندی‌شده‌ی شما تصویر ایجاد و ویرایش کند. تصاویر تولیدشده به‌صورت خودکار به‌عنوان پیوست‌های رسانه‌ای در پاسخ عامل تحویل داده می‌شوند.

## شروع سریع

* ### پیکربندی احراز هویت

برای دست‌کم یک ارائه‌دهنده یک کلید API تنظیم کنید (برای مثال `OPENAI_API_KEY`، `GEMINI_API_KEY`، `OPENROUTER_API_KEY`) یا با OpenAI Codex OAuth وارد شوید.

* ### انتخاب مدل پیش‌فرض (اختیاری)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth از همان ارجاع مدل `openai/gpt-image-2` استفاده می‌کند. وقتی یک پروفایل OAuth با نام `openai-codex` پیکربندی شده باشد، OpenClaw درخواست‌های تصویر را به‌جای اینکه ابتدا `OPENAI_API_KEY` را امتحان کند، از طریق همان پروفایل OAuth مسیریابی می‌کند. پیکربندی صریح `models.providers.openai` (کلید API، نشانی پایه‌ی سفارشی/Azure) مسیر مستقیم OpenAI Images API را دوباره فعال می‌کند.

* ### درخواست از عامل

_"تصویری از یک ربات نمادینِ دوستانه تولید کن."_

عامل به‌صورت خودکار `image_generate` را فراخوانی می‌کند. نیازی به فهرست مجاز ابزار نیست - وقتی یک ارائه‌دهنده در دسترس باشد، به‌طور پیش‌فرض فعال است.

## مسیرهای رایج

هدف | ارجاع مدل | احراز هویت  
---|---|---  
تولید تصویر OpenAI با صورت‌حساب API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
تولید تصویر OpenAI با احراز هویت اشتراک Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
PNG/WebP با پس‌زمینه شفاف در OpenAI | `openai/gpt-image-1.5` | `OPENAI_API_KEY` یا OpenAI Codex OAuth  
تولید تصویر DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
تولید تصویر OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
تولید تصویر LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
تولید تصویر Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` یا `GOOGLE_API_KEY`  
  
همان ابزار `image_generate` تبدیل متن به تصویر و ویرایش تصویر مرجع را مدیریت می‌کند. برای یک مرجع از `image` و برای چند مرجع از `images` استفاده کنید. راهنماهای خروجی پشتیبانی‌شده توسط ارائه‌دهنده مانند `quality`، `outputFormat` و `background` در صورت دسترس بودن ارسال می‌شوند و وقتی ارائه‌دهنده از آن‌ها پشتیبانی نکند، به‌عنوان نادیده‌گرفته‌شده گزارش می‌شوند. پشتیبانی همراه از پس‌زمینه شفاف مخصوص OpenAI است؛ ارائه‌دهندگان دیگر همچنان ممکن است اگر پشتیبان آن‌ها تولید کند، آلفای PNG را حفظ کنند.

## ارائه‌دهندگان پشتیبانی‌شده

ارائه‌دهنده | مدل پیش‌فرض | پشتیبانی از ویرایش | احراز هویت  
---|---|---|---  
ComfyUI | `workflow` | بله (۱ تصویر، پیکربندی‌شده با workflow) | `COMFY_API_KEY` یا `COMFY_CLOUD_API_KEY` برای ابر  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | بله (۱ تصویر) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | بله (محدودیت‌های وابسته به مدل) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | بله | `GEMINI_API_KEY` یا `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | بله (تا ۵ تصویر ورودی) | `LITELLM_API_KEY`  
MiniMax | `image-01` | بله (مرجع سوژه) | `MINIMAX_API_KEY` یا MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | بله (تا ۴ تصویر) | `OPENAI_API_KEY` یا OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | بله (تا ۵ تصویر ورودی) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | خیر | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | بله (تا ۵ تصویر) | `XAI_API_KEY`  
  
برای بررسی ارائه‌دهندگان و مدل‌های موجود در زمان اجرا، از `action: "list"` استفاده کنید:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## قابلیت‌های ارائه‌دهنده

قابلیت | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
تولید (حداکثر تعداد) | تعریف‌شده توسط Workflow | ۴ | ۴ | ۴ | ۹ | ۴ | ۱ | ۴  
ویرایش / مرجع | ۱ تصویر (workflow) | ۱ تصویر | Flux: 1; GPT: 10; NB2: 14 | تا ۵ تصویر | ۱ تصویر (مرجع سوژه) | تا ۵ تصویر | - | تا ۵ تصویر  
کنترل اندازه | - | ✓ | ✓ | ✓ | - | تا 4K | - | -  
نسبت تصویر | - | - | ✓ | ✓ | ✓ | - | - | ✓  
وضوح (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## پارامترهای ابزار

پرامپت تولید تصویر. برای `action: "generate"` الزامی است.

برای بررسی ارائه‌دهندگان و مدل‌های موجود در زمان اجرا از `"list"` استفاده کنید.

بازنویسی ارائه‌دهنده/مدل (مثلاً `openai/gpt-image-2`). برای پس‌زمینه‌های شفاف OpenAI از `openai/gpt-image-1.5` استفاده کنید.

مسیر یا URL یک تصویر مرجع برای حالت ویرایش.

چند تصویر مرجع برای حالت ویرایش (تا ۵ مورد در ارائه‌دهندگان پشتیبانی‌کننده).

راهنمای اندازه: `1024x1024`، `1536x1024`، `1024x1536`، `2048x2048`، `3840x2160`.

نسبت تصویر: `1:1`، `2:3`، `3:2`، `3:4`، `4:3`، `4:5`، `5:4`، `9:16`، `16:9`، `21:9`.

راهنمای کیفیت وقتی ارائه‌دهنده از آن پشتیبانی کند.

راهنمای قالب خروجی وقتی ارائه‌دهنده از آن پشتیبانی کند.

راهنمای پس‌زمینه وقتی ارائه‌دهنده از آن پشتیبانی کند. برای ارائه‌دهندگانی که توانایی شفافیت دارند، از `transparent` همراه با `outputFormat: "png"` یا `"webp"` استفاده کنید.

مهلت زمانی اختیاری درخواست ارائه‌دهنده بر حسب میلی‌ثانیه. وقتی Codex از طریق ابزارهای پویا `image_generate` را فراخوانی می‌کند، این مقدار هر فراخوانی همچنان مقدار پیش‌فرض پیکربندی‌شده را بازنویسی می‌کند و سقف آن 600000 میلی‌ثانیه است.

راهنماهای فقط مخصوص OpenAI: `background`، `moderation`، `outputCompression` و `user`.

## پیکربندی

### انتخاب مدل

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### ترتیب انتخاب ارائه‌دهنده

OpenClaw ارائه‌دهندگان را به این ترتیب امتحان می‌کند:

  1. **پارامتر`model`** از فراخوانی ابزار (اگر عامل یکی را مشخص کند).
  2. **`imageGenerationModel.primary`** از پیکربندی.
  3. **`imageGenerationModel.fallbacks`** به‌ترتیب.
  4. **تشخیص خودکار** \- فقط پیش‌فرض‌های ارائه‌دهنده با پشتوانه‌ی احراز هویت: 
     * ابتدا ارائه‌دهنده‌ی پیش‌فرض فعلی؛
     * سپس سایر ارائه‌دهندگان ثبت‌شده‌ی تولید تصویر به‌ترتیب شناسه‌ی ارائه‌دهنده.


اگر یک ارائه‌دهنده شکست بخورد (خطای احراز هویت، محدودیت نرخ و غیره)، نامزد پیکربندی‌شده‌ی بعدی به‌صورت خودکار امتحان می‌شود. اگر همه شکست بخورند، خطا شامل جزئیات هر تلاش خواهد بود.

بازنویسی‌های مدل در هر فراخوانی دقیق هستند

بازنویسی `model` در هر فراخوانی فقط همان ارائه‌دهنده/مدل را امتحان می‌کند و به ارائه‌دهندگان primary/fallback پیکربندی‌شده یا تشخیص‌داده‌شده‌ی خودکار ادامه نمی‌دهد.

تشخیص خودکار از احراز هویت آگاه است

پیش‌فرض یک ارائه‌دهنده فقط زمانی وارد فهرست نامزدها می‌شود که OpenClaw واقعاً بتواند آن ارائه‌دهنده را احراز هویت کند. برای استفاده فقط از ورودی‌های صریح `model`، `primary` و `fallbacks`، مقدار `agents.defaults.mediaGenerationAutoProviderFallback: false` را تنظیم کنید.

مهلت‌های زمانی

برای پشتیبان‌های کند تصویر، `agents.defaults.imageGenerationModel.timeoutMs` را تنظیم کنید. پارامتر ابزار `timeoutMs` در هر فراخوانی مقدار پیش‌فرض پیکربندی‌شده را بازنویسی می‌کند. فراخوانی‌های ابزار پویای Codex همان بودجه‌ی مهلت زمانی را رعایت می‌کنند که با حداکثر 600000 میلی‌ثانیه‌ی پل ابزار پویای OpenClaw محدود شده است.

بررسی در زمان اجرا

برای بررسی ارائه‌دهندگان ثبت‌شده‌ی فعلی، مدل‌های پیش‌فرض آن‌ها و راهنماهای متغیر محیطی احراز هویت، از `action: "list"` استفاده کنید.

### ویرایش تصویر

OpenAI، OpenRouter، Google، DeepInfra، fal، MiniMax، ComfyUI و xAI از ویرایش تصاویر مرجع پشتیبانی می‌کنند. یک مسیر یا URL تصویر مرجع ارسال کنید:

textCopy code
[code]
    "یک نسخه آبرنگی از این عکس تولید کن" + image: "/path/to/photo.jpg"
[/code]

OpenAI، OpenRouter، Google و xAI از حداکثر 5 تصویر مرجع از طریق پارامتر `images` پشتیبانی می‌کنند. fal برای Flux image-to-image از 1 تصویر مرجع، برای ویرایش‌های GPT Image 2 تا 10 تصویر، و برای ویرایش‌های Nano Banana 2 تا 14 تصویر پشتیبانی می‌کند. MiniMax و ComfyUI از 1 تصویر پشتیبانی می‌کنند.

## بررسی‌های عمیق Provider

OpenAI gpt-image-2 (and gpt-image-1.5)

تولید تصویر OpenAI به‌طور پیش‌فرض از `openai/gpt-image-2` استفاده می‌کند. اگر یک پروفایل OAuth برای `openai-codex` پیکربندی شده باشد، OpenClaw همان پروفایل OAuth مورد استفاده توسط مدل‌های چت اشتراکی Codex را دوباره استفاده می‌کند و درخواست تصویر را از طریق بک‌اند Codex Responses می‌فرستد. URLهای پایه قدیمی Codex مانند `https://chatgpt.com/backend-api` برای درخواست‌های تصویر به `https://chatgpt.com/backend-api/codex` به‌صورت canonical تبدیل می‌شوند. OpenClaw برای آن درخواست **بی‌سروصدا** به `OPENAI_API_KEY` بازنمی‌گردد - برای اجبار به مسیریابی مستقیم OpenAI Images API، گزینه `models.providers.openai` را صراحتا با یک کلید API، URL پایه سفارشی، یا endpoint مربوط به Azure پیکربندی کنید.

مدل‌های `openai/gpt-image-1.5`، `openai/gpt-image-1` و `openai/gpt-image-1-mini` همچنان می‌توانند صراحتا انتخاب شوند. برای خروجی PNG/WebP با پس‌زمینه شفاف از `gpt-image-1.5` استفاده کنید؛ API فعلی `gpt-image-2` مقدار `background: "transparent"` را رد می‌کند.

`gpt-image-2` هم از تولید متن‌به‌تصویر و هم از ویرایش با تصویر مرجع از طریق همان ابزار `image_generate` پشتیبانی می‌کند. OpenClaw مقدارهای `prompt`، `count`، `size`، `quality`، `outputFormat` و تصاویر مرجع را به OpenAI ارسال می‌کند. OpenAI مقدارهای `aspectRatio` یا `resolution` را مستقیما دریافت **نمی‌کند** ؛ در صورت امکان OpenClaw آن‌ها را به یک `size` پشتیبانی‌شده نگاشت می‌کند، و در غیر این صورت ابزار آن‌ها را به‌عنوان overrideهای نادیده‌گرفته‌شده گزارش می‌کند.

گزینه‌های اختصاصی OpenAI زیر شیء `openai` قرار می‌گیرند:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` مقدارهای `transparent`، `opaque` یا `auto` را می‌پذیرد؛ خروجی‌های شفاف به `outputFormat` برابر با `png` یا `webp` و یک مدل تصویر OpenAI با قابلیت شفافیت نیاز دارند. OpenClaw درخواست‌های پیش‌فرض `gpt-image-2` با پس‌زمینه شفاف را به `gpt-image-1.5` مسیریابی می‌کند. `openai.outputCompression` روی خروجی‌های JPEG/WebP اعمال می‌شود.

راهنمای سطح‌بالای `background` مستقل از Provider است و در حال حاضر وقتی Provider انتخاب‌شده OpenAI باشد، به همان فیلد درخواست `background` در OpenAI نگاشت می‌شود. Providerهایی که پشتیبانی از پس‌زمینه را اعلام نمی‌کنند، به‌جای دریافت پارامتر پشتیبانی‌نشده، آن را در `ignoredOverrides` برمی‌گردانند.

برای مسیریابی تولید تصویر OpenAI از طریق یک استقرار Azure OpenAI به‌جای `api.openai.com`، به [endpointهای Azure OpenAI](</fa/providers/openai#azure-openai-endpoints>) مراجعه کنید.

OpenRouter image models

تولید تصویر OpenRouter از همان `OPENROUTER_API_KEY` استفاده می‌کند و از طریق API تصویر chat completions مربوط به OpenRouter مسیریابی می‌شود. مدل‌های تصویر OpenRouter را با پیشوند `openrouter/` انتخاب کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw مقدارهای `prompt`، `count`، تصاویر مرجع، و راهنماهای سازگار با Gemini برای `aspectRatio` / `resolution` را به OpenRouter ارسال می‌کند. میان‌برهای فعلی مدل تصویر داخلی OpenRouter شامل `google/gemini-3.1-flash-image-preview`، `google/gemini-3-pro-image-preview` و `openai/gpt-5.4-image-2` هستند. برای دیدن آنچه Plugin پیکربندی‌شده شما در اختیار می‌گذارد، از `action: "list"` استفاده کنید.

MiniMax dual-auth

تولید تصویر MiniMax از طریق هر دو مسیر احراز هویت MiniMax همراه‌شده در دسترس است:

  * `minimax/image-01` برای راه‌اندازی‌های مبتنی بر کلید API
  * `minimax-portal/image-01` برای راه‌اندازی‌های مبتنی بر OAuth

xAI grok-imagine-image

Provider همراه‌شده xAI برای درخواست‌های فقط مبتنی بر prompt از `/v1/images/generations` و وقتی `image` یا `images` وجود داشته باشد از `/v1/images/edits` استفاده می‌کند.

  * مدل‌ها: `xai/grok-imagine-image`، `xai/grok-imagine-image-pro`
  * تعداد: حداکثر 4
  * مراجع: یک `image` یا حداکثر پنج `images`
  * نسبت‌های تصویر: `1:1`، `16:9`، `9:16`، `4:3`، `3:4`، `2:3`، `3:2`
  * وضوح‌ها: `1K`، `2K`
  * خروجی‌ها: به‌صورت پیوست‌های تصویر مدیریت‌شده توسط OpenClaw برگردانده می‌شوند


OpenClaw عمدا `quality`، `mask`، `user` یا نسبت‌های تصویر اضافی و فقط بومی xAI را تا زمانی که این کنترل‌ها در قرارداد مشترک و چند-Provider `image_generate` وجود نداشته باشند، در معرض استفاده قرار نمی‌دهد.

## مثال‌ها

### Generate (4K landscape)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generate (transparent PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

CLI معادل:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generate (two square)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (one reference)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (multiple references)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

همان flagهای `--output-format` و `--background` روی `openclaw infer image edit` نیز در دسترس هستند؛ `--openai-background` همچنان به‌عنوان نام مستعار اختصاصی OpenAI باقی می‌ماند. Providerهای همراه‌شده به‌جز OpenAI امروز کنترل صریح پس‌زمینه را اعلام نمی‌کنند، بنابراین `background: "transparent"` برای آن‌ها به‌عنوان نادیده‌گرفته‌شده گزارش می‌شود.

## مرتبط

  * [مرور ابزارها](</fa/tools>) \- همه ابزارهای عامل در دسترس
  * [ComfyUI](</fa/providers/comfy>) \- راه‌اندازی گردش کار ComfyUI محلی و Comfy Cloud
  * [fal](</fa/providers/fal>) \- راه‌اندازی Provider تصویر و ویدئوی fal
  * [Google (Gemini)](</fa/providers/google>) \- راه‌اندازی Provider تصویر Gemini
  * [MiniMax](</fa/providers/minimax>) \- راه‌اندازی Provider تصویر MiniMax
  * [OpenAI](</fa/providers/openai>) \- راه‌اندازی Provider مربوط به OpenAI Images
  * [Vydra](</fa/providers/vydra>) \- راه‌اندازی تصویر، ویدئو و گفتار Vydra
  * [xAI](</fa/providers/xai>) \- راه‌اندازی تصویر، ویدئو، جست‌وجو، اجرای کد و TTS مربوط به Grok
  * [مرجع پیکربندی](</fa/gateway/config-agents#agent-defaults>) \- پیکربندی `imageGenerationModel`
  * [مدل‌ها](</fa/concepts/models>) \- پیکربندی مدل و failover


Was this useful?YesNo