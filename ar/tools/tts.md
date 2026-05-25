---
title: تحويل النص إلى كلام
source_url: https://docs.openclaw.ai/ar/tools/tts
scraped_at: 2026-05-25
---

OpenClaw يمكنه تحويل الردود الصادرة إلى صوت عبر **14 مزود كلام** وتسليم رسائل صوتية أصلية على Feishu وMatrix وTelegram وWhatsApp، ومرفقات صوتية في كل مكان آخر، وتدفقات PCM/Ulaw للاتصالات الهاتفية وTalk.

TTS هو نصف إخراج الكلام في وضع `stt-tts` الخاص بـ Talk. جلسات Talk من نوع `realtime` الأصلية لدى المزود تُنشئ الكلام داخل مزود الوقت الحقيقي بدلاً من استدعاء مسار TTS هذا، بينما جلسات `transcription` لا تُنشئ استجابة صوتية للمساعد.

## البدء السريع

* ### اختر مزودًا

OpenAI وElevenLabs هما الخياران المستضافان الأكثر موثوقية. Microsoft و Local CLI يعملان من دون مفتاح API. راجع مصفوفة المزودين للاطلاع على القائمة الكاملة.

* ### اضبط مفتاح API

صدّر متغير البيئة الخاص بمزودك (على سبيل المثال `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). لا يحتاج Microsoft وLocal CLI إلى مفتاح.

* ### فعّله في الإعدادات

اضبط `messages.tts.auto: "always"` و`messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### جرّبه في الدردشة

يعرض `/tts status` الحالة الحالية. يرسل `/tts audio Hello from OpenClaw` ردًا صوتيًا لمرة واحدة.

## المزودون المدعومون

المزود | المصادقة | ملاحظات  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (أيضًا `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | إخراج ملاحظات صوتية Ogg/Opus أصلي والاتصالات الهاتفية.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS متوافق مع OpenAI. القيمة الافتراضية `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` أو `XI_API_KEY` | استنساخ الصوت، متعدد اللغات، حتمي عبر `seed`؛ يُبث لتشغيل صوت Discord.  
**Google Gemini** | `GEMINI_API_KEY` أو `GOOGLE_API_KEY` | TTS دفعي عبر Gemini API؛ مدرك للشخصية عبر `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | إخراج ملاحظات صوتية واتصالات هاتفية.  
**Inworld** | `INWORLD_API_KEY` | واجهة API لبث TTS. ملاحظات صوتية Opus أصلية واتصالات هاتفية PCM.  
**Local CLI** | لا شيء | يشغّل أمر TTS محليًا مُعدًا.  
**Microsoft** | لا شيء | TTS عصبي عام من Edge عبر `node-edge-tts`. بأفضل جهد، بلا SLA.  
**MiniMax** | `MINIMAX_API_KEY` (أو خطة Token: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | واجهة API من T2A v2. القيمة الافتراضية `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | يُستخدم أيضًا للتلخيص التلقائي؛ يدعم `instructions` للشخصية.  
**OpenRouter** | `OPENROUTER_API_KEY` (يمكن إعادة استخدام `models.providers.openrouter.apiKey`) | النموذج الافتراضي `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` أو `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/رمز قديمان: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | واجهة BytePlus Seed Speech HTTP API.  
**Vydra** | `VYDRA_API_KEY` | مزود مشترك للصور والفيديو والكلام.  
**xAI** | `XAI_API_KEY` | TTS دفعي من xAI. ملاحظات Opus الصوتية الأصلية **غير** مدعومة.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS عبر إكمالات دردشة Xiaomi.  
  
إذا تم إعداد عدة مزودين، فسيُستخدم المزود المحدد أولًا، وتكون المزودات الأخرى خيارات احتياطية. يستخدم التلخيص التلقائي `summaryModel` (أو `agents.defaults.model.primary`)، لذلك يجب أيضًا أن يكون ذلك المزود مصادقًا إذا أبقيت الملخصات مفعلة.

## الإعداد

توجد إعدادات TTS تحت `messages.tts` في `~/.openclaw/openclaw.json`. اختر إعدادًا مسبقًا وعدّل كتلة المزود:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (بلا مفتاح)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### تجاوزات الصوت لكل وكيل

استخدم `agents.list[].tts` عندما ينبغي لوكيل واحد أن يتحدث بمزود أو صوت أو نموذج أو شخصية أو وضع Auto-TTS مختلف. تدمج كتلة الوكيل بعمق فوق `messages.tts`، لذلك يمكن أن تبقى بيانات اعتماد المزود في إعدادات المزود العامة:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

لتثبيت شخصية لكل وكيل، عيّن `agents.list[].tts.persona` إلى جانب إعدادات المزوّد، فهي تتجاوز `messages.tts.persona` العامة لذلك الوكيل فقط.

ترتيب الأولوية للردود التلقائية، و`/tts audio`، و`/tts status`، وأداة الوكيل `tts`:

  1. `messages.tts`
  2. `agents.list[].tts` النشط
  3. تجاوز القناة، عندما تدعم القناة `channels.<channel>.tts`
  4. تجاوز الحساب، عندما تمرّر القناة `channels.<channel>.accounts.<id>.tts`
  5. تفضيلات `/tts` المحلية لهذا المضيف
  6. توجيهات `[[tts:...]]` المضمّنة عند تفعيل تجاوزات النموذج


تستخدم تجاوزات القنوات والحسابات البنية نفسها مثل `messages.tts` وتُدمج بعمق فوق الطبقات السابقة، لذلك يمكن أن تبقى بيانات اعتماد المزوّد المشتركة في `messages.tts` بينما تغيّر قناة أو حساب بوت الصوت أو النموذج أو الشخصية أو الوضع التلقائي فقط:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## الشخصيات

**الشخصية** هي هوية نطق ثابتة يمكن تطبيقها بشكل حتمي عبر المزوّدين. يمكنها تفضيل مزوّد واحد، وتعريف قصد موجّه محايد للمزوّد، وحمل ارتباطات خاصة بالمزوّدين للأصوات والنماذج وقوالب الموجّهات والبذور وإعدادات الصوت.

### شخصية بسيطة

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### شخصية كاملة (موجّه محايد للمزوّد)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### حلّ الشخصية

تُحدَّد الشخصية النشطة بشكل حتمي:

  1. تفضيل `/tts persona <id>` المحلي، إذا كان معيّنًا.
  2. `messages.tts.persona`، إذا كان معيّنًا.
  3. لا توجد شخصية.


يعمل اختيار المزوّد وفق الصريح أولًا:

  1. التجاوزات المباشرة (CLI، Gateway، Talk، توجيهات TTS المسموح بها).
  2. تفضيل `/tts provider <id>` المحلي.
  3. `provider` الخاص بالشخصية النشطة.
  4. `messages.tts.provider`.
  5. الاختيار التلقائي من السجل.


لكل محاولة مزوّد، يدمج OpenClaw الإعدادات بهذا الترتيب:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. تجاوزات الطلب الموثوقة
  4. تجاوزات توجيهات TTS المسموح بها والصادرة من النموذج


### كيف تستخدم المزوّدات موجّهات الشخصية

حقول موجّه الشخصية (`profile`، `scene`، `sampleContext`، `style`، `accent`، `pacing`، `constraints`) **محايدة للمزوّد**. يقرر كل مزوّد كيفية استخدامها:

Google Gemini

يغلّف حقول موجّه الشخصية في بنية موجّه Gemini TTS **فقط عندما** يعيّن إعداد مزوّد Google الفعّال `promptTemplate: "audio-profile-v1"` أو `personaPrompt`. ما زالت حقول `audioProfile` و`speakerName` الأقدم تُضاف في البداية كنص موجّه خاص بـ Google. تُحفظ وسوم الصوت المضمّنة مثل `[whispers]` أو `[laughs]` داخل كتلة `[[tts:text]]` داخل نص Gemini؛ لا ينشئ OpenClaw هذه الوسوم.

OpenAI

يربط حقول موجّه الشخصية بحقل الطلب `instructions` **فقط عندما** لا تكون هناك `instructions` صريحة مهيأة لـ OpenAI. تفوز `instructions` الصريحة دائمًا.

المزوّدون الآخرون

استخدم فقط ارتباطات الشخصية الخاصة بالمزوّد تحت `personas.<id>.providers.<provider>`. تُتجاهل حقول موجّه الشخصية ما لم ينفّذ المزوّد ربطًا خاصًا به لموجّه الشخصية.

### سياسة الرجوع

يتحكم `fallbackPolicy` في السلوك عندما لا يكون للشخصية **أي ارتباط** مع المزوّد الذي تتم محاولته:

السياسة | السلوك  
---|---  
`preserve-persona` | **الافتراضي.** تبقى حقول الموجّه المحايدة للمزوّد متاحة؛ قد يستخدمها المزوّد أو يتجاهلها.  
`provider-defaults` | تُحذف الشخصية من تحضير الموجّه لتلك المحاولة؛ يستخدم المزوّد افتراضاته المحايدة بينما يستمر الرجوع إلى مزوّدين آخرين.  
`fail` | تخطَّ محاولة ذلك المزوّد مع `reasonCode: "not_configured"` و`personaBinding: "missing"`. ما زالت مزوّدات الرجوع الأخرى تُجرَّب.  
  
لا يفشل طلب TTS بالكامل إلا عندما تُتخطى **كل** محاولات المزوّدين أو تفشل.

اختيار مزوّد جلسة Talk محصور بنطاق الجلسة. ينبغي لعميل Talk اختيار معرّفات المزوّدين، ومعرّفات النماذج، ومعرّفات الأصوات، واللغات من `talk.catalog` وتمريرها عبر جلسة Talk أو طلب التسليم. يجب ألا يؤدي فتح جلسة صوتية إلى تعديل `messages.tts` أو افتراضات مزوّد Talk العامة.

## التوجيهات المدفوعة بالنموذج

افتراضيًا، **يمكن** للمساعد إصدار توجيهات `[[tts:...]]` لتجاوز الصوت أو النموذج أو السرعة لرد واحد، إضافة إلى كتلة اختيارية `[[tts:text]]...[[/tts:text]]` للإشارات التعبيرية التي يجب أن تظهر في الصوت فقط:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

عندما تكون `messages.tts.auto` هي `"tagged"`، تكون **التوجيهات مطلوبة** لتشغيل الصوت. تزيل عملية تسليم كتل البث التوجيهات من النص المرئي قبل أن تراها القناة، حتى عند تقسيمها عبر كتل متجاورة.

يُتجاهل `provider=...` ما لم يكن `modelOverrides.allowProvider: true`. عندما يعلن رد عن `provider=...`، تُحلَّل المفاتيح الأخرى في ذلك التوجيه بواسطة ذلك المزوّد فقط؛ تُزال المفاتيح غير المدعومة وتُبلَّغ كتحذيرات لتوجيهات TTS.

**مفاتيح التوجيه المتاحة:**

  * `provider` (معرّف مزوّد مسجّل؛ يتطلب `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (مستوى صوت MiniMax، 0–10)
  * `pitch` (حدة MiniMax كعدد صحيح، −12 إلى 12؛ تُقتطع القيم الكسرية)
  * `emotion` (وسم العاطفة في Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**تعطيل تجاوزات النموذج بالكامل:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**السماح بتبديل المزوّد مع إبقاء عناصر التحكم الأخرى قابلة للتهيئة:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## أوامر الشرطة المائلة

أمر واحد `/tts`. على Discord، يسجل OpenClaw أيضًا `/voice` لأن `/tts` أمر مضمّن في Discord، وما زال نص `/tts ...` يعمل.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

ملاحظات السلوك:

  * يكتب `/tts on` تفضيل TTS المحلي إلى `always`؛ ويكتبه `/tts off` إلى `off`.
  * يكتب `/tts chat on|off|default` تجاوز TTS تلقائيًا محدودًا بنطاق الجلسة للمحادثة الحالية.
  * يكتب `/tts persona <id>` تفضيل الشخصية المحلي؛ ويمسحه `/tts persona off`.
  * يقرأ `/tts latest` أحدث رد للمساعد من نص جلسة المحادثة الحالية ويرسله كصوت مرة واحدة. لا يخزّن إلا تجزئة لذلك الرد على إدخال الجلسة لمنع إرسال صوت مكرر.
  * ينشئ `/tts audio` ردًا صوتيًا لمرة واحدة (لا يفعّل TTS).
  * يُخزَّن `limit` و`summary` في **التفضيلات المحلية** ، وليس في الإعداد الرئيسي.
  * يتضمن `/tts status` تشخيصات الرجوع لأحدث محاولة: `Fallback: <primary> -> <used>`، و`Attempts: ...`، وتفاصيل كل محاولة (`provider:outcome(reasonCode) latency`).
  * يعرض `/status` وضع TTS النشط، إضافة إلى المزوّد والنموذج والصوت وبيانات تعريف نقطة النهاية المخصصة بعد تنقيتها عندما يكون TTS مفعّلًا.


## تفضيلات كل مستخدم

تكتب أوامر الشرطة المائلة التجاوزات المحلية إلى `prefsPath`. الافتراضي هو `~/.openclaw/settings/tts.json`؛ ويمكن تجاوزه بمتغير البيئة `OPENCLAW_TTS_PREFS` أو `messages.tts.prefsPath`.

الحقل المخزّن | التأثير  
---|---  
`auto` | تجاوز TTS التلقائي المحلي (`always`, `off`, …)  
`provider` | تجاوز المزوّد الأساسي المحلي  
`persona` | تجاوز الشخصية المحلي  
`maxLength` | عتبة الملخّص (افتراضيًا `1500` حرفًا)  
`summarize` | مفتاح تشغيل الملخّص (افتراضيًا `true`)  
  
تتجاوز هذه الإعدادات الفعّالة من `messages.tts` إضافة إلى كتلة `agents.list[].tts` النشطة لذلك المضيف.

## صيغ الإخراج (ثابتة)

تسليم صوت TTS محكوم بإمكانات القناة. تعلن إضافات القنوات ما إذا كان على TTS بنمط الرسائل الصوتية أن يطلب من المزوّدين هدف `voice-note` أصليًا أو أن يحافظ على تركيب `audio-file` العادي ويكتفي بتمييز الإخراج المتوافق لتسليم الصوت.

  * **القنوات القادرة على الرسائل الصوتية** : تفضّل ردود الرسائل الصوتية Opus (`opus_48000_64` من ElevenLabs، و`opus` من OpenAI). 
    * 48kHz / 64kbps تمثل موازنة جيدة للرسائل الصوتية.
  * **Feishu / WhatsApp** : عندما يُنتَج رد الرسالة الصوتية بصيغة MP3/WebM/WAV/M4A أو كملف صوتي آخر محتمل، يحوّله Plugin القناة إلى Ogg/Opus بتردد 48kHz باستخدام `ffmpeg` قبل إرسال الرسالة الصوتية الأصلية. يرسل WhatsApp النتيجة عبر حمولة Baileys `audio` مع `ptt: true` و `audio/ogg; codecs=opus`. إذا فشل التحويل، يستلم Feishu الملف الأصلي كمرفق؛ أما إرسال WhatsApp فيفشل بدلاً من نشر حمولة PTT غير متوافقة.
  * **قنوات أخرى** : MP3 (`mp3_44100_128` من ElevenLabs، و`mp3` من OpenAI). 
    * 44.1kHz / 128kbps هي الموازنة الافتراضية لوضوح الكلام.
  * **MiniMax** : MP3 (نموذج `speech-2.8-hd`، ومعدل عينة 32kHz) لمرفقات الصوت العادية. بالنسبة إلى أهداف الرسائل الصوتية التي تعلنها القناة، يحوّل OpenClaw ملف MiniMax MP3 إلى Opus بتردد 48kHz باستخدام `ffmpeg` قبل التسليم عندما تعلن القناة دعم التحويل.
  * **Xiaomi MiMo** : MP3 افتراضياً، أو WAV عند ضبطه. بالنسبة إلى أهداف الرسائل الصوتية التي تعلنها القناة، يحوّل OpenClaw خرج Xiaomi إلى Opus بتردد 48kHz باستخدام `ffmpeg` قبل التسليم عندما تعلن القناة دعم التحويل.
  * **CLI المحلي** : يستخدم `outputFormat` المضبوط. تُحوّل أهداف الرسائل الصوتية إلى Ogg/Opus، ويُحوّل خرج الاتصالات الهاتفية إلى PCM أحادي خام بتردد 16 kHz باستخدام `ffmpeg`.
  * **Google Gemini** : تعيد TTS في Gemini API ملف PCM خاماً بتردد 24kHz. يغلّفه OpenClaw كملف WAV لمرفقات الصوت، ويحوّله إلى Opus بتردد 48kHz لأهداف الرسائل الصوتية، ويعيد PCM مباشرةً لـ Talk/الاتصالات الهاتفية.
  * **Gradium** : WAV لمرفقات الصوت، وOpus لأهداف الرسائل الصوتية، و`ulaw_8000` بتردد 8 kHz للاتصالات الهاتفية.
  * **Inworld** : MP3 لمرفقات الصوت العادية، و`OGG_OPUS` أصلي لأهداف الرسائل الصوتية، و`PCM` خام بتردد 22050 Hz لـ Talk/الاتصالات الهاتفية.
  * **xAI** : MP3 افتراضياً؛ يمكن أن تكون `responseFormat` إحدى القيم `mp3` أو `wav` أو `pcm` أو `mulaw` أو `alaw`. يستخدم OpenClaw نقطة نهاية TTS الدفعية عبر REST في xAI ويعيد مرفقاً صوتياً كاملاً؛ لا يُستخدم WebSocket الخاص ببث TTS في xAI ضمن مسار هذا المزوّد. لا يدعم هذا المسار صيغة Opus الأصلية للرسائل الصوتية.
  * **Microsoft** : يستخدم `microsoft.outputFormat` (الافتراضي `audio-24khz-48kbitrate-mono-mp3`). 
    * يقبل النقل المضمّن `outputFormat`، لكن ليست كل الصيغ متاحة من الخدمة.
    * تتبع قيم صيغة الخرج صيغ خرج Microsoft Speech (بما في ذلك Ogg/WebM Opus).
    * يقبل `sendVoice` في Telegram صيغ OGG/MP3/M4A؛ استخدم OpenAI/ElevenLabs إذا كنت تحتاج إلى رسائل صوتية مضمونة بصيغة Opus.
    * إذا فشلت صيغة خرج Microsoft المضبوطة، يعيد OpenClaw المحاولة باستخدام MP3.


صيغ خرج OpenAI/ElevenLabs ثابتة لكل قناة (انظر أعلاه).

## سلوك TTS التلقائي

عند تفعيل `messages.tts.auto`، يقوم OpenClaw بما يلي:

  * يتخطى TTS إذا كان الرد يحتوي بالفعل على وسائط أو توجيه `MEDIA:`.
  * يتخطى الردود القصيرة جداً (أقل من 10 أحرف).
  * يلخّص الردود الطويلة عند تفعيل الملخصات، باستخدام `summaryModel` (أو `agents.defaults.model.primary`).
  * يرفق الصوت المُنشأ بالرد.
  * في `mode: "final"`، يظل يرسل TTS صوتياً فقط للردود النهائية المتدفقة بعد اكتمال تدفق النص؛ تمر الوسائط المُنشأة عبر تطبيع وسائط القناة نفسه مثل مرفقات الرد العادية.


إذا تجاوز الرد `maxLength` وكان التلخيص متوقفاً (أو لا يوجد مفتاح API لنموذج التلخيص)، يتم تخطي الصوت ويُرسل الرد النصي العادي.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## صيغ الخرج حسب القناة

الهدف | التنسيق  
---|---  
Feishu / Matrix / Telegram / WhatsApp | تفضّل ردود الملاحظات الصوتية **Opus** (`opus_48000_64` من ElevenLabs، و`opus` من OpenAI). يوازن 48 kHz / 64 kbps بين الوضوح والحجم.  
قنوات أخرى | **MP3** (`mp3_44100_128` من ElevenLabs، و`mp3` من OpenAI). الإعداد الافتراضي للكلام هو 44.1 kHz / 128 kbps.  
Talk / الهاتف | **PCM** أصلي لدى المزوّد (Inworld ‏22050 Hz، وGoogle ‏24 kHz)، أو `ulaw_8000` من Gradium للهاتف.  
  
ملاحظات حسب المزوّد:

  * **تحويل Feishu / WhatsApp:** عندما يصل رد ملاحظة صوتية بصيغة MP3/WebM/WAV/M4A، يحوّل Plugin القناة ترميزه إلى Ogg/Opus بتردد 48 kHz باستخدام `ffmpeg`. يرسل WhatsApp عبر Baileys مع `ptt: true` و`audio/ogg; codecs=opus`. إذا فشل التحويل: يعود Feishu إلى إرفاق الملف الأصلي؛ ويفشل إرسال WhatsApp بدلاً من نشر حمولة PTT غير متوافقة.
  * **MiniMax / Xiaomi MiMo:** MP3 افتراضياً (32 kHz لـ MiniMax `speech-2.8-hd`)؛ ويُحوَّل إلى Opus بتردد 48 kHz لأهداف الملاحظات الصوتية عبر `ffmpeg`.
  * **CLI المحلي:** يستخدم `outputFormat` المكوَّن. تُحوَّل أهداف الملاحظات الصوتية إلى Ogg/Opus ومخرجات الهاتف إلى PCM خام أحادي القناة بتردد 16 kHz.
  * **Google Gemini:** يعيد PCM خاماً بتردد 24 kHz. يغلّفه OpenClaw كملف WAV للمرفقات، ويحوّله إلى Opus بتردد 48 kHz لأهداف الملاحظات الصوتية، ويعيد PCM مباشرة لـ Talk/الهاتف.
  * **Inworld:** مرفقات MP3، وملاحظة صوتية أصلية `OGG_OPUS`، و`PCM` خام بتردد 22050 Hz لـ Talk/الهاتف.
  * **xAI:** MP3 افتراضياً؛ يمكن أن تكون `responseFormat` هي `mp3|wav|pcm|mulaw|alaw`. يستخدم نقطة نهاية REST الدفعية من xAI — ولا يُستخدم TTS عبر WebSocket المتدفق. صيغة Opus الأصلية للملاحظات الصوتية **غير** مدعومة.
  * **Microsoft:** يستخدم `microsoft.outputFormat` (الافتراضي `audio-24khz-48kbitrate-mono-mp3`). يقبل `sendVoice` في Telegram صيغ OGG/MP3/M4A؛ استخدم OpenAI/ElevenLabs إذا كنت تحتاج إلى رسائل صوتية مضمونة بصيغة Opus. إذا فشلت صيغة Microsoft المكوَّنة، يعيد OpenClaw المحاولة باستخدام MP3.


صيغ مخرجات OpenAI وElevenLabs ثابتة لكل قناة كما هو مذكور أعلاه.

## مرجع الحقول

رسائل المستوى الأعلى messages.tts.*

وضع Auto-TTS. يرسل `inbound` الصوت فقط بعد رسالة صوتية واردة؛ ويرسل `tagged` الصوت فقط عندما يتضمن الرد توجيهات `[[tts:...]]` أو كتلة `[[tts:text]]`.

مفتاح تبديل قديم. يرحّل `openclaw doctor --fix` هذا إلى `auto`.

يتضمن `"all"` ردود الأدوات/الكتل إضافةً إلى الردود النهائية.

معرّف مزوّد الكلام. عند عدم تعيينه، يستخدم OpenClaw أول مزوّد مكوَّن في ترتيب الاختيار التلقائي للسجل. يعيد `openclaw doctor --fix` كتابة `provider: "edge"` القديم إلى `"microsoft"`.

معرّف الشخصية النشطة من `personas`. يُطبَّع إلى أحرف صغيرة.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> هوية منطوقة ثابتة. الحقول: `label`، `description`، `provider`، `fallbackPolicy`، `prompt`، `providers.<provider>`. راجع الشخصيات.

نموذج منخفض التكلفة للملخص التلقائي؛ الافتراضي هو `agents.defaults.model.primary`. يقبل `provider/model` أو اسماً مستعاراً لنموذج مكوَّن.

اسمح للنموذج بإصدار توجيهات TTS. القيمة الافتراضية لـ `enabled` هي `true`؛ والقيمة الافتراضية لـ `allowProvider` هي `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> إعدادات مملوكة للمزوّد ومفهرسة حسب معرّف مزوّد الكلام. يعيد `openclaw doctor --fix` كتابة الكتل المباشرة القديمة (`messages.tts.openai`، `.elevenlabs`، `.microsoft`، `.edge`)؛ اعتمد فقط `messages.tts.providers.<id>`.

حد صارم لعدد أحرف إدخال TTS. يفشل `/tts audio` إذا تم تجاوزه.

مهلة الطلب بالمللي ثانية.

تجاوز مسار JSON المحلي للتفضيلات (المزوّد/الحد/الملخص). الافتراضي `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`، أو `AZURE_SPEECH_API_KEY`، أو `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg منطقة Azure Speech (مثلاً `eastus`). Env: `AZURE_SPEECH_REGION` أو `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci تجاوز اختياري لنقطة نهاية Azure Speech (الاسم المستعار `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName لصوت Azure. الافتراضي `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI رمز لغة SSML. الافتراضي `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg ‏Azure `X-Microsoft-OutputFormat` للصوت القياسي. الافتراضي `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg ‏Azure `X-Microsoft-OutputFormat` لمخرجات الملاحظات الصوتية. الافتراضي `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg يعود إلى `ELEVENLABS_API_KEY` أو `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci معرّف النموذج (مثلاً `eleven_multilingual_v2`، `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`، و`similarityBoost`، و`style` (كل منها `0..1`)، و`useSpeakerBoost` (`true|false`)، و`speed` (`0.5..2.0`، `1.0` = عادي).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg رمز ISO 639-1 من حرفين (مثلاً `en`، `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI عدد صحيح `0..4294967295` للحتمية قدر الإمكان. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg يعود إلى `GEMINI_API_KEY` / `GOOGLE_API_KEY`. إذا حُذف، يمكن لـ TTS إعادة استخدام `models.providers.google.apiKey` قبل الرجوع إلى Env. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci نموذج Gemini TTS. الافتراضي `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg اسم صوت Gemini الجاهز. الافتراضي `Kore`. الاسم المستعار: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn اضبط على `audio-profile-v1` لتغليف حقول موجّه الشخصية النشطة في بنية موجّه Gemini TTS حتمية. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI لا يُقبل إلا `https://generativelanguage.googleapis.com`. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld الأساسي

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية `inworld-tts-1.5-max`. أيضًا: `inworld-tts-1.5-mini`، `inworld-tts-1-max`، `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi درجة حرارة أخذ العينات `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Local CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg وسيطات الأمر. تدعم العناصر النائبة `{{Text}}` و`{{OutputPath}}` و`{{OutputDir}}` و`{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic تنسيق خرج CLI المتوقع. القيمة الافتراضية `mp3` لمرفقات الصوت. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg مهلة الأمر بالمللي ثانية. القيمة الافتراضية `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (no API key)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci اسم صوت Microsoft العصبي (مثل `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI رمز اللغة (مثل `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg تنسيق خرج Microsoft. القيمة الافتراضية `audio-24khz-48kbitrate-mono-mp3`. ليست كل التنسيقات مدعومة بواسطة النقل المرفق المدعوم من Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg سلاسل النسب المئوية (مثل `+10%` و`-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk اسم مستعار قديم. شغّل `openclaw doctor --fix` لإعادة كتابة الإعدادات المحفوظة إلى `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg يرجع احتياطيًا إلى `MINIMAX_API_KEY`. مصادقة Token Plan عبر `MINIMAX_OAUTH_TOKEN` أو `MINIMAX_CODE_PLAN_KEY` أو `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://api.minimax.io`. متغير البيئة: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci القيمة الافتراضية `speech-2.8-hd`. متغير البيئة: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية `English_expressive_narrator`. متغير البيئة: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. القيمة الافتراضية `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. القيمة الافتراضية `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi عدد صحيح `-12..12`. القيمة الافتراضية `0`. يتم اقتطاع القيم الكسرية قبل الطلب. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg يرجع احتياطيًا إلى `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci معرّف نموذج OpenAI TTS (مثل `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci اسم الصوت (مثل `alloy` و`cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg حقل OpenAI `instructions` الصريح. عند ضبطه، **لا** يتم ربط حقول موجّه الشخصية تلقائيًا. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">حقول JSON إضافية يتم دمجها في أجسام طلبات `/audio/speech` بعد حقول OpenAI TTS المولّدة. استخدم هذا لنقاط النهاية المتوافقة مع OpenAI مثل Kokoro التي تتطلب مفاتيح خاصة بالمزوّد مثل `lang`؛ ويتم تجاهل مفاتيح النموذج الأولي غير الآمنة. OPENCLAW_DOCS_MARKER:paramClose:

تجاوز نقطة نهاية OpenAI TTS. ترتيب الحل: الإعدادات → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. تُعامل القيم غير الافتراضية كنقاط نهاية TTS متوافقة مع OpenAI، لذلك تُقبل أسماء النماذج والأصوات المخصصة.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `OPENROUTER_API_KEY`. يمكن إعادة استخدام `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://openrouter.ai/api/v1`. يتم تطبيع القيمة القديمة `https://openrouter.ai/v1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci القيمة الافتراضية `hexgrad/kokoro-82m`. الاسم المستعار: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci القيمة الافتراضية `af_alloy`. الاسم المستعار: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw القيمة الافتراضية `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `VOLCENGINE_TTS_API_KEY` أو `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية `seed-tts-1.0`. متغير البيئة: `VOLCENGINE_TTS_RESOURCE_ID`. استخدم `seed-tts-2.0` عندما يكون لمشروعك استحقاق TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg ترويسة مفتاح التطبيق. القيمة الافتراضية `aGjiRDfUWi`. متغير البيئة: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI تجاوز نقطة نهاية HTTP لـ Seed Speech TTS. متغير البيئة: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci نوع الصوت. القيمة الافتراضية `en_female_anna_mars_bigtts`. متغير البيئة: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ حقول Volcengine Speech Console القديمة. متغيرات البيئة: `VOLCENGINE_TTS_APPID`، `VOLCENGINE_TTS_TOKEN`، `VOLCENGINE_TTS_CLUSTER` (القيمة الافتراضية `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://api.x.ai/v1`. متغير البيئة: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI القيمة الافتراضية `eve`. الأصوات الحية: `ara`، `eve`، `leo`، `rex`، `sal`، `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci رمز لغة BCP-47 أو `auto`. القيمة الافتراضية `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw القيمة الافتراضية `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg متغير البيئة: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI القيمة الافتراضية `https://api.xiaomimimo.com/v1`. متغير البيئة: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci القيمة الافتراضية `mimo-v2.5-tts`. متغير البيئة: `XIAOMI_TTS_MODEL`. يدعم أيضًا `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci القيمة الافتراضية `mimo_default`. متغير البيئة: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic القيمة الافتراضية `mp3`. متغير البيئة: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## أداة الوكيل

تحوّل أداة `tts` النص إلى كلام وتعيد مرفقًا صوتيًا لتسليم الرد. على Feishu وMatrix وTelegram وWhatsApp، يتم تسليم الصوت كرسالة صوتية بدلًا من مرفق ملف. يمكن لـ Feishu وWhatsApp تحويل ترميز خرج TTS غير Opus في هذا المسار عند توفر `ffmpeg`.

يرسل WhatsApp الصوت عبر Baileys كملاحظة صوتية PTT (`audio` مع `ptt: true`) ويرسل النص المرئي **بشكل منفصل** عن صوت PTT لأن العملاء لا يعرضون التسميات التوضيحية على الملاحظات الصوتية باستمرار.

تقبل الأداة حقلي `channel` و`timeoutMs` الاختياريين؛ `timeoutMs` هو مهلة طلب المزوّد لكل استدعاء بالمللي ثانية.

## Gateway RPC

الطريقة | الغرض  
---|---  
`tts.status` | قراءة حالة TTS الحالية وآخر محاولة.  
`tts.enable` | ضبط التفضيل التلقائي المحلي إلى `always`.  
`tts.disable` | ضبط التفضيل التلقائي المحلي إلى `off`.  
`tts.convert` | تحويل نص لمرة واحدة → صوت.  
`tts.setProvider` | ضبط تفضيل المزوّد المحلي.  
`tts.setPersona` | ضبط تفضيل الشخصية المحلي.  
`tts.providers` | سرد المزوّدين المهيئين وحالتهم.  
  
## روابط الخدمة

  * [دليل OpenAI لتحويل النص إلى كلام](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [مرجع OpenAI Audio API](<https://platform.openai.com/docs/api-reference/audio>)
  * [تحويل النص إلى كلام عبر Azure Speech REST](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [مزوّد Azure Speech](</ar/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [مصادقة ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</ar/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</ar/providers/volcengine#text-to-speech>)
  * [تخليق الكلام في Xiaomi MiMo](</ar/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [تنسيقات خرج Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [تحويل النص إلى كلام في xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## ذات صلة

  * [نظرة عامة على الوسائط](</ar/tools/media-overview>)
  * [توليد الموسيقى](</ar/tools/music-generation>)
  * [توليد الفيديو](</ar/tools/video-generation>)
  * [أوامر الشرطة المائلة](</ar/tools/slash-commands>)
  * [Plugin المكالمات الصوتية](</ar/plugins/voice-call>)


Was this useful?YesNo