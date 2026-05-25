---
title: Konum komutu
source_url: https://docs.openclaw.ai/tr/nodes/location-command
scraped_at: 2026-05-25
---

## Kısaca

  * `location.get`, bir düğüm komutudur (`node.invoke` üzerinden).
  * Varsayılan olarak kapalıdır.
  * Android uygulama ayarları bir seçici kullanır: Kapalı / Kullanırken.
  * Ayrı anahtar: Hassas Konum.


## Neden seçici (sadece anahtar değil)

İşletim sistemi izinleri çok seviyelidir. Uygulama içinde bir seçici sunabiliriz, ancak gerçek izni yine işletim sistemi belirler.

  * iOS/macOS, sistem istemlerinde/Ayarlar'da **Kullanırken** veya **Her Zaman** seçeneklerini gösterebilir.
  * Android uygulaması şu anda yalnızca ön plan konumunu destekler.
  * Hassas konum ayrı bir izindir (iOS 14+ "Hassas", Android "fine" ve "coarse").


UI'daki seçici, istediğimiz modu yönlendirir; gerçek izin işletim sistemi ayarlarında tutulur.

## Ayarlar modeli

Düğüm cihazı başına:

  * `location.enabledMode`: `off | whileUsing`
  * `location.preciseEnabled`: bool


UI davranışı:

  * `whileUsing` seçildiğinde ön plan izni istenir.
  * İşletim sistemi istenen seviyeyi reddederse, izin verilen en yüksek seviyeye geri dön ve durumu göster.


## İzin eşlemesi (node.permissions)

İsteğe bağlıdır. macOS düğümü, izinler haritası üzerinden `location` bildirir; iOS/Android bunu atlayabilir.

## Komut: `location.get`

`node.invoke` üzerinden çağrılır.

Parametreler (önerilen):

jsonCopy code
[code]
    {  "timeoutMs": 10000,  "maxAgeMs": 15000,  "desiredAccuracy": "coarse|balanced|precise"}
[/code]

Yanıt yükü:

jsonCopy code
[code]
    {  "lat": 48.20849,  "lon": 16.37208,  "accuracyMeters": 12.5,  "altitudeMeters": 182.0,  "speedMps": 0.0,  "headingDeg": 270.0,  "timestamp": "2026-01-03T12:34:56.000Z",  "isPrecise": true,  "source": "gps|wifi|cell|unknown"}
[/code]

Hatalar (kararlı kodlar):

  * `LOCATION_DISABLED`: seçici kapalıdır.
  * `LOCATION_PERMISSION_REQUIRED`: istenen mod için izin eksik.
  * `LOCATION_BACKGROUND_UNAVAILABLE`: uygulama arka planda, ancak yalnızca Kullanırken izni verilmiş.
  * `LOCATION_TIMEOUT`: zamanında konum düzeltmesi alınamadı.
  * `LOCATION_UNAVAILABLE`: sistem hatası / sağlayıcı yok.


## Arka plan davranışı

  * Android uygulaması, arka plandayken `location.get` çağrısını reddeder.
  * Android'de konum isterken OpenClaw'ı açık tutun.
  * Diğer düğüm platformları farklı davranabilir.


## Model/araç entegrasyonu

  * Araç yüzeyi: `nodes` aracı `location_get` eylemini ekler (düğüm gerekli).
  * CLI: `openclaw nodes location get --node <id>`.
  * Ajan yönergeleri: yalnızca kullanıcı konumu etkinleştirdiğinde ve kapsamı anladığında çağırın.


## UX metni (önerilen)

  * Kapalı: "Konum paylaşımı devre dışı."
  * Kullanırken: "Yalnızca OpenClaw açıkken."
  * Hassas: "Hassas GPS konumunu kullan. Yaklaşık konumu paylaşmak için kapat."


## İlgili

  * [Kanal konumu ayrıştırma](</tr/channels/location>)
  * [Kamera yakalama](</tr/nodes/camera>)
  * [Konuşma modu](</tr/nodes/talk>)


Was this useful?YesNo