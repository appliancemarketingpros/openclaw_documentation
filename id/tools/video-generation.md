---
title: Pembuatan video
source_url: https://docs.openclaw.ai/id/tools/video-generation
scraped_at: 2026-05-25
---

Agen OpenClaw dapat menghasilkan video dari prompt teks, gambar referensi, atau video yang sudah ada. Enam belas backend penyedia didukung, masing-masing dengan opsi model, mode input, dan rangkaian fitur yang berbeda. Agen memilih penyedia yang tepat secara otomatis berdasarkan konfigurasi Anda dan kunci API yang tersedia.

OpenClaw memperlakukan pembuatan video sebagai tiga mode runtime:

  * `generate` \- permintaan teks-ke-video tanpa media referensi.
  * `imageToVideo` \- permintaan menyertakan satu atau beberapa gambar referensi.
  * `videoToVideo` \- permintaan menyertakan satu atau beberapa video referensi.


Penyedia dapat mendukung subset apa pun dari mode-mode tersebut. Tool memvalidasi mode aktif sebelum pengiriman dan melaporkan mode yang didukung di `action=list`.

## Mulai cepat

* ### Konfigurasikan autentikasi

Atur kunci API untuk penyedia mana pun yang didukung:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Pilih model default (opsional)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Minta agen

> Buat video sinematik berdurasi 5 detik tentang lobster ramah yang berselancar saat matahari terbenam.

Agen memanggil `video_generate` secara otomatis. Tidak diperlukan allowlist tool.

## Cara kerja pembuatan asinkron

Pembuatan video bersifat asinkron. Ketika agen memanggil `video_generate` dalam sebuah sesi:

  1. OpenClaw mengirimkan permintaan ke penyedia dan langsung mengembalikan id tugas.
  2. Penyedia memproses pekerjaan di latar belakang (biasanya 30 detik hingga beberapa menit tergantung penyedia dan resolusi; penyedia lambat berbasis antrean dapat berjalan hingga timeout yang dikonfigurasi).
  3. Ketika video siap, OpenClaw membangunkan sesi yang sama dengan peristiwa penyelesaian internal.
  4. Agen memberi tahu pengguna dan melampirkan video yang selesai. Dalam obrolan grup/channel yang menggunakan pengiriman terlihat hanya melalui tool pesan, agen meneruskan hasil melalui tool pesan alih-alih OpenClaw mempostingnya secara langsung.


Saat sebuah pekerjaan sedang berjalan, panggilan `video_generate` duplikat dalam sesi yang sama mengembalikan status tugas saat ini alih-alih memulai pembuatan lain. Gunakan `openclaw tasks list` atau `openclaw tasks show <taskId>` untuk memeriksa progres dari CLI.

Di luar eksekusi agen yang didukung sesi (misalnya, pemanggilan tool langsung), tool kembali ke pembuatan inline dan mengembalikan jalur media final dalam giliran yang sama.

File video yang dihasilkan disimpan di bawah penyimpanan media yang dikelola OpenClaw ketika penyedia mengembalikan byte. Batas simpan default untuk video yang dihasilkan mengikuti batas media video, dan `agents.defaults.mediaMaxMb` menaikkannya untuk render yang lebih besar. Ketika penyedia juga mengembalikan URL output yang di-host, OpenClaw dapat mengirimkan URL tersebut alih-alih menggagalkan tugas jika persistensi lokal menolak file yang terlalu besar.

### Siklus hidup tugas

Status | Arti  
---|---  
`queued` | Tugas dibuat, menunggu penyedia menerimanya.  
`running` | Penyedia sedang memproses (biasanya 30 detik hingga beberapa menit tergantung penyedia dan resolusi).  
`succeeded` | Video siap; agen bangun dan mempostingnya ke percakapan.  
`failed` | Kesalahan penyedia atau timeout; agen bangun dengan detail kesalahan.  
  
Periksa status dari CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Jika tugas video sudah `queued` atau `running` untuk sesi saat ini, `video_generate` mengembalikan status tugas yang ada alih-alih memulai yang baru. Gunakan `action: "status"` untuk memeriksa secara eksplisit tanpa memicu pembuatan baru.

