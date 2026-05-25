---
title: Kanal konum ayrıştırma
source_url: https://docs.openclaw.ai/tr/channels/location
scraped_at: 2026-05-25
---

OpenClaw, sohbet kanallarından paylaşılan konumları şu biçimde normalize eder:

  * gelen gövdeye eklenen kısa koordinat metni ve
  * otomatik yanıt bağlam yükündeki yapılandırılmış alanlar. Kanal tarafından sağlanan etiketler, adresler ve başlıklar/yorumlar, kullanıcı gövdesinin içinde satır içi olarak değil, paylaşılan güvenilmeyen metadata JSON bloğu üzerinden isteme işlenir.


Şu anda desteklenenler:

  * **Telegram** (konum iğneleri + mekanlar + canlı konumlar)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`geo_uri` içeren `m.location`)


## Metin biçimlendirme

Konumlar, köşeli parantezler olmadan anlaşılır satırlar olarak işlenir:

  * İğne: 
    * `📍 48.858844, 2.294351 ±12m`
  * Adlandırılmış yer: 
    * `📍 48.858844, 2.294351 ±12m`
  * Canlı paylaşım: 
    * `🛰 Canlı konum: 48.858844, 2.294351 ±12m`


Kanal bir etiket, adres veya başlık/yorum içeriyorsa, bu bağlam yükünde korunur ve istemde çevrili güvenilmeyen JSON olarak görünür:

textCopy code
[code]
    Konum (güvenilmeyen metadata):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## Bağlam alanları

Bir konum mevcut olduğunda bu alanlar `ctx` içine eklenir:

  * `LocationLat` (sayı)
  * `LocationLon` (sayı)
  * `LocationAccuracy` (sayı, metre; isteğe bağlı)
  * `LocationName` (dize; isteğe bağlı)
  * `LocationAddress` (dize; isteğe bağlı)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (boolean)
  * `LocationCaption` (dize; isteğe bağlı)


İstem işleyicisi `LocationName`, `LocationAddress` ve `LocationCaption` alanlarını güvenilmeyen metadata olarak değerlendirir ve bunları diğer kanal bağlamları için kullanılan aynı sınırlı JSON yolu üzerinden serileştirir.

## Kanal notları

  * **Telegram** : mekanlar `LocationName/LocationAddress` alanlarına eşlenir; canlı konumlar `live_period` kullanır.
  * **WhatsApp** : `locationMessage.comment` ve `liveLocationMessage.caption`, `LocationCaption` alanını doldurur.
  * **Matrix** : `geo_uri`, iğne konumu olarak ayrıştırılır; yükseklik yok sayılır ve `LocationIsLive` her zaman false olur.


## İlgili

  * [Konum komutu (Node'lar)](</tr/nodes/location-command>)
  * [Kamera yakalama](</tr/nodes/camera>)
  * [Medya anlama](</tr/nodes/media-understanding>)


Was this useful?YesNo