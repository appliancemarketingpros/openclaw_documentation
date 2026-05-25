---
title: Akses jarak jauh
source_url: https://docs.openclaw.ai/id/gateway/remote
scraped_at: 2026-05-25
---

Repo ini mendukung "jarak jauh lewat SSH" dengan menjaga satu Gateway (master) berjalan di host khusus (desktop/server) dan menghubungkan klien ke sana.

  * Untuk **operator (Anda / aplikasi macOS)** : tunneling SSH adalah fallback universal.
  * Untuk **node (iOS/Android dan perangkat masa depan)** : hubungkan ke **WebSocket** Gateway (LAN/tailnet atau tunnel SSH sesuai kebutuhan).


## Ide inti

  * WebSocket Gateway melakukan bind ke **loopback** pada port yang Anda konfigurasikan (default ke 18789).
  * Untuk penggunaan jarak jauh, Anda meneruskan port loopback itu lewat SSH (atau menggunakan tailnet/VPN dan lebih sedikit tunnel).


## Pengaturan VPN dan tailnet umum

Anggap **host Gateway** sebagai tempat agen hidup. Host ini memiliki sesi, profil auth, channel, dan state. Laptop, desktop, dan node Anda terhubung ke host itu.

### Gateway selalu aktif di tailnet Anda

Jalankan Gateway pada host persisten (VPS atau server rumah) dan jangkau melalui **Tailscale** atau SSH.

  * **UX terbaik:** pertahankan `gateway.bind: "loopback"` dan gunakan **Tailscale Serve** untuk UI Kontrol.
  * **Fallback:** pertahankan loopback plus tunnel SSH dari mesin mana pun yang memerlukan akses.
  * **Contoh:** [exe.dev](</id/install/exe-dev>) (VM mudah) atau [Hetzner](</id/install/hetzner>) (VPS produksi).


Ideal ketika laptop Anda sering tidur tetapi Anda ingin agen selalu aktif.

### Desktop rumah menjalankan Gateway

Laptop **tidak** menjalankan agen. Laptop terhubung dari jarak jauh:

  * Gunakan mode **Jarak jauh lewat SSH** aplikasi macOS (Pengaturan → Umum → OpenClaw berjalan).
  * Aplikasi membuka dan mengelola tunnel, sehingga WebChat dan pemeriksaan kesehatan langsung berfungsi.


Runbook: [akses jarak jauh macOS](</id/platforms/mac/remote>).

### Laptop menjalankan Gateway

Pertahankan Gateway lokal tetapi ekspos dengan aman:

  * Tunnel SSH ke laptop dari mesin lain, atau
  * Tailscale Serve UI Kontrol dan pertahankan Gateway hanya loopback.


Panduan: [Tailscale](</id/gateway/tailscale>) dan [ikhtisar Web](</id/web>).

## Alur perintah (apa yang berjalan di mana)

Satu layanan gateway memiliki state + channel. Node adalah periferal.

Contoh alur (Telegram → node):

  * Pesan Telegram tiba di **Gateway**.
  * Gateway menjalankan **agen** dan memutuskan apakah akan memanggil tool node.
  * Gateway memanggil **node** melalui WebSocket Gateway (RPC `node.*`).
  * Node mengembalikan hasil; Gateway membalas kembali ke Telegram.


Catatan:

  * **Node tidak menjalankan layanan gateway.** Hanya satu gateway yang seharusnya berjalan per host kecuali Anda sengaja menjalankan profil terisolasi (lihat [Beberapa gateway](</id/gateway/multiple-gateways>)).
  * "Mode node" aplikasi macOS hanyalah klien node melalui WebSocket Gateway.


## Tunnel SSH (CLI + tool)

Buat tunnel lokal ke WS Gateway jarak jauh:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Dengan tunnel aktif:

  * `openclaw health` dan `openclaw status --deep` sekarang menjangkau gateway jarak jauh melalui `ws://127.0.0.1:18789`.
  * `openclaw gateway status`, `openclaw gateway health`, `openclaw gateway probe`, dan `openclaw gateway call` juga dapat menargetkan URL yang diteruskan melalui `--url` bila diperlukan.


## Default jarak jauh CLI

Anda dapat menyimpan target jarak jauh agar perintah CLI menggunakannya secara default:

json5Copy code
[code]
    {  gateway: {    mode: "remote",    remote: {      url: "ws://127.0.0.1:18789",      token: "your-token",    },  },}
[/code]

Saat gateway hanya loopback, pertahankan URL di `ws://127.0.0.1:18789` dan buka tunnel SSH terlebih dahulu. Dalam transport tunnel SSH aplikasi macOS, hostname gateway yang ditemukan berada di `gateway.remote.sshTarget`; `gateway.remote.url` tetap menjadi URL tunnel lokal.

## Prioritas kredensial

Resolusi kredensial Gateway mengikuti satu kontrak bersama di seluruh path call/probe/status dan pemantauan persetujuan eksekusi Discord. Node-host menggunakan kontrak dasar yang sama dengan satu pengecualian mode lokal (ia sengaja mengabaikan `gateway.remote.*`):

  * Kredensial eksplisit (`--token`, `--password`, atau tool `gatewayToken`) selalu menang pada path call yang menerima auth eksplisit.
  * Keamanan override URL: 
    * Override URL CLI (`--url`) tidak pernah menggunakan ulang kredensial config/env implisit.
    * Override URL env (`OPENCLAW_GATEWAY_URL`) hanya boleh menggunakan kredensial env (`OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`).
  * Default mode lokal: 
    * token: `OPENCLAW_GATEWAY_TOKEN` -> `gateway.auth.token` -> `gateway.remote.token` (fallback jarak jauh hanya berlaku ketika input token auth lokal belum disetel)
    * password: `OPENCLAW_GATEWAY_PASSWORD` -> `gateway.auth.password` -> `gateway.remote.password` (fallback jarak jauh hanya berlaku ketika input password auth lokal belum disetel)
  * Default mode jarak jauh: 
    * token: `gateway.remote.token` -> `OPENCLAW_GATEWAY_TOKEN` -> `gateway.auth.token`
    * password: `OPENCLAW_GATEWAY_PASSWORD` -> `gateway.remote.password` -> `gateway.auth.password`
  * Pengecualian mode lokal node-host: `gateway.remote.token` / `gateway.remote.password` diabaikan.
  * Pemeriksaan token probe/status jarak jauh bersifat ketat secara default: pemeriksaan tersebut hanya menggunakan `gateway.remote.token` (tanpa fallback token lokal) saat menargetkan mode jarak jauh.
  * Override env Gateway hanya menggunakan `OPENCLAW_GATEWAY_*`.


## UI Chat lewat SSH

WebChat tidak lagi menggunakan port HTTP terpisah. UI chat SwiftUI terhubung langsung ke WebSocket Gateway.

  * Teruskan `18789` lewat SSH (lihat di atas), lalu hubungkan klien ke `ws://127.0.0.1:18789`.
  * Di macOS, pilih mode "Jarak jauh lewat SSH" aplikasi, yang mengelola tunnel secara otomatis.


## Jarak Jauh lewat SSH aplikasi macOS

Aplikasi bilah menu macOS dapat menjalankan pengaturan yang sama dari awal sampai akhir (pemeriksaan status jarak jauh, WebChat, dan penerusan Voice Wake).

Runbook: [akses jarak jauh macOS](</id/platforms/mac/remote>).

## Aturan keamanan (jarak jauh/VPN)

