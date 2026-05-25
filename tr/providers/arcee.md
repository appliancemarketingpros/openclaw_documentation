---
title: Arcee AI
source_url: https://docs.openclaw.ai/tr/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>), OpenAI uyumlu bir API aracılığıyla Trinity uzmanlar karışımı model ailesine erişim sağlar. Tüm Trinity modelleri Apache 2.0 lisanslıdır.

Arcee AI modellerine doğrudan Arcee platformu üzerinden veya [OpenRouter](</tr/providers/openrouter>) aracılığıyla erişilebilir.

Özellik | Değer  
---|---  
Sağlayıcı | `arcee`  
Kimlik doğrulama | `ARCEEAI_API_KEY` (doğrudan) veya `OPENROUTER_API_KEY` (OpenRouter üzerinden)  
API | OpenAI uyumlu  
Temel URL | `https://api.arcee.ai/api/v1` (doğrudan) veya `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Başlarken

### Direct (Arcee platform)

* ### Get an API key

[Arcee AI](<https://chat.arcee.ai/>) adresinde bir API anahtarı oluşturun.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Get an API key

[OpenRouter](<https://openrouter.ai/keys>) adresinde bir API anahtarı oluşturun.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Aynı model referansları hem doğrudan hem de OpenRouter kurulumları için çalışır (örneğin `arcee/trinity-large-thinking`).

## Etkileşimsiz kurulum

### Direct (Arcee platform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Yerleşik katalog

OpenClaw şu anda bu paketlenmiş Arcee kataloğuyla gelir:

Model referansı | Ad | Girdi | Bağlam | Maliyet (1M başına giriş/çıkış) | Notlar  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | metin | 256K | $0.25 / $0.90 | Varsayılan model; akıl yürütme etkin  
`arcee/trinity-large-preview` | Trinity Large Preview | metin | 128K | $0.25 / $1.00 | Genel amaçlı; 400B parametre, 13B aktif  
`arcee/trinity-mini` | Trinity Mini 26B | metin | 128K | $0.045 / $0.15 | Hızlı ve maliyet açısından verimli; fonksiyon çağırma  
  
## Desteklenen özellikler

Özellik | Destekleniyor  
---|---  
Streaming | Evet  
Araç kullanımı / fonksiyon çağırma | Evet (Trinity Mini, Trinity Large Preview)  
Yapılandırılmış çıktı (JSON modu ve JSON şeması) | Evet  
Genişletilmiş düşünme | Evet (Trinity Large Thinking; araçlar devre dışı)  
  
Environment note

Gateway bir daemon (launchd/systemd) olarak çalışıyorsa `ARCEEAI_API_KEY` (veya `OPENROUTER_API_KEY`) değişkeninin bu süreç için kullanılabilir olduğundan emin olun (örneğin `~/.openclaw/.env` içinde veya `env.shellEnv` aracılığıyla).

OpenRouter routing

Arcee modellerini OpenRouter üzerinden kullanırken aynı `arcee/*` model referansları geçerlidir. OpenClaw, kimlik doğrulama seçiminize göre yönlendirmeyi şeffaf biçimde yönetir. OpenRouter'a özgü yapılandırma ayrıntıları için [OpenRouter sağlayıcı belgelerine](</tr/providers/openrouter>) bakın.

## İlgili

[**OpenRouter** Arcee modellerine ve çok daha fazlasına tek bir API anahtarı üzerinden erişin. ](</tr/providers/openrouter>) [**Model selection** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>)

Was this useful?YesNo