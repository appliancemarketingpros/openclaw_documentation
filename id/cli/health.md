---
title: Kesehatan
source_url: https://docs.openclaw.ai/id/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Mengambil status kesehatan dari Gateway yang sedang berjalan.

## Opsi

Flag | Bawaan | Deskripsi  
---|---|---  
`--json` | `false` | Mencetak JSON yang dapat dibaca mesin, bukan teks.  
`--timeout <ms>` | `10000` | Tenggat waktu koneksi dalam milidetik.  
`--verbose` | `false` | Pencatatan log verbose. Memaksa probe langsung dan memperluas output per agen.  
`--debug` | `false` | Alias untuk `--verbose`.  
  
Contoh:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Catatan:

  * `openclaw health` bawaan meminta snapshot kesehatan dari gateway yang sedang berjalan. Ketika gateway sudah memiliki snapshot cache yang masih segar, perintah ini dapat mengembalikan payload cache tersebut dan menyegarkan di latar belakang.
  * `--verbose` memaksa probe langsung, mencetak detail koneksi gateway, dan memperluas output yang dapat dibaca manusia di semua akun dan agen yang dikonfigurasi.
  * Output mencakup penyimpanan sesi per agen ketika beberapa agen dikonfigurasi.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Kesehatan Gateway](</id/gateway/health>)


Was this useful?YesNo