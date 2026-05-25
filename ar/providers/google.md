---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/ar/providers/google
scraped_at: 2026-05-25
---

يوفّر Google Plugin إمكانية الوصول إلى نماذج Gemini عبر Google AI Studio، إضافةً إلى توليد الصور، وفهم الوسائط (الصور/الصوت/الفيديو)، وتحويل النص إلى كلام، والبحث على الويب عبر Gemini Grounding.

  * المزوّد: `google`
  * المصادقة: `GEMINI_API_KEY` أو `GOOGLE_API_KEY`
  * API: Google Gemini API
  * خيار وقت التشغيل: المزوّد/النموذج `agentRuntime.id: "google-gemini-cli"` يعيد استخدام Gemini CLI OAuth مع إبقاء مراجع النماذج معيارية بصيغة `google/*`.


## البدء

اختر طريقة المصادقة المفضلة لديك واتبع خطوات الإعداد.

### مفتاح API

**الأفضل لـ:** الوصول القياسي إلى Gemini API عبر Google AI Studio.

* ### تشغيل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

أو مرّر المفتاح مباشرةً:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### تعيين نموذج افتراضي

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### التحقق من توفر النموذج

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**الأفضل لـ:** إعادة استخدام تسجيل دخول Gemini CLI موجود عبر PKCE OAuth بدلًا من مفتاح API منفصل.

* ### تثبيت Gemini CLI

يجب أن يكون الأمر المحلي `gemini` متاحًا على `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

يدعم OpenClaw عمليات التثبيت عبر Homebrew وعمليات التثبيت العالمية عبر npm، بما في ذلك تخطيطات Windows/npm الشائعة.

* ### تسجيل الدخول عبر OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### التحقق من توفر النموذج

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * النموذج الافتراضي: `google/gemini-3.1-pro-preview`
  * وقت التشغيل: `google-gemini-cli`
  * الاسم المستعار: `gemini-cli`


معرّف نموذج Gemini API الخاص بـ Gemini 3.1 Pro هو `gemini-3.1-pro-preview`. يقبل OpenClaw الصيغة الأقصر `google/gemini-3.1-pro` كاسم مستعار للتيسير ويطبّعها قبل استدعاءات المزوّد.

**متغيرات البيئة:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(أو متغيرات `GEMINI_CLI_*`.)

مراجع نماذج `google-gemini-cli/*` هي أسماء مستعارة للتوافق القديم. ينبغي أن تستخدم الإعدادات الجديدة مراجع نماذج `google/*` بالإضافة إلى وقت تشغيل `google-gemini-cli` عندما تريد تنفيذ Gemini CLI محليًا.

## القدرات

القدرة | مدعومة  
---|---  
إكمالات المحادثة | نعم  
توليد الصور | نعم  
توليد الموسيقى | نعم  
تحويل النص إلى كلام | نعم  
الصوت الفوري | نعم (Google Live API)  
فهم الصور | نعم  
تفريغ الصوت | نعم  
فهم الفيديو | نعم  
البحث على الويب (Grounding) | نعم  
التفكير/الاستدلال | نعم (Gemini 2.5+ / Gemini 3+)  
نماذج Gemma 4 | نعم  
  
## البحث على الويب

يستخدم مزوّد البحث على الويب `gemini` المضمّن تأريض Gemini Google Search. اضبط مفتاح بحث مخصصًا ضمن `plugins.entries.google.config.webSearch`، أو دعه يعيد استخدام `models.providers.google.apiKey` بعد `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

أولوية بيانات الاعتماد هي `webSearch.apiKey` المخصص، ثم `GEMINI_API_KEY`، ثم `models.providers.google.apiKey`. يُعد `webSearch.baseUrl` اختياريًا وموجودًا لوكلاء المشغلين أو نقاط نهاية Gemini API المتوافقة؛ وعند حذفه، يعيد بحث الويب في Gemini استخدام `models.providers.google.baseUrl`. راجع [بحث Gemini](</ar/tools/gemini-search>) لمعرفة سلوك الأداة الخاص بالمزوّد.

## توليد الصور

يعتمد مزوّد توليد الصور `google` المضمّن افتراضيًا على `google/gemini-3.1-flash-image-preview`.

  * يدعم أيضًا `google/gemini-3-pro-image-preview`
  * التوليد: حتى 4 صور لكل طلب
  * وضع التحرير: مفعّل، حتى 5 صور إدخال
  * عناصر التحكم الهندسية: `size` و`aspectRatio` و`resolution`


لاستخدام Google كمزوّد الصور الافتراضي:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## توليد الفيديو

يسجّل Google Plugin المضمّن أيضًا توليد الفيديو عبر أداة `video_generate` المشتركة.

  * نموذج الفيديو الافتراضي: `google/veo-3.1-fast-generate-preview`
  * الأوضاع: تحويل النص إلى فيديو، وتحويل الصورة إلى فيديو، وتدفقات مرجع فيديو واحد
  * يدعم `aspectRatio` (`16:9` و`9:16`) و`resolution` (`720P` و`1080P`)؛ لا يدعم Veo إخراج الصوت حاليًا
  * المدد المدعومة: **4 أو 6 أو 8 ثوانٍ** (تُقرّب القيم الأخرى إلى أقرب قيمة مسموح بها)


لاستخدام Google كمزوّد الفيديو الافتراضي:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## توليد الموسيقى

يسجّل Google Plugin المضمّن أيضًا توليد الموسيقى عبر أداة `music_generate` المشتركة.

  * نموذج الموسيقى الافتراضي: `google/lyria-3-clip-preview`
  * يدعم أيضًا `google/lyria-3-pro-preview`
  * عناصر التحكم في الموجه: `lyrics` و`instrumental`
  * تنسيق الإخراج: `mp3` افتراضيًا، بالإضافة إلى `wav` على `google/lyria-3-pro-preview`
  * مدخلات مرجعية: حتى 10 صور
  * تنفصل عمليات التشغيل المدعومة بالجلسات عبر تدفق المهمة/الحالة المشترك، بما في ذلك `action: "status"`


لاستخدام Google كمزوّد الموسيقى الافتراضي:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## تحويل النص إلى كلام

يستخدم مزوّد الكلام `google` المضمّن مسار TTS في Gemini API مع `gemini-3.1-flash-tts-preview`.

  * الصوت الافتراضي: `Kore`
  * المصادقة: `messages.tts.providers.google.apiKey` أو `models.providers.google.apiKey` أو `GEMINI_API_KEY` أو `GOOGLE_API_KEY`
  * الإخراج: WAV لمرفقات TTS العادية، وOpus لأهداف الملاحظات الصوتية، وPCM لـ Talk/الهاتف
  * إخراج الملاحظات الصوتية: يُغلّف Google PCM كـ WAV ويُحوّل إلى Opus بتردد 48 كيلوهرتز باستخدام `ffmpeg`


يعيد مسار Gemini TTS الدفعي من Google الصوت المولّد في استجابة `generateContent` المكتملة. للحصول على محادثات منطوقة بأدنى زمن استجابة، استخدم مزوّد الصوت الفوري من Google المدعوم بـ Gemini Live API بدلًا من TTS الدفعي.

لاستخدام Google كمزوّد TTS الافتراضي:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

يستخدم Gemini API TTS التوجيه باللغة الطبيعية للتحكم في الأسلوب. اضبط `audioProfile` لإضافة موجه أسلوب قابل لإعادة الاستخدام قبل النص المنطوق. اضبط `speakerName` عندما يشير نص الموجه إلى متحدث مسمّى.

يقبل Gemini API TTS أيضًا وسومًا صوتية تعبيرية بين أقواس مربعة في النص، مثل `[whispers]` أو `[laughs]`. لإبقاء الوسوم خارج رد المحادثة المرئي مع إرسالها إلى TTS، ضعها داخل كتلة `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## الصوت الفوري

يسجّل Google Plugin المضمّن مزوّد صوت فوري مدعومًا بـ Gemini Live API لجسور الصوت الخلفية مثل Voice Call وGoogle Meet.

الإعداد | مسار الإعدادات | الافتراضي  
---|---|---  
النموذج | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
الصوت | `...google.voice` | `Kore`  
درجة الحرارة | `...google.temperature` | (غير معيّن)  
حساسية بدء VAD | `...google.startSensitivity` | (غير معيّن)  
حساسية انتهاء VAD | `...google.endSensitivity` | (غير معيّن)  
مدة الصمت | `...google.silenceDurationMs` | (غير معيّن)  
معالجة النشاط | `...google.activityHandling` | افتراضي Google، `start-of-activity-interrupts`  
تغطية الدور | `...google.turnCoverage` | افتراضي Google، `only-activity`  
تعطيل VAD التلقائي | `...google.automaticActivityDetectionDisabled` | `false`  
استئناف الجلسة | `...google.sessionResumption` | `true`  
ضغط السياق | `...google.contextWindowCompression` | `true`  
مفتاح API | `...google.apiKey` | يعود احتياطيًا إلى `models.providers.google.apiKey` أو `GEMINI_API_KEY` أو `GOOGLE_API_KEY`  
  
مثال لإعدادات الوقت الفعلي في Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

للتحقق المباشر من قِبل المشرفين، شغّل `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. يغطي اختبار الدخان أيضًا مسارات خلفية OpenAI وWebRTC؛ إذ ينشئ جزء Google شكل رمز Live API المقيد نفسه الذي تستخدمه Control UI Talk، ويفتح نقطة نهاية WebSocket في المتصفح، ويرسل حمولة الإعداد الأولية، وينتظر `setupComplete`.

## الإعدادات المتقدمة

Direct Gemini cache reuse

في عمليات تشغيل Gemini API المباشرة (`api: "google-generative-ai"`)، يمرر OpenClaw مقبض `cachedContent` المهيّأ إلى طلبات Gemini.

  * هيّئ معاملات على مستوى النموذج أو عالميًا باستخدام `cachedContent` أو `cached_content` القديم
  * إذا وُجدا معًا، تكون الأولوية لـ `cachedContent`
  * قيمة مثال: `cachedContents/prebuilt-context`
  * يتم توحيد استخدام إصابة ذاكرة التخزين المؤقت في Gemini إلى `cacheRead` في OpenClaw من `cachedContentTokenCount` في المصدر الأعلى

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON usage notes

عند استخدام موفّر OAuth ‏`google-gemini-cli`، يوحّد OpenClaw مخرجات CLI بصيغة JSON كما يلي:

  * يأتي نص الرد من حقل `response` في JSON الخاص بـ CLI.
  * يعود الاستخدام احتياطيًا إلى `stats` عندما يترك CLI قيمة `usage` فارغة.
  * يتم توحيد `stats.cached` إلى `cacheRead` في OpenClaw.
  * إذا كان `stats.input` مفقودًا، يستنتج OpenClaw رموز الإدخال من `stats.input_tokens - stats.cached`.

Environment and daemon setup

إذا كان Gateway يعمل كخدمة daemon (launchd/systemd)، فتأكد من أن `GEMINI_API_KEY` متاح لتلك العملية (على سبيل المثال، في `~/.openclaw/.env` أو عبر `env.shellEnv`).

## ذات صلة

[**Model selection** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Image generation** معاملات أداة الصور المشتركة واختيار المزوّد. ](</ar/tools/image-generation>) [**Video generation** معاملات أداة الفيديو المشتركة واختيار المزوّد. ](</ar/tools/video-generation>) [**Music generation** معاملات أداة الموسيقى المشتركة واختيار المزوّد. ](</ar/tools/music-generation>)

Was this useful?YesNo