---
title: Çıkarım yapar
source_url: https://docs.openclaw.ai/tr/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>), yerel modelleri OpenAI uyumlu bir `/v1` API arkasında sunabilir. OpenClaw, genel `openai-completions` yolu üzerinden `inferrs` ile çalışır.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `inferrs` (özel; `models.providers.inferrs` altında yapılandırın)  
Plugin | yok — `inferrs`, paketlenmiş bir OpenClaw sağlayıcı plugin'i değildir  
Kimlik doğrulama ortam değişkeni | İsteğe bağlı. inferrs sunucunuzda kimlik doğrulama yoksa herhangi bir değer çalışır  
API | OpenAI uyumlu (`openai-completions`)  
Önerilen temel URL | `http://127.0.0.1:8080/v1` (veya inferrs sunucunuzun bulunduğu yer)  
  
## Başlarken

* ### inferrs'i bir modelle başlatın

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Sunucuya erişilebildiğini doğrulayın

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Bir OpenClaw sağlayıcı girdisi ekleyin

Açık bir sağlayıcı girdisi ekleyin ve varsayılan modelinizi ona yönlendirin. Aşağıdaki tam yapılandırma örneğine bakın.

## Tam yapılandırma örneği

Bu örnek, yerel bir `inferrs` sunucusunda Gemma 4 kullanır.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## İstek üzerine başlatma

Inferrs, yalnızca bir `inferrs/...` modeli seçildiğinde OpenClaw tarafından da başlatılabilir. Aynı sağlayıcı girdisine `localService` ekleyin:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` mutlak olmalıdır. Gateway ana makinesinde `which inferrs` kullanın ve bu yolu yapılandırmaya koyun. Tam alan başvurusu için [Yerel model hizmetleri](</tr/gateway/local-model-services>) bölümüne bakın.

## Gelişmiş yapılandırma

requiresStringContent neden önemlidir

Bazı `inferrs` Chat Completions rotaları, yapılandırılmış içerik parçası dizileri yerine yalnızca dize `messages[].content` kabul eder.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw, isteği göndermeden önce saf metin içerik parçalarını düz dizelere dönüştürür.

Gemma ve araç şeması uyarısı

Bazı mevcut `inferrs` \+ Gemma kombinasyonları küçük doğrudan `/v1/chat/completions` isteklerini kabul eder, ancak tam OpenClaw agent-runtime turlarında yine de başarısız olur.

Bu olursa önce şunu deneyin:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Bu, model için OpenClaw'ın araç şeması yüzeyini devre dışı bırakır ve daha katı yerel backend'lerde prompt baskısını azaltabilir.

Küçük doğrudan istekler hâlâ çalışıyor ancak normal OpenClaw ajan turları `inferrs` içinde çökmeye devam ediyorsa, kalan sorun genellikle OpenClaw'ın taşıma katmanından ziyade upstream model/sunucu davranışıdır.

Manuel smoke testi

Yapılandırdıktan sonra iki katmanı da test edin:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

İlk komut çalışıp ikincisi başarısız olursa aşağıdaki sorun giderme bölümünü kontrol edin.

Proxy tarzı davranış

`inferrs`, yerel bir OpenAI uç noktası olarak değil, proxy tarzı OpenAI uyumlu bir `/v1` backend olarak ele alınır.

  * Yalnızca yerel OpenAI istek şekillendirmesi burada uygulanmaz
  * `service_tier` yok, Responses `store` yok, prompt-cache ipuçları yok ve OpenAI reasoning-compat payload şekillendirmesi yok
  * Gizli OpenClaw atıf başlıkları (`originator`, `version`, `User-Agent`) özel `inferrs` temel URL'lerine eklenmez


## Sorun giderme

curl /v1/models başarısız oluyor

`inferrs` çalışmıyor, erişilemiyor veya beklenen host/port'a bağlanmamış. Sunucunun başlatıldığından ve yapılandırdığınız adreste dinlediğinden emin olun.

messages[].content bir dize bekliyordu

Model girdisinde `compat.requiresStringContent: true` ayarlayın. Ayrıntılar için yukarıdaki `requiresStringContent` bölümüne bakın.

Doğrudan /v1/chat/completions çağrıları geçiyor ancak openclaw infer model run başarısız oluyor

Araç şeması yüzeyini devre dışı bırakmak için `compat.supportsTools: false` ayarlamayı deneyin. Yukarıdaki Gemma araç şeması uyarısına bakın.

inferrs daha büyük ajan turlarında hâlâ çöküyor

OpenClaw artık şema hataları almıyorsa ancak `inferrs` daha büyük ajan turlarında hâlâ çöküyorsa, bunu upstream `inferrs` veya model sınırlaması olarak ele alın. Prompt baskısını azaltın veya farklı bir yerel backend'e ya da modele geçin.

## İlgili

[**Yerel modeller** OpenClaw'ı yerel model sunucularına karşı çalıştırma. ](</tr/gateway/local-models>) [**Yerel model hizmetleri** Yapılandırılmış sağlayıcılar için yerel model sunucularını istek üzerine başlatma. ](</tr/gateway/local-model-services>) [**Gateway sorun giderme** Sınamalardan geçen ancak ajan çalıştırmalarında başarısız olan yerel OpenAI uyumlu backend'lerde hata ayıklama. ](</tr/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Model seçimi** Tüm sağlayıcılara, model ref'lerine ve failover davranışına genel bakış. ](</tr/concepts/model-providers>)

Was this useful?YesNo