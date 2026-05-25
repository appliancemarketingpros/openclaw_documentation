---
title: exe.dev
source_url: https://docs.openclaw.ai/id/install/exe-dev
scraped_at: 2026-05-25
---

Tujuan: OpenClaw Gateway berjalan di VM exe.dev, dapat dijangkau dari laptop Anda melalui: `https://<vm-name>.exe.xyz`

Halaman ini mengasumsikan image **exeuntu** default dari exe.dev. Jika Anda memilih distro lain, sesuaikan paketnya.

## Jalur cepat untuk pemula

  1. <https://exe.new/openclaw>
  2. Isi kunci/token autentikasi Anda sesuai kebutuhan
  3. Klik "Agen" di sebelah VM Anda dan tunggu Shelley selesai melakukan penyediaan
  4. Buka `https://<vm-name>.exe.xyz/` dan autentikasi dengan secret bersama yang dikonfigurasi (panduan ini menggunakan autentikasi token secara default, tetapi autentikasi kata sandi juga berfungsi jika Anda mengganti `gateway.auth.mode`)
  5. Setujui permintaan pemasangan perangkat yang tertunda dengan `openclaw devices approve <requestId>`


## Yang Anda butuhkan

  * Akun exe.dev
  * Akses `ssh exe.dev` ke mesin virtual [exe.dev](<https://exe.dev>) (opsional)


## Instalasi otomatis dengan Shelley

Shelley, agen [exe.dev](<https://exe.dev>), dapat langsung menginstal OpenClaw dengan prompt kami. Prompt yang digunakan adalah sebagai berikut:

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## Instalasi manual

## 1) Buat VM

Dari perangkat Anda:

bashCopy code
[code]
    ssh exe.dev new
[/code]

Lalu sambungkan:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) Instal prasyarat (di VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) Instal OpenClaw

Jalankan skrip instalasi OpenClaw:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) Siapkan nginx untuk mem-proxy OpenClaw ke port 8000

Edit `/etc/nginx/sites-enabled/default` dengan

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

Timpa header penerusan alih-alih mempertahankan rantai yang diberikan klien. OpenClaw memercayai metadata IP yang diteruskan hanya dari proxy yang dikonfigurasi secara eksplisit, dan rantai `X-Forwarded-For` bergaya append diperlakukan sebagai risiko hardening.

## 5) Akses OpenClaw dan berikan hak istimewa

Akses `https://<vm-name>.exe.xyz/` (lihat output Control UI dari onboarding). Jika meminta autentikasi, tempel secret bersama yang dikonfigurasi dari VM. Panduan ini menggunakan autentikasi token, jadi ambil `gateway.auth.token` dengan `openclaw config get gateway.auth.token` (atau buat satu dengan `openclaw doctor --generate-gateway-token`). Jika Anda mengubah gateway ke autentikasi kata sandi, gunakan `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` sebagai gantinya. Setujui perangkat dengan `openclaw devices list` dan `openclaw devices approve <requestId>`. Jika ragu, gunakan Shelley dari browser Anda!

## Penyiapan channel jarak jauh

Untuk host jarak jauh, lebih pilih satu panggilan `config patch` daripada banyak panggilan SSH ke `config set`. Simpan token asli di lingkungan VM atau `~/.openclaw/.env`, dan masukkan hanya SecretRefs di `openclaw.json`.

Di VM, buat lingkungan layanan berisi secret yang dibutuhkan:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

Dari mesin lokal Anda, buat file patch dan pipe ke VM:

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

Gunakan `--replace-path` saat allowlist bersarang harus menjadi persis nilai patch, misalnya saat mengganti allowlist channel Discord:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## Akses jarak jauh

Akses jarak jauh ditangani oleh autentikasi [exe.dev](<https://exe.dev>). Secara default, lalu lintas HTTP dari port 8000 diteruskan ke `https://<vm-name>.exe.xyz` dengan autentikasi email.

## Memperbarui

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

Panduan: [Memperbarui](</id/install/updating>)

## Terkait

  * [Gateway jarak jauh](</id/gateway/remote>)
  * [Ringkasan instalasi](</id/install>)


Was this useful?YesNo