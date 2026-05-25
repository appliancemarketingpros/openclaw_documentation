---
title: vLLM
source_url: https://docs.openclaw.ai/tr/providers/vllm
scraped_at: 2026-05-25
---

vLLM, açık kaynaklı (ve bazı özel) modelleri **OpenAI uyumlu** bir HTTP API aracılığıyla sunabilir. OpenClaw, `openai-completions` API kullanarak vLLM'ye bağlanır.

OpenClaw, `VLLM_API_KEY` ile dahil olduğunuzda vLLM'den kullanılabilir modelleri de **otomatik keşfedebilir** (sunucunuz kimlik doğrulamayı zorunlu kılmıyorsa herhangi bir değer çalışır). Özel bir vLLM temel URL'si de yapılandırdığınızda keşfi dinamik tutmak için `agents.defaults.models` içinde `vllm/*` kullanın.

OpenClaw, `vllm` değerini akışlı kullanım muhasebesini destekleyen yerel OpenAI uyumlu bir sağlayıcı olarak ele alır; böylece durum/bağlam token sayıları `stream_options.include_usage` yanıtlarından güncellenebilir.

Özellik | Değer  
---|---  
Sağlayıcı Kimliği | `vllm`  
API | `openai-completions` (OpenAI uyumlu)  
Kimlik doğrulama | `VLLM_API_KEY` ortam değişkeni  
Varsayılan temel URL | `http://127.0.0.1:8000/v1`  
  
## Başlarken

* ### vLLM'yi OpenAI uyumlu bir sunucuyla başlatın

Temel URL'niz `/v1` uç noktalarını sunmalıdır (ör. `/v1/models`, `/v1/chat/completions`). vLLM genellikle şu adreste çalışır:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### API anahtarı ortam değişkenini ayarlayın

Sunucunuz kimlik doğrulamayı zorunlu kılmıyorsa herhangi bir değer çalışır:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### Bir model seçin

Kendi vLLM model kimliklerinizden biriyle değiştirin:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## Model keşfi (örtük sağlayıcı)

`VLLM_API_KEY` ayarlandığında (veya bir kimlik doğrulama profili bulunduğunda) ve `models.providers.vllm` tanımlamadığınızda OpenClaw şu sorguyu yapar:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

ve dönen kimlikleri model girdilerine dönüştürür.

## Açık yapılandırma (manuel modeller)

Açık yapılandırmayı şu durumlarda kullanın:

  * vLLM farklı bir ana makinede veya bağlantı noktasında çalışıyorsa
  * `contextWindow` veya `maxTokens` değerlerini sabitlemek istiyorsanız
  * Sunucunuz gerçek bir API anahtarı gerektiriyorsa (veya üst bilgileri kontrol etmek istiyorsanız)
  * Güvenilir bir loopback, LAN veya Tailscale vLLM uç noktasına bağlanıyorsanız

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Her modeli manuel olarak listelemeden bu sağlayıcıyı dinamik tutmak için görünür model kataloğuna bir sağlayıcı joker karakteri ekleyin:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## Gelişmiş yapılandırma

Proxy tarzı davranış

vLLM, yerel bir OpenAI uç noktası olarak değil, proxy tarzı OpenAI uyumlu bir `/v1` arka ucu olarak ele alınır. Bunun anlamı:

Davranış | Uygulandı mı?  
---|---  
Yerel OpenAI istek şekillendirmesi | Hayır  
`service_tier` | Gönderilmez  
Responses `store` | Gönderilmez  
İstem önbelleği ipuçları | Gönderilmez  
OpenAI reasoning uyumluluk yükü şekillendirmesi | Uygulanmaz  
Gizli OpenClaw atıf üst bilgileri | Özel temel URL'lerde enjekte edilmez  
Qwen düşünme denetimleri

vLLM üzerinden sunulan Qwen modelleri için, sunucu Qwen sohbet şablonu kwargs beklediğinde model girdisinde `params.qwenThinkingFormat: "chat-template"` ayarlayın. OpenClaw `/think off` değerini şuna eşler:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

`off` dışındaki düşünme düzeyleri `enable_thinking: true` gönderir. Uç noktanız bunun yerine DashScope tarzı üst düzey bayraklar bekliyorsa istek kökünde `enable_thinking` göndermek için `params.qwenThinkingFormat: "top-level"` kullanın. Snake-case `params.qwen_thinking_format` da kabul edilir.

Nemotron 3 düşünme denetimleri

vLLM/Nemotron 3, reasoning'in gizli reasoning veya görünür yanıt metni olarak döndürülüp döndürülmeyeceğini kontrol etmek için sohbet şablonu kwargs kullanabilir. Bir OpenClaw oturumu düşünme kapalıyken `vllm/nemotron-3-*` kullandığında, paketli vLLM Plugin şunu gönderir:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

Bu değerleri özelleştirmek için model parametreleri altında `chat_template_kwargs` ayarlayın. Ayrıca `params.extra_body.chat_template_kwargs` ayarlarsanız, `extra_body` son istek gövdesi geçersiz kılması olduğundan bu değer son önceliğe sahip olur.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Qwen araç çağrıları metin olarak görünür

