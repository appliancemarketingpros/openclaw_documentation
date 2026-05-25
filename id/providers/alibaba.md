---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/id/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw menyertakan Plugin `alibaba` bawaan yang mendaftarkan penyedia pembuatan video untuk model Wan di Alibaba Model Studio (nama internasional untuk DashScope). Plugin ini diaktifkan secara default; Anda hanya perlu menetapkan API key.

Properti | Nilai  
---|---  
ID penyedia | `alibaba`  
Plugin | bawaan, `enabledByDefault: true`  
Variabel env auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (kecocokan pertama menang)  
Flag onboarding | `--auth-choice alibaba-model-studio-api-key`  
Flag CLI langsung | `--alibaba-model-studio-api-key <key>`  
Model default | `alibaba/wan2.6-t2v`  
URL dasar default | `https://dashscope-intl.aliyuncs.com`  
  
## Memulai

* ### Tetapkan API key

Gunakan onboarding untuk menyimpan key pada penyedia `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Atau teruskan key secara langsung selama instalasi/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Atau ekspor salah satu variabel env yang diterima sebelum memulai Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Tetapkan model video default

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verifikasi bahwa penyedia telah dikonfigurasi

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

Daftar tersebut seharusnya menyertakan kelima model Wan bawaan. Jika `MODELSTUDIO_API_KEY` belum terselesaikan, `openclaw models status --json` melaporkan kredensial yang hilang di bawah `auth.unusableProfiles`.

## Model Wan bawaan

Ref model | Mode  
---|---  
`alibaba/wan2.6-t2v` | Teks-ke-video (default)  
`alibaba/wan2.6-i2v` | Gambar-ke-video  
`alibaba/wan2.6-r2v` | Referensi-ke-video  
`alibaba/wan2.6-r2v-flash` | Referensi-ke-video (cepat)  
`alibaba/wan2.7-r2v` | Referensi-ke-video  
  
## Kemampuan dan batasan

Penyedia bawaan ini mencerminkan batas API video Wan DashScope. Ketiga mode memiliki jumlah video dan batas durasi per permintaan yang sama; hanya bentuk inputnya yang berbeda.

Mode | Video output maks | Gambar input maks | Video input maks | Durasi maks | Kontrol yang didukung  
---|---|---|---|---|---  
Teks-ke-video | 1 | n/a | n/a | 10 dtk | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Gambar-ke-video | 1 | 1 | n/a | 10 dtk | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Referensi-ke-video | 1 | n/a | 4 | 10 dtk | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Saat permintaan menghilangkan `durationSeconds`, penyedia mengirim default yang diterima DashScope sebesar **5 detik**. Tetapkan `durationSeconds` secara eksplisit pada [alat pembuatan video](</id/tools/video-generation>) untuk memperpanjang hingga 10 dtk.

## Konfigurasi lanjutan

Timpa URL dasar DashScope

Penyedia menggunakan endpoint DashScope internasional secara default. Untuk menargetkan endpoint region Tiongkok, tetapkan:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Penyedia menghapus garis miring penutup sebelum menyusun URL task AIGC.

Prioritas env auth

OpenClaw menyelesaikan API key Alibaba dari variabel lingkungan dalam urutan ini, dengan mengambil nilai pertama yang tidak kosong:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Entri `auth.profiles` yang dikonfigurasi (ditetapkan melalui `openclaw models auth login`) menimpa resolusi variabel env. Lihat [Profil auth di FAQ model](</id/help/faq-models#what-is-an-auth-profile>) untuk rotasi profil, cooldown, dan mekanisme penimpaan.

Hubungan dengan Plugin Qwen

Kedua Plugin bawaan berkomunikasi dengan DashScope dan menerima API key yang saling tumpang tindih. Gunakan:

  * ID `alibaba/wan*.*` untuk menjalankan penyedia video Wan khusus yang didokumentasikan di halaman ini.
  * ID `qwen/*` untuk chat, embedding, dan pemahaman media Qwen (lihat [Qwen](</id/providers/qwen>)).


Menetapkan `MODELSTUDIO_API_KEY` sekali akan mengautentikasi kedua Plugin karena daftar variabel env auth sengaja saling tumpang tindih; Anda tidak perlu melakukan onboarding tiap Plugin secara terpisah.

## Terkait

[**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Qwen** Penyiapan chat, embedding, dan pemahaman media Qwen pada auth DashScope yang sama. ](</id/providers/qwen>) [**Referensi konfigurasi** Default agent dan konfigurasi model. ](</id/gateway/config-agents#agent-defaults>) [**FAQ model** Profil auth, mengganti model, dan menyelesaikan error "no profile". ](</id/help/faq-models>)

Was this useful?YesNo