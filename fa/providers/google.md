---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/fa/providers/google
scraped_at: 2026-05-25
---

Plugin ‏Google از طریق Google AI Studio دسترسی به مدل‌های Gemini را فراهم می‌کند، به‌علاوه تولید تصویر، درک رسانه (تصویر/صدا/ویدیو)، تبدیل متن به گفتار، و جست‌وجوی وب از طریق Gemini Grounding.

  * ارائه‌دهنده: `google`
  * احراز هویت: `GEMINI_API_KEY` یا `GOOGLE_API_KEY`
  * API: Google Gemini API
  * گزینه زمان اجرا: provider/model ‏`agentRuntime.id: "google-gemini-cli"` از OAuth ‏Gemini CLI دوباره استفاده می‌کند و در عین حال ارجاع‌های مدل را به‌صورت canonical یعنی `google/*` نگه می‌دارد.


## شروع به کار

روش احراز هویت دلخواه خود را انتخاب کنید و مراحل راه‌اندازی را دنبال کنید.

### API key

**مناسب برای:** دسترسی استاندارد به Gemini API از طریق Google AI Studio.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

یا کلید را مستقیم ارسال کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**مناسب برای:** استفاده دوباره از ورود موجود Gemini CLI از طریق PKCE OAuth به‌جای یک کلید API جداگانه.

* ### Install the Gemini CLI

دستور محلی `gemini` باید در `PATH` در دسترس باشد.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw هم نصب‌های Homebrew و هم نصب‌های global ‏npm را پشتیبانی می‌کند، از جمله چیدمان‌های رایج Windows/npm.

* ### Log in via OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * مدل پیش‌فرض: `google/gemini-3.1-pro-preview`
  * زمان اجرا: `google-gemini-cli`
  * نام مستعار: `gemini-cli`


شناسه مدل Gemini API برای Gemini 3.1 Pro برابر `gemini-3.1-pro-preview` است. OpenClaw نام کوتاه‌تر `google/gemini-3.1-pro` را به‌عنوان نام مستعار کاربردی می‌پذیرد و پیش از فراخوانی‌های ارائه‌دهنده آن را normalizes می‌کند.

**متغیرهای محیطی:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(یا گونه‌های `GEMINI_CLI_*`.)

ارجاع‌های مدل `google-gemini-cli/*` نام‌های مستعار سازگاری قدیمی هستند. پیکربندی‌های جدید باید از ارجاع‌های مدل `google/*` به‌همراه زمان اجرای `google-gemini-cli` استفاده کنند وقتی اجرای محلی Gemini CLI را می‌خواهند.

## قابلیت‌ها

قابلیت | پشتیبانی‌شده  
---|---  
تکمیل‌های چت | بله  
تولید تصویر | بله  
تولید موسیقی | بله  
تبدیل متن به گفتار | بله  
صدای بلادرنگ | بله (Google Live API)  
درک تصویر | بله  
رونویسی صدا | بله  
درک ویدیو | بله  
جست‌وجوی وب (Grounding) | بله  
تفکر/استدلال | بله (Gemini 2.5+ / Gemini 3+)  
مدل‌های Gemma 4 | بله  
  
## جست‌وجوی وب

ارائه‌دهنده جست‌وجوی وب داخلی `gemini` از grounding جست‌وجوی Google در Gemini استفاده می‌کند. یک کلید جست‌وجوی اختصاصی را زیر `plugins.entries.google.config.webSearch` پیکربندی کنید، یا اجازه دهید پس از `GEMINI_API_KEY` از `models.providers.google.apiKey` دوباره استفاده کند:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

اولویت اعتبارنامه ابتدا `webSearch.apiKey`، سپس `GEMINI_API_KEY`، و سپس `models.providers.google.apiKey` است. `webSearch.baseUrl` اختیاری است و برای پروکسی‌های اپراتور یا endpointهای سازگار با Gemini API وجود دارد؛ وقتی حذف شود، جست‌وجوی وب Gemini از `models.providers.google.baseUrl` دوباره استفاده می‌کند. برای رفتار ابزار ویژه ارائه‌دهنده، [جست‌وجوی Gemini](</fa/tools/gemini-search>) را ببینید.

## تولید تصویر

