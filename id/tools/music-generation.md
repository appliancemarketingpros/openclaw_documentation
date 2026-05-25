---
title: Pembuatan musik
source_url: https://docs.openclaw.ai/id/tools/music-generation
scraped_at: 2026-05-25
---

Alat `music_generate` memungkinkan agen membuat musik atau audio melalui kapabilitas pembuatan musik bersama dengan penyedia yang dikonfigurasi — Google, MiniMax, dan ComfyUI yang dikonfigurasi alur kerja saat ini.

Untuk eksekusi agen berbasis sesi, OpenClaw memulai pembuatan musik sebagai tugas latar belakang, melacaknya di ledger tugas, lalu membangunkan agen lagi saat trek siap sehingga agen dapat memberi tahu pengguna dan melampirkan audio yang sudah selesai. Dalam obrolan grup/channel yang menggunakan pengiriman terlihat hanya melalui alat pesan, agen meneruskan hasil melalui alat pesan. Jika agen penyelesaian hanya menulis balasan akhir privat, OpenClaw melakukan fallback ke pengiriman channel langsung dengan media yang dihasilkan. Wake penyelesaian secara eksplisit memperingatkan agen bahwa balasan akhir normal bersifat privat di rute tersebut.

## Mulai cepat

### Didukung penyedia bersama

* ### Konfigurasikan auth

Tetapkan kunci API untuk setidaknya satu penyedia — misalnya `GEMINI_API_KEY` atau `MINIMAX_API_KEY`.

* ### Pilih model default (opsional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Minta agen

_"Generate an upbeat synthpop track about a night drive through a neon city."_

Agen memanggil `music_generate` secara otomatis. Tidak perlu allow-list alat.

Untuk konteks sinkron langsung tanpa eksekusi agen berbasis sesi, alat bawaan tetap melakukan fallback ke pembuatan inline dan mengembalikan path media akhir dalam hasil alat.

### Alur kerja ComfyUI

* ### Konfigurasikan alur kerja

Konfigurasikan `plugins.entries.comfy.config.music` dengan JSON alur kerja dan node prompt/output.

* ### Auth cloud (opsional)

Untuk Comfy Cloud, tetapkan `COMFY_API_KEY` atau `COMFY_CLOUD_API_KEY`.

* ### Panggil alat

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Contoh prompt:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Penyedia yang didukung

Penyedia | Model default | Input referensi | Kontrol yang didukung | Auth  
---|---|---|---|---  
ComfyUI | `workflow` | Hingga 1 gambar | Musik atau audio yang ditentukan alur kerja | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Hingga 10 gambar | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Tidak ada | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` atau OAuth MiniMax  
  
### Matriks kapabilitas

Kontrak mode eksplisit yang digunakan oleh `music_generate`, pengujian kontrak, dan sweep live bersama:

Penyedia | `generate` | `edit` | Batas edit | Lane live bersama  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 gambar | Tidak ada dalam sweep bersama; dicakup oleh `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 gambar | `generate`, `edit`  
MiniMax | ✓ | — | Tidak ada | `generate`  
  
Gunakan `action: "list"` untuk memeriksa penyedia dan model bersama yang tersedia saat runtime:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Gunakan `action: "status"` untuk memeriksa tugas musik berbasis sesi yang aktif:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Contoh pembuatan langsung:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Parameter alat

Prompt pembuatan musik. Wajib untuk `action: "generate"`.

`"status"` mengembalikan tugas sesi saat ini; `"list"` memeriksa penyedia.

Override penyedia/model (mis. `google/lyria-3-pro-preview`, `comfy/workflow`).

Lirik opsional ketika penyedia mendukung input lirik eksplisit.

Minta output khusus instrumental ketika penyedia mendukungnya.

Path atau URL gambar referensi tunggal.

Beberapa gambar referensi (hingga 10 pada penyedia yang mendukung).

Durasi target dalam detik ketika penyedia mendukung petunjuk durasi.

Petunjuk format output ketika penyedia mendukungnya.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Timeout permintaan penyedia opsional dalam milidetik. Jika dihilangkan, OpenClaw menggunakan `agents.defaults.musicGenerationModel.timeoutMs` jika dikonfigurasi. Nilai di bawah 10000ms dinaikkan menjadi 10000ms dan dilaporkan dalam hasil alat. OPENCLAW_DOCS_MARKER:paramClose:

## Perilaku async

Pembuatan musik berbasis sesi berjalan sebagai tugas latar belakang:

  * **Tugas latar belakang:** `music_generate` membuat tugas latar belakang, segera mengembalikan respons dimulai/tugas, dan memposting trek yang sudah selesai nanti dalam pesan agen tindak lanjut.
  * **Pencegahan duplikat:** saat tugas berstatus `queued` atau `running`, panggilan `music_generate` berikutnya dalam sesi yang sama mengembalikan status tugas alih-alih memulai pembuatan lain. Gunakan `action: "status"` untuk memeriksa secara eksplisit.
  * **Pencarian status:** `openclaw tasks list` atau `openclaw tasks show <taskId>` memeriksa status antrean, berjalan, dan terminal.
  * **Wake penyelesaian:** OpenClaw menyuntikkan event penyelesaian internal kembali ke sesi yang sama sehingga model dapat menulis tindak lanjut yang terlihat pengguna sendiri.
  * **Petunjuk prompt:** giliran pengguna/manual berikutnya dalam sesi yang sama mendapatkan petunjuk runtime kecil saat tugas musik sudah berjalan, sehingga model tidak memanggil `music_generate` lagi secara membabi buta.
  * **Fallback tanpa sesi:** konteks langsung/lokal tanpa sesi agen nyata berjalan inline dan mengembalikan hasil audio akhir dalam giliran yang sama.


### Siklus hidup tugas

Status | Arti  
---|---  
`queued` | Tugas dibuat, menunggu penyedia menerimanya.  
`running` | Penyedia sedang memproses (biasanya 30 detik hingga 3 menit tergantung penyedia dan durasi).  
`succeeded` | Trek siap; agen bangun dan mempostingnya ke percakapan.  
`failed` | Error penyedia atau timeout; agen bangun dengan detail error.  
  
Periksa status dari CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Konfigurasi

### Pemilihan model

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Urutan pemilihan penyedia

OpenClaw mencoba penyedia dalam urutan ini:

  1. Parameter `model` dari panggilan alat (jika agen menentukannya).
  2. `musicGenerationModel.primary` dari konfigurasi.
  3. `musicGenerationModel.fallbacks` secara berurutan.
  4. Deteksi otomatis hanya menggunakan default penyedia berbasis auth: 
     * penyedia default saat ini terlebih dahulu;
     * penyedia pembuatan musik terdaftar yang tersisa dalam urutan id penyedia.


Jika penyedia gagal, kandidat berikutnya dicoba secara otomatis. Jika semuanya gagal, error menyertakan detail dari setiap percobaan.

Tetapkan `agents.defaults.mediaGenerationAutoProviderFallback: false` untuk hanya menggunakan entri `model`, `primary`, dan `fallbacks` eksplisit.

## Catatan penyedia

ComfyUI

Digerakkan alur kerja dan bergantung pada graph yang dikonfigurasi plus pemetaan node untuk field prompt/output. Plugin `comfy` bawaan terhubung ke alat `music_generate` bersama melalui registry penyedia pembuatan musik bersama.

Google (Lyria 3)

Menggunakan pembuatan batch Lyria 3. Alur bawaan saat ini mendukung prompt, teks lirik opsional, dan gambar referensi opsional.

MiniMax

Menggunakan endpoint batch `music_generation`. Mendukung prompt, lirik opsional, mode instrumental, pengarah durasi, dan output mp3 melalui auth kunci API `minimax` atau OAuth `minimax-portal`.

## Memilih jalur yang tepat

  * **Didukung penyedia bersama** ketika Anda menginginkan pemilihan model, failover penyedia, dan alur async tugas/status bawaan.
  * **Jalur Plugin (ComfyUI)** ketika Anda memerlukan graph alur kerja khusus atau penyedia yang bukan bagian dari kapabilitas musik bawaan bersama.


Jika Anda men-debug perilaku khusus ComfyUI, lihat [ComfyUI](</id/providers/comfy>). Jika Anda men-debug perilaku penyedia bersama, mulai dengan [Google (Gemini)](</id/providers/google>) atau [MiniMax](</id/providers/minimax>).

## Mode kapabilitas penyedia

Kontrak pembuatan musik bersama mendukung deklarasi mode eksplisit:

  * `generate` untuk pembuatan hanya dari prompt.
  * `edit` ketika permintaan menyertakan satu atau beberapa gambar referensi.


Implementasi penyedia baru sebaiknya menggunakan blok mode eksplisit:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Field datar legacy seperti `maxInputImages`, `supportsLyrics`, dan `supportsFormat` **tidak** cukup untuk mengiklankan dukungan edit. Penyedia harus mendeklarasikan `generate` dan `edit` secara eksplisit agar pengujian live, pengujian kontrak, dan alat `music_generate` bersama dapat memvalidasi dukungan mode secara deterministik.

## Pengujian live

Cakupan live opt-in untuk penyedia bawaan bersama:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper repo:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

File live ini memuat env var penyedia yang hilang dari `~/.profile`, secara default memprioritaskan kunci API live/env di atas profil auth yang tersimpan, dan menjalankan cakupan `generate` serta `edit` yang dideklarasikan saat penyedia mengaktifkan mode edit. Cakupan saat ini:

  * `google`: `generate` plus `edit`
  * `minimax`: hanya `generate`
  * `comfy`: cakupan live Comfy terpisah, bukan sweep penyedia bersama


Ikut serta dalam cakupan live untuk jalur musik ComfyUI bawaan:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

File live Comfy juga mencakup alur kerja gambar dan video comfy saat bagian-bagian tersebut dikonfigurasi.

## Terkait

  * [Tugas latar belakang](</id/automation/tasks>) — pelacakan tugas untuk eksekusi `music_generate` yang terlepas
  * [ComfyUI](</id/providers/comfy>)
  * [Referensi konfigurasi](</id/gateway/config-agents#agent-defaults>) — konfigurasi `musicGenerationModel`
  * [Google (Gemini)](</id/providers/google>)
  * [MiniMax](</id/providers/minimax>)
  * [Model](</id/concepts/models>) — konfigurasi model dan failover
  * [Ikhtisar alat](</id/tools>)


Was this useful?YesNo