## Penyedia yang didukung

Penyedia | Model default | Teks | Referensi gambar | Referensi video | Autentikasi  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Ya (URL jarak jauh) | Ya (URL jarak jauh) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | Hingga 2 gambar (hanya model I2V; frame pertama + terakhir) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | Hingga 2 gambar (frame pertama + terakhir via role) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | Hingga 9 gambar referensi | Hingga 3 video | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 gambar | - | `COMFY_API_KEY` atau `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 gambar; hingga 9 dengan Seedance reference-to-video | Hingga 3 video dengan Seedance reference-to-video | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 gambar | 1 video | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 gambar | - | `MINIMAX_API_KEY` atau MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 gambar | 1 video | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | Hingga 4 gambar (frame pertama/terakhir atau referensi) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Ya (URL jarak jauh) | Ya (URL jarak jauh) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 gambar | 1 video | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 gambar | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 gambar (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 gambar frame pertama atau hingga 7 `reference_image` | 1 video | `XAI_API_KEY`  
  
Beberapa penyedia menerima variabel lingkungan kunci API tambahan atau alternatif. Lihat halaman penyedia individual untuk detail.

Jalankan `video_generate action=list` untuk memeriksa penyedia, model, dan mode runtime yang tersedia pada saat runtime.

### Matriks kemampuan

Kontrak mode eksplisit yang digunakan oleh `video_generate`, pengujian kontrak, dan sweep live bersama:

Penyedia | `generate` | `imageToVideo` | `videoToVideo` | Lane live bersama saat ini  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` dilewati karena penyedia ini memerlukan URL video `http(s)` jarak jauh  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Tidak ada dalam sweep bersama; cakupan khusus workflow berada bersama pengujian Comfy  
DeepInfra | ✓ | - | - | `generate`; skema video DeepInfra native adalah teks-ke-video dalam kontrak bawaan  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` hanya ketika menggunakan Seedance reference-to-video  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` bersama dilewati karena sweep Gemini/Veo berbasis buffer saat ini tidak menerima input tersebut  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` bersama dilewati karena jalur org/input ini saat ini memerlukan akses inpaint/remix sisi penyedia  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` dilewati karena penyedia ini memerlukan URL video `http(s)` jarak jauh  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` berjalan hanya ketika model yang dipilih adalah `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; `imageToVideo` bersama dilewati karena `veo3` bawaan hanya teks dan `kling` bawaan memerlukan URL gambar jarak jauh  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` dilewati karena penyedia ini saat ini memerlukan URL MP4 jarak jauh  
  
## Parameter tool

### Wajib

Deskripsi teks video yang akan dihasilkan. Wajib untuk `action: "generate"`.

### Input konten

Petunjuk peran per posisi opsional yang sejajar dengan daftar gambar gabungan. Nilai kanonis: `first_frame`, `last_frame`, `reference_image`.

Petunjuk peran per posisi opsional yang sejajar dengan daftar video gabungan. Nilai kanonis: `reference_video`.

Audio referensi tunggal (jalur atau URL). Digunakan untuk musik latar atau referensi suara ketika penyedia mendukung input audio.

Petunjuk peran per posisi opsional yang sejajar dengan daftar audio gabungan. Nilai kanonis: `reference_audio`.

### Kontrol gaya

Petunjuk rasio aspek seperti `1:1`, `16:9`, `9:16`, `adaptive`, atau nilai khusus penyedia. OpenClaw menormalkan atau mengabaikan nilai yang tidak didukung per penyedia.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI Petunjuk resolusi seperti `480P`, `720P`, `768P`, `1080P`, `4K`, atau nilai khusus penyedia. OpenClaw menormalkan atau mengabaikan nilai yang tidak didukung per penyedia. OPENCLAW_DOCS_MARKER:paramClose:

Durasi target dalam detik (dibulatkan ke nilai terdekat yang didukung penyedia).

Aktifkan audio yang dibuat dalam output ketika didukung. Berbeda dari `audioRef*` (input).

`adaptive` adalah sentinel khusus penyedia: nilai ini diteruskan apa adanya ke penyedia yang mendeklarasikan `adaptive` dalam kapabilitasnya (misalnya BytePlus Seedance menggunakannya untuk mendeteksi rasio secara otomatis dari dimensi gambar input). Penyedia yang tidak mendeklarasikannya menampilkan nilai melalui `details.ignoredOverrides` dalam hasil alat sehingga pengabaian terlihat.

### Lanjutan

`"status"` mengembalikan tugas sesi saat ini; `"list"` memeriksa penyedia.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Override penyedia/model (misalnya `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Timeout operasi penyedia opsional dalam milidetik. Jika dihilangkan, OpenClaw menggunakan `agents.defaults.videoGenerationModel.timeoutMs` jika dikonfigurasi. OPENCLAW_DOCS_MARKER:paramClose:

