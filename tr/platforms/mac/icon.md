---
title: Menü çubuğu simgesi
source_url: https://docs.openclaw.ai/tr/platforms/mac/icon
scraped_at: 2026-05-25
---

# Menü Çubuğu Simgesi Durumları

Yazar: steipete · Güncellendi: 2025-12-06 · Kapsam: macOS uygulaması (`apps/macos`)

  * **Boşta:** Normal simge animasyonu (göz kırpma, ara sıra hafif sallanma).
  * **Duraklatıldı:** Durum öğesi `appearsDisabled` kullanır; hareket yoktur.
  * **Ses tetikleyicisi (büyük kulaklar):** Sesle uyandırma algılayıcısı, uyandırma sözcüğü duyulduğunda `AppState.triggerVoiceEars(ttl: nil)` çağırır ve ifade yakalanırken `earBoostActive=true` değerini korur. Kulaklar büyür (1.9x), okunabilirlik için dairesel kulak delikleri alır, ardından 1 sn sessizlikten sonra `stopVoiceEars()` ile geri iner. Yalnızca uygulama içi ses işlem hattından tetiklenir.
  * **Çalışıyor (agent çalışıyor):** `AppState.isWorking=true`, "kuyruk/bacak koşturması" mikro hareketini çalıştırır: iş devam ederken daha hızlı bacak sallanması ve hafif kayma. Şu anda WebChat agent çalıştırmaları sırasında açılıp kapatılır; bunları bağladığınızda diğer uzun görevlerin etrafına da aynı açma/kapatmayı ekleyin.


Bağlantı noktaları

  * Sesle uyandırma: runtime/tester, yakalama penceresiyle eşleşmesi için tetikleme sırasında `AppState.triggerVoiceEars(ttl: nil)` ve 1 sn sessizlikten sonra `stopVoiceEars()` çağırır.
  * Agent etkinliği: iş aralıkları sırasında `AppStateStore.shared.setWorking(true/false)` ayarlayın (WebChat agent çağrısında zaten yapılıyor). Takılı kalan animasyonları önlemek için aralıkları kısa tutun ve `defer` bloklarında sıfırlayın.


Şekiller ve boyutlar

  * Temel simge `CritterIconRenderer.makeIcon(blink:legWiggle:earWiggle:earScale:earHoles:)` içinde çizilir.
  * Kulak ölçeği varsayılan olarak `1.0` olur; ses güçlendirmesi genel çerçeveyi değiştirmeden `earScale=1.9` ayarlar ve `earHoles=true` açar (36×36 px Retina arka depoya işlenen 18×18 pt şablon görüntü).
  * Koşturma, küçük bir yatay titremeyle birlikte bacak sallanmasını yaklaşık ~1.0 değerine kadar kullanır; mevcut boşta sallanmasına eklenir.


Davranış notları

  * Kulaklar/çalışma için harici CLI/broker açma kapaması yoktur; yanlışlıkla dalgalanmayı önlemek için bunu uygulamanın kendi sinyallerine dahili tutun.
  * TTL'leri kısa tutun (<10 sn), böylece bir iş takılırsa simge hızla başlangıç durumuna döner.


## İlgili

  * [Menü çubuğu](</tr/platforms/mac/menu-bar>)
  * [macOS uygulaması](</tr/platforms/macos>)


Was this useful?YesNo