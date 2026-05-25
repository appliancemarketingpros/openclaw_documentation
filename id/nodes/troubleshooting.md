---
title: Pemecahan masalah Node
source_url: https://docs.openclaw.ai/id/nodes/troubleshooting
scraped_at: 2026-05-25
---

Gunakan halaman ini saat sebuah Node terlihat di status tetapi alat Node gagal.

## Urutan perintah

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

Lalu jalankan pemeriksaan khusus Node:

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>
[/code]

Sinyal sehat:

  * Node terhubung dan dipasangkan untuk peran `node`.
  * `nodes describe` mencakup kapabilitas yang Anda panggil.
  * Persetujuan exec menampilkan mode/daftar izin yang diharapkan.


## Persyaratan latar depan

`canvas.*`, `camera.*`, dan `screen.*` hanya dapat berjalan di latar depan pada Node iOS/Android.

Pemeriksaan dan perbaikan cepat:

bashCopy code
[code]
    openclaw nodes describe --node <idOrNameOrIp>openclaw nodes canvas snapshot --node <idOrNameOrIp>openclaw logs --follow
[/code]

Jika Anda melihat `NODE_BACKGROUND_UNAVAILABLE`, bawa aplikasi Node ke latar depan dan coba lagi.

## Matriks izin

Kapabilitas | iOS | Android | aplikasi Node macOS | Kode kegagalan umum  
---|---|---|---|---  
`camera.snap`, `camera.clip` | Kamera (+ mikrofon untuk audio klip) | Kamera (+ mikrofon untuk audio klip) | Kamera (+ mikrofon untuk audio klip) | `*_PERMISSION_REQUIRED`  
`screen.record` | Perekaman Layar (+ mikrofon opsional) | Prompt tangkapan layar (+ mikrofon opsional) | Perekaman Layar | `*_PERMISSION_REQUIRED`  
`location.get` | Saat Menggunakan atau Selalu (bergantung mode) | Lokasi latar depan/latar belakang berdasarkan mode | Izin lokasi | `LOCATION_PERMISSION_REQUIRED`  
`system.run` | n/a (jalur host Node) | n/a (jalur host Node) | Persetujuan exec diperlukan | `SYSTEM_RUN_DENIED`  
  
## Pemasangan versus persetujuan

Ini adalah gerbang yang berbeda:

  1. **Pemasangan perangkat** : bisakah Node ini terhubung ke Gateway?
  2. **Kebijakan perintah Node Gateway** : apakah ID perintah RPC diizinkan oleh `gateway.nodes.allowCommands` / `denyCommands` dan default platform?
  3. **Persetujuan exec** : bisakah Node ini menjalankan perintah shell tertentu secara lokal?


Pemeriksaan cepat:

bashCopy code
[code]
    openclaw devices listopenclaw nodes statusopenclaw approvals get --node <idOrNameOrIp>openclaw approvals allowlist add --node <idOrNameOrIp> "/usr/bin/uname"
[/code]

Jika pemasangan belum ada, setujui perangkat Node terlebih dahulu. Jika `nodes describe` tidak memuat sebuah perintah, periksa kebijakan perintah Node Gateway dan apakah Node benar-benar mendeklarasikan perintah itu saat terhubung. Jika pemasangan baik-baik saja tetapi `system.run` gagal, perbaiki persetujuan exec/daftar izin pada Node tersebut.

Pemasangan Node adalah gerbang identitas/kepercayaan, bukan permukaan persetujuan per perintah. Untuk `system.run`, kebijakan per-Node berada di file persetujuan exec Node tersebut (`openclaw approvals get --node ...`), bukan di catatan pemasangan Gateway.

Untuk eksekusi `host=node` yang didukung persetujuan, Gateway juga mengikat eksekusi ke `systemRunPlan` kanonis yang telah disiapkan. Jika pemanggil berikutnya mengubah command/cwd atau metadata sesi sebelum eksekusi yang disetujui diteruskan, Gateway menolak eksekusi sebagai ketidakcocokan persetujuan alih-alih memercayai payload yang diedit.

## Kode kesalahan Node umum

  * `NODE_BACKGROUND_UNAVAILABLE` → aplikasi berada di latar belakang; bawa ke latar depan.
  * `CAMERA_DISABLED` → toggle kamera dinonaktifkan di pengaturan Node.
  * `*_PERMISSION_REQUIRED` → izin OS hilang/ditolak.
  * `LOCATION_DISABLED` → mode lokasi mati.
  * `LOCATION_PERMISSION_REQUIRED` → mode lokasi yang diminta belum diberikan.
  * `LOCATION_BACKGROUND_UNAVAILABLE` → aplikasi berada di latar belakang tetapi hanya izin Saat Menggunakan yang tersedia.
  * `SYSTEM_RUN_DENIED: approval required` → permintaan exec membutuhkan persetujuan eksplisit.
  * `SYSTEM_RUN_DENIED: allowlist miss` → perintah diblokir oleh mode daftar izin. Pada host Node Windows, bentuk pembungkus shell seperti `cmd.exe /c ...` diperlakukan sebagai ketidakcocokan daftar izin dalam mode daftar izin kecuali disetujui melalui alur tanya.


## Loop pemulihan cepat

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --follow
[/code]

Jika masih macet:

  * Setujui ulang pemasangan perangkat.
  * Buka ulang aplikasi Node (latar depan).
  * Berikan ulang izin OS.
  * Buat ulang/sesuaikan kebijakan persetujuan exec.


## Terkait

  * [Ringkasan Node](</id/nodes>)
  * [Node kamera](</id/nodes/camera>)
  * [Perintah lokasi](</id/nodes/location-command>)
  * [Persetujuan exec](</id/tools/exec-approvals>)
  * [Pemasangan Gateway](</id/gateway/pairing>)
  * [Pemecahan masalah Gateway](</id/gateway/troubleshooting>)
  * [Pemecahan masalah channel](</id/channels/troubleshooting>)


Was this useful?YesNo