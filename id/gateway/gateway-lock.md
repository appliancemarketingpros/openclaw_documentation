---
title: Penguncian Gateway
source_url: https://docs.openclaw.ai/id/gateway/gateway-lock
scraped_at: 2026-05-25
---

## Mengapa

  * Memastikan hanya satu instance Gateway berjalan per port dasar pada host yang sama; Gateway tambahan harus menggunakan profil terisolasi dan port unik.
  * Tetap pulih dari crash/SIGKILL tanpa meninggalkan berkas kunci yang basi.
  * Gagal cepat dengan error yang jelas ketika port kontrol sudah dipakai.


## Mekanisme

  * Gateway terlebih dahulu memperoleh berkas kunci per-konfigurasi di bawah direktori kunci status dan memeriksa port yang dikonfigurasi untuk listener yang sudah ada.
  * Jika pemilik kunci yang tercatat sudah tidak ada, port kosong, atau kunci basi, startup mengambil alih kembali kunci dan melanjutkan.
  * Gateway kemudian mengikat listener HTTP/WebSocket (default `ws://127.0.0.1:18789`) menggunakan listener TCP eksklusif.
  * Jika bind gagal dengan `EADDRINUSE`, startup melempar `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * Saat shutdown, Gateway menutup server HTTP/WebSocket dan menghapus berkas kunci.


## Permukaan error

  * Jika proses lain memegang port, startup melempar `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * Kegagalan bind lainnya muncul sebagai `GatewayLockError("failed to bind gateway socket on ws://127.0.0.1:<port>: …")`.


## Catatan operasional

  * Jika port ditempati oleh proses _lain_ , error-nya sama; kosongkan port atau pilih yang lain dengan `openclaw gateway --port <port>`.
  * Di bawah supervisor layanan, proses Gateway baru yang melihat responder `/healthz` sehat yang sudah ada membiarkan proses tersebut tetap memegang kontrol. Pada systemd, starter duplikat keluar dengan kode 78 sehingga default `RestartPreventExitStatus=78` menghentikan `Restart=always` agar tidak berulang karena konflik kunci atau `EADDRINUSE`. Jika proses yang sudah ada tidak pernah menjadi sehat, percobaan ulang dibatasi dan startup gagal dengan error kunci yang jelas alih-alih berulang selamanya.
  * Aplikasi macOS tetap mempertahankan guard PID ringan miliknya sendiri sebelum menelurkan Gateway; kunci runtime diterapkan oleh berkas kunci plus bind HTTP/WebSocket.


## Terkait

  * [Beberapa Gateway](</id/gateway/multiple-gateways>) — menjalankan beberapa instance dengan port unik
  * [Pemecahan Masalah](</id/gateway/troubleshooting>) — mendiagnosis `EADDRINUSE` dan konflik port


Was this useful?YesNo