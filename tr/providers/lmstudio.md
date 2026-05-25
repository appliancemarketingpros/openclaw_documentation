---
title: LM Studio
source_url: https://docs.openclaw.ai/tr/providers/lmstudio
scraped_at: 2026-05-25
---

LM Studio, kendi donanımınızda açık ağırlıklı modeller çalıştırmak için dostane ama güçlü bir uygulamadır. llama.cpp (GGUF) veya MLX modellerini (Apple Silicon) çalıştırmanızı sağlar. GUI paketi veya başsız daemon (`llmster`) olarak gelir. Ürün ve kurulum belgeleri için [lmstudio.ai](<https://lmstudio.ai/>) adresine bakın.

## Hızlı başlangıç

  1. LM Studio'yu (masaüstü) veya `llmster`'ı (başsız) kurun, ardından yerel sunucuyu başlatın:

bashCopy code
[code]
    curl -fsSL https://lmstudio.ai/install.sh | bash
[/code]

  2. Sunucuyu başlatın


Masaüstü uygulamayı başlattığınızdan veya daemon'ı şu komutla çalıştırdığınızdan emin olun:

bashCopy code
[code]
    lms daemon up
[/code]

bashCopy code
[code]
    lms server start --port 1234
[/code]

Uygulamayı kullanıyorsanız, sorunsuz bir deneyim için JIT'in etkin olduğundan emin olun. Daha fazla bilgi için [LM Studio JIT ve TTL kılavuzuna](<https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict>) bakın.

  3. LM Studio kimlik doğrulaması etkinse `LM_API_TOKEN` ayarlayın:

bashCopy code
[code]
    export LM_API_TOKEN="your-lm-studio-api-token"
[/code]

LM Studio kimlik doğrulaması devre dışıysa, etkileşimli OpenClaw kurulumu sırasında API anahtarını boş bırakabilirsiniz.

LM Studio kimlik doğrulaması kurulum ayrıntıları için [LM Studio Authentication](<https://lmstudio.ai/docs/developer/core/authentication>) sayfasına bakın.

  4. İlk kurulumu çalıştırın ve `LM Studio` seçin:

bashCopy code
[code]
    openclaw onboard
[/code]

  5. İlk kurulumda, LM Studio modelinizi seçmek için `Default model` istemini kullanın.


Daha sonra da ayarlayabilir veya değiştirebilirsiniz:

bashCopy code
[code]
    openclaw models set lmstudio/qwen/qwen3.5-9b
[/code]

LM Studio model anahtarları `author/model-name` biçimini izler (ör. `qwen/qwen3.5-9b`). OpenClaw model referansları sağlayıcı adını başa ekler: `lmstudio/qwen/qwen3.5-9b`. Bir modelin tam anahtarını `curl http://localhost:1234/api/v1/models` çalıştırıp `key` alanına bakarak bulabilirsiniz.

## Etkileşimsiz ilk kurulum

Kurulumu betiklemek istediğinizde (CI, provizyonlama, uzaktan bootstrap) etkileşimsiz ilk kurulumu kullanın:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio
[/code]

Veya temel URL'yi, modeli ve isteğe bağlı API anahtarını belirtin:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio \  --custom-base-url http://localhost:1234/v1 \  --lmstudio-api-key "$LM_API_TOKEN" \  --custom-model-id qwen/qwen3.5-9b
[/code]

`--custom-model-id`, LM Studio tarafından döndürülen model anahtarını alır (ör. `qwen/qwen3.5-9b`), `lmstudio/` sağlayıcı öneki olmadan.

Kimliği doğrulanmış LM Studio sunucuları için `--lmstudio-api-key` geçirin veya `LM_API_TOKEN` ayarlayın. Kimlik doğrulaması olmayan LM Studio sunucuları için anahtarı atlayın; OpenClaw yerel, gizli olmayan bir işaretçi depolar.

`--custom-api-key` uyumluluk için desteklenmeye devam eder, ancak LM Studio için `--lmstudio-api-key` tercih edilir.

Bu, `models.providers.lmstudio` yazar ve varsayılan modeli `lmstudio/<custom-model-id>` olarak ayarlar. Bir API anahtarı sağladığınızda, kurulum ayrıca `lmstudio:default` kimlik doğrulama profilini yazar.

Etkileşimli kurulum, isteğe bağlı tercih edilen yükleme bağlamı uzunluğu sorabilir ve bunu yapılandırmaya kaydettiği keşfedilmiş LM Studio modelleri genelinde uygular. LM Studio Plugin yapılandırması, loopback, LAN ve tailnet ana makineleri dahil olmak üzere model istekleri için yapılandırılmış LM Studio uç noktasına güvenir. `models.providers.lmstudio.request.allowPrivateNetwork: false` ayarlayarak bundan vazgeçebilirsiniz.

## Yapılandırma

### Akış kullanım uyumluluğu

LM Studio, akış kullanımıyla uyumludur. OpenAI biçimli bir `usage` nesnesi yaymadığında, OpenClaw bunun yerine token sayılarını llama.cpp tarzı `timings.prompt_n` / `timings.predicted_n` meta verilerinden kurtarır.

Aynı akış kullanım davranışı şu OpenAI uyumlu yerel arka uçlar için geçerlidir:

  * vLLM
  * SGLang
  * llama.cpp
  * LocalAI
  * Jan
  * TabbyAPI
  * text-generation-webui


### Düşünme uyumluluğu

LM Studio'nun `/api/v1/models` keşfi modele özgü muhakeme seçenekleri bildirdiğinde, OpenClaw model uyumluluk meta verilerinde eşleşen OpenAI uyumlu `reasoning_effort` değerlerini açığa çıkarır. Güncel LM Studio derlemeleri, bu değerleri `/v1/chat/completions` üzerinde reddederken `allowed_options: ["off", "on"]` gibi ikili UI seçeneklerinin reklamını yapabilir; OpenClaw bu ikili keşif biçimini istek göndermeden önce `none`, `minimal`, `low`, `medium`, `high` ve `xhigh` değerlerine normalleştirir. `off`/`on` muhakeme eşlemeleri içeren eski kaydedilmiş LM Studio yapılandırması da katalog yüklendiğinde aynı şekilde normalleştirilir.

### Açık yapılandırma

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        models: [          {            id: "qwen/qwen3-coder-next",            name: "Qwen 3 Coder Next",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Sorun giderme

### LM Studio algılanmadı

LM Studio'nun çalıştığından emin olun. Kimlik doğrulaması etkinse `LM_API_TOKEN` da ayarlayın:

bashCopy code
[code]
    # Start via desktop app, or headless:lms server start --port 1234
[/code]

API'nin erişilebilir olduğunu doğrulayın:

bashCopy code
[code]
    curl http://localhost:1234/api/v1/models
[/code]

### Kimlik doğrulama hataları (HTTP 401)

Kurulum HTTP 401 bildirirse API anahtarınızı doğrulayın:

  * `LM_API_TOKEN` değerinin LM Studio'da yapılandırılan anahtarla eşleştiğini kontrol edin.
  * LM Studio kimlik doğrulaması kurulum ayrıntıları için [LM Studio Authentication](<https://lmstudio.ai/docs/developer/core/authentication>) sayfasına bakın.
  * Sunucunuz kimlik doğrulaması gerektirmiyorsa, kurulum sırasında anahtarı boş bırakın.


### Tam zamanında model yükleme

LM Studio, modellerin ilk istekte yüklendiği tam zamanında (JIT) model yüklemeyi destekler. OpenClaw varsayılan olarak modelleri LM Studio'nun yerel yükleme uç noktası üzerinden önceden yükler; bu, JIT devre dışıyken yardımcı olur. LM Studio'nun JIT, boşta TTL ve otomatik çıkarma davranışının model yaşam döngüsünü sahiplenmesine izin vermek için OpenClaw'ın ön yükleme adımını devre dışı bırakın:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        api: "openai-completions",        params: { preload: false },        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

### LAN veya tailnet LM Studio ana makinesi

LM Studio ana makinesinin erişilebilir adresini kullanın, `/v1` yolunu koruyun ve LM Studio'nun o makinede loopback ötesine bağlı olduğundan emin olun:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://gpu-box.local:1234/v1",        apiKey: "lmstudio",        api: "openai-completions",        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

Genel OpenAI uyumlu sağlayıcıların aksine, `lmstudio` korumalı model istekleri için yapılandırılmış yerel/özel uç noktasına otomatik olarak güvenir. `localhost` veya `127.0.0.1` gibi özel loopback sağlayıcı kimliklerine de otomatik olarak güvenilir; LAN, tailnet veya özel DNS özel sağlayıcı kimlikleri için `models.providers.<id>.request.allowPrivateNetwork: true` açıkça ayarlayın.

## İlgili

  * [Model seçimi](</tr/concepts/model-providers>)
  * [Ollama](</tr/providers/ollama>)
  * [Yerel modeller](</tr/gateway/local-models>)


Was this useful?YesNo