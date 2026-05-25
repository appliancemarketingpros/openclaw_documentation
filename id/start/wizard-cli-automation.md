---
title: Otomatisasi CLI
source_url: https://docs.openclaw.ai/id/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Gunakan `--non-interactive` untuk mengotomatiskan `openclaw onboard`.

## Contoh non-interaktif dasar

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Tambahkan `--json` untuk ringkasan yang dapat dibaca mesin.

Gunakan `--skip-bootstrap` ketika otomasi Anda sudah mengisi file ruang kerja terlebih dahulu dan tidak ingin onboarding membuat file bootstrap default.

Gunakan `--secret-input-mode ref` untuk menyimpan ref berbasis env di profil auth, bukan nilai plaintext. Pemilihan interaktif antara ref env dan ref penyedia yang dikonfigurasi (`file` atau `exec`) tersedia dalam alur onboarding.

Dalam mode `ref` non-interaktif, variabel env penyedia harus ditetapkan di lingkungan proses. Meneruskan flag kunci inline tanpa variabel env yang cocok kini gagal cepat.

Contoh:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Contoh khusus penyedia

Contoh kunci API Anthropic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Ganti ke `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` untuk katalog Go.

Contoh Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Contoh penyedia kustom bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` bersifat opsional. Jika dihilangkan, onboarding memeriksa `CUSTOM_API_KEY`. OpenClaw menandai ID model vision umum sebagai berkemampuan gambar secara otomatis. Tambahkan `--custom-image-input` untuk ID vision kustom yang tidak dikenal, atau `--custom-text-input` untuk memaksa metadata hanya teks.

Varian mode ref:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Dalam mode ini, onboarding menyimpan `apiKey` sebagai `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

Setup-token Anthropic tetap tersedia sebagai jalur token onboarding yang didukung, tetapi OpenClaw kini lebih memilih penggunaan ulang Claude CLI jika tersedia. Untuk produksi, pilih kunci API Anthropic.

## Tambahkan agen lain

Gunakan `openclaw agents add <name>` untuk membuat agen terpisah dengan ruang kerja, sesi, dan profil auth-nya sendiri. Menjalankan tanpa `--workspace` akan meluncurkan wizard.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Yang ditetapkannya:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Catatan:

  * Ruang kerja default mengikuti `~/.openclaw/workspace-<agentId>`.
  * Tambahkan `bindings` untuk merutekan pesan masuk (wizard dapat melakukan ini).
  * Flag non-interaktif: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Dokumen terkait

  * Hub onboarding: [Onboarding (CLI)](</id/start/wizard>)
  * Referensi lengkap: [Referensi Penyiapan CLI](</id/start/wizard-cli-reference>)
  * Referensi perintah: [`openclaw onboard`](</id/cli/onboard>)


Was this useful?YesNo