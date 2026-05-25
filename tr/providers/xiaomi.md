---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/tr/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo, **MiMo** modelleri için API platformudur. OpenClaw, aynı `XIAOMI_API_KEY` ile hem OpenAI uyumlu bir sohbet sağlayıcısı hem de bir konuşma (TTS) sağlayıcısı kaydeden, birlikte gelen bir `xiaomi` Plugin içerir.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `xiaomi`  
Plugin | birlikte gelir, `enabledByDefault: true`  
Kimlik doğrulama env var | `XIAOMI_API_KEY`  
Başlatma bayrağı | `--auth-choice xiaomi-api-key`  
Doğrudan CLI bayrağı | `--xiaomi-api-key <key>`  
Sözleşmeler | sohbet tamamlama + `speechProviders`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.xiaomimimo.com/v1`  
Varsayılan model | `xiaomi/mimo-v2-flash`  
TTS varsayılanı | `mimo-v2.5-tts`, ses `mimo_default`  
  
## Başlarken

* ### API anahtarı alın

[Xiaomi MiMo konsolunda](<https://platform.xiaomimimo.com/#/console/api-keys>) bir API anahtarı oluşturun.

* ### Başlatmayı çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Ya da anahtarı doğrudan geçirin:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Yerleşik katalog

Model ref | Girdi | Bağlam | En fazla çıktı | Akıl yürütme | Notlar  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | metin | 262,144 | 8,192 | Hayır | Varsayılan model  
`xiaomi/mimo-v2-pro` | metin | 1,048,576 | 32,000 | Evet | Büyük bağlam  
`xiaomi/mimo-v2-omni` | metin, görüntü | 262,144 | 32,000 | Evet | Çok modlu  
  
## Metinden konuşmaya

Birlikte gelen `xiaomi` Plugin, Xiaomi MiMo'yu `messages.tts` için bir konuşma sağlayıcısı olarak da kaydeder. Metni bir `assistant` iletisi, isteğe bağlı üslup yönlendirmesini ise bir `user` iletisi olarak kullanarak Xiaomi'nin sohbet tamamlama TTS sözleşmesini çağırır.

Özellik | Değer  
---|---  
TTS kimliği | `xiaomi` (`mimo` diğer adı)  
Kimlik doğrulama | `XIAOMI_API_KEY`  
API | `audio` ile `POST /v1/chat/completions`  
Varsayılan | `mimo-v2.5-tts`, ses `mimo_default`  
Çıktı | Varsayılan olarak MP3; yapılandırıldığında WAV  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Desteklenen yerleşik sesler arasında `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` ve `Dean` bulunur. `mimo-v2-tts`, eski MiMo TTS hesapları için desteklenir; varsayılan, güncel MiMo-V2.5 TTS modelini kullanır. Feishu ve Telegram gibi sesli not hedefleri için OpenClaw, teslimattan önce Xiaomi çıktısını `ffmpeg` ile 48 kHz Opus'a dönüştürür.

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Otomatik enjeksiyon davranışı

Ortamınızda `XIAOMI_API_KEY` ayarlandığında veya bir kimlik doğrulama profili mevcut olduğunda `xiaomi` sağlayıcısı otomatik olarak enjekte edilir. Model meta verilerini veya temel URL'yi geçersiz kılmak istemediğiniz sürece sağlayıcıyı elle yapılandırmanız gerekmez.

Model ayrıntıları

  * **mimo-v2-flash** — hafif ve hızlıdır, genel amaçlı metin görevleri için idealdir. Akıl yürütme desteği yoktur.
  * **mimo-v2-pro** — uzun belge iş yükleri için 1M token bağlam penceresiyle akıl yürütmeyi destekler.
  * **mimo-v2-omni** — hem metin hem de görüntü girdilerini kabul eden, akıl yürütme özellikli çok modlu model.

Sorun giderme

  * Modeller görünmüyorsa `XIAOMI_API_KEY` değerinin ayarlı ve geçerli olduğunu doğrulayın.
  * Gateway bir daemon olarak çalıştığında, anahtarın o süreç tarafından kullanılabilir olduğundan emin olun (örneğin `~/.openclaw/.env` içinde veya `env.shellEnv` aracılığıyla).


## İlgili

[**Model seçimi** Sağlayıcıları, model ref değerlerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma başvurusu** Tam OpenClaw yapılandırma başvurusu. ](</tr/gateway/configuration-reference>) [**Xiaomi MiMo konsolu** Xiaomi MiMo panosu ve API anahtarı yönetimi. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo