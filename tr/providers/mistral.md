---
title: Mistral
source_url: https://docs.openclaw.ai/tr/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw, dört sözleşme kaydeden paketle gelen bir Mistral Plugin'i içerir: sohbet tamamlama, medya anlama (Voxtral toplu transkripsiyon), Voice Call için gerçek zamanlı STT (Voxtral Realtime) ve bellek embedding'leri (`mistral-embed`).

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `mistral`  
Plugin | paketle gelen, `enabledByDefault: true`  
Kimlik doğrulama env var'ı | `MISTRAL_API_KEY`  
Onboarding bayrağı | `--auth-choice mistral-api-key`  
Doğrudan CLI bayrağı | `--mistral-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.mistral.ai/v1`  
Varsayılan model | `mistral/mistral-large-latest`  
Embedding modeli | `mistral-embed`  
Voxtral toplu | `voxtral-mini-latest` (ses transkripsiyonu)  
Voxtral gerçek zamanlı | `voxtral-mini-transcribe-realtime-2602`  
  
## Başlarken

* ### API anahtarınızı alın

[Mistral Console](<https://console.mistral.ai/>) içinde bir API anahtarı oluşturun.

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Veya anahtarı doğrudan geçirin:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Varsayılan model ayarlayın

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Yerleşik LLM kataloğu

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) paketle gelen katalogdaki güncel harmanlanmış Medium modelidir: 128B yoğun ağırlık, metin ve görüntü girişi, 256K bağlam, işlev çağırma, yapılandırılmış çıktı, kodlama ve Chat Completions API üzerinden ayarlanabilir akıl yürütme. Varsayılan `mistral/mistral-large-latest` yerine Mistral'ın daha yeni birleşik ajan/kodlama modelini istediğinizde `mistral/mistral-medium-3-5` kullanın.

OpenClaw şu anda bu paketle gelen Mistral kataloğunu sağlar:

Model ref | Giriş | Bağlam | Maks. çıktı | Notlar  
---|---|---|---|---  
`mistral/mistral-large-latest` | metin, görüntü | 262,144 | 16,384 | Varsayılan model  
`mistral/mistral-medium-2508` | metin, görüntü | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | metin, görüntü | 262,144 | 8,192 | Mistral Medium 3.5; ayarlanabilir akıl yürütme  
`mistral/mistral-small-latest` | metin, görüntü | 128,000 | 16,384 | Mistral Small 4; API `reasoning_effort` üzerinden ayarlanabilir akıl yürütme  
`mistral/pixtral-large-latest` | metin, görüntü | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | metin | 256,000 | 4,096 | Kodlama  
`mistral/devstral-medium-latest` | metin | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | metin | 128,000 | 40,000 | Akıl yürütme etkin  
  
Onboarding'den sonra, Gateway'i başlatmadan Medium 3.5'i smoke test edin:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Yapılandırmayı değiştirmeden önce paketle gelen katalog satırına göz atmak için:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Ses transkripsiyonu (Voxtral)

Medya anlama işlem hattı üzerinden toplu ses transkripsiyonu için Voxtral kullanın.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Voice Call akış STT'si

Paketle gelen `mistral` Plugin'i, Voxtral Realtime'ı bir Voice Call akış STT sağlayıcısı olarak kaydeder.

Ayar | Yapılandırma yolu | Varsayılan  
---|---|---  
API anahtarı | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | `MISTRAL_API_KEY` değerine geri döner  
Model | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Kodlama | `...mistral.encoding` | `pcm_mulaw`  
Örnekleme hızı | `...mistral.sampleRate` | `8000`  
Hedef gecikme | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Gelişmiş yapılandırma

Ayarlanabilir akıl yürütme

`mistral/mistral-small-latest` (Mistral Small 4) ve `mistral/mistral-medium-3-5`, Chat Completions API üzerinde `reasoning_effort` aracılığıyla [ayarlanabilir akıl yürütmeyi](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) destekler (`none`, çıktıda ekstra düşünmeyi en aza indirir; `high`, son yanıttan önce tam düşünme izlerini gösterir). Mistral, Medium 3.5 ajan ve kod kullanım durumları için `reasoning_effort="high"` önerir.

OpenClaw, oturum **thinking** düzeyini Mistral'ın API'sine eşler:

OpenClaw thinking düzeyi | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Medium 3.5 akıl yürütmesi için model kapsamlı yapılandırma örneği:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Bellek embedding'leri

Mistral, `/v1/embeddings` üzerinden bellek embedding'leri sunabilir (varsayılan model: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Kimlik doğrulama ve temel URL

  * Mistral kimlik doğrulaması `MISTRAL_API_KEY` kullanır (Bearer başlığı).
  * Sağlayıcı temel URL'si varsayılan olarak `https://api.mistral.ai/v1` değerine ayarlanır ve standart OpenAI uyumlu chat-completions istek şeklini kabul eder.
  * Onboarding varsayılan modeli `mistral/mistral-large-latest`'tir.
  * Temel URL'yi `models.providers.mistral.baseUrl` altında yalnızca Mistral ihtiyacınız olan bölgesel bir uç noktayı açıkça yayımladığında geçersiz kılın.


## İlgili

[**Model seçimi** Sağlayıcıları, model ref'lerini ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**Medya anlama** Ses transkripsiyonu kurulumu ve sağlayıcı seçimi. ](</tr/nodes/media-understanding>)

Was this useful?YesNo