---
title: Pemecahan masalah peramban
source_url: https://docs.openclaw.ai/id/tools/browser-linux-troubleshooting
scraped_at: 2026-05-25
---

## Masalah: "Gagal memulai Chrome CDP pada port 18800"

Server kontrol browser OpenClaw gagal meluncurkan Chrome/Brave/Edge/Chromium dengan galat:

CodeCopy code
[code]
    {"error":"Error: Failed to start Chrome CDP on port 18800 for profile \"openclaw\"."}
[/code]

### Akar penyebab

Di Ubuntu (dan banyak distro Linux), instalasi Chromium bawaan adalah **paket snap**. Pembatasan AppArmor milik Snap mengganggu cara OpenClaw memunculkan dan memantau proses browser.

Perintah `apt install chromium` memasang paket stub yang mengalihkan ke snap:

CodeCopy code
[code]
    Note, selecting 'chromium-browser' instead of 'chromium'chromium-browser is already the newest version (2:1snap1-0ubuntu2).
[/code]

Ini BUKAN browser sungguhan - hanya sebuah wrapper.

Kegagalan peluncuran Linux umum lainnya:

  * `The profile appears to be in use by another Chromium process` berarti Chrome menemukan berkas kunci `Singleton*` usang di direktori profil terkelola. OpenClaw menghapus kunci tersebut dan mencoba sekali lagi ketika kunci menunjuk ke proses yang sudah mati atau host yang berbeda.
  * `Missing X server or $DISPLAY` berarti browser terlihat diminta secara eksplisit pada host tanpa sesi desktop. Secara default, profil lokal terkelola sekarang kembali ke mode headless di Linux ketika `DISPLAY` dan `WAYLAND_DISPLAY` sama-sama tidak disetel. Jika Anda menyetel `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless: false`, atau `browser.profiles.<name>.headless: false`, hapus override headed tersebut, setel `OPENCLAW_BROWSER_HEADLESS=1`, mulai `Xvfb`, jalankan `openclaw browser start --headless` untuk peluncuran terkelola sekali jalan, atau jalankan OpenClaw dalam sesi desktop sungguhan.


### Solusi 1: Pasang Google Chrome (Direkomendasikan)

Pasang paket resmi Google Chrome `.deb`, yang tidak di-sandbox oleh snap:

bashCopy code
[code]
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debsudo dpkg -i google-chrome-stable_current_amd64.debsudo apt --fix-broken install -y  # if there are dependency errors
[/code]

Lalu perbarui konfigurasi OpenClaw Anda (`~/.openclaw/openclaw.json`):

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "executablePath": "/usr/bin/google-chrome-stable",    "headless": true,    "noSandbox": true  }}
[/code]

### Solusi 2: Gunakan Snap Chromium dengan Mode Hanya-Attach

Jika Anda harus menggunakan snap Chromium, konfigurasikan OpenClaw untuk attach ke browser yang dimulai secara manual:

  1. Perbarui konfigurasi:

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "attachOnly": true,    "headless": true,    "noSandbox": true  }}
[/code]

  2. Mulai Chromium secara manual:

bashCopy code
[code]
    chromium-browser --headless --no-sandbox --disable-gpu \  --remote-debugging-port=18800 \  --user-data-dir=$HOME/.openclaw/browser/openclaw/user-data \  about:blank &
[/code]

  3. Secara opsional, buat layanan pengguna systemd untuk memulai Chrome otomatis:

iniCopy code
[code]
    # ~/.config/systemd/user/openclaw-browser.service[Unit]Description=OpenClaw Browser (Chrome CDP)After=network.target [Service]ExecStart=/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=18800 --user-data-dir=%h/.openclaw/browser/openclaw/user-data about:blankRestart=on-failureRestartSec=5 [Install]WantedBy=default.target
[/code]

Aktifkan dengan: `systemctl --user enable --now openclaw-browser.service`

### Memverifikasi Browser Berfungsi

Periksa status:

bashCopy code
[code]
    curl -s http://127.0.0.1:18791/ | jq '{running, pid, chosenBrowser}'
[/code]

Uji penjelajahan:

bashCopy code
[code]
    curl -s -X POST http://127.0.0.1:18791/startcurl -s http://127.0.0.1:18791/tabs
[/code]

### Referensi konfigurasi

Opsi | Deskripsi | Bawaan  
---|---|---  
`browser.enabled` | Aktifkan kontrol browser | `true`  
`browser.executablePath` | Path ke biner browser berbasis Chromium (Chrome/Brave/Edge/Chromium) | terdeteksi otomatis (mengutamakan browser bawaan jika berbasis Chromium)  
`browser.headless` | Jalankan tanpa GUI | `false`  
`OPENCLAW_BROWSER_HEADLESS` | Override per proses untuk mode headless browser lokal terkelola | tidak disetel  
`browser.noSandbox` | Tambahkan flag `--no-sandbox` (diperlukan untuk sebagian setup Linux) | `false`  
`browser.attachOnly` | Jangan luncurkan browser, hanya attach ke yang sudah ada | `false`  
`browser.cdpPort` | Port Chrome DevTools Protocol | `18800`  
`browser.localLaunchTimeoutMs` | Timeout penemuan Chrome lokal terkelola | `15000`  
`browser.localCdpReadyTimeoutMs` | Timeout kesiapan CDP setelah peluncuran lokal terkelola | `8000`  
  
Pada Raspberry Pi, host VPS lama, atau penyimpanan lambat, naikkan `browser.localLaunchTimeoutMs` ketika Chrome memerlukan lebih banyak waktu untuk mengekspos endpoint HTTP CDP-nya. Naikkan `browser.localCdpReadyTimeoutMs` ketika peluncuran berhasil tetapi `openclaw browser start` masih melaporkan `not reachable after start`. Nilai harus berupa bilangan bulat positif hingga `120000` ms; nilai konfigurasi yang tidak valid akan ditolak.

### Masalah: "Tidak ada tab Chrome yang ditemukan untuk profile="user""

Anda menggunakan profil `existing-session` / Chrome MCP. OpenClaw dapat melihat Chrome lokal, tetapi tidak ada tab terbuka yang tersedia untuk di-attach.

Opsi perbaikan:

  1. **Gunakan browser terkelola:** `openclaw browser start --browser-profile openclaw` (atau setel `browser.defaultProfile: "openclaw"`).
  2. **Gunakan Chrome MCP:** pastikan Chrome lokal berjalan dengan setidaknya satu tab terbuka, lalu coba lagi dengan `--browser-profile user`.


Catatan:

  * `user` hanya untuk host lokal. Untuk server Linux, kontainer, atau host jarak jauh, utamakan profil CDP.
  * Profil `user` / `existing-session` lainnya mempertahankan batasan Chrome MCP saat ini: aksi berbasis ref, hook unggah satu berkas, tanpa override timeout dialog, tanpa `wait --load networkidle`, dan tanpa `responsebody`, ekspor PDF, intersepsi unduhan, atau aksi batch.
  * Profil `openclaw` lokal menetapkan otomatis `cdpPort`/`cdpUrl`; hanya setel itu untuk CDP jarak jauh.
  * Profil CDP jarak jauh menerima `http://`, `https://`, `ws://`, dan `wss://`. Gunakan HTTP(S) untuk penemuan `/json/version`, atau WS(S) ketika layanan browser Anda memberi URL soket DevTools langsung.


## Terkait

  * [Browser](</id/tools/browser>)
  * [Login browser](</id/tools/browser-login>)
  * [Pemecahan masalah Browser WSL2](</id/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo