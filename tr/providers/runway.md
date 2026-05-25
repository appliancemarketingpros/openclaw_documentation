---
title: Runway
source_url: https://docs.openclaw.ai/tr/providers/runway
scraped_at: 2026-05-25
---

OpenClaw, barındırılan video oluşturma için paketle birlikte gelen bir `runway` sağlayıcısıyla gelir. Plugin varsayılan olarak etkindir ve `videoGenerationProviders` sözleşmesine karşı `runway` sağlayıcısını kaydeder.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `runway`  
Plugin | paketle birlikte gelir, `enabledByDefault: true`  
Kimlik doğrulama env değişkenleri | `RUNWAYML_API_SECRET` (kanonik) veya `RUNWAY_API_KEY`  
İlk kurulum bayrağı | `--auth-choice runway-api-key`  
Doğrudan CLI bayrağı | `--runway-api-key <key>`  
API | Runway görev tabanlı video oluşturma (`GET /v1/tasks/{id}` yoklaması)  
Varsayılan model | `runway/gen4.5`  
  
## Başlarken

* ### API anahtarını ayarlayın

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Runway’i varsayılan video sağlayıcısı olarak ayarlayın

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Video oluşturun

Ajanınızdan bir video oluşturmasını isteyin. Runway otomatik olarak kullanılacaktır.

## Desteklenen modlar ve modeller

Sağlayıcı, üç moda bölünmüş yedi Runway modelini kullanıma sunar. Aynı model kimliği birden fazla moda hizmet edebilir (örneğin `gen4.5` hem metinden videoya hem de görüntüden videoya için çalışır).

Mod | Modeller | Referans girdi  
---|---|---  
Metinden videoya | `gen4.5` (varsayılan), `veo3.1`, `veo3.1_fast`, `veo3` | Yok  
Görüntüden videoya | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 yerel veya uzak görüntü  
Videodan videoya | `gen4_aleph` | 1 yerel veya uzak video  
  
Yerel görüntü ve video referansları data URI’leri aracılığıyla desteklenir.

En boy oranları | İzin verilen değerler  
---|---  
Metinden videoya | `16:9`, `9:16`  
Görüntü ve video düzenlemeleri | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Yapılandırma

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Gelişmiş yapılandırma

Ortam değişkeni takma adları

OpenClaw hem `RUNWAYML_API_SECRET` (kanonik) hem de `RUNWAY_API_KEY` değerini tanır. Her iki değişken de Runway sağlayıcısının kimliğini doğrular.

Görev yoklaması

Runway görev tabanlı bir API kullanır. Bir oluşturma isteği gönderildikten sonra OpenClaw, video hazır olana kadar `GET /v1/tasks/{id}` yoklar. Yoklama davranışı için ek yapılandırma gerekmez.

## İlgili

[**Video oluşturma** Paylaşılan araç parametreleri, sağlayıcı seçimi ve zaman uyumsuz davranış. ](</tr/tools/video-generation>) [**Yapılandırma referansı** Video oluşturma modeli dahil ajan varsayılan ayarları. ](</tr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo