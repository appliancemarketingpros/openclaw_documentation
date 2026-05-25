---
title: Video oluşturma
source_url: https://docs.openclaw.ai/tr/tools/video-generation
scraped_at: 2026-05-25
---

OpenClaw aracıları metin istemlerinden, referans görüntülerden veya mevcut videolardan video oluşturabilir. Her biri farklı model seçenekleri, girdi modları ve özellik kümeleri sunan on altı sağlayıcı arka ucu desteklenir. Aracı, yapılandırmanıza ve mevcut API anahtarlarınıza göre doğru sağlayıcıyı otomatik olarak seçer.

OpenClaw video oluşturmayı üç çalışma zamanı modu olarak ele alır:

  * `generate` \- referans medya içermeyen metinden videoya istekleri.
  * `imageToVideo` \- istek bir veya daha fazla referans görüntü içerir.
  * `videoToVideo` \- istek bir veya daha fazla referans video içerir.


Sağlayıcılar bu modların herhangi bir alt kümesini destekleyebilir. Araç, göndermeden önce etkin modu doğrular ve desteklenen modları `action=list` içinde bildirir.

## Hızlı başlangıç

* ### Kimlik doğrulamayı yapılandırın

Desteklenen herhangi bir sağlayıcı için bir API anahtarı ayarlayın:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Varsayılan bir model seçin (isteğe bağlı)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Aracıya sorun

> Gün batımında sörf yapan dost canlısı bir ıstakozun 5 saniyelik sinematik bir videosunu oluştur.

Aracı `video_generate` çağrısını otomatik olarak yapar. Araç için izin listesi gerekmez.

## Zaman uyumsuz oluşturma nasıl çalışır?

Video oluşturma zaman uyumsuzdur. Aracı bir oturumda `video_generate` çağırdığında:

  1. OpenClaw isteği sağlayıcıya gönderir ve hemen bir görev kimliği döndürür.
  2. Sağlayıcı işi arka planda işler (genellikle sağlayıcıya ve çözünürlüğe bağlı olarak 30 saniye ile birkaç dakika arası; yavaş kuyruk destekli sağlayıcılar yapılandırılan zaman aşımına kadar çalışabilir).
  3. Video hazır olduğunda OpenClaw aynı oturumu dahili bir tamamlama olayıyla uyandırır.
  4. Aracı kullanıcıya bildirir ve tamamlanan videoyu ekler. Yalnızca mesaj aracıyla görünür teslimat kullanan grup/kanal sohbetlerinde aracı, sonucu OpenClaw doğrudan göndermek yerine mesaj aracı üzerinden iletir.


Bir iş devam ederken aynı oturumdaki yinelenen `video_generate` çağrıları, başka bir oluşturma başlatmak yerine mevcut görev durumunu döndürür. CLI'den ilerlemeyi denetlemek için `openclaw tasks list` veya `openclaw tasks show <taskId>` kullanın.

Oturum destekli aracı çalıştırmaları dışında (örneğin doğrudan araç çağrılarında), araç satır içi oluşturmaya geri döner ve aynı turda son medya yolunu döndürür.

Sağlayıcı bayt döndürdüğünde oluşturulan video dosyaları OpenClaw tarafından yönetilen medya depolama alanına kaydedilir. Varsayılan oluşturulan video kaydetme üst sınırı video medya sınırını izler ve `agents.defaults.mediaMaxMb` daha büyük işleme çıktıları için bu sınırı yükseltir. Bir sağlayıcı ayrıca barındırılan bir çıktı URL'si döndürürse, yerel kalıcılık aşırı büyük bir dosyayı reddettiğinde OpenClaw görevi başarısız kılmak yerine bu URL'yi teslim edebilir.

### Görev yaşam döngüsü

Durum | Anlam  
---|---  
`queued` | Görev oluşturuldu, sağlayıcının kabul etmesi bekleniyor.  
`running` | Sağlayıcı işliyor (genellikle sağlayıcıya ve çözünürlüğe bağlı olarak 30 saniye ile birkaç dakika arası).  
`succeeded` | Video hazır; aracı uyanır ve videoyu konuşmaya gönderir.  
`failed` | Sağlayıcı hatası veya zaman aşımı; aracı hata ayrıntılarıyla uyanır.  
  
CLI'den durumu denetleyin:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Geçerli oturum için bir video görevi zaten `queued` veya `running` durumundaysa, `video_generate` yeni bir görev başlatmak yerine mevcut görev durumunu döndürür. Yeni bir oluşturmayı tetiklemeden açıkça denetlemek için `action: "status"` kullanın.

