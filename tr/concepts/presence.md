---
title: Durum bilgisi
source_url: https://docs.openclaw.ai/tr/concepts/presence
scraped_at: 2026-05-25
---

OpenClaw "presence", aşağıdakilerin hafif, mümkün olan en iyi çabayla sunulan bir görünümüdür:

  * **Gateway** ’in kendisi ve
  * **Gateway** ’e bağlı **istemciler** (mac uygulaması, WebChat, CLI vb.)


Presence, öncelikli olarak macOS uygulamasının **Instances** sekmesini oluşturmak ve operatöre hızlı görünürlük sağlamak için kullanılır.

## Presence alanları (neler görünür)

Presence girdileri, şunlar gibi alanlara sahip yapılandırılmış nesnelerdir:

  * `instanceId` (isteğe bağlı ama önemle önerilir): kararlı istemci kimliği (genellikle `connect.client.instanceId`)
  * `host`: insan tarafından okunabilir ana makine adı
  * `ip`: mümkün olan en iyi çabayla belirlenen IP adresi
  * `version`: istemci sürüm dizesi
  * `deviceFamily` / `modelIdentifier`: donanım ipuçları
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: "son kullanıcı girişinden bu yana geçen saniye" (biliniyorsa)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: son güncelleme zaman damgası (epoch’tan bu yana ms)


## Üreticiler (presence nereden gelir)

Presence girdileri birden fazla kaynak tarafından üretilir ve **birleştirilir**.

### 1) Gateway self girdisi

Gateway, başlatma sırasında her zaman bir "self" girdisi oluşturur; böylece kullanıcı arayüzleri, herhangi bir istemci bağlanmadan önce bile gateway ana makinesini gösterir.

### 2) WebSocket connect

Her WS istemcisi bir `connect` isteğiyle başlar. Başarılı el sıkışmadan sonra Gateway, bu bağlantı için bir presence girdisini ekler veya günceller.

#### Tek seferlik CLI komutları neden görünmez

CLI genellikle kısa, tek seferlik komutlar için bağlanır. Instances listesini kalabalıklaştırmamak için `client.mode === "cli"` bir presence girdisine **dönüştürülmez**.

### 3) `system-event` işaretleri

İstemciler `system-event` yöntemiyle daha zengin periyodik işaretler gönderebilir. mac uygulaması bunu ana makine adını, IP’yi ve `lastInputSeconds` değerini bildirmek için kullanır.

### 4) Node bağlantıları (role: node)

Bir node, Gateway WebSocket üzerinden `role: node` ile bağlandığında, Gateway bu node için bir presence girdisini ekler veya günceller (diğer WS istemcileriyle aynı akış).

## Birleştirme + tekilleştirme kuralları (`instanceId` neden önemlidir)

Presence girdileri tek bir bellek içi haritada saklanır:

  * Girdiler bir **presence anahtarı** ile anahtarlanır.
  * En iyi anahtar, yeniden başlatmalardan sonra da korunan kararlı bir `instanceId`’dir (`connect.client.instanceId` içinden).
  * Anahtarlar büyük/küçük harfe duyarsızdır.


Bir istemci kararlı bir `instanceId` olmadan yeniden bağlanırsa, **yinelenen** satır olarak görünebilir.

## TTL ve sınırlı boyut

Presence bilerek geçicidir:

  * **TTL:** 5 dakikadan eski girdiler budanır
  * **Maksimum girdi:** 200 (önce en eskiler atılır)


Bu, listenin güncel kalmasını sağlar ve sınırsız bellek büyümesini önler.

## Uzak/tünel uyarısı (loopback IP’leri)

Bir istemci SSH tüneli / yerel port yönlendirme üzerinden bağlandığında, Gateway uzak adresi `127.0.0.1` olarak görebilir. İstemcinin bildirdiği iyi bir IP’nin üzerine yazmamak için loopback uzak adresleri yok sayılır.

## Tüketiciler

### macOS Instances sekmesi

macOS uygulaması `system-presence` çıktısını işler ve son güncellemenin yaşına göre küçük bir durum göstergesi (Etkin/Boşta/Eski) uygular.

## Hata ayıklama ipuçları

  * Ham listeyi görmek için Gateway’e karşı `system-presence` çağırın.
  * Yinelenenler görürseniz: 
    * istemcilerin el sıkışmada kararlı bir `client.instanceId` gönderdiğini doğrulayın
    * periyodik işaretlerin aynı `instanceId` değerini kullandığını doğrulayın
    * bağlantıdan türetilen girdide `instanceId` eksik olup olmadığını kontrol edin (yinelenenler beklenir)


## İlgili

[**Yazma göstergeleri** Yazma göstergelerinin ne zaman gönderildiği ve nasıl ayarlanacağı. ](</tr/concepts/typing-indicators>) [**Akış ve parçalama** Giden akış, parçalama ve kanal başına biçimlendirme. ](</tr/concepts/streaming>) [**Gateway mimarisi** Gateway bileşenleri ve presence güncellemelerini çalıştıran WebSocket protokolü. ](</tr/concepts/architecture>) [**Gateway protokolü** `connect`, `system-event` ve `system-presence` için kablo protokolü. ](</tr/gateway/protocol>)

Was this useful?YesNo