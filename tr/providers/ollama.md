---
title: Ollama
source_url: https://docs.openclaw.ai/tr/providers/ollama
scraped_at: 2026-05-25
---

OpenClaw, barındırılan bulut modelleri ve yerel/kendi barındırdığınız Ollama sunucuları için Ollama'nın yerel API'siyle (`/api/chat`) entegre olur. Ollama'yı üç modda kullanabilirsiniz: erişilebilir bir Ollama ana makinesi üzerinden `Cloud + Local`, `https://ollama.com` üzerinden `Cloud only` veya erişilebilir bir Ollama ana makinesi üzerinden `Local only`.

Ollama sağlayıcı yapılandırması, kanonik anahtar olarak `baseUrl` kullanır. OpenClaw, OpenAI SDK tarzı örneklerle uyumluluk için `baseURL` değerini de kabul eder, ancak yeni yapılandırmalar `baseUrl` değerini tercih etmelidir.

## Kimlik doğrulama kuralları

Yerel ve LAN ana makineleri

Yerel ve LAN Ollama ana makineleri gerçek bir bearer token gerektirmez. OpenClaw, yerel `ollama-local` işaretçisini yalnızca loopback, özel ağ, `.local` ve yalın ana makine adlı Ollama temel URL'leri için kullanır.

Uzak ve Ollama Cloud ana makineleri

Uzak genel ana makineler ve Ollama Cloud (`https://ollama.com`), `OLLAMA_API_KEY`, bir kimlik doğrulama profili veya sağlayıcının `apiKey` değeri üzerinden gerçek bir kimlik bilgisi gerektirir.

Özel sağlayıcı kimlikleri

`api: "ollama"` ayarlayan özel sağlayıcı kimlikleri aynı kuralları izler. Örneğin, özel bir LAN Ollama ana makinesini işaret eden bir `ollama-remote` sağlayıcısı `apiKey: "ollama-local"` kullanabilir ve alt ajanlar, bunu eksik bir kimlik bilgisi olarak ele almak yerine Ollama sağlayıcı kancası üzerinden çözer. Bellek araması da `agents.defaults.memorySearch.provider` değerini bu özel sağlayıcı kimliğine ayarlayabilir; böylece embedding'ler eşleşen Ollama uç noktasını kullanır.

Kimlik doğrulama profilleri

`auth-profiles.json`, bir sağlayıcı kimliği için kimlik bilgisini depolar. Uç nokta ayarlarını (`baseUrl`, `api`, model kimlikleri, üstbilgiler, zaman aşımları) `models.providers.<id>` içine koyun. `{ "ollama-windows": { "apiKey": "ollama-local" } }` gibi eski düz kimlik doğrulama profili dosyaları bir çalışma zamanı biçimi değildir; bunları yedekle birlikte kanonik `ollama-windows:default` API anahtarı profiline yeniden yazmak için `openclaw doctor --fix` çalıştırın. Bu dosyadaki `baseUrl` uyumluluk gürültüsüdür ve sağlayıcı yapılandırmasına taşınmalıdır.

Bellek embedding kapsamı

Ollama bellek embedding'leri için kullanıldığında, bearer kimlik doğrulaması bildirildiği ana makineyle sınırlıdır:

  * Sağlayıcı düzeyindeki anahtar yalnızca o sağlayıcının Ollama ana makinesine gönderilir.
  * `agents.*.memorySearch.remote.apiKey` yalnızca kendi uzak embedding ana makinesine gönderilir.
  * Saf bir `OLLAMA_API_KEY` ortam değeri, Ollama Cloud kuralı olarak ele alınır; varsayılan olarak yerel veya kendi barındırdığınız ana makinelere gönderilmez.


## Başlarken

Tercih ettiğiniz kurulum yöntemini ve modu seçin.

### Başlatma (önerilir)

**En uygunu:** çalışan bir Ollama bulut veya yerel kurulumuna en hızlı yol.

* ### Başlatmayı çalıştırın

bashCopy code
[code]
    openclaw onboard
[/code]

Sağlayıcı listesinden **Ollama** öğesini seçin.

* ### Modunuzu seçin

  * **Cloud + Local** — yerel Ollama ana makinesi ve bu ana makine üzerinden yönlendirilen bulut modelleri
  * **Cloud only** — `https://ollama.com` üzerinden barındırılan Ollama modelleri
  * **Local only** — yalnızca yerel modeller


* ### Bir model seçin

`Cloud only`, `OLLAMA_API_KEY` ister ve barındırılan bulut varsayılanlarını önerir. `Cloud + Local` ve `Local only`, bir Ollama temel URL'si ister, kullanılabilir modelleri keşfeder ve seçilen yerel modeli henüz mevcut değilse otomatik olarak çeker. Ollama, `gemma4:latest` gibi yüklü bir `:latest` etiketi bildirdiğinde kurulum, hem `gemma4` hem de `gemma4:latest` göstermenin veya yalın takma adı yeniden çekmenin yerine bu yüklü modeli bir kez gösterir. `Cloud + Local`, ilgili Ollama ana makinesinin bulut erişimi için oturum açmış olup olmadığını da denetler.

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider ollama
[/code]

### Etkileşimsiz mod

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --accept-risk
[/code]

İsteğe bağlı olarak özel bir temel URL veya model belirtin:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

### Elle kurulum

**En uygunu:** bulut veya yerel kurulum üzerinde tam denetim.

* ### Bulut veya yereli seçin

  * **Cloud + Local** : Ollama'yı kurun, `ollama signin` ile oturum açın ve bulut isteklerini bu ana makine üzerinden yönlendirin
  * **Cloud only** : `OLLAMA_API_KEY` ile `https://ollama.com` kullanın
  * **Local only** : Ollama'yı [ollama.com/download](<https://ollama.com/download>) adresinden kurun


* ### Yerel bir modeli çekin (yalnızca yerel)

bashCopy code
[code]
    ollama pull gemma4# orollama pull gpt-oss:20b# orollama pull llama3.3
[/code]

* ### OpenClaw için Ollama'yı etkinleştirin

`Cloud only` için gerçek `OLLAMA_API_KEY` değerinizi kullanın. Ana makine destekli kurulumlar için herhangi bir yer tutucu değer çalışır:

bashCopy code
[code]
    # Cloudexport OLLAMA_API_KEY="your-ollama-api-key" # Local-onlyexport OLLAMA_API_KEY="ollama-local" # Or configure in your config fileopenclaw config set models.providers.ollama.apiKey "OLLAMA_API_KEY"
[/code]

* ### Modelinizi inceleyin ve ayarlayın

bashCopy code
[code]
    openclaw models listopenclaw models set ollama/gemma4
[/code]

Veya varsayılanı yapılandırmada ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ollama/gemma4" },    },  },}
[/code]

## Bulut modelleri

### Cloud + Local

`Cloud + Local`, hem yerel hem de bulut modelleri için denetim noktası olarak erişilebilir bir Ollama ana makinesi kullanır. Bu, Ollama'nın tercih ettiği hibrit akıştır.

Kurulum sırasında **Cloud + Local** kullanın. OpenClaw, Ollama temel URL'sini ister, bu ana makineden yerel modelleri keşfeder ve `ollama signin` ile ana makinenin bulut erişimi için oturum açmış olup olmadığını denetler. Ana makine oturum açmışsa OpenClaw ayrıca `kimi-k2.5:cloud`, `minimax-m2.7:cloud` ve `glm-5.1:cloud` gibi barındırılan bulut varsayılanlarını önerir.

Ana makine henüz oturum açmamışsa OpenClaw, siz `ollama signin` çalıştırana kadar kurulumu yalnızca yerel tutar.

### Cloud only

`Cloud only`, `https://ollama.com` adresindeki Ollama'nın barındırılan API'sine karşı çalışır.

Kurulum sırasında **Cloud only** kullanın. OpenClaw, `OLLAMA_API_KEY` ister, `baseUrl: "https://ollama.com"` ayarlar ve barındırılan bulut model listesini başlatır. Bu yol, yerel bir Ollama sunucusu veya `ollama signin` gerektirmez.

`openclaw onboard` sırasında gösterilen bulut model listesi, `https://ollama.com/api/tags` adresinden canlı olarak doldurulur ve 500 girdiyle sınırlandırılır; böylece seçici statik bir başlangıç listesi yerine mevcut barındırılan kataloğu yansıtır. `ollama.com` erişilemezse veya kurulum sırasında hiç model döndürmezse OpenClaw, başlatmanın yine de tamamlanması için önceki sabit kodlanmış önerilere geri döner.

### Local only

Yalnızca yerel modda OpenClaw, yapılandırılan Ollama örneğinden modelleri keşfeder. Bu yol, yerel veya kendi barındırdığınız Ollama sunucuları içindir.

OpenClaw şu anda yerel varsayılan olarak `gemma4` önerir.

## Model keşfi (örtük sağlayıcı)

`OLLAMA_API_KEY` (veya bir kimlik doğrulama profili) ayarladığınızda ve `models.providers.ollama` ya da `api: "ollama"` içeren başka bir özel uzak sağlayıcı tanımlamadığınızda OpenClaw, `http://127.0.0.1:11434` adresindeki yerel Ollama örneğinden modelleri keşfeder.

Davranış | Ayrıntı  
---|---  
Katalog sorgusu | `/api/tags` sorgular  
Yetenek algılama | `contextWindow`, genişletilmiş `num_ctx` Modelfile parametreleri ve görme/araçlar dahil yetenekleri okumak için en iyi çaba `/api/show` aramalarını kullanır  
Görme modelleri | `/api/show` tarafından bildirilen `vision` yeteneğine sahip modeller görüntü yetenekli (`input: ["text", "image"]`) olarak işaretlenir; böylece OpenClaw görüntüleri prompt'a otomatik olarak enjekte eder  
Akıl yürütme algılama | Kullanılabilir olduğunda `thinking` dahil `/api/show` yeteneklerini kullanır; Ollama yetenekleri atladığında model adı sezgisel kuralına (`r1`, `reasoning`, `think`) geri döner  
Token sınırları | `maxTokens` değerini OpenClaw tarafından kullanılan varsayılan Ollama maksimum token sınırına ayarlar  
Maliyetler | Tüm maliyetleri `0` olarak ayarlar  
  
Bu, kataloğu yerel Ollama örneğiyle hizalı tutarken elle model girdileri oluşturma ihtiyacını ortadan kaldırır. Yerel `infer model run` içinde `ollama/<pulled-model>:latest` gibi tam bir ref kullanabilirsiniz; OpenClaw bu yüklü modeli, elle yazılmış bir `models.json` girdisi gerektirmeden Ollama'nın canlı kataloğundan çözer.

Oturum açılmış Ollama ana makinelerinde, bazı `:cloud` modeller `/api/tags` içinde görünmeden önce `/api/chat` ve `/api/show` üzerinden kullanılabilir olabilir. Tam bir `ollama/<model>:cloud` ref'ini açıkça seçtiğinizde, OpenClaw eksik olan bu modeli `/api/show` ile doğrular ve yalnızca Ollama model metadatasını doğrularsa çalışma zamanı kataloğuna ekler. Yazım hataları yine otomatik oluşturulmak yerine bilinmeyen model olarak başarısız olur.

bashCopy code
[code]
    # See what models are availableollama listopenclaw models list
[/code]

Tam ajan araç yüzeyinden kaçınan dar bir metin üretimi duman testi için, tam bir Ollama model ref'iyle yerel `infer model run` kullanın:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/llama3.2:latest \    --prompt "Reply with exactly: pong" \    --json
[/code]

Bu yol yine de OpenClaw'ın yapılandırılmış sağlayıcısını, kimlik doğrulamasını ve yerel Ollama taşımasını kullanır, ancak bir sohbet ajanı turu başlatmaz veya MCP/araç bağlamı yüklemez. Bu başarılı olurken normal ajan yanıtları başarısız olursa, sonraki adımda modelin ajan prompt/araç kapasitesini sorun giderin.

Aynı yalın yolda dar bir görme modeli duman testi için `infer model run` komutuna bir veya daha fazla görüntü dosyası ekleyin. Bu, prompt'u ve görüntüyü sohbet araçlarını, belleği veya önceki oturum bağlamını yüklemeden doğrudan seçilen Ollama görme modeline gönderir:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/qwen2.5vl:7b \    --prompt "Describe this image in one sentence." \    --file ./photo.jpg \    --json
[/code]

`model run --file`, yaygın PNG, JPEG ve WebP girdileri dahil `image/*` olarak algılanan dosyaları kabul eder. Görüntü olmayan dosyalar, Ollama çağrılmadan önce reddedilir. Konuşma tanıma için bunun yerine `openclaw infer audio transcribe` kullanın.

Bir konuşmayı `/model ollama/<model>` ile değiştirdiğinizde OpenClaw bunu tam bir kullanıcı seçimi olarak ele alır. Yapılandırılan Ollama `baseUrl` değeri erişilemez durumdaysa, sonraki yanıt başka bir yapılandırılmış yedek modelden sessizce yanıt vermek yerine sağlayıcı hatasıyla başarısız olur.

İzole cron işleri, agent dönüşünü başlatmadan önce fazladan bir yerel güvenlik denetimi yapar. Seçilen model yerel, özel ağ veya `.local` Ollama sağlayıcısına çözümlenirse ve `/api/tags` erişilemez durumdaysa OpenClaw, bu cron çalıştırmasını hata metninde seçilen `ollama/<model>` ile `skipped` olarak kaydeder. Uç nokta ön denetimi 5 dakika boyunca önbelleğe alınır; bu nedenle aynı durdurulmuş Ollama daemon’una yönlendirilmiş birden fazla cron işi, hepsi birden başarısız model istekleri başlatmaz.

Yerel metin yolunu, yerel akış yolunu ve embeddings’i yerel Ollama’ya karşı canlı doğrulamak için:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA=1 OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=0 \  pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

Yeni bir model eklemek için modeli Ollama ile çekmeniz yeterlidir:

bashCopy code
[code]
    ollama pull mistral
[/code]

Yeni model otomatik olarak keşfedilir ve kullanıma hazır olur.

## Görü ve görüntü açıklaması

Paketle gelen Ollama Plugin’i, Ollama’yı görüntü yetenekli bir medya anlama sağlayıcısı olarak kaydeder. Bu, OpenClaw’ın açık görüntü açıklama isteklerini ve yapılandırılmış görüntü modeli varsayılanlarını yerel veya barındırılan Ollama görü modelleri üzerinden yönlendirmesini sağlar.

Yerel görü için görüntüleri destekleyen bir model çekin:

bashCopy code
[code]
    ollama pull qwen2.5vl:7bexport OLLAMA_API_KEY="ollama-local"
[/code]

Ardından infer CLI ile doğrulayın:

bashCopy code
[code]
    openclaw infer image describe \  --file ./photo.jpg \  --model ollama/qwen2.5vl:7b \  --json
[/code]

`--model` tam bir `<provider/model>` başvurusu olmalıdır. Ayarlandığında `openclaw infer image describe`, model yerel görüyü desteklediği için açıklamayı atlamak yerine bu modeli doğrudan çalıştırır.

OpenClaw’ın görüntü anlama sağlayıcı akışını, yapılandırılmış `agents.defaults.imageModel` değerini ve görüntü açıklama çıktı biçimini istediğinizde `infer image describe` kullanın. Özel bir prompt ve bir veya daha fazla görüntüyle ham multimodal model yoklaması istediğinizde `infer model run --file` kullanın.

Ollama’yı gelen medya için varsayılan görüntü anlama modeli yapmak üzere `agents.defaults.imageModel` yapılandırın:

json5Copy code
[code]
    {  agents: {    defaults: {      imageModel: {        primary: "ollama/qwen2.5vl:7b",      },    },  },}
[/code]

