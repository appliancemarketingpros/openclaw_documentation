---
title: Hetzner
source_url: https://docs.openclaw.ai/id/install/hetzner
scraped_at: 2026-05-25
---

## Tujuan

Menjalankan OpenClaw Gateway yang persisten di VPS Hetzner menggunakan Docker, dengan state yang tahan lama, biner yang sudah disertakan, dan perilaku restart yang aman.

Jika Anda menginginkan "OpenClaw 24/7 seharga sekitar $5", ini adalah penyiapan andal yang paling sederhana. Harga Hetzner dapat berubah; pilih VPS Debian/Ubuntu terkecil dan tingkatkan skalanya jika Anda mengalami OOM.

Pengingat model keamanan:

  * Agen yang dibagikan di perusahaan tidak masalah ketika semua orang berada dalam batas kepercayaan yang sama dan runtime hanya untuk bisnis.
  * Pertahankan pemisahan ketat: VPS/runtime khusus + akun khusus; jangan gunakan profil Apple/Google/browser/password-manager pribadi di host tersebut.
  * Jika pengguna saling tidak tepercaya, pisahkan berdasarkan gateway/host/pengguna OS.


Lihat [Keamanan](</id/gateway/security>) dan [hosting VPS](</id/vps>).

## Apa yang kita lakukan (dalam istilah sederhana)?

  * Menyewa server Linux kecil (VPS Hetzner)
  * Menginstal Docker (runtime aplikasi terisolasi)
  * Memulai OpenClaw Gateway di Docker
  * Mempertahankan `~/.openclaw` \+ `~/.openclaw/workspace` di host (tetap ada setelah restart/rebuild)
  * Mengakses Control UI dari laptop Anda melalui tunnel SSH


State `~/.openclaw` yang di-mount tersebut mencakup `openclaw.json`, per agen `agents/<agentId>/agent/auth-profiles.json`, dan `.env`.

Gateway dapat diakses melalui:

  * Penerusan port SSH dari laptop Anda
  * Paparan port langsung jika Anda mengelola firewall dan token sendiri


Panduan ini mengasumsikan Ubuntu atau Debian di Hetzner.  
Jika Anda menggunakan VPS Linux lain, sesuaikan paketnya. Untuk alur Docker generik, lihat [Docker](</id/install/docker>).

* * *

## Jalur cepat (operator berpengalaman)

  1. Sediakan VPS Hetzner
  2. Instal Docker
  3. Clone repositori OpenClaw
  4. Buat direktori host persisten
  5. Konfigurasikan `.env` dan `docker-compose.yml`
  6. Sertakan biner yang diperlukan ke dalam image
  7. `docker compose up -d`
  8. Verifikasi persistensi dan akses Gateway


* * *

## Yang Anda perlukan

  * VPS Hetzner dengan akses root
  * Akses SSH dari laptop Anda
  * Kenyamanan dasar dengan SSH + salin/tempel
  * ~20 menit
  * Docker dan Docker Compose
  * Kredensial auth model
  * Kredensial provider opsional 
    * QR WhatsApp
    * Token bot Telegram
    * OAuth Gmail


* * *

* ### Provision the VPS

Buat VPS Ubuntu atau Debian di Hetzner.

Hubungkan sebagai root:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Panduan ini mengasumsikan VPS bersifat stateful. Jangan perlakukan sebagai infrastruktur sekali pakai.

* ### Install Docker (on the VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Verifikasi:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone the OpenClaw repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Panduan ini mengasumsikan Anda akan membangun image kustom untuk menjamin persistensi biner.

* ### Create persistent host directories

Container Docker bersifat sementara. Semua state jangka panjang harus berada di host.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configure environment variables

Buat `.env` di root repositori.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Atur `OPENCLAW_GATEWAY_TOKEN` ketika Anda ingin mengelola token gateway stabil melalui `.env`; jika tidak, konfigurasikan `gateway.auth.token` sebelum mengandalkan klien lintas restart. Jika kedua sumber tidak ada, OpenClaw menggunakan token khusus runtime untuk startup tersebut. Buat kata sandi keyring dan tempelkan ke `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Jangan commit file ini.**

File `.env` ini untuk env container/runtime seperti `OPENCLAW_GATEWAY_TOKEN`. Auth OAuth/API-key provider yang disimpan berada di `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` yang di-mount.

* ### Docker Compose configuration

Buat atau perbarui `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` hanya untuk kemudahan bootstrap, bukan pengganti konfigurasi gateway yang benar. Tetap atur auth (`gateway.auth.token` atau kata sandi) dan gunakan pengaturan bind yang aman untuk deployment Anda.

* ### Shared Docker VM runtime steps

Gunakan panduan runtime bersama untuk alur host Docker umum:

  * [Sertakan biner yang diperlukan ke dalam image](</id/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Build dan luncurkan](</id/install/docker-vm-runtime#build-and-launch>)
  * [Apa yang bertahan di mana](</id/install/docker-vm-runtime#what-persists-where>)
  * [Pembaruan](</id/install/docker-vm-runtime#updates>)


* ### Hetzner-specific access

Setelah langkah build dan peluncuran bersama, selesaikan penyiapan berikut untuk membuka tunnel:

**Prasyarat:** Pastikan konfigurasi sshd VPS Anda mengizinkan penerusan TCP. Jika Anda telah memperketat konfigurasi SSH, periksa `/etc/ssh/sshd_config` dan atur:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` mengizinkan penerusan lokal `ssh -L` dari laptop Anda sekaligus memblokir penerusan jarak jauh dari server. Mengaturnya ke `no` akan membuat tunnel gagal dengan: `channel 3: open failed: administratively prohibited: open failed`

Setelah mengonfirmasi penerusan TCP diaktifkan, restart layanan SSH (`systemctl restart ssh`) dan jalankan tunnel dari laptop Anda:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Buka:

`http://127.0.0.1:18789/`

Tempel rahasia bersama yang dikonfigurasi. Panduan ini menggunakan token gateway secara default; jika Anda beralih ke auth kata sandi, gunakan kata sandi tersebut.

Peta persistensi bersama berada di [Runtime VM Docker](</id/install/docker-vm-runtime#what-persists-where>).

## Infrastructure as Code (Terraform)

Untuk tim yang lebih memilih alur kerja infrastructure-as-code, penyiapan Terraform yang dikelola komunitas menyediakan:

  * Konfigurasi Terraform modular dengan manajemen state jarak jauh
  * Provisioning otomatis melalui cloud-init
  * Skrip deployment (bootstrap, deploy, backup/restore)
  * Pengerasan keamanan (firewall, UFW, akses khusus SSH)
  * Konfigurasi tunnel SSH untuk akses gateway


**Repositori:**

  * Infrastruktur: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Konfigurasi Docker: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Pendekatan ini melengkapi penyiapan Docker di atas dengan deployment yang dapat direproduksi, infrastruktur yang dikontrol versi, dan pemulihan bencana otomatis.

## Langkah berikutnya

  * Siapkan channel perpesanan: [Channel](</id/channels>)
  * Konfigurasikan Gateway: [Konfigurasi Gateway](</id/gateway/configuration>)
  * Tetap perbarui OpenClaw: [Memperbarui](</id/install/updating>)


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Fly.io](</id/install/fly>)
  * [Docker](</id/install/docker>)
  * [hosting VPS](</id/vps>)


Was this useful?YesNo