---
title: Gateway di macOS
source_url: https://docs.openclaw.ai/id/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app tidak lagi membundel Node/Bun atau runtime Gateway. Aplikasi macOS mengharapkan pemasangan CLI `openclaw` **eksternal** , tidak menjalankan Gateway sebagai proses anak, dan mengelola layanan launchd per pengguna untuk menjaga Gateway tetap berjalan (atau tersambung ke Gateway lokal yang sudah ada jika sudah berjalan).

## Instal CLI (wajib untuk mode lokal)

Node 24 adalah runtime default di Mac. Node 22 LTS, saat ini `22.16+`, masih berfungsi untuk kompatibilitas. Lalu instal `openclaw` secara global:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Tombol **Instal CLI** di aplikasi macOS menjalankan alur pemasangan global yang sama dengan yang digunakan aplikasi secara internal: aplikasi lebih memilih npm terlebih dahulu, lalu pnpm, lalu bun jika itu satu-satunya pengelola paket yang terdeteksi. Node tetap menjadi runtime Gateway yang direkomendasikan.

## Launchd (Gateway sebagai LaunchAgent)

Label:

  * `ai.openclaw.gateway` (atau `ai.openclaw.<profile>`; warisan `com.openclaw.*` mungkin tetap ada)


Lokasi plist (per pengguna):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (atau `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Pengelola:

  * Aplikasi macOS memiliki pemasangan/pembaruan LaunchAgent dalam mode Lokal.
  * CLI juga dapat memasangnya: `openclaw gateway install`.


Perilaku:

  * "OpenClaw Aktif" mengaktifkan/menonaktifkan LaunchAgent.
  * Keluar dari aplikasi **tidak** menghentikan gateway (launchd menjaganya tetap aktif).
  * Jika Gateway sudah berjalan pada port yang dikonfigurasi, aplikasi akan tersambung ke Gateway tersebut alih-alih memulai yang baru.


Pencatatan log:

  * stdout/err launchd: `/tmp/openclaw/openclaw-gateway.log`


## Kompatibilitas versi

Aplikasi macOS memeriksa versi gateway terhadap versinya sendiri. Jika keduanya tidak kompatibel, perbarui CLI global agar sesuai dengan versi aplikasi.

## Pemeriksaan smoke

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Kemudian:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Terkait

  * [aplikasi macOS](</id/platforms/macos>)
  * [Runbook Gateway](</id/gateway>)


Was this useful?YesNo