Opsi khusus penyedia sebagai objek JSON (misalnya `{"seed": 42, "draft": true}`). Penyedia yang mendeklarasikan skema bertipe memvalidasi kunci dan tipe; kunci yang tidak dikenal atau ketidakcocokan melewati kandidat selama fallback. Penyedia tanpa skema yang dideklarasikan menerima opsi apa adanya. Jalankan `video_generate action=list` untuk melihat apa yang diterima setiap penyedia.

Input referensi memilih mode runtime:

  * Tidak ada media referensi → `generate`
  * Referensi gambar apa pun → `imageToVideo`
  * Referensi video apa pun → `videoToVideo`
  * Input audio referensi **tidak** mengubah mode yang diselesaikan; input tersebut diterapkan di atas mode apa pun yang dipilih referensi gambar/video, dan hanya berfungsi dengan penyedia yang mendeklarasikan `maxInputAudios`.


Referensi gambar dan video campuran bukan permukaan kapabilitas bersama yang stabil. Pilih satu jenis referensi per permintaan.

#### Fallback dan opsi bertipe

Beberapa pemeriksaan kapabilitas diterapkan di lapisan fallback, bukan di batas alat, sehingga permintaan yang melampaui batas penyedia utama masih dapat berjalan pada fallback yang mampu:

  * Kandidat aktif yang tidak mendeklarasikan `maxInputAudios` (atau `0`) dilewati ketika permintaan berisi referensi audio; kandidat berikutnya dicoba.
  * `maxDurationSeconds` kandidat aktif di bawah `durationSeconds` yang diminta tanpa daftar `supportedDurationSeconds` yang dideklarasikan → dilewati.
  * Permintaan berisi `providerOptions` dan kandidat aktif secara eksplisit mendeklarasikan skema `providerOptions` bertipe → dilewati jika kunci yang diberikan tidak ada dalam skema atau tipe nilai tidak cocok. Penyedia tanpa skema yang dideklarasikan menerima opsi apa adanya (penerusan yang kompatibel ke belakang). Penyedia dapat menolak semua opsi penyedia dengan mendeklarasikan skema kosong (`capabilities.providerOptions: {}`), yang menyebabkan pelewatan yang sama seperti ketidakcocokan tipe.


Alasan pelewatan pertama dalam permintaan dicatat pada `warn` agar operator melihat ketika penyedia utama mereka dilewati; pelewatan berikutnya dicatat pada `debug` untuk menjaga rantai fallback yang panjang tetap senyap. Jika setiap kandidat dilewati, error agregat menyertakan alasan pelewatan untuk masing-masing.

## Tindakan

Tindakan | Apa yang dilakukan  
---|---  
`generate` | Default. Buat video dari prompt yang diberikan dan input referensi opsional.  
`status` | Periksa status tugas video yang sedang berjalan untuk sesi saat ini tanpa memulai pembuatan lain.  
`list` | Tampilkan penyedia, model, dan kapabilitas yang tersedia.  
  
## Pemilihan model

OpenClaw menyelesaikan model dalam urutan ini:

  1. **Parameter alat`model`** \- jika agen menentukannya dalam panggilan.
  2. **`videoGenerationModel.primary`** dari config.
  3. **`videoGenerationModel.fallbacks`** secara berurutan.
  4. **Deteksi otomatis** \- penyedia yang memiliki auth valid, dimulai dengan penyedia default saat ini, lalu penyedia yang tersisa dalam urutan alfabetis.


Jika penyedia gagal, kandidat berikutnya dicoba secara otomatis. Jika semua kandidat gagal, error menyertakan detail dari setiap percobaan.

Setel `agents.defaults.mediaGenerationAutoProviderFallback: false` untuk menggunakan hanya entri `model`, `primary`, dan `fallbacks` yang eksplisit.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Catatan penyedia

Alibaba

Menggunakan endpoint asinkron DashScope / Model Studio. Gambar dan video referensi harus berupa URL `http(s)` jarak jauh.

BytePlus (1.0)

ID penyedia: `byteplus`.

Model: `seedance-1-0-pro-250528` (default), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

Model T2V (`*-t2v-*`) tidak menerima input gambar; model I2V dan model `*-pro-*` umum mendukung satu gambar referensi (frame pertama). Berikan gambar secara posisional atau setel `role: "first_frame"`. ID model T2V secara otomatis dialihkan ke varian I2V yang sesuai ketika gambar diberikan.

Kunci `providerOptions` yang didukung: `seed` (number), `draft` (boolean - memaksa 480p), `camera_fixed` (boolean).

BytePlus Seedance 1.5

Memerlukan plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID penyedia: `byteplus-seedance15`. Model: `seedance-1-5-pro-251215`.

Menggunakan API `content[]` terpadu. Mendukung paling banyak 2 gambar input (`first_frame` \+ `last_frame`). Semua input harus berupa URL `https://` jarak jauh. Setel `role: "first_frame"` / `"last_frame"` pada setiap gambar, atau berikan gambar secara posisional.

`aspectRatio: "adaptive"` mendeteksi rasio secara otomatis dari gambar input. `audio: true` dipetakan ke `generate_audio`. `providerOptions.seed` (number) diteruskan.

BytePlus Seedance 2.0

Memerlukan plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID penyedia: `byteplus-seedance2`. Model: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Menggunakan API `content[]` terpadu. Mendukung hingga 9 gambar referensi, 3 video referensi, dan 3 audio referensi. Semua input harus berupa URL `https://` jarak jauh. Setel `role` pada setiap aset - nilai yang didukung: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` mendeteksi rasio secara otomatis dari gambar input. `audio: true` dipetakan ke `generate_audio`. `providerOptions.seed` (number) diteruskan.

ComfyUI

Eksekusi lokal atau cloud berbasis alur kerja. Mendukung teks-ke-video dan gambar-ke-video melalui grafik yang dikonfigurasi.

fal

Menggunakan alur berbasis antrean untuk pekerjaan yang berjalan lama. OpenClaw menunggu hingga 20 menit secara default sebelum memperlakukan pekerjaan antrean fal yang masih berjalan sebagai waktu habis. Sebagian besar model video fal menerima satu referensi gambar. Model referensi-ke-video Seedance 2.0 menerima hingga 9 gambar, 3 video, dan 3 referensi audio, dengan paling banyak 12 file referensi total.

Google (Gemini / Veo)

Mendukung satu referensi gambar atau satu referensi video. Permintaan audio yang dihasilkan diabaikan dengan peringatan pada jalur API Gemini karena API tersebut menolak parameter `generateAudio` untuk pembuatan video Veo saat ini.

MiniMax

Hanya satu referensi gambar. MiniMax menerima resolusi `768P` dan `1080P`; permintaan seperti `720P` dinormalisasi ke nilai terdekat yang didukung sebelum dikirim.

OpenAI

Hanya penggantian `size` yang diteruskan. Penggantian gaya lain (`aspectRatio`, `resolution`, `audio`, `watermark`) diabaikan dengan peringatan.

OpenRouter

Menggunakan API `/videos` asinkron OpenRouter. OpenClaw mengirim pekerjaan, melakukan polling `polling_url`, dan mengunduh `unsigned_urls` atau titik akhir konten pekerjaan yang terdokumentasi. Default bawaan `google/veo-3.1-fast` mengiklankan durasi 4/6/8 detik, resolusi `720P`/`1080P`, dan rasio aspek `16:9`/`9:16`.

Qwen

Backend DashScope yang sama seperti Alibaba. Input referensi harus berupa URL `http(s)` jarak jauh; file lokal ditolak sejak awal.

Runway

Mendukung file lokal melalui URI data. Video-ke-video memerlukan `runway/gen4_aleph`. Proses hanya teks mengekspos rasio aspek `16:9` dan `9:16`.

Together

Hanya satu referensi gambar.

Vydra

Menggunakan `https://www.vydra.ai/api/v1` secara langsung untuk menghindari pengalihan yang menghapus autentikasi. `veo3` dibundel hanya sebagai teks-ke-video; `kling` memerlukan URL gambar jarak jauh.

