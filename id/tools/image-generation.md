---
title: Pembuatan gambar
source_url: https://docs.openclaw.ai/id/tools/image-generation
scraped_at: 2026-05-25
---

Alat `image_generate` memungkinkan agen membuat dan mengedit gambar menggunakan penyedia yang Anda konfigurasikan. Gambar yang dibuat dikirim otomatis sebagai lampiran media dalam balasan agen.

## Mulai cepat

* ### Konfigurasikan autentikasi

Tetapkan kunci API untuk setidaknya satu penyedia (misalnya `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) atau masuk dengan OpenAI Codex OAuth.

* ### Pilih model default (opsional)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth menggunakan referensi model `openai/gpt-image-2` yang sama. Ketika profil OAuth `openai-codex` dikonfigurasi, OpenClaw merutekan permintaan gambar melalui profil OAuth tersebut, alih-alih mencoba `OPENAI_API_KEY` terlebih dahulu. Konfigurasi `models.providers.openai` eksplisit (kunci API, URL dasar kustom/Azure) memilih kembali rute OpenAI Images API langsung.

* ### Minta agen

_"Buat gambar maskot robot yang ramah."_

Agen memanggil `image_generate` secara otomatis. Tidak perlu allow-list alat - ini diaktifkan secara default ketika penyedia tersedia.

## Rute umum

Tujuan | Referensi model | Autentikasi  
---|---|---  
Pembuatan gambar OpenAI dengan penagihan API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
Pembuatan gambar OpenAI dengan autentikasi langganan Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
PNG/WebP latar belakang transparan OpenAI | `openai/gpt-image-1.5` | `OPENAI_API_KEY` atau OpenAI Codex OAuth  
Pembuatan gambar DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
Pembuatan gambar OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
Pembuatan gambar LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Pembuatan gambar Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` atau `GOOGLE_API_KEY`  
  
Alat `image_generate` yang sama menangani teks-ke-gambar dan pengeditan gambar referensi. Gunakan `image` untuk satu referensi atau `images` untuk beberapa referensi. Petunjuk keluaran yang didukung penyedia seperti `quality`, `outputFormat`, dan `background` diteruskan ketika tersedia dan dilaporkan sebagai diabaikan ketika penyedia tidak mendukungnya. Dukungan latar belakang transparan bawaan bersifat khusus OpenAI; penyedia lain mungkin tetap mempertahankan alfa PNG jika backend mereka memancarkannya.

## Penyedia yang didukung

Penyedia | Model default | Dukungan edit | Autentikasi  
---|---|---|---  
ComfyUI | `workflow` | Ya (1 gambar, dikonfigurasi alur kerja) | `COMFY_API_KEY` atau `COMFY_CLOUD_API_KEY` untuk cloud  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Ya (1 gambar) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Ya (batas khusus model) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Ya | `GEMINI_API_KEY` atau `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Ya (hingga 5 gambar input) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Ya (referensi subjek) | `MINIMAX_API_KEY` atau MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Ya (hingga 4 gambar) | `OPENAI_API_KEY` atau OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Ya (hingga 5 gambar input) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | Tidak | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Ya (hingga 5 gambar) | `XAI_API_KEY`  
  
Gunakan `action: "list"` untuk memeriksa penyedia dan model yang tersedia saat runtime:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Kemampuan penyedia

Kemampuan | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Buat (jumlah maks) | Ditentukan alur kerja | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Edit / referensi | 1 gambar (alur kerja) | 1 gambar | Flux: 1; GPT: 10; NB2: 14 | Hingga 5 gambar | 1 gambar (ref subjek) | Hingga 5 gambar | - | Hingga 5 gambar  
Kontrol ukuran | - | ✓ | ✓ | ✓ | - | Hingga 4K | - | -  
Rasio aspek | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Resolusi (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Parameter alat

Prompt pembuatan gambar. Wajib untuk `action: "generate"`.

Gunakan `"list"` untuk memeriksa penyedia dan model yang tersedia saat runtime.

Override penyedia/model (mis. `openai/gpt-image-2`). Gunakan `openai/gpt-image-1.5` untuk latar belakang OpenAI transparan.

Path atau URL gambar referensi tunggal untuk mode edit.

Beberapa gambar referensi untuk mode edit (hingga 5 pada penyedia yang mendukung).

Petunjuk ukuran: `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Rasio aspek: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Petunjuk kualitas ketika penyedia mendukungnya.

Petunjuk format keluaran ketika penyedia mendukungnya.

Petunjuk latar belakang ketika penyedia mendukungnya. Gunakan `transparent` dengan `outputFormat: "png"` atau `"webp"` untuk penyedia yang mampu transparansi.

Timeout permintaan penyedia opsional dalam milidetik. Ketika Codex memanggil `image_generate` melalui alat dinamis, nilai per panggilan ini tetap menggantikan default yang dikonfigurasi dan dibatasi pada 600000 md.

Petunjuk khusus OpenAI: `background`, `moderation`, `outputCompression`, dan `user`.

## Konfigurasi

### Pemilihan model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Urutan pemilihan penyedia

OpenClaw mencoba penyedia dalam urutan ini:

  1. Parameter **`model`** dari panggilan alat (jika agen menentukannya).
  2. **`imageGenerationModel.primary`** dari konfigurasi.
  3. **`imageGenerationModel.fallbacks`** secara berurutan.
  4. **Deteksi otomatis** \- hanya default penyedia yang didukung autentikasi: 
     * penyedia default saat ini terlebih dahulu;
     * penyedia pembuatan gambar terdaftar lainnya dalam urutan id penyedia.


Jika penyedia gagal (kesalahan autentikasi, batas laju, dll.), kandidat terkonfigurasi berikutnya dicoba secara otomatis. Jika semua gagal, kesalahan menyertakan detail dari setiap percobaan.

Override model per panggilan bersifat tepat

Override `model` per panggilan hanya mencoba penyedia/model tersebut dan tidak melanjutkan ke primary/fallback yang dikonfigurasi atau penyedia yang terdeteksi otomatis.

Deteksi otomatis sadar autentikasi

Default penyedia hanya masuk ke daftar kandidat ketika OpenClaw benar-benar dapat mengautentikasi penyedia tersebut. Tetapkan `agents.defaults.mediaGenerationAutoProviderFallback: false` untuk hanya menggunakan entri `model`, `primary`, dan `fallbacks` eksplisit.

Timeout

Tetapkan `agents.defaults.imageGenerationModel.timeoutMs` untuk backend gambar yang lambat. Parameter alat `timeoutMs` per panggilan menggantikan default yang dikonfigurasi. Panggilan alat dinamis Codex menghormati anggaran timeout yang sama, dibatasi oleh maksimum bridge alat dinamis OpenClaw sebesar 600000 md.

Periksa saat runtime

Gunakan `action: "list"` untuk memeriksa penyedia yang saat ini terdaftar, model default mereka, dan petunjuk env-var autentikasi.

### Pengeditan gambar

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI, dan xAI mendukung pengeditan gambar referensi. Berikan path atau URL gambar referensi:

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google, dan xAI mendukung hingga 5 gambar referensi melalui parameter `images`. fal mendukung 1 gambar referensi untuk Flux image-to-image, hingga 10 untuk edit GPT Image 2, dan hingga 14 untuk edit Nano Banana 2. MiniMax dan ComfyUI mendukung 1.

## Pembahasan mendalam penyedia

OpenAI gpt-image-2 (dan gpt-image-1.5)

Pembuatan gambar OpenAI secara default menggunakan `openai/gpt-image-2`. Jika profil OAuth `openai-codex` dikonfigurasi, OpenClaw menggunakan ulang profil OAuth yang sama dengan yang digunakan oleh model chat langganan Codex dan mengirim permintaan gambar melalui backend Codex Responses. URL dasar Codex lama seperti `https://chatgpt.com/backend-api` dikanonisasi menjadi `https://chatgpt.com/backend-api/codex` untuk permintaan gambar. OpenClaw **tidak** diam-diam beralih ke `OPENAI_API_KEY` untuk permintaan tersebut - untuk memaksa perutean langsung OpenAI Images API, konfigurasikan `models.providers.openai` secara eksplisit dengan kunci API, URL dasar kustom, atau endpoint Azure.

Model `openai/gpt-image-1.5`, `openai/gpt-image-1`, dan `openai/gpt-image-1-mini` masih dapat dipilih secara eksplisit. Gunakan `gpt-image-1.5` untuk output PNG/WebP dengan latar belakang transparan; API `gpt-image-2` saat ini menolak `background: "transparent"`.

`gpt-image-2` mendukung pembuatan text-to-image dan pengeditan gambar referensi melalui alat `image_generate` yang sama. OpenClaw meneruskan `prompt`, `count`, `size`, `quality`, `outputFormat`, dan gambar referensi ke OpenAI. OpenAI **tidak** menerima `aspectRatio` atau `resolution` secara langsung; jika memungkinkan OpenClaw memetakan keduanya ke `size` yang didukung, jika tidak alat melaporkannya sebagai override yang diabaikan.

Opsi khusus OpenAI berada di bawah objek `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` menerima `transparent`, `opaque`, atau `auto`; output transparan memerlukan `outputFormat` `png` atau `webp` dan model gambar OpenAI yang mendukung transparansi. OpenClaw merutekan permintaan latar belakang transparan default `gpt-image-2` ke `gpt-image-1.5`. `openai.outputCompression` berlaku untuk output JPEG/WebP.

Petunjuk `background` tingkat atas bersifat netral penyedia dan saat ini dipetakan ke bidang permintaan `background` OpenAI yang sama ketika penyedia OpenAI dipilih. Penyedia yang tidak mendeklarasikan dukungan latar belakang mengembalikannya di `ignoredOverrides`, alih-alih menerima parameter yang tidak didukung.

Untuk merutekan pembuatan gambar OpenAI melalui deployment Azure OpenAI alih-alih `api.openai.com`, lihat [endpoint Azure OpenAI](</id/providers/openai#azure-openai-endpoints>).

Model gambar OpenRouter

Pembuatan gambar OpenRouter menggunakan `OPENROUTER_API_KEY` yang sama dan dirutekan melalui API gambar chat completions OpenRouter. Pilih model gambar OpenRouter dengan prefiks `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw meneruskan `prompt`, `count`, gambar referensi, serta petunjuk `aspectRatio` / `resolution` yang kompatibel dengan Gemini ke OpenRouter. Pintasan model gambar OpenRouter bawaan saat ini mencakup `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview`, dan `openai/gpt-5.4-image-2`. Gunakan `action: "list"` untuk melihat apa yang diekspos Plugin terkonfigurasi Anda.

Autentikasi ganda MiniMax

Pembuatan gambar MiniMax tersedia melalui kedua jalur autentikasi MiniMax bawaan:

  * `minimax/image-01` untuk penyiapan kunci API
  * `minimax-portal/image-01` untuk penyiapan OAuth

xAI grok-imagine-image

Penyedia xAI bawaan menggunakan `/v1/images/generations` untuk permintaan yang hanya berisi prompt dan `/v1/images/edits` ketika `image` atau `images` ada.

  * Model: `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Jumlah: hingga 4
  * Referensi: satu `image` atau hingga lima `images`
  * Rasio aspek: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Resolusi: `1K`, `2K`
  * Output: dikembalikan sebagai lampiran gambar yang dikelola OpenClaw


OpenClaw sengaja tidak mengekspos `quality`, `mask`, `user`, atau rasio aspek tambahan yang hanya native xAI hingga kontrol tersebut tersedia dalam kontrak `image_generate` lintas penyedia bersama.

## Contoh

### Buat (lanskap 4K)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Buat (PNG transparan)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

CLI ekuivalen:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Buat (dua persegi)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (satu referensi)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (beberapa referensi)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Flag `--output-format` dan `--background` yang sama tersedia pada `openclaw infer image edit`; `--openai-background` tetap menjadi alias khusus OpenAI. Penyedia bawaan selain OpenAI saat ini tidak mendeklarasikan kontrol latar belakang eksplisit, sehingga `background: "transparent"` dilaporkan sebagai diabaikan untuk mereka.

## Terkait

  * [Ikhtisar alat](</id/tools>) \- semua alat agen yang tersedia
  * [ComfyUI](</id/providers/comfy>) \- penyiapan alur kerja ComfyUI lokal dan Comfy Cloud
  * [fal](</id/providers/fal>) \- penyiapan penyedia gambar dan video fal
  * [Google (Gemini)](</id/providers/google>) \- penyiapan penyedia gambar Gemini
  * [MiniMax](</id/providers/minimax>) \- penyiapan penyedia gambar MiniMax
  * [OpenAI](</id/providers/openai>) \- penyiapan penyedia OpenAI Images
  * [Vydra](</id/providers/vydra>) \- penyiapan gambar, video, dan ucapan Vydra
  * [xAI](</id/providers/xai>) \- penyiapan gambar, video, pencarian, eksekusi kode, dan TTS Grok
  * [Referensi konfigurasi](</id/gateway/config-agents#agent-defaults>) \- konfigurasi `imageGenerationModel`
  * [Model](</id/concepts/models>) \- konfigurasi model dan failover


Was this useful?YesNo