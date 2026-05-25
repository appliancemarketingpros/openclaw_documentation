---
title: Fly.io
source_url: https://docs.openclaw.ai/id/install/fly
scraped_at: 2026-05-25
---

**Tujuan:** OpenClaw Gateway berjalan di mesin [Fly.io](<https://fly.io>) dengan penyimpanan persisten, HTTPS otomatis, dan akses Discord/saluran.

## Yang Anda perlukan

  * [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>) terpasang
  * Akun [Fly.io](<http://Fly.io>) (tingkat gratis dapat digunakan)
  * Autentikasi model: kunci API untuk penyedia model pilihan Anda
  * Kredensial saluran: token bot Discord, token Telegram, dll.


## Jalur cepat pemula

  1. Klon repo → sesuaikan `fly.toml`
  2. Buat aplikasi + volume → atur secret
  3. Deploy dengan `fly deploy`
  4. SSH masuk untuk membuat konfigurasi atau gunakan Control UI


* ### Create the Fly app

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Tips:** Pilih region yang dekat dengan Anda. Opsi umum: `lhr` (London), `iad` (Virginia), `sjc` (San Jose).

* ### Configure fly.toml

Edit `fly.toml` agar sesuai dengan nama aplikasi dan kebutuhan Anda.

**Catatan keamanan:** Konfigurasi default mengekspos URL publik. Untuk deployment yang diperkuat tanpa IP publik, lihat Deployment privat atau gunakan `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

Image Docker OpenClaw menggunakan `tini` sebagai titik masuknya. Perintah proses Fly menggantikan Docker `CMD` tanpa menggantikan `ENTRYPOINT`, sehingga proses tetap berjalan di bawah `tini`.

**Pengaturan utama:**

Pengaturan | Alasan  
---|---  
`--bind lan` | Mengikat ke `0.0.0.0` agar proxy Fly dapat menjangkau gateway  
`--allow-unconfigured` | Memulai tanpa file konfigurasi (Anda akan membuatnya setelah itu)  
`internal_port = 3000` | Harus cocok dengan `--port 3000` (atau `OPENCLAW_GATEWAY_PORT`) untuk pemeriksaan kesehatan Fly  
`memory = "2048mb"` | 512MB terlalu kecil; 2GB direkomendasikan  
`OPENCLAW_STATE_DIR = "/data"` | Menyimpan state secara persisten pada volume  
* ### Set secrets

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**Catatan:**

  * Bind non-loopback (`--bind lan`) memerlukan jalur autentikasi gateway yang valid. Contoh [Fly.io](<http://Fly.io>) ini menggunakan `OPENCLAW_GATEWAY_TOKEN`, tetapi `gateway.auth.password` atau deployment `trusted-proxy` non-loopback yang dikonfigurasi dengan benar juga memenuhi persyaratan.
  * Perlakukan token ini seperti kata sandi.
  * **Lebih pilih env vars daripada file konfigurasi** untuk semua kunci API dan token. Ini menjaga secret tetap di luar `openclaw.json` agar tidak terekspos atau tercatat secara tidak sengaja.


* ### Deploy

bashCopy code
[code]
    fly deploy
[/code]

Deployment pertama membangun image Docker (~2-3 menit). Deployment berikutnya lebih cepat.

Setelah deployment, verifikasi:

bashCopy code
[code]
    fly statusfly logs
[/code]

Anda seharusnya melihat:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Create config file

SSH masuk ke mesin untuk membuat konfigurasi yang tepat:

bashCopy code
[code]
    fly ssh console
[/code]

Buat direktori dan file konfigurasi:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Catatan:** Dengan `OPENCLAW_STATE_DIR=/data`, path konfigurasi adalah `/data/openclaw.json`.

**Catatan:** Ganti `https://my-openclaw.fly.dev` dengan origin aplikasi Fly Anda yang sebenarnya. Startup Gateway mengisi origin Control UI lokal dari nilai runtime `--bind` dan `--port` sehingga boot pertama dapat berjalan sebelum konfigurasi ada, tetapi akses browser melalui Fly tetap memerlukan origin HTTPS persis yang tercantum di `gateway.controlUi.allowedOrigins`.

**Catatan:** Token Discord dapat berasal dari salah satu:

  * Variabel lingkungan: `DISCORD_BOT_TOKEN` (direkomendasikan untuk secret)
  * File konfigurasi: `channels.discord.token`


Jika menggunakan env var, tidak perlu menambahkan token ke konfigurasi. Gateway membaca `DISCORD_BOT_TOKEN` secara otomatis.

Mulai ulang untuk menerapkan:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Access the Gateway

### Control UI

Buka di browser:

bashCopy code
[code]
    fly open
[/code]

Atau kunjungi `https://my-openclaw.fly.dev/`

Autentikasi dengan secret bersama yang dikonfigurasi. Panduan ini menggunakan token gateway dari `OPENCLAW_GATEWAY_TOKEN`; jika Anda beralih ke autentikasi kata sandi, gunakan kata sandi tersebut sebagai gantinya.

### Log

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### Konsol SSH

bashCopy code
[code]
    fly ssh console
[/code]

## Pemecahan masalah

### "App is not listening on expected address"

Gateway mengikat ke `127.0.0.1` alih-alih `0.0.0.0`.

**Perbaikan:** Tambahkan `--bind lan` ke perintah proses Anda di `fly.toml`.

### Pemeriksaan kesehatan gagal / koneksi ditolak

Fly tidak dapat menjangkau gateway pada port yang dikonfigurasi.

**Perbaikan:** Pastikan `internal_port` cocok dengan port gateway (atur `--port 3000` atau `OPENCLAW_GATEWAY_PORT=3000`).

### OOM / Masalah Memori

Container terus dimulai ulang atau dihentikan. Tanda-tandanya: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration`, atau restart diam-diam.

**Perbaikan:** Tingkatkan memori di `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Atau perbarui mesin yang sudah ada:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Catatan:** 512MB terlalu kecil. 1GB mungkin berfungsi tetapi dapat mengalami OOM saat beban tinggi atau dengan logging verbose. **2GB direkomendasikan.**

### Masalah lock Gateway

Gateway menolak untuk memulai dengan kesalahan "already running".

Ini terjadi ketika container dimulai ulang tetapi file lock PID tetap ada pada volume.

**Perbaikan:** Hapus file lock:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

File lock berada di `/data/gateway.*.lock` (bukan di subdirektori).

### Konfigurasi tidak dibaca

`--allow-unconfigured` hanya melewati penjaga startup. Ini tidak membuat atau memperbaiki `/data/openclaw.json`, jadi pastikan konfigurasi nyata Anda ada dan menyertakan `gateway.mode="local"` ketika Anda menginginkan startup gateway lokal normal.

Verifikasi konfigurasi ada:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Menulis konfigurasi melalui SSH

Perintah `fly ssh console -C` tidak mendukung pengalihan shell. Untuk menulis file konfigurasi:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Catatan:** `fly sftp` mungkin gagal jika file sudah ada. Hapus terlebih dahulu:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### State tidak persisten

Jika Anda kehilangan profil autentikasi, state saluran/penyedia, atau sesi setelah restart, direktori state sedang menulis ke sistem file container.

**Perbaikan:** Pastikan `OPENCLAW_STATE_DIR=/data` diatur di `fly.toml` dan deploy ulang.

## Pembaruan

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Memperbarui perintah mesin

Jika Anda perlu mengubah perintah startup tanpa deployment ulang penuh:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Catatan:** Setelah `fly deploy`, perintah mesin mungkin direset ke yang ada di `fly.toml`. Jika Anda membuat perubahan manual, terapkan ulang setelah deploy.

## Deployment privat (diperkuat)

Secara default, Fly mengalokasikan IP publik, sehingga gateway Anda dapat diakses di `https://your-app.fly.dev`. Ini praktis tetapi berarti deployment Anda dapat ditemukan oleh pemindai internet (Shodan, Censys, dll.).

Untuk deployment yang diperkuat dengan **tanpa paparan publik** , gunakan templat privat.

### Kapan menggunakan deployment privat

  * Anda hanya membuat panggilan/pesan **outbound** (tanpa webhook inbound)
  * Anda menggunakan tunnel **ngrok atau Tailscale** untuk callback webhook apa pun
  * Anda mengakses gateway melalui **SSH, proxy, atau WireGuard** alih-alih browser
  * Anda ingin deployment **tersembunyi dari pemindai internet**


### Penyiapan

Gunakan `deploy/fly.private.toml` alih-alih konfigurasi standar:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Atau konversi deployment yang sudah ada:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

Setelah ini, `fly ips list` seharusnya hanya menampilkan IP bertipe `private`:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Mengakses deployment privat

Karena tidak ada URL publik, gunakan salah satu metode berikut:

**Opsi 1: Proxy lokal (paling sederhana)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Opsi 2: VPN WireGuard**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Opsi 3: SSH saja**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhook dengan deployment privat

Jika Anda memerlukan callback Webhook (Twilio, Telnyx, dll.) tanpa eksposur publik:

  1. **tunnel ngrok** \- Jalankan ngrok di dalam container atau sebagai sidecar
  2. **Tailscale Funnel** \- Ekspos path tertentu melalui Tailscale
  3. **Hanya outbound** \- Beberapa penyedia (Twilio) berfungsi dengan baik untuk panggilan outbound tanpa Webhook


Contoh konfigurasi panggilan suara dengan ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

Tunnel ngrok berjalan di dalam container dan menyediakan URL Webhook publik tanpa mengekspos aplikasi Fly itu sendiri. Atur `webhookSecurity.allowedHosts` ke nama host tunnel publik agar header host yang diteruskan diterima.

### Manfaat keamanan

Aspek | Publik | Privat  
---|---|---  
Pemindai internet | Dapat ditemukan | Tersembunyi  
Serangan langsung | Mungkin | Diblokir  
Akses UI kontrol | Browser | Proxy/VPN  
Pengiriman Webhook | Langsung | Melalui tunnel  
  
## Catatan

  * [Fly.io](<http://Fly.io>) menggunakan **arsitektur x86** (bukan ARM)
  * Dockerfile kompatibel dengan kedua arsitektur
  * Untuk onboarding WhatsApp/Telegram, gunakan `fly ssh console`
  * Data persisten berada pada volume di `/data`
  * Signal memerlukan Java + signal-cli; gunakan image kustom dan pertahankan memori 2GB+.


## Biaya

Dengan konfigurasi yang direkomendasikan (`shared-cpu-2x`, RAM 2GB):

  * ~$10-15/bulan tergantung penggunaan
  * Tingkat gratis mencakup sebagian kuota


Lihat [harga Fly.io](<https://fly.io/docs/about/pricing/>) untuk detail.

## Langkah berikutnya

  * Siapkan kanal pesan: [Kanal](</id/channels>)
  * Konfigurasi Gateway: [Konfigurasi Gateway](</id/gateway/configuration>)
  * Jaga OpenClaw tetap terbaru: [Memperbarui](</id/install/updating>)


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Hetzner](</id/install/hetzner>)
  * [Docker](</id/install/docker>)
  * [Hosting VPS](</id/vps>)


Was this useful?YesNo