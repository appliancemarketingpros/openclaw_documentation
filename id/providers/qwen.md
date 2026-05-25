---
title: Qwen
source_url: https://docs.openclaw.ai/id/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw sekarang memperlakukan Qwen sebagai penyedia bawaan kelas utama dengan id kanonis `qwen`. Penyedia bawaan menargetkan endpoint Qwen Cloud / Alibaba DashScope dan Coding Plan serta menjaga id lama `modelstudio` tetap berfungsi sebagai alias kompatibilitas.

  * Penyedia: `qwen`
  * Variabel env pilihan: `QWEN_API_KEY`
  * Juga diterima untuk kompatibilitas: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * Gaya API: kompatibel dengan OpenAI


## Memulai

Pilih jenis paket Anda dan ikuti langkah penyiapan.

### Coding Plan (langganan)

**Paling cocok untuk:** akses berbasis langganan melalui Qwen Coding Plan.

* ### Dapatkan kunci API Anda

Buat atau salin kunci API dari [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Jalankan onboarding

Untuk endpoint **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

Untuk endpoint **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standar (bayar sesuai pemakaian)

**Paling cocok untuk:** akses bayar sesuai pemakaian melalui endpoint Standard Model Studio, termasuk model seperti `qwen3.6-plus` yang mungkin tidak tersedia di Coding Plan.

* ### Dapatkan kunci API Anda

Buat atau salin kunci API dari [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Jalankan onboarding

Untuk endpoint **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Untuk endpoint **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## Jenis paket dan endpoint

Paket | Wilayah | Pilihan auth | Endpoint  
---|---|---|---  
Standar (bayar sesuai pemakaian) | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standar (bayar sesuai pemakaian) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (langganan) | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (langganan) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Penyedia otomatis memilih endpoint berdasarkan pilihan auth Anda. Pilihan kanonis menggunakan keluarga `qwen-*`; `modelstudio-*` tetap hanya untuk kompatibilitas. Anda dapat menimpanya dengan `baseUrl` kustom dalam konfigurasi.

## Katalog bawaan

OpenClaw saat ini mengirimkan katalog Qwen bawaan ini. Katalog yang dikonfigurasi sadar-endpoint: konfigurasi Coding Plan menghilangkan model yang hanya diketahui berfungsi pada endpoint Standar.

Ref model | Masukan | Konteks | Catatan  
---|---|---|---  
`qwen/qwen3.5-plus` | teks, gambar | 1,000,000 | Model default  
`qwen/qwen3.6-plus` | teks, gambar | 1,000,000 | Pilih endpoint Standar saat Anda membutuhkan model ini  
`qwen/qwen3-max-2026-01-23` | teks | 262,144 | Lini Qwen Max  
`qwen/qwen3-coder-next` | teks | 262,144 | Pengodean  
`qwen/qwen3-coder-plus` | teks | 1,000,000 | Pengodean  
`qwen/MiniMax-M2.5` | teks | 1,000,000 | Penalaran diaktifkan  
`qwen/glm-5` | teks | 202,752 | GLM  
`qwen/glm-4.7` | teks | 202,752 | GLM  
`qwen/kimi-k2.5` | teks, gambar | 262,144 | Moonshot AI melalui Alibaba  
  
## Kontrol Berpikir

Untuk model Qwen Cloud yang mendukung penalaran, penyedia bawaan memetakan level berpikir OpenClaw ke flag permintaan tingkat atas `enable_thinking` milik DashScope. Berpikir yang dinonaktifkan mengirim `enable_thinking: false`; level berpikir lain mengirim `enable_thinking: true`.

## Add-on multimodal

Plugin `qwen` juga mengekspos kapabilitas multimodal pada endpoint DashScope **Standar** (bukan endpoint Coding Plan):

  * **Pemahaman video** melalui `qwen-vl-max-latest`
  * **Pembuatan video Wan** melalui `wan2.6-t2v` (default), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


Untuk menggunakan Qwen sebagai penyedia video default:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Konfigurasi lanjutan

Pemahaman gambar dan video

Plugin Qwen bawaan mendaftarkan pemahaman media untuk gambar dan video pada endpoint DashScope **Standar** (bukan endpoint Coding Plan).

Properti | Nilai  
---|---  
Model | `qwen-vl-max-latest`  
Masukan yang didukung | Gambar, video  
  
Pemahaman media diselesaikan otomatis dari auth Qwen yang dikonfigurasi — tidak ada konfigurasi tambahan yang diperlukan. Pastikan Anda menggunakan endpoint Standar (bayar sesuai pemakaian) untuk dukungan pemahaman media.

Ketersediaan Qwen 3.6 Plus

`qwen3.6-plus` tersedia pada endpoint Model Studio Standar (bayar sesuai pemakaian):

  * China: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Jika endpoint Coding Plan mengembalikan kesalahan "model tidak didukung" untuk `qwen3.6-plus`, beralihlah ke Standar (bayar sesuai pemakaian), bukan pasangan endpoint/kunci Coding Plan.

Katalog Qwen bawaan OpenClaw tidak mengiklankan `qwen3.6-plus` pada endpoint Coding Plan, tetapi entri `qwen/qwen3.6-plus` yang dikonfigurasi secara eksplisit di bawah `models.providers.qwen.models` dihormati pada baseUrl Coding Plan sehingga Anda dapat memilih model tersebut jika Aliyun mengaktifkannya pada langganan Anda. API upstream tetap memutuskan apakah panggilan berhasil.

Rencana kapabilitas

Plugin `qwen` sedang diposisikan sebagai rumah vendor untuk seluruh permukaan Qwen Cloud, bukan hanya model pengodean/teks.

  * **Model teks/chat:** sudah dibundel sekarang
  * **Pemanggilan alat, keluaran terstruktur, berpikir:** diwarisi dari transport yang kompatibel dengan OpenAI
  * **Pembuatan gambar:** direncanakan di lapisan Plugin penyedia
  * **Pemahaman gambar/video:** sudah dibundel sekarang pada endpoint Standar
  * **Ucapan/audio:** direncanakan di lapisan Plugin penyedia
  * **Embedding/reranking memori:** direncanakan melalui permukaan adaptor embedding
  * **Pembuatan video:** sudah dibundel sekarang melalui kapabilitas pembuatan video bersama

Detail pembuatan video

Untuk pembuatan video, OpenClaw memetakan wilayah Qwen yang dikonfigurasi ke host AIGC DashScope yang sesuai sebelum mengirimkan pekerjaan:

  * Global/Internasional: `https://dashscope-intl.aliyuncs.com`
  * China: `https://dashscope.aliyuncs.com`


Itu berarti `models.providers.qwen.baseUrl` normal yang menunjuk ke host Qwen Coding Plan atau Standar tetap menjaga pembuatan video pada endpoint video DashScope regional yang benar.

Batas pembuatan video Qwen bawaan saat ini:

  * Hingga **1** video keluaran per permintaan
  * Hingga **1** gambar masukan
  * Hingga **4** video masukan
  * Durasi hingga **10 detik**
  * Mendukung `size`, `aspectRatio`, `resolution`, `audio`, dan `watermark`
  * Mode gambar/video referensi saat ini memerlukan **URL http(s) jarak jauh**. Jalur file lokal ditolak di awal karena endpoint video DashScope tidak menerima buffer lokal yang diunggah untuk referensi tersebut.

Kompatibilitas penggunaan streaming

Endpoint Model Studio native mengiklankan kompatibilitas penggunaan streaming pada transport bersama `openai-completions`. OpenClaw sekarang menentukannya berdasarkan kapabilitas endpoint, sehingga id penyedia kustom yang kompatibel dengan DashScope dan menargetkan host native yang sama mewarisi perilaku penggunaan streaming yang sama, alih-alih secara khusus memerlukan id penyedia bawaan `qwen`.

Kompatibilitas penggunaan streaming native berlaku untuk host Coding Plan maupun host Standar yang kompatibel dengan DashScope:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Wilayah endpoint multimodal

Permukaan multimodal (pemahaman video dan pembuatan video Wan) menggunakan endpoint DashScope **Standar** , bukan endpoint Coding Plan:

  * URL dasar Standar Global/Internasional: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * URL dasar Standar China: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Penyiapan lingkungan dan daemon

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `QWEN_API_KEY` tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

## Terkait

[**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Alibaba (ModelStudio)** Penyedia ModelStudio lama dan catatan migrasi. ](</id/providers/alibaba>) [**Pemecahan masalah** Pemecahan masalah umum dan FAQ. ](</id/help/troubleshooting>)

Was this useful?YesNo