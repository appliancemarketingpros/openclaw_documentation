---
title: ClawDock
source_url: https://docs.openclaw.ai/id/install/clawdock
scraped_at: 2026-05-25
---

ClawDock adalah lapisan bantuan shell kecil untuk instalasi OpenClaw berbasis Docker.

Ini memberi Anda perintah singkat seperti `clawdock-start`, `clawdock-dashboard`, dan `clawdock-fix-token` alih-alih pemanggilan `docker compose ...` yang lebih panjang.

Jika Anda belum menyiapkan Docker, mulai dengan [Docker](</id/install/docker>).

## Instalasi

Gunakan path helper kanonis:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Jika sebelumnya Anda menginstal ClawDock dari `scripts/shell-helpers/clawdock-helpers.sh`, instal ulang dari path baru `scripts/clawdock/clawdock-helpers.sh`. Path GitHub raw lama telah dihapus.

## Yang Anda dapatkan

### Operasi dasar

Perintah | Deskripsi  
---|---  
`clawdock-start` | Memulai gateway  
`clawdock-stop` | Menghentikan gateway  
`clawdock-restart` | Memulai ulang gateway  
`clawdock-status` | Memeriksa status kontainer  
`clawdock-logs` | Mengikuti log gateway  
  
### Akses kontainer

Perintah | Deskripsi  
---|---  
`clawdock-shell` | Membuka shell di dalam kontainer gateway  
`clawdock-cli <command>` | Menjalankan perintah CLI OpenClaw di Docker  
`clawdock-exec <command>` | Menjalankan perintah arbitrer di dalam kontainer  
  
### UI web dan pairing

Perintah | Deskripsi  
---|---  
`clawdock-dashboard` | Membuka URL Control UI  
`clawdock-devices` | Mencantumkan pairing perangkat yang tertunda  
`clawdock-approve <id>` | Menyetujui permintaan pairing  
  
### Penyiapan dan pemeliharaan

Perintah | Deskripsi  
---|---  
`clawdock-fix-token` | Mengonfigurasi token gateway di dalam kontainer  
`clawdock-update` | Pull, rebuild, dan mulai ulang  
`clawdock-rebuild` | Rebuild image Docker saja  
`clawdock-clean` | Menghapus kontainer dan volume  
  
### Utilitas

Perintah | Deskripsi  
---|---  
`clawdock-health` | Menjalankan pemeriksaan kesehatan gateway  
`clawdock-token` | Mencetak token gateway  
`clawdock-cd` | Lompat ke direktori proyek OpenClaw  
`clawdock-config` | Membuka `~/.openclaw`  
`clawdock-show-config` | Mencetak file konfigurasi dengan nilai yang disamarkan  
`clawdock-workspace` | Membuka direktori workspace  
  
## Alur pertama kali

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Jika browser mengatakan pairing diperlukan:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Konfigurasi dan rahasia

ClawDock bekerja dengan pemisahan konfigurasi Docker yang sama seperti dijelaskan di [Docker](</id/install/docker>):

  * `<project>/.env` untuk nilai khusus Docker seperti nama image, port, dan token gateway
  * `~/.openclaw/.env` untuk kunci provider berbasis env dan token bot
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` untuk autentikasi OAuth/API-key provider yang disimpan
  * `~/.openclaw/openclaw.json` untuk konfigurasi perilaku


Gunakan `clawdock-show-config` saat Anda ingin memeriksa file `.env` dan `openclaw.json` dengan cepat. Ini menyamarkan nilai `.env` dalam output yang dicetak.

## Terkait

[**Docker** Instalasi Docker kanonis untuk OpenClaw. ](</id/install/docker>) [**Runtime VM Docker** Runtime VM yang dikelola Docker untuk isolasi yang diperkuat. ](</id/install/docker-vm-runtime>) [**Memperbarui** Memperbarui paket OpenClaw dan layanan terkelola. ](</id/install/updating>)

Was this useful?YesNo