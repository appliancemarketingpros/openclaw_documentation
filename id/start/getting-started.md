---
title: Memulai
source_url: https://docs.openclaw.ai/id/start/getting-started
scraped_at: 2026-05-25
---

Instal OpenClaw, jalankan onboarding, dan chat dengan asisten AI Anda — semuanya dalam sekitar 5 menit. Pada akhirnya Anda akan memiliki Gateway yang berjalan, auth yang dikonfigurasi, dan sesi chat yang berfungsi.

## Yang Anda butuhkan

  * **Node.js** — Node 24 direkomendasikan (Node 22.16+ juga didukung)
  * **Kunci API** dari penyedia model (Anthropic, OpenAI, Google, dll.) — onboarding akan meminta Anda memasukkannya


## Penyiapan cepat

* ### Instal OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Proses Skrip Instalasi](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Wizard memandu Anda memilih penyedia model, mengatur kunci API, dan mengonfigurasi Gateway. Ini memerlukan sekitar 2 menit.

Lihat [Onboarding (CLI)](</id/start/wizard>) untuk referensi lengkap.

* ### Verifikasi Gateway sedang berjalan

bashCopy code
[code]
    openclaw gateway status
[/code]

Anda akan melihat Gateway mendengarkan pada port 18789.

* ### Buka dashboard

bashCopy code
[code]
    openclaw dashboard
[/code]

Ini membuka Control UI di browser Anda. Jika halaman dimuat, semuanya berfungsi.

* ### Kirim pesan pertama Anda

Ketik pesan di chat Control UI dan Anda akan mendapatkan balasan AI.

Ingin chat dari ponsel sebagai gantinya? Channel tercepat untuk disiapkan adalah [Telegram](</id/channels/telegram>) (hanya token bot). Lihat [Channel](</id/channels>) untuk semua opsi.

Lanjutan: mount build Control UI kustom

Jika Anda memelihara build dashboard yang dilokalkan atau dikustomisasi, arahkan `gateway.controlUi.root` ke direktori yang berisi aset statis hasil build dan `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Lalu atur:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Mulai ulang gateway dan buka kembali dashboard:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Yang dapat dilakukan berikutnya

[**Hubungkan channel** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, dan lainnya. ](</id/channels>) [**Pairing dan keamanan** Kendalikan siapa yang dapat mengirim pesan ke agen Anda. ](</id/channels/pairing>) [**Konfigurasikan Gateway** Model, alat, sandbox, dan pengaturan lanjutan. ](</id/gateway/configuration>) [**Jelajahi alat** Browser, exec, pencarian web, Skills, dan plugin. ](</id/tools>)

Lanjutan: variabel lingkungan

Jika Anda menjalankan OpenClaw sebagai akun layanan atau menginginkan path kustom:

  * `OPENCLAW_HOME` — direktori home untuk resolusi path internal
  * `OPENCLAW_STATE_DIR` — timpa direktori state
  * `OPENCLAW_CONFIG_PATH` — timpa path file konfigurasi


Referensi lengkap: [Variabel lingkungan](</id/help/environment>).

## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Ikhtisar channel](</id/channels>)
  * [Penyiapan](</id/start/setup>)


Was this useful?YesNo