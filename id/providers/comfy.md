---
title: ComfyUI
source_url: https://docs.openclaw.ai/id/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw mengirim Plugin `comfy` bawaan untuk run ComfyUI berbasis alur kerja. Plugin ini sepenuhnya berbasis alur kerja, jadi OpenClaw tidak mencoba memetakan `size`, `aspectRatio`, `resolution`, `durationSeconds`, atau kontrol bergaya TTS generik ke graph Anda.

Properti | Detail  
---|---  
Provider | `comfy`  
Model | `comfy/workflow`  
Permukaan bersama | `image_generate`, `video_generate`, `music_generate`  
Auth | Tidak ada untuk ComfyUI lokal; `COMFY_API_KEY` atau `COMFY_CLOUD_API_KEY` untuk Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` dan Comfy Cloud `/api/*`  
  
## Yang didukung

  * Pembuatan gambar dari JSON alur kerja
  * Pengeditan gambar dengan 1 gambar referensi yang diunggah
  * Pembuatan video dari JSON alur kerja
  * Pembuatan video dengan 1 gambar referensi yang diunggah
  * Pembuatan musik atau audio melalui tool `music_generate` bersama
  * Pengunduhan output dari node yang dikonfigurasi atau semua node output yang cocok


## Memulai

Pilih antara menjalankan ComfyUI di mesin Anda sendiri atau menggunakan Comfy Cloud.

### Lokal

**Terbaik untuk:** menjalankan instance ComfyUI Anda sendiri di mesin atau LAN Anda.

* ### Mulai ComfyUI secara lokal

Pastikan instance ComfyUI lokal Anda berjalan (default ke `http://127.0.0.1:8188`).

* ### Siapkan JSON alur kerja Anda

Ekspor atau buat file JSON alur kerja ComfyUI. Catat ID node untuk node input prompt dan node output yang ingin dibaca OpenClaw.

* ### Konfigurasikan provider

Atur `mode: "local"` dan arahkan ke file alur kerja Anda. Berikut contoh gambar minimal:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Atur model default

Arahkan OpenClaw ke model `comfy/workflow` untuk capability yang Anda konfigurasi:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifikasi

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Terbaik untuk:** menjalankan alur kerja di Comfy Cloud tanpa mengelola resource GPU lokal.

* ### Dapatkan API key

Daftar di [comfy.org](<https://comfy.org>) dan buat API key dari dashboard akun Anda.

* ### Atur API key

Berikan key Anda melalui salah satu metode berikut:

bashCopy code
[code]
    # Environment variable (disarankan)export COMFY_API_KEY="your-key" # Environment variable alternatifexport COMFY_CLOUD_API_KEY="your-key" # Atau inline di configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Siapkan JSON alur kerja Anda

Ekspor atau buat file JSON alur kerja ComfyUI. Catat ID node untuk node input prompt dan node output.

* ### Konfigurasikan provider

Atur `mode: "cloud"` dan arahkan ke file alur kerja Anda:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Atur model default

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifikasi

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Konfigurasi

Comfy mendukung pengaturan koneksi tingkat atas bersama plus bagian alur kerja per-capability (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Kunci bersama

Kunci | Tipe | Deskripsi  
---|---|---  
`mode` | `"local"` atau `"cloud"` | Mode koneksi.  
`baseUrl` | string | Default ke `http://127.0.0.1:8188` untuk lokal atau `https://cloud.comfy.org` untuk cloud.  
`apiKey` | string | Key inline opsional, alternatif dari env var `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Izinkan `baseUrl` private/LAN dalam mode cloud.  
  
### Kunci per-capability

Kunci ini berlaku di dalam bagian `image`, `video`, atau `music`:

Kunci | Wajib | Default | Deskripsi  
---|---|---|---  
`workflow` atau `workflowPath` | Ya | \-- | Path ke file JSON alur kerja ComfyUI.  
`promptNodeId` | Ya | \-- | ID node yang menerima prompt teks.  
`promptInputName` | Tidak | `"text"` | Nama input pada node prompt.  
`outputNodeId` | Tidak | \-- | ID node untuk membaca output. Jika dihilangkan, semua node output yang cocok digunakan.  
`pollIntervalMs` | Tidak | \-- | Interval polling dalam milidetik untuk penyelesaian pekerjaan.  
`timeoutMs` | Tidak | \-- | Timeout dalam milidetik untuk run alur kerja.  
  
Bagian `image` dan `video` juga mendukung:

Kunci | Wajib | Default | Deskripsi  
---|---|---|---  
`inputImageNodeId` | Ya (saat meneruskan gambar referensi) | \-- | ID node yang menerima gambar referensi yang diunggah.  
`inputImageInputName` | Tidak | `"image"` | Nama input pada node gambar.  
  
## Detail alur kerja

Alur kerja gambar

Atur model gambar default ke `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Contoh pengeditan gambar referensi:**

Untuk mengaktifkan pengeditan gambar dengan gambar referensi yang diunggah, tambahkan `inputImageNodeId` ke config gambar Anda:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Alur kerja video

Atur model video default ke `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Alur kerja video Comfy mendukung text-to-video dan image-to-video melalui graph yang dikonfigurasi.

Alur kerja musik

Plugin bawaan mendaftarkan provider pembuatan musik untuk output audio atau musik yang didefinisikan alur kerja, yang ditampilkan melalui tool `music_generate` bersama:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Gunakan bagian config `music` untuk mengarahkan ke JSON alur kerja audio dan node output Anda.

Kompatibilitas mundur

Config gambar tingkat atas yang sudah ada (tanpa bagian `image` bertingkat) tetap berfungsi:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw memperlakukan bentuk lama tersebut sebagai config alur kerja gambar. Anda tidak perlu segera bermigrasi, tetapi bagian bertingkat `image` / `video` / `music` disarankan untuk pengaturan baru.

Pengujian live

Cakupan live opt-in tersedia untuk plugin bawaan:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Pengujian live melewati kasus gambar, video, atau musik individual kecuali bagian alur kerja Comfy yang cocok telah dikonfigurasi.

## Terkait

[**Pembuatan Gambar** Konfigurasi dan penggunaan tool pembuatan gambar. ](</id/tools/image-generation>) [**Pembuatan Video** Konfigurasi dan penggunaan tool pembuatan video. ](</id/tools/video-generation>) [**Pembuatan Musik** Pengaturan tool pembuatan musik dan audio. ](</id/tools/music-generation>) [**Direktori Provider** Ikhtisar semua provider dan referensi model. ](</id/providers>) [**Referensi konfigurasi** Referensi config lengkap termasuk default agen. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo