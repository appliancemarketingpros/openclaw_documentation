---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/id/install/raspberry-pi
scraped_at: 2026-05-25
---

Jalankan Gateway OpenClaw yang persisten dan selalu aktif di Raspberry Pi. Karena Pi hanya berfungsi sebagai gateway (model berjalan di cloud melalui API), bahkan Pi sederhana dapat menangani beban kerja dengan baik — biaya perangkat keras biasanya **$35–80 sekali bayar** , tanpa biaya bulanan.

## Kompatibilitas perangkat keras

Model Pi | RAM | Berfungsi? | Catatan  
---|---|---|---  
Pi 5 | 4/8 GB | Terbaik | Paling cepat, direkomendasikan.  
Pi 4 | 4 GB | Baik | Pilihan ideal untuk sebagian besar pengguna.  
Pi 4 | 2 GB | Oke | Tambahkan swap.  
Pi 4 | 1 GB | Terbatas | Memungkinkan dengan swap, konfigurasi minimal.  
Pi 3B+ | 1 GB | Lambat | Berfungsi tetapi terasa lamban.  
Pi Zero 2 W | 512 MB | Tidak | Tidak direkomendasikan.  
  
**Minimum:** RAM 1 GB, 1 core, disk kosong 500 MB, OS 64-bit. **Direkomendasikan:** RAM 2 GB+, kartu SD 16 GB+ (atau SSD USB), Ethernet.

## Prasyarat

  * Raspberry Pi 4 atau 5 dengan RAM 2 GB+ (4 GB direkomendasikan)
  * Kartu MicroSD (16 GB+) atau SSD USB (performa lebih baik)
  * Catu daya Pi resmi
  * Koneksi jaringan (Ethernet atau WiFi)
  * Raspberry Pi OS 64-bit (wajib -- jangan gunakan 32-bit)
  * Sekitar 30 menit


## Penyiapan

* ### Flash OS

Gunakan **Raspberry Pi OS Lite (64-bit)** \-- desktop tidak diperlukan untuk server headless.

  1. Unduh [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>).
  2. Pilih OS: **Raspberry Pi OS Lite (64-bit)**.
  3. Di dialog pengaturan, prakonfigurasikan: 
     * Hostname: `gateway-host`
     * Aktifkan SSH
     * Atur nama pengguna dan kata sandi
     * Konfigurasikan WiFi (jika tidak menggunakan Ethernet)
  4. Flash ke kartu SD atau drive USB Anda, masukkan, lalu boot Pi.


* ### Hubungkan via SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Perbarui sistem

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Instal Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Tambahkan swap (penting untuk 2 GB atau kurang)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### Instal OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Ikuti wizard. Kunci API direkomendasikan dibanding OAuth untuk perangkat headless. Telegram adalah kanal termudah untuk memulai.

* ### Verifikasi

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Akses Control UI

Di komputer Anda, dapatkan URL dasbor dari Pi:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Lalu buat tunnel SSH di terminal lain:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Buka URL yang dicetak di browser lokal Anda. Untuk akses jarak jauh yang selalu aktif, lihat [integrasi Tailscale](</id/gateway/tailscale>).

## Tips performa

**Gunakan SSD USB** \-- Kartu SD lambat dan cepat aus. SSD USB meningkatkan performa secara drastis. Lihat [panduan boot USB Pi](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>).

**Aktifkan cache kompilasi modul** \-- Mempercepat pemanggilan CLI berulang di host Pi berdaya lebih rendah:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Kurangi penggunaan memori** \-- Untuk penyiapan headless, kosongkan memori GPU dan nonaktifkan layanan yang tidak digunakan:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**Drop-in systemd untuk restart stabil** \-- Jika Pi ini terutama menjalankan OpenClaw, tambahkan drop-in layanan:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Lalu `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`. Pada Pi headless, aktifkan juga lingering sekali agar layanan pengguna tetap bertahan setelah logout: `sudo loginctl enable-linger "$(whoami)"`.

## Penyiapan model yang direkomendasikan

Karena Pi hanya menjalankan gateway, gunakan model API yang di-host di cloud:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Jangan jalankan LLM lokal di Pi — bahkan model kecil terlalu lambat untuk berguna. Biarkan Claude atau GPT menangani pekerjaan model.

## Catatan biner ARM

Sebagian besar fitur OpenClaw berfungsi di ARM64 tanpa perubahan (Node.js, Telegram, WhatsApp/Baileys, Chromium). Biner yang sesekali tidak memiliki build ARM biasanya adalah alat CLI Go/Rust opsional yang dikirim oleh skills. Verifikasi halaman rilis biner yang hilang untuk artefak `linux-arm64` / `aarch64` sebelum beralih ke build dari sumber.

## Persistensi dan pencadangan

Status OpenClaw berada di bawah:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` per agen, status kanal/penyedia, sesi.
  * `~/.openclaw/workspace/` — ruang kerja agen ([SOUL.md](<http://SOUL.md>), memori, artefak).


Ini tetap bertahan setelah reboot. Ambil snapshot portabel dengan:

bashCopy code
[code]
    openclaw backup create
[/code]

Jika Anda menyimpannya di SSD, performa dan umur pakai akan meningkat dibanding kartu SD.

## Pemecahan masalah

**Kehabisan memori** \-- Verifikasi swap aktif dengan `free -h`. Nonaktifkan layanan yang tidak digunakan (`sudo systemctl disable cups bluetooth avahi-daemon`). Gunakan hanya model berbasis API.

**Performa lambat** \-- Gunakan SSD USB alih-alih kartu SD. Periksa throttling CPU dengan `vcgencmd get_throttled` (seharusnya mengembalikan `0x0`).

**Layanan tidak dapat dimulai** \-- Periksa log dengan `journalctl --user -u openclaw-gateway.service --no-pager -n 100` dan jalankan `openclaw doctor --non-interactive`. Jika ini Pi headless, verifikasi juga bahwa lingering diaktifkan: `sudo loginctl enable-linger "$(whoami)"`.

**Masalah biner ARM** \-- Jika skill gagal dengan "exec format error", periksa apakah biner memiliki build ARM64. Verifikasi arsitektur dengan `uname -m` (seharusnya menampilkan `aarch64`).

**WiFi terputus** \-- Nonaktifkan manajemen daya WiFi: `sudo iwconfig wlan0 power off`.

## Langkah berikutnya

  * [Kanal](</id/channels>) \-- hubungkan Telegram, WhatsApp, Discord, dan lainnya
  * [Konfigurasi Gateway](</id/gateway/configuration>) \-- semua opsi konfigurasi
  * [Memperbarui](</id/install/updating>) \-- jaga OpenClaw tetap terbaru


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Server Linux](</id/vps>)
  * [Platform](</id/platforms>)


Was this useful?YesNo