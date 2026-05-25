---
title: Gateway AI Vercel
source_url: https://docs.openclaw.ai/id/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) menyediakan API terpadu untuk mengakses ratusan model melalui satu endpoint.

Properti | Nilai  
---|---  
Penyedia | `vercel-ai-gateway`  
Autentikasi | `AI_GATEWAY_API_KEY`  
API | Kompatibel dengan Anthropic Messages  
Katalog model | Ditemukan otomatis melalui `/v1/models`  
  
## Memulai

* ### Atur kunci API

Jalankan onboarding dan pilih opsi autentikasi AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Atur model default

Tambahkan model ke konfigurasi OpenClaw Anda:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Contoh non-interaktif

Untuk penyiapan berbasis skrip atau CI, berikan semua nilai pada baris perintah:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Singkatan ID model

OpenClaw menerima ref model singkatan Vercel Claude dan menormalkannya saat runtime:

Input singkatan | Ref model yang dinormalkan  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Konfigurasi lanjutan

Variabel lingkungan untuk proses daemon

Jika OpenClaw Gateway berjalan sebagai daemon (launchd/systemd), pastikan `AI_GATEWAY_API_KEY` tersedia untuk proses tersebut.

Perutean penyedia

Vercel AI Gateway merutekan permintaan ke penyedia upstream berdasarkan prefiks ref model. Misalnya, `vercel-ai-gateway/anthropic/claude-opus-4.6` dirutekan melalui Anthropic, sedangkan `vercel-ai-gateway/openai/gpt-5.5` dirutekan melalui OpenAI dan `vercel-ai-gateway/moonshotai/kimi-k2.6` dirutekan melalui MoonshotAI. Satu `AI_GATEWAY_API_KEY` Anda menangani autentikasi untuk semua penyedia upstream.

Tingkat berpikir

Opsi `/think` mengikuti prefiks model upstream tepercaya ketika OpenClaw mengetahui kontrak penyedia upstream. `vercel-ai-gateway/anthropic/...` menggunakan profil berpikir Claude, termasuk default adaptif untuk model Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5`, dan ref bergaya Codex mengekspos `/think xhigh` sama seperti penyedia OpenAI/OpenAI Codex langsung. Ref bernamespaced lainnya mempertahankan tingkat penalaran normal kecuali metadata katalog mereka menyatakan lebih banyak.

## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pemecahan masalah** Pemecahan masalah umum dan FAQ. ](</id/help/troubleshooting>)

Was this useful?YesNo