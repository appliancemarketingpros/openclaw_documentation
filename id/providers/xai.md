---
title: xAI
source_url: https://docs.openclaw.ai/id/providers/xai
scraped_at: 2026-05-25
---

OpenClaw mengirimkan Plugin penyedia `xai` bawaan untuk model Grok.

## Memulai

* ### Create an API key

Buat kunci API di [konsol xAI](<https://console.x.ai/>).

* ### Set your API key

Tetapkan `XAI_API_KEY`, atau jalankan:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### Pick a model

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## Katalog bawaan

OpenClaw menyertakan keluarga model xAI berikut secara langsung:

Keluarga | ID model  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Plugin ini juga meneruskan resolusi ID `grok-4*` dan `grok-code-fast*` yang lebih baru saat ID tersebut mengikuti bentuk API yang sama.

## Cakupan fitur OpenClaw

Plugin bawaan memetakan permukaan API publik xAI saat ini ke kontrak penyedia dan alat bersama OpenClaw. Kapabilitas yang tidak sesuai dengan kontrak bersama (misalnya TTS streaming dan suara realtime) tidak diekspos - lihat tabel di bawah.

Kapabilitas xAI | Permukaan OpenClaw | Status  
---|---|---  
Chat / Responses | Penyedia model `xai/<model>` | Ya  
Pencarian web sisi server | Penyedia `web_search` `grok` | Ya  
Pencarian X sisi server | Alat `x_search` | Ya  
Eksekusi kode sisi server | Alat `code_execution` | Ya  
Gambar | `image_generate` | Ya  
Video | `video_generate` | Ya  
Text-to-speech batch | `messages.tts.provider: "xai"` / `tts` | Ya  
TTS streaming | - | Tidak diekspos; kontrak TTS OpenClaw mengembalikan buffer audio lengkap  
Speech-to-text batch | `tools.media.audio` / pemahaman media | Ya  
Speech-to-text streaming | Voice Call `streaming.provider: "xai"` | Ya  
Suara realtime | - | Belum diekspos; kontrak sesi/WebSocket berbeda  
File / batch | Hanya kompatibilitas API model generik | Bukan alat OpenClaw kelas utama  
  
### Pemetaan mode cepat

`/fast on` atau `agents.defaults.models["xai/<model>"].params.fastMode: true` menulis ulang permintaan xAI native sebagai berikut:

Model sumber | Target mode cepat  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Alias kompatibilitas lama

Alias lama masih dinormalisasi ke ID bawaan kanonis:

Alias lama | ID kanonis  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Fitur

Web search

Penyedia pencarian web `grok` bawaan dapat menggunakan `XAI_API_KEY` atau kunci pencarian web Plugin:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

Video generation

Plugin `xai` bawaan mendaftarkan pembuatan video melalui alat bersama `video_generate`.

  * Model video default: `xai/grok-imagine-video`
  * Mode: text-to-video, image-to-video, pembuatan gambar referensi, edit video jarak jauh, dan ekstensi video jarak jauh
  * Rasio aspek: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Resolusi: `480P`, `720P`
  * Durasi: 1-15 detik untuk pembuatan/image-to-video, 1-10 detik saat menggunakan peran `reference_image`, 2-10 detik untuk ekstensi
  * Pembuatan gambar referensi: tetapkan `imageRoles` ke `reference_image` untuk setiap gambar yang disediakan; xAI menerima hingga 7 gambar seperti itu


Untuk menggunakan xAI sebagai penyedia video default:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Image generation

Plugin `xai` bawaan mendaftarkan pembuatan gambar melalui alat bersama `image_generate`.

  * Model gambar default: `xai/grok-imagine-image`
  * Model tambahan: `xai/grok-imagine-image-pro`
  * Mode: text-to-image dan edit gambar referensi
  * Input referensi: satu `image` atau hingga lima `images`
  * Rasio aspek: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Resolusi: `1K`, `2K`
  * Jumlah: hingga 4 gambar


OpenClaw meminta respons gambar `b64_json` dari xAI agar media yang dibuat dapat disimpan dan dikirim melalui jalur lampiran kanal normal. Gambar referensi lokal dikonversi menjadi URL data; referensi `http(s)` jarak jauh diteruskan apa adanya.

Untuk menggunakan xAI sebagai penyedia gambar default:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

Text-to-speech

Plugin `xai` bawaan mendaftarkan text-to-speech melalui permukaan penyedia `tts` bersama.

  * Suara: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * Suara default: `eve`
  * Format: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * Bahasa: kode BCP-47 atau `auto`
  * Kecepatan: override kecepatan native penyedia
  * Format catatan suara Opus native tidak didukung


Untuk menggunakan xAI sebagai penyedia TTS default:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

Speech-to-text

Plugin `xai` bawaan mendaftarkan speech-to-text batch melalui permukaan transkripsi pemahaman media OpenClaw.

  * Model default: `grok-stt`
  * Endpoint: xAI REST `/v1/stt`
  * Jalur input: unggahan file audio multipart
  * Didukung oleh OpenClaw di mana pun transkripsi audio masuk menggunakan `tools.media.audio`, termasuk segmen kanal suara Discord dan lampiran audio kanal


Untuk memaksa xAI bagi transkripsi audio masuk:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

Bahasa dapat disediakan melalui konfigurasi media audio bersama atau permintaan transkripsi per panggilan. Petunjuk prompt diterima oleh permukaan OpenClaw bersama, tetapi integrasi STT REST xAI hanya meneruskan file, model, dan bahasa karena ketiganya dipetakan dengan jelas ke endpoint xAI publik saat ini.

Streaming speech-to-text

Plugin `xai` bawaan juga mendaftarkan penyedia transkripsi realtime untuk audio panggilan suara langsung.

  * Endpoint: xAI WebSocket `wss://api.x.ai/v1/stt`
  * Encoding default: `mulaw`
  * Laju sampel default: `8000`
  * Endpointing default: `800ms`
  * Transkrip sementara: diaktifkan secara default


Stream media Twilio Voice Call mengirim frame audio G.711 µ-law, sehingga penyedia xAI dapat meneruskan frame tersebut secara langsung tanpa transcoding:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

Konfigurasi milik penyedia berada di bawah `plugins.entries.voice-call.config.streaming.providers.xai`. Kunci yang didukung adalah `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw`, atau `alaw`), `interimResults`, `endpointingMs`, dan `language`.

