---
title: Hostinger
source_url: https://docs.openclaw.ai/tr/install/hostinger
scraped_at: 2026-05-25
---

[Hostinger](<https://www.hostinger.com/openclaw>) üzerinde **1-Click** yönetilen dağıtım veya **VPS** kurulumu ile kalıcı bir OpenClaw Gateway çalıştırın.

## Önkoşullar

  * Hostinger hesabı ([kayıt ol](<https://www.hostinger.com/openclaw>))
  * Yaklaşık 5-10 dakika


## Seçenek A: 1-Click OpenClaw

Başlamanın en hızlı yolu. Hostinger altyapıyı, Docker'ı ve otomatik güncellemeleri yönetir.

* ### Satın alın ve başlatın

  1. [Hostinger OpenClaw sayfasından](<https://www.hostinger.com/openclaw>) bir Managed OpenClaw planı seçin ve satın alma işlemini tamamlayın.


* ### Bir mesajlaşma kanalı seçin

Bağlamak için bir veya daha fazla kanal seçin:

  * **WhatsApp** \-- kurulum sihirbazında gösterilen QR kodunu tarayın.
  * **Telegram** \-- [BotFather](<https://t.me/BotFather>) üzerinden aldığınız bot belirtecini yapıştırın.


* ### Kurulumu tamamlayın

Örneği dağıtmak için **Finish** düğmesine tıklayın. Hazır olduğunda hPanel içindeki **OpenClaw Overview** üzerinden OpenClaw panosuna erişin.

## Seçenek B: VPS üzerinde OpenClaw

Sunucunuz üzerinde daha fazla denetim sağlar. Hostinger, VPS'inize Docker üzerinden OpenClaw dağıtır ve siz bunu hPanel içindeki **Docker Manager** üzerinden yönetirsiniz.

* ### Bir VPS satın alın

  1. [Hostinger OpenClaw sayfasından](<https://www.hostinger.com/openclaw>) bir OpenClaw on VPS planı seçin ve satın alma işlemini tamamlayın.


* ### OpenClaw'ı yapılandırın

VPS hazırlandığında yapılandırma alanlarını doldurun:

  * **Gateway token** \-- otomatik oluşturulur; daha sonra kullanmak için kaydedin.
  * **WhatsApp number** \-- ülke koduyla birlikte numaranız (isteğe bağlı).
  * **Telegram bot token** \-- [BotFather](<https://t.me/BotFather>) üzerinden (isteğe bağlı).
  * **API keys** \-- yalnızca satın alma sırasında Ready-to-Use AI kredilerini seçmediyseniz gerekir.


* ### OpenClaw'ı başlatın

**Deploy** düğmesine tıklayın. Çalışmaya başladıktan sonra hPanel içinden **Open** düğmesine tıklayarak OpenClaw panosunu açın.

Günlükler, yeniden başlatmalar ve güncellemeler doğrudan hPanel içindeki Docker Manager arayüzünden yönetilir. Güncellemek için Docker Manager içindeki **Update** düğmesine basın; bu en son imajı çekecektir.

## Kurulumunuzu doğrulayın

Bağladığınız kanalda asistanınıza "Hi" gönderin. OpenClaw yanıt verir ve sizi ilk tercihlerin ayarlanması konusunda yönlendirir.

## Sorun giderme

**Pano yüklenmiyor** \-- Kapsayıcının hazırlanmasını tamamlaması için birkaç dakika bekleyin. hPanel içindeki Docker Manager günlüklerini kontrol edin.

**Docker kapsayıcısı sürekli yeniden başlıyor** \-- Docker Manager günlüklerini açın ve yapılandırma hatalarını arayın (eksik belirteçler, geçersiz API anahtarları).

**Telegram botu yanıt vermiyor** \-- Bağlantıyı tamamlamak için eşleştirme kodu mesajınızı Telegram'dan doğrudan OpenClaw sohbetinizin içine mesaj olarak gönderin.

## Sonraki adımlar

  * [Kanallar](</tr/channels>) \-- Telegram, WhatsApp, Discord ve daha fazlasını bağlayın
  * [Gateway yapılandırması](</tr/gateway/configuration>) \-- tüm yapılandırma seçenekleri


## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [VPS barındırma](</tr/vps>)
  * [DigitalOcean](</tr/install/digitalocean>)


Was this useful?YesNo