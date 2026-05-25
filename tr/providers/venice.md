---
title: Venice AI
source_url: https://docs.openclaw.ai/tr/providers/venice
scraped_at: 2026-05-25
---

Venice AI, sansürsüz modellere destek ve anonimleştirilmiş proxy'leri üzerinden başlıca özel mülk modellere erişimle **gizlilik odaklı yapay zeka çıkarımı** sağlar. Tüm çıkarım varsayılan olarak özeldir — verileriniz üzerinde eğitim yapılmaz, kayıt tutulmaz.

## OpenClaw’da neden Venice

  * Açık kaynak modeller için **özel çıkarım** (kayıt yok).
  * İhtiyacınız olduğunda **sansürsüz modeller**.
  * Kalite önemli olduğunda özel mülk modellere (Opus/GPT/Gemini) **anonimleştirilmiş erişim**.
  * OpenAI uyumlu `/v1` uç noktaları.


## Gizlilik modları

Venice iki gizlilik düzeyi sunar — bunu anlamak modelinizi seçmenin anahtarıdır:

Mod | Açıklama | Modeller  
---|---|---  
**Özel** | Tamamen özel. İstemler/yanıtlar **asla saklanmaz veya kaydedilmez**. Geçici. | Llama, Qwen, DeepSeek, Kimi, MiniMax, Venice Uncensored, vb.  
**Anonimleştirilmiş** | Meta veriler çıkarılarak Venice üzerinden proxylanır. Altta yatan sağlayıcı (OpenAI, Anthropic, Google, xAI) anonimleştirilmiş istekleri görür. | Claude, GPT, Gemini, Grok  
  
## Özellikler

  * **Gizlilik odaklı** : "özel" (tamamen özel) ve "anonimleştirilmiş" (proxylanmış) modlar arasında seçim yapın
  * **Sansürsüz modeller** : İçerik kısıtlamaları olmayan modellere erişim
  * **Başlıca model erişimi** : Venice'in anonimleştirilmiş proxy'si üzerinden Claude, GPT, Gemini ve Grok kullanın
  * **OpenAI uyumlu API** : Kolay entegrasyon için standart `/v1` uç noktaları
  * **Akış** : Tüm modellerde desteklenir
  * **Fonksiyon çağırma** : Seçili modellerde desteklenir (model yeteneklerini kontrol edin)
  * **Görüntü** : Görüntü yeteneği olan modellerde desteklenir
  * **Katı hız sınırları yok** : Aşırı kullanım için adil kullanım kısıtlaması uygulanabilir


## Başlarken

* ### API anahtarınızı alın

  1. [venice.ai](<https://venice.ai>) adresinden kaydolun
  2. **Ayarlar > API Anahtarları > Yeni anahtar oluştur** bölümüne gidin
  3. API anahtarınızı kopyalayın (biçim: `vapi_xxxxxxxxxxxx`)


* ### OpenClaw’ı yapılandırın

Tercih ettiğiniz kurulum yöntemini seçin:

### Etkileşimli (önerilir)

bashCopy code
[code]
    openclaw onboard --auth-choice venice-api-key
[/code]

Bu şunları yapar:

  1. API anahtarınızı ister (veya mevcut `VENICE_API_KEY` değerini kullanır)
  2. Kullanılabilir tüm Venice modellerini gösterir
  3. Varsayılan modelinizi seçmenizi sağlar
  4. Sağlayıcıyı otomatik olarak yapılandırır


### Ortam değişkeni

bashCopy code
[code]
    export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
[/code]

### Etkileşimsiz

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice venice-api-key \  --venice-api-key "vapi_xxxxxxxxxxxx"
[/code]

* ### Kurulumu doğrulayın

bashCopy code
[code]
    openclaw agent --model venice/kimi-k2-5 --message "Hello, are you working?"
[/code]

## Model seçimi

Kurulumdan sonra OpenClaw kullanılabilir tüm Venice modellerini gösterir. İhtiyaçlarınıza göre seçin:

  * **Varsayılan model** : Güçlü özel akıl yürütme ve görüntü için `venice/kimi-k2-5`.
  * **Yüksek yetenekli seçenek** : En güçlü anonimleştirilmiş Venice yolu için `venice/claude-opus-4-6`.
  * **Gizlilik** : Tamamen özel çıkarım için "özel" modelleri seçin.
  * **Yetenek** : Venice'in proxy'si üzerinden Claude, GPT, Gemini erişimi için "anonimleştirilmiş" modelleri seçin.


Varsayılan modelinizi istediğiniz zaman değiştirin:

bashCopy code
[code]
    openclaw models set venice/kimi-k2-5openclaw models set venice/claude-opus-4-6
[/code]

Kullanılabilir tüm modelleri listeleyin:

bashCopy code
[code]
    openclaw models list --all --provider venice
[/code]

Ayrıca `openclaw configure` komutunu çalıştırıp **Model/kimlik doğrulama** seçeneğini ve ardından **Venice AI** seçeneğini seçebilirsiniz.

## DeepSeek V4 yeniden oynatma davranışı

Venice `venice/deepseek-v4-pro` veya `venice/deepseek-v4-flash` gibi DeepSeek V4 modellerini sunarsa, proxy bunu atladığında OpenClaw asistan mesajlarında gerekli DeepSeek V4 `reasoning_content` yeniden oynatma yer tutucusunu doldurur. Venice, DeepSeek'in yerel üst düzey `thinking` denetimini reddeder; bu nedenle OpenClaw, sağlayıcıya özgü bu yeniden oynatma düzeltmesini yerel DeepSeek sağlayıcısının düşünme denetimlerinden ayrı tutar.

## Yerleşik katalog (toplam 41)

Özel modeller (26) — tamamen özel, kayıt yok Model Kimliği | Ad | Bağlam | Özellikler  
---|---|---|---  
`kimi-k2-5` | Kimi K2.5 | 256k | Varsayılan, akıl yürütme, görüntü  
`kimi-k2-thinking` | Kimi K2 Thinking | 256k | Akıl yürütme  
`llama-3.3-70b` | Llama 3.3 70B | 128k | Genel  
`llama-3.2-3b` | Llama 3.2 3B | 128k | Genel  
`hermes-3-llama-3.1-405b` | Hermes 3 Llama 3.1 405B | 128k | Genel, araçlar devre dışı  
`qwen3-235b-a22b-thinking-2507` | Qwen3 235B Thinking | 128k | Akıl yürütme  
`qwen3-235b-a22b-instruct-2507` | Qwen3 235B Instruct | 128k | Genel  
`qwen3-coder-480b-a35b-instruct` | Qwen3 Coder 480B | 256k | Kodlama  
`qwen3-coder-480b-a35b-instruct-turbo` | Qwen3 Coder 480B Turbo | 256k | Kodlama  
`qwen3-5-35b-a3b` | Qwen3.5 35B A3B | 256k | Akıl yürütme, görüntü  
`qwen3-next-80b` | Qwen3 Next 80B | 256k | Genel  
`qwen3-vl-235b-a22b` | Qwen3 VL 235B (Vision) | 256k | Görüntü  
`qwen3-4b` | Venice Small (Qwen3 4B) | 32k | Hızlı, akıl yürütme  
`deepseek-v3.2` | DeepSeek V3.2 | 160k | Akıl yürütme, araçlar devre dışı  
`venice-uncensored` | Venice Uncensored (Dolphin-Mistral) | 32k | Sansürsüz, araçlar devre dışı  
`mistral-31-24b` | Venice Medium (Mistral) | 128k | Görüntü  
`google-gemma-3-27b-it` | Google Gemma 3 27B Instruct | 198k | Görüntü  
`openai-gpt-oss-120b` | OpenAI GPT OSS 120B | 128k | Genel  
`nvidia-nemotron-3-nano-30b-a3b` | NVIDIA Nemotron 3 Nano 30B | 128k | Genel  
`olafangensan-glm-4.7-flash-heretic` | GLM 4.7 Flash Heretic | 128k | Akıl yürütme  
`zai-org-glm-4.6` | GLM 4.6 | 198k | Genel  
`zai-org-glm-4.7` | GLM 4.7 | 198k | Akıl yürütme  
`zai-org-glm-4.7-flash` | GLM 4.7 Flash | 128k | Akıl yürütme  
`zai-org-glm-5` | GLM 5 | 198k | Akıl yürütme  
`minimax-m21` | MiniMax M2.1 | 198k | Akıl yürütme  
`minimax-m25` | MiniMax M2.5 | 198k | Akıl yürütme  
Anonimleştirilmiş modeller (15) — Venice proxy'si üzerinden Model Kimliği | Ad | Bağlam | Özellikler  
---|---|---|---  
`claude-opus-4-6` | Claude Opus 4.6 (Venice üzerinden) | 1M | Akıl yürütme, görüntü  
`claude-opus-4-5` | Claude Opus 4.5 (Venice üzerinden) | 198k | Akıl yürütme, görüntü  
`claude-sonnet-4-6` | Claude Sonnet 4.6 (Venice üzerinden) | 1M | Akıl yürütme, görüntü  
`claude-sonnet-4-5` | Claude Sonnet 4.5 (Venice üzerinden) | 198k | Akıl yürütme, görüntü  
`openai-gpt-54` | GPT-5.4 (Venice üzerinden) | 1M | Akıl yürütme, görüntü  
`openai-gpt-53-codex` | GPT-5.3 Codex (Venice üzerinden) | 400k | Akıl yürütme, görüntü, kodlama  
`openai-gpt-52` | GPT-5.2 (Venice üzerinden) | 256k | Akıl yürütme  
`openai-gpt-52-codex` | GPT-5.2 Codex (Venice üzerinden) | 256k | Akıl yürütme, görüntü, kodlama  
`openai-gpt-4o-2024-11-20` | GPT-4o (Venice üzerinden) | 128k | Görüntü  
`openai-gpt-4o-mini-2024-07-18` | GPT-4o Mini (Venice üzerinden) | 128k | Görüntü  
`gemini-3-1-pro-preview` | Gemini 3.1 Pro (Venice üzerinden) | 1M | Akıl yürütme, görüntü  
`gemini-3-pro-preview` | Gemini 3 Pro (Venice üzerinden) | 198k | Akıl yürütme, görüntü  
`gemini-3-flash-preview` | Gemini 3 Flash (Venice üzerinden) | 256k | Akıl yürütme, görüntü  
`grok-41-fast` | Grok 4.1 Fast (Venice üzerinden) | 1M | Akıl yürütme, görüntü  
`grok-code-fast-1` | Grok Code Fast 1 (Venice üzerinden) | 256k | Akıl yürütme, kodlama  
  
## Model keşfi

OpenClaw, salt okunur model listeleme için manifest destekli bir Venice başlangıç kataloğuyla gelir. Çalışma zamanı yenilemesi yine de Venice API'den modelleri keşfedebilir ve API'ye ulaşılamazsa manifest kataloğuna geri döner.

`/models` uç noktası herkese açıktır (listeleme için kimlik doğrulama gerekmez), ancak çıkarım geçerli bir API anahtarı gerektirir.

## Akış ve araç desteği

Özellik | Destek  
---|---  
**Akış** | Tüm modeller  
**İşlev çağırma** | Çoğu model (API’de `supportsFunctionCalling` değerini kontrol edin)  
**Görme/Görüntüler** | "Vision" özelliğiyle işaretlenmiş modeller  
**JSON modu** | `response_format` aracılığıyla desteklenir  
  
## Fiyatlandırma

Venice kredi tabanlı bir sistem kullanır. Güncel ücretler için [venice.ai/pricing](<https://venice.ai/pricing>) sayfasını kontrol edin:

  * **Özel modeller** : Genellikle daha düşük maliyet
  * **Anonimleştirilmiş modeller** : Doğrudan API fiyatlandırmasına benzer + küçük Venice ücreti


### Venice (anonimleştirilmiş) ve doğrudan API karşılaştırması

Yön | Venice (Anonimleştirilmiş) | Doğrudan API  
---|---|---  
**Gizlilik** | Metadata kaldırılır, anonimleştirilir | Hesabınız bağlanır  
**Gecikme** | +10-50ms (proxy) | Doğrudan  
**Özellikler** | Çoğu özellik desteklenir | Tüm özellikler  
**Faturalama** | Venice kredileri | Sağlayıcı faturalandırması  
  
## Kullanım örnekleri

bashCopy code
[code]
    # Use the default private modelopenclaw agent --model venice/kimi-k2-5 --message "Quick health check" # Use Claude Opus via Venice (anonymized)openclaw agent --model venice/claude-opus-4-6 --message "Summarize this task" # Use uncensored modelopenclaw agent --model venice/venice-uncensored --message "Draft options" # Use vision model with imageopenclaw agent --model venice/qwen3-vl-235b-a22b --message "Review attached image" # Use coding modelopenclaw agent --model venice/qwen3-coder-480b-a35b-instruct --message "Refactor this function"
[/code]

## Sorun giderme

API key not recognized bashCopy code
[code]
    echo $VENICE_API_KEYopenclaw models list | grep venice
[/code]

Anahtarın `vapi_` ile başladığından emin olun.

Model not available

Venice model kataloğu dinamik olarak güncellenir. Şu anda kullanılabilir modelleri görmek için `openclaw models list` komutunu çalıştırın. Bazı modeller geçici olarak çevrimdışı olabilir.

Connection issues

Venice API `https://api.venice.ai/api/v1` adresindedir. Ağınızın HTTPS bağlantılarına izin verdiğinden emin olun.

## Gelişmiş yapılandırma

Config file example json5Copy code
[code]
    {  env: { VENICE_API_KEY: "vapi_..." },  agents: { defaults: { model: { primary: "venice/kimi-k2-5" } } },  models: {    mode: "merge",    providers: {      venice: {        baseUrl: "https://api.venice.ai/api/v1",        apiKey: "${VENICE_API_KEY}",        api: "openai-completions",        models: [          {            id: "kimi-k2-5",            name: "Kimi K2.5",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## İlgili

[**Model selection** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Venice AI** Venice AI ana sayfası ve hesap kaydı. ](<https://venice.ai>) [**API documentation** Venice API referansı ve geliştirici belgeleri. ](<https://docs.venice.ai>) [**Pricing** Güncel Venice kredi ücretleri ve planları. ](<https://venice.ai/pricing>)

Was this useful?YesNo