---
title: Gateway’e ait eşleştirme
source_url: https://docs.openclaw.ai/tr/gateway/pairing
scraped_at: 2026-05-25
---

Gateway tarafından sahiplenilen eşleştirmede, hangi Node'ların katılmasına izin verildiği konusunda doğruluk kaynağı **Gateway** 'dir. UI'lar (macOS uygulaması, gelecekteki istemciler) yalnızca bekleyen istekleri onaylayan veya reddeden ön yüzlerdir.

**Önemli:** WS Node'ları `connect` sırasında **cihaz eşleştirmesi** (rol `node`) kullanır. `node.pair.*` ayrı bir eşleştirme deposudur ve WS el sıkışmasını **geçitlemez**. Yalnızca açıkça `node.pair.*` çağıran istemciler bu akışı kullanır.

## Kavramlar

  * **Bekleyen istek** : Bir Node katılmayı istedi; onay gerekir.
  * **Eşleştirilmiş Node** : Verilmiş bir auth token ile onaylanmış Node.
  * **Taşıma** : Gateway WS uç noktası istekleri iletir ancak üyeliğe karar vermez. (Eski TCP bridge desteği kaldırılmıştır.)


## Eşleştirme nasıl çalışır?

  1. Bir Node Gateway WS'ye bağlanır ve eşleştirme ister.
  2. Gateway bir **bekleyen istek** saklar ve `node.pair.requested` yayınlar.
  3. İsteği onaylar veya reddedersiniz (CLI ya da UI).
  4. Onayda, Gateway **yeni bir token** verir (yeniden eşleştirmede token'lar döndürülür).
  5. Node token'ı kullanarak yeniden bağlanır ve artık "eşleştirilmiş" olur.


Bekleyen istekler **5 dakika** sonra otomatik olarak sona erer.

## CLI iş akışı (headless için uygun)

bashCopy code
[code]
    openclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes statusopenclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name "Living Room iPad"
[/code]

`nodes status` eşleştirilmiş/bağlı Node'ları ve yeteneklerini gösterir.

## API yüzeyi (gateway protocol)

Olaylar:

  * `node.pair.requested` \- yeni bir bekleyen istek oluşturulduğunda yayınlanır.
  * `node.pair.resolved` \- bir istek onaylandığında/reddedildiğinde/süresi dolduğunda yayınlanır.


Yöntemler:

  * `node.pair.request` \- bekleyen bir istek oluşturur veya yeniden kullanır.
  * `node.pair.list` \- bekleyen + eşleştirilmiş Node'ları listeler (`operator.pairing`).
  * `node.pair.approve` \- bekleyen bir isteği onaylar (token verir).
  * `node.pair.reject` \- bekleyen bir isteği reddeder.
  * `node.pair.remove` \- eski bir eşleştirilmiş Node girdisini kaldırır.
  * `node.pair.verify` \- `{ nodeId, token }` doğrular.


Notlar:

  * `node.pair.request` Node başına idempotent'tir: yinelenen çağrılar aynı bekleyen isteği döndürür.
  * Aynı bekleyen Node için yinelenen istekler, saklanan Node metadata'sını ve operatör görünürlüğü için en son izin listesine alınmış beyan edilen komut anlık görüntüsünü de yeniler.
  * Onay **her zaman** yeni bir token üretir; `node.pair.request` içinden hiçbir token döndürülmez.
  * Operatör kapsam düzeyleri ve onay zamanı kontrolleri [Operatör kapsamları](</tr/gateway/operator-scopes>) bölümünde özetlenmiştir.
  * İstekler, otomatik onay akışları için bir ipucu olarak `silent: true` içerebilir.
  * `node.pair.approve`, ek onay kapsamlarını zorunlu kılmak için bekleyen isteğin beyan edilen komutlarını kullanır: 
    * komutsuz istek: `operator.pairing`
    * exec olmayan komut isteği: `operator.pairing` \+ `operator.write`
    * `system.run` / `system.run.prepare` / `system.which` isteği: `operator.pairing` \+ `operator.admin`


## Node komut geçitleme (2026.3.31+)

Bir Node ilk kez bağlandığında, eşleştirme otomatik olarak istenir. Eşleştirme isteği onaylanana kadar, o Node'dan gelen tüm bekleyen Node komutları filtrelenir ve yürütülmez. Eşleştirme onayıyla güven kurulduktan sonra, Node'un beyan edilen komutları normal komut politikasına tabi olarak kullanılabilir hale gelir.

Bunun anlamı:

  * Komutları açığa çıkarmak için daha önce yalnızca cihaz eşleştirmesine güvenen Node'lar artık Node eşleştirmesini tamamlamalıdır.
  * Eşleştirme onayından önce kuyruğa alınan komutlar ertelenmez, düşürülür.


## Node olay güven sınırları (2026.3.31+)

Node kaynaklı özetler ve ilgili oturum olayları, amaçlanan güvenilir yüzeyle sınırlandırılır. Daha önce daha geniş host veya oturum araç erişimine dayanan bildirim odaklı veya Node tarafından tetiklenen akışların ayarlanması gerekebilir. Bu sertleştirme, Node olaylarının Node'un güven sınırının izin verdiğinin ötesinde host düzeyinde araç erişimine yükselmesini engeller.

Kalıcı Node varlık güncellemeleri aynı kimlik sınırını izler. `node.presence.alive` olayı yalnızca kimliği doğrulanmış Node cihaz oturumlarından kabul edilir ve eşleştirme metadata'sını yalnızca cihaz/Node kimliği zaten eşleştirilmiş olduğunda günceller. Kendi beyan ettiği `client.id` değerleri son görülme durumunu yazmak için yeterli değildir.

## Otomatik onay (macOS uygulaması)

macOS uygulaması isteğe bağlı olarak şu durumlarda **sessiz onay** deneyebilir:

  * istek `silent` olarak işaretlenmişse ve
  * uygulama aynı kullanıcıyı kullanarak gateway host'una SSH bağlantısını doğrulayabiliyorsa.


Sessiz onay başarısız olursa, normal "Onayla/Reddet" istemine geri döner.

## Güvenilir CIDR cihaz otomatik onayı

`role: node` için WS cihaz eşleştirmesi varsayılan olarak manuel kalır. Gateway'in ağ yoluna zaten güvendiği özel Node ağlarında, operatörler açık CIDR'ler veya tam IP'ler ile katılmayı seçebilir:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

Güvenlik sınırı:

  * `gateway.nodes.pairing.autoApproveCidrs` ayarlanmamışsa devre dışıdır.
  * Genel bir LAN veya özel ağ otomatik onay modu yoktur.
  * Yalnızca istenen kapsamı olmayan yeni `role: node` cihaz eşleştirmesi uygundur.
  * Operatör, tarayıcı, Control UI ve WebChat istemcileri manuel kalır.
  * Rol, kapsam, metadata ve public-key yükseltmeleri manuel kalır.
  * Aynı host local loopback güvenilir proxy header yolları uygun değildir çünkü bu yol yerel çağıranlar tarafından sahte olarak üretilebilir.


## Metadata yükseltmesi otomatik onayı

Zaten eşleştirilmiş bir cihaz yalnızca hassas olmayan metadata değişiklikleriyle yeniden bağlandığında (örneğin görünen ad veya istemci platform ipuçları), OpenClaw bunu bir `metadata-upgrade` olarak ele alır. Sessiz otomatik onay dardır: yalnızca yerel veya paylaşılan kimlik bilgilerine sahip olduğunu zaten kanıtlamış güvenilir, tarayıcı olmayan yerel yeniden bağlantılar için geçerlidir; OS sürümü metadata değişikliklerinden sonra aynı host yerel uygulama yeniden bağlantıları dahil. Tarayıcı/Control UI istemcileri ve uzak istemciler yine açık yeniden onay akışını kullanır. Kapsam yükseltmeleri (okumadan yazma/admin'e) ve public key değişiklikleri metadata yükseltmesi otomatik onayı için uygun **değildir** \- açık yeniden onay istekleri olarak kalırlar.

## QR eşleştirme yardımcıları

`/pair qr`, mobil ve tarayıcı istemcilerinin doğrudan tarayabilmesi için eşleştirme payload'unu yapılandırılmış medya olarak işler.

Bir cihazı silmek, o cihaz id'si için eski bekleyen eşleştirme isteklerini de temizler; böylece `nodes pending`, iptalden sonra sahipsiz satırlar göstermez.

## Yerellik ve iletilen header'lar

Gateway eşleştirmesi bir bağlantıyı yalnızca hem ham soket hem de tüm upstream proxy kanıtları aynı fikirde olduğunda loopback olarak ele alır. Bir istek loopback üzerinden gelir ancak yerel olmayan bir kaynağı işaret eden `X-Forwarded-For` / `X-Forwarded-Host` / `X-Forwarded-Proto` header'ları taşırsa, bu iletilen-header kanıtı loopback yerellik iddiasını geçersiz kılar. Eşleştirme yolu daha sonra isteği aynı host bağlantısı olarak sessizce ele almak yerine açık onay gerektirir. Operatör kimlik doğrulamasındaki eşdeğer kural için [Güvenilir Proxy Auth](</tr/gateway/trusted-proxy-auth>) bölümüne bakın.

## Depolama (yerel, özel)

Eşleştirme durumu Gateway durum dizini altında saklanır (varsayılan `~/.openclaw`):

  * `~/.openclaw/nodes/paired.json`
  * `~/.openclaw/nodes/pending.json`


`OPENCLAW_STATE_DIR` değerini geçersiz kılarsanız, `nodes/` klasörü onunla birlikte taşınır.

Güvenlik notları:

  * Token'lar gizlidir; `paired.json` dosyasını hassas kabul edin.
  * Bir token'ı döndürmek yeniden onay gerektirir (veya Node girdisini silmeyi).


## Taşıma davranışı

  * Taşıma **durumsuzdur** ; üyelik saklamaz.
  * Gateway çevrimdışıysa veya eşleştirme devre dışıysa, Node'lar eşleşemez.
  * Gateway remote moddaysa, eşleştirme yine remote Gateway'in deposuna karşı gerçekleşir.


## İlgili

  * [Kanal eşleştirmesi](</tr/channels/pairing>)
  * [Node'lar](</tr/nodes>)
  * [Cihazlar CLI](</tr/cli/devices>)


Was this useful?YesNo