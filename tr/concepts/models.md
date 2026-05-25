---
title: Modeller CLI
source_url: https://docs.openclaw.ai/tr/concepts/models
scraped_at: 2026-05-25
---

[**Model yük devretme** Auth profili rotasyonu, bekleme süreleri ve bunun geri dönüşlerle nasıl etkileştiği. ](</tr/concepts/model-failover>) [**Model sağlayıcıları** Hızlı sağlayıcı özeti ve örnekler. ](</tr/concepts/model-providers>) [**Ajan çalışma zamanları** PI, Codex ve diğer ajan döngüsü çalışma zamanları. ](</tr/concepts/agent-runtimes>) [**Yapılandırma referansı** Model yapılandırma anahtarları. ](</tr/gateway/config-agents#agent-defaults>)

Model referansları bir sağlayıcı ve model seçer. Genellikle düşük seviyeli ajan çalışma zamanını seçmezler. OpenAI ajan referansları ana istisnadır: `openai/gpt-5.5`, resmi OpenAI sağlayıcısında varsayılan olarak Codex app-server çalışma zamanı üzerinden çalışır. Açık çalışma zamanı geçersiz kılmaları, tüm ajan veya oturum üzerinde değil, sağlayıcı/model politikasında yer alır. Codex çalışma zamanı modunda `openai/gpt-*` referansı API anahtarıyla faturalandırmayı ima etmez; kimlik doğrulama bir Codex hesabından veya `openai-codex` auth profilinden gelebilir. Bkz. [Ajan çalışma zamanları](</tr/concepts/agent-runtimes>).

## Model seçimi nasıl çalışır?

OpenClaw modelleri şu sırayla seçer:

* ### Birincil model

`agents.defaults.model.primary` (veya `agents.defaults.model`).

* ### Geri dönüşler

`agents.defaults.model.fallbacks` (sırayla).

* ### Sağlayıcı auth yük devretmesi

Auth yük devretmesi, bir sonraki modele geçmeden önce sağlayıcının içinde gerçekleşir.

İlgili model yüzeyleri

  * `agents.defaults.models`, OpenClaw tarafından kullanılabilen modellerin izin listesi/kataloğudur (aliaslar dahil). Sağlayıcı keşfini dinamik tutarken görünür sağlayıcıları sınırlamak için `provider/*` girdilerini kullanın.
  * `agents.defaults.imageModel` **yalnızca** birincil model görüntüleri kabul edemediğinde kullanılır.
  * `agents.defaults.pdfModel`, `pdf` aracı tarafından kullanılır. Atlanırsa araç `agents.defaults.imageModel` değerine, ardından çözümlenmiş oturum/varsayılan modele geri döner.
  * `agents.defaults.imageGenerationModel`, paylaşılan görüntü üretimi yeteneği tarafından kullanılır. Atlanırsa `image_generate` yine de auth destekli bir sağlayıcı varsayılanı çıkarabilir. Önce geçerli varsayılan sağlayıcıyı, ardından kalan kayıtlı görüntü üretimi sağlayıcılarını sağlayıcı kimliği sırasıyla dener. Belirli bir sağlayıcı/model ayarlarsanız o sağlayıcının auth/API anahtarını da yapılandırın.
  * `agents.defaults.musicGenerationModel`, paylaşılan müzik üretimi yeteneği tarafından kullanılır. Atlanırsa `music_generate` yine de auth destekli bir sağlayıcı varsayılanı çıkarabilir. Önce geçerli varsayılan sağlayıcıyı, ardından kalan kayıtlı müzik üretimi sağlayıcılarını sağlayıcı kimliği sırasıyla dener. Belirli bir sağlayıcı/model ayarlarsanız o sağlayıcının auth/API anahtarını da yapılandırın.
  * `agents.defaults.videoGenerationModel`, paylaşılan video üretimi yeteneği tarafından kullanılır. Atlanırsa `video_generate` yine de auth destekli bir sağlayıcı varsayılanı çıkarabilir. Önce geçerli varsayılan sağlayıcıyı, ardından kalan kayıtlı video üretimi sağlayıcılarını sağlayıcı kimliği sırasıyla dener. Belirli bir sağlayıcı/model ayarlarsanız o sağlayıcının auth/API anahtarını da yapılandırın.
  * Ajan başına varsayılanlar, bağlamalarla birlikte `agents.list[].model` üzerinden `agents.defaults.model` değerini geçersiz kılabilir (bkz. [Çok ajanlı yönlendirme](</tr/concepts/multi-agent>)).


## Seçim kaynağı ve geri dönüş davranışı

Aynı `provider/model`, nereden geldiğine bağlı olarak farklı şeyler ifade edebilir:

  * Yapılandırılmış varsayılanlar (`agents.defaults.model.primary` ve ajana özgü birinciller) normal başlangıç noktasıdır ve `agents.defaults.model.fallbacks` kullanır.
  * Otomatik geri dönüş seçimleri geçici kurtarma durumudur. Daha sonraki turların önce bilinen bozuk birincili yoklamadan geri dönüş zincirini kullanmaya devam edebilmesi için `modelOverrideSource: "auto"` ile depolanırlar.
  * Kullanıcı oturumu seçimleri kesindir. `/model`, model seçici, `session_status(model=...)` ve `sessions.patch`, `modelOverrideSource: "user"` depolar; seçilen sağlayıcı/model erişilemez durumdaysa OpenClaw başka bir yapılandırılmış modele geçmek yerine görünür biçimde başarısız olur.
  * Cron `--model` / payload `model`, iş başına bir birincildir. İş açık payload `fallbacks` sağlamadığı sürece yine de yapılandırılmış geri dönüşleri kullanır (katı bir cron çalıştırması için `fallbacks: []` kullanın).
  * CLI varsayılan model ve izin listesi seçicileri, tam yerleşik kataloğu yüklemek yerine açık `models.providers.*.models` listeleyerek `models.mode: "replace"` değerine uyar.
  * Control UI model seçici, Gateway’den yapılandırılmış model görünümünü ister: varsa sağlayıcı genelindeki `provider/*` girdileri dahil `agents.defaults.models`; aksi halde açık `models.providers.*.models` ve kullanılabilir auth bulunan sağlayıcılar. Tam yerleşik katalog, `view: "all"` ile `models.list` veya `openclaw models list --all` gibi açık göz atma görünümleri için ayrılmıştır.


## Hızlı model politikası

  * Birincilinizi, kullanabileceğiniz en güçlü en yeni nesil modele ayarlayın.
  * Maliyet/gecikme duyarlı görevler ve daha düşük riskli sohbet için geri dönüşleri kullanın.
  * Araç etkin ajanlar veya güvenilmeyen girdiler için eski/zayıf model katmanlarından kaçının.


## İlk kurulum (önerilen)

Yapılandırmayı elle düzenlemek istemiyorsanız ilk kurulumu çalıştırın:

bashCopy code
[code]
    openclaw onboard
[/code]

**OpenAI Code (Codex) aboneliği** (OAuth) ve **Anthropic** (API anahtarı veya Claude CLI) dahil yaygın sağlayıcılar için model + auth ayarlayabilir.

## Yapılandırma anahtarları (genel bakış)

  * `agents.defaults.model.primary` ve `agents.defaults.model.fallbacks`
  * `agents.defaults.imageModel.primary` ve `agents.defaults.imageModel.fallbacks`
  * `agents.defaults.pdfModel.primary` ve `agents.defaults.pdfModel.fallbacks`
  * `agents.defaults.imageGenerationModel.primary` ve `agents.defaults.imageGenerationModel.fallbacks`
  * `agents.defaults.videoGenerationModel.primary` ve `agents.defaults.videoGenerationModel.fallbacks`
  * `agents.defaults.models` (izin listesi + aliaslar + sağlayıcı parametreleri + `provider/*` dinamik sağlayıcı girdileri)
  * `models.providers` (`models.json` içine yazılan özel sağlayıcılar)


### Güvenli izin listesi düzenlemeleri

`agents.defaults.models` değerini elle güncellerken eklemeli yazmaları kullanın:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --merge
[/code]

Üzerine yazma koruması kuralları

`openclaw config set`, model/sağlayıcı haritalarını yanlışlıkla üzerine yazmalardan korur. `agents.defaults.models`, `models.providers` veya `models.providers.<id>.models` için düz bir nesne ataması, mevcut girdileri kaldıracaksa reddedilir. Eklemeli değişiklikler için `--merge` kullanın; `--replace` yalnızca sağlanan değer eksiksiz hedef değer olmalıysa kullanın.

Etkileşimli sağlayıcı kurulumu ve `openclaw configure --section model` de sağlayıcı kapsamlı seçimleri mevcut izin listesiyle birleştirir; böylece Codex, Ollama veya başka bir sağlayıcı eklemek ilgisiz model girdilerini düşürmez. Yapılandırma, sağlayıcı auth yeniden uygulandığında mevcut `agents.defaults.model.primary` değerini korur. `openclaw models auth login --provider <id> --set-default` ve `openclaw models set <model>` gibi açık varsayılan ayarlama komutları yine de `agents.defaults.model.primary` değerini değiştirir.

## "Modele izin verilmiyor" (ve yanıtların neden durduğu)

`agents.defaults.models` ayarlanmışsa `/model` ve oturum geçersiz kılmaları için **izin listesi** haline gelir. Bir kullanıcı bu izin listesinde olmayan bir model seçtiğinde OpenClaw şunu döndürür:

CodeCopy code
[code]
    Model "provider/model" is not allowed. Use /models to list providers, or /models <provider> to list models.Add it with: openclaw config set agents.defaults.models '{"provider/model":{}}' --strict-json --merge
[/code]

Reddedilen komut `/model openai/gpt-5.5 --runtime codex` gibi bir çalışma zamanı geçersiz kılması içeriyorsa önce izin listesini düzeltin, ardından aynı `/model ... --runtime ...` komutunu yeniden deneyin. Yerel Codex yürütmesi için seçilen model hâlâ `openai/gpt-5.5` olur; `codex` çalışma zamanı harness’ı seçer ve Codex auth değerini ayrı kullanır.

Yerel/GGUF modeller için tam sağlayıcı ön ekli referansı izin listesinde saklayın; örneğin `ollama/gemma4:26b`, `lmstudio/Gemma4-26b-a4-it-gguf` veya `openclaw models list --provider <provider>` tarafından gösterilen tam sağlayıcı/model. İzin listesi aktifken yalın yerel dosya adları veya görünen adlar yeterli değildir.

Her modeli elle listelemeden sağlayıcıları sınırlamak istiyorsanız `agents.defaults.models` içine `provider/*` girdileri ekleyin:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai-codex/*": {},        "vllm/*": {},      },    },  },}
[/code]

Bu politikayla `/model`, `/models` ve model seçiciler yalnızca bu sağlayıcılar için keşfedilen kataloğu gösterir. Seçilen sağlayıcılardan gelen yeni modeller, izin listesini düzenlemeden görünebilir. Başka bir sağlayıcıdan tek bir belirli modele ihtiyacınız olduğunda kesin `provider/model` girdileri `provider/*` girdileriyle karıştırılabilir.

Örnek izin listesi yapılandırması:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-sonnet-4-6" },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "anthropic/claude-opus-4-6": { alias: "Opus" },      },    },  },}
[/code]

## Sohbette model değiştirme (`/model`)

Geçerli oturum için modelleri yeniden başlatmadan değiştirebilirsiniz:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model status
[/code]

Seçici davranışı

  * `/model` (ve `/model list`) kompakt, numaralı bir seçicidir (model ailesi + kullanılabilir sağlayıcılar).
  * Discord’da `/model` ve `/models`, sağlayıcı ve model açılır menüleri ile bir Submit adımı içeren etkileşimli bir seçici açar.
  * Telegram’da `/models` seçici seçimleri oturum kapsamlıdır; ajanın `openclaw.json` içindeki kalıcı varsayılanını değiştirmez.
  * `/models add` kullanımdan kaldırılmıştır ve artık sohbetten model kaydetmek yerine kullanımdan kaldırma mesajı döndürür.
  * `/model <#>` bu seçiciden seçim yapar.

Kalıcılık ve canlı geçiş

  * `/model`, yeni oturum seçimini hemen kalıcı hale getirir.
  * Ajan boşta ise sonraki çalıştırma yeni modeli hemen kullanır.
  * Bir çalıştırma zaten etkinse OpenClaw canlı geçişi beklemede olarak işaretler ve yalnızca temiz bir yeniden deneme noktasında yeni modele yeniden başlar.
  * Araç etkinliği veya yanıt çıktısı zaten başladıysa bekleyen geçiş, daha sonraki bir yeniden deneme fırsatına veya sonraki kullanıcı turuna kadar kuyrukta kalabilir.
  * Kullanıcı tarafından seçilen `/model` referansı o oturum için katıdır: seçilen sağlayıcı/model erişilemezse yanıt, sessizce `agents.defaults.model.fallbacks` üzerinden yanıtlamak yerine görünür biçimde başarısız olur. Bu, yapılandırılmış varsayılanlardan ve hâlâ geri dönüş zincirlerini kullanabilen cron işi birincillerinden farklıdır.
  * `/model status`, ayrıntılı görünümdür (auth adayları ve yapılandırıldığında sağlayıcı uç noktası `baseUrl` \+ `api` modu).

Ref ayrıştırma

  * Model ref'leri **ilk** `/` üzerinden bölünerek ayrıştırılır. `/model <ref>` yazarken `provider/model` kullanın.
  * Model kimliğinin kendisi `/` içeriyorsa (OpenRouter tarzı), sağlayıcı önekini eklemelisiniz (örnek: `/model openrouter/moonshotai/kimi-k2`).
  * Sağlayıcıyı atlarsanız OpenClaw girdiyi şu sırayla çözümler: 
    1. takma ad eşleşmesi
    2. o tam öneksiz model kimliği için benzersiz yapılandırılmış sağlayıcı eşleşmesi
    3. yapılandırılmış varsayılan sağlayıcıya kullanımdan kaldırılmış geri dönüş — bu sağlayıcı artık yapılandırılmış varsayılan modeli sunmuyorsa OpenClaw, eski ve kaldırılmış sağlayıcı varsayılanını göstermemek için bunun yerine ilk yapılandırılmış sağlayıcı/modele geri döner.


Tam komut davranışı/yapılandırması: [Slash komutları](</tr/tools/slash-commands>).

## CLI komutları

bashCopy code
[code]
    openclaw models listopenclaw models statusopenclaw models set <provider/model>openclaw models set-image <provider/model> openclaw models aliases listopenclaw models aliases add <alias> <provider/model>openclaw models aliases remove <alias> openclaw models fallbacks listopenclaw models fallbacks add <provider/model>openclaw models fallbacks remove <provider/model>openclaw models fallbacks clear openclaw models image-fallbacks listopenclaw models image-fallbacks add <provider/model>openclaw models image-fallbacks remove <provider/model>openclaw models image-fallbacks clear
[/code]

`openclaw models` (alt komut olmadan), `models status` için bir kısayoldur.

### `models list`

Varsayılan olarak yapılandırılmış/kimlik doğrulaması kullanılabilir modelleri gösterir. Kullanışlı bayraklar:

Tam katalog. Kimlik doğrulaması yapılandırılmadan önce paketlenmiş sağlayıcıya ait statik katalog satırlarını içerir; böylece yalnızca keşif görünümleri, eşleşen sağlayıcı kimlik bilgilerini ekleyene kadar kullanılamayan modelleri gösterebilir.

Yalnızca yerel sağlayıcılar.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcHJvdmlkZXIgPGlk " type="string"> Sağlayıcı kimliğine göre filtreleyin; örneğin `moonshot`. Etkileşimli seçicilerdeki görüntü etiketleri kabul edilmez.

Her satırda bir model.

Makine tarafından okunabilir çıktı.

### `models status`

Çözümlenen birincil modeli, geri dönüşleri, görüntü modelini ve yapılandırılmış sağlayıcıların kimlik doğrulama özetini gösterir. Ayrıca kimlik doğrulama deposunda bulunan profiller için OAuth süre sonu durumunu da gösterir (varsayılan olarak 24 saat içinde uyarır). `--plain` yalnızca çözümlenen birincil modeli yazdırır.

Kimlik doğrulama ve yoklama davranışı

  * OAuth durumu her zaman gösterilir (ve `--json` çıktısına dahil edilir). Yapılandırılmış bir sağlayıcının kimlik bilgileri yoksa `models status` bir **Eksik kimlik doğrulama** bölümü yazdırır.
  * JSON, `auth.oauth` (uyarı penceresi + profiller) ve `auth.providers` (env destekli kimlik bilgileri dahil sağlayıcı başına etkin kimlik doğrulama) içerir. `auth.oauth` yalnızca kimlik doğrulama deposu profil sağlığıdır; yalnızca env kullanan sağlayıcılar burada görünmez.
  * Otomasyon için `--check` kullanın (eksik/süresi dolmuş olduğunda çıkış `1`, süresi dolmak üzere olduğunda `2`).
  * Canlı kimlik doğrulama kontrolleri için `--probe` kullanın; yoklama satırları kimlik doğrulama profillerinden, env kimlik bilgilerinden veya `models.json` dosyasından gelebilir.
  * Açık `auth.order.<provider>` depolanmış bir profili atlıyorsa, yoklama bunu denemek yerine `excluded_by_auth_order` bildirir. Kimlik doğrulama varsa ancak bu sağlayıcı için yoklanabilir bir model çözümlenemiyorsa, yoklama `status: no_model` bildirir.


Örnek (Claude CLI):

bashCopy code
[code]
    claude auth loginopenclaw models status
[/code]

## Tarama (OpenRouter ücretsiz modelleri)

`openclaw models scan`, OpenRouter'ın **ücretsiz model kataloğunu** inceler ve isteğe bağlı olarak modelleri araç ve görüntü desteği açısından yoklayabilir.

Canlı yoklamaları atla (yalnızca meta veri).

`agents.defaults.model.primary` değerini ilk seçime ayarla.

`agents.defaults.imageModel.primary` değerini ilk görüntü seçimine ayarla.

Tarama sonuçları şuna göre sıralanır:

  1. Görüntü desteği
  2. Araç gecikmesi
  3. Bağlam boyutu
  4. Parametre sayısı


Girdi:

  * OpenRouter `/models` listesi (filtre `:free`)
  * Canlı yoklamalar, kimlik doğrulama profillerinden veya `OPENROUTER_API_KEY` üzerinden OpenRouter API anahtarı gerektirir (bkz. [Ortam değişkenleri](</tr/help/environment>))
  * İsteğe bağlı filtreler: `--max-age-days`, `--min-params`, `--provider`, `--max-candidates`
  * İstek/yoklama kontrolleri: `--timeout`, `--concurrency`


Canlı yoklamalar bir TTY içinde çalıştığında, geri dönüşleri etkileşimli olarak seçebilirsiniz. Etkileşimli olmayan modda varsayılanları kabul etmek için `--yes` iletin. Yalnızca meta veri sonuçları bilgilendirme amaçlıdır; `--set-default` ve `--set-image`, OpenClaw'ın kullanılamaz anahtarsız bir OpenRouter modeli yapılandırmaması için canlı yoklamalar gerektirir.

## Modeller kayıt defteri (`models.json`)

`models.providers` içindeki özel sağlayıcılar, aracı dizini altında `models.json` dosyasına yazılır (varsayılan `~/.openclaw/agents/<agentId>/agent/models.json`). Bu dosya, `models.mode` değeri `replace` olarak ayarlanmadıkça varsayılan olarak birleştirilir.

Birleştirme modu önceliği

Eşleşen sağlayıcı kimlikleri için birleştirme modu önceliği:

  * Aracı `models.json` dosyasında zaten bulunan boş olmayan `baseUrl` kazanır.
  * Aracı `models.json` dosyasındaki boş olmayan `apiKey`, yalnızca bu sağlayıcı mevcut yapılandırma/kimlik doğrulama profili bağlamında SecretRef tarafından yönetilmiyorsa kazanır.
  * SecretRef tarafından yönetilen sağlayıcı `apiKey` değerleri, çözümlenmiş gizli değerleri kalıcı hale getirmek yerine kaynak işaretçilerinden (env ref'leri için `ENV_VAR_NAME`, file/exec ref'leri için `secretref-managed`) yenilenir.
  * SecretRef tarafından yönetilen sağlayıcı üst bilgi değerleri, kaynak işaretçilerinden (env ref'leri için `secretref-env:ENV_VAR_NAME`, file/exec ref'leri için `secretref-managed`) yenilenir.
  * Boş veya eksik aracı `apiKey`/`baseUrl`, yapılandırma `models.providers` değerine geri döner.
  * Diğer sağlayıcı alanları yapılandırmadan ve normalleştirilmiş katalog verilerinden yenilenir.


## İlgili

  * [Aracı çalışma zamanları](</tr/concepts/agent-runtimes>) — PI, Codex ve diğer aracı döngüsü çalışma zamanları
  * [Yapılandırma başvurusu](</tr/gateway/config-agents#agent-defaults>) — model yapılandırma anahtarları
  * [Görüntü oluşturma](</tr/tools/image-generation>) — görüntü modeli yapılandırması
  * [Model yük devri](</tr/concepts/model-failover>) — geri dönüş zincirleri
  * [Model sağlayıcıları](</tr/concepts/model-providers>) — sağlayıcı yönlendirme ve kimlik doğrulama
  * [Müzik oluşturma](</tr/tools/music-generation>) — müzik modeli yapılandırması
  * [Video oluşturma](</tr/tools/video-generation>) — video modeli yapılandırması


Was this useful?YesNo