Tam `ollama/<model>` başvurusunu tercih edin. Aynı model `models.providers.ollama.models` altında `input: ["text", "image"]` ile listelenmişse ve yapılandırılmış başka hiçbir görüntü sağlayıcı bu yalın model kimliğini açığa çıkarmıyorsa OpenClaw, `qwen2.5vl:7b` gibi yalın bir `imageModel` başvurusunu da `ollama/qwen2.5vl:7b` olarak normalleştirir. Aynı yalın kimliğe birden fazla yapılandırılmış görüntü sağlayıcı sahipse sağlayıcı önekini açıkça kullanın.

Yavaş yerel görü modelleri, bulut modellerinden daha uzun bir görüntü anlama zaman aşımına ihtiyaç duyabilir. Ayrıca Ollama kısıtlı donanımda duyurulan tam görü bağlamını ayırmaya çalıştığında çökebilir veya durabilirler. Bir yetenek zaman aşımı ayarlayın ve yalnızca normal bir görüntü açıklama dönüşüne ihtiyacınız olduğunda model girdisinde `num_ctx` değerini sınırlayın:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        models: [          {            id: "qwen2.5vl:7b",            name: "qwen2.5vl:7b",            input: ["text", "image"],            params: { num_ctx: 2048, keep_alive: "1m" },          },        ],      },    },  },  tools: {    media: {      image: {        timeoutSeconds: 180,        models: [{ provider: "ollama", model: "qwen2.5vl:7b", timeoutSeconds: 300 }],      },    },  },}
[/code]

Bu zaman aşımı, gelen görüntü anlamaya ve agent’ın bir dönüş sırasında çağırabileceği açık `image` aracına uygulanır. Sağlayıcı düzeyindeki `models.providers.ollama.timeoutSeconds`, normal model çağrıları için alttaki Ollama HTTP isteği korumasını kontrol etmeye devam eder.

Açık görüntü aracını yerel Ollama’ya karşı canlı doğrulamak için:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA_IMAGE=1 \  pnpm test:live -- src/agents/tools/image-tool.ollama.live.test.ts
[/code]

`models.providers.ollama.models` değerini elle tanımlarsanız görü modellerini görüntü girişi desteğiyle işaretleyin:

json5Copy code
[code]
    {  id: "qwen2.5vl:7b",  name: "qwen2.5vl:7b",  input: ["text", "image"],  contextWindow: 128000,  maxTokens: 8192,}
[/code]

OpenClaw, görüntü yetenekli olarak işaretlenmemiş modeller için görüntü açıklama isteklerini reddeder. Örtük keşifte OpenClaw, `/api/show` bir görü yeteneği bildirdiğinde bunu Ollama’dan okur.

## Yapılandırma

### Basic (implicit discovery)

En basit yalnızca yerel etkinleştirme yolu ortam değişkeni üzerinden yapılır:

bashCopy code
[code]
    export OLLAMA_API_KEY="ollama-local"
[/code]

### Explicit (manual models)

Barındırılan bulut kurulumu istediğinizde, Ollama başka bir host/port üzerinde çalıştığında, belirli bağlam pencerelerini veya model listelerini zorlamak istediğinizde ya da tamamen elle model tanımları istediğinizde açık yapılandırma kullanın.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192          }        ]      }    }  }}
[/code]

### Custom base URL

Ollama farklı bir host veya port üzerinde çalışıyorsa (açık yapılandırma otomatik keşfi devre dışı bırakır, bu yüzden modelleri elle tanımlayın):

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        apiKey: "ollama-local",        baseUrl: "http://ollama-host:11434", // No /v1 - use native Ollama API URL        api: "ollama", // Set explicitly to guarantee native tool-calling behavior        timeoutSeconds: 300, // Optional: give cold local models longer to connect and stream        models: [          {            id: "qwen3:32b",            name: "qwen3:32b",            params: {              keep_alive: "15m", // Optional: keep the model loaded between turns            },          },        ],      },    },  },}
[/code]

## Yaygın tarifler

Bunları başlangıç noktası olarak kullanın ve model kimliklerini `ollama list` veya `openclaw models list --provider ollama` çıktısındaki tam adlarla değiştirin.

Local model with auto-discovery

Ollama Gateway ile aynı makinede çalıştığında ve OpenClaw’ın kurulu modelleri otomatik olarak keşfetmesini istediğinizde bunu kullanın.

bashCopy code
[code]
    ollama serveollama pull gemma4export OLLAMA_API_KEY="ollama-local"openclaw models list --provider ollamaopenclaw models set ollama/gemma4
[/code]

Bu yol yapılandırmayı en az düzeyde tutar. Modelleri elle tanımlamak istemediğiniz sürece bir `models.providers.ollama` bloğu eklemeyin.

LAN Ollama host with manual models

LAN host’ları için yerel Ollama URL’leri kullanın. `/v1` eklemeyin.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            reasoning: true,            input: ["text"],            params: {              num_ctx: 32768,              thinking: false,              keep_alive: "15m",            },          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/qwen3.5:9b" },    },  },}
[/code]

`contextWindow`, OpenClaw tarafındaki bağlam bütçesidir. `params.num_ctx`, istek için Ollama’ya gönderilir. Donanımınız modelin duyurulan tam bağlamını çalıştıramadığında bunları uyumlu tutun.

Ollama Cloud only

Yerel daemon çalıştırmadığınızda ve barındırılan Ollama modellerini doğrudan istediğinizde bunu kullanın.

bashCopy code
[code]
    export OLLAMA_API_KEY="your-ollama-api-key"
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/kimi-k2.5:cloud" },    },  },}
[/code]

Cloud plus local through a signed-in daemon

Yerel veya LAN Ollama daemon’u `ollama signin` ile oturum açmışsa ve hem yerel modelleri hem de `:cloud` modellerini sunması gerekiyorsa bunu kullanın.

bashCopy code
[code]
    ollama signinollama pull gemma4
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        models: [          { id: "gemma4", name: "gemma4", input: ["text"] },          { id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text", "image"] },        ],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama/gemma4",        fallbacks: ["ollama/kimi-k2.5:cloud"],      },    },  },}
[/code]

Multiple Ollama hosts

Birden fazla Ollama sunucunuz olduğunda özel sağlayıcı kimlikleri kullanın. Her sağlayıcının kendi host’u, modelleri, kimlik doğrulaması, zaman aşımı ve model başvuruları olur.

json5Copy code
[code]
    {  models: {    providers: {      "ollama-fast": {        baseUrl: "http://mini.local:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [{ id: "gemma4", name: "gemma4", input: ["text"] }],      },      "ollama-large": {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 420,        contextWindow: 131072,        maxTokens: 16384,        models: [{ id: "qwen3.5:27b", name: "qwen3.5:27b", input: ["text"] }],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama-fast/gemma4",        fallbacks: ["ollama-large/qwen3.5:27b"],      },    },  },}
[/code]

OpenClaw isteği gönderdiğinde etkin sağlayıcı öneki kaldırılır; böylece `ollama-large/qwen3.5:27b`, Ollama’ya `qwen3.5:27b` olarak ulaşır.

Lean local model profile

Bazı yerel modeller basit prompt’ları yanıtlayabilir ancak tam agent araç yüzeyiyle zorlanabilir. Küresel çalışma zamanı ayarlarını değiştirmeden önce araçları ve bağlamı sınırlayarak başlayın.

json5Copy code
[code]
    {  agents: {    defaults: {      experimental: {        localModelLean: true,      },      model: { primary: "ollama/gemma4" },    },  },  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [          {            id: "gemma4",            name: "gemma4",            input: ["text"],            params: { num_ctx: 32768 },            compat: { supportsTools: false },          },        ],      },    },  },}
[/code]

`compat.supportsTools: false` yalnızca model veya sunucu araç şemalarında güvenilir biçimde başarısız olduğunda kullanın. Bu, kararlılık karşılığında ajan yeteneğinden ödün verir. `localModelLean`, tarayıcı, cron ve mesaj araçlarını ajan yüzeyinden kaldırır, ancak Ollama'nın çalışma zamanı bağlamını veya düşünme modunu değiştirmez. Döngüye giren ya da yanıt bütçesini gizli akıl yürütmeye harcayan küçük Qwen tarzı düşünme modelleri için bunu açık `params.num_ctx` ve `params.thinking: false` ile eşleştirin.

### Model seçimi

Yapılandırıldıktan sonra tüm Ollama modelleriniz kullanılabilir:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "ollama/gpt-oss:20b",        fallbacks: ["ollama/llama3.3", "ollama/qwen2.5-coder:32b"],      },    },  },}
[/code]

Özel Ollama sağlayıcı kimlikleri de desteklenir. Bir model başvurusu etkin sağlayıcı önekini kullandığında, örneğin `ollama-spark/qwen3:32b`, OpenClaw Ollama'yı çağırmadan önce yalnızca bu öneki kaldırır, böylece sunucu `qwen3:32b` alır.

Yavaş yerel modeller için, tüm ajan çalışma zamanı zaman aşımını yükseltmeden önce sağlayıcı kapsamlı istek ayarlamasını tercih edin:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

`timeoutSeconds`, bağlantı kurulumu, başlıklar, gövde akışı ve toplam korumalı getirme iptali dahil olmak üzere model HTTP isteğine uygulanır. `params.keep_alive`, yerel `/api/chat` isteklerinde üst düzey `keep_alive` olarak Ollama'ya iletilir; ilk tur yükleme süresi darboğaz olduğunda bunu model başına ayarlayın.

### Hızlı doğrulama

bashCopy code
[code]
    # Ollama daemon visible to this machinecurl http://127.0.0.1:11434/api/tags # OpenClaw catalog and selected modelopenclaw models list --provider ollamaopenclaw models status # Direct model smokeopenclaw infer model run \  --model ollama/gemma4 \  --prompt "Reply with exactly: ok"
[/code]

Uzak ana makineler için `127.0.0.1` değerini `baseUrl` içinde kullanılan ana makineyle değiştirin. `curl` çalışıyor ancak OpenClaw çalışmıyorsa Gateway'in farklı bir makinede, kapsayıcıda veya hizmet hesabında çalışıp çalışmadığını kontrol edin.

## Ollama Web Search

OpenClaw, paketlenmiş bir `web_search` sağlayıcısı olarak **Ollama Web Search** desteği sunar.

Özellik | Ayrıntı  
---|---  
Ana makine | Yapılandırılmış Ollama ana makinenizi kullanır (`models.providers.ollama.baseUrl` ayarlanmışsa o, aksi halde `http://127.0.0.1:11434`); `https://ollama.com` barındırılan API'yi doğrudan kullanır  
Kimlik doğrulama | Oturum açılmış yerel Ollama ana makineleri için anahtarsızdır; doğrudan `https://ollama.com` araması veya kimlik doğrulaması korumalı ana makineler için `OLLAMA_API_KEY` ya da yapılandırılmış sağlayıcı kimlik doğrulaması  
Gereksinim | Yerel/kendi barındırdığınız ana makineler çalışıyor ve `ollama signin` ile oturum açılmış olmalıdır; doğrudan barındırılan arama, `baseUrl: "https://ollama.com"` ve gerçek bir Ollama API anahtarı gerektirir  
  
