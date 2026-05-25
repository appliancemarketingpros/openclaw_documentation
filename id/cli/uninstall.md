---
title: Uninstall
source_url: https://docs.openclaw.ai/id/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Copot layanan gateway + data lokal (CLI tetap ada).

Opsi:

  * `--service`: hapus layanan gateway
  * `--state`: hapus status dan config
  * `--workspace`: hapus direktori workspace
  * `--app`: hapus aplikasi macOS
  * `--all`: hapus layanan, status, workspace, dan aplikasi
  * `--yes`: lewati prompt konfirmasi
  * `--non-interactive`: nonaktifkan prompt; memerlukan `--yes`
  * `--dry-run`: cetak tindakan tanpa menghapus file


Contoh:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Catatan:

  * Jalankan `openclaw backup create` terlebih dahulu jika Anda menginginkan snapshot yang dapat dipulihkan sebelum menghapus status atau workspace.
  * `--all` adalah singkatan untuk menghapus layanan, status, workspace, dan aplikasi sekaligus.
  * `--non-interactive` memerlukan `--yes`.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Uninstall](</id/install/uninstall>)


Was this useful?YesNo