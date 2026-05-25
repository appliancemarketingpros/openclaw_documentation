---
title: Teks ke ucapan
source_url: https://docs.openclaw.ai/id/tools/tts
scraped_at: 2026-05-25
---

OpenClaw dapat mengonversi balasan keluar menjadi audio di **14 penyedia ucapan** dan mengirim pesan suara native di Feishu, Matrix, Telegram, dan WhatsApp, lampiran audio di tempat lain, serta stream PCM/Ulaw untuk telepon dan Talk.

TTS adalah separuh keluaran ucapan dari mode `stt-tts` Talk. Sesi Talk `realtime` native penyedia menyintesis ucapan di dalam penyedia realtime, bukan memanggil jalur TTS ini, sementara sesi `transcription` tidak menyintesis respons suara asisten.

## Mulai cepat

* ### Pilih penyedia

OpenAI dan ElevenLabs adalah opsi hosted yang paling andal. Microsoft dan Local CLI berfungsi tanpa kunci API. Lihat matriks penyedia untuk daftar lengkapnya.

* ### Atur kunci API

Ekspor variabel env untuk penyedia Anda (misalnya `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft dan Local CLI tidak memerlukan kunci.

* ### Aktifkan di konfigurasi

Atur `messages.tts.auto: "always"` dan `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Coba di chat

`/tts status` menampilkan status saat ini. `/tts audio Hello from OpenClaw` mengirim balasan audio sekali pakai.

## Penyedia yang didukung

Penyedia | Auth | Catatan  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (juga `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Keluaran catatan suara Ogg/Opus native dan telepon.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS kompatibel OpenAI. Default ke `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` atau `XI_API_KEY` | Kloning suara, multibahasa, deterministik melalui `seed`; di-stream untuk pemutaran suara Discord.  
**Google Gemini** | `GEMINI_API_KEY` atau `GOOGLE_API_KEY` | TTS batch Gemini API; sadar persona melalui `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Keluaran catatan suara dan telepon.  
**Inworld** | `INWORLD_API_KEY` | API TTS streaming. Catatan suara Opus native dan telepon PCM.  
**Local CLI** | tidak ada | Menjalankan perintah TTS lokal yang dikonfigurasi.  
**Microsoft** | tidak ada | TTS neural Edge publik melalui `node-edge-tts`. Upaya terbaik, tanpa SLA.  
**MiniMax** | `MINIMAX_API_KEY` (atau Paket Token: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | API T2A v2. Default ke `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Juga digunakan untuk ringkasan otomatis; mendukung persona `instructions`.  
**OpenRouter** | `OPENROUTER_API_KEY` (dapat memakai ulang `models.providers.openrouter.apiKey`) | Model default `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` atau `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/token lama: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | API HTTP BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Penyedia gambar, video, dan ucapan bersama.  
**xAI** | `XAI_API_KEY` | TTS batch xAI. Catatan suara Opus native **tidak** didukung.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | TTS MiMo melalui completion chat Xiaomi.  
  
Jika beberapa penyedia dikonfigurasi, penyedia yang dipilih digunakan terlebih dahulu dan yang lain menjadi opsi fallback. Ringkasan otomatis menggunakan `summaryModel` (atau `agents.defaults.model.primary`), sehingga penyedia tersebut juga harus diautentikasi jika Anda tetap mengaktifkan ringkasan.

## Konfigurasi

Konfigurasi TTS berada di bawah `messages.tts` dalam `~/.openclaw/openclaw.json`. Pilih preset dan sesuaikan blok penyedia:

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

### Microsoft (tanpa kunci)

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

### Penggantian suara per agen

Gunakan `agents.list[].tts` ketika satu agen harus berbicara dengan penyedia, suara, model, persona, atau mode Auto-TTS yang berbeda. Blok agen melakukan deep merge di atas `messages.tts`, sehingga kredensial penyedia dapat tetap berada di konfigurasi penyedia global:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Untuk menetapkan persona per agen, atur `agents.list[].tts.persona` bersama konfigurasi provider — ini menimpa `messages.tts.persona` global hanya untuk agen tersebut.

Urutan prioritas untuk balasan otomatis, `/tts audio`, `/tts status`, dan tool agen `tts`:

  1. `messages.tts`
  2. `agents.list[].tts` aktif
  3. override channel, ketika channel mendukung `channels.<channel>.tts`
  4. override akun, ketika channel meneruskan `channels.<channel>.accounts.<id>.tts`
  5. preferensi `/tts` lokal untuk host ini
  6. direktif inline `[[tts:...]]` ketika override model diaktifkan


Override channel dan akun menggunakan bentuk yang sama seperti `messages.tts` dan melakukan deep-merge di atas lapisan sebelumnya, sehingga kredensial provider bersama dapat tetap berada di `messages.tts` sementara channel atau akun bot hanya mengubah suara, model, persona, atau mode otomatis:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Persona

**Persona** adalah identitas lisan stabil yang dapat diterapkan secara deterministik di berbagai provider. Persona dapat mengutamakan satu provider, mendefinisikan intensi prompt yang netral terhadap provider, dan membawa binding khusus provider untuk suara, model, template prompt, seed, dan pengaturan suara.

### Persona minimal

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Persona lengkap (prompt netral provider)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Resolusi persona

Persona aktif dipilih secara deterministik:

  1. preferensi lokal `/tts persona <id>`, jika diatur.
  2. `messages.tts.persona`, jika diatur.
  3. Tanpa persona.


Pemilihan provider berjalan dengan prioritas eksplisit:

  1. Override langsung (CLI, Gateway, Talk, direktif TTS yang diizinkan).
  2. preferensi lokal `/tts provider <id>`.
  3. `provider` milik persona aktif.
  4. `messages.tts.provider`.
  5. Pemilihan otomatis registry.


Untuk setiap upaya provider, OpenClaw menggabungkan konfigurasi dalam urutan ini:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Override permintaan tepercaya
  4. Override direktif TTS yang dipancarkan model dan diizinkan


### Cara provider menggunakan prompt persona

Field prompt persona (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) bersifat **netral terhadap provider**. Setiap provider memutuskan cara menggunakannya:

Google Gemini

Membungkus field prompt persona dalam struktur prompt TTS Gemini **hanya ketika** konfigurasi provider Google efektif mengatur `promptTemplate: "audio-profile-v1"` atau `personaPrompt`. Field lama `audioProfile` dan `speakerName` masih ditambahkan di awal sebagai teks prompt khusus Google. Tag audio inline seperti `[whispers]` atau `[laughs]` di dalam blok `[[tts:text]]` dipertahankan di dalam transkrip Gemini; OpenClaw tidak membuat tag ini.

OpenAI

Memetakan field prompt persona ke field permintaan `instructions` **hanya ketika** tidak ada `instructions` OpenAI eksplisit yang dikonfigurasi. `instructions` eksplisit selalu menang.

Provider lain

Hanya menggunakan binding persona khusus provider di bawah `personas.<id>.providers.<provider>`. Field prompt persona diabaikan kecuali provider menerapkan pemetaan prompt-persona sendiri.

### Kebijakan fallback

`fallbackPolicy` mengontrol perilaku ketika persona **tidak memiliki binding** untuk provider yang dicoba:

Kebijakan | Perilaku  
---|---  
`preserve-persona` | **Default.** Field prompt yang netral terhadap provider tetap tersedia; provider dapat menggunakannya atau mengabaikannya.  
`provider-defaults` | Persona dihilangkan dari persiapan prompt untuk upaya tersebut; provider menggunakan default netralnya sementara fallback ke provider lain berlanjut.  
`fail` | Lewati upaya provider tersebut dengan `reasonCode: "not_configured"` dan `personaBinding: "missing"`. Provider fallback tetap dicoba.  
  
Seluruh permintaan TTS hanya gagal ketika **setiap** provider yang dicoba dilewati atau gagal.

Pemilihan provider sesi Talk dibatasi pada sesi. Klien Talk sebaiknya memilih id provider, id model, id suara, dan locale dari `talk.catalog` dan meneruskannya melalui sesi Talk atau permintaan handoff. Membuka sesi suara sebaiknya tidak mengubah `messages.tts` atau default provider Talk global.

## Direktif berbasis model

Secara default, asisten **dapat** memancarkan direktif `[[tts:...]]` untuk menimpa suara, model, atau kecepatan untuk satu balasan, plus blok opsional `[[tts:text]]...[[/tts:text]]` untuk isyarat ekspresif yang seharusnya muncul hanya dalam audio:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Ketika `messages.tts.auto` adalah `"tagged"`, **direktif diperlukan** untuk memicu audio. Pengiriman blok streaming menghapus direktif dari teks yang terlihat sebelum channel melihatnya, bahkan ketika terpisah di blok yang bersebelahan.

`provider=...` diabaikan kecuali `modelOverrides.allowProvider: true`. Ketika sebuah balasan mendeklarasikan `provider=...`, key lain dalam direktif tersebut diurai hanya oleh provider tersebut; key yang tidak didukung dihapus dan dilaporkan sebagai peringatan direktif TTS.

**Key direktif yang tersedia:**

  * `provider` (id provider terdaftar; memerlukan `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (volume MiniMax, 0–10)
  * `pitch` (pitch bilangan bulat MiniMax, −12 hingga 12; nilai pecahan dipotong)
  * `emotion` (tag emosi Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Nonaktifkan override model sepenuhnya:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Izinkan pengalihan provider sambil tetap menjaga knob lain dapat dikonfigurasi:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Perintah slash

Satu perintah `/tts`. Di Discord, OpenClaw juga mendaftarkan `/voice` karena `/tts` adalah perintah bawaan Discord — teks `/tts ...` tetap berfungsi.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Catatan perilaku:

  * `/tts on` menulis preferensi TTS lokal ke `always`; `/tts off` menulisnya ke `off`.
  * `/tts chat on|off|default` menulis override TTS otomatis yang dibatasi sesi untuk chat saat ini.
  * `/tts persona <id>` menulis preferensi persona lokal; `/tts persona off` menghapusnya.
  * `/tts latest` membaca balasan asisten terbaru dari transkrip sesi saat ini dan mengirimkannya sebagai audio satu kali. Perintah ini hanya menyimpan hash balasan tersebut pada entri sesi untuk menekan pengiriman suara duplikat.
  * `/tts audio` menghasilkan balasan audio sekali pakai (tidak **mengaktifkan** TTS).
  * `limit` dan `summary` disimpan di **preferensi lokal** , bukan konfigurasi utama.
  * `/tts status` menyertakan diagnostik fallback untuk upaya terbaru — `Fallback: <primary> -> <used>`, `Attempts: ...`, dan detail per upaya (`provider:outcome(reasonCode) latency`).
  * `/status` menampilkan mode TTS aktif plus provider, model, suara, dan metadata endpoint kustom yang disanitasi ketika TTS diaktifkan.


## Preferensi per pengguna

Perintah slash menulis override lokal ke `prefsPath`. Default-nya adalah `~/.openclaw/settings/tts.json`; timpa dengan variabel env `OPENCLAW_TTS_PREFS` atau `messages.tts.prefsPath`.

Field tersimpan | Efek  
---|---  
`auto` | Override TTS otomatis lokal (`always`, `off`, …)  
`provider` | Override provider utama lokal  
`persona` | Override persona lokal  
`maxLength` | Ambang ringkasan (default `1500` karakter)  
`summarize` | Toggle ringkasan (default `true`)  
  
Ini menimpa konfigurasi efektif dari `messages.tts` plus blok `agents.list[].tts` aktif untuk host tersebut.

## Format output (tetap)

Pengiriman suara TTS digerakkan oleh kapabilitas channel. Plugin channel mengiklankan apakah TTS bergaya suara harus meminta target `voice-note` native kepada provider atau mempertahankan sintesis `audio-file` normal dan hanya menandai output yang kompatibel untuk pengiriman suara.

  * **Saluran yang mendukung catatan suara** : balasan catatan suara lebih memilih Opus (`opus_48000_64` dari ElevenLabs, `opus` dari OpenAI). 
    * 48kHz / 64kbps adalah tradeoff yang baik untuk pesan suara.
  * **Feishu / WhatsApp** : ketika balasan catatan suara dibuat sebagai MP3/WebM/WAV/M4A atau file audio lain yang kemungkinan sesuai, Plugin saluran mentranskodenya ke 48kHz Ogg/Opus dengan `ffmpeg` sebelum mengirim pesan suara native. WhatsApp mengirim hasilnya melalui payload `audio` Baileys dengan `ptt: true` dan `audio/ogg; codecs=opus`. Jika konversi gagal, Feishu menerima file asli sebagai lampiran; pengiriman WhatsApp gagal alih-alih memposting payload PTT yang tidak kompatibel.
  * **Saluran lain** : MP3 (`mp3_44100_128` dari ElevenLabs, `mp3` dari OpenAI). 
    * 44.1kHz / 128kbps adalah keseimbangan default untuk kejernihan ucapan.
  * **MiniMax** : MP3 (model `speech-2.8-hd`, laju sampel 32kHz) untuk lampiran audio normal. Untuk target catatan suara yang diiklankan saluran, OpenClaw mentranskode MP3 MiniMax ke Opus 48kHz dengan `ffmpeg` sebelum pengiriman ketika saluran mengiklankan transcoding.
  * **Xiaomi MiMo** : MP3 secara default, atau WAV ketika dikonfigurasi. Untuk target catatan suara yang diiklankan saluran, OpenClaw mentranskode output Xiaomi ke Opus 48kHz dengan `ffmpeg` sebelum pengiriman ketika saluran mengiklankan transcoding.
  * **CLI Lokal** : menggunakan `outputFormat` yang dikonfigurasi. Target catatan suara dikonversi ke Ogg/Opus dan output telepon dikonversi ke PCM mono mentah 16 kHz dengan `ffmpeg`.
  * **Google Gemini** : TTS Gemini API mengembalikan PCM mentah 24kHz. OpenClaw membungkusnya sebagai WAV untuk lampiran audio, mentranskodenya ke Opus 48kHz untuk target catatan suara, dan mengembalikan PCM langsung untuk Talk/telepon.
  * **Gradium** : WAV untuk lampiran audio, Opus untuk target catatan suara, dan `ulaw_8000` pada 8 kHz untuk telepon.
  * **Inworld** : MP3 untuk lampiran audio normal, `OGG_OPUS` native untuk target catatan suara, dan `PCM` mentah pada 22050 Hz untuk Talk/telepon.
  * **xAI** : MP3 secara default; `responseFormat` dapat berupa `mp3`, `wav`, `pcm`, `mulaw`, atau `alaw`. OpenClaw menggunakan endpoint TTS REST batch xAI dan mengembalikan lampiran audio lengkap; WebSocket TTS streaming xAI tidak digunakan oleh jalur penyedia ini. Format catatan suara Opus native tidak didukung oleh jalur ini.
  * **Microsoft** : menggunakan `microsoft.outputFormat` (default `audio-24khz-48kbitrate-mono-mp3`). 
    * Transport yang dibundel menerima `outputFormat`, tetapi tidak semua format tersedia dari layanan.
    * Nilai format output mengikuti format output Microsoft Speech (termasuk Ogg/WebM Opus).
    * Telegram `sendVoice` menerima OGG/MP3/M4A; gunakan OpenAI/ElevenLabs jika Anda memerlukan pesan suara Opus yang terjamin.
    * Jika format output Microsoft yang dikonfigurasi gagal, OpenClaw mencoba lagi dengan MP3.


Format output OpenAI/ElevenLabs bersifat tetap per saluran (lihat di atas).

## Perilaku Auto-TTS

Ketika `messages.tts.auto` diaktifkan, OpenClaw:

  * Melewati TTS jika balasan sudah berisi media atau direktif `MEDIA:`.
  * Melewati balasan yang sangat pendek (di bawah 10 karakter).
  * Meringkas balasan panjang ketika ringkasan diaktifkan, menggunakan `summaryModel` (atau `agents.defaults.model.primary`).
  * Melampirkan audio yang dihasilkan ke balasan.
  * Dalam `mode: "final"`, tetap mengirim TTS hanya-audio untuk balasan final yang di-streaming setelah stream teks selesai; media yang dihasilkan melalui normalisasi media saluran yang sama seperti lampiran balasan normal.


Jika balasan melebihi `maxLength` dan ringkasan nonaktif (atau tidak ada API key untuk model ringkasan), audio dilewati dan balasan teks normal dikirim.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Format output berdasarkan saluran

Target | Format  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Balasan catatan suara lebih memilih **Opus** (`opus_48000_64` dari ElevenLabs, `opus` dari OpenAI). 48 kHz / 64 kbps menyeimbangkan kejernihan dan ukuran.  
Saluran lain | **MP3** (`mp3_44100_128` dari ElevenLabs, `mp3` dari OpenAI). 44.1 kHz / 128 kbps default untuk ucapan.  
Talk / telefoni | **PCM** native penyedia (Inworld 22050 Hz, Google 24 kHz), atau `ulaw_8000` dari Gradium untuk telefoni.  
  
Catatan per penyedia:

  * **Transkode Feishu / WhatsApp:** Ketika balasan catatan suara masuk sebagai MP3/WebM/WAV/M4A, plugin saluran mentranskode ke Ogg/Opus 48 kHz dengan `ffmpeg`. WhatsApp mengirim melalui Baileys dengan `ptt: true` dan `audio/ogg; codecs=opus`. Jika konversi gagal: Feishu fallback dengan melampirkan file asli; pengiriman WhatsApp gagal alih-alih memposting payload PTT yang tidak kompatibel.
  * **MiniMax / Xiaomi MiMo:** MP3 default (32 kHz untuk MiniMax `speech-2.8-hd`); ditranskode ke Opus 48 kHz untuk target catatan suara melalui `ffmpeg`.
  * **CLI lokal:** Menggunakan `outputFormat` yang dikonfigurasi. Target catatan suara dikonversi ke Ogg/Opus dan keluaran telefoni ke PCM mono 16 kHz mentah.
  * **Google Gemini:** Mengembalikan PCM 24 kHz mentah. OpenClaw membungkusnya sebagai WAV untuk lampiran, mentranskode ke Opus 48 kHz untuk target catatan suara, mengembalikan PCM langsung untuk Talk/telefoni.
  * **Inworld:** Lampiran MP3, catatan suara `OGG_OPUS` native, `PCM` mentah 22050 Hz untuk Talk/telefoni.
  * **xAI:** MP3 secara default; `responseFormat` dapat berupa `mp3|wav|pcm|mulaw|alaw`. Menggunakan endpoint REST batch xAI — TTS WebSocket streaming **tidak** digunakan. Format catatan suara Opus native **tidak** didukung.
  * **Microsoft:** Menggunakan `microsoft.outputFormat` (default `audio-24khz-48kbitrate-mono-mp3`). `sendVoice` Telegram menerima OGG/MP3/M4A; gunakan OpenAI/ElevenLabs jika Anda memerlukan pesan suara Opus yang dijamin. Jika format Microsoft yang dikonfigurasi gagal, OpenClaw mencoba ulang dengan MP3.


Format keluaran OpenAI dan ElevenLabs ditetapkan per saluran seperti yang tercantum di atas.

## Referensi bidang

Top-level messages.tts.*

Mode Auto-TTS. `inbound` hanya mengirim audio setelah pesan suara masuk; `tagged` hanya mengirim audio ketika balasan menyertakan direktif `[[tts:...]]` atau blok `[[tts:text]]`.

Toggle lama. `openclaw doctor --fix` memigrasikan ini ke `auto`.

`"all"` menyertakan balasan alat/blok selain balasan final.

ID penyedia ucapan. Jika tidak disetel, OpenClaw menggunakan penyedia pertama yang dikonfigurasi dalam urutan pilih otomatis registry. `provider: "edge"` lama ditulis ulang menjadi `"microsoft"` oleh `openclaw doctor --fix`.

ID persona aktif dari `personas`. Dinormalisasi ke huruf kecil.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Identitas lisan yang stabil. Bidang: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Lihat Persona.

Model murah untuk ringkasan otomatis; default ke `agents.defaults.model.primary`. Menerima `provider/model` atau alias model yang dikonfigurasi.

Izinkan model memancarkan direktif TTS. `enabled` default ke `true`; `allowProvider` default ke `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Pengaturan milik penyedia yang dikunci berdasarkan ID penyedia ucapan. Blok langsung lama (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) ditulis ulang oleh `openclaw doctor --fix`; commit hanya `messages.tts.providers.<id>`.

Batas keras untuk karakter input TTS. `/tts audio` gagal jika terlampaui.

Timeout permintaan dalam milidetik.

Timpa path JSON preferensi lokal (penyedia/batas/ringkasan). Default `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, atau `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Region Azure Speech (mis. `eastus`). Env: `AZURE_SPEECH_REGION` atau `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Penimpaan endpoint Azure Speech opsional (alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName suara Azure. Default `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Kode bahasa SSML. Default `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` Azure untuk audio standar. Default `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` Azure untuk keluaran catatan suara. Default `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fallback ke `ELEVENLABS_API_KEY` atau `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ID model (mis. `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (masing-masing `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg ISO 639-1 2 huruf (mis. `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Bilangan bulat `0..4294967295` untuk determinisme best-effort. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fallback ke `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Jika dihilangkan, TTS dapat menggunakan kembali `models.providers.google.apiKey` sebelum fallback env. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Model TTS Gemini. Default `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Nama suara bawaan Gemini. Default `Kore`. Alias: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Setel ke `audio-profile-v1` untuk membungkus bidang prompt persona aktif dalam struktur prompt TTS Gemini yang deterministik. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Hanya `https://generativelanguage.googleapis.com` yang diterima. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Bawaan Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Primer Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Bawaan `inworld-tts-1.5-max`. Juga: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Bawaan `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Suhu sampling `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

CLI Lokal (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Argumen perintah. Mendukung placeholder `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Format output CLI yang diharapkan. Bawaan `mp3` untuk lampiran audio. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Batas waktu perintah dalam milidetik. Bawaan `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (tanpa kunci API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nama suara neural Microsoft (mis. `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Kode bahasa (mis. `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Format output Microsoft. Bawaan `audio-24khz-48kbitrate-mono-mp3`. Tidak semua format didukung oleh transport bawaan berbasis Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg String persen (mis. `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Alias lama. Jalankan `openclaw doctor --fix` untuk menulis ulang konfigurasi tersimpan ke `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fallback ke `MINIMAX_API_KEY`. Autentikasi Token Plan melalui `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, atau `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://api.minimax.io`. Lingkungan: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Bawaan `speech-2.8-hd`. Lingkungan: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Bawaan `English_expressive_narrator`. Lingkungan: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Bawaan `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Bawaan `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Bilangan bulat `-12..12`. Bawaan `0`. Nilai pecahan dipotong sebelum permintaan. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fallback ke `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ID model TTS OpenAI (mis. `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nama suara (mis. `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Kolom OpenAI `instructions` eksplisit. Saat disetel, kolom prompt persona **tidak** dipetakan otomatis. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Kolom JSON tambahan yang digabungkan ke dalam body permintaan `/audio/speech` setelah kolom TTS OpenAI yang dihasilkan. Gunakan ini untuk endpoint yang kompatibel dengan OpenAI seperti Kokoro yang memerlukan kunci khusus penyedia seperti `lang`; kunci prototipe yang tidak aman diabaikan. OPENCLAW_DOCS_MARKER:paramClose:

Override endpoint TTS OpenAI. Urutan resolusi: konfigurasi → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Nilai non-bawaan diperlakukan sebagai endpoint TTS yang kompatibel dengan OpenAI, sehingga nama model dan suara khusus diterima.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `OPENROUTER_API_KEY`. Dapat menggunakan ulang `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://openrouter.ai/api/v1`. Lama `https://openrouter.ai/v1` dinormalisasi. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Bawaan `hexgrad/kokoro-82m`. Alias: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Bawaan `af_alloy`. Alias: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Bawaan `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `VOLCENGINE_TTS_API_KEY` atau `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Bawaan `seed-tts-1.0`. Lingkungan: `VOLCENGINE_TTS_RESOURCE_ID`. Gunakan `seed-tts-2.0` saat proyek Anda memiliki hak TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg Header kunci aplikasi. Bawaan `aGjiRDfUWi`. Lingkungan: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Override endpoint HTTP Seed Speech TTS. Lingkungan: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Jenis suara. Bawaan `en_female_anna_mars_bigtts`. Lingkungan: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Kolom lama Volcengine Speech Console. Lingkungan: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (bawaan `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://api.x.ai/v1`. Lingkungan: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Bawaan `eve`. Suara live: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Kode bahasa BCP-47 atau `auto`. Bawaan `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Bawaan `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Lingkungan: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Bawaan `https://api.xiaomimimo.com/v1`. Lingkungan: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Bawaan `mimo-v2.5-tts`. Lingkungan: `XIAOMI_TTS_MODEL`. Juga mendukung `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Bawaan `mimo_default`. Lingkungan: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Bawaan `mp3`. Lingkungan: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Alat agen

Alat `tts` mengonversi teks menjadi ucapan dan mengembalikan lampiran audio untuk pengiriman balasan. Di Feishu, Matrix, Telegram, dan WhatsApp, audio dikirim sebagai pesan suara, bukan lampiran file. Feishu dan WhatsApp dapat mentranskode output TTS non-Opus pada jalur ini saat `ffmpeg` tersedia.

WhatsApp mengirim audio melalui Baileys sebagai catatan suara PTT (`audio` dengan `ptt: true`) dan mengirim teks yang terlihat **secara terpisah** dari audio PTT karena klien tidak selalu merender keterangan pada catatan suara secara konsisten.

Alat ini menerima kolom `channel` dan `timeoutMs` opsional; `timeoutMs` adalah batas waktu permintaan penyedia per panggilan dalam milidetik.

## RPC Gateway

Metode | Tujuan  
---|---  
`tts.status` | Membaca status TTS saat ini dan percobaan terakhir.  
`tts.enable` | Mengatur preferensi otomatis lokal ke `always`.  
`tts.disable` | Mengatur preferensi otomatis lokal ke `off`.  
`tts.convert` | Teks satu kali → audio.  
`tts.setProvider` | Mengatur preferensi penyedia lokal.  
`tts.setPersona` | Mengatur preferensi persona lokal.  
`tts.providers` | Mencantumkan penyedia yang dikonfigurasi dan statusnya.  
  
## Tautan layanan

  * [Panduan teks-ke-ucapan OpenAI](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Referensi API Audio OpenAI](<https://platform.openai.com/docs/api-reference/audio>)
  * [Teks-ke-ucapan REST Azure Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Penyedia Azure Speech](</id/providers/azure-speech>)
  * [Teks ke Ucapan ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Autentikasi ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</id/providers/gradium>)
  * [API TTS Inworld](<https://docs.inworld.ai/tts/tts>)
  * [API MiniMax T2A v2](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [API HTTP TTS Volcengine](</id/providers/volcengine#text-to-speech>)
  * [Sintesis ucapan Xiaomi MiMo](</id/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Format output Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [Teks ke ucapan xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Terkait

  * [Ikhtisar media](</id/tools/media-overview>)
  * [Pembuatan musik](</id/tools/music-generation>)
  * [Pembuatan video](</id/tools/video-generation>)
  * [Perintah slash](</id/tools/slash-commands>)
  * [Plugin panggilan suara](</id/plugins/voice-call>)


Was this useful?YesNo