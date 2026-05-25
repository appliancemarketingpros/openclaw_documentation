---
title: Reset
source_url: https://docs.openclaw.ai/id/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Reset config/status lokal (CLI tetap terpasang).

Opsi:

  * `--scope <scope>`: `config`, `config+creds+sessions`, atau `full`
  * `--yes`: lewati prompt konfirmasi
  * `--non-interactive`: nonaktifkan prompt; memerlukan `--scope` dan `--yes`
  * `--dry-run`: cetak tindakan tanpa menghapus file


Contoh:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Catatan:

  * Jalankan `openclaw backup create` terlebih dahulu jika Anda menginginkan snapshot yang dapat dipulihkan sebelum menghapus status lokal.
  * Jika Anda tidak memberikan `--scope`, `openclaw reset` menggunakan prompt interaktif untuk memilih apa yang akan dihapus.
  * `--non-interactive` hanya valid saat `--scope` dan `--yes` sama-sama diatur.


## Terkait

  * [Referensi CLI](</id/cli>)


Was this useful?YesNo