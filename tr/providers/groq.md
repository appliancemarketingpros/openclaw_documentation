---
title: Groq
source_url: https://docs.openclaw.ai/tr/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>), özel LPU donanımı kullanarak açık ağırlıklı modellerde (Llama, Gemma, Kimi, Qwen, GPT OSS ve daha fazlası) ultra hızlı çıkarım sağlar. OpenClaw, hem OpenAI uyumlu bir sohbet sağlayıcısı hem de sesli medya anlama sağlayıcısı kaydeden yerleşik bir Groq Plugin içerir.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `groq`  
Plugin | yerleşik, `enabledByDefault: true`  
Kimlik doğrulama ortam değişkeni | `GROQ_API_KEY`  
İlk kurulum bayrağı | `--auth-choice groq-api-key`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.groq.com/openai/v1`  
Ses transkripsiyonu | `whisper-large-v3-turbo` (varsayılan)  
Önerilen sohbet varsayılanı | `groq/llama-3.3-70b-versatile`  
  
## Başlarken

* ### Bir API anahtarı alın

[console.groq.com/keys](<https://console.groq.com/keys>) adresinden bir API anahtarı oluşturun.

* ### API anahtarını ayarlayın

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Yalnızca ortamCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Varsayılan bir model ayarlayın

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Kataloğa erişilebildiğini doğrulayın

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Yapılandırma dosyası örneği

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Yerleşik katalog

OpenClaw, hem akıl yürütme hem de akıl yürütme dışı girdiler içeren manifest destekli bir Groq kataloğuyla gelir. Kurulu sürümünüz için yerleşik satırları görmek üzere `openclaw models list --provider groq` komutunu çalıştırın veya Groq'un yetkili listesi için [console.groq.com/docs/models](<https://console.groq.com/docs/models>) adresini kontrol edin.

Model ref | Ad | Akıl yürütme | Girdi | Bağlam  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | hayır | metin | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | hayır | metin | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | hayır | metin + görsel | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | hayır | metin + görsel | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | hayır | metin | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | hayır | metin | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | hayır | metin | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | hayır | metin | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | hayır | metin | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | hayır | metin | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | evet | metin | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | evet | metin | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | evet | metin | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | evet | metin | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | evet | metin | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | evet | metin | 131,072  
`groq/groq/compound` | Compound | evet | metin | 131,072  
`groq/groq/compound-mini` | Compound Mini | evet | metin | 131,072  
  
## Akıl yürütme modelleri

OpenClaw, paylaşılan `/think` düzeylerini Groq'un modele özgü `reasoning_effort` değerlerine eşler:

  * `qwen/qwen3-32b` için devre dışı düşünme `none`, etkin düşünme ise `default` gönderir.
  * Groq GPT OSS akıl yürütme modelleri (`openai/gpt-oss-*`) için OpenClaw, `/think` düzeyine göre `low`, `medium` veya `high` gönderir. Devre dışı düşünme `reasoning_effort` değerini çıkarır, çünkü bu modeller devre dışı bir değeri desteklemez.
  * DeepSeek R1 Distill, Qwen QwQ ve Compound, Groq'un yerel akıl yürütme yüzeyini kullanır; `/think` görünürlüğü kontrol eder ancak model her zaman akıl yürütür.


Paylaşılan `/think` düzeyleri ve OpenClaw'ın bunları sağlayıcı başına nasıl çevirdiği için [Düşünme modları](</tr/tools/thinking>) bölümüne bakın.

## Ses transkripsiyonu

Groq'un yerleşik Plugin'i ayrıca sesli mesajların paylaşılan `tools.media.audio` yüzeyi üzerinden transkribe edilebilmesi için bir **sesli medya anlama sağlayıcısı** kaydeder.

Özellik | Değer  
---|---  
Paylaşılan yapılandırma yolu | `tools.media.audio`  
Varsayılan temel URL | `https://api.groq.com/openai/v1`  
Varsayılan model | `whisper-large-v3-turbo`  
Otomatik öncelik | 20  
API uç noktası | OpenAI uyumlu `/audio/transcriptions`  
  
Groq'u varsayılan ses arka ucu yapmak için:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Daemon için ortam erişilebilirliği

Gateway yönetilen bir servis olarak çalışıyorsa (launchd, systemd, Docker), `GROQ_API_KEY` yalnızca etkileşimli kabuğunuzda değil, o süreç tarafından da görünür olmalıdır.

Özel Groq model kimlikleri

OpenClaw çalışma zamanında herhangi bir Groq model kimliğini kabul eder. Groq tarafından gösterilen tam kimliği kullanın ve başına `groq/` ekleyin. Yerleşik katalog yaygın durumları kapsar; katalogda olmayan kimlikler varsayılan OpenAI uyumlu şablona düşer.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## İlgili

[**Model sağlayıcıları** Sağlayıcı, model ref değerleri ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Düşünme modları** Akıl yürütme çabası düzeyleri ve sağlayıcı ilkesi etkileşimi. ](</tr/tools/thinking>) [**Yapılandırma başvurusu** Sağlayıcı ve ses ayarlarını içeren tam yapılandırma şeması. ](</tr/gateway/configuration-reference>) [**Groq Console** Groq panosu, API belgeleri ve fiyatlandırma. ](<https://console.groq.com>)

Was this useful?YesNo