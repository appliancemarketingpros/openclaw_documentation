---
title: LiteLLM
source_url: https://docs.openclaw.ai/tr/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>), 100+ model sağlayıcısına birleşik API sunan açık kaynaklı bir LLM Gateway’idir. Merkezi maliyet takibi, günlükleme ve OpenClaw yapılandırmanızı değiştirmeden arka uçlar arasında geçiş esnekliği elde etmek için OpenClaw’ı LiteLLM üzerinden yönlendirin.

## Hızlı başlangıç

### Başlangıç kurulumu (önerilir)

**Şunun için en iyisi:** çalışan bir LiteLLM kurulumuna en hızlı yol.

* ### Başlangıç kurulumunu çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Uzak bir proxy’ye karşı etkileşimsiz kurulum için proxy URL’sini açıkça iletin:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manuel kurulum

**Şunun için en iyisi:** kurulum ve yapılandırma üzerinde tam denetim.

* ### LiteLLM Proxy’yi başlatın

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### OpenClaw’ı LiteLLM’e yönlendirin

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Hepsi bu. OpenClaw artık LiteLLM üzerinden yönlendirilir.

## Yapılandırma

### Ortam değişkenleri

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Yapılandırma dosyası

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Gelişmiş yapılandırma

### Görsel üretimi

LiteLLM, OpenAI uyumlu `/images/generations` ve `/images/edits` rotaları üzerinden `image_generate` aracını da destekleyebilir. `agents.defaults.imageGenerationModel` altında bir LiteLLM görsel modeli yapılandırın:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

`http://localhost:4000` gibi loopback LiteLLM URL’leri genel bir özel ağ geçersiz kılması olmadan çalışır. LAN’da barındırılan bir proxy için `models.providers.litellm.request.allowPrivateNetwork: true` ayarını yapın; çünkü API anahtarı yapılandırılmış proxy ana makinesine gönderilecektir.

Sanal anahtarlar

OpenClaw için harcama limitleri olan özel bir anahtar oluşturun:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Üretilen anahtarı `LITELLM_API_KEY` olarak kullanın.

Model yönlendirme

LiteLLM, model isteklerini farklı arka uçlara yönlendirebilir. LiteLLM `config.yaml` dosyanızda yapılandırın:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw `claude-opus-4-6` istemeye devam eder — yönlendirmeyi LiteLLM yönetir.

Kullanımı görüntüleme

LiteLLM’in panosunu veya API’sini kontrol edin:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy davranışı notları

  * LiteLLM varsayılan olarak `http://localhost:4000` üzerinde çalışır
  * OpenClaw, LiteLLM’in proxy tarzı OpenAI uyumlu `/v1` uç noktası üzerinden bağlanır
  * Yerel OpenAI’ye özel istek biçimlendirmesi LiteLLM üzerinden uygulanmaz: `service_tier` yok, Responses `store` yok, prompt cache ipuçları yok ve OpenAI reasoning uyumluluk yükü biçimlendirmesi yok
  * Gizli OpenClaw atıf başlıkları (`originator`, `version`, `User-Agent`) özel LiteLLM temel URL’lerine eklenmez


## İlgili

[**LiteLLM Belgeleri** Resmi LiteLLM belgeleri ve API başvurusu. ](<https://docs.litellm.ai>) [**Model seçimi** Tüm sağlayıcılara, model referanslarına ve yük devretme davranışına genel bakış. ](</tr/concepts/model-providers>) [**Yapılandırma** Tam yapılandırma başvurusu. ](</tr/gateway/configuration>) [**Model seçimi** Modellerin nasıl seçileceği ve yapılandırılacağı. ](</tr/concepts/models>)

Was this useful?YesNo