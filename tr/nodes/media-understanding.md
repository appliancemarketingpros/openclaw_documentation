---
title: Medya anlama
source_url: https://docs.openclaw.ai/tr/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw, yanıt işlem hattı çalışmadan önce **gelen medyayı özetleyebilir** (görsel/ses/video). Yerel araçlar veya sağlayıcı anahtarları kullanılabilir olduğunda otomatik algılar ve devre dışı bırakılabilir ya da özelleştirilebilir. Anlama kapalıysa modeller yine özgün dosyaları/URL'leri her zamanki gibi alır.

Tedarikçiye özgü medya davranışı tedarikçi Plugin'leri tarafından kaydedilirken, OpenClaw çekirdeği paylaşılan `tools.media` yapılandırmasına, geri dönüş sırasına ve yanıt işlem hattı entegrasyonuna sahip olur.

## Hedefler

  * İsteğe bağlı: gelen medyayı daha hızlı yönlendirme + daha iyi komut ayrıştırma için kısa metne önceden sindirme.
  * Özgün medya teslimini modele koruma (her zaman).
  * **Sağlayıcı API'lerini** ve **CLI geri dönüşlerini** destekleme.
  * Sıralı geri dönüşlü birden çok modele izin verme (hata/boyut/zaman aşımı).


## Üst düzey davranış

* ### Ekleri topla

Gelen ekleri topla (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Yetenek başına seç

Etkinleştirilmiş her yetenek (görsel/ses/video) için ekleri ilkeye göre seç (varsayılan: **ilk**).

* ### Model seç

İlk uygun model girdisini seç (boyut + yetenek + kimlik doğrulama).

* ### Başarısızlıkta geri dön

Bir model başarısız olursa veya medya çok büyükse **sonraki girdiye geri dön**.

* ### Başarı bloğunu uygula

Başarı durumunda:

  * `Body`, `[Image]`, `[Audio]` veya `[Video]` bloğu olur.
  * Ses `{{Transcript}}` değerini ayarlar; komut ayrıştırma varsa açıklama metnini, yoksa dökümü kullanır.
  * Açıklamalar blok içinde `User text:` olarak korunur.


Anlama başarısız olursa veya devre dışıysa **yanıt akışı devam eder** ; özgün gövde + eklerle.

## Yapılandırma özeti

`tools.media`, **paylaşılan modelleri** ve yetenek başına geçersiz kılmaları destekler:

Üst düzey anahtarlar

  * `tools.media.models`: paylaşılan model listesi (kapılama için `capabilities` kullanın).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * varsayılanlar (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * sağlayıcı geçersiz kılmaları (`baseUrl`, `headers`, `providerOptions`)
    * `tools.media.audio.providerOptions.deepgram` üzerinden Deepgram ses seçenekleri
    * ses dökümü yankı denetimleri (`echoTranscript`, varsayılan `false`; `echoFormat`)
    * isteğe bağlı **yetenek başına`models` listesi** (paylaşılan modellerden önce tercih edilir)
    * `attachments` ilkesi (`mode`, `maxAttachments`, `prefer`)
    * `scope` (kanal/chatType/oturum anahtarına göre isteğe bağlı kapılama)
  * `tools.media.concurrency`: eşzamanlı en fazla yetenek çalıştırma sayısı (varsayılan **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Model girdileri

Her `models[]` girdisi **sağlayıcı** veya **CLI** olabilir:

### Sağlayıcı girdisi

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### CLI girdisi

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

CLI şablonları şunları da kullanabilir:

  * `{{MediaDir}}` (medya dosyasını içeren dizin)
  * `{{OutputDir}}` (bu çalıştırma için oluşturulan geçici dizin)
  * `{{OutputBase}}` (geçici dosya temel yolu, uzantı yok)


## Varsayılanlar ve sınırlar

Önerilen varsayılanlar:

  * `maxChars`: görsel/video için **500** (kısa, komut dostu)
  * `maxChars`: ses için **ayarlanmamış** (siz bir sınır belirlemezseniz tam döküm)
  * `maxBytes`: 
    * görsel: **10MB**
    * ses: **20MB**
    * video: **50MB**


Kurallar

  * Medya `maxBytes` değerini aşarsa o model atlanır ve **sonraki model denenir**.
  * **1024 bayttan** küçük ses dosyaları boş/bozuk kabul edilir ve sağlayıcı/CLI dökümünden önce atlanır; gelen yanıt bağlamı, ajanın notun çok küçük olduğunu bilmesi için deterministik bir yer tutucu döküm alır.
  * Model `maxChars` değerinden fazlasını döndürürse çıktı kırpılır.
  * `prompt` varsayılanı, basit "Describe the {media}." ifadesi ve `maxChars` kılavuzudur (yalnızca görsel/video).
  * Etkin birincil görsel modeli zaten yerel olarak görmeyi destekliyorsa OpenClaw `[Image]` özet bloğunu atlar ve bunun yerine özgün görseli modele geçirir.
  * Gateway/WebChat birincil modeli yalnızca metinse görsel ekleri, eki kaybetmek yerine görsel/PDF araçları veya yapılandırılmış görsel modelin bunları hâlâ inceleyebilmesi için dışa aktarılmış `media://inbound/*` referansları olarak korunur.
  * Açık `openclaw infer image describe --model <provider/model>` istekleri farklıdır: `ollama/qwen2.5vl:7b` gibi Ollama referansları dahil olmak üzere o görsel yetenekli sağlayıcı/modeli doğrudan çalıştırırlar.
  * `<capability>.enabled: true` ise ancak hiçbir model yapılandırılmamışsa OpenClaw, sağlayıcısı yeteneği desteklediğinde **etkin yanıt modelini** dener.


### Medya anlamayı otomatik algılama (varsayılan)

`tools.media.<capability>.enabled` **`false` olarak ayarlanmamışsa** ve model yapılandırmadıysanız OpenClaw bu sırayla otomatik algılar ve **ilk çalışan seçenekte durur** :

* ### Etkin yanıt modeli

Sağlayıcısı yeteneği desteklediğinde etkin yanıt modeli.

* ### agents.defaults.imageModel

`agents.defaults.imageModel` birincil/geri dönüş referansları (yalnızca görsel). `provider/model` referanslarını tercih edin. Çıplak referanslar, yalnızca eşleşme benzersiz olduğunda yapılandırılmış görsel yetenekli sağlayıcı model girdilerinden nitelendirilir.

* ### Yerel CLI'lar (yalnızca ses)

Yerel CLI'lar (kuruluysa):

  * `sherpa-onnx-offline` (encoder/decoder/joiner/tokens içeren `SHERPA_ONNX_MODEL_DIR` gerektirir)
  * `whisper-cli` (`whisper-cpp`; `WHISPER_CPP_MODEL` veya paketlenmiş tiny modeli kullanır)
  * `whisper` (Python CLI; modelleri otomatik indirir)


* ### Gemini CLI

`read_many_files` kullanan `gemini`.

* ### Sağlayıcı kimlik doğrulaması

  * Yeteneği destekleyen yapılandırılmış `models.providers.*` girdileri, paketlenmiş geri dönüş sırasından önce denenir.
  * Görsel yetenekli bir modele sahip yalnızca görsel yapılandırma sağlayıcıları, paketlenmiş bir tedarikçi Plugin'i olmadıklarında bile medya anlama için otomatik kaydolur.
  * Ollama görsel anlama, örneğin `agents.defaults.imageModel` veya `openclaw infer image describe --model ollama/<vision-model>` üzerinden açıkça seçildiğinde kullanılabilir.


Paketlenmiş geri dönüş sırası:

  * Ses: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Görsel: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Video: Google → Qwen → Moonshot


Otomatik algılamayı devre dışı bırakmak için şunu ayarlayın:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Proxy ortam desteği (sağlayıcı modelleri)

Sağlayıcı tabanlı **ses** ve **video** medya anlama etkinleştirildiğinde OpenClaw, sağlayıcı HTTP çağrıları için standart giden proxy ortam değişkenlerini dikkate alır:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Proxy ortam değişkenleri ayarlanmamışsa medya anlama doğrudan çıkış kullanır. Proxy değeri hatalı biçimlendirilmişse OpenClaw bir uyarı kaydeder ve doğrudan getirmeye geri döner.

## Yetenekler (isteğe bağlı)

`capabilities` ayarlarsanız girdi yalnızca bu medya türleri için çalışır. Paylaşılan listeler için OpenClaw varsayılanları çıkarabilir:

  * `openai`, `anthropic`, `minimax`: **görsel**
  * `minimax-portal`: **görsel**
  * `moonshot`: **görsel + video**
  * `openrouter`: **görsel + ses**
  * `google` (Gemini API): **görsel + ses + video**
  * `qwen`: **görsel + video**
  * `mistral`: **ses**
  * `zai`: **görsel**
  * `groq`: **ses**
  * `xai`: **ses**
  * `deepgram`: **ses**
  * Görsel yetenekli bir modele sahip herhangi bir `models.providers.<id>.models[]` kataloğu: **görsel**


CLI girdileri için şaşırtıcı eşleşmelerden kaçınmak üzere **`capabilities` değerini açıkça ayarlayın**. `capabilities` atlarsanız girdi, içinde göründüğü liste için uygundur.

## Sağlayıcı destek matrisi (OpenClaw entegrasyonları)

Yetenek | Sağlayıcı entegrasyonu | Notlar  
---|---|---  
Görsel | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), yapılandırma sağlayıcıları | Tedarikçi Plugin'leri görsel desteği kaydeder; `openai-codex/*` OAuth sağlayıcı tesisatını kullanır; `codex/*` sınırlı bir Codex app-server turu kullanır; MiniMax ve MiniMax OAuth ikisi de `MiniMax-VL-01` kullanır; görsel yetenekli yapılandırma sağlayıcıları otomatik kaydolur.  
Ses | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Sağlayıcı dökümü (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Video | Google, Qwen, Moonshot | Tedarikçi Plugin'leri üzerinden sağlayıcı video anlama; Qwen video anlama Standard DashScope uç noktalarını kullanır.  
  
## Model seçimi kılavuzu

  * Kalite ve güvenlik önemli olduğunda her medya yeteneği için kullanılabilir en güçlü en yeni nesil modeli tercih edin.
  * Güvenilmeyen girdileri işleyen araç etkin ajanlar için eski/daha zayıf medya modellerinden kaçının.
  * Kullanılabilirlik için yetenek başına en az bir geri dönüş tutun (kalite modeli + daha hızlı/daha ucuz model).
  * CLI geri dönüşleri (`whisper-cli`, `whisper`, `gemini`), sağlayıcı API'leri kullanılamadığında yararlıdır.
  * `parakeet-mlx` notu: `--output-dir` ile, çıktı biçimi `txt` olduğunda (veya belirtilmediğinde) OpenClaw `<output-dir>/<media-basename>.txt` okur; `txt` olmayan biçimler stdout'a geri döner.


## Ek ilkesi

Yetenek başına `attachments`, hangi eklerin işleneceğini denetler:

İlk seçilen eki mi yoksa tümünü mü işleyeceğini belirler.

İşlenen sayıyı sınırlar.

Aday ekler arasındaki seçim tercihi.

`mode: "all"` olduğunda çıktılar `[Image 1/2]`, `[Audio 2/2]` vb. olarak etiketlenir.

Dosya eki çıkarma davranışı

  * Çıkarılan dosya metni, medya istemine eklenmeden önce **güvenilmeyen harici içerik** olarak sarmalanır.
  * Enjekte edilen blok `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` gibi açık sınır işaretleyicileri kullanır ve bir `Source: External` meta veri satırı içerir.
  * Bu ek çıkarma yolu, medya istemini şişirmemek için uzun `SECURITY NOTICE:` başlığını bilinçli olarak atlar; sınır işaretleyicileri ve meta veriler yine de kalır.
  * Bir dosyada çıkarılabilir metin yoksa OpenClaw `[No extractable text]` enjekte eder.
  * Bir PDF bu yolda işlenmiş sayfa görüntülerine geri dönerse medya istemi `[PDF content rendered to images; images not forwarded to model]` yer tutucusunu korur, çünkü bu ek çıkarma adımı işlenmiş PDF görüntülerini değil metin bloklarını iletir.


## Yapılandırma örnekleri

### Paylaşılan modeller + geçersiz kılmalar

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Yalnızca ses + video

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Yalnızca görüntü

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Çok modlu tek giriş

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Durum çıktısı

Medya anlama çalıştığında `/status` kısa bir özet satırı içerir:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Bu, uygun olduğunda yetenek başına sonuçları ve seçilen sağlayıcıyı/modeli gösterir.

## Notlar

  * Anlama **en iyi çaba** ilkesine göre çalışır. Hatalar yanıtları engellemez.
  * Anlama devre dışı olsa bile ekler modellere aktarılmaya devam eder.
  * Anlamanın nerede çalışacağını sınırlamak için `scope` kullanın (ör. yalnızca DM'ler).


## İlgili

  * [Yapılandırma](</tr/gateway/configuration>)
  * [Görüntü ve medya desteği](</tr/nodes/images>)


Was this useful?YesNo