`openclaw onboard` veya `openclaw configure --section web` sırasında **Ollama Web Search** seçin ya da şunu ayarlayın:

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Ollama Cloud üzerinden doğrudan barındırılan arama için:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [{ id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text"] }],      },    },  },  tools: {    web: {      search: { provider: "ollama" },    },  },}
[/code]

Oturum açılmış yerel daemon için OpenClaw, daemon'un `/api/experimental/web_search` proxy'sini kullanır. `https://ollama.com` için barındırılan `/api/web_search` uç noktasını doğrudan çağırır.

## Gelişmiş yapılandırma

Eski OpenAI uyumlu mod

Bunun yerine OpenAI uyumlu uç noktayı kullanmanız gerekiyorsa (örneğin yalnızca OpenAI biçimini destekleyen bir proxy arkasında), `api: "openai-completions"` değerini açıkça ayarlayın:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: true, // default: true        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Bu mod, akış ve araç çağırmayı aynı anda desteklemeyebilir. Model yapılandırmasında `params: { streaming: false }` ile akışı devre dışı bırakmanız gerekebilir.

Ollama ile `api: "openai-completions"` kullanıldığında OpenClaw varsayılan olarak `options.num_ctx` enjekte eder, böylece Ollama sessizce 4096 bağlam penceresine geri dönmez. Proxy'niz/yukarı akışınız bilinmeyen `options` alanlarını reddediyorsa bu davranışı devre dışı bırakın:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: false,        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Bağlam pencereleri

Otomatik keşfedilen modeller için OpenClaw, mevcut olduğunda özel Modelfile'lardan gelen daha büyük `PARAMETER num_ctx` değerleri dahil olmak üzere Ollama tarafından bildirilen bağlam penceresini kullanır. Aksi halde OpenClaw tarafından kullanılan varsayılan Ollama bağlam penceresine geri döner.

O Ollama sağlayıcısı altındaki her model için sağlayıcı düzeyinde `contextWindow`, `contextTokens` ve `maxTokens` varsayılanlarını ayarlayabilir, ardından gerektiğinde model başına bunları geçersiz kılabilirsiniz. `contextWindow`, OpenClaw'ın istem ve Compaction bütçesidir. Yerel Ollama istekleri, `params.num_ctx` değerini açıkça yapılandırmadığınız sürece `options.num_ctx` alanını ayarlamaz; böylece Ollama kendi modelini, `OLLAMA_CONTEXT_LENGTH` değerini veya VRAM tabanlı varsayılanını uygulayabilir. Bir Modelfile'ı yeniden oluşturmadan Ollama'nın istek başına çalışma zamanı bağlamını sınırlamak veya zorlamak için `params.num_ctx` ayarlayın; geçersiz, sıfır, negatif ve sonlu olmayan değerler yok sayılır. OpenAI uyumlu Ollama bağdaştırıcısı, varsayılan olarak yapılandırılmış `params.num_ctx` veya `contextWindow` değerinden `options.num_ctx` enjekte etmeye devam eder; yukarı akışınız `options` değerini reddediyorsa bunu `injectNumCtxForOpenAICompat: false` ile devre dışı bırakın.

Yerel Ollama model girdileri ayrıca `params` altında `temperature`, `top_p`, `top_k`, `min_p`, `num_predict`, `stop`, `repeat_penalty`, `num_batch`, `num_thread` ve `use_mmap` dahil ortak Ollama çalışma zamanı seçeneklerini kabul eder. OpenClaw yalnızca Ollama istek anahtarlarını iletir, bu nedenle `streaming` gibi OpenClaw çalışma zamanı parametreleri Ollama'ya sızdırılmaz. Üst düzey Ollama `think` göndermek için `params.think` veya `params.thinking` kullanın; `false`, Qwen tarzı düşünme modelleri için API düzeyinde düşünmeyi devre dışı bırakır.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        models: [          {            id: "llama3.3",            contextWindow: 131072,            maxTokens: 65536,            params: {              num_ctx: 32768,              temperature: 0.7,              top_p: 0.9,              thinking: false,            },          }        ]      }    }  }}
[/code]

Model başına `agents.defaults.models["ollama/<model>"].params.num_ctx` da çalışır. İkisi de yapılandırılmışsa, açık sağlayıcı model girdisi ajan varsayılanına göre önceliklidir.

Düşünme denetimi

Yerel Ollama modelleri için OpenClaw düşünme denetimini Ollama'nın beklediği şekilde iletir: `options.think` değil, üst düzey `think`. `/api/show` yanıtı `thinking` yeteneğini içeren otomatik keşfedilen modeller `/think low`, `/think medium`, `/think high` ve `/think max` sunar; düşünmeyen modeller yalnızca `/think off` sunar.

bashCopy code
[code]
    openclaw agent --model ollama/gemma4 --thinking offopenclaw agent --model ollama/gemma4 --thinking low
[/code]

Ayrıca bir model varsayılanı da ayarlayabilirsiniz:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "ollama/gemma4": {          thinking: "low",        },      },    },  },}
[/code]

