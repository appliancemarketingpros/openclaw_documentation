---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/id/providers/google
scraped_at: 2026-05-25
---

Plugin Google menyediakan akses ke model Gemini melalui Google AI Studio, plus pembuatan gambar, pemahaman media (gambar/audio/video), text-to-speech, dan pencarian web melalui Gemini Grounding.

  * Penyedia: `google`
  * Auth: `GEMINI_API_KEY` atau `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Opsi runtime: provider/model `agentRuntime.id: "google-gemini-cli"` menggunakan ulang OAuth Gemini CLI sambil menjaga referensi model tetap kanonis sebagai `google/*`.


## Memulai

Pilih metode auth yang Anda inginkan dan ikuti langkah-langkah penyiapannya.

### Kunci API

**Paling cocok untuk:** akses Gemini API standar melalui Google AI Studio.

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Atau teruskan kunci secara langsung:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Paling cocok untuk:** menggunakan ulang login Gemini CLI yang sudah ada melalui PKCE OAuth alih-alih kunci API terpisah.

* ### Instal Gemini CLI

Perintah `gemini` lokal harus tersedia di `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw mendukung instalasi Homebrew dan instalasi npm global, termasuk tata letak Windows/npm yang umum.

* ### Masuk melalui OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Model default: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * Alias: `gemini-cli`


Id model Gemini API untuk Gemini 3.1 Pro adalah `gemini-3.1-pro-preview`. OpenClaw menerima bentuk yang lebih pendek `google/gemini-3.1-pro` sebagai alias praktis dan menormalisasinya sebelum panggilan penyedia.

**Variabel lingkungan:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Atau varian `GEMINI_CLI_*`.)

Referensi model `google-gemini-cli/*` adalah alias kompatibilitas lama. Konfigurasi baru sebaiknya menggunakan referensi model `google/*` plus runtime `google-gemini-cli` saat menginginkan eksekusi Gemini CLI lokal.

## Kapabilitas

Kapabilitas | Didukung  
---|---  
Penyelesaian chat | Ya  
Pembuatan gambar | Ya  
Pembuatan musik | Ya  
Text-to-speech | Ya  
Suara realtime | Ya (Google Live API)  
Pemahaman gambar | Ya  
Transkripsi audio | Ya  
Pemahaman video | Ya  
Pencarian web (Grounding) | Ya  
Thinking/penalaran | Ya (Gemini 2.5+ / Gemini 3+)  
Model Gemma 4 | Ya  
  
## Pencarian web

Penyedia pencarian web `gemini` bawaan menggunakan Gemini Google Search grounding. Konfigurasikan kunci pencarian khusus di bawah `plugins.entries.google.config.webSearch`, atau biarkan menggunakan ulang `models.providers.google.apiKey` setelah `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Prioritas kredensial adalah `webSearch.apiKey` khusus, lalu `GEMINI_API_KEY`, lalu `models.providers.google.apiKey`. `webSearch.baseUrl` bersifat opsional dan ada untuk proxy operator atau endpoint Gemini API yang kompatibel; jika dihilangkan, pencarian web Gemini menggunakan ulang `models.providers.google.baseUrl`. Lihat [Gemini search](</id/tools/gemini-search>) untuk perilaku tool khusus penyedia.

## Pembuatan gambar

Penyedia pembuatan gambar `google` bawaan menggunakan default `google/gemini-3.1-flash-image-preview`.

  * Juga mendukung `google/gemini-3-pro-image-preview`
  * Buat: hingga 4 gambar per permintaan
  * Mode edit: diaktifkan, hingga 5 gambar input
  * Kontrol geometri: `size`, `aspectRatio`, dan `resolution`


Untuk menggunakan Google sebagai penyedia gambar default:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Pembuatan video

Plugin `google` bawaan juga mendaftarkan pembuatan video melalui tool bersama `video_generate`.

  * Model video default: `google/veo-3.1-fast-generate-preview`
  * Mode: alur teks-ke-video, gambar-ke-video, dan referensi video tunggal
  * Mendukung `aspectRatio` (`16:9`, `9:16`) dan `resolution` (`720P`, `1080P`); output audio belum didukung oleh Veo saat ini
  * Durasi yang didukung: **4, 6, atau 8 detik** (nilai lain disesuaikan ke nilai terdekat yang diizinkan)


Untuk menggunakan Google sebagai penyedia video default:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Pembuatan musik

Plugin `google` bawaan juga mendaftarkan pembuatan musik melalui tool bersama `music_generate`.

  * Model musik default: `google/lyria-3-clip-preview`
  * Juga mendukung `google/lyria-3-pro-preview`
  * Kontrol prompt: `lyrics` dan `instrumental`
  * Format output: `mp3` secara default, plus `wav` pada `google/lyria-3-pro-preview`
  * Input referensi: hingga 10 gambar
  * Proses yang didukung sesi dilepas melalui alur tugas/status bersama, termasuk `action: "status"`


Untuk menggunakan Google sebagai penyedia musik default:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Text-to-speech

Penyedia ucapan `google` bawaan menggunakan jalur TTS Gemini API dengan `gemini-3.1-flash-tts-preview`.

  * Suara default: `Kore`
  * Auth: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY`, atau `GOOGLE_API_KEY`
  * Output: WAV untuk lampiran TTS reguler, Opus untuk target catatan suara, PCM untuk Talk/telepon
  * Output catatan suara: PCM Google dibungkus sebagai WAV dan ditranskode ke Opus 48 kHz dengan `ffmpeg`


Jalur batch Gemini TTS Google mengembalikan audio yang dihasilkan dalam respons `generateContent` yang selesai. Untuk percakapan lisan dengan latensi terendah, gunakan penyedia suara realtime Google yang didukung Gemini Live API alih-alih TTS batch.

Untuk menggunakan Google sebagai penyedia TTS default:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS menggunakan prompting bahasa alami untuk kontrol gaya. Tetapkan `audioProfile` untuk menambahkan prompt gaya yang dapat digunakan ulang sebelum teks yang diucapkan. Tetapkan `speakerName` saat teks prompt Anda merujuk ke pembicara bernama.

Gemini API TTS juga menerima tag audio ekspresif dalam tanda kurung siku di teks, seperti `[whispers]` atau `[laughs]`. Untuk menjaga tag tidak muncul dalam balasan chat yang terlihat sambil tetap mengirimkannya ke TTS, letakkan di dalam blok `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Suara realtime

Plugin `google` bawaan mendaftarkan penyedia suara realtime yang didukung oleh Gemini Live API untuk jembatan audio backend seperti Voice Call dan Google Meet.

Pengaturan | Jalur konfigurasi | Default  
---|---|---  
Model | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Suara | `...google.voice` | `Kore`  
Suhu | `...google.temperature` | (belum diatur)  
Sensitivitas awal VAD | `...google.startSensitivity` | (belum diatur)  
Sensitivitas akhir VAD | `...google.endSensitivity` | (belum diatur)  
Durasi hening | `...google.silenceDurationMs` | (belum diatur)  
Penanganan aktivitas | `...google.activityHandling` | Default Google, `start-of-activity-interrupts`  
Cakupan giliran | `...google.turnCoverage` | Default Google, `only-activity`  
Nonaktifkan VAD otomatis | `...google.automaticActivityDetectionDisabled` | `false`  
Pelanjutan sesi | `...google.sessionResumption` | `true`  
Kompresi konteks | `...google.contextWindowCompression` | `true`  
Kunci API | `...google.apiKey` | Beralih ke `models.providers.google.apiKey`, `GEMINI_API_KEY`, atau `GOOGLE_API_KEY`  
  
Contoh konfigurasi realtime Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Untuk verifikasi live maintainer, jalankan `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Smoke ini juga mencakup jalur backend/WebRTC OpenAI; bagian Google membuat bentuk token Live API terbatas yang sama seperti yang digunakan oleh Control UI Talk, membuka endpoint WebSocket browser, mengirim payload penyiapan awal, dan menunggu `setupComplete`.

## Konfigurasi lanjutan

Penggunaan ulang cache Gemini langsung

Untuk eksekusi Gemini API langsung (`api: "google-generative-ai"`), OpenClaw meneruskan handle `cachedContent` yang dikonfigurasi ke permintaan Gemini.

  * Konfigurasikan parameter per model atau global dengan `cachedContent` atau `cached_content` lama
  * Jika keduanya ada, `cachedContent` yang berlaku
  * Nilai contoh: `cachedContents/prebuilt-context`
  * Penggunaan cache-hit Gemini dinormalisasi ke OpenClaw `cacheRead` dari upstream `cachedContentTokenCount`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Catatan penggunaan JSON Gemini CLI

Saat menggunakan penyedia OAuth `google-gemini-cli`, OpenClaw menormalisasi keluaran JSON CLI sebagai berikut:

  * Teks balasan berasal dari kolom CLI JSON `response`.
  * Penggunaan beralih ke `stats` saat CLI membiarkan `usage` kosong.
  * `stats.cached` dinormalisasi ke OpenClaw `cacheRead`.
  * Jika `stats.input` tidak ada, OpenClaw memperoleh token input dari `stats.input_tokens - stats.cached`.

Penyiapan lingkungan dan daemon

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `GEMINI_API_KEY` tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

## Terkait

[**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pembuatan gambar** Parameter alat gambar bersama dan pemilihan penyedia. ](</id/tools/image-generation>) [**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Pembuatan musik** Parameter alat musik bersama dan pemilihan penyedia. ](</id/tools/music-generation>)

Was this useful?YesNo