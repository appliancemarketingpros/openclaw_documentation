---
title: Tugas latar belakang
source_url: https://docs.openclaw.ai/id/automation/tasks
scraped_at: 2026-05-25
---

Tugas latar belakang melacak pekerjaan yang berjalan **di luar sesi percakapan utama Anda** : eksekusi ACP, pemijahan subagen, eksekusi tugas cron terisolasi, dan operasi yang dimulai CLI.

Tugas **tidak** menggantikan sesi, tugas cron, atau heartbeat - tugas adalah **buku besar aktivitas** yang mencatat pekerjaan terpisah apa yang terjadi, kapan, dan apakah berhasil.

## TL;DR

  * Tugas adalah **catatan** , bukan penjadwal - cron dan heartbeat menentukan _kapan_ pekerjaan berjalan, tugas melacak _apa yang terjadi_.
  * ACP, subagen, semua tugas cron, dan operasi CLI membuat tugas. Giliran heartbeat tidak.
  * Setiap tugas bergerak melalui `queued → running → terminal` (succeeded, failed, timed_out, cancelled, atau lost).
  * Tugas Cron tetap aktif selama runtime cron masih memiliki tugas tersebut; jika status runtime dalam memori hilang, pemeliharaan tugas pertama-tama memeriksa riwayat eksekusi cron yang persisten sebelum menandai tugas sebagai hilang.
  * Penyelesaian didorong push: pekerjaan terpisah dapat memberi tahu secara langsung atau membangunkan sesi/heartbeat peminta saat selesai, sehingga loop polling status biasanya bukan bentuk yang tepat.
  * Eksekusi cron terisolasi dan penyelesaian subagen berupaya sebaik mungkin membersihkan tab/proses browser yang dilacak untuk sesi turunannya sebelum pembukuan pembersihan akhir.
  * Pengiriman cron terisolasi menekan balasan induk sementara yang usang saat pekerjaan subagen turunan masih dikuras, dan lebih memilih output turunan akhir saat output itu tiba sebelum pengiriman.
  * Notifikasi penyelesaian dikirim langsung ke channel atau diantrekan untuk heartbeat berikutnya.
  * `openclaw tasks list` menampilkan semua tugas; `openclaw tasks audit` memunculkan masalah.
  * Catatan terminal disimpan selama 7 hari, lalu dipangkas otomatis.


## Mulai cepat

### Daftar dan filter

bashCopy code
[code]
    # List all tasks (newest first)openclaw tasks list # Filter by runtime or statusopenclaw tasks list --runtime acpopenclaw tasks list --status running
[/code]

### Periksa

bashCopy code
[code]
    # Show details for a specific task (by ID, run ID, or session key)openclaw tasks show <lookup>
[/code]

### Batalkan dan beri tahu

bashCopy code
[code]
    # Cancel a running task (kills the child session)openclaw tasks cancel <lookup> # Change notification policy for a taskopenclaw tasks notify <lookup> state_changes
[/code]

### Audit dan pemeliharaan

bashCopy code
[code]
    # Run a health auditopenclaw tasks audit # Preview or apply maintenanceopenclaw tasks maintenanceopenclaw tasks maintenance --apply
[/code]

### Alur tugas

bashCopy code
[code]
    # Inspect TaskFlow stateopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Apa yang membuat tugas

Sumber | Jenis runtime | Kapan catatan tugas dibuat | Kebijakan notifikasi default  
---|---|---|---  
Eksekusi latar belakang ACP | `acp` | Memijahkan sesi ACP turunan | `done_only`  
Orkestrasi subagen | `subagent` | Memijahkan subagen melalui `sessions_spawn` | `done_only`  
Tugas Cron (semua jenis) | `cron` | Setiap eksekusi cron (sesi utama dan terisolasi) | `silent`  
Operasi CLI | `cli` | Perintah `openclaw agent` yang berjalan melalui gateway | `silent`  
Tugas media agen | `cli` | Eksekusi `music_generate`/`video_generate` berbasis sesi | `silent`  
  
Default notifikasi untuk cron dan media

Tugas cron sesi utama menggunakan kebijakan notifikasi `silent` secara default - tugas tersebut membuat catatan untuk pelacakan tetapi tidak menghasilkan notifikasi. Tugas cron terisolasi juga default ke `silent` tetapi lebih terlihat karena berjalan dalam sesinya sendiri.

Eksekusi `music_generate` dan `video_generate` berbasis sesi juga menggunakan kebijakan notifikasi `silent`. Eksekusi tersebut tetap membuat catatan tugas, tetapi penyelesaian diserahkan kembali ke sesi agen asli sebagai wake internal agar agen dapat menulis pesan tindak lanjut dan melampirkan media yang selesai sendiri. Penyelesaian grup/channel mengikuti kebijakan balasan terlihat yang normal, sehingga agen menggunakan alat pesan saat pengiriman sumber memerlukannya. Jika agen penyelesaian gagal menghasilkan bukti pengiriman alat pesan dalam rute hanya alat, OpenClaw mengirim fallback penyelesaian langsung ke channel asli alih-alih membiarkan media tetap privat.

Guardrail video_generate bersamaan

Saat tugas `video_generate` berbasis sesi masih aktif, alat tersebut juga bertindak sebagai guardrail: panggilan `video_generate` berulang dalam sesi yang sama mengembalikan status tugas aktif alih-alih memulai pembuatan bersamaan kedua. Gunakan `action: "status"` saat Anda menginginkan pencarian progres/status eksplisit dari sisi agen.

Apa yang tidak membuat tugas

  * Giliran Heartbeat - sesi utama; lihat [Heartbeat](</id/gateway/heartbeat>)
  * Giliran chat interaktif normal
  * Respons `/command` langsung


## Siklus hidup tugas
[code] 
    stateDiagram-v2
        [*] --> queued
        queued --> running : agent starts
        running --> succeeded : completes ok
        running --> failed : error
        running --> timed_out : timeout exceeded
        running --> cancelled : operator cancels
        queued --> lost : session gone > 5 min
        running --> lost : session gone > 5 min
[/code]

Status | Artinya  
---|---  
`queued` | Dibuat, menunggu agen dimulai  
`running` | Giliran agen sedang aktif dieksekusi  
`succeeded` | Selesai dengan berhasil  
`failed` | Selesai dengan error  
`timed_out` | Melebihi timeout yang dikonfigurasi  
`cancelled` | Dihentikan oleh operator melalui `openclaw tasks cancel`  
`lost` | Runtime kehilangan status pendukung otoritatif setelah masa tenggang 5 menit  
  
Transisi terjadi otomatis - saat eksekusi agen terkait berakhir, status tugas diperbarui agar sesuai.

Penyelesaian eksekusi agen bersifat otoritatif untuk catatan tugas aktif. Eksekusi terpisah yang berhasil difinalisasi sebagai `succeeded`, error eksekusi biasa difinalisasi sebagai `failed`, dan hasil timeout atau abort difinalisasi sebagai `timed_out`. Jika operator sudah membatalkan tugas, atau runtime sudah mencatat status terminal yang lebih kuat seperti `failed`, `timed_out`, atau `lost`, sinyal keberhasilan yang datang belakangan tidak menurunkan status terminal tersebut.

`lost` sadar runtime:

  * Tugas ACP: metadata sesi turunan ACP pendukung menghilang.
  * Tugas subagen: sesi turunan pendukung menghilang dari penyimpanan agen target.
  * Tugas Cron: runtime cron tidak lagi melacak tugas sebagai aktif dan riwayat eksekusi cron yang persisten tidak menampilkan hasil terminal untuk eksekusi tersebut. Audit CLI offline tidak memperlakukan status runtime cron dalam prosesnya sendiri yang kosong sebagai otoritas.
  * Tugas CLI: tugas dengan id eksekusi/id sumber menggunakan konteks eksekusi live, sehingga baris sesi turunan atau sesi chat yang tertinggal tidak membuatnya tetap aktif setelah eksekusi milik gateway menghilang. Tugas CLI lama tanpa identitas eksekusi tetap fallback ke sesi turunan. Eksekusi `openclaw agent` yang didukung Gateway juga difinalisasi dari hasil eksekusinya, sehingga eksekusi yang selesai tidak tetap aktif sampai penyapu menandainya `lost`.


## Pengiriman dan notifikasi

Saat tugas mencapai status terminal, OpenClaw memberi tahu Anda. Ada dua jalur pengiriman:

**Pengiriman langsung** \- jika tugas memiliki target channel (`requesterOrigin`), pesan penyelesaian langsung menuju channel tersebut (Telegram, Discord, Slack, dll.). Penyelesaian tugas grup dan channel sebaliknya dirutekan melalui sesi peminta agar agen induk dapat menulis balasan yang terlihat. Untuk penyelesaian subagen, OpenClaw juga mempertahankan perutean thread/topik terikat bila tersedia dan dapat mengisi `to` / akun yang hilang dari rute tersimpan sesi peminta (`lastChannel` / `lastTo` / `lastAccountId`) sebelum menyerah pada pengiriman langsung.

**Pengiriman antrean sesi** \- jika pengiriman langsung gagal atau tidak ada origin yang disetel, pembaruan diantrekan sebagai event sistem dalam sesi peminta dan muncul pada heartbeat berikutnya.

Itu berarti workflow biasanya berbasis push: mulai pekerjaan terpisah sekali, lalu biarkan runtime membangunkan atau memberi tahu Anda saat selesai. Poll status tugas hanya saat Anda membutuhkan debugging, intervensi, atau audit eksplisit.

### Kebijakan notifikasi

Kontrol seberapa banyak yang Anda dengar tentang setiap tugas:

Kebijakan | Apa yang dikirim  
---|---  
`done_only` (default) | Hanya status terminal (succeeded, failed, dll.) - **ini adalah default**  
`state_changes` | Setiap transisi status dan pembaruan progres  
`silent` | Tidak ada sama sekali  
  
Ubah kebijakan saat tugas sedang berjalan:

bashCopy code
[code]
    openclaw tasks notify <lookup> state_changes
[/code]

## Referensi CLI

tasks list bashCopy code
[code]
    openclaw tasks list [--runtime <acp|subagent|cron|cli>] [--status <status>] [--json]
[/code]

Kolom output: ID Tugas, Jenis, Status, Pengiriman, ID Eksekusi, Sesi Turunan, Ringkasan.

tasks show bashCopy code
[code]
    openclaw tasks show <lookup>
[/code]

Token pencarian menerima ID tugas, ID eksekusi, atau kunci sesi. Menampilkan catatan lengkap termasuk waktu, status pengiriman, error, dan ringkasan terminal.

tasks cancel bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Untuk tugas ACP dan subagen, ini mematikan sesi turunan. Untuk tugas yang dilacak CLI, pembatalan dicatat dalam registry tugas (tidak ada handle runtime turunan terpisah). Status bertransisi ke `cancelled` dan notifikasi pengiriman dikirim bila berlaku.

tasks notify bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

tasks audit bashCopy code
[code]
    openclaw tasks audit [--json]
[/code]

Memunculkan masalah operasional. Temuan juga muncul di `openclaw status` saat masalah terdeteksi.

Temuan | Keparahan | Pemicu  
---|---|---  
`stale_queued` | peringatan | Mengantre selama lebih dari 10 menit  
`stale_running` | kesalahan | Berjalan selama lebih dari 30 menit  
`lost` | peringatan/kesalahan | Kepemilikan tugas yang didukung runtime menghilang; tugas hilang yang dipertahankan memperingatkan hingga `cleanupAfter`, lalu menjadi kesalahan  
`delivery_failed` | peringatan | Pengiriman gagal dan kebijakan notifikasi bukan `silent`  
`missing_cleanup` | peringatan | Tugas terminal tanpa stempel waktu pembersihan  
`inconsistent_timestamps` | peringatan | Pelanggaran linimasa (misalnya berakhir sebelum dimulai)  
pemeliharaan tugas bashCopy code
[code]
    openclaw tasks maintenance [--json]openclaw tasks maintenance --apply [--json]
[/code]

Gunakan ini untuk meninjau atau menerapkan rekonsiliasi, penandaan pembersihan, dan pemangkasan untuk tugas, status Task Flow, serta baris registri sesi eksekusi cron yang usang.

Rekonsiliasi sadar runtime:

  * Tugas ACP/subagent memeriksa sesi anak yang mendukungnya.
  * Tugas subagent yang sesi anaknya memiliki tombstone pemulihan restart ditandai hilang alih-alih diperlakukan sebagai sesi pendukung yang dapat dipulihkan.
  * Tugas Cron memeriksa apakah runtime cron masih memiliki job, lalu memulihkan status terminal dari log eksekusi cron/status job yang dipersistenkan sebelum fallback ke `lost`. Hanya proses Gateway yang berwenang atas set job aktif cron dalam memori; audit CLI offline menggunakan riwayat tahan lama tetapi tidak menandai tugas cron hilang hanya karena Set lokal itu kosong.
  * Tugas CLI dengan identitas eksekusi memeriksa konteks eksekusi live pemilik, bukan hanya baris sesi anak atau sesi chat.


Pembersihan penyelesaian juga sadar runtime:

  * Penyelesaian subagent berupaya sebaik mungkin menutup tab/proses browser yang terlacak untuk sesi anak sebelum pembersihan pengumuman berlanjut.
  * Penyelesaian cron terisolasi berupaya sebaik mungkin menutup tab/proses browser yang terlacak untuk sesi cron sebelum eksekusi sepenuhnya dibongkar.
  * Pengiriman cron terisolasi menunggu tindak lanjut subagent turunan bila diperlukan dan menekan teks pengakuan induk yang usang alih-alih mengumumkannya.
  * Pengiriman penyelesaian subagent lebih memilih teks asisten terbaru yang terlihat; jika kosong, ia fallback ke teks tool/toolResult terbaru yang telah disanitasi, dan eksekusi panggilan tool yang hanya timeout dapat diringkas menjadi ringkasan kemajuan parsial singkat. Eksekusi terminal yang gagal mengumumkan status kegagalan tanpa memutar ulang teks balasan yang ditangkap.
  * Kegagalan pembersihan tidak menutupi hasil tugas yang sebenarnya.


Saat menerapkan pemeliharaan, OpenClaw juga menghapus baris registri sesi `cron:<jobId>:run:<uuid>` yang usang lebih dari 7 hari, sambil mempertahankan baris untuk job cron yang sedang berjalan dan membiarkan baris sesi non-cron tidak tersentuh.

tasks flow list | show | cancel bashCopy code
[code]
    openclaw tasks flow list [--status <status>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Gunakan ini ketika Task Flow pengorkestrasi adalah hal yang Anda pedulikan, bukan satu catatan tugas latar belakang individual.

## Papan tugas chat (`/tasks`)

Gunakan `/tasks` dalam sesi chat apa pun untuk melihat tugas latar belakang yang ditautkan ke sesi tersebut. Papan menampilkan tugas aktif dan yang baru selesai dengan runtime, status, waktu, serta detail kemajuan atau kesalahan.

Ketika sesi saat ini tidak memiliki tugas tertaut yang terlihat, `/tasks` fallback ke jumlah tugas lokal agen sehingga Anda tetap mendapatkan ikhtisar tanpa membocorkan detail sesi lain.

Untuk ledger operator lengkap, gunakan CLI: `openclaw tasks list`.

## Integrasi status (tekanan tugas)

`openclaw status` menyertakan ringkasan tugas sekilas:

CodeCopy code
[code]
    Tasks: 3 queued · 2 running · 1 issues
[/code]

Ringkasan melaporkan:

  * **aktif** \- jumlah `queued` \+ `running`
  * **kegagalan** \- jumlah `failed` \+ `timed_out` \+ `lost`
  * **byRuntime** \- rincian menurut `acp`, `subagent`, `cron`, `cli`


Baik `/status` maupun tool `session_status` menggunakan snapshot tugas yang sadar pembersihan: tugas aktif diprioritaskan, baris selesai yang usang disembunyikan, dan kegagalan terbaru hanya ditampilkan ketika tidak ada pekerjaan aktif yang tersisa. Ini menjaga kartu status tetap berfokus pada hal yang penting saat ini.

## Penyimpanan dan pemeliharaan

### Tempat tugas berada

Catatan tugas dipersistenkan di SQLite pada:

CodeCopy code
[code]
    $OPENCLAW_STATE_DIR/tasks/runs.sqlite
[/code]

Registri dimuat ke memori saat gateway dimulai dan menyinkronkan penulisan ke SQLite untuk ketahanan lintas restart. Gateway menjaga log write-ahead SQLite tetap terbatas dengan menggunakan ambang batas autocheckpoint default SQLite plus checkpoint `TRUNCATE` berkala dan saat shutdown.

### Pemeliharaan otomatis

Sweeper berjalan setiap **60 detik** dan menangani empat hal:

* ### Rekonsiliasi

Memeriksa apakah tugas aktif masih memiliki dukungan runtime yang berwenang. Tugas ACP/subagent menggunakan status sesi anak, tugas cron menggunakan kepemilikan job aktif, dan tugas CLI dengan identitas eksekusi menggunakan konteks eksekusi pemilik. Jika status pendukung itu hilang selama lebih dari 5 menit, tugas ditandai `lost`.

* ### Perbaikan sesi ACP

Menutup sesi ACP one-shot milik induk yang terminal atau yatim, dan menutup sesi ACP persisten yang terminal usang atau yatim hanya ketika tidak ada binding percakapan aktif yang tersisa.

* ### Penandaan pembersihan

Menetapkan stempel waktu `cleanupAfter` pada tugas terminal (endedAt + 7 hari). Selama retensi, tugas hilang masih muncul dalam audit sebagai peringatan; setelah `cleanupAfter` kedaluwarsa atau ketika metadata pembersihan hilang, tugas tersebut menjadi kesalahan.

* ### Pemangkasan

Menghapus catatan yang melewati tanggal `cleanupAfter` mereka.

## Cara tugas terkait dengan sistem lain

Tugas dan Task Flow

[Task Flow](</id/automation/taskflow>) adalah lapisan orkestrasi flow di atas tugas latar belakang. Satu flow dapat mengoordinasikan beberapa tugas selama masa pakainya menggunakan mode sinkronisasi terkelola atau tercermin. Gunakan `openclaw tasks` untuk memeriksa catatan tugas individual dan `openclaw tasks flow` untuk memeriksa flow pengorkestrasi.

Lihat [Task Flow](</id/automation/taskflow>) untuk detail.

Tugas dan cron

**Definisi** job cron berada di `~/.openclaw/cron/jobs.json`; status eksekusi runtime berada di sampingnya di `~/.openclaw/cron/jobs-state.json`. **Setiap** eksekusi cron membuat catatan tugas - baik sesi utama maupun terisolasi. Tugas cron sesi utama default ke kebijakan notifikasi `silent` sehingga dapat dilacak tanpa menghasilkan notifikasi.

Lihat [Cron Jobs](</id/automation/cron-jobs>).

Tugas dan heartbeat

Eksekusi Heartbeat adalah giliran sesi utama - eksekusi tersebut tidak membuat catatan tugas. Ketika sebuah tugas selesai, tugas tersebut dapat memicu bangun heartbeat sehingga Anda segera melihat hasilnya.

Lihat [Heartbeat](</id/gateway/heartbeat>).

Tugas dan sesi

Tugas dapat merujuk ke `childSessionKey` (tempat pekerjaan berjalan) dan `requesterSessionKey` (siapa yang memulainya). Sesi adalah konteks percakapan; tugas adalah pelacakan aktivitas di atasnya.

Tugas dan eksekusi agen

`runId` tugas menautkan ke eksekusi agen yang melakukan pekerjaan. Peristiwa siklus hidup agen (mulai, selesai, kesalahan) otomatis memperbarui status tugas - Anda tidak perlu mengelola siklus hidup secara manual.

## Terkait

  * [Otomatisasi](</id/automation>) \- semua mekanisme otomatisasi sekilas
  * [CLI: Tugas](</id/cli/tasks>) \- referensi perintah CLI
  * [Heartbeat](</id/gateway/heartbeat>) \- giliran sesi utama berkala
  * [Tugas Terjadwal](</id/automation/cron-jobs>) \- menjadwalkan pekerjaan latar belakang
  * [Task Flow](</id/automation/taskflow>) \- orkestrasi flow di atas tugas


Was this useful?YesNo