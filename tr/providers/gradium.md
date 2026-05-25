---
title: Gradium
source_url: https://docs.openclaw.ai/tr/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>), OpenClaw için paketle birlikte gelen bir metinden sese sağlayıcısıdır. Plugin normal sesli yanıtları (WAV), sesli not uyumlu Opus çıktısını ve telefon yüzeyleri için 8 kHz u-law sesi oluşturabilir.

Özellik | Değer  
---|---  
Sağlayıcı id | `gradium`  
Kimlik doğrulama | `GRADIUM_API_KEY` veya config `apiKey`  
Temel URL | `https://api.gradium.ai` (varsayılan)  
Varsayılan ses | `Emma` (`YTpq7expH9539ERJ`)  
  
## Kurulum

Bir Gradium API anahtarı oluşturun, ardından bunu bir ortam değişkeni veya config anahtarıyla OpenClaw'a sunun.

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Config key

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin önce çözümlenen `apiKey` değerini denetler ve ardından `GRADIUM_API_KEY` ortam değişkenine geri döner.

## Config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Anahtar | Tür | Açıklama  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Çözümlenen API anahtarı. `${ENV}` ve gizli referansları destekler.  
`messages.tts.providers.gradium.baseUrl` | string | API kökenini geçersiz kılar. Sondaki eğik çizgiler kaldırılır. Varsayılan değer `https://api.gradium.ai` olur.  
`messages.tts.providers.gradium.voiceId` | string | Yönerge geçersiz kılması bulunmadığında kullanılan varsayılan ses id'si.  
  
Çıkış ses biçimi, hedef yüzeye göre çalışma zamanı tarafından otomatik olarak seçilir ve `openclaw.json` üzerinden yapılandırılamaz. Aşağıdaki Çıktı bölümüne bakın.

## Sesler

Ad | Ses ID'si  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Varsayılan ses: Emma.

### İleti başına ses geçersiz kılması

Etkin konuşma ilkesi ses geçersiz kılmalarına izin verdiğinde, bir yönerge belirteci kullanarak satır içinde sesleri değiştirebilirsiniz. Bunların tümü aynı `voiceId` geçersiz kılmasına çözümlenir:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Konuşma ilkesi ses geçersiz kılmalarını devre dışı bırakırsa yönerge tüketilir, ancak yok sayılır.

## Çıktı

Çalışma zamanı çıkış biçimini hedef yüzeyden seçer. Sağlayıcı bugün başka biçimler sentezlemez.

Hedef | Biçim | Dosya uzantısı | Örnekleme hızı | Ses uyumluluğu bayrağı  
---|---|---|---|---  
Standart ses | `wav` | `.wav` | sağlayıcı | hayır  
Sesli not | `opus` | `.opus` | sağlayıcı | evet  
Telefon | `ulaw_8000` | yok | 8 kHz | yok  
  
## Otomatik seçim sırası

Yapılandırılmış TTS sağlayıcıları arasında Gradium'un otomatik seçim sırası `30` değeridir. `messages.tts.provider` sabitlenmediğinde OpenClaw'ın etkin sağlayıcıyı nasıl seçtiği için [Metinden Sese](</tr/tools/tts>) bölümüne bakın.

## İlgili

  * [Metinden Sese](</tr/tools/tts>)
  * [Medya Genel Bakışı](</tr/tools/media-overview>)


Was this useful?YesNo