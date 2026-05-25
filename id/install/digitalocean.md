---
title: DigitalOcean
source_url: https://docs.openclaw.ai/id/install/digitalocean
scraped_at: 2026-05-25
---

Jalankan OpenClaw Gateway persisten di DigitalOcean Droplet (~$6/bulan untuk paket Basic 1 GB).

DigitalOcean adalah jalur VPS berbayar paling sederhana. Jika Anda lebih memilih opsi yang lebih murah atau gratis:

  * [Hetzner](</id/install/hetzner>) — €3,79/bln, lebih banyak core/RAM per dolar.
  * [Oracle Cloud](</id/install/oracle>) — ARM Always Free (hingga 4 OCPU, RAM 24 GB), tetapi pendaftarannya bisa rumit dan hanya ARM.


## Prasyarat

  * Akun DigitalOcean ([daftar](<https://cloud.digitalocean.com/registrations/new>))
  * Pasangan kunci SSH (atau bersedia menggunakan autentikasi kata sandi)
  * Sekitar 20 menit


## Penyiapan

* ### Create a Droplet

  1. Masuk ke [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Klik **Create > Droplets**.
  3. Pilih: 
     * **Wilayah:** Yang terdekat dengan Anda
     * **Image:** Ubuntu 24.04 LTS
     * **Ukuran:** Basic, Regular, 1 vCPU / RAM 1 GB / SSD 25 GB
     * **Autentikasi:** Kunci SSH (direkomendasikan) atau kata sandi
  4. Klik **Create Droplet** dan catat alamat IP-nya.


* ### Connect and install

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Gunakan shell root hanya untuk bootstrap sistem. Jalankan perintah OpenClaw sebagai pengguna non-root `openclaw` agar state berada di bawah `/home/openclaw/.openclaw/` dan Gateway dipasang sebagai layanan systemd milik pengguna tersebut.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Wizard memandu Anda melalui autentikasi model, penyiapan channel, pembuatan token gateway, dan pemasangan daemon (systemd).

* ### Add swap (recommended for 1 GB Droplets)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Verify the gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Access the Control UI

Gateway terikat ke loopback secara default. Pilih salah satu opsi ini.

**Opsi A: Tunnel SSH (paling sederhana)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Lalu buka `http://localhost:18789`.

**Opsi B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Lalu buka `https://<magicdns>/` dari perangkat apa pun di tailnet Anda.

Tailscale Serve mengautentikasi lalu lintas UI Kontrol dan WebSocket melalui header identitas tailnet, yang mengasumsikan host gateway itu sendiri tepercaya. Endpoint HTTP API tetap mengikuti mode autentikasi normal gateway (token/kata sandi). Untuk mewajibkan kredensial rahasia bersama eksplisit melalui Serve, setel `gateway.auth.allowTailscale: false` dan gunakan `gateway.auth.mode: "token"` atau `"password"`.

**Opsi C: Bind tailnet (tanpa Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Lalu buka `http://<tailscale-ip>:18789` (token diperlukan).

## Persistensi dan cadangan

State OpenClaw berada di bawah:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` per agen, state channel/provider, dan data sesi.
  * `~/.openclaw/workspace/` — workspace agen ([SOUL.md](<http://SOUL.md>), memori, artefak).


Ini bertahan setelah Droplet reboot. Untuk mengambil snapshot portabel:

bashCopy code
[code]
    openclaw backup create
[/code]

Snapshot DigitalOcean mencadangkan seluruh Droplet; `openclaw backup create` portabel lintas host.

## Tips RAM 1 GB

Droplet $6 hanya memiliki RAM 1 GB. Agar semuanya tetap lancar:

  * Pastikan langkah swap di atas ada di `/etc/fstab` agar bertahan setelah reboot.
  * Pilih model berbasis API (Claude, GPT) daripada model lokal — inferensi LLM lokal tidak muat di 1 GB.
  * Setel `agents.defaults.model.primary` ke model yang lebih kecil jika Anda mengalami OOM pada prompt besar.
  * Pantau dengan `free -h` dan `htop`.


## Pemecahan masalah

**Gateway tidak bisa dimulai** \-- Jalankan `openclaw doctor --non-interactive` dan periksa log dengan `journalctl --user -u openclaw-gateway.service -n 50`.

**Port sudah digunakan** \-- Jalankan `lsof -i :18789` untuk menemukan prosesnya, lalu hentikan.

**Kehabisan memori** \-- Verifikasi swap aktif dengan `free -h`. Jika masih mengalami OOM, gunakan model berbasis API (Claude, GPT) alih-alih model lokal, atau tingkatkan ke Droplet 2 GB.

## Langkah berikutnya

  * [Channel](</id/channels>) \-- hubungkan Telegram, WhatsApp, Discord, dan lainnya
  * [Konfigurasi Gateway](</id/gateway/configuration>) \-- semua opsi konfigurasi
  * [Memperbarui](</id/install/updating>) \-- jaga OpenClaw tetap mutakhir


## Terkait

  * [Ringkasan instalasi](</id/install>)
  * [Fly.io](</id/install/fly>)
  * [Hetzner](</id/install/hetzner>)
  * [Hosting VPS](</id/vps>)


Was this useful?YesNo