ارائه‌دهنده تولید تصویر داخلی `google` به‌طور پیش‌فرض از `google/gemini-3.1-flash-image-preview` استفاده می‌کند.

  * همچنین از `google/gemini-3-pro-image-preview` پشتیبانی می‌کند
  * تولید: تا 4 تصویر در هر درخواست
  * حالت ویرایش: فعال، تا 5 تصویر ورودی
  * کنترل‌های هندسه: `size`، `aspectRatio`، و `resolution`


برای استفاده از Google به‌عنوان ارائه‌دهنده پیش‌فرض تصویر:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## تولید ویدیو

Plugin داخلی `google` همچنین تولید ویدیو را از طریق ابزار مشترک `video_generate` ثبت می‌کند.

  * مدل ویدیوی پیش‌فرض: `google/veo-3.1-fast-generate-preview`
  * حالت‌ها: متن‌به‌ویدیو، تصویر‌به‌ویدیو، و جریان‌های مرجع تک‌ویدیو
  * از `aspectRatio` (`16:9`، `9:16`) و `resolution` (`720P`، `1080P`) پشتیبانی می‌کند؛ خروجی صدا امروزه توسط Veo پشتیبانی نمی‌شود
  * مدت‌های پشتیبانی‌شده: **4، 6، یا 8 ثانیه** (مقادیر دیگر به نزدیک‌ترین مقدار مجاز چفت می‌شوند)


برای استفاده از Google به‌عنوان ارائه‌دهنده پیش‌فرض ویدیو:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## تولید موسیقی

Plugin داخلی `google` همچنین تولید موسیقی را از طریق ابزار مشترک `music_generate` ثبت می‌کند.

  * مدل موسیقی پیش‌فرض: `google/lyria-3-clip-preview`
  * همچنین از `google/lyria-3-pro-preview` پشتیبانی می‌کند
  * کنترل‌های prompt: `lyrics` و `instrumental`
  * قالب خروجی: به‌طور پیش‌فرض `mp3`، به‌علاوه `wav` روی `google/lyria-3-pro-preview`
  * ورودی‌های مرجع: تا 10 تصویر
  * اجراهای متکی به session از طریق جریان مشترک task/status جدا می‌شوند، از جمله `action: "status"`


برای استفاده از Google به‌عنوان ارائه‌دهنده پیش‌فرض موسیقی:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## تبدیل متن به گفتار

ارائه‌دهنده گفتار داخلی `google` از مسیر TTS در Gemini API با `gemini-3.1-flash-tts-preview` استفاده می‌کند.

  * صدای پیش‌فرض: `Kore`
  * احراز هویت: `messages.tts.providers.google.apiKey`، `models.providers.google.apiKey`، `GEMINI_API_KEY`، یا `GOOGLE_API_KEY`
  * خروجی: WAV برای پیوست‌های معمول TTS، ‏Opus برای مقصدهای یادداشت صوتی، PCM برای Talk/telephony
  * خروجی یادداشت صوتی: Google PCM به‌صورت WAV بسته‌بندی می‌شود و با `ffmpeg` به Opus با 48 kHz ترنسکد می‌شود


مسیر batch ‏Gemini TTS در Google، صدای تولیدشده را در پاسخ کامل‌شده `generateContent` برمی‌گرداند. برای مکالمه‌های گفتاری با کمترین تاخیر، به‌جای batch TTS از ارائه‌دهنده صدای بلادرنگ Google با پشتوانه Gemini Live API استفاده کنید.

برای استفاده از Google به‌عنوان ارائه‌دهنده پیش‌فرض TTS:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS برای کنترل سبک از prompt‌نویسی زبان طبیعی استفاده می‌کند. `audioProfile` را تنظیم کنید تا یک prompt سبک قابل استفاده‌مجدد پیش از متن گفتاری اضافه شود. وقتی متن prompt شما به یک گوینده نام‌دار اشاره می‌کند، `speakerName` را تنظیم کنید.

Gemini API TTS همچنین tagهای صوتی بیانی داخل کروشه را در متن می‌پذیرد، مانند `[whispers]` یا `[laughs]`. برای اینکه tagها از پاسخ چت قابل مشاهده بیرون بمانند اما به TTS ارسال شوند، آن‌ها را داخل یک بلوک `[[tts:text]]...[[/tts:text]]` قرار دهید:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## صدای بلادرنگ

