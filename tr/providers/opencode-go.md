---
title: OpenCode Go
source_url: https://docs.openclaw.ai/tr/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go, [OpenCode](</tr/providers/opencode>) içindeki Go kataloğudur. Zen kataloğuyla aynı `OPENCODE_API_KEY` anahtarını kullanır, ancak üst akış model başına yönlendirmenin doğru kalması için çalışma zamanı sağlayıcı kimliğini `opencode-go` olarak korur.

Özellik | Değer  
---|---  
Çalışma zamanı sağlayıcısı | `opencode-go`  
Kimlik doğrulama | `OPENCODE_API_KEY`  
Üst kurulum | [OpenCode](</tr/providers/opencode>)  
  
## Yerleşik katalog

OpenClaw, Go kataloğu satırlarının çoğunu paketlenmiş Pi model kaydından alır ve kayıt güncellenene kadar güncel üst akış satırlarıyla bunu tamamlar. Geçerli model listesi için `openclaw models list --provider opencode-go` çalıştırın.

Sağlayıcı şunları içerir:

Model başvurusu | Ad  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (3x sınırlar)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Başlangıç

### Etkileşimli

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
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

### Etkileşimsiz

* ### Anahtarı doğrudan iletin

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Gelişmiş yapılandırma

Yönlendirme davranışı

OpenClaw, model başvurusu `opencode-go/...` kullandığında model başına yönlendirmeyi otomatik olarak işler. Ek bir sağlayıcı yapılandırması gerekmez.

Çalışma zamanı başvuru kuralı

Çalışma zamanı başvuruları açık kalır: Zen için `opencode/...`, Go için `opencode-go/...`. Bu, her iki katalogda da üst akış model başına yönlendirmenin doğru kalmasını sağlar.

Paylaşılan kimlik bilgileri

Aynı `OPENCODE_API_KEY`, hem Zen hem de Go katalogları tarafından kullanılır. Kurulum sırasında anahtar girildiğinde her iki çalışma zamanı sağlayıcısı için kimlik bilgileri depolanır.

## İlgili

[**OpenCode (üst)** Paylaşılan onboarding, katalog genel bakışı ve gelişmiş notlar. ](</tr/providers/opencode>) [**Model seçimi** Sağlayıcıları, model başvurularını ve failover davranışını seçme. ](</tr/concepts/model-providers>)

Was this useful?YesNo