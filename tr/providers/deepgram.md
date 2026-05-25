---
title: Deepgram
source_url: https://docs.openclaw.ai/tr/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram bir konuşmadan metne API'sidir. OpenClaw içinde, `tools.media.audio` aracılığıyla gelen ses/sesli not transkripsiyonu için ve Voice Call akış STT'si için `plugins.entries.voice-call.config.streaming` üzerinden kullanılır.

Toplu transkripsiyon için OpenClaw, tam ses dosyasını Deepgram'a yükler ve transkripti yanıt işlem hattına enjekte eder (`{{Transcript}}` \+ `[Audio]` bloğu). Voice Call akışı için OpenClaw, canlı G.711 u-law karelerini Deepgram'ın WebSocket `listen` uç noktasına iletir ve Deepgram bunları döndürdükçe kısmi veya nihai transkriptler üretir.

Ayrıntı | Değer  
---|---  
Web sitesi | [deepgram.com](<https://deepgram.com>)  
Belgeler | [developers.deepgram.com](<https://developers.deepgram.com>)  
Kimlik doğrulama | `DEEPGRAM_API_KEY`  
Varsayılan model | `nova-3`  
  
## Başlangıç

* ### API anahtarınızı ayarlayın

Deepgram API anahtarınızı ortama ekleyin:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Ses sağlayıcısını etkinleştirin

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Bir sesli not gönderin

Bağlı herhangi bir kanal üzerinden bir ses mesajı gönderin. OpenClaw bunu Deepgram aracılığıyla transkribe eder ve transkripti yanıt işlem hattına enjekte eder.

## Yapılandırma seçenekleri

Seçenek | Yol | Açıklama  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram model kimliği (varsayılan: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Dil ipucu (isteğe bağlı)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Dil algılamayı etkinleştirir (isteğe bağlı)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Noktalama işaretlerini etkinleştirir (isteğe bağlı)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Akıllı biçimlendirmeyi etkinleştirir (isteğe bağlı)  
  
### Dil ipucuyla

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Deepgram seçenekleriyle

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call akış STT'si

Paketlenmiş `deepgram` Plugin'i, Voice Call Plugin'i için bir gerçek zamanlı transkripsiyon sağlayıcısı da kaydeder.

Ayar | Yapılandırma yolu | Varsayılan  
---|---|---  
API anahtarı | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | `DEEPGRAM_API_KEY` değerine geri döner  
Model | `...deepgram.model` | `nova-3`  
Dil | `...deepgram.language` | (ayarlanmamış)  
Kodlama | `...deepgram.encoding` | `mulaw`  
Örnekleme oranı | `...deepgram.sampleRate` | `8000`  
Uç noktalama | `...deepgram.endpointingMs` | `800`  
Ara sonuçlar | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Notlar

Kimlik doğrulama

Kimlik doğrulama standart sağlayıcı kimlik doğrulama sırasını izler. `DEEPGRAM_API_KEY` en basit yoldur.

Proxy ve özel uç noktalar

Bir proxy kullanırken uç noktaları veya üst bilgileri `tools.media.audio.baseUrl` ve `tools.media.audio.headers` ile geçersiz kılın.

Çıktı davranışı

Çıktı, diğer sağlayıcılarla aynı ses kurallarını izler (boyut sınırları, zaman aşımları, transkript enjeksiyonu).

## İlgili

[**Medya araçları** Ses, görüntü ve video işleme işlem hattına genel bakış. ](</tr/tools/media-overview>) [**Yapılandırma** Medya aracı ayarları dahil tam yapılandırma başvurusu. ](</tr/gateway/configuration>) [**Sorun giderme** Yaygın sorunlar ve hata ayıklama adımları. ](</tr/help/troubleshooting>) [**SSS** OpenClaw kurulumu hakkında sık sorulan sorular. ](</tr/help/faq>)

Was this useful?YesNo