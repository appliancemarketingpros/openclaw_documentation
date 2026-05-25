---
title: Inworld
source_url: https://docs.openclaw.ai/tr/providers/inworld
scraped_at: 2026-05-25
---

Inworld, akışlı metinden sese dönüştürme (TTS) sağlayıcısıdır. OpenClaw içinde giden yanıt sesini (varsayılan olarak MP3, sesli notlar için OGG_OPUS) ve Voice Call gibi telefon kanalları için PCM sesini sentezler.

OpenClaw, Inworld'ün akışlı TTS uç noktasına gönderi yapar, döndürülen base64 ses parçalarını tek bir arabellekte birleştirir ve sonucu standart yanıt-ses işlem hattına verir.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `inworld`  
Plugin | paketle birlikte gelir, `enabledByDefault: true`  
Sözleşme | `speechProviders` (yalnızca TTS)  
Kimlik doğrulama ortam değişkeni | `INWORLD_API_KEY` (HTTP Basic, Base64 kontrol paneli kimlik bilgisi)  
Temel URL | `https://api.inworld.ai`  
Varsayılan ses | `Sarah`  
Varsayılan model | `inworld-tts-1.5-max`  
Çıkış | MP3 (varsayılan), OGG_OPUS (sesli notlar), PCM 22050 Hz (telefon)  
Web sitesi | [inworld.ai](<https://inworld.ai>)  
Belgeler | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Başlarken

* ### API anahtarınızı ayarlayın

Kimlik bilgisini Inworld kontrol panelinizden (Workspace > API Keys) kopyalayın ve bir ortam değişkeni olarak ayarlayın. Değer, HTTP Basic kimlik bilgisi olarak aynen gönderilir; bu nedenle yeniden Base64 ile kodlamayın veya bearer belirtecine dönüştürmeyin.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### messages.tts içinde Inworld'ü seçin

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Bir mesaj gönderin

Bağlı herhangi bir kanal üzerinden yanıt gönderin. OpenClaw sesi Inworld ile sentezler ve MP3 olarak (veya kanal sesli not beklediğinde OGG_OPUS olarak) iletir.

## Yapılandırma seçenekleri

Seçenek | Yol | Açıklama  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64 kontrol paneli kimlik bilgisi. `INWORLD_API_KEY` değerine geri döner.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Inworld API temel URL'sini geçersiz kılar (varsayılan `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Ses tanımlayıcısı (varsayılan `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS model kimliği (varsayılan `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Örnekleme sıcaklığı `0..2` (isteğe bağlı).  
  
## Notlar

Kimlik doğrulama

Inworld, tek bir Base64 kodlu kimlik bilgisi dizesiyle HTTP Basic kimlik doğrulaması kullanır. Bunu Inworld kontrol panelinden aynen kopyalayın. Sağlayıcı bunu başka bir kodlama yapmadan `Authorization: Basic <apiKey>` olarak gönderir; bu nedenle kendiniz Base64 ile kodlamayın ve bearer tarzı belirteç iletmeyin. Aynı vurgu için [TTS kimlik doğrulama notları](</tr/tools/tts#inworld-primary>) bölümüne bakın.

Modeller

Desteklenen model kimlikleri: `inworld-tts-1.5-max` (varsayılan), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Ses çıkışları

Yanıtlar varsayılan olarak MP3 kullanır. Kanal hedefi `voice-note` olduğunda OpenClaw, sesin yerel bir ses balonu olarak oynatılması için Inworld'den `OGG_OPUS` ister. Telefon sentezi, telefon köprüsünü beslemek için 22050 Hz'de ham `PCM` kullanır.

Özel uç noktalar

API ana makinesini `messages.tts.providers.inworld.baseUrl` ile geçersiz kılın. İstekler gönderilmeden önce sondaki eğik çizgiler kaldırılır.

## İlgili

[**Metinden sese dönüştürme** TTS genel bakışı, sağlayıcılar ve `messages.tts` yapılandırması. ](</tr/tools/tts>) [**Yapılandırma** `messages.tts` ayarları dahil tam yapılandırma başvurusu. ](</tr/gateway/configuration>) [**Sağlayıcılar** Paketle birlikte gelen tüm OpenClaw sağlayıcıları. ](</tr/providers>) [**Sorun giderme** Yaygın sorunlar ve hata ayıklama adımları. ](</tr/help/troubleshooting>)

Was this useful?YesNo