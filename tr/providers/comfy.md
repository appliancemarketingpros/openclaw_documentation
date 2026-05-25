---
title: ComfyUI
source_url: https://docs.openclaw.ai/tr/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw, iş akışı tabanlı ComfyUI çalıştırmaları için paketlenmiş bir `comfy` Plugin'i ile gelir. Plugin tamamen iş akışı odaklıdır; bu nedenle OpenClaw genel `size`, `aspectRatio`, `resolution`, `durationSeconds` veya TTS tarzı denetimleri grafiğinize eşlemeye çalışmaz.

Özellik | Ayrıntı  
---|---  
Sağlayıcı | `comfy`  
Modeller | `comfy/workflow`  
Paylaşılan yüzeyler | `image_generate`, `video_generate`, `music_generate`  
Kimlik doğrulama | Yerel ComfyUI için yok; Comfy Cloud için `COMFY_API_KEY` veya `COMFY_CLOUD_API_KEY`  
API | ComfyUI `/prompt` / `/history` / `/view` ve Comfy Cloud `/api/*`  
  
## Destekledikleri

  * Bir iş akışı JSON'undan görsel üretimi
  * 1 yüklenmiş referans görselle görsel düzenleme
  * Bir iş akışı JSON'undan video üretimi
  * 1 yüklenmiş referans görselle video üretimi
  * Paylaşılan `music_generate` aracı üzerinden müzik veya ses üretimi
  * Yapılandırılmış bir node'dan veya eşleşen tüm çıktı node'larından çıktı indirme


## Başlarken

ComfyUI'ı kendi makinenizde çalıştırma veya Comfy Cloud kullanma arasında seçim yapın.

### Yerel

**En iyisi:** Kendi ComfyUI örneğinizi makinenizde veya LAN üzerinde çalıştırmak.

* ### ComfyUI'ı yerelde başlatın

Yerel ComfyUI örneğinizin çalıştığından emin olun (varsayılan `http://127.0.0.1:8188`).

* ### İş akışı JSON'unuzu hazırlayın

Bir ComfyUI iş akışı JSON dosyasını dışa aktarın veya oluşturun. Prompt girdi node'u ile OpenClaw'ın okuyacağı çıktı node'u için node kimliklerini not edin.

* ### Sağlayıcıyı yapılandırın

`mode: "local"` ayarlayın ve iş akışı dosyanıza işaret edin. Burada en düşük bir görsel örneği bulunuyor:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Varsayılan modeli ayarlayın

OpenClaw'ı, yapılandırdığınız yetenek için `comfy/workflow` modeline yönlendirin:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Doğrulayın

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**En iyisi:** Yerel GPU kaynaklarını yönetmeden iş akışlarını Comfy Cloud üzerinde çalıştırmak.

* ### Bir API anahtarı alın

[comfy.org](<https://comfy.org>) adresinden kaydolun ve hesap kontrol panelinizden bir API anahtarı oluşturun.

* ### API anahtarını ayarlayın

Anahtarınızı şu yöntemlerden biriyle sağlayın:

bashCopy code
[code]
    # Ortam değişkeni (tercih edilen)export COMFY_API_KEY="your-key" # Alternatif ortam değişkeniexport COMFY_CLOUD_API_KEY="your-key" # Veya doğrudan config içindeopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### İş akışı JSON'unuzu hazırlayın

Bir ComfyUI iş akışı JSON dosyasını dışa aktarın veya oluşturun. Prompt girdi node'u ile çıktı node'u için node kimliklerini not edin.

* ### Sağlayıcıyı yapılandırın

`mode: "cloud"` ayarlayın ve iş akışı dosyanıza işaret edin:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Varsayılan modeli ayarlayın

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Doğrulayın

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Yapılandırma

Comfy, paylaşılan üst düzey bağlantı ayarlarını ve yetenek başına iş akışı bölümlerini (`image`, `video`, `music`) destekler:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Paylaşılan anahtarlar

Anahtar | Tür | Açıklama  
---|---|---  
`mode` | `"local"` veya `"cloud"` | Bağlantı modu.  
`baseUrl` | string | Yerel için varsayılan `http://127.0.0.1:8188`, bulut için `https://cloud.comfy.org`.  
`apiKey` | string | İsteğe bağlı doğrudan anahtar; `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY` env değişkenlerine alternatiftir.  
`allowPrivateNetwork` | boolean | Cloud modunda özel/LAN `baseUrl` değerine izin verir.  
  
### Yetenek başına anahtarlar

Bu anahtarlar `image`, `video` veya `music` bölümleri içinde geçerlidir:

Anahtar | Gerekli | Varsayılan | Açıklama  
---|---|---|---  
`workflow` veya `workflowPath` | Evet | \-- | ComfyUI iş akışı JSON dosyasının yolu.  
`promptNodeId` | Evet | \-- | Metin prompt'unu alan node kimliği.  
`promptInputName` | Hayır | `"text"` | Prompt node'u üzerindeki girdi adı.  
`outputNodeId` | Hayır | \-- | Çıktının okunacağı node kimliği. Atlanırsa, eşleşen tüm çıktı node'ları kullanılır.  
`pollIntervalMs` | Hayır | \-- | İş tamamlanması için milisaniye cinsinden yoklama aralığı.  
`timeoutMs` | Hayır | \-- | İş akışı çalıştırması için milisaniye cinsinden zaman aşımı.  
  
`image` ve `video` bölümleri ayrıca şunları da destekler:

Anahtar | Gerekli | Varsayılan | Açıklama  
---|---|---|---  
`inputImageNodeId` | Evet (referans görsel geçirilirken) | \-- | Yüklenmiş referans görseli alan node kimliği.  
`inputImageInputName` | Hayır | `"image"` | Görsel node'u üzerindeki girdi adı.  
  
## İş akışı ayrıntıları

Görsel iş akışları

Varsayılan görsel modelini `comfy/workflow` olarak ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Referans görsel düzenleme örneği:**

Yüklenmiş bir referans görselle görsel düzenlemeyi etkinleştirmek için görsel config'inize `inputImageNodeId` ekleyin:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video iş akışları

Varsayılan video modelini `comfy/workflow` olarak ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy video iş akışları, yapılandırılmış grafik üzerinden metinden videoya ve görselden videoya desteği sunar.

Müzik iş akışları

Paketlenmiş Plugin, iş akışıyla tanımlanan ses veya müzik çıktıları için shared `music_generate` aracı üzerinden sunulan bir müzik üretim sağlayıcısı kaydeder:

textCopy code
[code]
    /tool music_generate prompt="Sıcak ambient synth loop, yumuşak tape dokulu"
[/code]

Ses iş akışı JSON'unuza ve çıktı node'unuza işaret etmek için `music` config bölümünü kullanın.

Geriye dönük uyumluluk

Mevcut üst düzey görsel config'i (`image` iç içe bölümü olmadan) hâlâ çalışır:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw, bu eski biçimi görsel iş akışı config'i olarak ele alır. Hemen taşımanız gerekmez, ancak yeni kurulumlar için iç içe `image` / `video` / `music` bölümleri önerilir.

Canlı testler

Paketlenmiş Plugin için isteğe bağlı canlı kapsama mevcuttur:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Eşleşen Comfy iş akışı bölümü yapılandırılmamışsa canlı test, tek tek görsel, video veya müzik vakalarını atlar.

## İlgili

[**Görsel Üretimi** Görsel üretim aracı yapılandırması ve kullanımı. ](</tr/tools/image-generation>) [**Video Üretimi** Video üretim aracı yapılandırması ve kullanımı. ](</tr/tools/video-generation>) [**Müzik Üretimi** Müzik ve ses üretim aracı kurulumu. ](</tr/tools/music-generation>) [**Sağlayıcı Dizini** Tüm sağlayıcılara ve model referanslarına genel bakış. ](</tr/providers>) [**Yapılandırma başvurusu** Aracı varsayılanları dâhil tam yapılandırma başvurusu. ](</tr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo