---
title: Flag diagnostik
source_url: https://docs.openclaw.ai/id/diagnostics/flags
scraped_at: 2026-05-25
---

Flag diagnostik memungkinkan Anda mengaktifkan log debug yang ditargetkan tanpa menyalakan logging verbose di semua tempat. Flag bersifat opt-in dan tidak berpengaruh kecuali suatu subsistem memeriksanya.

## Cara kerjanya

  * Flag adalah string (tidak peka huruf besar/kecil).
  * Anda dapat mengaktifkan flag di konfigurasi atau melalui override env.
  * Wildcard didukung: 
    * `telegram.*` cocok dengan `telegram.http`
    * `*` mengaktifkan semua flag


## Aktifkan melalui konfigurasi

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Beberapa flag:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Mulai ulang gateway setelah mengubah flag.

## Override env (sekali pakai)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Nonaktifkan semua flag:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Artefak linimasa

Flag `timeline` menulis peristiwa waktu startup dan runtime terstruktur untuk harness QA eksternal:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Anda juga dapat mengaktifkannya di konfigurasi:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Jalur file linimasa tetap berasal dari `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Ketika `timeline` hanya diaktifkan dari konfigurasi, span pemuatan konfigurasi paling awal tidak dipancarkan karena OpenClaw belum membaca konfigurasi; span startup berikutnya menggunakan flag konfigurasi.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all`, dan `OPENCLAW_DIAGNOSTICS=*` juga mengaktifkan linimasa karena semuanya mengaktifkan setiap flag diagnostik. Pilih `timeline` jika Anda hanya menginginkan artefak waktu JSONL.

Catatan linimasa menggunakan envelope `openclaw.diagnostics.v1`. Peristiwa dapat menyertakan ID proses, nama fase, nama span, durasi, ID Plugin, jumlah dependensi, sampel penundaan event-loop, nama operasi penyedia, status keluar proses anak, dan nama/pesan kesalahan startup. Perlakukan file linimasa sebagai artefak diagnostik lokal; tinjau sebelum membagikannya ke luar mesin Anda.

## Lokasi log

Flag memancarkan log ke file log diagnostik standar. Secara default:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Jika Anda mengatur `logging.file`, gunakan jalur tersebut sebagai gantinya. Log adalah JSONL (satu objek JSON per baris). Redaksi tetap diterapkan berdasarkan `logging.redactSensitive`.

## Ekstrak log

Pilih file log terbaru:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filter untuk diagnostik HTTP Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filter untuk diagnostik HTTP Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Atau tail saat mereproduksi:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Untuk Gateway jarak jauh, Anda juga dapat menggunakan `openclaw logs --follow` (lihat [/cli/logs](</id/cli/logs>)).

## Catatan

  * Jika `logging.level` diatur lebih tinggi dari `warn`, log ini mungkin ditekan. Default `info` sudah memadai.
  * `brave.http` mencatat URL/parameter kueri permintaan Brave Search, status/waktu respons, dan peristiwa cache hit/miss/write. Ini tidak mencatat kunci API atau isi respons, tetapi kueri pencarian dapat bersifat sensitif.
  * Flag aman dibiarkan aktif; flag hanya memengaruhi volume log untuk subsistem tertentu.
  * Gunakan [/logging](</id/logging>) untuk mengubah tujuan, level, dan redaksi log.


## Terkait

  * [Diagnostik Gateway](</id/gateway/diagnostics>)
  * [Pemecahan masalah Gateway](</id/gateway/troubleshooting>)


Was this useful?YesNo