Önce vLLM'nin model için doğru araç çağrısı ayrıştırıcısı ve sohbet şablonuyla başlatıldığından emin olun. Örneğin vLLM, Qwen2.5 modelleri için `hermes` ve Qwen3-Coder modelleri için `qwen3_xml` belgeler.

Belirtiler:

  * skills veya araçlar hiç çalışmaz
  * asistan `{"name":"read","arguments":...}` gibi ham JSON/XML yazdırır
  * OpenClaw `tool_choice: "auto"` gönderdiğinde vLLM boş bir `tool_calls` dizisi döndürür


Bazı Qwen/vLLM kombinasyonları yapılandırılmış araç çağrılarını yalnızca istek `tool_choice: "required"` kullandığında döndürür. Bu model girdileri için OpenAI uyumlu istek alanını `params.extra_body` ile zorlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

`Qwen-Qwen2.5-Coder-32B-Instruct` değerini şu komutun döndürdüğü tam kimlikle değiştirin:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

Aynı geçersiz kılmayı CLI üzerinden uygulayabilirsiniz:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

Bu, isteğe bağlı bir uyumluluk geçici çözümüdür. Araçlarla yapılan her model turunun bir araç çağrısı gerektirmesine neden olur; bu yüzden yalnızca bu davranışın kabul edilebilir olduğu özel bir yerel model girdisi için kullanın. Bunu tüm vLLM modelleri için genel varsayılan olarak kullanmayın ve rastgele asistan metnini körü körüne çalıştırılabilir araç çağrılarına dönüştüren bir proxy kullanmayın.

Özel temel URL

vLLM sunucunuz varsayılan olmayan bir ana makinede veya bağlantı noktasında çalışıyorsa açık sağlayıcı yapılandırmasında `baseUrl` ayarlayın:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Sorun giderme

Yavaş ilk yanıt veya uzak sunucu zaman aşımı

Büyük yerel modeller, uzak LAN ana makineleri veya tailnet bağlantıları için sağlayıcı kapsamlı bir istek zaman aşımı ayarlayın:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` yalnızca bağlantı kurulumu, yanıt üst bilgileri, gövde akışı ve toplam korumalı fetch iptali dahil olmak üzere vLLM model HTTP isteklerine uygulanır. Tüm agent çalışmasını kontrol eden `agents.defaults.timeoutSeconds` değerini artırmadan önce bunu tercih edin.

Sunucuya ulaşılamıyor

vLLM sunucusunun çalıştığını ve erişilebilir olduğunu kontrol edin:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

Bir bağlantı hatası görürseniz ana makineyi, bağlantı noktasını ve vLLM'nin OpenAI uyumlu sunucu moduyla başlatıldığını doğrulayın. Açık loopback, LAN veya Tailscale uç noktaları için ayrıca `models.providers.vllm.request.allowPrivateNetwork: true` ayarlayın; sağlayıcı açıkça güvenilir olarak işaretlenmedikçe sağlayıcı istekleri varsayılan olarak özel ağ URL'lerini engeller.

İsteklerde kimlik doğrulama hataları

İstekler kimlik doğrulama hatalarıyla başarısız olursa, sunucu yapılandırmanızla eşleşen gerçek bir `VLLM_API_KEY` ayarlayın veya sağlayıcıyı `models.providers.vllm` altında açıkça yapılandırın.

Hiç model keşfedilmedi

Otomatik keşif için `VLLM_API_KEY` ayarlanmış olmalıdır. `models.providers.vllm` tanımladıysanız, `agents.defaults.models` `"vllm/*": {}` içermediği sürece OpenClaw yalnızca bildirdiğiniz modelleri kullanır.

Araçlar ham metin olarak işleniyor

Bir Qwen modeli bir skill çalıştırmak yerine JSON/XML araç söz dizimi yazdırıyorsa yukarıdaki Gelişmiş yapılandırma bölümündeki Qwen yönergelerini kontrol edin. Olağan düzeltme şudur:

  * vLLM'yi o model için doğru ayrıştırıcı/şablonla başlatın
  * tam model kimliğini `openclaw models list --provider vllm` ile onaylayın
  * yalnızca `tool_choice: "auto"` hâlâ boş veya yalnızca metin araç çağrıları döndürüyorsa özel model başına `params.extra_body.tool_choice: "required"` geçersiz kılmasını ekleyin


## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**OpenAI** Yerel OpenAI sağlayıcısı ve OpenAI uyumlu rota davranışı. ](</tr/providers/openai>) [**OAuth ve kimlik doğrulama** Kimlik doğrulama ayrıntıları ve kimlik bilgisi yeniden kullanım kuralları. ](</tr/gateway/authentication>) [**Sorun giderme** Yaygın sorunlar ve bunların nasıl çözüleceği. ](</tr/help/troubleshooting>)

Was this useful?YesNo