Konfigurasi x_search

Plugin xAI bawaan mengekspos `x_search` sebagai alat OpenClaw untuk mencari konten X (sebelumnya Twitter) melalui Grok.

Jalur config: `plugins.entries.xai.config.xSearch`

Kunci | Tipe | Bawaan | Deskripsi  
---|---|---|---  
`enabled` | boolean | - | Aktifkan atau nonaktifkan x_search  
`model` | string | `grok-4-1-fast` | Model yang digunakan untuk permintaan x_search  
`baseUrl` | string | - | Override URL dasar xAI Responses  
`inlineCitations` | boolean | - | Sertakan sitasi inline dalam hasil  
`maxTurns` | number | - | Jumlah giliran percakapan maksimum  
`timeoutSeconds` | number | - | Timeout permintaan dalam detik  
`cacheTtlMinutes` | number | - | Masa hidup cache dalam menit  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

Konfigurasi eksekusi kode

Plugin xAI bawaan mengekspos `code_execution` sebagai alat OpenClaw untuk eksekusi kode jarak jauh di lingkungan sandbox xAI.

Jalur config: `plugins.entries.xai.config.codeExecution`

Kunci | Tipe | Bawaan | Deskripsi  
---|---|---|---  
`enabled` | boolean | `true` (jika kunci tersedia) | Aktifkan atau nonaktifkan eksekusi kode  
`model` | string | `grok-4-1-fast` | Model yang digunakan untuk permintaan eksekusi kode  
`maxTurns` | number | - | Jumlah giliran percakapan maksimum  
`timeoutSeconds` | number | - | Timeout permintaan dalam detik  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

Batasan yang diketahui

  * Auth saat ini hanya berbasis API key. API key dapat disimpan dalam profil auth xAI, variabel lingkungan, atau config Plugin; belum ada alur OAuth xAI atau kode perangkat di OpenClaw.
  * `grok-4.20-multi-agent-experimental-beta-0304` tidak didukung pada jalur penyedia xAI normal karena memerlukan permukaan API upstream yang berbeda dari transport xAI OpenClaw standar.
  * Suara Realtime xAI belum terdaftar sebagai penyedia OpenClaw. Ini memerlukan kontrak sesi suara bidirectional yang berbeda dari STT batch atau transkripsi streaming.
  * `quality` gambar xAI, `mask` gambar, dan rasio aspek tambahan yang hanya native tidak diekspos sampai alat bersama `image_generate` memiliki kontrol lintas-penyedia yang sesuai.

Catatan lanjutan

  * OpenClaw menerapkan perbaikan kompatibilitas tool-schema dan tool-call khusus xAI secara otomatis pada jalur runner bersama.
  * Permintaan xAI native menetapkan `tool_stream: true` secara default. Atur `agents.defaults.models["xai/<model>"].params.tool_stream` ke `false` untuk menonaktifkannya.
  * Wrapper xAI bawaan menghapus flag tool-schema strict yang tidak didukung dan kunci payload reasoning sebelum mengirim permintaan xAI native.
  * `web_search`, `x_search`, dan `code_execution` diekspos sebagai alat OpenClaw. OpenClaw mengaktifkan built-in xAI spesifik yang dibutuhkan di dalam setiap permintaan alat, alih-alih melampirkan semua alat native ke setiap giliran chat.
  * Grok `web_search` membaca `plugins.entries.xai.config.webSearch.baseUrl`. `x_search` membaca `plugins.entries.xai.config.xSearch.baseUrl`, lalu fallback ke URL dasar web-search Grok.
  * `x_search` dan `code_execution` dimiliki oleh Plugin xAI bawaan, bukan di-hardcode ke runtime model inti.
  * `code_execution` adalah eksekusi sandbox xAI jarak jauh, bukan [`exec`](</id/tools/exec>) lokal.


## Pengujian live

Jalur media xAI dicakup oleh pengujian unit dan suite live opt-in. Perintah live memuat secret dari shell login Anda, termasuk `~/.profile`, sebelum memeriksa `XAI_API_KEY`.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

File live khusus penyedia menyintesis TTS normal, TTS PCM yang ramah telepon, mentranskripsi audio melalui STT batch xAI, melakukan streaming PCM yang sama melalui STT realtime xAI, menghasilkan output text-to-image, dan mengedit gambar referensi. File live gambar bersama memverifikasi penyedia xAI yang sama melalui pemilihan runtime, fallback, normalisasi, dan jalur lampiran media OpenClaw.

## Terkait

[**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Semua penyedia** Gambaran umum penyedia yang lebih luas. ](</id/providers>) [**Pemecahan masalah** Masalah umum dan perbaikannya. ](</id/help/troubleshooting>)

Was this useful?YesNo