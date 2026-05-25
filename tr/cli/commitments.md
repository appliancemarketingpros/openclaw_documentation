---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/tr/cli/commitments
scraped_at: 2026-05-25
---

Çıkarılan takip taahhütlerini listeleyin ve yönetin.

Taahhütler, konuşma bağlamından oluşturulan, katılım gerektiren ve kısa ömürlü takip bellekleridir. Kavramsal kılavuz için [Çıkarılan taahhütler](</tr/concepts/commitments>) bölümüne bakın.

Alt komut olmadan, `openclaw commitments` bekleyen taahhütleri listeler.

## Kullanım

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Seçenekler

  * `--all`: yalnızca bekleyen taahhütler yerine tüm durumları gösterir.
  * `--agent <id>`: tek bir ajan kimliğine göre filtreler.
  * `--status <status>`: duruma göre filtreler. Değerler: `pending`, `sent`, `dismissed`, `snoozed` veya `expired`.
  * `--json`: makine tarafından okunabilir JSON çıktısı verir.


## Örnekler

Bekleyen taahhütleri listeleyin:

bashCopy code
[code]
    openclaw commitments
[/code]

Saklanan her taahhüdü listeleyin:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Tek bir ajana göre filtreleyin:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Ertelenmiş taahhütleri bulun:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Bir veya daha fazla taahhüdü kapatın:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

JSON olarak dışa aktarın:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Çıktı

Metin çıktısı şunları içerir:

  * taahhüt kimliği
  * durum
  * tür
  * en erken son tarih
  * kapsam
  * önerilen yoklama metni


JSON çıktısı ayrıca taahhüt deposu yolunu ve saklanan kayıtların tamamını içerir.

## İlgili

  * [Çıkarılan taahhütler](</tr/concepts/commitments>)
  * [Belleğe genel bakış](</tr/concepts/memory>)
  * [Heartbeat](</tr/gateway/heartbeat>)
  * [Zamanlanmış görevler](</tr/automation/cron-jobs>)


Was this useful?YesNo