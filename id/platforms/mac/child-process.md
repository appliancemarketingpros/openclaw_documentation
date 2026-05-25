---
title: Siklus hidup Gateway di macOS
source_url: https://docs.openclaw.ai/id/platforms/mac/child-process
scraped_at: 2026-05-25
---

Aplikasi macOS **mengelola Gateway melalui launchd** secara default dan tidak menjalankan Gateway sebagai proses anak. Aplikasi pertama-tama mencoba terhubung ke Gateway yang sudah berjalan pada port yang dikonfigurasi; jika tidak ada yang dapat dijangkau, aplikasi mengaktifkan layanan launchd melalui CLI `openclaw` eksternal (tanpa runtime tertanam). Ini memberi Anda mulai otomatis yang andal saat masuk dan mulai ulang saat terjadi kegagalan.

Mode proses anak (Gateway dijalankan langsung oleh aplikasi) **tidak digunakan** saat ini. Jika Anda memerlukan keterikatan yang lebih erat dengan UI, jalankan Gateway secara manual di terminal.

## Perilaku default (launchd)

  * Aplikasi memasang LaunchAgent per pengguna berlabel `ai.openclaw.gateway` (atau `ai.openclaw.<profile>` saat menggunakan `--profile`/`OPENCLAW_PROFILE`; `com.openclaw.*` lama didukung).
  * Saat mode Lokal diaktifkan, aplikasi memastikan LaunchAgent dimuat dan memulai Gateway jika diperlukan.
  * Log ditulis ke jalur log Gateway launchd (terlihat di Pengaturan Debug).


Perintah umum:

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.gatewaylaunchctl bootout gui/$UID/ai.openclaw.gateway
[/code]

Ganti label dengan `ai.openclaw.<profile>` saat menjalankan profil bernama.

## Build dev tanpa tanda tangan

`scripts/restart-mac.sh --no-sign` ditujukan untuk build lokal cepat saat Anda tidak memiliki kunci penandatanganan. Untuk mencegah launchd mengarah ke biner relay tanpa tanda tangan, perintah ini:

  * Menulis `~/.openclaw/disable-launchagent`.


Jalankan bertanda tangan dari `scripts/restart-mac.sh` akan menghapus pengesampingan ini jika marker ada. Untuk mengatur ulang secara manual:

bashCopy code
[code]
    rm ~/.openclaw/disable-launchagent
[/code]

## Mode hanya terhubung

Untuk memaksa aplikasi macOS **tidak pernah memasang atau mengelola launchd** , jalankan dengan `--attach-only` (atau `--no-launchd`). Ini menyetel `~/.openclaw/disable-launchagent`, sehingga aplikasi hanya terhubung ke Gateway yang sudah berjalan. Anda dapat mengaktifkan perilaku yang sama di Pengaturan Debug.

## Mode jarak jauh

Mode jarak jauh tidak pernah memulai Gateway lokal. Aplikasi menggunakan tunnel SSH ke host jarak jauh dan terhubung melalui tunnel tersebut.

## Mengapa kami memilih launchd

  * Mulai otomatis saat masuk.
  * Semantik mulai ulang/KeepAlive bawaan.
  * Log dan supervisi yang dapat diprediksi.


Jika mode proses anak yang sebenarnya diperlukan lagi, mode tersebut harus didokumentasikan sebagai mode khusus pengembangan yang terpisah dan eksplisit.

## Terkait

  * [aplikasi macOS](</id/platforms/macos>)
  * [Runbook Gateway](</id/gateway>)


Was this useful?YesNo