---
title: OpenRouter
source_url: https://docs.openclaw.ai/id/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter menyediakan **API terpadu** yang merutekan permintaan ke banyak model di balik satu endpoint dan kunci API. Ini kompatibel dengan OpenAI, sehingga sebagian besar SDK OpenAI berfungsi dengan mengganti URL dasar.

## Memulai

* ### Get your API key

Buat kunci API di [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Optional) Switch to a specific model

Onboarding menggunakan default `openrouter/auto`. Pilih model konkret nanti:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Contoh konfigurasi

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Referensi model

Contoh fallback bawaan:

Ref model | Catatan  
---|---  
`openrouter/auto` | Perutean otomatis OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 via MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 via MoonshotAI  
  
## Pembuatan gambar

OpenRouter juga dapat mendukung alat `image_generate`. Gunakan model gambar OpenRouter di bawah `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw mengirim permintaan gambar ke API gambar chat completions OpenRouter dengan `modalities: ["image", "text"]`. Model gambar Gemini menerima petunjuk `aspectRatio` dan `resolution` yang didukung melalui `image_config` OpenRouter. Gunakan `agents.defaults.imageGenerationModel.timeoutMs` untuk model gambar OpenRouter yang lebih lambat; parameter `timeoutMs` per panggilan milik alat `image_generate` tetap diutamakan.

## Pembuatan video

OpenRouter juga dapat mendukung alat `video_generate` melalui API asinkron `/videos` miliknya. Gunakan model video OpenRouter di bawah `agents.defaults.videoGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw mengirim tugas teks-ke-video dan gambar-ke-video ke OpenRouter, melakukan polling pada `polling_url` yang dikembalikan, dan mengunduh video yang selesai dari `unsigned_urls` OpenRouter atau endpoint konten tugas yang terdokumentasi. Gambar referensi dikirim sebagai gambar bingkai pertama/terakhir secara default; gambar yang ditandai dengan `reference_image` dikirim sebagai referensi input OpenRouter. Default bawaan `google/veo-3.1-fast` mengiklankan durasi 4/6/8 detik yang saat ini didukung, resolusi `720P`/`1080P`, dan rasio aspek `16:9`/`9:16`. Video-ke-video tidak didaftarkan untuk OpenRouter karena API pembuatan video upstream saat ini menerima teks dan referensi gambar.

## Teks-ke-ucapan

OpenRouter juga dapat digunakan sebagai penyedia TTS melalui endpoint `/audio/speech` yang kompatibel dengan OpenAI.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Jika `messages.tts.providers.openrouter.apiKey` dihilangkan, TTS menggunakan kembali `models.providers.openrouter.apiKey`, lalu `OPENROUTER_API_KEY`.

## Ucapan-ke-teks (audio masuk)

OpenRouter dapat mentranskripsikan lampiran suara/audio masuk melalui jalur bersama `tools.media.audio` menggunakan endpoint STT miliknya (`/audio/transcriptions`). Ini berlaku untuk Plugin kanal apa pun yang meneruskan suara/audio masuk ke pra-pemeriksaan pemahaman media.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw mengirim permintaan STT OpenRouter sebagai JSON dengan audio base64 di bawah `input_audio` (kontrak STT OpenRouter), bukan sebagai unggahan formulir multipart OpenAI.

## Autentikasi dan header

OpenRouter menggunakan token Bearer dengan kunci API Anda di balik layar.

Pada permintaan OpenRouter sungguhan (`https://openrouter.ai/api/v1`), OpenClaw juga menambahkan header atribusi aplikasi yang terdokumentasi oleh OpenRouter:

Header | Nilai  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Konfigurasi lanjutan

Response caching

Caching respons OpenRouter bersifat opt-in. Aktifkan per model OpenRouter dengan parameter model:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw mengirim `X-OpenRouter-Cache: true` dan, saat dikonfigurasi, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` memaksa penyegaran untuk permintaan saat ini dan menyimpan respons pengganti. Alias snake_case (`response_cache`, `response_cache_ttl_seconds`, dan `response_cache_clear`) juga diterima.

Ini terpisah dari caching prompt penyedia dan dari penanda `cache_control` Anthropic milik OpenRouter. Ini hanya diterapkan pada rute `openrouter.ai` terverifikasi, bukan URL dasar proksi kustom.

Anthropic cache markers

Pada rute OpenRouter terverifikasi, ref model Anthropic mempertahankan penanda `cache_control` Anthropic khusus OpenRouter yang digunakan OpenClaw untuk penggunaan ulang cache prompt yang lebih baik pada blok prompt sistem/pengembang.

Anthropic reasoning prefill

Pada rute OpenRouter terverifikasi, ref model Anthropic dengan reasoning diaktifkan menghapus giliran prefill asisten di akhir sebelum permintaan mencapai OpenRouter, sesuai dengan persyaratan Anthropic bahwa percakapan reasoning berakhir dengan giliran pengguna.

Thinking / reasoning injection

Pada rute non-`auto` yang didukung, OpenClaw memetakan level thinking yang dipilih ke payload reasoning proksi OpenRouter. Petunjuk model yang tidak didukung dan `openrouter/auto` melewati injeksi reasoning tersebut. Hunter Alpha juga melewati reasoning proksi untuk ref model terkonfigurasi yang kedaluwarsa karena OpenRouter dapat mengembalikan teks jawaban akhir dalam kolom reasoning untuk rute yang telah dihentikan tersebut.

DeepSeek V4 reasoning replay

Pada rute OpenRouter terverifikasi, `openrouter/deepseek/deepseek-v4-flash` dan `openrouter/deepseek/deepseek-v4-pro` mengisi `reasoning_content` yang hilang pada giliran asisten yang diputar ulang agar percakapan thinking/alat mempertahankan bentuk tindak lanjut yang diperlukan DeepSeek V4. OpenClaw mengirim nilai `reasoning_effort` yang didukung OpenRouter untuk rute ini; `xhigh` adalah level tertinggi yang diiklankan, dan override `max` yang kedaluwarsa dipetakan ke `xhigh`.

OpenAI-only request shaping

OpenRouter tetap berjalan melalui jalur kompatibel OpenAI bergaya proksi, sehingga pembentukan permintaan khusus OpenAI native seperti `serviceTier`, Responses `store`, payload kompatibilitas reasoning OpenAI, dan petunjuk cache prompt tidak diteruskan.

Gemini-backed routes

Ref OpenRouter yang didukung Gemini tetap berada di jalur proksi-Gemini: OpenClaw mempertahankan sanitasi tanda tangan pemikiran Gemini di sana, tetapi tidak mengaktifkan validasi replay Gemini native atau penulisan ulang bootstrap.

Provider routing metadata

Jika Anda meneruskan perutean penyedia OpenRouter di bawah parameter model, OpenClaw meneruskannya sebagai metadata perutean OpenRouter sebelum wrapper stream bersama berjalan.

## Terkait

[**Model selection** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Configuration reference** Referensi konfigurasi lengkap untuk agent, model, dan penyedia. ](</id/gateway/configuration-reference>)

Was this useful?YesNo