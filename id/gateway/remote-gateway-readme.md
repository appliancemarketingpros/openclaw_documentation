---
title: Penyiapan Gateway jarak jauh
source_url: https://docs.openclaw.ai/id/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Konten ini telah digabungkan ke [Akses Jarak Jauh](</id/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Lihat halaman tersebut untuk panduan saat ini.

# Menjalankan OpenClaw.app dengan Gateway Jarak Jauh

OpenClaw.app menggunakan tunneling SSH untuk terhubung ke gateway jarak jauh. Panduan ini menunjukkan cara menyiapkannya.

## Ikhtisar
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Penyiapan cepat

### Langkah 1: Tambahkan Konfigurasi SSH

Edit `~/.ssh/config` dan tambahkan:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Ganti `&lt;REMOTE_IP&gt;` dan `&lt;REMOTE_USER&gt;` dengan nilai Anda.

### Langkah 2: Salin Kunci SSH

Salin kunci publik Anda ke mesin jarak jauh (masukkan kata sandi sekali):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Langkah 3: Konfigurasikan Autentikasi Gateway Jarak Jauh

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Gunakan `gateway.remote.password` sebagai gantinya jika gateway jarak jauh Anda menggunakan autentikasi kata sandi. `OPENCLAW_GATEWAY_TOKEN` masih valid sebagai override tingkat shell, tetapi penyiapan klien jarak jauh yang tahan lama adalah `gateway.remote.token` / `gateway.remote.password`.

### Langkah 4: Mulai Tunnel SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Langkah 5: Mulai Ulang OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

Aplikasi sekarang akan terhubung ke gateway jarak jauh melalui tunnel SSH.

* * *

## Mulai Otomatis Tunnel saat Login

Agar tunnel SSH dimulai otomatis saat Anda login, buat Launch Agent.

### Buat file PLIST

Simpan ini sebagai `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Muat Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Tunnel sekarang akan:

  * Dimulai otomatis saat Anda login
  * Dimulai ulang jika crash
  * Tetap berjalan di latar belakang


Catatan lama: hapus LaunchAgent `com.openclaw.ssh-tunnel` yang tersisa jika ada.

* * *

## Pemecahan masalah

**Periksa apakah tunnel sedang berjalan:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Mulai ulang tunnel:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Hentikan tunnel:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Cara kerjanya

Komponen | Apa Fungsinya  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Meneruskan port lokal 18789 ke port jarak jauh 18789  
`ssh -N` | SSH tanpa menjalankan perintah jarak jauh (hanya penerusan port)  
`KeepAlive` | Memulai ulang tunnel secara otomatis jika crash  
`RunAtLoad` | Memulai tunnel saat agen dimuat  
  
OpenClaw.app terhubung ke `ws://127.0.0.1:18789` di mesin klien Anda. Tunnel SSH meneruskan koneksi tersebut ke port 18789 pada mesin jarak jauh tempat Gateway berjalan.

## Terkait

  * [Akses jarak jauh](</id/gateway/remote>)
  * [Tailscale](</id/gateway/tailscale>)


Was this useful?YesNo