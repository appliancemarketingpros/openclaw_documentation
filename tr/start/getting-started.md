---
title: Başlarken
source_url: https://docs.openclaw.ai/tr/start/getting-started
scraped_at: 2026-05-25
---

OpenClaw'ı kurun, ilk kurulum sihirbazını çalıştırın ve AI asistanınızla sohbet edin — tümü yaklaşık 5 dakika içinde. Sonunda çalışan bir Gateway'e, yapılandırılmış kimlik doğrulamaya ve çalışan bir sohbet oturumuna sahip olacaksınız.

## Gerekenler

  * **Node.js** — Node 24 önerilir (Node 22.16+ da desteklenir)
  * Bir model sağlayıcısından **API anahtarı** (Anthropic, OpenAI, Google vb.) — ilk kurulum sihirbazı sizden isteyecek


## Hızlı kurulum

* ### OpenClaw'ı kur

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Kurulum Betiği Süreci](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### İlk kurulum sihirbazını çalıştır

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Sihirbaz, bir model sağlayıcısı seçme, API anahtarı ayarlama ve Gateway'i yapılandırma adımlarında size rehberlik eder. Yaklaşık 2 dakika sürer.

Tam başvuru için bkz. [İlk kurulum (CLI)](</tr/start/wizard>).

* ### Gateway'in çalıştığını doğrula

bashCopy code
[code]
    openclaw gateway status
[/code]

Gateway'in 18789 numaralı bağlantı noktasını dinlediğini görmelisiniz.

* ### Panoyu aç

bashCopy code
[code]
    openclaw dashboard
[/code]

Bu, Control UI'ı tarayıcınızda açar. Yüklenirse her şey çalışıyor demektir.

* ### İlk mesajınızı gönderin

Control UI sohbetine bir mesaj yazın; bir AI yanıtı almalısınız.

Bunun yerine telefonunuzdan mı sohbet etmek istiyorsunuz? Kurulumu en hızlı kanal [Telegram](</tr/channels/telegram>)'dır (yalnızca bir bot token'ı). Tüm seçenekler için bkz. [Kanallar](</tr/channels>).

Gelişmiş: özel bir Control UI derlemesi bağlayın

Yerelleştirilmiş veya özelleştirilmiş bir pano derlemesini yönetiyorsanız, `gateway.controlUi.root` değerini derlenmiş statik varlıklarınızı ve `index.html` dosyasını içeren bir dizine yönlendirin.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Derlenmiş statik dosyalarınızı bu dizine kopyalayın.
[/code]

Ardından şunu ayarlayın:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Gateway'i yeniden başlatın ve panoyu yeniden açın:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Sırada ne var

[**Bir kanala bağlan** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo ve daha fazlası. ](</tr/channels>) [**Eşleştirme ve güvenlik** Agent'ınıza kimlerin mesaj gönderebileceğini kontrol edin. ](</tr/channels/pairing>) [**Gateway'i yapılandır** Modeller, araçlar, sandbox ve gelişmiş ayarlar. ](</tr/gateway/configuration>) [**Araçlara göz at** Tarayıcı, exec, web araması, Skills ve Plugin'ler. ](</tr/tools>)

Gelişmiş: ortam değişkenleri

OpenClaw'ı bir hizmet hesabı olarak çalıştırıyorsanız veya özel yollar istiyorsanız:

  * `OPENCLAW_HOME` — dahili yol çözümlemesi için ana dizin
  * `OPENCLAW_STATE_DIR` — durum dizinini geçersiz kıl
  * `OPENCLAW_CONFIG_PATH` — yapılandırma dosyası yolunu geçersiz kıl


Tam başvuru: [Ortam değişkenleri](</tr/help/environment>).

## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [Kanallar genel bakışı](</tr/channels>)
  * [Kurulum](</tr/start/setup>)


Was this useful?YesNo