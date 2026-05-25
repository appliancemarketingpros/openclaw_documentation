---
title: Node'lar
source_url: https://docs.openclaw.ai/tr/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Eşleştirilmiş Node'ları (cihazları) yönetin ve Node yeteneklerini çağırın.

İlgili:

  * Node'lara genel bakış: [Node'lar](</tr/nodes>)
  * Kamera: [Kamera Node'ları](</tr/nodes/camera>)
  * Görseller: [Görsel Node'ları](</tr/nodes/images>)


Yaygın seçenekler:

  * `--url`, `--token`, `--timeout`, `--json`


## Yaygın komutlar

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` bekleyen/eşleştirilmiş tabloları yazdırır. Eşleştirilmiş satırlar en son bağlantı yaşını (Son Bağlantı) içerir. Yalnızca şu anda bağlı Node'ları göstermek için `--connected` kullanın. Bir süre içinde bağlanmış Node'larla filtrelemek için `--last-connected <duration>` kullanın (örn. `24h`, `7d`). Eski bir Gateway'e ait Node eşleştirme kaydını silmek için `nodes remove --node <id|name|ip>` kullanın.

Onay notu:

  * `openclaw nodes pending` yalnızca eşleştirme kapsamı gerektirir.
  * `gateway.nodes.pairing.autoApproveCidrs`, bekleme adımını yalnızca açıkça güvenilen, ilk kez yapılan `role: node` cihaz eşleştirmesi için atlayabilir. Varsayılan olarak kapalıdır ve yükseltmeleri onaylamaz.
  * `openclaw nodes approve <requestId>`, bekleyen istekten ek kapsam gereksinimlerini devralır: 
    * komutsuz istek: yalnızca eşleştirme
    * yürütme dışı Node komutları: eşleştirme + yazma
    * `system.run` / `system.run.prepare` / `system.which`: eşleştirme + yönetici


## Çağırma

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Çağırma bayrakları:

  * `--params <json>`: JSON nesnesi dizesi (varsayılan `{}`).
  * `--invoke-timeout <ms>`: Node çağırma zaman aşımı (varsayılan `15000`).
  * `--idempotency-key <key>`: isteğe bağlı idempotency anahtarı.
  * `system.run` ve `system.run.prepare` burada engellenir; shell yürütmesi için `host=node` ile `exec` aracını kullanın.


Bir Node üzerinde shell yürütmesi için `openclaw nodes run` yerine `host=node` ile `exec` aracını kullanın. `nodes` CLI artık yetenek odaklıdır: `nodes invoke` üzerinden doğrudan RPC; ayrıca eşleştirme, kamera, ekran, konum, Canvas ve bildirimler. Canvas komutları birlikte gelen deneysel Canvas Plugin tarafından uygulanır; çekirdek, bunların `openclaw nodes canvas` altında kalması için bir uyumluluk kancası tutar.

## İlgili

  * [CLI referansı](</tr/cli>)
  * [Node'lar](</tr/nodes>)


Was this useful?YesNo