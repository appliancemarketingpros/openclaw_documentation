---
title: Anthropic
source_url: https://docs.openclaw.ai/id/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic membangun keluarga model **Claude**. OpenClaw mendukung dua rute autentikasi:

  * **Kunci API** — akses API Anthropic langsung dengan penagihan berbasis penggunaan (model `anthropic/*`)
  * **Claude CLI** — gunakan kembali login Claude CLI yang sudah ada pada host yang sama


## Memulai

### Kunci API

**Paling cocok untuk:** akses API standar dan penagihan berbasis penggunaan.

* ### Dapatkan kunci API Anda

Buat kunci API di [Anthropic Console](<https://console.anthropic.com/>).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Atau berikan kunci secara langsung:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Contoh konfigurasi

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Paling cocok untuk:** menggunakan kembali login Claude CLI yang sudah ada tanpa kunci API terpisah.

* ### Pastikan Claude CLI terinstal dan sudah login

Verifikasi dengan:

bashCopy code
[code]
    claude --version
[/code]

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw mendeteksi dan menggunakan kembali kredensial Claude CLI yang sudah ada.

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Contoh konfigurasi

Utamakan ref model Anthropic kanonis ditambah override runtime CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Ref model lama `claude-cli/claude-opus-4-7` masih berfungsi untuk kompatibilitas, tetapi konfigurasi baru sebaiknya mempertahankan pemilihan penyedia/model sebagai `anthropic/*` dan menempatkan backend eksekusi dalam kebijakan runtime penyedia/model.

## Default thinking (Claude 4.6)

Model Claude 4.6 menggunakan thinking `adaptive` secara default di OpenClaw jika tidak ada level thinking eksplisit yang ditetapkan.

Override per pesan dengan `/think:<level>` atau di parameter model:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Caching prompt

OpenClaw mendukung fitur caching prompt Anthropic untuk autentikasi kunci API.

Nilai | Durasi cache | Deskripsi  
---|---|---  
`"short"` (default) | 5 menit | Diterapkan otomatis untuk autentikasi kunci API  
`"long"` | 1 jam | Cache diperpanjang  
`"none"` | Tanpa caching | Nonaktifkan caching prompt  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Override cache per agen

Gunakan parameter tingkat model sebagai baseline, lalu override agen tertentu melalui `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Urutan penggabungan konfigurasi:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (`id` yang cocok, override berdasarkan kunci)


Ini memungkinkan satu agen mempertahankan cache berumur panjang sementara agen lain pada model yang sama menonaktifkan caching untuk traffic yang bursty/berpenggunaan ulang rendah.

Catatan Bedrock Claude

  * Model Anthropic Claude di Bedrock (`amazon-bedrock/*anthropic.claude*`) menerima pass-through `cacheRetention` saat dikonfigurasi.
  * Model Bedrock non-Anthropic dipaksa ke `cacheRetention: "none"` saat runtime.
  * Default cerdas kunci API juga mengisi `cacheRetention: "short"` untuk ref Claude-on-Bedrock saat tidak ada nilai eksplisit yang ditetapkan.


## Konfigurasi lanjutan

Mode cepat

Toggle `/fast` bersama OpenClaw mendukung traffic Anthropic langsung (kunci API dan OAuth ke `api.anthropic.com`).

Perintah | Dipetakan ke  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Pemahaman media (gambar dan PDF)

Plugin Anthropic bawaan mendaftarkan pemahaman gambar dan PDF. OpenClaw menyelesaikan kapabilitas media secara otomatis dari autentikasi Anthropic yang dikonfigurasi — tidak diperlukan konfigurasi tambahan.

Properti | Nilai  
---|---  
Model default | `claude-opus-4-7`  
Input yang didukung | Gambar, dokumen PDF  
  
Saat gambar atau PDF dilampirkan ke percakapan, OpenClaw secara otomatis merutekannya melalui penyedia pemahaman media Anthropic.

Jendela konteks 1M (beta)

Jendela konteks 1M Anthropic dikontrol oleh beta gate. Aktifkan per model:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw memetakan ini ke `anthropic-beta: context-1m-2025-08-07` pada permintaan.

`params.context1m: true` juga berlaku untuk backend Claude CLI (`claude-cli/*`) bagi model Opus dan Sonnet yang memenuhi syarat, memperluas jendela konteks runtime untuk sesi CLI tersebut agar sesuai dengan perilaku API langsung.

Konteks 1M Claude Opus 4.7

`anthropic/claude-opus-4.7` dan varian `claude-cli`-nya memiliki jendela konteks 1M secara default — tidak perlu `params.context1m: true`.

## Pemecahan masalah

Error 401 / token tiba-tiba tidak valid

Auth token Anthropic kedaluwarsa dan dapat dicabut. Untuk penyiapan baru, gunakan kunci API Anthropic sebagai gantinya.

Tidak ada kunci API ditemukan untuk penyedia "anthropic"

Auth Anthropic bersifat **per agen** — agen baru tidak mewarisi kunci agen utama. Jalankan ulang onboarding untuk agen tersebut (atau konfigurasikan kunci API pada host Gateway), lalu verifikasi dengan `openclaw models status`.

Tidak ada kredensial ditemukan untuk profil "anthropic:default"

Jalankan `openclaw models status` untuk melihat profil auth mana yang aktif. Jalankan ulang onboarding, atau konfigurasikan kunci API untuk path profil tersebut.

Tidak ada profil auth yang tersedia (semuanya dalam cooldown)

Periksa `openclaw models status --json` untuk `auth.unusableProfiles`. Cooldown rate-limit Anthropic dapat bersifat scoped per model, sehingga model Anthropic saudara mungkin masih dapat digunakan. Tambahkan profil Anthropic lain atau tunggu cooldown.

## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Backend CLI** Detail penyiapan dan runtime backend Claude CLI. ](</id/gateway/cli-backends>) [**Caching prompt** Cara kerja caching prompt lintas penyedia. ](</id/reference/prompt-caching>) [**OAuth dan auth** Detail auth dan aturan penggunaan ulang kredensial. ](</id/gateway/authentication>)

Was this useful?YesNo