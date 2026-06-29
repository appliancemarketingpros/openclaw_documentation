---
title: CLI Transkrip
source_url: https://docs.openclaw.ai/id/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

Periksa transkrip yang ditulis oleh alat inti `transcripts` OpenClaw. CLI ini bersifat hanya-baca; penangkapan, impor, dan peringkasan dimiliki oleh alat agen dan sumber mulai-otomatis yang dikonfigurasi.

Gunakan CLI saat Anda ingin menemukan catatan kemarin, membuka file Markdown di editor, memasukkan transkrip ke alat lain, atau men-debug lokasi sesi tersimpan di disk. Ini tidak memulai atau menghentikan penangkapan.

Artefak berada di bawah direktori status OpenClaw:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

Direktori status default adalah `~/.openclaw`; atur `OPENCLAW_STATE_DIR` untuk menggunakan direktori lain. Direktori tanggal berasal dari waktu mulai sesi, dan direktori sesi adalah segmen sistem file aman yang diturunkan dari id sesi.

## Perintah

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: mencantumkan sesi yang tersimpan, pemilih berkualifikasi tanggal, waktu mulai, judul, dan path `summary.md`.
  * `show <session>`: mencetak `summary.md` yang tersimpan.
  * `path <session>`: mencetak path `summary.md`.
  * `path <session> --dir`: mencetak direktori sesi.
  * `path <session> --metadata`: mencetak `metadata.json`.
  * `path <session> --transcript`: mencetak `transcript.jsonl`.
  * `--json`: mencetak output yang dapat dibaca mesin.


Saat id sesi manusia berulang di beberapa hari, gunakan pemilih berkualifikasi tanggal dari `list`, misalnya `openclaw transcripts show 2026-05-22/standup`. Id sesi default menyertakan timestamp dan sufiks acak; konfigurasikan id sesi tetap hanya saat id tersebut unik dalam satu hari.

## Output

`list` mencetak satu sesi per baris:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

Output dipisahkan dengan tab. Kolomnya adalah pemilih, waktu mulai, judul, dan path ringkasan. Pemilih adalah nilai paling aman untuk diteruskan kembali ke `show` atau `path`.

`list --json` mencetak objek dengan:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` mengembalikan metadata sesi yang tersimpan, pemilih, direktori sesi, path ringkasan, dan teks Markdown ringkasan. `path --json` mengembalikan path yang dipilih dan apakah file tersebut ada.

## Banyak rapat per hari

Transkrip mengelompokkan sesi berdasarkan tanggal, lalu berdasarkan id sesi. Sepuluh rapat dalam satu hari menjadi sepuluh folder sejajar:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

Gunakan id default yang dihasilkan untuk sebagian besar otomatisasi. Gunakan id tetap seperti `standup` hanya saat id yang sama tidak akan digunakan dua kali pada tanggal yang sama.

## Ringkasan hilang

Sesi langsung menulis `summary.md` saat sesi berhenti. Transkrip yang diimpor menulis `summary.md` segera setelah impor. Sesi tetap dapat muncul di `list` tanpa ringkasan saat penangkapan aktif, provider gagal saat berhenti, atau metadata ditulis sebelum ada ujaran yang masuk.

Gunakan `path <session> --transcript` untuk memeriksa transkrip append-only, dan gunakan aksi alat `transcripts` `summarize` untuk membuat ulang ringkasan Markdown.

## Konfigurasi

Penangkapan transkrip bersifat opt-in karena sumber langsung dapat bergabung dan merekam audio rapat. Aktifkan alat dengan `transcripts.enabled` tingkat atas:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

Konfigurasikan sumber mulai-otomatis dengan `transcripts.autoStart` di `openclaw.json`. Setiap entri diaktifkan dengan keberadaannya; hilangkan entri untuk menonaktifkan sumber tersebut.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue