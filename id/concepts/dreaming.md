---
title: Dreaming
source_url: https://docs.openclaw.ai/id/concepts/dreaming
scraped_at: 2026-05-25
---

Dreaming adalah sistem konsolidasi memori latar belakang di `memory-core`. Ini membantu OpenClaw memindahkan sinyal jangka pendek yang kuat ke memori tahan lama sambil menjaga prosesnya dapat dijelaskan dan ditinjau.

## Apa yang ditulis Dreaming

Dreaming menyimpan dua jenis keluaran:

  * **Status mesin** di `memory/.dreams/` (penyimpanan recall, sinyal fase, checkpoint ingestion, lock).
  * **Keluaran yang dapat dibaca manusia** di `DREAMS.md` (atau `dreams.md` yang sudah ada) dan file laporan fase opsional di bawah `memory/dreaming/<phase>/YYYY-MM-DD.md`.


Promosi jangka panjang tetap hanya menulis ke `MEMORY.md`.

## Model fase

Dreaming menggunakan tiga fase kooperatif:

Fase | Tujuan | Penulisan tahan lama  
---|---|---  
Light | Mengurutkan dan menyiapkan materi jangka pendek terbaru | Tidak  
Deep | Menilai dan mempromosikan kandidat tahan lama | Ya (`MEMORY.md`)  
REM | Merefleksikan tema dan ide berulang | Tidak  
  
Fase-fase ini adalah detail implementasi internal, bukan "mode" terpisah yang dikonfigurasi pengguna.

Fase Light

Fase Light menelan sinyal memori harian terbaru dan jejak recall, melakukan deduplikasi, lalu menyiapkan baris kandidat.

  * Membaca dari status recall jangka pendek, file memori harian terbaru, dan transkrip sesi yang telah direduksi saat tersedia.
  * Menulis blok `## Light Sleep` terkelola saat penyimpanan menyertakan keluaran inline.
  * Mencatat sinyal penguatan untuk pemeringkatan Deep berikutnya.
  * Tidak pernah menulis ke `MEMORY.md`.

Fase Deep

Fase Deep memutuskan apa yang menjadi memori jangka panjang.

  * Memeringkat kandidat menggunakan penilaian berbobot dan gerbang ambang.
  * Mengharuskan `minScore`, `minRecallCount`, dan `minUniqueQueries` lulus.
  * Merehidrasi cuplikan dari file harian live sebelum menulis, sehingga cuplikan usang/terhapus dilewati.
  * Menambahkan entri yang dipromosikan ke `MEMORY.md`.
  * Menulis ringkasan `## Deep Sleep` ke `DREAMS.md` dan secara opsional menulis `memory/dreaming/deep/YYYY-MM-DD.md`.

Fase REM

Fase REM mengekstrak pola dan sinyal reflektif.

  * Membangun ringkasan tema dan refleksi dari jejak jangka pendek terbaru.
  * Menulis blok `## REM Sleep` terkelola saat penyimpanan menyertakan keluaran inline.
  * Mencatat sinyal penguatan REM yang digunakan oleh pemeringkatan Deep.
  * Tidak pernah menulis ke `MEMORY.md`.


## Ingestion transkrip sesi

Dreaming dapat menelan transkrip sesi yang telah direduksi ke dalam korpus Dreaming. Saat transkrip tersedia, transkrip tersebut dimasukkan ke fase Light bersama sinyal memori harian dan jejak recall. Konten pribadi dan sensitif direduksi sebelum ingestion.

## Dream Diary

Dreaming juga menyimpan **Dream Diary** naratif di `DREAMS.md`. Setelah setiap fase memiliki materi yang cukup, `memory-core` menjalankan giliran subagent latar belakang best-effort dan menambahkan entri buku harian singkat. Ini menggunakan model runtime default kecuali `dreaming.model` dikonfigurasi. Jika model yang dikonfigurasi tidak tersedia, Dream Diary mencoba sekali lagi dengan model default sesi.

Ada juga jalur backfill historis grounded untuk pekerjaan peninjauan dan pemulihan:

Perintah backfill

  * `memory rem-harness --path ... --grounded` menampilkan pratinjau keluaran buku harian grounded dari catatan historis `YYYY-MM-DD.md`.
  * `memory rem-backfill --path ...` menulis entri buku harian grounded yang dapat dibalik ke `DREAMS.md`.
  * `memory rem-backfill --path ... --stage-short-term` menyiapkan kandidat tahan lama grounded ke penyimpanan bukti jangka pendek yang sama dengan yang sudah digunakan fase Deep normal.
  * `memory rem-backfill --rollback` dan `--rollback-short-term` menghapus artefak backfill yang disiapkan tersebut tanpa menyentuh entri buku harian biasa atau recall jangka pendek live.


