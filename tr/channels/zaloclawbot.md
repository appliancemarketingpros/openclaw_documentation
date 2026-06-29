---
title: Zalo ClawBot
source_url: https://docs.openclaw.ai/tr/channels/zaloclawbot
scraped_at: 2026-06-29
---

ChannelsRegional platforms

OpenClaw, katalogda listelenen harici `@zalo-platforms/openclaw-zaloclawbot` Plugin aracılığıyla Zalo ClawBot'a bağlanır. Oturum açma, Zalo Mini App QR kodu kullanır.

## Uyumluluk

Plugin Sürümü | OpenClaw Sürümü | npm dist-tag | Durum  
---|---|---|---  
0.1.x | >=2026.4.10 | `latest` | Etkin / Beta  
  
## Önkoşullar

  * Node.js **> = 22**
  * [OpenClaw](<https://docs.openclaw.ai/install>) yüklü olmalıdır (`openclaw` CLI kullanılabilir olmalıdır).
  * Oturum açma QR kodunu taramak için mobil cihazda bir Zalo hesabı.


## onboard ile yükleme (önerilir)

OpenClaw başlangıç sihirbazını çalıştırın ve kanal menüsünden **Zalo ClawBot** seçin:

bashCopy code
[code]
    openclaw onboard
[/code]

Sihirbaz, Plugin'i resmi katalogdan yükler (bütünlüğü doğrulanmış), oturum açma QR kodunu doğrudan terminalde oluşturur ve Zalo uygulamasıyla taradığınızda kanalı tamamlar. Ek komut gerekmez.

## Elle Kurulum

Kanalı zaten başlatılmış bir Gateway'e eklemek için şu adımları izleyin:

### 1\. Plugin'i yükleyin

bashCopy code
[code]
    openclaw plugins install "@zalo-platforms/openclaw-zaloclawbot@0.1.4"
[/code]

Yukarıda gösterilen sabitlenmiş tam sürümü kullanın (resmi katalog girdisiyle eşleşir); böylece OpenClaw, yükleme sırasında paketi katalog bütünlük karmasına göre doğrular.

### 2\. Yapılandırmada Plugin'i etkinleştirin

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-zaloclawbot.enabled true
[/code]

### 3\. QR kodu oluşturun ve oturum açın

bashCopy code
[code]
    openclaw channels login --channel openclaw-zaloclawbot
[/code]

Terminalde oluşturulan QR kodunu Zalo mobil uygulamasıyla tarayın, Zalo Mini App içindeki Kullanım Şartları'nı kabul edin ve oturumu yetkilendirin.

### 4\. Gateway'i yeniden başlatın

bashCopy code
[code]
    openclaw gateway restart
[/code]

* * *

## Nasıl Çalışır

Kendi Zalo Official Account (OA) hesabınızı kaydetmenizi ve statik geliştirici kimlik bilgilerini yapıştırmanızı gerektiren standart geliştirici Zalo kanalının aksine, Zalo ClawBot paylaşılan resmi altyapıyı kullanarak **sahibine bağlı kişisel asistan** olarak çalışır:

  1. **Güvenli Başlatma:** QR kodu, paylaşılan resmi bir OA altında yeni sağlanan özel bir botu doğrudan Zalo User ID'nize bağlayan güvenli bir Zalo Mini App'e yönlenir.
  2. **Sahibe Bağlı Gizlilik:** Tasarım gereği bot, _yalnızca_ sahibiyle iletişim kuracak şekilde kısıtlanmıştır. Diğer kullanıcılardan gelen mesajlar platform düzeyinde bırakılır; bu da bağlantıyı özel ve güvenli kılar.
  3. **Resmi API yolu:** Plugin, tarayıcı veya web oturumu otomasyonu yerine Zalo Bot Platform API'lerini kullanır.


## Arka Planda

Zalo ClawBot Plugin'i, kalıcı bir uzun yoklama mesaj döngüsü aracılığıyla Zalo API'leriyle iletişim kurar. Temiz ve hafif bir çalışma zamanı sağlamak için:

  * Uzun yoklama bağlantıları `getUpdates` uç noktasını kullanır.
  * Yerel masaüstü/terminal Gateway çalıştırmaları için Webhook'lar varsayılan olarak devre dışıdır.
  * Mesajlar istemci tarafında işlenir ve doğrudan yerel ajan çalışma zamanınıza eşlenir.


Harici Plugin, bot kimlik bilgilerini OpenClaw durum dizini altında yönetir. Bu dizini hassas kabul edin ve OpenClaw durumunuzun geri kalanıyla aynı erişim denetimi ve yedekleme politikasına dahil edin.

* * *

## Sorun Giderme

  * **QR ile Oturum Açma Zaman Aşımı:** Oturum açma belirteci (`zbsk`) güvenlik nedeniyle 5 dakika sonra sona erer. QR kodu taramadan önce sona ererse, yeni bir tane oluşturmak için oturum açma komutunu yeniden çalıştırmanız yeterlidir.
  * **Gateway Yüklenemiyor:** OpenClaw ana makine sürümünüzün `2026.4.10` veya daha yüksek olduğundan emin olun. Daha eski sürümler harici npm Plugin yükleme defterini desteklemez.


Was this useful?YesNo

Open issue