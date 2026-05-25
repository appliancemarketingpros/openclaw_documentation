---
title: Proxy API Claude Max
source_url: https://docs.openclaw.ai/id/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** adalah alat komunitas yang mengekspos subscription Claude Max/Pro Anda sebagai endpoint API yang kompatibel dengan OpenAI. Ini memungkinkan Anda menggunakan subscription Anda dengan alat apa pun yang mendukung format API OpenAI.

## Mengapa menggunakannya?

Pendekatan | Biaya | Paling cocok untuk  
---|---|---  
API Anthropic | Bayar per token (~$15/M input, $75/M output untuk Opus) | Aplikasi produksi, volume tinggi  
Subscription Claude Max | $200/bulan flat | Penggunaan personal, pengembangan, penggunaan tak terbatas  
  
Jika Anda memiliki subscription Claude Max dan ingin menggunakannya dengan alat yang kompatibel dengan OpenAI, proxy ini dapat mengurangi biaya untuk beberapa alur kerja. API key tetap merupakan jalur kebijakan yang lebih jelas untuk penggunaan produksi.

## Cara kerjanya

CodeCopy code
[code]
    Aplikasi Anda → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (format OpenAI)                (mengonversi format)    (menggunakan login Anda)
[/code]

Proxy ini:

  1. Menerima permintaan format OpenAI di `http://localhost:3456/v1/chat/completions`
  2. Mengonversinya menjadi perintah Claude Code CLI
  3. Mengembalikan respons dalam format OpenAI (streaming didukung)


## Memulai

* ### Instal proxy

Memerlukan Node.js 20+ dan Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verifikasi Claude CLI sudah diautentikasiclaude --version
[/code]

* ### Mulai server

bashCopy code
[code]
    claude-max-api# Server berjalan di http://localhost:3456
[/code]

* ### Uji proxy

bashCopy code
[code]
    # Pemeriksaan kesehatancurl http://localhost:3456/health # Daftar modelcurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Konfigurasikan OpenClaw

Arahkan OpenClaw ke proxy sebagai endpoint kustom yang kompatibel dengan OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Katalog bawaan

ID Model | Dipetakan ke  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Konfigurasi lanjutan

Catatan gaya proxy yang kompatibel dengan OpenAI

Jalur ini menggunakan rute gaya proxy yang kompatibel dengan OpenAI yang sama seperti backend kustom `/v1` lainnya:

  * Pembentukan permintaan khusus OpenAI native tidak berlaku
  * Tidak ada `service_tier`, tidak ada Responses `store`, tidak ada petunjuk prompt-cache, dan tidak ada pembentukan payload reasoning-compat OpenAI
  * Header atribusi OpenClaw tersembunyi (`originator`, `version`, `User-Agent`) tidak disisipkan pada URL proxy

Auto-start di macOS dengan LaunchAgent

Buat LaunchAgent untuk menjalankan proxy secara otomatis:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Tautan

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Catatan

  * Ini adalah **alat komunitas** , tidak didukung secara resmi oleh Anthropic atau OpenClaw
  * Memerlukan subscription Claude Max/Pro aktif dengan Claude Code CLI yang sudah diautentikasi
  * Proxy berjalan secara lokal dan tidak mengirim data ke server pihak ketiga mana pun
  * Respons streaming didukung penuh


## Terkait

[**Anthropic provider** Integrasi OpenClaw native dengan Claude CLI atau API key. ](</id/providers/anthropic>) [**OpenAI provider** Untuk subscription OpenAI/Codex. ](</id/providers/openai>) [**Model selection** Ikhtisar semua provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Configuration** Referensi konfigurasi lengkap. ](</id/gateway/configuration>)

Was this useful?YesNo