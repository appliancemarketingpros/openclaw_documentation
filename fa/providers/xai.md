---
title: xAI
source_url: https://docs.openclaw.ai/fa/providers/xai
scraped_at: 2026-05-25
---

OpenClaw یک Plugin ارائه‌دهنده‌ی bundled به نام `xai` برای مدل‌های Grok ارائه می‌کند.

## شروع به کار

* ### ساخت کلید API

یک کلید API در [کنسول xAI](<https://console.x.ai/>) بسازید.

* ### تنظیم کلید API

`XAI_API_KEY` را تنظیم کنید، یا اجرا کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### انتخاب مدل

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## کاتالوگ داخلی

OpenClaw این خانواده‌های مدل xAI را به‌صورت پیش‌فرض شامل می‌شود:

خانواده | شناسه‌های مدل  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
این Plugin همچنین شناسه‌های جدیدتر `grok-4*` و `grok-code-fast*` را، وقتی از همان شکل API پیروی کنند، به‌صورت forward-resolve حل می‌کند.

## پوشش قابلیت‌های OpenClaw

Plugin bundled سطح API عمومی فعلی xAI را روی قراردادهای مشترک ارائه‌دهنده و ابزار OpenClaw نگاشت می‌کند. قابلیت‌هایی که با قرارداد مشترک سازگار نیستند (برای مثال TTS استریم‌شونده و صدای بلادرنگ) در معرض استفاده قرار نمی‌گیرند - جدول زیر را ببینید.

قابلیت xAI | سطح OpenClaw | وضعیت  
---|---|---  
چت / پاسخ‌ها | ارائه‌دهنده‌ی مدل `xai/<model>` | بله  
جست‌وجوی وب سمت سرور | ارائه‌دهنده‌ی `web_search` با `grok` | بله  
جست‌وجوی X سمت سرور | ابزار `x_search` | بله  
اجرای کد سمت سرور | ابزار `code_execution` | بله  
تصاویر | `image_generate` | بله  
ویدیوها | `video_generate` | بله  
تبدیل متن به گفتار batch | `messages.tts.provider: "xai"` / `tts` | بله  
TTS استریم‌شونده | - | در معرض استفاده نیست؛ قرارداد TTS در OpenClaw بافرهای کامل صوتی برمی‌گرداند  
تبدیل گفتار به متن batch | `tools.media.audio` / درک رسانه | بله  
تبدیل گفتار به متن استریم‌شونده | Voice Call `streaming.provider: "xai"` | بله  
صدای بلادرنگ | - | هنوز در معرض استفاده نیست؛ قرارداد نشست/WebSocket متفاوتی دارد  
فایل‌ها / batchها | فقط سازگاری عمومی API مدل | ابزار first-class OpenClaw نیست  
  
### نگاشت‌های حالت سریع

`/fast on` یا `agents.defaults.models["xai/<model>"].params.fastMode: true` درخواست‌های بومی xAI را به‌صورت زیر بازنویسی می‌کند:

مدل مبدا | هدف حالت سریع  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### نام‌های مستعار سازگاری legacy

نام‌های مستعار legacy همچنان به شناسه‌های canonical bundled نرمال‌سازی می‌شوند:

نام مستعار legacy | شناسه canonical  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## قابلیت‌ها

جست‌وجوی وب

ارائه‌دهنده‌ی bundled جست‌وجوی وب `grok` می‌تواند از `XAI_API_KEY` یا یک کلید جست‌وجوی وب Plugin استفاده کند:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

تولید ویدیو

Plugin bundled `xai` تولید ویدیو را از طریق ابزار مشترک `video_generate` ثبت می‌کند.

  * مدل ویدیوی پیش‌فرض: `xai/grok-imagine-video`
  * حالت‌ها: متن به ویدیو، تصویر به ویدیو، تولید تصویر مرجع، ویرایش ویدیوی راه‌دور، و گسترش ویدیوی راه‌دور
  * نسبت‌های تصویر: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * وضوح‌ها: `480P`, `720P`
  * مدت: 1-15 ثانیه برای تولید/تصویر به ویدیو، 1-10 ثانیه هنگام استفاده از نقش‌های `reference_image`، 2-10 ثانیه برای گسترش
  * تولید تصویر مرجع: `imageRoles` را برای هر تصویر ارائه‌شده روی `reference_image` تنظیم کنید؛ xAI تا 7 تصویر از این نوع را می‌پذیرد


برای استفاده از xAI به‌عنوان ارائه‌دهنده‌ی پیش‌فرض ویدیو:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

تولید تصویر

Plugin bundled `xai` تولید تصویر را از طریق ابزار مشترک `image_generate` ثبت می‌کند.

  * مدل تصویر پیش‌فرض: `xai/grok-imagine-image`
  * مدل اضافی: `xai/grok-imagine-image-pro`
  * حالت‌ها: متن به تصویر و ویرایش تصویر مرجع
  * ورودی‌های مرجع: یک `image` یا حداکثر پنج `images`
  * نسبت‌های تصویر: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * وضوح‌ها: `1K`, `2K`
  * تعداد: حداکثر 4 تصویر


OpenClaw از xAI پاسخ‌های تصویری `b64_json` درخواست می‌کند تا رسانه‌ی تولیدشده بتواند از مسیر معمول پیوست کانال ذخیره و تحویل داده شود. تصاویر مرجع محلی به URLهای داده‌ای تبدیل می‌شوند؛ مراجع راه‌دور `http(s)` بدون تغییر عبور داده می‌شوند.

برای استفاده از xAI به‌عنوان ارائه‌دهنده‌ی پیش‌فرض تصویر:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

تبدیل متن به گفتار

Plugin bundled `xai` تبدیل متن به گفتار را از طریق سطح مشترک ارائه‌دهنده‌ی `tts` ثبت می‌کند.

  * صداها: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * صدای پیش‌فرض: `eve`
  * فرمت‌ها: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * زبان: کد BCP-47 یا `auto`
  * سرعت: override سرعت بومی ارائه‌دهنده
  * فرمت بومی voice-note با Opus پشتیبانی نمی‌شود


برای استفاده از xAI به‌عنوان ارائه‌دهنده‌ی پیش‌فرض TTS:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

تبدیل گفتار به متن

Plugin bundled `xai` تبدیل گفتار به متن batch را از طریق سطح رونویسی درک رسانه‌ی OpenClaw ثبت می‌کند.

  * مدل پیش‌فرض: `grok-stt`
  * endpoint: xAI REST `/v1/stt`
  * مسیر ورودی: بارگذاری فایل صوتی multipart
  * در OpenClaw هرجا رونویسی صوت ورودی از `tools.media.audio` استفاده کند پشتیبانی می‌شود، از جمله بخش‌های کانال صوتی Discord و پیوست‌های صوتی کانال


برای اجبار xAI برای رونویسی صوت ورودی:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

زبان می‌تواند از طریق پیکربندی مشترک رسانه‌ی صوتی یا درخواست رونویسی در هر فراخوانی ارائه شود. راهنمایی‌های prompt توسط سطح مشترک OpenClaw پذیرفته می‌شوند، اما یکپارچه‌سازی xAI REST STT فقط فایل، مدل، و زبان را forward می‌کند، زیرا این‌ها به‌شکل تمیز با endpoint عمومی فعلی xAI نگاشت می‌شوند.

تبدیل گفتار به متن استریم‌شونده

Plugin bundled `xai` همچنین یک ارائه‌دهنده‌ی رونویسی بلادرنگ برای صوت تماس صوتی زنده ثبت می‌کند.

  * endpoint: xAI WebSocket `wss://api.x.ai/v1/stt`
  * کدگذاری پیش‌فرض: `mulaw`
  * نرخ نمونه‌برداری پیش‌فرض: `8000`
  * endpointing پیش‌فرض: `800ms`
  * رونوشت‌های موقت: به‌صورت پیش‌فرض فعال است


استریم رسانه‌ی Twilio در Voice Call فریم‌های صوتی G.711 µ-law ارسال می‌کند، بنابراین ارائه‌دهنده‌ی xAI می‌تواند آن فریم‌ها را بدون transcode مستقیم forward کند:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

پیکربندی متعلق به ارائه‌دهنده زیر `plugins.entries.voice-call.config.streaming.providers.xai` قرار می‌گیرد. کلیدهای پشتیبانی‌شده عبارت‌اند از `apiKey`، `baseUrl`، `sampleRate`، `encoding` (`pcm`، `mulaw`، یا `alaw`)، `interimResults`، `endpointingMs`، و `language`.

پیکربندی x_search

Plugin همراه xAI، `x_search` را به‌عنوان یک ابزار OpenClaw برای جست‌وجوی محتوای X (که پیش‌تر Twitter بود) از طریق Grok ارائه می‌کند.

مسیر پیکربندی: `plugins.entries.xai.config.xSearch`

کلید | نوع | پیش‌فرض | توضیح  
---|---|---|---  
`enabled` | boolean | - | فعال یا غیرفعال کردن x_search  
`model` | string | `grok-4-1-fast` | مدل استفاده‌شده برای درخواست‌های x_search  
`baseUrl` | string | - | بازنویسی URL پایه xAI Responses  
`inlineCitations` | boolean | - | افزودن ارجاع‌های درون‌خطی در نتایج  
`maxTurns` | number | - | بیشینه نوبت‌های مکالمه  
`timeoutSeconds` | number | - | مهلت زمانی درخواست برحسب ثانیه  
`cacheTtlMinutes` | number | - | مدت زنده‌ماندن کش برحسب دقیقه  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

پیکربندی اجرای کد

Plugin همراه xAI، `code_execution` را به‌عنوان یک ابزار OpenClaw برای اجرای کد از راه دور در محیط سندباکس xAI ارائه می‌کند.

مسیر پیکربندی: `plugins.entries.xai.config.codeExecution`

کلید | نوع | پیش‌فرض | توضیح  
---|---|---|---  
`enabled` | boolean | `true` (اگر کلید موجود باشد) | فعال یا غیرفعال کردن اجرای کد  
`model` | string | `grok-4-1-fast` | مدل استفاده‌شده برای درخواست‌های اجرای کد  
`maxTurns` | number | - | بیشینه نوبت‌های مکالمه  
`timeoutSeconds` | number | - | مهلت زمانی درخواست برحسب ثانیه  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

محدودیت‌های شناخته‌شده

  * احراز هویت امروز فقط با کلید API انجام می‌شود. کلید API می‌تواند در یک پروفایل احراز هویت xAI، متغیر محیطی، یا پیکربندی Plugin ذخیره شود؛ هنوز هیچ جریان xAI OAuth یا device-code در OpenClaw وجود ندارد.
  * `grok-4.20-multi-agent-experimental-beta-0304` در مسیر عادی ارائه‌دهنده xAI پشتیبانی نمی‌شود، زیرا به سطح API بالادستی متفاوتی نسبت به ترنسپورت استاندارد xAI در OpenClaw نیاز دارد.
  * صدای xAI Realtime هنوز به‌عنوان یک ارائه‌دهنده OpenClaw ثبت نشده است. این مورد به قرارداد نشست صدای دوسویه متفاوتی نسبت به STT دسته‌ای یا رونویسی استریمینگ نیاز دارد.
  * `quality` تصویر xAI، `mask` تصویر، و نسبت‌های ابعاد اضافی فقط-بومی تا زمانی که ابزار مشترک `image_generate` کنترل‌های متناظر میان‌ارائه‌دهنده داشته باشد، ارائه نمی‌شوند.

نکات پیشرفته

  * OpenClaw اصلاحات سازگاری طرح‌واره ابزار و فراخوانی ابزار ویژه xAI را به‌صورت خودکار روی مسیر رانر مشترک اعمال می‌کند.
  * درخواست‌های بومی xAI به‌طور پیش‌فرض `tool_stream: true` دارند. برای غیرفعال کردن آن، `agents.defaults.models["xai/<model>"].params.tool_stream` را روی `false` تنظیم کنید.
  * wrapper همراه xAI، پرچم‌های strict پشتیبانی‌نشده در طرح‌واره ابزار و کلیدهای payload استدلال را پیش از ارسال درخواست‌های بومی xAI حذف می‌کند.
  * `web_search`، `x_search`، و `code_execution` به‌عنوان ابزارهای OpenClaw ارائه می‌شوند. OpenClaw به‌جای پیوست کردن همه ابزارهای بومی به هر نوبت گفت‌وگو، built-in خاص xAI موردنیاز را داخل هر درخواست ابزار فعال می‌کند.
  * `web_search` در Grok مقدار `plugins.entries.xai.config.webSearch.baseUrl` را می‌خواند. `x_search` مقدار `plugins.entries.xai.config.xSearch.baseUrl` را می‌خواند، سپس به URL پایه جست‌وجوی وب Grok برمی‌گردد.
  * `x_search` و `code_execution` متعلق به Plugin همراه xAI هستند، نه اینکه در runtime مدل هسته hardcode شده باشند.
  * `code_execution` اجرای سندباکس xAI از راه دور است، نه [`exec`](</fa/tools/exec>) محلی.


## آزمون زنده

مسیرهای رسانه xAI با تست‌های واحد و مجموعه‌های زنده اختیاری پوشش داده شده‌اند. فرمان‌های زنده، secrets را پیش از بررسی `XAI_API_KEY` از login shell شما، از جمله `~/.profile`، بارگذاری می‌کنند.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

فایل زنده ویژه ارائه‌دهنده، TTS عادی، TTS مبتنی بر PCM مناسب تلفن، رونویسی صدا از طریق STT دسته‌ای xAI، استریم همان PCM از طریق STT بلادرنگ xAI، تولید خروجی متن‌به‌تصویر، و ویرایش یک تصویر مرجع را تولید می‌کند. فایل زنده مشترک تصویر، همان ارائه‌دهنده xAI را از طریق مسیر انتخاب runtime، fallback، نرمال‌سازی، و پیوست رسانه در OpenClaw تأیید می‌کند.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهنده‌ها، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**تولید ویدیو** پارامترهای ابزار ویدیوی مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**همه ارائه‌دهنده‌ها** نمای کلی گسترده‌تر ارائه‌دهنده‌ها. ](</fa/providers>) [**عیب‌یابی** مشکلات رایج و راه‌حل‌ها. ](</fa/help/troubleshooting>)

Was this useful?YesNo