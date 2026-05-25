---
title: Metinden konuşmaya
source_url: https://docs.openclaw.ai/tr/tools/tts
scraped_at: 2026-05-25
---

OpenClaw, giden yanıtları **14 konuşma sağlayıcısı** genelinde sese dönüştürebilir ve Feishu, Matrix, Telegram ve WhatsApp üzerinde yerel sesli mesajlar, diğer her yerde ses ekleri ve telefon ile Talk için PCM/Ulaw akışları iletebilir.

TTS, Talk'ın `stt-tts` modunun konuşma çıktısı yarısıdır. Sağlayıcıya yerel `realtime` Talk oturumları, bu TTS yolunu çağırmak yerine konuşmayı gerçek zamanlı sağlayıcının içinde sentezler; `transcription` oturumları ise asistan için sesli yanıt sentezlemez.

## Hızlı başlangıç

* ### Bir sağlayıcı seçin

OpenAI ve ElevenLabs en güvenilir barındırılan seçeneklerdir. Microsoft ve Yerel CLI bir API anahtarı olmadan çalışır. Tam liste için sağlayıcı matrisine bakın.

* ### API anahtarını ayarlayın

Sağlayıcınız için env var'ı dışa aktarın (örneğin `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft ve Yerel CLI anahtar gerektirmez.

* ### Yapılandırmada etkinleştirin

`messages.tts.auto: "always"` ve `messages.tts.provider` ayarlarını yapın:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Sohbette deneyin

`/tts status` mevcut durumu gösterir. `/tts audio Hello from OpenClaw` tek seferlik bir sesli yanıt gönderir.

## Desteklenen sağlayıcılar

