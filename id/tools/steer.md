---
title: Arahkan
source_url: https://docs.openclaw.ai/id/tools/steer
scraped_at: 2026-05-25
---

`/steer` mengirim panduan ke eksekusi yang sudah aktif. Ini untuk momen "sesuaikan eksekusi ini saat masih bekerja", bukan untuk memulai giliran baru.

## Sesi saat ini

Gunakan `/steer` tingkat atas untuk menargetkan eksekusi aktif untuk sesi saat ini:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Perilaku:

  * Hanya menargetkan eksekusi aktif sesi saat ini.
  * Bekerja secara independen dari mode `/queue` sesi.
  * Tidak memulai eksekusi baru ketika sesi sedang menganggur.
  * Membalas dengan peringatan ketika tidak ada eksekusi aktif untuk diarahkan.
  * Menggunakan jalur pengarahan runtime aktif, sehingga model melihat panduan pada batas runtime berikutnya yang didukung.


## Pengarahan vs antrean

`/queue steer` mengubah perilaku pesan masuk normal ketika pesan tersebut tiba saat eksekusi sedang aktif. `/steer <message>` adalah perintah eksplisit yang mencoba menyuntikkan pesan perintah tersebut ke eksekusi aktif pada batas runtime berikutnya yang didukung, terlepas dari pengaturan `/queue` yang tersimpan.

Gunakan:

  * `/steer <message>` ketika Anda ingin memandu eksekusi aktif sekarang.
  * `/queue steer` ketika Anda ingin pesan normal berikutnya mengarahkan eksekusi aktif secara default.
  * `/queue collect` atau `/queue followup` ketika pesan baru harus menunggu giliran berikutnya alih-alih mengarahkan eksekusi aktif.


Untuk mode antrean dan perilaku fallback, lihat [Antrean perintah](</id/concepts/queue>) dan [Antrean pengarahan](</id/concepts/queue-steering>).

## Sub-agen

Gunakan `/subagents steer` ketika targetnya adalah eksekusi anak:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` tingkat atas tidak memilih sub-agen berdasarkan id atau indeks daftar. Perintah ini selalu menargetkan eksekusi aktif sesi saat ini. Lihat [Sub-agen](</id/tools/subagents>) untuk id, label, dan perintah kontrol sub-agen.

## Sesi ACP

Gunakan `/acp steer` ketika targetnya adalah sesi harness ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Lihat [Agen ACP](</id/tools/acp-agents>) untuk pemilihan sesi ACP dan perilaku runtime.

## Terkait

  * [Perintah slash](</id/tools/slash-commands>)
  * [Antrean perintah](</id/concepts/queue>)
  * [Antrean pengarahan](</id/concepts/queue-steering>)
  * [Sub-agen](</id/tools/subagents>)


Was this useful?YesNo