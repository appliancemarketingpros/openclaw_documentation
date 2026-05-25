---
title: تولید موسیقی
source_url: https://docs.openclaw.ai/fa/tools/music-generation
scraped_at: 2026-05-25
---

ابزار `music_generate` به عامل اجازه می‌دهد از طریق قابلیت مشترک تولید موسیقی با ارائه‌دهندگان پیکربندی‌شده، موسیقی یا صدا بسازد — در حال حاضر Google، MiniMax، و ComfyUI پیکربندی‌شده با گردش کار.

برای اجرای عامل‌های مبتنی بر نشست، OpenClaw تولید موسیقی را به‌عنوان یک وظیفه پس‌زمینه آغاز می‌کند، آن را در دفتر وظایف دنبال می‌کند، سپس وقتی قطعه آماده شد عامل را دوباره بیدار می‌کند تا عامل بتواند به کاربر اطلاع دهد و صدای نهایی را پیوست کند. در گفت‌وگوهای گروهی/کانالی که از تحویل قابل مشاهده فقط با ابزار پیام استفاده می‌کنند، عامل نتیجه را از طریق ابزار پیام منتقل می‌کند. اگر عامل تکمیل فقط یک پاسخ نهایی خصوصی بنویسد، OpenClaw به ارسال مستقیم کانال همراه با رسانه تولیدشده برمی‌گردد. بیدارسازی تکمیل به‌صراحت به عامل هشدار می‌دهد که پاسخ‌های نهایی معمولی در آن مسیرها خصوصی هستند.

## شروع سریع

### پشتیبانی‌شده با ارائه‌دهنده مشترک

* ### پیکربندی احراز هویت

برای حداقل یک ارائه‌دهنده یک کلید API تنظیم کنید — برای نمونه `GEMINI_API_KEY` یا `MINIMAX_API_KEY`.

* ### انتخاب یک مدل پیش‌فرض (اختیاری)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### درخواست از عامل

_"Generate an upbeat synthpop track about a night drive through a neon city."_

عامل به‌طور خودکار `music_generate` را فراخوانی می‌کند. نیازی به فهرست مجاز ابزار نیست.

برای زمینه‌های همگام مستقیم بدون اجرای عامل مبتنی بر نشست، ابزار داخلی همچنان به تولید درون‌خطی برمی‌گردد و مسیر رسانه نهایی را در نتیجه ابزار برمی‌گرداند.

### گردش کار ComfyUI

* ### پیکربندی گردش کار

`plugins.entries.comfy.config.music` را با JSON گردش کار و گره‌های درخواست/خروجی پیکربندی کنید.

* ### احراز هویت ابری (اختیاری)

برای Comfy Cloud، `COMFY_API_KEY` یا `COMFY_CLOUD_API_KEY` را تنظیم کنید.

* ### فراخوانی ابزار

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

نمونه درخواست‌ها:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## ارائه‌دهندگان پشتیبانی‌شده

