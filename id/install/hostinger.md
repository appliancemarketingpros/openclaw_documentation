---
title: Hostinger
source_url: https://docs.openclaw.ai/id/install/hostinger
scraped_at: 2026-05-25
---

Jalankan Gateway OpenClaw persisten di [Hostinger](<https://www.hostinger.com/openclaw>) melalui deployment terkelola **1-Click** atau pemasangan **VPS**.

## Prasyarat

  * Akun Hostinger ([daftar](<https://www.hostinger.com/openclaw>))
  * Sekitar 5-10 menit


## Opsi A: OpenClaw 1-Click

Cara tercepat untuk memulai. Hostinger menangani infrastruktur, Docker, dan pembaruan otomatis.

* ### Beli dan luncurkan

  1. Dari [halaman OpenClaw Hostinger](<https://www.hostinger.com/openclaw>), pilih paket Managed OpenClaw dan selesaikan checkout.


* ### Pilih channel pesan

Pilih satu atau lebih channel yang akan dihubungkan:

  * **WhatsApp** \-- pindai kode QR yang ditampilkan di wizard penyiapan.
  * **Telegram** \-- tempel token bot dari [BotFather](<https://t.me/BotFather>).


* ### Selesaikan instalasi

Klik **Finish** untuk men-deploy instans. Setelah siap, akses dashboard OpenClaw dari **OpenClaw Overview** di hPanel.

## Opsi B: OpenClaw di VPS

Kontrol lebih besar atas server Anda. Hostinger men-deploy OpenClaw melalui Docker di VPS Anda dan Anda mengelolanya melalui **Docker Manager** di hPanel.

* ### Beli VPS

  1. Dari [halaman OpenClaw Hostinger](<https://www.hostinger.com/openclaw>), pilih paket OpenClaw on VPS dan selesaikan checkout.


* ### Konfigurasikan OpenClaw

Setelah VPS diprovisikan, isi bidang konfigurasi:

  * **Gateway token** \-- dibuat otomatis; simpan untuk digunakan nanti.
  * **Nomor WhatsApp** \-- nomor Anda dengan kode negara (opsional).
  * **Token bot Telegram** \-- dari [BotFather](<https://t.me/BotFather>) (opsional).
  * **API key** \-- hanya diperlukan jika Anda tidak memilih kredit Ready-to-Use AI selama checkout.


* ### Mulai OpenClaw

Klik **Deploy**. Setelah berjalan, buka dashboard OpenClaw dari hPanel dengan mengklik **Open**.

Log, restart, dan pembaruan dikelola langsung dari antarmuka Docker Manager di hPanel. Untuk memperbarui, tekan **Update** di Docker Manager dan itu akan menarik image terbaru.

## Verifikasi penyiapan Anda

Kirim "Hi" ke asisten Anda di channel yang Anda hubungkan. OpenClaw akan membalas dan memandu Anda melalui preferensi awal.

## Pemecahan masalah

**Dashboard tidak memuat** \-- Tunggu beberapa menit sampai container selesai diprovisikan. Periksa log Docker Manager di hPanel.

**Container Docker terus restart** \-- Buka log Docker Manager dan cari error konfigurasi (token hilang, API key tidak valid).

**Bot Telegram tidak merespons** \-- Kirim pesan kode pairing Anda dari Telegram langsung sebagai pesan di dalam chat OpenClaw Anda untuk menyelesaikan koneksi.

## Langkah selanjutnya

  * [Channels](</id/channels>) \-- hubungkan Telegram, WhatsApp, Discord, dan lainnya
  * [Konfigurasi Gateway](</id/gateway/configuration>) \-- semua opsi config


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Hosting VPS](</id/vps>)
  * [DigitalOcean](</id/install/digitalocean>)


Was this useful?YesNo