---
title: Sistem
source_url: https://docs.openclaw.ai/tr/cli/system
scraped_at: 2026-05-25
---

# `openclaw system`

Gateway için sistem düzeyi yardımcılar: sistem olaylarını kuyruğa alır, Heartbeat'leri kontrol eder ve varlık durumunu görüntüler.

Tüm `system` alt komutları Gateway RPC kullanır ve paylaşılan istemci bayraklarını kabul eder:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## Yaygın komutlar

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

Varsayılan olarak **main** oturumda bir sistem olayını kuyruğa alır. Sonraki Heartbeat bunu istemde bir `System:` satırı olarak enjekte eder. Heartbeat'i hemen tetiklemek için `--mode now` kullanın; `next-heartbeat` bir sonraki zamanlanmış işareti bekler.

Belirli bir oturumu hedeflemek için `--session-key` iletin (örneğin bir async-task tamamlanmasını, onu başlatan kanala geri aktarmak için).

> **`--session-key` ile zamanlama istisnası:** `--session-key` sağlandığında, `--mode next-heartbeat` bir sonraki zamanlanmış işareti beklemek yerine hemen hedeflenen bir uyandırmaya indirgenir. Hedeflenen uyandırmalar Heartbeat amacı olarak `immediate` kullanır; böylece aksi halde bir `event` amaçlı uyandırmayı erteleyecek (ve fiilen düşürecek) çalıştırıcının zamanı gelmemiş kapısını atlarlar. Gecikmeli teslim istiyorsanız, `--session-key` kullanmayın; böylece olay main oturuma düşer ve bir sonraki normal Heartbeat ile ilerler.

Bayraklar:

  * `--text <text>`: gerekli sistem olayı metni.
  * `--mode <mode>`: `now` veya `next-heartbeat` (varsayılan).
  * `--session-key <sessionKey>`: isteğe bağlı; ajanın main oturumu yerine belirli bir ajan oturumunu hedefler. Çözümlenen ajana ait olmayan anahtarlar ajanın main oturumuna geri döner.
  * `--json`: makine tarafından okunabilir çıktı.
  * `--url`, `--token`, `--timeout`, `--expect-final`: paylaşılan Gateway RPC bayrakları.


## `system heartbeat last|enable|disable`

Heartbeat kontrolleri:

  * `last`: son Heartbeat olayını gösterir.
  * `enable`: Heartbeat'leri yeniden açar (devre dışı bırakılmışlarsa bunu kullanın).
  * `disable`: Heartbeat'leri duraklatır.


Bayraklar:

  * `--json`: makine tarafından okunabilir çıktı.
  * `--url`, `--token`, `--timeout`, `--expect-final`: paylaşılan Gateway RPC bayrakları.


## `system presence`

Gateway'in bildiği geçerli sistem varlığı girdilerini listeler (düğümler, örnekler ve benzer durum satırları).

Bayraklar:

  * `--json`: makine tarafından okunabilir çıktı.
  * `--url`, `--token`, `--timeout`, `--expect-final`: paylaşılan Gateway RPC bayrakları.


## Notlar

  * Mevcut yapılandırmanızla erişilebilen çalışan bir Gateway gerektirir (yerel veya uzak).
  * Sistem olayları geçicidir ve yeniden başlatmalar arasında kalıcı değildir.


## İlgili

  * [CLI başvurusu](</tr/cli>)


Was this useful?YesNo