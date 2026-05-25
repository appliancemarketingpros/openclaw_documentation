---
title: İlk kurulum (macOS uygulaması)
source_url: https://docs.openclaw.ai/tr/start/onboarding
scraped_at: 2026-05-25
---

Bu belge **mevcut** ilk çalıştırma kurulum akışını açıklar. Amaç, sorunsuz bir "0. gün" deneyimidir: Gateway'in nerede çalışacağını seçmek, kimlik doğrulamayı bağlamak, sihirbazı çalıştırmak ve ajanın kendini başlatmasına izin vermek. Katılım yollarına genel bir bakış için bkz. [Katılım Genel Bakışı](</tr/start/onboarding-overview>).

* ### macOS uyarısını onaylayın

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Yerel ağları bulmayı onaylayın

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Karşılama ve güvenlik bildirimi

Gösterilen güvenlik bildirimini okuyun ve buna göre karar verin ![](/assets/macos-onboarding/03-security-notice.png)

Güvenlik güven modeli:

  * Varsayılan olarak OpenClaw kişisel bir ajandır: tek bir güvenilir operatör sınırı.
  * Paylaşılan/çok kullanıcılı kurulumlar sıkılaştırma gerektirir (güven sınırlarını ayırın, araç erişimini minimumda tutun ve [Güvenlik](</tr/gateway/security>) yönergelerini izleyin).
  * Yerel katılım artık yeni yapılandırmalarda varsayılan olarak `tools.profile: "coding"` kullanır; böylece yeni yerel kurulumlar, sınırsız `full` profilini zorunlu kılmadan dosya sistemi/çalışma zamanı araçlarını korur.
  * Hook/webhook'lar veya diğer güvenilmeyen içerik beslemeleri etkinse, güçlü ve modern bir model katmanı kullanın ve sıkı araç politikası/korumalı alan uygulayın.


* ### Yerel ve Uzak

![](/assets/macos-onboarding/04-choose-gateway.png)

**Gateway** nerede çalışır?

  * **Bu Mac (Yalnızca yerel):** katılım, kimlik doğrulamayı yapılandırabilir ve kimlik bilgilerini yerel olarak yazabilir.
  * **Uzak (SSH/Tailnet üzerinden):** katılım yerel kimlik doğrulamayı yapılandırmaz; kimlik bilgilerinin gateway ana makinesinde mevcut olması gerekir.
  * **Daha sonra yapılandır:** kurulumu atlayın ve uygulamayı yapılandırılmamış bırakın.


* ### İzinler

OpenClaw'a hangi izinleri vermek istediğinizi seçin ![](/assets/macos-onboarding/05-permissions.png)

Katılım, şunlar için gereken TCC izinlerini ister:

  * Otomasyon (AppleScript)
  * Bildirimler
  * Erişilebilirlik
  * Ekran Kaydı
  * Mikrofon
  * Konuşma Tanıma
  * Kamera
  * Konum


* ### CLI

* ### Katılım Sohbeti (adanmış oturum)

Kurulumdan sonra uygulama, ajanın kendini tanıtabilmesi ve sonraki adımlara rehberlik edebilmesi için adanmış bir katılım sohbet oturumu açar. Bu, ilk çalıştırma rehberliğini normal konuşmanızdan ayrı tutar. İlk ajan çalıştırması sırasında gateway ana makinesinde neler olduğunu öğrenmek için bkz. [Başlatma](</tr/start/bootstrapping>).

## İlgili

  * [Katılım genel bakışı](</tr/start/onboarding-overview>)
  * [Başlarken](</tr/start/getting-started>)


Was this useful?YesNo