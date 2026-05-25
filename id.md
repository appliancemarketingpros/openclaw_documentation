---
title: OpenClaw
source_url: https://docs.openclaw.ai/id
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EKSFOLIASI! EKSFOLIASI!"_ — Seekor lobster luar angkasa, mungkin

**Gateway OS apa pun untuk agen AI di Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, dan lainnya.**

Kirim pesan, dapatkan respons agen dari saku Anda. Jalankan satu Gateway di seluruh kanal bawaan, Plugin kanal terbundel, WebChat, dan Node seluler.

[**Mulai** Instal OpenClaw dan jalankan Gateway dalam hitungan menit. ](</id/start/getting-started>) [**Jalankan Onboarding** Penyiapan terpandu dengan `openclaw onboard` dan alur pemasangan. ](</id/start/wizard>) [**Buka UI Kontrol** Luncurkan dasbor browser untuk chat, konfigurasi, dan sesi. ](</id/web/control-ui>)

## Apa itu OpenClaw?

OpenClaw adalah **gateway yang di-host sendiri** yang menghubungkan aplikasi chat dan permukaan kanal favorit Anda — kanal bawaan ditambah Plugin kanal terbundel atau eksternal seperti Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, dan lainnya — ke agen coding AI seperti Pi. Anda menjalankan satu proses Gateway di mesin Anda sendiri (atau server), dan proses itu menjadi jembatan antara aplikasi pesan Anda dan asisten AI yang selalu tersedia.

**Untuk siapa ini?** Developer dan pengguna tingkat lanjut yang menginginkan asisten AI pribadi yang bisa mereka kirimi pesan dari mana saja — tanpa melepaskan kendali atas data mereka atau bergantung pada layanan yang di-host.

**Apa yang membuatnya berbeda?**

  * **Di-host sendiri** : berjalan di perangkat keras Anda, dengan aturan Anda
  * **Multi-kanal** : satu Gateway melayani kanal bawaan ditambah Plugin kanal terbundel atau eksternal secara bersamaan
  * **Native untuk agen** : dibuat untuk agen coding dengan penggunaan alat, sesi, memori, dan perutean multi-agen
  * **Sumber terbuka** : berlisensi MIT, digerakkan oleh komunitas


**Apa yang Anda perlukan?** Node 24 (direkomendasikan), atau Node 22 LTS (`22.16+`) untuk kompatibilitas, kunci API dari penyedia pilihan Anda, dan 5 menit. Untuk kualitas dan keamanan terbaik, gunakan model generasi terbaru terkuat yang tersedia.

## Cara kerjanya
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway adalah sumber kebenaran tunggal untuk sesi, perutean, dan koneksi kanal.

## Kemampuan utama

[**Gateway multi-kanal** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, dan lainnya dengan satu proses Gateway. ](</id/channels>) [**Kanal Plugin** Plugin terbundel menambahkan Matrix, Nostr, Twitch, Zalo, dan lainnya dalam rilis terkini normal. ](</id/tools/plugin>) [**Perutean multi-agen** Sesi terisolasi per agen, ruang kerja, atau pengirim. ](</id/concepts/multi-agent>) [**Dukungan media** Kirim dan terima gambar, audio, dan dokumen. ](</id/nodes/images>) [**UI Kontrol Web** Dasbor browser untuk chat, konfigurasi, sesi, dan Node. ](</id/web/control-ui>) [**Node seluler** Pasangkan Node iOS dan Android untuk alur kerja yang mendukung Canvas, kamera, dan suara. ](</id/nodes>)

## Mulai cepat

* ### Instal OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Onboard dan instal layanan

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chat

Buka UI Kontrol di browser Anda dan kirim pesan:

bashCopy code
[code]
    openclaw dashboard
[/code]

Atau hubungkan kanal ([Telegram](</id/channels/telegram>) adalah yang tercepat) dan chat dari ponsel Anda.

Perlu penyiapan instalasi dan dev lengkap? Lihat [Mulai](</id/start/getting-started>).

## Dasbor

Buka UI Kontrol browser setelah Gateway dimulai.

  * Default lokal: <http://127.0.0.1:18789/>
  * Akses jarak jauh: [Permukaan web](</id/web>) dan [Tailscale](</id/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Konfigurasi (opsional)

Konfigurasi berada di `~/.openclaw/openclaw.json`.

  * Jika Anda **tidak melakukan apa pun** , OpenClaw menggunakan biner Pi terbundel dalam mode RPC dengan sesi per pengirim.
  * Jika Anda ingin menguncinya, mulai dengan `channels.whatsapp.allowFrom` dan (untuk grup) aturan penyebutan.


Contoh:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Mulai di sini

[**Hub dokumentasi** Semua dokumentasi dan panduan, diatur berdasarkan kasus penggunaan. ](</id/start/hubs>) [**Konfigurasi** Pengaturan Gateway inti, token, dan konfigurasi penyedia. ](</id/gateway/configuration>) [**Akses jarak jauh** Pola akses SSH dan tailnet. ](</id/gateway/remote>) [**Kanal** Penyiapan khusus kanal untuk Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, dan lainnya. ](</id/channels/telegram>) [**Node** Node iOS dan Android dengan pemasangan, Canvas, kamera, dan tindakan perangkat. ](</id/nodes>) [**Bantuan** Titik awal untuk perbaikan umum dan pemecahan masalah. ](</id/help>)

## Pelajari lebih lanjut

[**Daftar fitur lengkap** Kemampuan kanal, perutean, dan media yang lengkap. ](</id/concepts/features>) [**Perutean multi-agen** Isolasi ruang kerja dan sesi per agen. ](</id/concepts/multi-agent>) [**Keamanan** Token, daftar izin, dan kontrol keselamatan. ](</id/gateway/security>) [**Pemecahan masalah** Diagnostik Gateway dan kesalahan umum. ](</id/gateway/troubleshooting>) [**Tentang dan kredit** Asal-usul proyek, kontributor, dan lisensi. ](</id/reference/credits>)

Was this useful?YesNo