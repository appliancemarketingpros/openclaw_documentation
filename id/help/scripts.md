---
title: Skrip
source_url: https://docs.openclaw.ai/id/help/scripts
scraped_at: 2026-05-25
---

Direktori `scripts/` berisi skrip pembantu untuk alur kerja lokal dan tugas operasional. Gunakan ini saat sebuah tugas jelas terkait dengan skrip; jika tidak, utamakan CLI.

## Konvensi

  * Skrip bersifat **opsional** kecuali dirujuk dalam dokumentasi atau checklist rilis.
  * Utamakan permukaan CLI saat tersedia (contoh: pemantauan autentikasi menggunakan `openclaw models status --check`).
  * Anggap skrip bersifat spesifik host; baca sebelum menjalankannya di mesin baru.


## Skrip pemantauan autentikasi

Pemantauan autentikasi dibahas di [Autentikasi](</id/gateway/authentication>). Skrip di bawah `scripts/` adalah tambahan opsional untuk alur kerja ponsel systemd/Termux.

## Pembantu baca GitHub

Gunakan `scripts/gh-read` saat Anda ingin `gh` menggunakan token instalasi GitHub App untuk panggilan baca yang dicakup repo sambil membiarkan `gh` normal tetap memakai login pribadi Anda untuk tindakan tulis.

Env wajib:

  * `OPENCLAW_GH_READ_APP_ID`
  * `OPENCLAW_GH_READ_PRIVATE_KEY_FILE`


Env opsional:

  * `OPENCLAW_GH_READ_INSTALLATION_ID` saat Anda ingin melewati pencarian instalasi berbasis repo
  * `OPENCLAW_GH_READ_PERMISSIONS` sebagai override yang dipisahkan koma untuk subset izin baca yang akan diminta


Urutan resolusi repo:

  * `gh ... -R owner/repo`
  * `GH_REPO`
  * `git remote origin`


Contoh:

  * `scripts/gh-read pr view 123`
  * `scripts/gh-read run list -R openclaw/openclaw`
  * `scripts/gh-read api repos/openclaw/openclaw/pulls/123`


## Saat menambahkan skrip

  * Jaga agar skrip tetap terfokus dan terdokumentasi.
  * Tambahkan entri singkat di dokumen yang relevan (atau buat satu jika belum ada).


## Terkait

  * [Pengujian](</id/help/testing>)
  * [Pengujian langsung](</id/help/testing-live>)


Was this useful?YesNo