---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/tr/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway, sağlayıcı API'lerinin önünde yer alır ve analiz, önbelleğe alma ve denetimler eklemenizi sağlar. Anthropic için OpenClaw, Gateway uç noktanız üzerinden Anthropic Messages API'sini kullanır.

Özellik | Değer  
---|---  
Sağlayıcı | `cloudflare-ai-gateway`  
Temel URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Varsayılan model | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API anahtarı | `CLOUDFLARE_AI_GATEWAY_API_KEY` (Gateway üzerinden yapılan istekler için sağlayıcı API anahtarınız)  
  
Anthropic Messages modellerinde düşünme etkinleştirildiğinde OpenClaw, yükü Cloudflare AI Gateway üzerinden göndermeden önce sondaki asistan ön doldurma dönüşlerini kaldırır. Anthropic, genişletilmiş düşünme ile yanıt ön doldurmayı reddederken, sıradan düşünmesiz ön doldurma kullanılabilir kalır.

## Başlarken

* ### Sağlayıcı API anahtarını ve Gateway ayrıntılarını ayarlayın

İlk kurulumu çalıştırın ve Cloudflare AI Gateway kimlik doğrulama seçeneğini belirleyin:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Bu, hesap ID'nizi, gateway ID'nizi ve API anahtarınızı ister.

* ### Varsayılan bir model ayarlayın

Modeli OpenClaw yapılandırmanıza ekleyin:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Etkileşimsiz örnek

Betikli veya CI kurulumları için tüm değerleri komut satırında geçirin:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Gelişmiş yapılandırma

Kimliği doğrulanmış gateway'ler

Cloudflare'da Gateway kimlik doğrulamasını etkinleştirdiyseniz `cf-aig-authorization` üst bilgisini ekleyin. Bu, sağlayıcı API anahtarınıza **ek olarak** kullanılır.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Ortam notu

Gateway bir daemon (launchd/systemd) olarak çalışıyorsa `CLOUDFLARE_AI_GATEWAY_API_KEY` değerinin bu işlem için kullanılabilir olduğundan emin olun.

## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Sorun giderme** Genel sorun giderme ve SSS. ](</tr/help/troubleshooting>)

Was this useful?YesNo