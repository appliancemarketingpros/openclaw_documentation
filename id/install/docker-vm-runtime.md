---
title: Runtime VM Docker
source_url: https://docs.openclaw.ai/id/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Langkah runtime bersama untuk instalasi Docker berbasis VM seperti GCP, Hetzner, dan penyedia VPS serupa.

## Masukkan biner yang diperlukan ke dalam image

Menginstal biner di dalam container yang sedang berjalan adalah jebakan. Apa pun yang diinstal saat runtime akan hilang saat restart.

Semua biner eksternal yang diperlukan oleh Skills harus diinstal saat image dibangun.

Contoh di bawah hanya menampilkan tiga biner umum:

  * `gog` (dari `gogcli`) untuk akses Gmail
  * `goplaces` untuk Google Places
  * `wacli` untuk WhatsApp


Ini adalah contoh, bukan daftar lengkap. Anda dapat menginstal biner sebanyak yang diperlukan dengan pola yang sama.

Jika nanti Anda menambahkan Skills baru yang bergantung pada biner tambahan, Anda harus:

  1. Memperbarui Dockerfile
  2. Membangun ulang image
  3. Me-restart container


**Contoh Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Bangun dan jalankan

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Jika build gagal dengan `Killed` atau `exit code 137` selama `pnpm install --frozen-lockfile`, VM kehabisan memori. Gunakan kelas mesin yang lebih besar sebelum mencoba lagi.

Verifikasi biner:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Keluaran yang diharapkan:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Verifikasi Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Keluaran yang diharapkan:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Apa yang persisten di mana

OpenClaw berjalan di Docker, tetapi Docker bukan sumber kebenaran. Semua state jangka panjang harus bertahan melewati restart, rebuild, dan reboot.

Komponen | Lokasi | Mekanisme persistensi | Catatan  
---|---|---|---  
Konfigurasi Gateway | `/home/node/.openclaw/` | Mount volume host | Mencakup `openclaw.json`, `.env`  
Profil autentikasi model | `/home/node/.openclaw/agents/` | Mount volume host | `agents/<agentId>/agent/auth-profiles.json` (OAuth, kunci API)  
Kunci profil autentikasi | `/home/node/.config/openclaw/` | Mount volume host | Kunci enkripsi lokal untuk material token profil autentikasi OAuth  
Konfigurasi Skills | `/home/node/.openclaw/skills/` | Mount volume host | State tingkat Skill  
Ruang kerja agen | `/home/node/.openclaw/workspace/` | Mount volume host | Kode dan artefak agen  
Sesi WhatsApp | `/home/node/.openclaw/` | Mount volume host | Mempertahankan login QR  
Keyring Gmail | `/home/node/.openclaw/` | Volume host + kata sandi | Memerlukan `GOG_KEYRING_PASSWORD`  
Paket Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Mount volume host | Root paket Plugin yang dapat diunduh  
Biner eksternal | `/usr/local/bin/` | Image Docker | Harus dimasukkan saat build  
Runtime Node | Sistem berkas container | Image Docker | Dibangun ulang setiap build image  
Paket OS | Sistem berkas container | Image Docker | Jangan instal saat runtime  
Container Docker | Sementara | Dapat di-restart | Aman untuk dihancurkan  
  
## Pembaruan

Untuk memperbarui OpenClaw di VM:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Terkait

  * [Docker](</id/install/docker>)
  * [Podman](</id/install/podman>)
  * [ClawDock](</id/install/clawdock>)


Was this useful?YesNo