ارائه‌دهنده | مدل پیش‌فرض | ورودی‌های مرجع | کنترل‌های پشتیبانی‌شده | احراز هویت  
---|---|---|---|---  
ComfyUI | `workflow` | تا 1 تصویر | موسیقی یا صدای تعریف‌شده در گردش کار | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | تا 10 تصویر | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | هیچ‌کدام | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` یا MiniMax OAuth  
  
### ماتریس قابلیت‌ها

قرارداد حالت صریحی که توسط `music_generate`، آزمون‌های قرارداد، و پیمایش زنده مشترک استفاده می‌شود:

ارائه‌دهنده | `generate` | `edit` | محدودیت ویرایش | مسیرهای زنده مشترک  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 تصویر | در پیمایش مشترک نیست؛ با `extensions/comfy/comfy.live.test.ts` پوشش داده می‌شود  
Google | ✓ | ✓ | 10 تصویر | `generate`, `edit`  
MiniMax | ✓ | — | هیچ‌کدام | `generate`  
  
برای بررسی ارائه‌دهندگان و مدل‌های مشترک در دسترس در زمان اجرا، از `action: "list"` استفاده کنید:

textCopy code
[code]
    /tool music_generate action=list
[/code]

برای بررسی وظیفه موسیقی فعال مبتنی بر نشست، از `action: "status"` استفاده کنید:

textCopy code
[code]
    /tool music_generate action=status
[/code]

نمونه تولید مستقیم:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## پارامترهای ابزار

درخواست تولید موسیقی. برای `action: "generate"` الزامی است.

`"status"` وظیفه فعلی نشست را برمی‌گرداند؛ `"list"` ارائه‌دهندگان را بررسی می‌کند.

بازنویسی ارائه‌دهنده/مدل (مانند `google/lyria-3-pro-preview`, `comfy/workflow`).

متن اختیاری ترانه وقتی ارائه‌دهنده از ورودی صریح متن ترانه پشتیبانی می‌کند.

وقتی ارائه‌دهنده پشتیبانی می‌کند، خروجی فقط بی‌کلام درخواست کنید.

مسیر یا URL یک تصویر مرجع واحد.

چندین تصویر مرجع (تا 10 مورد در ارائه‌دهندگان پشتیبان).

مدت هدف بر حسب ثانیه وقتی ارائه‌دهنده از راهنمایی مدت پشتیبانی می‌کند.

راهنمای قالب خروجی وقتی ارائه‌دهنده از آن پشتیبانی می‌کند.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg زمان‌پایان اختیاری درخواست ارائه‌دهنده بر حسب میلی‌ثانیه. وقتی حذف شود، اگر `agents.defaults.musicGenerationModel.timeoutMs` پیکربندی شده باشد، OpenClaw از آن استفاده می‌کند. مقادیر کمتر از 10000ms به 10000ms افزایش داده می‌شوند و در نتیجه ابزار گزارش می‌شوند. OPENCLAW_DOCS_MARKER:paramClose:

## رفتار ناهمگام

تولید موسیقی مبتنی بر نشست به‌عنوان یک وظیفه پس‌زمینه اجرا می‌شود:

  * **وظیفه پس‌زمینه:** `music_generate` یک وظیفه پس‌زمینه ایجاد می‌کند، بلافاصله یک پاسخ شروع‌شده/وظیفه برمی‌گرداند، و قطعه نهایی را بعدا در یک پیام پیگیری عامل ارسال می‌کند.
  * **جلوگیری از تکرار:** تا وقتی یک وظیفه `queued` یا `running` است، فراخوانی‌های بعدی `music_generate` در همان نشست به‌جای آغاز تولید دیگر، وضعیت وظیفه را برمی‌گردانند. برای بررسی صریح از `action: "status"` استفاده کنید.
  * **جست‌وجوی وضعیت:** `openclaw tasks list` یا `openclaw tasks show <taskId>` وضعیت‌های در صف، در حال اجرا، و پایانی را بررسی می‌کند.
  * **بیدارسازی تکمیل:** OpenClaw یک رویداد تکمیل داخلی را دوباره به همان نشست تزریق می‌کند تا مدل بتواند خودش پیگیری قابل مشاهده برای کاربر را بنویسد.
  * **راهنمای درخواست:** نوبت‌های بعدی کاربر/دستی در همان نشست، وقتی یک وظیفه موسیقی از قبل در جریان باشد، یک راهنمای کوچک زمان اجرا دریافت می‌کنند تا مدل کورکورانه دوباره `music_generate` را فراخوانی نکند.
  * **بازگشت بدون نشست:** زمینه‌های مستقیم/محلی بدون نشست واقعی عامل به‌صورت درون‌خطی اجرا می‌شوند و نتیجه نهایی صدا را در همان نوبت برمی‌گردانند.


### چرخه عمر وظیفه

وضعیت | معنی  
---|---  
`queued` | وظیفه ایجاد شده و منتظر پذیرش آن توسط ارائه‌دهنده است.  
`running` | ارائه‌دهنده در حال پردازش است (معمولا 30 ثانیه تا 3 دقیقه بسته به ارائه‌دهنده و مدت).  
`succeeded` | قطعه آماده است؛ عامل بیدار می‌شود و آن را در گفت‌وگو ارسال می‌کند.  
`failed` | خطای ارائه‌دهنده یا زمان‌پایان؛ عامل با جزئیات خطا بیدار می‌شود.  
  
بررسی وضعیت از CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## پیکربندی

### انتخاب مدل

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### ترتیب انتخاب ارائه‌دهنده

OpenClaw ارائه‌دهندگان را به این ترتیب امتحان می‌کند:

  1. پارامتر `model` از فراخوانی ابزار (اگر عامل یکی مشخص کند).
  2. `musicGenerationModel.primary` از پیکربندی.
  3. `musicGenerationModel.fallbacks` به‌ترتیب.
  4. تشخیص خودکار فقط با استفاده از پیش‌فرض‌های ارائه‌دهنده مبتنی بر احراز هویت: 
     * ابتدا ارائه‌دهنده پیش‌فرض فعلی؛
     * سپس باقی ارائه‌دهندگان ثبت‌شده تولید موسیقی به‌ترتیب شناسه ارائه‌دهنده.


اگر یک ارائه‌دهنده شکست بخورد، نامزد بعدی به‌طور خودکار امتحان می‌شود. اگر همه شکست بخورند، خطا شامل جزئیات هر تلاش خواهد بود.

برای استفاده فقط از ورودی‌های صریح `model`، `primary`، و `fallbacks`، `agents.defaults.mediaGenerationAutoProviderFallback: false` را تنظیم کنید.

## نکات ارائه‌دهنده

ComfyUI

مبتنی بر گردش کار است و به گراف پیکربندی‌شده به‌همراه نگاشت گره‌ها برای فیلدهای درخواست/خروجی وابسته است. Plugin داخلی `comfy` از طریق رجیستری ارائه‌دهنده تولید موسیقی به ابزار مشترک `music_generate` متصل می‌شود.

Google (Lyria 3)

از تولید دسته‌ای Lyria 3 استفاده می‌کند. جریان داخلی فعلی از درخواست، متن اختیاری ترانه، و تصاویر مرجع اختیاری پشتیبانی می‌کند.

MiniMax

از نقطه پایانی دسته‌ای `music_generation` استفاده می‌کند. از درخواست، متن اختیاری ترانه، حالت بی‌کلام، هدایت مدت، و خروجی mp3 از طریق احراز هویت کلید API `minimax` یا OAuth `minimax-portal` پشتیبانی می‌کند.

## انتخاب مسیر مناسب

  * **پشتیبانی‌شده با ارائه‌دهنده مشترک** وقتی انتخاب مدل، جایگزینی خودکار ارائه‌دهنده، و جریان داخلی ناهمگام وظیفه/وضعیت را می‌خواهید.
  * **مسیر Plugin (ComfyUI)** وقتی به یک گراف گردش کار سفارشی یا ارائه‌دهنده‌ای نیاز دارید که بخشی از قابلیت موسیقی مشترک داخلی نیست.


اگر در حال اشکال‌زدایی رفتار مختص ComfyUI هستید، [ComfyUI](</fa/providers/comfy>) را ببینید. اگر در حال اشکال‌زدایی رفتار ارائه‌دهنده مشترک هستید، با [Google (Gemini)](</fa/providers/google>) یا [MiniMax](</fa/providers/minimax>) شروع کنید.

## حالت‌های قابلیت ارائه‌دهنده

قرارداد مشترک تولید موسیقی از اعلام حالت‌های صریح پشتیبانی می‌کند:

  * `generate` برای تولید فقط با درخواست.
  * `edit` وقتی درخواست شامل یک یا چند تصویر مرجع است.


پیاده‌سازی‌های جدید ارائه‌دهنده بهتر است از بلوک‌های حالت صریح استفاده کنند:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

فیلدهای تخت قدیمی مانند `maxInputImages`، `supportsLyrics`، و `supportsFormat` برای اعلام پشتیبانی از ویرایش **کافی نیستند**. ارائه‌دهندگان باید `generate` و `edit` را به‌صراحت اعلام کنند تا آزمون‌های زنده، آزمون‌های قرارداد، و ابزار مشترک `music_generate` بتوانند پشتیبانی حالت را به‌صورت قطعی اعتبارسنجی کنند.

## آزمون‌های زنده

پوشش زنده اختیاری برای ارائه‌دهندگان داخلی مشترک:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

پوشش‌دهنده repo:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

این فایل live متغیرهای محیطی ارائه‌دهنده را که وجود ندارند از `~/.profile` بارگذاری می‌کند، به‌طور پیش‌فرض کلیدهای API زنده/محیطی را بر پروفایل‌های احراز هویت ذخیره‌شده ترجیح می‌دهد، و وقتی ارائه‌دهنده حالت ویرایش را فعال کرده باشد، هم پوشش `generate` و هم پوشش اعلام‌شدهٔ `edit` را اجرا می‌کند. پوشش فعلی:

  * `google`: `generate` به‌همراه `edit`
  * `minimax`: فقط `generate`
  * `comfy`: پوشش زندهٔ جداگانهٔ Comfy، نه sweep مشترک ارائه‌دهنده


برای پوشش زندهٔ مسیر موسیقی ComfyUI همراه‌شده، به‌صورت opt-in فعال کنید:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

فایل live مربوط به Comfy همچنین وقتی آن بخش‌ها پیکربندی شده باشند، گردش‌کارهای تصویر و ویدیوی comfy را پوشش می‌دهد.

## مرتبط

  * [وظایف پس‌زمینه](</fa/automation/tasks>) — پیگیری وظایف برای اجرای جداشدهٔ `music_generate`
  * [ComfyUI](</fa/providers/comfy>)
  * [مرجع پیکربندی](</fa/gateway/config-agents#agent-defaults>) — پیکربندی `musicGenerationModel`
  * [Google (Gemini)](</fa/providers/google>)
  * [MiniMax](</fa/providers/minimax>)
  * [مدل‌ها](</fa/concepts/models>) — پیکربندی مدل و failover
  * [نمای کلی ابزارها](</fa/tools>)


Was this useful?YesNo