---
title: Together AI
source_url: https://docs.openclaw.ai/tr/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>), birleşik bir API üzerinden Llama, DeepSeek, Kimi ve daha fazlası dahil önde gelen açık kaynak modellere erişim sağlar.

Özellik | Değer  
---|---  
Sağlayıcı | `together`  
Kimlik doğrulama | `TOGETHER_API_KEY`  
API | OpenAI uyumlu  
Temel URL | `https://api.together.xyz/v1`  
  
## Başlarken

* ### Bir API anahtarı alın

[api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>) adresinde bir API anahtarı oluşturun.

* ### İlk kurulumu çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Varsayılan bir model ayarlayın

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Etkileşimsiz örnek

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Yerleşik katalog

OpenClaw, bu paketlenmiş Together kataloğuyla gelir:

Model ref | Ad | Girdi | Bağlam | Notlar  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | metin, görüntü | 262,144 | Varsayılan model; akıl yürütme etkin  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | metin | 202,752 | Genel amaçlı metin modeli  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | metin | 131,072 | Hızlı yönerge modeli  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | metin, görüntü | 10,000,000 | Çok modlu  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | metin, görüntü | 20,000,000 | Çok modlu  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | metin | 131,072 | Genel metin modeli  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | metin | 131,072 | Akıl yürütme modeli  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | metin | 262,144 | İkincil Kimi metin modeli  
  
## Video oluşturma

Paketlenmiş `together` Plugin'i, paylaşılan `video_generate` aracı üzerinden video oluşturmayı da kaydeder.

Özellik | Değer  
---|---  
Varsayılan video modeli | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modlar | metinden videoya, tek görüntülü referans  
Desteklenen parametreler | `aspectRatio`, `resolution`  
  
Together'ı varsayılan video sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Ortam notu

Gateway bir daemon (launchd/systemd) olarak çalışıyorsa, `TOGETHER_API_KEY` değişkeninin bu süreç tarafından kullanılabilir olduğundan emin olun (örneğin `~/.openclaw/.env` içinde veya `env.shellEnv` aracılığıyla).

Sorun giderme

  * Anahtarınızın çalıştığını doğrulayın: `openclaw models list --provider together`
  * Modeller görünmüyorsa, API anahtarının Gateway süreciniz için doğru ortamda ayarlandığını doğrulayın.
  * Model ref'leri `together/<model-id>` biçimini kullanır.


## İlgili

[**Model seçimi** Sağlayıcı kuralları, model ref'leri ve yük devretme davranışı. ](</tr/concepts/model-providers>) [**Video oluşturma** Paylaşılan video oluşturma aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/video-generation>) [**Yapılandırma referansı** Sağlayıcı ayarları dahil tam yapılandırma şeması. ](</tr/gateway/configuration-reference>) [**Together AI** Together AI panosu, API belgeleri ve fiyatlandırma. ](<https://together.ai>)

Was this useful?YesNo