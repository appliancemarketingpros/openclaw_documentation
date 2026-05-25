---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/id/cli/commitments
scraped_at: 2026-05-25
---

Cantumkan dan kelola komitmen tindak lanjut yang diinferensi.

Komitmen bersifat opt-in, berupa memori tindak lanjut berumur pendek yang dibuat dari konteks percakapan. Lihat [Komitmen yang diinferensi](</id/concepts/commitments>) untuk panduan konseptual.

Tanpa subperintah, `openclaw commitments` mencantumkan komitmen tertunda.

## Penggunaan

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opsi

  * `--all`: tampilkan semua status alih-alih hanya komitmen tertunda.
  * `--agent <id>`: filter ke satu id agen.
  * `--status <status>`: filter menurut status. Nilai: `pending`, `sent`, `dismissed`, `snoozed`, atau `expired`.
  * `--json`: keluarkan JSON yang dapat dibaca mesin.


## Contoh

Cantumkan komitmen tertunda:

bashCopy code
[code]
    openclaw commitments
[/code]

Cantumkan setiap komitmen yang tersimpan:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filter ke satu agen:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Temukan komitmen yang ditunda:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Abaikan satu atau beberapa komitmen:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Ekspor sebagai JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Keluaran

Keluaran teks mencakup:

  * id komitmen
  * status
  * jenis
  * waktu jatuh tempo paling awal
  * cakupan
  * teks check-in yang disarankan


Keluaran JSON juga mencakup jalur penyimpanan komitmen dan rekaman tersimpan lengkap.

## Terkait

  * [Komitmen yang diinferensi](</id/concepts/commitments>)
  * [Ikhtisar memori](</id/concepts/memory>)
  * [Heartbeat](</id/gateway/heartbeat>)
  * [Tugas terjadwal](</id/automation/cron-jobs>)


Was this useful?YesNo