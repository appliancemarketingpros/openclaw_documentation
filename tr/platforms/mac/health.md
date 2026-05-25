---
title: Sağlık kontrolleri (macOS)
source_url: https://docs.openclaw.ai/tr/platforms/mac/health
scraped_at: 2026-05-25
---

# macOS üzerinde Sağlık Kontrolleri

Menü çubuğu uygulamasından bağlı kanalın sağlıklı olup olmadığını nasıl görebileceğiniz.

## Menü çubuğu

  * Durum noktası artık Baileys sağlığını yansıtır: 
    * Yeşil: bağlı + soket kısa süre önce açıldı.
    * Turuncu: bağlanıyor/yeniden deniyor.
    * Kırmızı: oturum kapatıldı veya yoklama başarısız oldu.
  * İkincil satır `"linked · auth 12m"` okur veya hata nedenini gösterir.
  * `"Run Health Check"` menü öğesi isteğe bağlı bir yoklama tetikler.


## Ayarlar

  * General sekmesi artık bağlı auth yaşı, oturum deposu yolu/sayısı, son denetim zamanı, son hata/durum kodu ve Run Health Check / Reveal Logs düğmelerini gösteren bir Health kartı içerir.
  * UI'nin anında yüklenmesi ve çevrimdışıyken sorunsuz şekilde geri dönmesi için önbelleğe alınmış anlık görüntü kullanır.
  * **Channels sekmesi** , WhatsApp/Telegram için kanal durumu + denetimleri gösterir (giriş QR, çıkış, yoklama, son kopma/hata).


## Yoklama nasıl çalışır

  * Uygulama, `ShellExecutor` üzerinden yaklaşık her 60 saniyede bir ve isteğe bağlı olarak `openclaw health --json` çalıştırır. Yoklama, mesaj göndermeden kimlik bilgilerini yükler ve durumu bildirir.
  * Titremeyi önlemek için son iyi anlık görüntü ile son hatayı ayrı ayrı önbelleğe alın; her birinin zaman damgasını gösterin.


## Emin değilseniz

  * [Gateway sağlığı](</tr/gateway/health>) içindeki CLI akışını yine de kullanabilirsiniz (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) ve `web-heartbeat` / `web-reconnect` için `/tmp/openclaw/openclaw-*.log` dosyasını izleyebilirsiniz.


## İlgili

  * [Gateway sağlığı](</tr/gateway/health>)
  * [macOS uygulaması](</tr/platforms/macos>)


Was this useful?YesNo