---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/tr/providers/google
scraped_at: 2026-05-25
---

Google Plugin'i, Google AI Studio üzerinden Gemini modellerine erişimin yanı sıra görüntü oluşturma, medya anlama (görüntü/ses/video), metinden sese dönüştürme ve Gemini Grounding aracılığıyla web araması sağlar.

  * Sağlayıcı: `google`
  * Kimlik doğrulama: `GEMINI_API_KEY` veya `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Çalışma zamanı seçeneği: sağlayıcı/model `agentRuntime.id: "google-gemini-cli"` model başvurularını `google/*` olarak kanonik tutarken Gemini CLI OAuth'u yeniden kullanır.


## Başlarken

Tercih ettiğiniz kimlik doğrulama yöntemini seçin ve kurulum adımlarını izleyin.

### API key

**En uygun kullanım:** Google AI Studio üzerinden standart Gemini API erişimi.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Ya da anahtarı doğrudan geçirin:

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

**En uygun kullanım:** ayrı bir API anahtarı yerine PKCE OAuth aracılığıyla mevcut bir Gemini CLI oturumunu yeniden kullanma.

* ### Install the Gemini CLI

Yerel `gemini` komutu `PATH` üzerinde kullanılabilir olmalıdır.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw, yaygın Windows/npm düzenleri dahil olmak üzere hem Homebrew kurulumlarını hem de global npm kurulumlarını destekler.

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

  * Varsayılan model: `google/gemini-3.1-pro-preview`
  * Çalışma zamanı: `google-gemini-cli`
  * Takma ad: `gemini-cli`


Gemini 3.1 Pro'nun Gemini API model kimliği `gemini-3.1-pro-preview` şeklindedir. OpenClaw, kolaylık takma adı olarak daha kısa `google/gemini-3.1-pro` değerini kabul eder ve sağlayıcı çağrılarından önce bunu normalleştirir.

**Ortam değişkenleri:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Ya da `GEMINI_CLI_*` varyantları.)

`google-gemini-cli/*` model başvuruları eski uyumluluk takma adlarıdır. Yeni yapılandırmalar, yerel Gemini CLI yürütmesi istediklerinde `google/*` model başvurularını ve `google-gemini-cli` çalışma zamanını kullanmalıdır.

## Yetenekler

Yetenek | Destekleniyor  
---|---  
Sohbet tamamlamaları | Evet  
Görüntü oluşturma | Evet  
Müzik oluşturma | Evet  
Metinden sese | Evet  
Gerçek zamanlı ses | Evet (Google Live API)  
Görüntü anlama | Evet  
Ses transkripsiyonu | Evet  
Video anlama | Evet  
Web araması (Grounding) | Evet  
Düşünme/akıl yürütme | Evet (Gemini 2.5+ / Gemini 3+)  
Gemma 4 modelleri | Evet  
  
## Web araması

Paketlenen `gemini` web araması sağlayıcısı, Gemini Google Search grounding kullanır. `plugins.entries.google.config.webSearch` altında özel bir arama anahtarı yapılandırın ya da `GEMINI_API_KEY` sonrasında `models.providers.google.apiKey` değerini yeniden kullanmasına izin verin:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Kimlik bilgisi önceliği önce özel `webSearch.apiKey`, sonra `GEMINI_API_KEY`, ardından `models.providers.google.apiKey` şeklindedir. `webSearch.baseUrl` isteğe bağlıdır ve operatör proxy'leri veya uyumlu Gemini API uç noktaları için bulunur; atlandığında Gemini web araması `models.providers.google.baseUrl` değerini yeniden kullanır. Sağlayıcıya özgü araç davranışı için [Gemini araması](</tr/tools/gemini-search>) bölümüne bakın.

## Görüntü oluşturma

Paketlenen `google` görüntü oluşturma sağlayıcısı varsayılan olarak `google/gemini-3.1-flash-image-preview` kullanır.

  * `google/gemini-3-pro-image-preview` da desteklenir
  * Oluşturma: istek başına en fazla 4 görüntü
  * Düzenleme modu: etkin, en fazla 5 giriş görüntüsü
  * Geometri denetimleri: `size`, `aspectRatio` ve `resolution`


Google'ı varsayılan görüntü sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Video oluşturma

Paketlenen `google` Plugin'i, paylaşılan `video_generate` aracı üzerinden video oluşturmayı da kaydeder.

  * Varsayılan video modeli: `google/veo-3.1-fast-generate-preview`
  * Modlar: metinden videoya, görüntüden videoya ve tek video referans akışları
  * `aspectRatio` (`16:9`, `9:16`) ve `resolution` (`720P`, `1080P`) destekler; ses çıktısı bugün Veo tarafından desteklenmez
  * Desteklenen süreler: **4, 6 veya 8 saniye** (diğer değerler en yakın izin verilen değere yuvarlanır)


Google'ı varsayılan video sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Müzik oluşturma

Paketlenen `google` Plugin'i, paylaşılan `music_generate` aracı üzerinden müzik oluşturmayı da kaydeder.

  * Varsayılan müzik modeli: `google/lyria-3-clip-preview`
  * `google/lyria-3-pro-preview` da desteklenir
  * İstem denetimleri: `lyrics` ve `instrumental`
  * Çıkış biçimi: varsayılan olarak `mp3`, ayrıca `google/lyria-3-pro-preview` üzerinde `wav`
  * Referans girişleri: en fazla 10 görüntü
  * Oturum destekli çalıştırmalar, `action: "status"` dahil olmak üzere paylaşılan görev/durum akışı üzerinden ayrılır


Google'ı varsayılan müzik sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Metinden sese

Paketlenen `google` konuşma sağlayıcısı, Gemini API TTS yolunu `gemini-3.1-flash-tts-preview` ile kullanır.

  * Varsayılan ses: `Kore`
  * Kimlik doğrulama: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` veya `GOOGLE_API_KEY`
  * Çıkış: normal TTS ekleri için WAV, sesli not hedefleri için Opus, Talk/telephony için PCM
  * Sesli not çıktısı: Google PCM, WAV olarak sarılır ve `ffmpeg` ile 48 kHz Opus'a dönüştürülür


Google'ın toplu Gemini TTS yolu, tamamlanmış `generateContent` yanıtında oluşturulan sesi döndürür. En düşük gecikmeli konuşmalı görüşmeler için toplu TTS yerine Gemini Live API tarafından desteklenen Google gerçek zamanlı ses sağlayıcısını kullanın.

Google'ı varsayılan TTS sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS, stil denetimi için doğal dil istemleri kullanır. Konuşulan metinden önce yeniden kullanılabilir bir stil istemi eklemek için `audioProfile` ayarlayın. İstem metniniz adlandırılmış bir konuşmacıya atıfta bulunuyorsa `speakerName` ayarlayın.

Gemini API TTS ayrıca metinde `[whispers]` veya `[laughs]` gibi ifadeli köşeli parantez ses etiketlerini kabul eder. Etiketleri görünür sohbet yanıtının dışında tutarken TTS'ye göndermek için bunları bir `[[tts:text]]...[[/tts:text]]` bloğunun içine koyun:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Gerçek zamanlı ses

Paketlenen `google` Plugin'i, Voice Call ve Google Meet gibi arka uç ses köprüleri için Gemini Live API tarafından desteklenen bir gerçek zamanlı ses sağlayıcısı kaydeder.

Ayar | Yapılandırma yolu | Varsayılan  
---|---|---  
Model | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Ses | `...google.voice` | `Kore`  
Sıcaklık | `...google.temperature` | (ayarlanmamış)  
VAD başlangıç hassasiyeti | `...google.startSensitivity` | (ayarlanmamış)  
VAD bitiş hassasiyeti | `...google.endSensitivity` | (ayarlanmamış)  
Sessizlik süresi | `...google.silenceDurationMs` | (ayarlanmamış)  
Etkinlik işleme | `...google.activityHandling` | Google varsayılanı, `start-of-activity-interrupts`  
Tur kapsamı | `...google.turnCoverage` | Google varsayılanı, `only-activity`  
Otomatik VAD'yi devre dışı bırak | `...google.automaticActivityDetectionDisabled` | `false`  
Oturum sürdürme | `...google.sessionResumption` | `true`  
Bağlam sıkıştırma | `...google.contextWindowCompression` | `true`  
API anahtarı | `...google.apiKey` | `models.providers.google.apiKey`, `GEMINI_API_KEY` veya `GOOGLE_API_KEY` değerine geri döner  
  
Örnek Voice Call gerçek zamanlı yapılandırması:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Bakımcı canlı doğrulaması için `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts` çalıştırın. Smoke, OpenAI arka uç/WebRTC yollarını da kapsar; Google ayağı, Control UI Talk tarafından kullanılan aynı kısıtlı Live API belirteci şeklini üretir, tarayıcı WebSocket uç noktasını açar, ilk kurulum yükünü gönderir ve `setupComplete` için bekler.

## Gelişmiş yapılandırma

Doğrudan Gemini önbellek yeniden kullanımı

Doğrudan Gemini API çalıştırmaları (`api: "google-generative-ai"`) için OpenClaw, yapılandırılmış bir `cachedContent` tanıtıcısını Gemini isteklerine geçirir.

  * Model başına veya genel parametreleri `cachedContent` ya da eski `cached_content` ile yapılandırın
  * İkisi de varsa `cachedContent` kazanır
  * Örnek değer: `cachedContents/prebuilt-context`
  * Gemini önbellek isabeti kullanımı, yukarı akış `cachedContentTokenCount` değerinden OpenClaw `cacheRead` içine normalize edilir

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON kullanım notları

`google-gemini-cli` OAuth sağlayıcısı kullanılırken OpenClaw, CLI JSON çıktısını aşağıdaki şekilde normalize eder:

  * Yanıt metni, CLI JSON `response` alanından gelir.
  * CLI `usage` değerini boş bıraktığında kullanım `stats` değerine geri döner.
  * `stats.cached`, OpenClaw `cacheRead` içine normalize edilir.
  * `stats.input` eksikse OpenClaw, giriş belirteçlerini `stats.input_tokens - stats.cached` değerinden türetir.

Ortam ve daemon kurulumu

Gateway bir daemon (launchd/systemd) olarak çalışıyorsa `GEMINI_API_KEY` değerinin bu süreç tarafından kullanılabildiğinden emin olun (örneğin, `~/.openclaw/.env` içinde veya `env.shellEnv` üzerinden).

## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Görüntü oluşturma** Paylaşılan görüntü aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/image-generation>) [**Video oluşturma** Paylaşılan video aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/video-generation>) [**Müzik oluşturma** Paylaşılan müzik aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/music-generation>)

Was this useful?YesNo