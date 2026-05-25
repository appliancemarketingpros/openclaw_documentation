---
title: Z.AI
source_url: https://docs.openclaw.ai/tr/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>), **GLM** modelleri için API platformudur. GLM için REST API'leri sağlar ve kimlik doğrulama için API anahtarları kullanır. API anahtarınızı [Z.AI](<http://Z.AI>) konsolunda oluşturun. OpenClaw, [Z.AI](<http://Z.AI>) API anahtarıyla `zai` sağlayıcısını kullanır.

  * Sağlayıcı: `zai`
  * Kimlik doğrulama: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (Bearer kimlik doğrulaması)


## Başlarken

### Auto-detect endpoint

**En uygun olduğu durum:** çoğu kullanıcı. OpenClaw, anahtardan eşleşen [Z.AI](<http://Z.AI>) uç noktasını algılar ve doğru temel URL'yi otomatik olarak uygular.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Explicit regional endpoint

**En uygun olduğu durum:** belirli bir Coding Plan'ı veya genel API yüzeyini zorunlu kılmak isteyen kullanıcılar.

* ### Pick the right onboarding choice

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Yerleşik katalog

OpenClaw, Plugin manifestinde paketli `zai` sağlayıcı kataloğunu gönderir; bu nedenle salt okunur listeleme, sağlayıcı çalışma zamanını yüklemeden bilinen GLM satırlarını gösterebilir:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Manifest destekli katalog şu anda şunları içerir:

Model ref | Notlar  
---|---  
`zai/glm-5.1` | Varsayılan model  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Gelişmiş yapılandırma

Forward-resolving unknown GLM-5 models

Bilinmeyen `glm-5*` kimlikleri, kimlik geçerli GLM-5 ailesi biçimiyle eşleştiğinde `glm-4.7` şablonundan sağlayıcının sahibi olduğu metadata sentezlenerek paketli sağlayıcı yolunda ileriye dönük çözümlenmeye devam eder.

Tool-call streaming

[Z.AI](<http://Z.AI>) tool-call akışı için `tool_stream` varsayılan olarak etkindir. Devre dışı bırakmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking and preserved thinking

[Z.AI](<http://Z.AI>) thinking, OpenClaw'ın `/think` kontrollerini izler. Thinking kapalıyken, OpenClaw görünür metinden önce çıktı bütçesini `reasoning_content` üzerinde harcayan yanıtları önlemek için `thinking: { type: "disabled" }` gönderir.

Korunan thinking isteğe bağlıdır; çünkü [Z.AI](<http://Z.AI>), tam geçmiş `reasoning_content` içeriğinin yeniden oynatılmasını gerektirir ve bu da prompt tokenlarını artırır. Bunu model başına etkinleştirin:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Etkinleştirildiğinde ve thinking açık olduğunda OpenClaw `thinking: { type: "enabled", clear_thinking: false }` gönderir ve aynı OpenAI uyumlu transkript için önceki `reasoning_content` içeriğini yeniden oynatır.

Gelişmiş kullanıcılar, tam sağlayıcı yükünü yine de `params.extra_body.thinking` ile geçersiz kılabilir.

Image understanding

Paketli [Z.AI](<http://Z.AI>) Plugin'i görüntü anlamayı kaydeder.

Özellik | Değer  
---|---  
Model | `glm-4.6v`  
  
Görüntü anlama, yapılandırılmış [Z.AI](<http://Z.AI>) kimlik doğrulamasından otomatik olarak çözümlenir; ek yapılandırma gerekmez.

Auth details

  * [Z.AI](<http://Z.AI>), API anahtarınızla Bearer kimlik doğrulaması kullanır.
  * `zai-api-key` onboarding seçimi, anahtar önekinden eşleşen [Z.AI](<http://Z.AI>) uç noktasını otomatik algılar.
  * Belirli bir API yüzeyini zorunlu kılmak istediğinizde açık bölgesel seçimleri (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) kullanın.


## İlgili

[**GLM model family** GLM için model ailesi genel görünümü. ](</tr/providers/glm>) [**Model selection** Sağlayıcıları, model ref'lerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>)

Was this useful?YesNo