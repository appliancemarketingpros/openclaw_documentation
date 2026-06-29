---
title: Kotak Upstash
source_url: https://docs.openclaw.ai/id/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Jalankan OpenClaw Gateway persisten di Upstash Box, lingkungan Linux terkelola dengan dukungan siklus hidup keep-alive.

Gunakan tunnel SSH untuk akses dasbor. Jangan mengekspos port Gateway secara langsung ke internet publik.

## Prasyarat

  * Akun Upstash
  * Upstash Box keep-alive
  * Klien SSH di mesin lokal Anda


## Buat Box

Buat Box keep-alive di Upstash Console. Catat ID Box, seperti `right-flamingo-14486`, dan kunci API Box Anda.

Upstash mempertahankan panduan OpenClaw Box terkininya di [Penyiapan OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Terhubung dengan tunnel SSH

Teruskan port dasbor OpenClaw ke mesin lokal Anda. Gunakan kunci API Box Anda sebagai kata sandi SSH saat diminta:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Opsi keepalive mengurangi terputusnya tunnel yang menganggur selama onboarding.

## Instal OpenClaw

Di dalam Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Ikuti prompt. Salin URL dasbor dan token saat onboarding selesai.

## Mulai Gateway

Konfigurasikan Gateway untuk jaringan Box dan mulai di latar belakang:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Dengan tunnel SSH aktif, buka URL dasbor secara lokal:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Mulai ulang otomatis

Tetapkan perintah ini sebagai skrip init Box agar Gateway dimulai ulang saat Box dimulai:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Pemecahan masalah

Jika SSH berhenti merespons selama onboarding, hubungkan ulang dengan konfigurasi SSH yang bersih dan keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Ini melewati pengaturan lokal `~/.ssh/config` yang usang dan menjaga tunnel tetap aktif selama periode jaringan menganggur.

## Terkait

  * [Akses jarak jauh](</id/gateway/remote>)
  * [Keamanan Gateway](</id/gateway/security>)
  * [Memperbarui OpenClaw](</id/install/updating>)


Was this useful?YesNo

Open issue