Versi singkat: **pertahankan Gateway hanya loopback** kecuali Anda yakin memerlukan bind.

  * **Loopback + SSH/Tailscale Serve** adalah default paling aman (tanpa eksposur publik).
  * Plaintext `ws://` hanya loopback secara default. Untuk jaringan privat tepercaya, setel `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` pada proses klien sebagai break-glass. Tidak ada padanan `openclaw.json`; ini harus menjadi environment proses untuk klien yang membuat koneksi WebSocket.
  * **Bind non-loopback** (`lan`/`tailnet`/`custom`, atau `auto` saat loopback tidak tersedia) harus menggunakan auth gateway: token, password, atau reverse proxy yang sadar identitas dengan `gateway.auth.mode: "trusted-proxy"`.
  * `gateway.remote.token` / `.password` adalah sumber kredensial klien. Keduanya **tidak** mengonfigurasi auth server dengan sendirinya.
  * Path call lokal dapat menggunakan `gateway.remote.*` sebagai fallback hanya ketika `gateway.auth.*` belum disetel.
  * Jika `gateway.auth.token` / `gateway.auth.password` dikonfigurasi secara eksplisit melalui SecretRef dan tidak terselesaikan, resolusi gagal tertutup (tanpa masking fallback jarak jauh).
  * `gateway.remote.tlsFingerprint` melakukan pin pada sertifikat TLS jarak jauh saat menggunakan `wss://`.
  * **Tailscale Serve** dapat mengautentikasi traffic UI Kontrol/WebSocket melalui header identitas ketika `gateway.auth.allowTailscale: true`; endpoint API HTTP tidak menggunakan auth header Tailscale itu dan sebagai gantinya mengikuti mode auth HTTP normal gateway. Alur tanpa token ini mengasumsikan host gateway tepercaya. Setel ke `false` jika Anda menginginkan auth rahasia bersama di semua tempat.
  * Auth **trusted-proxy** mengharapkan pengaturan proxy sadar identitas non-loopback secara default. Reverse proxy loopback di host yang sama memerlukan `gateway.auth.trustedProxy.allowLoopback = true` secara eksplisit.
  * Perlakukan kontrol browser seperti akses operator: hanya tailnet + pairing node yang disengaja.


Pembahasan mendalam: [Keamanan](</id/gateway/security>).

### macOS: tunnel SSH persisten melalui LaunchAgent

Untuk klien macOS yang terhubung ke gateway jarak jauh, pengaturan persisten termudah menggunakan entri konfigurasi SSH `LocalForward` plus LaunchAgent untuk menjaga tunnel tetap hidup melewati reboot dan crash.

#### Langkah 1: tambahkan config SSH

Edit `~/.ssh/config`:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;    User &lt;REMOTE_USER&gt;    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Ganti `&lt;REMOTE_IP&gt;` dan `&lt;REMOTE_USER&gt;` dengan nilai Anda.

#### Langkah 2: salin key SSH (sekali saja)

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

#### Langkah 3: konfigurasikan token gateway

Simpan token dalam config agar tetap ada setelah restart:

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

#### Langkah 4: buat LaunchAgent

Simpan ini sebagai `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

#### Langkah 5: muat LaunchAgent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Tunnel akan dimulai otomatis saat login, restart saat crash, dan menjaga port yang diteruskan tetap aktif.

#### Pemecahan masalah

Periksa apakah tunnel berjalan:

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

Restart tunnel:

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

Hentikan tunnel:

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

Entri config | Apa yang dilakukannya  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Meneruskan port lokal 18789 ke port jarak jauh 18789  
`ssh -N` | SSH tanpa menjalankan perintah jarak jauh (hanya penerusan port)  
`KeepAlive` | Otomatis me-restart tunnel jika crash  
`RunAtLoad` | Memulai tunnel saat LaunchAgent dimuat saat login  
  
## Terkait

  * [Tailscale](</id/gateway/tailscale>)
  * [Autentikasi](</id/gateway/authentication>)
  * [Pengaturan gateway jarak jauh](</id/gateway/remote-gateway-readme>)


Was this useful?YesNo