xAI

Mendukung teks-ke-video, gambar bingkai pertama tunggal-ke-video, hingga 7 input `reference_image` melalui `reference_images` xAI, serta alur edit/perpanjang video jarak jauh.

## Mode kapabilitas penyedia

Kontrak pembuatan video bersama mendukung kapabilitas khusus mode alih-alih hanya batas agregat datar. Implementasi penyedia baru sebaiknya memilih blok mode eksplisit:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

Kolom agregat datar seperti `maxInputImages` dan `maxInputVideos` **tidak** cukup untuk mengiklankan dukungan mode transformasi. Penyedia sebaiknya mendeklarasikan `generate`, `imageToVideo`, dan `videoToVideo` secara eksplisit agar pengujian langsung, pengujian kontrak, dan alat bersama `video_generate` dapat memvalidasi dukungan mode secara deterministik.

Ketika satu model dalam sebuah penyedia memiliki dukungan input referensi yang lebih luas daripada yang lain, gunakan `maxInputImagesByModel`, `maxInputVideosByModel`, atau `maxInputAudiosByModel` alih-alih menaikkan batas untuk seluruh mode.

## Pengujian langsung

Cakupan langsung ikut serta untuk penyedia bawaan bersama:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Pembungkus repo:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

File langsung ini memuat variabel lingkungan penyedia yang hilang dari `~/.profile`, secara default memilih kunci API langsung/lingkungan sebelum profil autentikasi tersimpan, dan menjalankan uji dasar aman rilis secara default:

  * `generate` untuk setiap penyedia non-FAL dalam penyapuan.
  * Prompt lobster satu detik.
  * Batas operasi per penyedia dari `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (`180000` secara default).


FAL bersifat ikut serta karena latensi antrean sisi penyedia dapat mendominasi waktu rilis:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Atur `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` untuk juga menjalankan mode transformasi yang dideklarasikan yang dapat dijalankan dengan aman oleh penyapuan bersama dengan media lokal:

  * `imageToVideo` ketika `capabilities.imageToVideo.enabled`.
  * `videoToVideo` ketika `capabilities.videoToVideo.enabled` dan penyedia/model menerima input video lokal berbasis buffer dalam penyapuan bersama.


Saat ini jalur langsung `videoToVideo` bersama mencakup `runway` hanya ketika Anda memilih `runway/gen4_aleph`.

## Konfigurasi

Atur model pembuatan video default di konfigurasi OpenClaw Anda:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

Atau melalui CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## Terkait

  * [Alibaba Model Studio](</id/providers/alibaba>)
  * [Tugas latar belakang](</id/automation/tasks>) \- pelacakan tugas untuk pembuatan video asinkron
  * [BytePlus](</id/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</id/providers/comfy>)
  * [Referensi konfigurasi](</id/gateway/config-agents#agent-defaults>)
  * [fal](</id/providers/fal>)
  * [Google (Gemini)](</id/providers/google>)
  * [MiniMax](</id/providers/minimax>)
  * [Model](</id/concepts/models>)
  * [OpenAI](</id/providers/openai>)
  * [Qwen](</id/providers/qwen>)
  * [Runway](</id/providers/runway>)
  * [Together AI](</id/providers/together>)
  * [Ikhtisar alat](</id/tools>)
  * [Vydra](</id/providers/vydra>)
  * [xAI](</id/providers/xai>)


Was this useful?YesNo