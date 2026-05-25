---
title: Vercel AI ağ geçidi
source_url: https://docs.openclaw.ai/tr/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>), tek bir uç nokta üzerinden yüzlerce modele erişmek için birleşik bir API sağlar.

Özellik | Değer  
---|---  
Sağlayıcı | `vercel-ai-gateway`  
Kimlik doğrulama | `AI_GATEWAY_API_KEY`  
API | Anthropic Messages uyumlu  
Model kataloğu | `/v1/models` üzerinden otomatik keşfedilir  
  
## Başlarken

* ### Set the API key

Onboarding’i çalıştırın ve AI Gateway kimlik doğrulama seçeneğini seçin:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Set a default model

Modeli OpenClaw yapılandırmanıza ekleyin:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Etkileşimsiz örnek

Betikli veya CI kurulumları için tüm değerleri komut satırında geçirin:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Model kimliği kısaltması

OpenClaw, Vercel Claude kısa model referanslarını kabul eder ve bunları çalışma zamanında normalleştirir:

Kısaltma girdisi | Normalleştirilmiş model referansı  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Gelişmiş yapılandırma

Environment variable for daemon processes

OpenClaw Gateway bir artalan süreci (launchd/systemd) olarak çalışıyorsa, `AI_GATEWAY_API_KEY` değerinin bu süreç için kullanılabilir olduğundan emin olun.

Provider routing

Vercel AI Gateway, istekleri model referansı önekine göre yukarı akış sağlayıcısına yönlendirir. Örneğin, `vercel-ai-gateway/anthropic/claude-opus-4.6` Anthropic üzerinden yönlendirilirken, `vercel-ai-gateway/openai/gpt-5.5` OpenAI üzerinden ve `vercel-ai-gateway/moonshotai/kimi-k2.6` MoonshotAI üzerinden yönlendirilir. Tek `AI_GATEWAY_API_KEY` değeriniz, tüm yukarı akış sağlayıcıları için kimlik doğrulamayı yönetir.

Thinking levels

`/think` seçenekleri, OpenClaw yukarı akış sağlayıcı sözleşmesini bildiğinde güvenilir yukarı akış model öneklerini izler. `vercel-ai-gateway/anthropic/...`, Claude 4.6 modelleri için uyarlanabilir varsayılanlar dahil olmak üzere Claude düşünme profilini kullanır. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` ve Codex tarzı referanslar, doğrudan OpenAI/OpenAI Codex sağlayıcıları gibi `/think xhigh` seçeneğini sunar. Diğer ad alanlı referanslar, katalog meta verileri daha fazlasını bildirmedikçe normal akıl yürütme düzeylerini korur.

## İlgili

[**Model selection** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Troubleshooting** Genel sorun giderme ve SSS. ](</tr/help/troubleshooting>)

Was this useful?YesNo