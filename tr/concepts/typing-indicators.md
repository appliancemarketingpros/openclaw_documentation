---
title: Yazıyor göstergeleri
source_url: https://docs.openclaw.ai/tr/concepts/typing-indicators
scraped_at: 2026-05-25
---

Yazıyor göstergeleri, bir çalıştırma etkin olduğu sürece sohbet kanalına gönderilir. Yazmanın **ne zaman** başlayacağını denetlemek için `agents.defaults.typingMode`, **ne sıklıkta** yenileneceğini denetlemek için `typingIntervalSeconds` kullanın.

## Varsayılanlar

`agents.defaults.typingMode` **ayarlanmamışsa** , OpenClaw eski davranışı korur:

  * **Doğrudan sohbetler** : model döngüsü başladığında yazma hemen başlar.
  * **Bahsetme içeren grup sohbetleri** : yazma hemen başlar.
  * **Bahsetme içermeyen grup sohbetleri** : yazma yalnızca mesaj metni akmaya başladığında başlar.
  * **Heartbeat çalıştırmaları** : çözümlenen Heartbeat hedefi yazma destekleyen bir sohbetse ve yazma devre dışı değilse, Heartbeat çalıştırması başladığında yazma başlar.


## Modlar

`agents.defaults.typingMode` değerini şunlardan birine ayarlayın:

  * `never` \- hiçbir zaman yazıyor göstergesi gösterilmez.
  * `instant` \- çalıştırma daha sonra yalnızca sessiz yanıt belirtecini döndürse bile **model döngüsü başlar başlamaz** yazmaya başla.
  * `thinking` \- **ilk akıl yürütme deltası** geldiğinde yazmaya başla (çalıştırma için `reasoningLevel: "stream"` gerektirir).
  * `message` \- **ilk sessiz olmayan metin deltası** geldiğinde yazmaya başla (`NO_REPLY` sessiz belirtecini yok sayar).


"Ne kadar erken tetiklenir" sırası: `never` → `message` → `thinking` → `instant`

## Yapılandırma

Aracı düzeyindeki varsayılanı ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Oturum başına modu veya ritmi geçersiz kılın:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Notlar

  * Tüm yük tam olarak sessiz belirteç olduğunda (örneğin `NO_REPLY` / `no_reply`, büyük/küçük harfe duyarsız olarak eşleştirilir), `message` modu yalnızca sessiz yanıtlarda yazmayı göstermez.
  * `thinking` yalnızca çalıştırma akıl yürütmeyi akış olarak yayınlıyorsa tetiklenir (`reasoningLevel: "stream"`). Model akıl yürütme deltaları yaymazsa yazma başlamaz.
  * Heartbeat yazması, çözümlenen teslim hedefi için bir canlılık sinyalidir. `message` veya `thinking` akış zamanlamasını izlemek yerine Heartbeat çalıştırmasının başlangıcında başlar. Devre dışı bırakmak için `typingMode: "never"` ayarlayın.
  * Heartbeat'ler `target: "none"` olduğunda, hedef çözümlenemediğinde, Heartbeat için sohbet teslimi devre dışı olduğunda veya kanal yazmayı desteklemediğinde yazmayı göstermez.
  * `typingIntervalSeconds`, başlangıç zamanını değil **yenileme ritmini** denetler. Varsayılan 6 saniyedir.


## İlgili

[**Varlık** Gateway'in bağlı istemcileri nasıl izlediği ve bunları macOS Örnekler sekmesinde nasıl gösterdiği. ](</tr/concepts/presence>) [**Akış ve parçalama** Giden akış davranışı, parça sınırları ve kanala özgü teslim. ](</tr/concepts/streaming>)

Was this useful?YesNo