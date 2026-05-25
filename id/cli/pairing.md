---
title: Penyandingan
source_url: https://docs.openclaw.ai/id/cli/pairing
scraped_at: 2026-05-25
---

# `openclaw pairing`

Setujui atau periksa permintaan pemasangan melalui pesan langsung (untuk saluran yang mendukung pemasangan).

Terkait:

  * Alur pemasangan: [Pemasangan](</id/channels/pairing>)


## Perintah

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing list --channel telegram --account workopenclaw pairing list telegram --json openclaw pairing approve <code>openclaw pairing approve telegram <code>openclaw pairing approve --channel telegram --account work <code> --notify
[/code]

## `pairing list`

Cantumkan permintaan pemasangan yang tertunda untuk satu saluran.

Opsi:

  * `[channel]`: id saluran posisional
  * `--channel <channel>`: id saluran eksplisit
  * `--account <accountId>`: id akun untuk saluran multi-akun
  * `--json`: keluaran yang dapat dibaca mesin


Catatan:

  * Jika beberapa saluran yang mendukung pemasangan dikonfigurasi, Anda harus menyediakan saluran baik secara posisional maupun dengan `--channel`.
  * Saluran ekstensi diizinkan selama id saluran valid.


## `pairing approve`

Setujui kode pemasangan yang tertunda dan izinkan pengirim tersebut.

Penggunaan:

  * `openclaw pairing approve <channel> <code>`
  * `openclaw pairing approve --channel <channel> <code>`
  * `openclaw pairing approve <code>` ketika tepat satu saluran yang mendukung pemasangan dikonfigurasi


Opsi:

  * `--channel <channel>`: id saluran eksplisit
  * `--account <accountId>`: id akun untuk saluran multi-akun
  * `--notify`: kirim konfirmasi kembali kepada pemohon di saluran yang sama


Bootstrap pemilik:

  * Jika `commands.ownerAllowFrom` kosong saat Anda menyetujui kode pemasangan, OpenClaw juga mencatat pengirim yang disetujui sebagai pemilik perintah, menggunakan entri berbasis cakupan saluran seperti `telegram:123456789`.
  * Ini hanya melakukan bootstrap pemilik pertama. Persetujuan pemasangan berikutnya tidak mengganti atau memperluas `commands.ownerAllowFrom`.
  * Pemilik perintah adalah akun operator manusia yang diizinkan menjalankan perintah khusus pemilik dan menyetujui tindakan berbahaya seperti `/diagnostics`, `/export-trajectory`, `/config`, dan persetujuan eksekusi.


## Catatan

  * Input saluran: berikan secara posisional (`pairing list telegram`) atau dengan `--channel <channel>`.
  * `pairing list` mendukung `--account <accountId>` untuk saluran multi-akun.
  * `pairing approve` mendukung `--account <accountId>` dan `--notify`.
  * Jika hanya satu saluran yang mendukung pemasangan dikonfigurasi, `pairing approve <code>` diizinkan.
  * Jika Anda menyetujui pengirim sebelum bootstrap ini ada, jalankan `openclaw doctor`; perintah ini memperingatkan ketika tidak ada pemilik perintah yang dikonfigurasi dan menampilkan perintah `openclaw config set commands.ownerAllowFrom ...` untuk memperbaikinya.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Pemasangan saluran](</id/channels/pairing>)


Was this useful?YesNo