UI Control mengekspos alur backfill/reset buku harian yang sama sehingga Anda dapat memeriksa hasil di scene Dreams sebelum memutuskan apakah kandidat grounded layak dipromosikan. Scene juga menampilkan jalur grounded yang berbeda sehingga Anda dapat melihat entri jangka pendek yang disiapkan mana yang berasal dari replay historis, item yang dipromosikan mana yang dipimpin grounded, dan menghapus hanya entri yang disiapkan khusus grounded tanpa menyentuh status jangka pendek live biasa.

## Sinyal pemeringkatan Deep

Pemeringkatan Deep menggunakan enam sinyal dasar berbobot plus penguatan fase:

Sinyal | Bobot | Deskripsi  
---|---|---  
Frekuensi | 0.24 | Berapa banyak sinyal jangka pendek yang dikumpulkan entri  
Relevansi | 0.30 | Kualitas retrieval rata-rata untuk entri  
Keragaman kueri | 0.15 | Konteks kueri/hari berbeda yang memunculkannya  
Keterkinian | 0.15 | Skor kesegaran dengan peluruhan waktu  
Konsolidasi | 0.10 | Kekuatan pengulangan multi-hari  
Kekayaan konseptual | 0.06 | Kepadatan tag konsep dari cuplikan/path  
  
Hit fase Light dan REM menambahkan boost kecil yang meluruh berdasarkan keterkinian dari `memory/.dreams/phase-signals.json`.

## Penjadwalan

Saat diaktifkan, `memory-core` mengelola otomatis satu tugas Cron untuk sweep Dreaming penuh. Setiap sweep menjalankan fase secara berurutan: Light → REM → Deep.

Sweep mencakup workspace runtime utama dan workspace agent yang dikonfigurasi, dengan deduplikasi berdasarkan path, sehingga fan-out workspace subagent tidak mengecualikan `DREAMS.md` dan status memori agent utama.

Perilaku cadence default:

Pengaturan | Default  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | model default  
  
## Mulai cepat

### Aktifkan Dreaming

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Cadence sweep kustom

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Perintah slash

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## Alur kerja CLI

### Pratinjau promosi / terapkan

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

`memory promote` manual menggunakan ambang fase Deep secara default kecuali ditimpa dengan flag CLI.

### Jelaskan promosi

Jelaskan mengapa kandidat tertentu akan atau tidak akan dipromosikan:

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### Pratinjau harness REM

Pratinjau refleksi REM, kebenaran kandidat, dan keluaran promosi Deep tanpa menulis apa pun:

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Default utama

Semua pengaturan berada di bawah `plugins.entries.memory-core.config.dreaming`.

Aktifkan atau nonaktifkan sweep Dreaming.

Cadence Cron untuk sweep Dreaming penuh.

Override model subagent Dream Diary opsional. Gunakan nilai `provider/model` kanonis saat juga menetapkan allowlist `allowedModels` subagent.

## UI Dreams

Saat diaktifkan, tab **Dreams** Gateway menampilkan:

  * status aktif Dreaming saat ini
  * status tingkat fase dan keberadaan sweep terkelola
  * jumlah jangka pendek, grounded, sinyal, dan dipromosikan-hari-ini
  * waktu run terjadwal berikutnya
  * jalur Scene grounded yang berbeda untuk entri replay historis yang disiapkan
  * pembaca Dream Diary yang dapat diperluas yang didukung oleh `doctor.memory.dreamDiary`


## Dreaming tidak pernah berjalan: status menunjukkan diblokir

Jika `openclaw memory status` melaporkan `Dreaming status: blocked`, Cron terkelola ada tetapi Heartbeat agent default tidak berjalan. Periksa bahwa Heartbeat diaktifkan untuk agent default dan targetnya bukan `none`, lalu jalankan `openclaw memory status --deep` lagi setelah interval Heartbeat berikutnya.

## Terkait

  * [Memori](</id/concepts/memory>)
  * [CLI memori](</id/cli/memory>)
  * [Referensi konfigurasi memori](</id/reference/memory-config>)
  * [Pencarian memori](</id/concepts/memory-search>)


Was this useful?YesNo