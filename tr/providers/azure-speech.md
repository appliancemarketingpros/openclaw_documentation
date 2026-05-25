---
title: Azure Speech
source_url: https://docs.openclaw.ai/tr/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech, bir Azure AI Speech text-to-speech sağlayıcısıdır. OpenClaw içinde giden yanıt sesini varsayılan olarak MP3, sesli notlar için yerel Ogg/Opus ve Voice Call gibi telefon kanalları için 8 kHz mulaw ses olarak sentezler.

OpenClaw, Azure Speech REST API'sini doğrudan SSML ile kullanır ve sağlayıcı sahipli çıktı biçimini `X-Microsoft-OutputFormat` üzerinden gönderir.

Ayrıntı | Değer  
---|---  
Website | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Dokümanlar | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Kimlik doğrulama | `AZURE_SPEECH_KEY` artı `AZURE_SPEECH_REGION`  
Varsayılan ses | `en-US-JennyNeural`  
Varsayılan dosya çıktısı | `audio-24khz-48kbitrate-mono-mp3`  
Varsayılan sesli not dosyası | `ogg-24khz-16bit-mono-opus`  
  
## Başlarken

* ### Bir Azure Speech kaynağı oluşturun

Azure portalında bir Speech kaynağı oluşturun. Resource Management > Keys and Endpoint bölümünden **KEY 1** değerini kopyalayın ve `eastus` gibi kaynak konumunu da kopyalayın.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### messages.tts içinde Azure Speech'i seçin

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Bir mesaj gönderin

Bağlı herhangi bir kanal üzerinden bir yanıt gönderin. OpenClaw sesi Azure Speech ile sentezler ve standart ses için MP3, kanal sesli not beklediğinde ise Ogg/Opus teslim eder.

## Yapılandırma seçenekleri

Seçenek | Yol | Açıklama  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Azure Speech kaynak anahtarı. `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` veya `SPEECH_KEY` değerlerine fallback yapar.  
`region` | `messages.tts.providers.azure-speech.region` | Azure Speech kaynak bölgesi. `AZURE_SPEECH_REGION` veya `SPEECH_REGION` değerlerine fallback yapar.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | İsteğe bağlı Azure Speech uç noktası/base URL geçersiz kılması.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | İsteğe bağlı Azure Speech base URL geçersiz kılması.  
`voice` | `messages.tts.providers.azure-speech.voice` | Azure ses `ShortName` değeri (varsayılan `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | SSML dil kodu (varsayılan `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Ses dosyası çıktı biçimi (varsayılan `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Sesli not çıktı biçimi (varsayılan `ogg-24khz-16bit-mono-opus`).  
  
## Notlar

Kimlik doğrulama

Azure Speech, Azure OpenAI anahtarı değil, bir Speech kaynak anahtarı kullanır. Anahtar `Ocp-Apim-Subscription-Key` olarak gönderilir; OpenClaw, siz `endpoint` veya `baseUrl` sağlamadığınız sürece `region` değerinden `https://<region>.tts.speech.microsoft.com` türetir.

Ses adları

Azure Speech ses `ShortName` değerini kullanın; örneğin `en-US-JennyNeural`. Paketlenmiş sağlayıcı sesleri aynı Speech kaynağı üzerinden listeleyebilir ve kullanımdan kaldırılmış veya emekliye ayrılmış olarak işaretlenen sesleri filtreler.

Ses çıktıları

Azure; `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` ve `riff-24khz-16bit-mono-pcm` gibi çıktı biçimlerini kabul eder. OpenClaw, `voice-note` hedefleri için Ogg/Opus ister; böylece kanallar ekstra MP3 dönüştürmesi olmadan yerel ses baloncukları gönderebilir.

Takma ad

`azure`, mevcut PR'ler ve kullanıcı config'i için sağlayıcı takma adı olarak kabul edilir, ancak yeni config, Azure OpenAI model sağlayıcılarıyla karışıklığı önlemek için `azure-speech` kullanmalıdır.

## İlgili

[**Text-to-speech** TTS genel bakışı, sağlayıcılar ve `messages.tts` config'i. ](</tr/tools/tts>) [**Yapılandırma** `messages.tts` ayarları dahil tam config referansı. ](</tr/gateway/configuration>) [**Sağlayıcılar** Tüm paketlenmiş OpenClaw sağlayıcıları. ](</tr/providers>) [**Sorun giderme** Yaygın sorunlar ve hata ayıklama adımları. ](</tr/help/troubleshooting>)

Was this useful?YesNo