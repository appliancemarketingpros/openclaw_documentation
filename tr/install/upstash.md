---
title: Upstash Kutusu
source_url: https://docs.openclaw.ai/tr/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Upstash Box üzerinde, sürekli çalışır yaşam döngüsü desteğine sahip yönetilen bir Linux ortamında kalıcı bir OpenClaw Gateway çalıştırın.

Kontrol paneli erişimi için bir SSH tüneli kullanın. Gateway bağlantı noktasını doğrudan herkese açık internete açmayın.

## Önkoşullar

  * Upstash hesabı
  * Sürekli çalışır Upstash Box
  * Yerel makinenizde SSH istemcisi


## Bir Box oluşturun

Upstash Console içinde sürekli çalışır bir Box oluşturun. `right-flamingo-14486` gibi Box ID değerini ve Box API anahtarınızı not edin.

Upstash, güncel OpenClaw Box kurulum kılavuzunu [OpenClaw Kurulumu](<https://upstash.com/docs/box/guides/openclaw-setup>) sayfasında tutar.

## SSH tüneliyle bağlanın

OpenClaw kontrol paneli bağlantı noktasını yerel makinenize yönlendirin. İstendiğinde SSH parolası olarak Box API anahtarınızı kullanın:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Keepalive seçenekleri, onboarding sırasında boşta kalan tünel kopmalarını azaltır.

## OpenClaw'ı yükleyin

Box içinde:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

İstemleri izleyin. Onboarding tamamlandığında kontrol paneli URL'sini ve token'ı kopyalayın.

## Gateway'i başlatın

Gateway'i Box ağı için yapılandırın ve arka planda başlatın:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

SSH tüneli etkin durumdayken kontrol paneli URL'sini yerel olarak açın:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Otomatik yeniden başlatma

Gateway'in Box başlatıldığında yeniden başlaması için bu komutu Box init betiği olarak ayarlayın:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Sorun giderme

Onboarding sırasında SSH donarsa temiz bir SSH yapılandırması ve keepalive'larla yeniden bağlanın:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Bu, eskimiş yerel `~/.ssh/config` ayarlarını atlar ve boşta kalan ağ dönemlerinde tüneli etkin tutar.

## İlgili

  * [Uzaktan erişim](</tr/gateway/remote>)
  * [Gateway güvenliği](</tr/gateway/security>)
  * [OpenClaw'ı güncelleme](</tr/install/updating>)


Was this useful?YesNo

Open issue