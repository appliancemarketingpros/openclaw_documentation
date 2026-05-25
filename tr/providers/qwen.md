---
title: Qwen
source_url: https://docs.openclaw.ai/tr/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw artık Qwen'i standart kimliği `qwen` olan birinci sınıf paketlenmiş sağlayıcı olarak ele alır. Paketlenmiş sağlayıcı, Qwen Cloud / Alibaba DashScope ve Coding Plan uç noktalarını hedefler ve eski `modelstudio` kimliklerinin uyumluluk takma adı olarak çalışmasını sürdürür.

  * Sağlayıcı: `qwen`
  * Tercih edilen ortam değişkeni: `QWEN_API_KEY`
  * Uyumluluk için ayrıca kabul edilir: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * API stili: OpenAI uyumlu


## Başlarken

Plan türünüzü seçin ve kurulum adımlarını izleyin.

### Coding Plan (subscription)

**En uygun olduğu durum:** Qwen Coding Plan üzerinden abonelik tabanlı erişim.

* ### Get your API key

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) üzerinden bir API anahtarı oluşturun veya kopyalayın.

* ### Run onboarding

**Global** uç nokta için:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

**China** uç noktası için:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pay-as-you-go)

**En uygun olduğu durum:** Coding Plan'da kullanılamayabilecek `qwen3.6-plus` gibi modeller dahil olmak üzere Standard Model Studio uç noktası üzerinden kullandıkça öde erişimi.

* ### Get your API key

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) üzerinden bir API anahtarı oluşturun veya kopyalayın.

* ### Run onboarding

**Global** uç nokta için:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

**China** uç noktası için:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## Plan türleri ve uç noktalar

Plan | Bölge | Kimlik doğrulama seçimi | Uç nokta  
---|---|---|---  
Standard (pay-as-you-go) | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (pay-as-you-go) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (subscription) | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (subscription) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Sağlayıcı, auth choice seçiminize göre uç noktayı otomatik olarak seçer. Standart seçimler `qwen-*` ailesini kullanır; `modelstudio-*` yalnızca uyumluluk için kalır. Yapılandırmada özel bir `baseUrl` ile geçersiz kılabilirsiniz.

## Yerleşik katalog

OpenClaw şu anda bu paketlenmiş Qwen kataloğuyla gelir. Yapılandırılan katalog uç nokta farkındadır: Coding Plan yapılandırmaları, yalnızca Standard uç noktasında çalıştığı bilinen modelleri hariç tutar.

Model başvurusu | Girdi | Bağlam | Notlar  
---|---|---|---  
`qwen/qwen3.5-plus` | metin, görüntü | 1,000,000 | Varsayılan model  
`qwen/qwen3.6-plus` | metin, görüntü | 1,000,000 | Bu modele ihtiyacınız olduğunda Standard uç noktalarını tercih edin  
`qwen/qwen3-max-2026-01-23` | metin | 262,144 | Qwen Max serisi  
`qwen/qwen3-coder-next` | metin | 262,144 | Kodlama  
`qwen/qwen3-coder-plus` | metin | 1,000,000 | Kodlama  
`qwen/MiniMax-M2.5` | metin | 1,000,000 | Akıl yürütme etkin  
`qwen/glm-5` | metin | 202,752 | GLM  
`qwen/glm-4.7` | metin | 202,752 | GLM  
`qwen/kimi-k2.5` | metin, görüntü | 262,144 | Alibaba üzerinden Moonshot AI  
  
## Düşünme Kontrolleri

Akıl yürütme etkin Qwen Cloud modelleri için paketlenmiş sağlayıcı, OpenClaw düşünme düzeylerini DashScope'un üst düzey `enable_thinking` istek bayrağına eşler. Devre dışı düşünme `enable_thinking: false` gönderir; diğer düşünme düzeyleri `enable_thinking: true` gönderir.

## Çok modlu eklentiler

`qwen` Plugin, **Standard** DashScope uç noktalarında da çok modlu yetenekler sunar (Coding Plan uç noktalarında değil):

  * `qwen-vl-max-latest` üzerinden **video anlama**
  * `wan2.6-t2v` (varsayılan), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v` üzerinden **Wan video oluşturma**


Qwen'i varsayılan video sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Gelişmiş yapılandırma

Image and video understanding

Paketlenmiş Qwen Plugin, **Standard** DashScope uç noktalarında görüntüler ve video için medya anlamayı kaydeder (Coding Plan uç noktalarında değil).

Özellik | Değer  
---|---  
Model | `qwen-vl-max-latest`  
Desteklenen girdi | Görüntüler, video  
  
Medya anlama, yapılandırılmış Qwen kimlik doğrulamasından otomatik olarak çözümlenir; ek yapılandırma gerekmez. Medya anlama desteği için Standard (pay-as-you-go) uç noktası kullandığınızdan emin olun.

Qwen 3.6 Plus availability

`qwen3.6-plus`, Standard (pay-as-you-go) Model Studio uç noktalarında kullanılabilir:

  * China: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Coding Plan uç noktaları `qwen3.6-plus` için "unsupported model" hatası döndürürse, Coding Plan uç noktası/anahtar çifti yerine Standard (pay-as-you-go) kullanın.

OpenClaw'ın paketlenmiş Qwen kataloğu, Coding Plan uç noktalarında `qwen3.6-plus` ilan etmez, ancak `models.providers.qwen.models` altında açıkça yapılandırılmış `qwen/qwen3.6-plus` girdileri Coding Plan baseUrl'lerinde dikkate alınır; böylece Aliyun aboneliğinizde bunu etkinleştirirse bu modeli dahil etmeyi seçebilirsiniz. Çağrının başarılı olup olmayacağına yine yukarı akış API karar verir.

Capability plan

`qwen` Plugin, yalnızca kodlama/metin modelleri için değil, tam Qwen Cloud yüzeyi için sağlayıcı evi olarak konumlandırılıyor.

  * **Metin/sohbet modelleri:** şimdi paketlenmiş
  * **Araç çağırma, yapılandırılmış çıktı, düşünme:** OpenAI uyumlu aktarımdan devralınır
  * **Görüntü oluşturma:** sağlayıcı-Plugin katmanında planlanıyor
  * **Görüntü/video anlama:** şimdi Standard uç noktasında paketlenmiş
  * **Konuşma/ses:** sağlayıcı-Plugin katmanında planlanıyor
  * **Bellek gömmeleri/yeniden sıralama:** gömme bağdaştırıcısı yüzeyi üzerinden planlanıyor
  * **Video oluşturma:** paylaşılan video oluşturma yeteneği üzerinden şimdi paketlenmiş

Video generation details

Video oluşturma için OpenClaw, işi göndermeden önce yapılandırılmış Qwen bölgesini eşleşen DashScope AIGC ana makinesine eşler:

  * Global/Intl: `https://dashscope-intl.aliyuncs.com`
  * China: `https://dashscope.aliyuncs.com`


Bu, Coding Plan veya Standard Qwen ana makinelerinden birini işaret eden normal bir `models.providers.qwen.baseUrl` değerinin bile video oluşturmayı doğru bölgesel DashScope video uç noktasında tuttuğu anlamına gelir.

Mevcut paketlenmiş Qwen video oluşturma sınırları:

  * İstek başına en fazla **1** çıktı videosu
  * En fazla **1** girdi görüntüsü
  * En fazla **4** girdi videosu
  * En fazla **10 saniye** süre
  * `size`, `aspectRatio`, `resolution`, `audio` ve `watermark` desteklenir
  * Referans görüntü/video modu şu anda **uzak http(s) URL'leri** gerektirir. DashScope video uç noktası bu referanslar için yüklenmiş yerel arabellekleri kabul etmediğinden yerel dosya yolları baştan reddedilir.

Streaming usage compatibility

Yerel Model Studio uç noktaları, paylaşılan `openai-completions` aktarımında akış kullanım uyumluluğunu duyurur. OpenClaw artık bunu uç nokta yeteneklerine göre anahtarlar; bu nedenle aynı yerel ana makineleri hedefleyen DashScope uyumlu özel sağlayıcı kimlikleri, özellikle yerleşik `qwen` sağlayıcı kimliğini gerektirmek yerine aynı akış kullanım davranışını devralır.

Yerel akış kullanım uyumluluğu hem Coding Plan ana makineleri hem de Standard DashScope uyumlu ana makineler için geçerlidir:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Multimodal endpoint regions

Çok modlu yüzeyler (video anlama ve Wan video oluşturma), Coding Plan uç noktalarını değil **Standard** DashScope uç noktalarını kullanır:

  * Global/Intl Standard temel URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * China Standard temel URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Ortam ve daemon kurulumu

Gateway bir daemon olarak çalışıyorsa (launchd/systemd), `QWEN_API_KEY` değerinin bu işlem için kullanılabilir olduğundan emin olun (örneğin `~/.openclaw/.env` içinde veya `env.shellEnv` aracılığıyla).

## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Video oluşturma** Paylaşılan video aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/video-generation>) [**Alibaba (ModelStudio)** Eski ModelStudio sağlayıcısı ve geçiş notları. ](</tr/providers/alibaba>) [**Sorun giderme** Genel sorun giderme ve SSS. ](</tr/help/troubleshooting>)

Was this useful?YesNo