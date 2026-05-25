---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/id/cli/tasks
scraped_at: 2026-05-25
---

Periksa tugas latar belakang persisten dan status Task Flow. Tanpa subperintah, `openclaw tasks` setara dengan `openclaw tasks list`.

Lihat [Tugas Latar Belakang](</id/automation/tasks>) untuk siklus hidup dan model pengiriman.

## Penggunaan

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Opsi Root

  * `--json`: keluarkan JSON.
  * `--runtime <name>`: filter menurut jenis: `subagent`, `acp`, `cron`, atau `cli`.
  * `--status <name>`: filter menurut status: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, atau `lost`.


## Subperintah

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Mencantumkan tugas latar belakang yang dilacak, yang terbaru lebih dulu.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Menampilkan satu tugas berdasarkan ID tugas, ID eksekusi, atau kunci sesi.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Mengubah kebijakan notifikasi untuk tugas yang sedang berjalan.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Membatalkan tugas latar belakang yang sedang berjalan.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Memunculkan catatan tugas dan Task Flow yang basi, hilang, gagal dikirim, atau tidak konsisten. Tugas hilang yang dipertahankan hingga `cleanupAfter` adalah peringatan; tugas hilang yang kedaluwarsa atau tidak diberi stempel adalah kesalahan.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Mempratinjau atau menerapkan rekonsiliasi tugas dan Task Flow, pemberian stempel pembersihan, pemangkasan, dan pembersihan registri sesi eksekusi cron yang basi. Untuk tugas cron, rekonsiliasi menggunakan log eksekusi/status pekerjaan yang dipersistenkan sebelum menandai tugas aktif lama sebagai `lost`, sehingga eksekusi cron yang selesai tidak menjadi kesalahan audit palsu hanya karena status runtime Gateway di memori sudah hilang. Audit CLI offline tidak otoritatif untuk kumpulan pekerjaan aktif cron lokal-proses milik Gateway. Tugas CLI dengan ID eksekusi/ID sumber ditandai `lost` saat konteks eksekusi Gateway langsungnya hilang, meskipun baris sesi anak lama masih ada. Saat diterapkan, pemeliharaan juga memangkas baris registri sesi `cron:<jobId>:run:<uuid>` yang lebih lama dari 7 hari sambil mempertahankan pekerjaan cron yang sedang berjalan dan membiarkan baris sesi non-cron tidak tersentuh.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Memeriksa atau membatalkan status Task Flow persisten di bawah ledger tugas.

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Tugas latar belakang](</id/automation/tasks>)


Was this useful?YesNo