---
title: Kembang Api
source_url: https://docs.openclaw.ai/id/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) mengekspos model berbobot terbuka dan model yang dirutekan melalui API yang kompatibel dengan OpenAI. OpenClaw menyertakan Plugin penyedia Fireworks bawaan yang dikirim dengan dua model Kimi yang sudah dikatalogkan dan menerima model Fireworks atau id router apa pun saat runtime.

Properti | Nilai  
---|---  
Id penyedia | `fireworks` (alias: `fireworks-ai`)  
Plugin | bawaan, `enabledByDefault: true`  
Variabel env auth | `FIREWORKS_API_KEY`  
Flag onboarding | `--auth-choice fireworks-api-key`  
Flag CLI langsung | `--fireworks-api-key <key>`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.fireworks.ai/inference/v1`  
Model default | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Alias default | `Kimi K2.5 Turbo`  
  
## Memulai

* ### Atur kunci API Fireworks

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Flag langsungCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env sajaCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding menyimpan kunci terhadap penyedia `fireworks` di profil autentikasi Anda dan menetapkan router **Fire Pass** Kimi K2.5 Turbo sebagai model default.

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Daftar tersebut harus menyertakan `Kimi K2.6` dan `Kimi K2.5 Turbo (Fire Pass)`. Jika `FIREWORKS_API_KEY` belum terselesaikan, `openclaw models status --json` melaporkan kredensial yang hilang di bawah `auth.unusableProfiles`.

## Penyiapan noninteraktif

Untuk instalasi berskrip atau CI, teruskan semuanya di baris perintah:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Katalog bawaan

Referensi model | Nama | Input | Konteks | Output maks | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | teks + gambar | 262,144 | 262,144 | Dipaksa nonaktif  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | teks + gambar | 256,000 | 256,000 | Dipaksa nonaktif (default)  
  
## Id model Fireworks kustom

OpenClaw menerima model Fireworks atau id router apa pun saat runtime. Gunakan id persis yang ditampilkan oleh Fireworks dan beri awalan `fireworks/`. Resolusi dinamis menggandakan templat Fire Pass (input teks + gambar, API yang kompatibel dengan OpenAI, biaya default nol) dan menonaktifkan thinking secara otomatis ketika id cocok dengan pola Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Cara kerja pemberian awalan id model

Setiap referensi model Fireworks di OpenClaw dimulai dengan `fireworks/` diikuti id persis atau jalur router dari platform Fireworks. Contoh:

  * Model router: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Model langsung: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw menghapus awalan `fireworks/` saat membuat permintaan API dan mengirim jalur yang tersisa ke endpoint Fireworks sebagai bidang `model` yang kompatibel dengan OpenAI.

Mengapa thinking dipaksa nonaktif untuk Kimi

Fireworks K2.6 mengembalikan 400 jika permintaan membawa parameter `reasoning_*` meskipun Kimi mendukung thinking melalui API milik Moonshot. Kebijakan bawaan (`extensions/fireworks/thinking-policy.ts`) hanya mengiklankan level thinking `off` untuk id model Kimi, sehingga peralihan `/think` manual dan permukaan kebijakan penyedia tetap selaras dengan kontrak runtime.

Untuk menggunakan penalaran Kimi end-to-end, konfigurasikan [penyedia Moonshot](</id/providers/moonshot>) dan rutekan model yang sama melaluinya.

Ketersediaan lingkungan untuk daemon

Jika Gateway berjalan sebagai layanan terkelola (launchd, systemd, Docker), kunci Fireworks harus terlihat oleh proses tersebut, bukan hanya oleh shell interaktif Anda.

Di macOS, `openclaw gateway install` sudah menghubungkan `~/.openclaw/.env` ke file lingkungan LaunchAgent. Jalankan ulang instalasi (atau `openclaw doctor --fix`) setelah merotasi kunci.

## Terkait

[**Penyedia model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Mode thinking** Level `/think`, kebijakan penyedia, dan perutean model yang mampu bernalar. ](</id/tools/thinking>) [**Moonshot** Jalankan Kimi dengan output thinking native melalui API milik Moonshot. ](</id/providers/moonshot>) [**Pemecahan masalah** Pemecahan masalah umum dan FAQ. ](</id/help/troubleshooting>)

Was this useful?YesNo