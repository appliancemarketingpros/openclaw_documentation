---
title: Ikhtisar orientasi awal
source_url: https://docs.openclaw.ai/id/start/onboarding-overview
scraped_at: 2026-05-25
---

OpenClaw memiliki dua jalur onboarding. Keduanya mengonfigurasi autentikasi, Gateway, dan channel chat opsional — perbedaannya hanya pada cara Anda berinteraksi dengan penyiapan.

## Jalur mana yang sebaiknya saya gunakan?

| Onboarding CLI | Onboarding aplikasi macOS  
---|---|---  
**Platform** | macOS, Linux, Windows (native atau WSL2) | Hanya macOS  
**Antarmuka** | Wizard terminal | UI terpandu di aplikasi  
**Paling cocok untuk** | Server, headless, kontrol penuh | Mac desktop, penyiapan visual  
**Otomasi** | `--non-interactive` untuk skrip | Hanya manual  
**Perintah** | `openclaw onboard` | Jalankan aplikasi  
  
Sebagian besar pengguna sebaiknya mulai dengan **onboarding CLI** — ini berfungsi di mana saja dan memberi Anda kontrol paling besar.

## Yang dikonfigurasi onboarding

Terlepas dari jalur yang Anda pilih, onboarding menyiapkan:

  1. **Penyedia model dan autentikasi** — kunci API, OAuth, atau token penyiapan untuk penyedia yang Anda pilih
  2. **Workspace** — direktori untuk file agent, templat bootstrap, dan memori
  3. **Gateway** — port, alamat bind, mode autentikasi
  4. **Channel** (opsional) — channel chat bawaan dan terbundel seperti iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, Telegram, WhatsApp, dan lainnya
  5. **Daemon** (opsional) — layanan latar belakang agar Gateway dimulai secara otomatis


## Onboarding CLI

Jalankan di terminal apa pun:

bashCopy code
[code]
    openclaw onboard
[/code]

Tambahkan `--install-daemon` untuk juga menginstal layanan latar belakang dalam satu langkah.

Referensi lengkap: [Onboarding (CLI)](</id/start/wizard>) Dokumentasi perintah CLI: [`openclaw onboard`](</id/cli/onboard>)

## Onboarding aplikasi macOS

Buka aplikasi OpenClaw. Wizard saat pertama dijalankan memandu Anda melalui langkah yang sama dengan antarmuka visual.

Referensi lengkap: [Onboarding (Aplikasi macOS)](</id/start/onboarding>)

## Penyedia kustom atau tidak terdaftar

Jika penyedia Anda tidak tercantum dalam onboarding, pilih **Penyedia Kustom** dan masukkan:

  * Mode kompatibilitas API (kompatibel dengan OpenAI, kompatibel dengan Anthropic, atau deteksi otomatis)
  * URL dasar dan kunci API
  * ID model dan alias opsional


Beberapa endpoint kustom dapat berdampingan — masing-masing mendapatkan ID endpoint sendiri.

## Terkait

  * [Memulai](</id/start/getting-started>)
  * [Referensi penyiapan CLI](</id/start/wizard-cli-reference>)


Was this useful?YesNo