Sağlayıcı | Kimlik doğrulama | Notlar  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (ayrıca `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Yerel Ogg/Opus sesli not çıktısı ve telefon.  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI uyumlu TTS. Varsayılan olarak `hexgrad/Kokoro-82M` kullanır.  
**ElevenLabs** | `ELEVENLABS_API_KEY` veya `XI_API_KEY` | Ses klonlama, çok dilli, `seed` ile deterministik; Discord ses oynatması için akışlıdır.  
**Google Gemini** | `GEMINI_API_KEY` veya `GOOGLE_API_KEY` | Gemini API toplu TTS; `promptTemplate: "audio-profile-v1"` ile persona duyarlıdır.  
**Gradium** | `GRADIUM_API_KEY` | Sesli not ve telefon çıktısı.  
**Inworld** | `INWORLD_API_KEY` | Akışlı TTS API. Yerel Opus sesli not ve PCM telefon.  
**Yerel CLI** | yok | Yapılandırılmış yerel bir TTS komutu çalıştırır.  
**Microsoft** | yok | `node-edge-tts` üzerinden genel Edge sinirsel TTS. En iyi çaba, SLA yok.  
**MiniMax** | `MINIMAX_API_KEY` (veya Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2 API. Varsayılan olarak `speech-2.8-hd` kullanır.  
**OpenAI** | `OPENAI_API_KEY` | Otomatik özet için de kullanılır; persona `instructions` desteği sağlar.  
**OpenRouter** | `OPENROUTER_API_KEY` (`models.providers.openrouter.apiKey` yeniden kullanılabilir) | Varsayılan model `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` veya `BYTEPLUS_SEED_SPEECH_API_KEY` (eski AppID/token: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP API.  
**Vydra** | `VYDRA_API_KEY` | Paylaşılan görüntü, video ve konuşma sağlayıcısı.  
**xAI** | `XAI_API_KEY` | xAI toplu TTS. Yerel Opus sesli not **desteklenmez**.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | Xiaomi sohbet tamamlama üzerinden MiMo TTS.  
  
Birden fazla sağlayıcı yapılandırılmışsa, önce seçilen sağlayıcı kullanılır ve diğerleri yedek seçeneklerdir. Otomatik özet `summaryModel` (veya `agents.defaults.model.primary`) kullanır; bu nedenle özetleri etkin tutarsanız o sağlayıcının da kimliğinin doğrulanmış olması gerekir.

## Yapılandırma

TTS yapılandırması `~/.openclaw/openclaw.json` içinde `messages.tts` altında bulunur. Bir ön ayar seçin ve sağlayıcı bloğunu uyarlayın:

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

### Yerel CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (anahtar yok)

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

### Ajan başına ses geçersiz kılmaları

Bir ajanın farklı bir sağlayıcı, ses, model, persona veya Auto-TTS modu ile konuşması gerektiğinde `agents.list[].tts` kullanın. Ajan bloğu `messages.tts` üzerine derin birleştirme yapar; bu nedenle sağlayıcı kimlik bilgileri genel sağlayıcı yapılandırmasında kalabilir:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Aracı başına bir persona sabitlemek için sağlayıcı yapılandırmasının yanında `agents.list[].tts.persona` ayarlayın; bu, yalnızca ilgili aracı için genel `messages.tts.persona` değerini geçersiz kılar.

Otomatik yanıtlar, `/tts audio`, `/tts status` ve `tts` aracı aracı için öncelik sırası:

  1. `messages.tts`
  2. etkin `agents.list[].tts`
  3. kanal `channels.<channel>.tts` destekliyorsa kanal geçersiz kılması
  4. kanal `channels.<channel>.accounts.<id>.tts` geçiriyorsa hesap geçersiz kılması
  5. bu ana makine için yerel `/tts` tercihleri
  6. model geçersiz kılmaları etkinleştirildiğinde satır içi `[[tts:...]]` yönergeleri


Kanal ve hesap geçersiz kılmaları `messages.tts` ile aynı şekli kullanır ve önceki katmanların üzerine derin birleştirme yapar; böylece paylaşılan sağlayıcı kimlik bilgileri `messages.tts` içinde kalırken bir kanal veya bot hesabı yalnızca sesi, modeli, personayı veya otomatik modu değiştirebilir:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Personalar

**Persona** , sağlayıcılar arasında deterministik olarak uygulanabilen kararlı bir konuşma kimliğidir. Tek bir sağlayıcıyı tercih edebilir, sağlayıcıdan bağımsız istem amacını tanımlayabilir ve sesler, modeller, istem şablonları, seed değerleri ve ses ayarları için sağlayıcıya özel bağlamaları taşıyabilir.

### Minimal persona

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Tam persona (sağlayıcıdan bağımsız istem)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Persona çözümleme

Etkin persona deterministik olarak seçilir:

  1. Ayarlanmışsa `/tts persona <id>` yerel tercihi.
  2. Ayarlanmışsa `messages.tts.persona`.
  3. Persona yok.


Sağlayıcı seçimi açık olan önce çalışacak şekilde yürür:

  1. Doğrudan geçersiz kılmalar (CLI, Gateway, Talk, izin verilen TTS yönergeleri).
  2. `/tts provider <id>` yerel tercihi.
  3. Etkin personanın `provider` değeri.
  4. `messages.tts.provider`.
  5. Kayıt defteri otomatik seçimi.


Her sağlayıcı denemesi için OpenClaw yapılandırmaları şu sırayla birleştirir:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Güvenilen istek geçersiz kılmaları
  4. İzin verilen model tarafından yayımlanmış TTS yönergesi geçersiz kılmaları


### Sağlayıcılar persona istemlerini nasıl kullanır

Persona istem alanları (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) **sağlayıcıdan bağımsızdır**. Her sağlayıcı bunları nasıl kullanacağına kendisi karar verir:

Google Gemini

Yalnızca etkili Google sağlayıcı yapılandırması `promptTemplate: "audio-profile-v1"` veya `personaPrompt` ayarladığında persona istem alanlarını bir Gemini TTS istem yapısına sarar. Eski `audioProfile` ve `speakerName` alanları hâlâ Google'a özel istem metni olarak başa eklenir. Bir `[[tts:text]]` bloğunun içindeki `[whispers]` veya `[laughs]` gibi satır içi ses etiketleri Gemini transkripti içinde korunur; OpenClaw bu etiketleri üretmez.

OpenAI

Yalnızca açık bir OpenAI `instructions` yapılandırılmadığında persona istem alanlarını istekteki `instructions` alanına eşler. Açık `instructions` her zaman kazanır.

Other providers

Yalnızca `personas.<id>.providers.<provider>` altındaki sağlayıcıya özel persona bağlamalarını kullanır. Sağlayıcı kendi persona istemi eşlemesini uygulamadığı sürece persona istem alanları yok sayılır.

### Geri dönüş ilkesi

`fallbackPolicy`, bir personanın denenen sağlayıcı için **hiç bağlaması yoksa** davranışı kontrol eder:

İlke | Davranış  
---|---  
`preserve-persona` | **Varsayılan.** Sağlayıcıdan bağımsız istem alanları kullanılabilir kalır; sağlayıcı bunları kullanabilir veya yok sayabilir.  
`provider-defaults` | Bu deneme için persona istem hazırlığından çıkarılır; diğer sağlayıcılara geri dönüş sürerken sağlayıcı kendi nötr varsayılanlarını kullanır.  
`fail` | Bu sağlayıcı denemesini `reasonCode: "not_configured"` ve `personaBinding: "missing"` ile atla. Geri dönüş sağlayıcıları yine de denenir.  
  
Tüm TTS isteği yalnızca denenen **her** sağlayıcı atlandığında veya başarısız olduğunda başarısız olur.

Talk oturumu sağlayıcı seçimi oturum kapsamındadır. Bir Talk istemcisi sağlayıcı kimliklerini, model kimliklerini, ses kimliklerini ve yerel ayarları `talk.catalog` içinden seçmeli ve bunları Talk oturumu veya devretme isteği üzerinden geçirmelidir. Bir ses oturumu açmak `messages.tts` değerini veya genel Talk sağlayıcı varsayılanlarını değiştirmemelidir.

## Model güdümlü yönergeler

Varsayılan olarak yardımcı, tek bir yanıt için sesi, modeli veya hızı geçersiz kılmak üzere `[[tts:...]]` yönergeleri ve yalnızca seste görünmesi gereken ifade ipuçları için isteğe bağlı bir `[[tts:text]]...[[/tts:text]]` bloğu yayımlayabilir:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

`messages.tts.auto` `"tagged"` olduğunda sesi tetiklemek için **yönergeler zorunludur**. Akış blok teslimi, bitişik bloklara bölünmüş olsa bile, kanal bunları görmeden önce yönergeleri görünür metinden çıkarır.

`modelOverrides.allowProvider: true` olmadığı sürece `provider=...` yok sayılır. Bir yanıt `provider=...` bildirdiğinde, bu yönergedeki diğer anahtarlar yalnızca o sağlayıcı tarafından ayrıştırılır; desteklenmeyen anahtarlar çıkarılır ve TTS yönergesi uyarıları olarak raporlanır.

**Kullanılabilir yönerge anahtarları:**

  * `provider` (kayıtlı sağlayıcı kimliği; `allowProvider: true` gerektirir)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (MiniMax ses düzeyi, 0-10)
  * `pitch` (MiniMax tamsayı perde, -12 ile 12 arası; kesirli değerler kırpılır)
  * `emotion` (Volcengine duygu etiketi)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Model geçersiz kılmalarını tamamen devre dışı bırak:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Diğer ayarlar yapılandırılabilir kalırken sağlayıcı değiştirmeye izin ver:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Eğik çizgi komutları

Tek komut `/tts`. Discord üzerinde OpenClaw ayrıca `/voice` kaydeder çünkü `/tts` yerleşik bir Discord komutudur; metin olarak `/tts ...` yine de çalışır.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Davranış notları:

  * `/tts on`, yerel TTS tercihini `always` olarak yazar; `/tts off` bunu `off` olarak yazar.
  * `/tts chat on|off|default`, geçerli sohbet için oturum kapsamlı bir otomatik TTS geçersiz kılması yazar.
  * `/tts persona <id>`, yerel persona tercihini yazar; `/tts persona off` bunu temizler.
  * `/tts latest`, geçerli oturum transkriptinden en son yardımcı yanıtını okur ve bunu bir kez ses olarak gönderir. Yinelenen ses gönderimlerini bastırmak için oturum girdisinde yalnızca bu yanıtın hash değerini saklar.
  * `/tts audio`, tek seferlik bir sesli yanıt üretir (TTS'yi **açmaz**).
  * `limit` ve `summary`, ana yapılandırmada değil **yerel tercihlerde** saklanır.
  * `/tts status`, en son deneme için geri dönüş tanılarını içerir: `Fallback: <primary> -> <used>`, `Attempts: ...` ve deneme başına ayrıntı (`provider:outcome(reasonCode) latency`).
  * `/status`, TTS etkin olduğunda etkin TTS modunun yanı sıra yapılandırılmış sağlayıcıyı, modeli, sesi ve temizlenmiş özel uç nokta meta verilerini gösterir.


## Kullanıcı başına tercihler

Eğik çizgi komutları yerel geçersiz kılmaları `prefsPath` yoluna yazar. Varsayılan değer `~/.openclaw/settings/tts.json`; `OPENCLAW_TTS_PREFS` ortam değişkeni veya `messages.tts.prefsPath` ile geçersiz kılın.

Saklanan alan | Etki  
---|---  
`auto` | Yerel otomatik TTS geçersiz kılması (`always`, `off`, …)  
`provider` | Yerel birincil sağlayıcı geçersiz kılması  
`persona` | Yerel persona geçersiz kılması  
`maxLength` | Özet eşiği (varsayılan `1500` karakter)  
`summarize` | Özet anahtarı (varsayılan `true`)  
  
Bunlar, `messages.tts` içinden gelen etkili yapılandırmayı ve ilgili ana makine için etkin `agents.list[].tts` bloğunu geçersiz kılar.

## Çıktı biçimleri (sabit)

TTS ses teslimi kanal yeteneği tarafından yönlendirilir. Kanal Plugin'leri, ses tarzı TTS'nin sağlayıcılardan yerel bir `voice-note` hedefi istemesi mi gerektiğini yoksa normal `audio-file` sentezini koruyup yalnızca uyumlu çıktıyı ses teslimi için işaretlemesi mi gerektiğini duyurur.

  * **Sesli not destekli kanallar** : sesli not yanıtları Opus'u tercih eder (ElevenLabs'ten `opus_48000_64`, OpenAI'den `opus`). 
    * 48kHz / 64kbps, sesli mesaj için iyi bir denge sunar.
  * **Feishu / WhatsApp** : bir sesli not yanıtı MP3/WebM/WAV/M4A veya muhtemel başka bir ses dosyası olarak üretildiğinde, kanal Plugin'i yerel sesli mesajı göndermeden önce bunu `ffmpeg` ile 48kHz Ogg/Opus'a transkodlar. WhatsApp, sonucu Baileys `audio` payload'ı üzerinden `ptt: true` ve `audio/ogg; codecs=opus` ile gönderir. Dönüştürme başarısız olursa Feishu özgün dosyayı ek olarak alır; WhatsApp gönderimi ise uyumsuz bir PTT payload'ı paylaşmak yerine başarısız olur.
  * **Diğer kanallar** : MP3 (ElevenLabs'ten `mp3_44100_128`, OpenAI'den `mp3`). 
    * 44.1kHz / 128kbps, konuşma netliği için varsayılan dengedir.
  * **MiniMax** : normal ses ekleri için MP3 (`speech-2.8-hd` modeli, 32kHz örnekleme hızı). Kanal tarafından duyurulan sesli not hedefleri için, kanal transkodlama desteği bildirdiğinde OpenClaw teslimattan önce MiniMax MP3'ü `ffmpeg` ile 48kHz Opus'a transkodlar.
  * **Xiaomi MiMo** : varsayılan olarak MP3 veya yapılandırıldığında WAV. Kanal tarafından duyurulan sesli not hedefleri için, kanal transkodlama desteği bildirdiğinde OpenClaw teslimattan önce Xiaomi çıktısını `ffmpeg` ile 48kHz Opus'a transkodlar.
  * **Yerel CLI** : yapılandırılan `outputFormat` değerini kullanır. Sesli not hedefleri Ogg/Opus'a dönüştürülür ve telefon çıktısı `ffmpeg` ile ham 16 kHz mono PCM'ye dönüştürülür.
  * **Google Gemini** : Gemini API TTS, ham 24kHz PCM döndürür. OpenClaw bunu ses ekleri için WAV olarak sarmalar, sesli not hedefleri için 48kHz Opus'a transkodlar ve Talk/telefon için PCM'yi doğrudan döndürür.
  * **Gradium** : ses ekleri için WAV, sesli not hedefleri için Opus ve telefon için 8 kHz'de `ulaw_8000`.
  * **Inworld** : normal ses ekleri için MP3, sesli not hedefleri için yerel `OGG_OPUS` ve Talk/telefon için 22050 Hz'de ham `PCM`.
  * **xAI** : varsayılan olarak MP3; `responseFormat` `mp3`, `wav`, `pcm`, `mulaw` veya `alaw` olabilir. OpenClaw, xAI'nin toplu REST TTS uç noktasını kullanır ve tam bir ses eki döndürür; xAI'nin akışlı TTS WebSocket'i bu sağlayıcı yolu tarafından kullanılmaz. Yerel Opus sesli not biçimi bu yol tarafından desteklenmez.
  * **Microsoft** : `microsoft.outputFormat` değerini kullanır (varsayılan `audio-24khz-48kbitrate-mono-mp3`). 
    * Birlikte gelen aktarım bir `outputFormat` kabul eder, ancak tüm biçimler hizmetten kullanılamaz.
    * Çıktı biçimi değerleri Microsoft Speech çıktı biçimlerini izler (Ogg/WebM Opus dahil).
    * Telegram `sendVoice`, OGG/MP3/M4A kabul eder; garantili Opus sesli mesajlarına ihtiyacınız varsa OpenAI/ElevenLabs kullanın.
    * Yapılandırılan Microsoft çıktı biçimi başarısız olursa OpenClaw MP3 ile yeniden dener.


OpenAI/ElevenLabs çıktı biçimleri kanal başına sabittir (yukarıya bakın).

## Otomatik TTS davranışı

`messages.tts.auto` etkinleştirildiğinde OpenClaw:

  * Yanıt zaten medya veya bir `MEDIA:` direktifi içeriyorsa TTS'yi atlar.
  * Çok kısa yanıtları atlar (10 karakterin altında).
  * Özetler etkinleştirildiğinde uzun yanıtları `summaryModel` (veya `agents.defaults.model.primary`) kullanarak özetler.
  * Üretilen sesi yanıta ekler.
  * `mode: "final"` içinde, metin akışı tamamlandıktan sonra akışlı son yanıtlar için yine de yalnızca ses TTS gönderir; üretilen medya, normal yanıt ekleriyle aynı kanal medya normalizasyonundan geçer.


Yanıt `maxLength` değerini aşarsa ve özet kapalıysa (veya özet modeli için API anahtarı yoksa), ses atlanır ve normal metin yanıtı gönderilir.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Kanala göre çıktı biçimleri

Hedef | Biçim  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Sesli not yanıtları **Opus** tercih eder (ElevenLabs'ten `opus_48000_64`, OpenAI'dan `opus`). 48 kHz / 64 kbps netlik ve boyutu dengeler.  
Diğer kanallar | **MP3** (ElevenLabs'ten `mp3_44100_128`, OpenAI'dan `mp3`). Konuşma için varsayılan 44,1 kHz / 128 kbps.  
Konuşma / telefon | Sağlayıcıya özgü **PCM** (Inworld 22050 Hz, Google 24 kHz) veya telefon için Gradium'dan `ulaw_8000`.  
  
Sağlayıcıya göre notlar:

  * **Feishu / WhatsApp dönüştürme:** Bir sesli not yanıtı MP3/WebM/WAV/M4A olarak geldiğinde, kanal Plugin'i `ffmpeg` ile 48 kHz Ogg/Opus'a dönüştürür. WhatsApp, Baileys üzerinden `ptt: true` ve `audio/ogg; codecs=opus` ile gönderir. Dönüştürme başarısız olursa: Feishu özgün dosyayı eklemeye geri döner; WhatsApp ise uyumsuz bir PTT yükü göndermek yerine gönderimi başarısız yapar.
  * **MiniMax / Xiaomi MiMo:** Varsayılan MP3 (MiniMax `speech-2.8-hd` için 32 kHz); sesli not hedefleri için `ffmpeg` ile 48 kHz Opus'a dönüştürülür.
  * **Yerel CLI:** Yapılandırılmış `outputFormat` değerini kullanır. Sesli not hedefleri Ogg/Opus'a, telefon çıktısı ise ham 16 kHz mono PCM'ye dönüştürülür.
  * **Google Gemini:** Ham 24 kHz PCM döndürür. OpenClaw ekler için WAV olarak sarar, sesli not hedefleri için 48 kHz Opus'a dönüştürür, Konuşma/telefon için PCM'yi doğrudan döndürür.
  * **Inworld:** MP3 ekleri, yerel `OGG_OPUS` sesli notu, Konuşma/telefon için ham `PCM` 22050 Hz.
  * **xAI:** Varsayılan olarak MP3; `responseFormat`, `mp3|wav|pcm|mulaw|alaw` olabilir. xAI'nin toplu REST uç noktasını kullanır — akışlı WebSocket TTS **kullanılmaz**. Yerel Opus sesli not biçimi **desteklenmez**.
  * **Microsoft:** `microsoft.outputFormat` kullanır (varsayılan `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice`, OGG/MP3/M4A kabul eder; garantili Opus sesli mesajları gerekiyorsa OpenAI/ElevenLabs kullanın. Yapılandırılmış Microsoft biçimi başarısız olursa OpenClaw MP3 ile yeniden dener.


OpenAI ve ElevenLabs çıktı biçimleri, yukarıda listelendiği gibi kanal başına sabittir.

## Alan başvurusu

Top-level messages.tts.*

Otomatik TTS modu. `inbound` yalnızca gelen bir sesli mesajdan sonra ses gönderir; `tagged` yalnızca yanıt `[[tts:...]]` yönergeleri veya bir `[[tts:text]]` bloğu içerdiğinde ses gönderir.

Eski geçiş anahtarı. `openclaw doctor --fix` bunu `auto` değerine taşır.

`"all"`, son yanıtlara ek olarak araç/blok yanıtlarını da içerir.

Konuşma sağlayıcısı kimliği. Ayarlanmadığında OpenClaw, kayıt defteri otomatik seçim sırasındaki ilk yapılandırılmış sağlayıcıyı kullanır. Eski `provider: "edge"`, `openclaw doctor --fix` tarafından `"microsoft"` olarak yeniden yazılır.

`personas` içindeki etkin persona kimliği. Küçük harfe normalleştirilir.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Kararlı konuşulan kimlik. Alanlar: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Bkz. Personalar.

Otomatik özet için ucuz model; varsayılan `agents.defaults.model.primary`. `provider/model` veya yapılandırılmış bir model takma adını kabul eder.

Modelin TTS yönergeleri yaymasına izin verin. `enabled` varsayılan olarak `true`; `allowProvider` varsayılan olarak `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Konuşma sağlayıcısı kimliğine göre anahtarlanan, sağlayıcıya ait ayarlar. Eski doğrudan bloklar (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) `openclaw doctor --fix` tarafından yeniden yazılır; yalnızca `messages.tts.providers.<id>` kaydedin.

TTS giriş karakterleri için katı üst sınır. Aşılırsa `/tts audio` başarısız olur.

Milisaniye cinsinden istek zaman aşımı.

Yerel tercihler JSON yolunu (sağlayıcı/sınır/özet) geçersiz kılın. Varsayılan `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` veya `SPEECH_KEY` değerine geri döner. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Azure Speech bölgesi (örn. `eastus`). Env: `AZURE_SPEECH_REGION` veya `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci İsteğe bağlı Azure Speech uç noktası geçersiz kılması (takma ad `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Azure ses ShortName'i. Varsayılan `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI SSML dil kodu. Varsayılan `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Standart ses için Azure `X-Microsoft-OutputFormat`. Varsayılan `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Sesli not çıktısı için Azure `X-Microsoft-OutputFormat`. Varsayılan `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `ELEVENLABS_API_KEY` veya `XI_API_KEY` değerine geri döner. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Model kimliği (örn. `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (her biri `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2 harfli ISO 639-1 (örn. `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI En iyi çaba determinizmi için `0..4294967295` tamsayısı. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `GEMINI_API_KEY` / `GOOGLE_API_KEY` değerine geri döner. Atlanırsa TTS, env geri dönüşünden önce `models.providers.google.apiKey` değerini yeniden kullanabilir. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Gemini TTS modeli. Varsayılan `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Gemini önceden oluşturulmuş ses adı. Varsayılan `Kore`. Takma ad: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Etkin persona istem alanlarını deterministik bir Gemini TTS istem yapısına sarmak için `audio-profile-v1` olarak ayarlayın. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Yalnızca `https://generativelanguage.googleapis.com` kabul edilir. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Varsayılan Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld birincil

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Varsayılan `inworld-tts-1.5-max`. Ayrıca: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Varsayılan `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Örnekleme sıcaklığı `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Local CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Komut argümanları. `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}` yer tutucularını destekler. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Beklenen CLI çıktı biçimi. Ses ekleri için varsayılan `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Komut zaman aşımı, milisaniye cinsinden. Varsayılan `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (no API key)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Microsoft neural voice adı (örn. `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Dil kodu (örn. `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Microsoft çıktı biçimi. Varsayılan `audio-24khz-48kbitrate-mono-mp3`. Paketle gelen Edge destekli aktarım tüm biçimleri desteklemez. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Yüzde dizeleri (örn. `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Eski diğer ad. Kalıcı yapılandırmayı `providers.microsoft` olarak yeniden yazmak için `openclaw doctor --fix` çalıştırın. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `MINIMAX_API_KEY` değerine geri döner. Token Plan kimlik doğrulaması `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` veya `MINIMAX_CODING_API_KEY` üzerinden yapılır. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://api.minimax.io`. Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Varsayılan `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Varsayılan `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Varsayılan `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Varsayılan `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Tam sayı `-12..12`. Varsayılan `0`. Kesirli değerler istekten önce kırpılır. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg `OPENAI_API_KEY` değerine geri döner. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci OpenAI TTS model kimliği (örn. `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Ses adı (örn. `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Açık OpenAI `instructions` alanı. Ayarlandığında persona istem alanları otomatik olarak eşlenmez. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Oluşturulan OpenAI TTS alanlarından sonra `/audio/speech` istek gövdelerine birleştirilen ek JSON alanları. Bunu, `lang` gibi sağlayıcıya özgü anahtarlar gerektiren Kokoro gibi OpenAI uyumlu uç noktalar için kullanın; güvensiz prototip anahtarları yoksayılır. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI TTS uç noktasını geçersiz kıl. Çözümleme sırası: config → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Varsayılan olmayan değerler OpenAI uyumlu TTS uç noktaları olarak ele alınır, bu nedenle özel model ve ses adları kabul edilir.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY`. `models.providers.openrouter.apiKey` yeniden kullanılabilir. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://openrouter.ai/api/v1`. Eski `https://openrouter.ai/v1` normalleştirilir. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Varsayılan `hexgrad/kokoro-82m`. Diğer ad: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Varsayılan `af_alloy`. Diğer ad: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Varsayılan `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` veya `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Varsayılan `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Projenizde TTS 2.0 yetkisi varsa `seed-tts-2.0` kullanın. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg App key üstbilgisi. Varsayılan `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Seed Speech TTS HTTP uç noktasını geçersiz kıl. Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Ses türü. Varsayılan `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Eski Volcengine Speech Console alanları. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (varsayılan `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://api.x.ai/v1`. Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Varsayılan `eve`. Canlı sesler: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci BCP-47 dil kodu veya `auto`. Varsayılan `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Varsayılan `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Varsayılan `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Varsayılan `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. `mimo-v2-tts` de desteklenir. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Varsayılan `mimo_default`. Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Varsayılan `mp3`. Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Ajan aracı

`tts` aracı metni konuşmaya dönüştürür ve yanıt teslimi için bir ses eki döndürür. Feishu, Matrix, Telegram ve WhatsApp üzerinde ses, dosya eki yerine sesli mesaj olarak teslim edilir. Feishu ve WhatsApp, `ffmpeg` mevcut olduğunda bu yolda Opus olmayan TTS çıktısını dönüştürebilir.

WhatsApp, sesi Baileys üzerinden PTT ses notu olarak gönderir (`audio`, `ptt: true` ile) ve görünür metni PTT sesinden **ayrı** gönderir, çünkü istemciler ses notlarında başlıkları tutarlı biçimde işlemez.

Araç isteğe bağlı `channel` ve `timeoutMs` alanlarını kabul eder; `timeoutMs`, çağrı başına sağlayıcı istek zaman aşımıdır ve milisaniye cinsindendir.

## Gateway RPC

Yöntem | Amaç  
---|---  
`tts.status` | Geçerli TTS durumunu ve son denemeyi oku.  
`tts.enable` | Yerel otomatik tercihi `always` olarak ayarla.  
`tts.disable` | Yerel otomatik tercihi `off` olarak ayarla.  
`tts.convert` | Tek seferlik metin → ses.  
`tts.setProvider` | Yerel sağlayıcı tercihini ayarla.  
`tts.setPersona` | Yerel persona tercihini ayarla.  
`tts.providers` | Yapılandırılmış sağlayıcıları ve durumu listele.  
  
## Hizmet bağlantıları

  * [OpenAI metinden konuşmaya kılavuzu](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API başvurusu](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST metinden konuşmaya](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Azure Speech sağlayıcısı](</tr/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs Authentication](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</tr/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</tr/providers/volcengine#text-to-speech>)
  * [Xiaomi MiMo konuşma sentezi](</tr/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech çıktı biçimleri](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI metinden konuşmaya](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## İlgili

  * [Medya genel bakışı](</tr/tools/media-overview>)
  * [Müzik oluşturma](</tr/tools/music-generation>)
  * [Video oluşturma](</tr/tools/video-generation>)
  * [Slash komutları](</tr/tools/slash-commands>)
  * [Sesli arama plugin'i](</tr/plugins/voice-call>)


Was this useful?YesNo