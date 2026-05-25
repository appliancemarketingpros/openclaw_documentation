---
title: CLI otomasyonu
source_url: https://docs.openclaw.ai/tr/start/wizard-cli-automation
scraped_at: 2026-05-25
---

`openclaw onboard` işlemini otomatikleştirmek için `--non-interactive` kullanın.

## Temel etkileşimsiz örnek

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Makine tarafından okunabilir bir özet için `--json` ekleyin.

Otomasyonunuz çalışma alanı dosyalarını önceden hazırlıyorsa ve onboarding'in varsayılan bootstrap dosyalarını oluşturmasını istemiyorsanız `--skip-bootstrap` kullanın.

Düz metin değerleri yerine kimlik doğrulama profillerinde env destekli referanslar depolamak için `--secret-input-mode ref` kullanın. Env referansları ile yapılandırılmış sağlayıcı referansları (`file` veya `exec`) arasında etkileşimli seçim onboarding akışında kullanılabilir.

Etkileşimsiz `ref` modunda, sağlayıcı env değişkenleri süreç ortamında ayarlanmış olmalıdır. Eşleşen env değişkeni olmadan satır içi anahtar bayrakları geçirmek artık hızlıca başarısız olur.

Örnek:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Sağlayıcıya özel örnekler

Anthropic API key example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Gemini example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AI example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gateway example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshot example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistral example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Synthetic example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCode example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Go kataloğu için `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` seçeneğine geçin.

Ollama example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Custom provider example bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` isteğe bağlıdır. Atlanırsa onboarding `CUSTOM_API_KEY` değerini kontrol eder. OpenClaw, yaygın vision model kimliklerini otomatik olarak görüntü yetenekli olarak işaretler. Bilinmeyen özel vision kimlikleri için `--custom-image-input` ekleyin veya yalnızca metin meta verisini zorlamak için `--custom-text-input` kullanın.

Ref modu varyantı:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Bu modda onboarding, `apiKey` değerini `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }` olarak depolar.

Anthropic setup-token, desteklenen bir onboarding belirteci yolu olarak kullanılmaya devam eder, ancak OpenClaw artık mevcut olduğunda Claude CLI yeniden kullanımını tercih eder. Üretim için bir Anthropic API anahtarını tercih edin.

## Başka bir ajan ekleme

Kendi çalışma alanına, oturumlarına ve kimlik doğrulama profillerine sahip ayrı bir ajan oluşturmak için `openclaw agents add <name>` kullanın. `--workspace` olmadan çalıştırmak sihirbazı başlatır.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Ayarladıkları:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Notlar:

  * Varsayılan çalışma alanları `~/.openclaw/workspace-<agentId>` biçimini izler.
  * Gelen mesajları yönlendirmek için `bindings` ekleyin (sihirbaz bunu yapabilir).
  * Etkileşimsiz bayraklar: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## İlgili belgeler

  * Onboarding merkezi: [Onboarding (CLI)](</tr/start/wizard>)
  * Tam başvuru: [CLI Kurulum Başvurusu](</tr/start/wizard-cli-reference>)
  * Komut başvurusu: [`openclaw onboard`](</tr/cli/onboard>)


Was this useful?YesNo