---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/id/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway berada di depan API penyedia dan memungkinkan Anda menambahkan analitik, caching, dan kontrol. Untuk Anthropic, OpenClaw menggunakan Anthropic Messages API melalui endpoint Gateway Anda.

Properti | Nilai  
---|---  
Penyedia | `cloudflare-ai-gateway`  
URL Dasar | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Model default | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Kunci API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (kunci API penyedia Anda untuk permintaan melalui Gateway)  
  
Saat thinking diaktifkan untuk model Anthropic Messages, OpenClaw menghapus giliran prefill asisten di akhir sebelum mengirim payload melalui Cloudflare AI Gateway. Anthropic menolak prefilling respons dengan extended thinking, sementara prefill non-thinking biasa tetap tersedia.

## Memulai

* ### Set the provider API key and Gateway details

Jalankan onboarding dan pilih opsi auth Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Ini meminta ID akun, ID gateway, dan kunci API Anda.

* ### Set a default model

Tambahkan model ke config OpenClaw Anda:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Contoh non-interaktif

Untuk penyiapan skrip atau CI, teruskan semua nilai di baris perintah:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Konfigurasi lanjutan

Authenticated gateways

Jika Anda mengaktifkan autentikasi Gateway di Cloudflare, tambahkan header `cf-aig-authorization`. Ini **sebagai tambahan dari** kunci API penyedia Anda.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Environment note

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `CLOUDFLARE_AI_GATEWAY_API_KEY` tersedia untuk proses tersebut.

## Terkait

[**Model selection** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Troubleshooting** Pemecahan masalah umum dan FAQ. ](</id/help/troubleshooting>)

Was this useful?YesNo