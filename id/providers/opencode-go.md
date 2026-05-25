---
title: OpenCode Go
source_url: https://docs.openclaw.ai/id/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go adalah katalog Go di dalam [OpenCode](</id/providers/opencode>). Katalog ini menggunakan `OPENCODE_API_KEY` yang sama dengan katalog Zen, tetapi mempertahankan ID provider runtime `opencode-go` agar perutean per-model upstream tetap benar.

Properti | Nilai  
---|---  
Provider runtime | `opencode-go`  
Auth | `OPENCODE_API_KEY`  
Setup induk | [OpenCode](</id/providers/opencode>)  
  
## Katalog bawaan

OpenClaw mengambil sebagian besar baris katalog Go dari registry model pi bawaan dan melengkapi baris upstream saat ini sementara registry masih menyusul. Jalankan `openclaw models list --provider opencode-go` untuk daftar model saat ini.

Provider ini mencakup:

Referensi model | Nama  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (limit 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Memulai

### Interaktif

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Atur model Go sebagai default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Non-interaktif

* ### Berikan key secara langsung

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Contoh config

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Konfigurasi lanjutan

Perilaku perutean

OpenClaw menangani perutean per-model secara otomatis saat referensi model menggunakan `opencode-go/...`. Tidak diperlukan config provider tambahan.

Konvensi referensi runtime

Referensi runtime tetap eksplisit: `opencode/...` untuk Zen, `opencode-go/...` untuk Go. Ini menjaga perutean per-model upstream tetap benar di kedua katalog.

Kredensial bersama

`OPENCODE_API_KEY` yang sama digunakan oleh katalog Zen dan Go. Memasukkan key selama setup menyimpan kredensial untuk kedua provider runtime.

## Terkait

[**OpenCode (induk)** Onboarding bersama, ikhtisar katalog, dan catatan lanjutan. ](</id/providers/opencode>) [**Pemilihan model** Memilih provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>)

Was this useful?YesNo