Model başına `params.think` veya `params.thinking`, belirli bir yapılandırılmış model için Ollama API düşünmesini devre dışı bırakabilir ya da zorlayabilir. Etkin çalıştırmada yalnızca örtük varsayılan `off` olduğunda OpenClaw bu açık model parametrelerini korur; `/think medium` gibi off dışı çalışma zamanı komutları yine de etkin çalıştırmayı geçersiz kılar.

Akıl yürütme modelleri

OpenClaw, `deepseek-r1`, `reasoning` veya `think` gibi adlara sahip modelleri varsayılan olarak akıl yürütme yetenekli kabul eder.

bashCopy code
[code]
    ollama pull deepseek-r1:32b
[/code]

Ek yapılandırma gerekmez. OpenClaw bunları otomatik olarak işaretler.

Model maliyetleri

Ollama ücretsizdir ve yerel olarak çalışır, bu nedenle tüm model maliyetleri $0 olarak ayarlanır. Bu, hem otomatik keşfedilen hem de elle tanımlanan modellere uygulanır.

Bellek gömmeleri

Paketlenmiş Ollama Plugin'i, [bellek araması](</tr/concepts/memory>) için bir bellek gömme sağlayıcısı kaydeder. Yapılandırılmış Ollama temel URL'sini ve API anahtarını kullanır, Ollama'nın mevcut `/api/embed` uç noktasını çağırır ve mümkün olduğunda birden fazla bellek parçasını tek bir `input` isteğinde toplu işler.

Özellik | Değer  
---|---  
Varsayılan model | `nomic-embed-text`  
Otomatik çekme | Evet — gömme modeli yerelde yoksa otomatik olarak çekilir  
  
Sorgu zamanı gömmeleri, `nomic-embed-text`, `qwen3-embedding` ve `mxbai-embed-large` dahil bunları gerektiren veya öneren modeller için alma öneklerini kullanır. Mevcut dizinlerin biçim geçişine ihtiyaç duymaması için bellek belge toplu işlemleri ham kalır.

Bellek araması gömme sağlayıcısı olarak Ollama'yı seçmek için:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        remote: {          // Default for Ollama. Raise on larger hosts if reindexing is too slow.          nonBatchConcurrency: 1,        },      },    },  },}
[/code]

Uzak gömme ana makinesi için kimlik doğrulamayı o ana makineyle sınırlı tutun:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        model: "nomic-embed-text",        remote: {          baseUrl: "http://gpu-box.local:11434",          apiKey: "ollama-local",          nonBatchConcurrency: 2,        },      },    },  },}
[/code]

Akış yapılandırması

OpenClaw'ın Ollama entegrasyonu varsayılan olarak **yerel Ollama API** (`/api/chat`) kullanır; bu API akışı ve araç çağırmayı aynı anda tam olarak destekler. Özel yapılandırma gerekmez.

Yerel `/api/chat` istekleri için OpenClaw düşünme denetimini de doğrudan Ollama'ya iletir: `/think off` ve `openclaw agent --thinking off`, açık bir model `params.think`/`params.thinking` değeri yapılandırılmadığı sürece üst düzey `think: false` gönderir; `/think low|medium|high` ise eşleşen üst düzey `think` çaba dizesini gönderir. `/think max`, Ollama'nın en yüksek yerel çabasına, yani `think: "high"` değerine eşlenir.

## Sorun Giderme

WSL2 çökme döngüsü (tekrarlanan yeniden başlatmalar)

NVIDIA/CUDA kullanılan WSL2'de, resmi Ollama Linux yükleyicisi `Restart=always` içeren bir `ollama.service` systemd birimi oluşturur. Bu hizmet otomatik başlar ve WSL2 önyüklemesi sırasında GPU destekli bir model yüklerse, Ollama model yüklenirken ana makine belleğini sabitleyebilir. Hyper-V bellek geri kazanımı bu sabitlenmiş sayfaları her zaman geri alamaz; bu nedenle Windows WSL2 VM'ini sonlandırabilir, systemd Ollama'yı yeniden başlatır ve döngü tekrarlanır.

Yaygın kanıtlar:

  * Windows tarafından tekrarlanan WSL2 yeniden başlatmaları veya sonlandırmaları
  * WSL2 başlangıcından kısa süre sonra `app.slice` veya `ollama.service` içinde yüksek CPU kullanımı
  * Linux OOM-killer olayı yerine systemd kaynaklı SIGTERM


OpenClaw, WSL2'yi, `Restart=always` ile etkinleştirilmiş `ollama.service` birimini ve görünür CUDA işaretçilerini algıladığında başlangıçta bir uyarı günlüğe yazar.

Azaltma:

bashCopy code
[code]
    sudo systemctl disable ollama
[/code]

Bunu Windows tarafında `%USERPROFILE%\.wslconfig` dosyasına ekleyin, ardından `wsl --shutdown` çalıştırın:

iniCopy code
[code]
    [experimental]autoMemoryReclaim=disabled
[/code]

Ollama hizmet ortamında daha kısa bir canlı tutma süresi ayarlayın veya Ollama'yı yalnızca ihtiyaç duyduğunuzda elle başlatın:

bashCopy code
[code]
    export OLLAMA_KEEP_ALIVE=5mollama serve
[/code]

Bkz. [ollama/ollama#11317](<https://github.com/ollama/ollama/issues/11317>).

Ollama algılanmadı

Ollama'nın çalıştığından, `OLLAMA_API_KEY` değerini (veya bir kimlik doğrulama profili) ayarladığınızdan ve açık bir `models.providers.ollama` girdisi tanımlamadığınızdan emin olun:

bashCopy code
[code]
    ollama serve
[/code]

API'nin erişilebilir olduğunu doğrulayın:

bashCopy code
[code]
    curl http://localhost:11434/api/tags
[/code]

Kullanılabilir model yok

Modeliniz listelenmiyorsa modeli yerel olarak çekin veya `models.providers.ollama` içinde açıkça tanımlayın.

bashCopy code
[code]
    ollama list  # Nelerin kurulu olduğunu görünollama pull gemma4ollama pull gpt-oss:20bollama pull llama3.3     # Veya başka bir model
[/code]

Bağlantı reddedildi

Ollama'nın doğru bağlantı noktasında çalıştığını kontrol edin:

bashCopy code
[code]
    # Ollama'nın çalışıp çalışmadığını kontrol edinps aux | grep ollama # Veya Ollama'yı yeniden başlatınollama serve
[/code]

Uzak ana makine curl ile çalışıyor ama OpenClaw ile çalışmıyor

Gateway'i çalıştıran aynı makineden ve çalışma zamanından doğrulayın:

bashCopy code
[code]
    openclaw gateway status --deepcurl http://ollama-host:11434/api/tags
[/code]

Yaygın nedenler:

  * `baseUrl`, `localhost` değerini gösterir, ancak Gateway Docker içinde veya başka bir ana makinede çalışır.
  * URL `/v1` kullanır; bu da yerel Ollama yerine OpenAI uyumlu davranışı seçer.
  * Uzak ana makinede Ollama tarafında güvenlik duvarı veya LAN bağlama değişiklikleri gerekir.
  * Model dizüstü bilgisayarınızdaki daemon'da vardır ancak uzak daemon'da yoktur.

Model araç JSON'unu metin olarak çıkarıyor

Bu genellikle sağlayıcının OpenAI uyumlu modu kullandığı veya modelin araç şemalarını işleyemediği anlamına gelir.

Yerel Ollama modunu tercih edin:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",        api: "ollama",      },    },  },}
[/code]

Küçük bir yerel model araç şemalarında hâlâ başarısız oluyorsa, o model girdisinde `compat.supportsTools: false` ayarlayın ve yeniden test edin.

Kimi veya GLM bozuk semboller döndürüyor

Uzun, dilsel olmayan sembol dizilerinden oluşan barındırılan Kimi/GLM yanıtları, başarılı bir asistan yanıtı yerine başarısız sağlayıcı çıktısı olarak değerlendirilir. Bu, bozuk metni oturuma kalıcı olarak yazmadan normal yeniden deneme, fallback veya hata işlemeyi devreye sokar.

Bu durum tekrar tekrar olursa ham model adını, geçerli oturum dosyasını ve çalıştırmanın `Cloud + Local` mı yoksa `Cloud only` mi kullandığını yakalayın; ardından yeni bir oturum ve bir fallback model deneyin:

bashCopy code
[code]
    openclaw infer model run --model ollama/kimi-k2.5:cloud --prompt "Reply with exactly: ok" --jsonopenclaw models set ollama/gemma4
[/code]

Soğuk yerel model zaman aşımına uğruyor

Büyük yerel modeller, akış başlamadan önce uzun bir ilk yükleme süresine ihtiyaç duyabilir. Zaman aşımını Ollama sağlayıcısıyla sınırlı tutun ve isteğe bağlı olarak Ollama'dan modeli dönüşler arasında yüklü tutmasını isteyin:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

Ana makinenin kendisi bağlantıları kabul etmekte yavaşsa, `timeoutSeconds` bu sağlayıcı için korumalı Undici bağlantı zaman aşımını da uzatır.

Büyük bağlamlı model çok yavaş veya belleği tükeniyor

Birçok Ollama modeli, donanımınızın rahatça çalıştırabileceğinden daha büyük bağlamlar duyurur. Yerel Ollama, `params.num_ctx` ayarlamadığınız sürece Ollama'nın kendi çalışma zamanı bağlamı varsayılanını kullanır. Öngörülebilir ilk belirteç gecikmesi istediğinizde hem OpenClaw'ın bütçesini hem de Ollama'nın istek bağlamını sınırlayın:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            params: { num_ctx: 32768, thinking: false },          },        ],      },    },  },}
[/code]

OpenClaw çok fazla istem gönderiyorsa önce `contextWindow` değerini düşürün. Ollama makine için çok büyük bir çalışma zamanı bağlamı yüklüyorsa `params.num_ctx` değerini düşürün. Üretim çok uzun sürüyorsa `maxTokens` değerini düşürün.

## İlgili

[**Model sağlayıcıları** Tüm sağlayıcılara, model referanslarına ve yük devretme davranışına genel bakış. ](</tr/concepts/model-providers>) [**Model seçimi** Modellerin nasıl seçileceği ve yapılandırılacağı. ](</tr/concepts/models>) [**Ollama Web Arama** Ollama destekli web araması için tam kurulum ve davranış ayrıntıları. ](</tr/tools/ollama-search>) [**Yapılandırma** Tam yapılandırma başvurusu. ](</tr/gateway/configuration>)

Was this useful?YesNo