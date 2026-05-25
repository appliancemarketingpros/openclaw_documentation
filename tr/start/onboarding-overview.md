---
title: Başlangıç sürecine genel bakış
source_url: https://docs.openclaw.ai/tr/start/onboarding-overview
scraped_at: 2026-05-25
---

OpenClaw'ın iki ilk kurulum yolu vardır. İkisi de kimlik doğrulamayı, Gateway'i ve isteğe bağlı sohbet kanallarını yapılandırır; yalnızca kurulumla nasıl etkileşim kurduğunuz farklıdır.

## Hangi yolu kullanmalıyım?

| CLI ilk kurulumu | macOS uygulaması ilk kurulumu  
---|---|---  
**Platformlar** | macOS, Linux, Windows (yerel veya WSL2) | Yalnızca macOS  
**Arayüz** | Terminal sihirbazı | Uygulamada rehberli kullanıcı arayüzü  
**En uygun** | Sunucular, başsız kullanım, tam kontrol | Masaüstü Mac, görsel kurulum  
**Otomasyon** | Betikler için `--non-interactive` | Yalnızca manuel  
**Komut** | `openclaw onboard` | Uygulamayı başlatın  
  
Çoğu kullanıcı **CLI ilk kurulumu** ile başlamalıdır; her yerde çalışır ve size en fazla kontrolü sağlar.

## İlk kurulumun yapılandırdıkları

Hangi yolu seçerseniz seçin, ilk kurulum şunları ayarlar:

  1. **Model sağlayıcısı ve kimlik doğrulama** — seçtiğiniz sağlayıcı için API anahtarı, OAuth veya kurulum belirteci
  2. **Çalışma alanı** — agent dosyaları, bootstrap şablonları ve bellek için dizin
  3. **Gateway** — bağlantı noktası, bağlanma adresi, kimlik doğrulama modu
  4. **Kanallar** (isteğe bağlı) — iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, Telegram, WhatsApp ve daha fazlası gibi yerleşik ve paketlenmiş sohbet kanalları
  5. **Daemon** (isteğe bağlı) — Gateway'in otomatik olarak başlaması için arka plan hizmeti


## CLI ilk kurulumu

Herhangi bir terminalde çalıştırın:

bashCopy code
[code]
    openclaw onboard
[/code]

Arka plan hizmetini de tek adımda yüklemek için `--install-daemon` ekleyin.

Tam başvuru: [İlk kurulum (CLI)](</tr/start/wizard>) CLI komut belgeleri: [`openclaw onboard`](</tr/cli/onboard>)

## macOS uygulaması ilk kurulumu

OpenClaw uygulamasını açın. İlk çalıştırma sihirbazı, aynı adımlarda size görsel bir arayüzle yol gösterir.

Tam başvuru: [İlk kurulum (macOS Uygulaması)](</tr/start/onboarding>)

## Özel veya listelenmeyen sağlayıcılar

Sağlayıcınız ilk kurulumda listelenmiyorsa **Özel Sağlayıcı** seçeneğini belirleyin ve şunları girin:

  * API uyumluluk modu (OpenAI uyumlu, Anthropic uyumlu veya otomatik algılama)
  * Temel URL ve API anahtarı
  * Model kimliği ve isteğe bağlı takma ad


Birden çok özel uç nokta birlikte var olabilir; her biri kendi uç nokta kimliğini alır.

## İlgili

  * [Başlarken](</tr/start/getting-started>)
  * [CLI kurulum başvurusu](</tr/start/wizard-cli-reference>)


Was this useful?YesNo