---
title: OpenCode
source_url: https://docs.openclaw.ai/id/providers/opencode
scraped_at: 2026-05-25
---

OpenCode mengekspos dua katalog hosting di OpenClaw:

Catalog | Prefix | Runtime provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Kedua katalog menggunakan OpenCode API key yang sama. OpenClaw tetap memisahkan ID penyedia runtime agar perutean per-model upstream tetap benar, tetapi onboarding dan dokumentasi memperlakukannya sebagai satu penyiapan OpenCode.

## Memulai

### Katalog Zen

**Terbaik untuk:** proxy multi-model OpenCode yang telah dikurasi (Claude, GPT, Gemini).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Atau berikan key secara langsung:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Tetapkan model Zen sebagai default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Katalog Go

**Terbaik untuk:** jajaran Kimi, GLM, dan MiniMax yang dihosting OpenCode.

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Atau berikan key secara langsung:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Tetapkan model Go sebagai default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Contoh config

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Katalog bawaan

### Zen

Property | Value  
---|---  
Penyedia runtime | `opencode`  
Contoh model | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Property | Value  
---|---  
Penyedia runtime | `opencode-go`  
Contoh model | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Konfigurasi lanjutan

Alias API key

`OPENCODE_ZEN_API_KEY` juga didukung sebagai alias untuk `OPENCODE_API_KEY`.

Kredensial bersama

Memasukkan satu key OpenCode saat penyiapan akan menyimpan kredensial untuk kedua penyedia runtime. Anda tidak perlu melakukan onboarding untuk setiap katalog secara terpisah.

Penagihan dan dashboard

Anda masuk ke OpenCode, menambahkan detail penagihan, dan menyalin API key Anda. Penagihan dan ketersediaan katalog dikelola dari dashboard OpenCode.

Perilaku replay Gemini

Ref OpenCode berbasis Gemini tetap berada di jalur proxy-Gemini, sehingga OpenClaw mempertahankan sanitasi thought-signature Gemini di sana tanpa mengaktifkan validasi replay Gemini native atau penulisan ulang bootstrap.

Perilaku replay non-Gemini

Ref OpenCode non-Gemini mempertahankan kebijakan replay minimal yang kompatibel dengan OpenAI.

## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Referensi config lengkap untuk agen, model, dan penyedia. ](</id/gateway/configuration-reference>)

Was this useful?YesNo