## Desteklenen sağlayıcılar

Sağlayıcı | Varsayılan model | Metin | Görüntü ref | Video ref | Kimlik doğrulama  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Evet (uzak URL) | Evet (uzak URL) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | En fazla 2 görüntü (yalnızca I2V modelleri; ilk + son kare) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | En fazla 2 görüntü (rol aracılığıyla ilk + son kare) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | En fazla 9 referans görüntü | En fazla 3 video | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 görüntü | - | `COMFY_API_KEY` veya `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 görüntü; Seedance referanstan videoya ile en fazla 9 | Seedance referanstan videoya ile en fazla 3 video | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 görüntü | 1 video | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 görüntü | - | `MINIMAX_API_KEY` veya MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 görüntü | 1 video | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | En fazla 4 görüntü (ilk/son kare veya referanslar) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Evet (uzak URL) | Evet (uzak URL) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 görüntü | 1 video | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 görüntü | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 görüntü (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 ilk kare görüntüsü veya en fazla 7 `reference_image` | 1 video | `XAI_API_KEY`  
  
Bazı sağlayıcılar ek veya alternatif API anahtarı ortam değişkenlerini kabul eder. Ayrıntılar için ilgili sağlayıcı sayfalarına bakın.

Çalışma zamanında mevcut sağlayıcıları, modelleri ve çalışma zamanı modlarını incelemek için `video_generate action=list` çalıştırın.

### Yetenek matrisi

`video_generate`, sözleşme testleri ve paylaşılan canlı tarama tarafından kullanılan açık mod sözleşmesi:

Sağlayıcı | `generate` | `imageToVideo` | `videoToVideo` | Bugünkü paylaşılan canlı hatlar  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` atlanır çünkü bu sağlayıcı uzak `http(s)` video URL'leri gerektirir  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Paylaşılan taramada yoktur; iş akışına özgü kapsam Comfy testleriyle birlikte yaşar  
DeepInfra | ✓ | - | - | `generate`; yerel DeepInfra video şemaları paketlenmiş sözleşmede metinden videoya yöneliktir  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` yalnızca Seedance referanstan videoya kullanılırken  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; paylaşılan `videoToVideo` atlanır çünkü mevcut tampon destekli Gemini/Veo taraması bu girdiyi kabul etmez  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; paylaşılan `videoToVideo` atlanır çünkü bu kuruluş/girdi yolu şu anda sağlayıcı tarafı inpaint/remix erişimi gerektirir  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` atlanır çünkü bu sağlayıcı uzak `http(s)` video URL'leri gerektirir  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` yalnızca seçili model `runway/gen4_aleph` olduğunda çalışır  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; paylaşılan `imageToVideo` atlanır çünkü paketlenmiş `veo3` yalnızca metin destekler ve paketlenmiş `kling` uzak görüntü URL'si gerektirir  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` atlanır çünkü bu sağlayıcı şu anda uzak bir MP4 URL'si gerektirir  
  
## Araç parametreleri

### Gerekli

Oluşturulacak videonun metin açıklaması. `action: "generate"` için gereklidir.

### İçerik girdileri

Birleştirilmiş görüntü listesine paralel, konum başına isteğe bağlı rol ipuçları. Kanonik değerler: `first_frame`, `last_frame`, `reference_image`.

Birleştirilmiş video listesine paralel, konum başına isteğe bağlı rol ipuçları. Kanonik değer: `reference_video`.

Tek referans sesi (yol veya URL). Sağlayıcı ses girişlerini desteklediğinde arka plan müziği veya ses referansı için kullanılır.

Birleştirilmiş ses listesine paralel, konum başına isteğe bağlı rol ipuçları. Kanonik değer: `reference_audio`.

### Stil denetimleri

`1:1`, `16:9`, `9:16`, `adaptive` veya sağlayıcıya özgü bir değer gibi en-boy oranı ipucu. OpenClaw desteklenmeyen değerleri sağlayıcı başına normalleştirir veya yok sayar.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI `480P`, `720P`, `768P`, `1080P`, `4K` veya sağlayıcıya özgü bir değer gibi çözünürlük ipucu. OpenClaw desteklenmeyen değerleri sağlayıcı başına normalleştirir veya yok sayar. OPENCLAW_DOCS_MARKER:paramClose:

Saniye cinsinden hedef süre (sağlayıcının desteklediği en yakın değere yuvarlanır).

Desteklendiğinde çıktıda üretilmiş sesi etkinleştirir. `audioRef*` girdilerinden ayrıdır.

`adaptive`, sağlayıcıya özgü bir belirteçtir: yeteneklerinde `adaptive` bildiren sağlayıcılara olduğu gibi iletilir (ör. BytePlus Seedance, giriş görüntüsünün boyutlarından oranı otomatik algılamak için bunu kullanır). Bunu bildirmeyen sağlayıcılar, düşüşün görünür olması için araç sonucunda değeri `details.ignoredOverrides` üzerinden gösterir.

### Gelişmiş

`"status"` geçerli oturum görevini döndürür; `"list"` sağlayıcıları inceler.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Sağlayıcı/model geçersiz kılma (ör. `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Milisaniye cinsinden isteğe bağlı sağlayıcı işlem zaman aşımı. Atlandığında, yapılandırılmışsa OpenClaw `agents.defaults.videoGenerationModel.timeoutMs` kullanır. OPENCLAW_DOCS_MARKER:paramClose:

JSON nesnesi olarak sağlayıcıya özgü seçenekler (ör. `{"seed": 42, "draft": true}`). Türlü şema bildiren sağlayıcılar anahtarları ve türleri doğrular; bilinmeyen anahtarlar veya uyuşmazlıklar fallback sırasında adayı atlar. Bildirilmiş şeması olmayan sağlayıcılar seçenekleri olduğu gibi alır. Her sağlayıcının ne kabul ettiğini görmek için `video_generate action=list` çalıştırın.

Referans girdileri çalışma zamanı modunu seçer:

  * Referans medya yok → `generate`
  * Herhangi bir görüntü referansı → `imageToVideo`
  * Herhangi bir video referansı → `videoToVideo`
  * Referans ses girdileri çözümlenen modu **değiştirmez** ; görüntü/video referanslarının seçtiği modun üzerine uygulanır ve yalnızca `maxInputAudios` bildiren sağlayıcılarla çalışır.


Karışık görüntü ve video referansları kararlı bir ortak yetenek yüzeyi değildir. İstek başına tek bir referans türünü tercih edin.

#### Fallback ve türlü seçenekler

Bazı yetenek denetimleri araç sınırı yerine fallback katmanında uygulanır; bu nedenle birincil sağlayıcının sınırlarını aşan bir istek yine de yetenekli bir fallback üzerinde çalışabilir:

  * `maxInputAudios` bildirmeyen (veya `0` bildiren) etkin aday, istek ses referansları içerdiğinde atlanır; sonraki aday denenir.
  * Etkin adayın `maxDurationSeconds` değeri, bildirilmiş `supportedDurationSeconds` listesi olmadan istenen `durationSeconds` değerinin altındaysa → atlanır.
  * İstek `providerOptions` içerir ve etkin aday açıkça türlü bir `providerOptions` şeması bildirirse → sağlanan anahtarlar şemada yoksa veya değer türleri eşleşmiyorsa atlanır. Bildirilmiş şeması olmayan sağlayıcılar seçenekleri olduğu gibi alır (geriye dönük uyumlu geçiş). Bir sağlayıcı boş şema (`capabilities.providerOptions: {}`) bildirerek tüm sağlayıcı seçeneklerinden çıkabilir; bu da tür uyuşmazlığıyla aynı atlamaya neden olur.


Bir istekteki ilk atlama nedeni `warn` düzeyinde günlüğe yazılır; böylece operatörler birincil sağlayıcılarının ne zaman geçildiğini görür. Sonraki atlamalar, uzun fallback zincirlerini sessiz tutmak için `debug` düzeyinde günlüğe yazılır. Her aday atlanırsa, birleştirilmiş hata her biri için atlama nedenini içerir.

## Eylemler

Eylem | Ne yapar  
---|---  
`generate` | Varsayılan. Verilen istemden ve isteğe bağlı referans girdilerinden bir video oluşturur.  
`status` | Başka bir üretim başlatmadan geçerli oturum için devam eden video görevinin durumunu denetler.  
`list` | Kullanılabilir sağlayıcıları, modelleri ve yeteneklerini gösterir.  
  
## Model seçimi

OpenClaw modeli şu sırayla çözer:

  1. **`model` araç parametresi** \- aracı agent çağrıda bir tane belirtirse.
  2. Yapılandırmadan **`videoGenerationModel.primary`**.
  3. Sırayla **`videoGenerationModel.fallbacks`**.
  4. **Otomatik algılama** \- geçerli varsayılan sağlayıcıdan başlayarak, ardından kalan sağlayıcılar alfabetik sırayla, geçerli kimlik doğrulaması olan sağlayıcılar.


Bir sağlayıcı başarısız olursa, sonraki aday otomatik olarak denenir. Tüm adaylar başarısız olursa, hata her denemeden ayrıntılar içerir.

Yalnızca açık `model`, `primary` ve `fallbacks` girdilerini kullanmak için `agents.defaults.mediaGenerationAutoProviderFallback: false` ayarlayın.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Sağlayıcı notları

Alibaba

DashScope / Model Studio zaman uyumsuz uç noktasını kullanır. Referans görüntüleri ve videoları uzak `http(s)` URL'leri olmalıdır.

BytePlus (1.0)

Sağlayıcı kimliği: `byteplus`.

Modeller: `seedance-1-0-pro-250528` (varsayılan), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

T2V modelleri (`*-t2v-*`) görüntü girdilerini kabul etmez; I2V modelleri ve genel `*-pro-*` modelleri tek bir referans görüntüsünü (ilk kare) destekler. Görüntüyü konumsal olarak geçirin veya `role: "first_frame"` ayarlayın. Bir görüntü sağlandığında T2V model kimlikleri otomatik olarak karşılık gelen I2V varyantına geçirilir.

Desteklenen `providerOptions` anahtarları: `seed` (sayı), `draft` (boolean - 480p'yi zorlar), `camera_fixed` (boolean).

BytePlus Seedance 1.5

[`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>) Plugin gerektirir. Sağlayıcı kimliği: `byteplus-seedance15`. Model: `seedance-1-5-pro-251215`.

Birleşik `content[]` API'sini kullanır. En fazla 2 giriş görüntüsünü (`first_frame` \+ `last_frame`) destekler. Tüm girdiler uzak `https://` URL'leri olmalıdır. Her görüntüde `role: "first_frame"` / `"last_frame"` ayarlayın veya görüntüleri konumsal olarak geçirin.

`aspectRatio: "adaptive"` oranı giriş görüntüsünden otomatik algılar. `audio: true`, `generate_audio` değerine eşlenir. `providerOptions.seed` (sayı) iletilir.

BytePlus Seedance 2.0

[`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>) Plugin gerektirir. Sağlayıcı kimliği: `byteplus-seedance2`. Modeller: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Birleşik `content[]` API'sini kullanır. En fazla 9 referans görüntüsü, 3 referans videosu ve 3 referans sesi destekler. Tüm girdiler uzak `https://` URL'leri olmalıdır. Her varlıkta `role` ayarlayın - desteklenen değerler: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` oranı giriş görüntüsünden otomatik algılar. `audio: true`, `generate_audio` değerine eşlenir. `providerOptions.seed` (sayı) iletilir.

ComfyUI

İş akışı odaklı yerel veya bulut yürütme. Yapılandırılmış grafik üzerinden metinden videoya ve görüntüden videoya dönüştürmeyi destekler.

fal

Uzun süren işler için kuyruk destekli bir akış kullanır. OpenClaw, devam eden bir fal kuyruk işini zaman aşımına uğramış saymadan önce varsayılan olarak en fazla 20 dakika bekler. Çoğu fal video modeli tek bir görüntü referansı kabul eder. Seedance 2.0 referanstan videoya modelleri en fazla 9 görüntü, 3 video ve 3 ses referansı kabul eder; toplam referans dosyası sayısı en fazla 12 olabilir.

Google (Gemini / Veo)

Bir görüntü veya bir video referansını destekler. Ses oluşturma istekleri, Gemini API yolunda bir uyarıyla yok sayılır çünkü bu API mevcut Veo video oluşturma için `generateAudio` parametresini reddeder.

MiniMax

Yalnızca tek görüntü referansı. MiniMax `768P` ve `1080P` çözünürlüklerini kabul eder; `720P` gibi istekler gönderilmeden önce en yakın desteklenen değere normalleştirilir.

OpenAI

Yalnızca `size` geçersiz kılması iletilir. Diğer stil geçersiz kılmaları (`aspectRatio`, `resolution`, `audio`, `watermark`) bir uyarıyla yok sayılır.

OpenRouter

OpenRouter'ın eşzamansız `/videos` API'sini kullanır. OpenClaw işi gönderir, `polling_url` adresini yoklar ve `unsigned_urls` ya da belgelenmiş iş içeriği uç noktasını indirir. Birlikte sunulan varsayılan `google/veo-3.1-fast`, 4/6/8 saniyelik süreleri, `720P`/`1080P` çözünürlükleri ve `16:9`/`9:16` en boy oranlarını duyurur.

Qwen

Alibaba ile aynı DashScope arka ucunu kullanır. Referans girdileri uzak `http(s)` URL'leri olmalıdır; yerel dosyalar baştan reddedilir.

Runway

Veri URI'leri aracılığıyla yerel dosyaları destekler. Videodan videoya dönüştürme `runway/gen4_aleph` gerektirir. Yalnızca metin çalıştırmaları `16:9` ve `9:16` en boy oranlarını sunar.

Together

Yalnızca tek görüntü referansı.

Vydra

Kimlik doğrulamasını düşüren yönlendirmelerden kaçınmak için doğrudan `https://www.vydra.ai/api/v1` kullanır. `veo3` yalnızca metinden videoya olarak birlikte sunulur; `kling` uzak bir görüntü URL'si gerektirir.

xAI

Metinden videoya, tek ilk kare görüntüsünden videoya, xAI `reference_images` üzerinden en fazla 7 `reference_image` girdisini ve uzak video düzenleme/genişletme akışlarını destekler.

## Sağlayıcı yetenek modları

Paylaşılan video oluşturma sözleşmesi yalnızca düz toplu sınırlar yerine moda özgü yetenekleri destekler. Yeni sağlayıcı uygulamaları açık mod bloklarını tercih etmelidir:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

`maxInputImages` ve `maxInputVideos` gibi düz toplu alanlar, dönüştürme modu desteğini duyurmak için **yeterli değildir**. Sağlayıcılar `generate`, `imageToVideo` ve `videoToVideo` alanlarını açıkça tanımlamalıdır; böylece canlı testler, sözleşme testleri ve paylaşılan `video_generate` aracı mod desteğini deterministik olarak doğrulayabilir.

Bir sağlayıcıdaki tek bir model, diğerlerinden daha geniş referans girdisi desteğine sahipse mod genelindeki sınırı yükseltmek yerine `maxInputImagesByModel`, `maxInputVideosByModel` veya `maxInputAudiosByModel` kullanın.

## Canlı testler

Paylaşılan birlikte sunulan sağlayıcılar için isteğe bağlı canlı kapsam:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Repo sarmalayıcısı:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

Bu canlı dosya eksik sağlayıcı env değişkenlerini `~/.profile` dosyasından yükler, varsayılan olarak canlı/env API anahtarlarını saklanan kimlik doğrulama profillerinden önce tercih eder ve varsayılan olarak sürüm için güvenli bir smoke çalıştırır:

  * Taramadaki FAL dışındaki her sağlayıcı için `generate`.
  * Bir saniyelik ıstakoz promptu.
  * Sağlayıcı başına işlem sınırı `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` değerinden alınır (varsayılan `180000`).


FAL isteğe bağlıdır çünkü sağlayıcı tarafındaki kuyruk gecikmesi sürüm süresine baskın gelebilir:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Paylaşılan taramanın yerel medya ile güvenle çalıştırabileceği tanımlı dönüştürme modlarını da çalıştırmak için `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` ayarlayın:

  * `capabilities.imageToVideo.enabled` olduğunda `imageToVideo`.
  * `capabilities.videoToVideo.enabled` olduğunda ve sağlayıcı/model paylaşılan taramada arabellek destekli yerel video girdisini kabul ettiğinde `videoToVideo`.


Bugün paylaşılan `videoToVideo` canlı hattı, yalnızca `runway/gen4_aleph` seçtiğinizde `runway` kapsamına alır.

## Yapılandırma

OpenClaw yapılandırmanızda varsayılan video oluşturma modelini ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

Ya da CLI üzerinden:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## İlgili

  * [Alibaba Model Studio](</tr/providers/alibaba>)
  * [Arka plan görevleri](</tr/automation/tasks>) \- eşzamansız video oluşturma için görev takibi
  * [BytePlus](</tr/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</tr/providers/comfy>)
  * [Yapılandırma başvurusu](</tr/gateway/config-agents#agent-defaults>)
  * [fal](</tr/providers/fal>)
  * [Google (Gemini)](</tr/providers/google>)
  * [MiniMax](</tr/providers/minimax>)
  * [Modeller](</tr/concepts/models>)
  * [OpenAI](</tr/providers/openai>)
  * [Qwen](</tr/providers/qwen>)
  * [Runway](</tr/providers/runway>)
  * [Together AI](</tr/providers/together>)
  * [Araçlara genel bakış](</tr/tools>)
  * [Vydra](</tr/providers/vydra>)
  * [xAI](</tr/providers/xai>)


Was this useful?YesNo