Plugin داخلی `google` یک ارائه‌دهنده صدای بلادرنگ را ثبت می‌کند که برای پل‌های صوتی backend مانند Voice Call و Google Meet، با Gemini Live API پشتیبانی می‌شود.

تنظیم | مسیر پیکربندی | پیش‌فرض  
---|---|---  
مدل | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
صدا | `...google.voice` | `Kore`  
دما | `...google.temperature` | (تنظیم‌نشده)  
حساسیت شروع VAD | `...google.startSensitivity` | (تنظیم‌نشده)  
حساسیت پایان VAD | `...google.endSensitivity` | (تنظیم‌نشده)  
مدت سکوت | `...google.silenceDurationMs` | (تنظیم‌نشده)  
رسیدگی به فعالیت | `...google.activityHandling` | پیش‌فرض Google، `start-of-activity-interrupts`  
پوشش نوبت | `...google.turnCoverage` | پیش‌فرض Google، `only-activity`  
غیرفعال کردن VAD خودکار | `...google.automaticActivityDetectionDisabled` | `false`  
ازسرگیری نشست | `...google.sessionResumption` | `true`  
فشرده‌سازی زمینه | `...google.contextWindowCompression` | `true`  
کلید API | `...google.apiKey` | به `models.providers.google.apiKey`، `GEMINI_API_KEY`، یا `GOOGLE_API_KEY` بازمی‌گردد  
  
نمونه پیکربندی بلادرنگ تماس صوتی:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

برای راستی‌آزمایی زنده نگه‌دارنده، اجرا کنید: `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. این smoke همچنین مسیرهای پشتیبان OpenAI/WebRTC را پوشش می‌دهد؛ بخش Google همان شکل توکن محدود Live API را که Control UI Talk استفاده می‌کند صادر می‌کند، نقطه پایانی WebSocket مرورگر را باز می‌کند، payload راه‌اندازی اولیه را می‌فرستد و منتظر `setupComplete` می‌ماند.

## پیکربندی پیشرفته

استفاده دوباره مستقیم از کش Gemini

برای اجرای مستقیم Gemini API (`api: "google-generative-ai"`)، OpenClaw یک شناسه `cachedContent` پیکربندی‌شده را به درخواست‌های Gemini عبور می‌دهد.

  * پارامترهای سراسری یا مختص هر مدل را با یکی از `cachedContent` یا `cached_content` قدیمی پیکربندی کنید
  * اگر هر دو وجود داشته باشند، `cachedContent` اولویت دارد
  * مقدار نمونه: `cachedContents/prebuilt-context`
  * مصرف hit کش Gemini از `cachedContentTokenCount` بالادستی به `cacheRead` در OpenClaw نرمال‌سازی می‌شود

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

یادداشت‌های استفاده JSON برای Gemini CLI

هنگام استفاده از ارائه‌دهنده OAuth مربوط به `google-gemini-cli`، OpenClaw خروجی JSON مربوط به CLI را به شکل زیر نرمال‌سازی می‌کند:

  * متن پاسخ از فیلد `response` در JSON مربوط به CLI می‌آید.
  * وقتی CLI مقدار `usage` را خالی می‌گذارد، مصرف به `stats` بازمی‌گردد.
  * `stats.cached` به `cacheRead` در OpenClaw نرمال‌سازی می‌شود.
  * اگر `stats.input` وجود نداشته باشد، OpenClaw توکن‌های ورودی را از `stats.input_tokens - stats.cached` استخراج می‌کند.

محیط و راه‌اندازی daemon

اگر Gateway به‌صورت daemon اجرا می‌شود (launchd/systemd)، مطمئن شوید `GEMINI_API_KEY` برای آن فرایند در دسترس است (برای مثال، در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**تولید تصویر** پارامترهای ابزار تصویر مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/image-generation>) [**تولید ویدیو** پارامترهای ابزار ویدیوی مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**تولید موسیقی** پارامترهای ابزار موسیقی مشترک و انتخاب ارائه‌دهنده. ](</fa/tools/music-generation>)

Was this useful?YesNo