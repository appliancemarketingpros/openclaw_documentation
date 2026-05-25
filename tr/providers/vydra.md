---
title: Vydra
source_url: https://docs.openclaw.ai/tr/providers/vydra
scraped_at: 2026-05-25
---

Paketle birlikte gelen Vydra Plugin'i şunları ekler:

  * `vydra/grok-imagine` ile görüntü oluşturma
  * `vydra/veo3` ve `vydra/kling` ile video oluşturma
  * Vydra'nın ElevenLabs destekli TTS rotası ile konuşma sentezi


OpenClaw, üç yeteneğin tamamı için aynı `VYDRA_API_KEY` değerini kullanır.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `vydra`  
Plugin | paketle birlikte gelir, `enabledByDefault: true`  
Kimlik doğrulama env var | `VYDRA_API_KEY`  
İlk kurulum bayrağı | `--auth-choice vydra-api-key`  
Doğrudan CLI bayrağı | `--vydra-api-key <key>`  
Sözleşmeler | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Temel URL | `https://www.vydra.ai/api/v1` (`www` ana makinesini kullanın)  
  
## Kurulum

* ### Etkileşimli ilk kurulumu çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Ya da env var değerini doğrudan ayarlayın:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Varsayılan yetenek seçin

Aşağıdaki yeteneklerden birini veya daha fazlasını seçin (görüntü, video ya da konuşma) ve eşleşen yapılandırmayı uygulayın.

## Yetenekler

Görüntü oluşturma

Varsayılan görüntü modeli:

  * `vydra/grok-imagine`


Bunu varsayılan görüntü sağlayıcısı olarak ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Mevcut paketli destek yalnızca metinden görüntüyedir. Vydra'nın barındırılan düzenleme rotaları uzak görüntü URL'leri bekler ve OpenClaw, paketle birlikte gelen Plugin'de henüz Vydra'ya özgü bir yükleme köprüsü eklemez.

Video oluşturma

Kayıtlı video modelleri:

  * metinden videoya için `vydra/veo3`
  * görüntüden videoya için `vydra/kling`


Vydra'yı varsayılan video sağlayıcısı olarak ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Notlar:

  * `vydra/veo3`, yalnızca metinden videoya olarak paketlenmiştir.
  * `vydra/kling` şu anda uzak bir görüntü URL referansı gerektirir. Yerel dosya yüklemeleri baştan reddedilir.
  * Vydra'nın mevcut `kling` HTTP rotası, `image_url` mı yoksa `video_url` mı gerektirdiği konusunda tutarsız olmuştur; paketle birlikte gelen sağlayıcı aynı uzak görüntü URL'sini iki alana da eşler.
  * Paketle birlikte gelen Plugin, temkinli kalır ve en boy oranı, çözünürlük, filigran veya oluşturulan ses gibi belgelenmemiş stil ayarlarını iletmez.

Video canlı testleri

Sağlayıcıya özgü canlı kapsam:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Paketle birlikte gelen Vydra canlı dosyası artık şunları kapsar:

  * `vydra/veo3` metinden videoya
  * uzak görüntü URL'si kullanan `vydra/kling` görüntüden videoya


Gerektiğinde uzak görüntü fixture'ını geçersiz kılın:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Konuşma sentezi

Vydra'yı konuşma sağlayıcısı olarak ayarlayın:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Varsayılanlar:

  * Model: `elevenlabs/tts`
  * Ses kimliği: `21m00Tcm4TlvDq8ikWAM`


Paketle birlikte gelen Plugin şu anda bilinen ve iyi çalışan tek bir varsayılan sesi sunar ve MP3 ses dosyaları döndürür.

## İlgili

[**Sağlayıcı dizini** Mevcut tüm sağlayıcılara göz atın. ](</tr/providers>) [**Görüntü oluşturma** Paylaşılan görüntü aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/image-generation>) [**Video oluşturma** Paylaşılan video aracı parametreleri ve sağlayıcı seçimi. ](</tr/tools/video-generation>) [**Yapılandırma referansı** Aracı varsayılanları ve model yapılandırması. ](</tr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo