---
title: OpenCode
source_url: https://docs.openclaw.ai/tr/providers/opencode
scraped_at: 2026-05-25
---

OpenCode, OpenClaw içinde iki barındırılan katalog açığa çıkarır:

Catalog | Prefix | Runtime provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Her iki katalog da aynı OpenCode API anahtarını kullanır. OpenClaw, yukarı akış model başına yönlendirmenin doğru kalması için çalışma zamanı sağlayıcı kimliklerini ayrı tutar, ancak onboarding ve belgeler bunları tek bir OpenCode kurulumu olarak ele alır.

## Başlarken

### Zen kataloğu

**Şunun için en iyisi:** küratörlü OpenCode çok modelli proxy (Claude, GPT, Gemini).

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Veya anahtarı doğrudan verin:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Varsayılan olarak bir Zen modeli ayarlayın

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go kataloğu

**Şunun için en iyisi:** OpenCode tarafından barındırılan Kimi, GLM ve MiniMax dizilimi.

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Veya anahtarı doğrudan verin:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Varsayılan olarak bir Go modeli ayarlayın

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Yerleşik kataloglar

### Zen

Property | Value  
---|---  
Runtime provider | `opencode`  
Example models | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Property | Value  
---|---  
Runtime provider | `opencode-go`  
Example models | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Gelişmiş yapılandırma

API anahtarı takma adları

`OPENCODE_ZEN_API_KEY`, `OPENCODE_API_KEY` için takma ad olarak da desteklenir.

Paylaşılan kimlik bilgileri

Kurulum sırasında tek bir OpenCode anahtarı girildiğinde, kimlik bilgileri her iki çalışma zamanı sağlayıcısı için de saklanır. Her kataloğu ayrı ayrı onboard etmeniz gerekmez.

Faturalandırma ve kontrol paneli

OpenCode'da oturum açar, faturalandırma bilgilerinizi eklersiniz ve API anahtarınızı kopyalarsınız. Faturalandırma ve katalog kullanılabilirliği OpenCode kontrol panelinden yönetilir.

Gemini yeniden oynatma davranışı

Gemini destekli OpenCode başvuruları proxy-Gemini yolunda kalır, bu yüzden OpenClaw yerel Gemini yeniden oynatma doğrulamasını veya bootstrap yeniden yazımlarını etkinleştirmeden orada Gemini düşünce-imzası sanitize işlemini korur.

Gemini olmayan yeniden oynatma davranışı

Gemini olmayan OpenCode başvuruları en düşük düzeyde OpenAI uyumlu yeniden oynatma ilkesini korur.

## İlgili

[**Model seçimi** Sağlayıcıları, model başvurularını ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma başvurusu** Aracılar, modeller ve sağlayıcılar için tam config başvurusu. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo