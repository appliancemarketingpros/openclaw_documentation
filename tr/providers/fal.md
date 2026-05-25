---
title: Fal
source_url: https://docs.openclaw.ai/tr/providers/fal
scraped_at: 2026-05-25
---

OpenClaw, barındırılan görüntü ve video üretimi için yerleşik bir `fal` sağlayıcısıyla gelir.

Özellik | Değer  
---|---  
Sağlayıcı | `fal`  
Kimlik doğrulama | `FAL_KEY` (kanonik; `FAL_API_KEY` yedek olarak da çalışır)  
API | fal model uç noktaları  
  
## Başlarken

* ### API anahtarını ayarlayın

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Varsayılan bir görüntü modeli ayarlayın

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Görüntü üretimi

Yerleşik `fal` görüntü üretimi sağlayıcısının varsayılanı `fal/fal-ai/flux/dev` olur.

Yetenek | Değer  
---|---  
Maksimum görüntü | İstek başına 4  
Düzenleme modu | Flux: 1 referans görüntü; GPT Image 2: 10; Nano Banana 2: 14  
Boyut geçersiz kılmaları | Desteklenir  
En boy oranı | Üretme ve GPT Image 2/Nano Banana 2 düzenleme için desteklenir  
Çözünürlük | Desteklenir  
Çıktı biçimi | `png` veya `jpeg`  
  
PNG çıktısı istediğinizde `outputFormat: "png"` kullanın. fal, OpenClaw içinde açık bir saydam arka plan denetimi bildirmez; bu nedenle `background: "transparent"` fal modelleri için yok sayılan bir geçersiz kılma olarak raporlanır.

fal'i varsayılan görüntü sağlayıcısı olarak kullanmak için:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Video üretimi

Yerleşik `fal` video üretimi sağlayıcısının varsayılanı `fal/fal-ai/minimax/video-01-live` olur.

Yetenek | Değer  
---|---  
Modlar | Metinden videoya, tek görüntü referansı, Seedance referanstan videoya  
Çalışma zamanı | Uzun süren işler için kuyruk destekli gönderme/durum/sonuç akışı  
  
Kullanılabilir video modelleri

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 yapılandırma örneği json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 referanstan videoya yapılandırma örneği json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Referanstan videoya, paylaşılan `video_generate` `images`, `videos` ve `audioRefs` parametreleri aracılığıyla en fazla 9 görüntü, 3 video ve 3 ses referansı kabul eder; toplamda en fazla 12 referans dosyası olabilir.

HeyGen video-agent yapılandırma örneği json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## İlgili

[**Görüntü üretimi** Paylaşılan görüntü aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/image-generation>) [**Video üretimi** Paylaşılan video aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/video-generation>) [**Yapılandırma başvurusu** Görüntü ve video modeli seçimi dahil aracı varsayılanları. ](</tr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo