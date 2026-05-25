---
title: Perbarui
source_url: https://docs.openclaw.ai/id/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Perbarui OpenClaw dengan aman dan beralih antara kanal stable/beta/dev.

Jika Anda menginstal melalui **npm/pnpm/bun** (instalasi global, tanpa metadata git), pembaruan terjadi melalui alur pengelola paket di [Memperbarui](</id/install/updating>).

## Penggunaan

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opsi

  * `--no-restart`: lewati restart layanan Gateway setelah pembaruan berhasil. Pembaruan pengelola paket yang me-restart Gateway memverifikasi bahwa layanan yang direstart melaporkan versi terbaru yang diharapkan sebelum perintah berhasil.
  * `--channel <stable|beta|dev>`: tetapkan kanal pembaruan (git + npm; disimpan dalam konfigurasi).
  * `--tag <dist-tag|version|spec>`: timpa target paket hanya untuk pembaruan ini. Untuk instalasi paket, `main` dipetakan ke `github:openclaw/openclaw#main`.
  * `--dry-run`: pratinjau tindakan pembaruan yang direncanakan (alur kanal/tag/target/restart) tanpa menulis konfigurasi, menginstal, menyinkronkan plugin, atau me-restart.
  * `--json`: cetak JSON `UpdateRunResult` yang dapat dibaca mesin, termasuk `postUpdate.plugins.warnings` saat plugin terkelola yang rusak atau tidak dapat dimuat perlu diperbaiki setelah pembaruan core berhasil, detail fallback plugin kanal beta saat plugin tidak memiliki rilis beta, dan `postUpdate.plugins.integrityDrifts` saat drift artefak plugin npm terdeteksi selama sinkronisasi plugin pascapembaruan.
  * `--timeout <seconds>`: timeout per langkah (default 1800 dtk).
  * `--yes`: lewati prompt konfirmasi (misalnya konfirmasi downgrade).


`openclaw update` tidak memiliki flag `--verbose`. Gunakan `--dry-run` untuk mempratinjau tindakan kanal/tag/instal/restart yang direncanakan, `--json` untuk hasil yang dapat dibaca mesin, dan `openclaw update status --json` saat Anda hanya memerlukan detail kanal dan ketersediaan. Jika Anda men-debug log Gateway seputar pembaruan, verbosity konsol dan level log file terpisah: Gateway `--verbose` memengaruhi output terminal/WebSocket, sementara log file memerlukan `logging.level: "debug"` atau `"trace"` dalam konfigurasi. Lihat [logging Gateway](</id/gateway/logging>).

## `update status`

Tampilkan kanal pembaruan aktif + tag/branch/SHA git (untuk checkout sumber), ditambah ketersediaan pembaruan.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opsi:

  * `--json`: cetak JSON status yang dapat dibaca mesin.
  * `--timeout <seconds>`: timeout untuk pemeriksaan (default 3 dtk).


## `update wizard`

Alur interaktif untuk memilih kanal pembaruan dan mengonfirmasi apakah akan me-restart Gateway setelah memperbarui (default-nya adalah restart). Jika Anda memilih `dev` tanpa checkout git, alur ini menawarkan untuk membuatnya.

Opsi:

  * `--timeout <seconds>`: timeout untuk setiap langkah pembaruan (default `1800`)


## Yang dilakukan

Saat Anda beralih kanal secara eksplisit (`--channel ...`), OpenClaw juga menjaga metode instalasi tetap selaras:

  * `dev` → memastikan ada checkout git (default: `~/openclaw`, timpa dengan `OPENCLAW_GIT_DIR`), memperbaruinya, dan menginstal CLI global dari checkout tersebut.
  * `stable` → menginstal dari npm menggunakan `latest`.
  * `beta` → mengutamakan dist-tag npm `beta`, tetapi fallback ke `latest` saat beta hilang atau lebih lama daripada rilis stable saat ini.


Auto-updater core Gateway (saat diaktifkan melalui konfigurasi) meluncurkan jalur pembaruan CLI di luar handler permintaan Gateway yang sedang berjalan. Pembaruan pengelola paket control-plane `update.run` memaksa restart pembaruan tanpa penundaan dan tanpa cooldown setelah pertukaran paket, karena proses Gateway lama mungkin masih memiliki chunk dalam memori yang menunjuk ke file yang dihapus oleh paket baru.

Untuk instalasi pengelola paket, `openclaw update` menyelesaikan versi paket target sebelum memanggil pengelola paket. Instalasi global npm menggunakan instalasi bertahap: OpenClaw menginstal paket baru ke prefix npm sementara, memverifikasi inventaris `dist` yang dipaketkan di sana, lalu menukar pohon paket bersih tersebut ke prefix global yang sebenarnya. Jika verifikasi gagal, doctor pascapembaruan, sinkronisasi plugin, dan pekerjaan restart tidak berjalan dari pohon yang dicurigai. Bahkan saat versi terinstal sudah cocok dengan target, perintah menyegarkan instalasi paket global, lalu menjalankan sinkronisasi plugin, penyegaran penyelesaian perintah core, dan pekerjaan restart. Ini menjaga sidecar yang dipaketkan dan record plugin milik kanal tetap selaras dengan build OpenClaw yang terinstal sekaligus menyerahkan pembangunan ulang penyelesaian perintah plugin penuh ke eksekusi eksplisit `openclaw completion --write-state`.

Saat layanan Gateway terkelola lokal terinstal dan restart diaktifkan, pembaruan pengelola paket menghentikan layanan yang berjalan sebelum mengganti pohon paket, lalu menyegarkan metadata layanan dari instalasi yang diperbarui, me-restart layanan, dan memverifikasi Gateway yang direstart melaporkan versi yang diharapkan sebelum melaporkan keberhasilan. Di macOS, pemeriksaan pascapembaruan juga memverifikasi bahwa LaunchAgent dimuat/berjalan untuk profil aktif dan port loopback yang dikonfigurasi sehat. Jika plist terinstal tetapi launchd tidak mengawasinya, OpenClaw melakukan bootstrap ulang LaunchAgent secara otomatis, lalu menjalankan ulang pemeriksaan kesiapan kesehatan/versi/kanal. Bootstrap baru memuat job RunAtLoad secara langsung, sehingga pemulihan pembaruan tidak langsung menjalankan `kickstart -k` pada Gateway yang baru dimunculkan. Jika Gateway masih tidak menjadi sehat, perintah keluar non-zero dan mencetak path log restart serta instruksi restart, instal ulang, dan rollback paket yang eksplisit. Dengan `--no-restart`, penggantian paket tetap berjalan tetapi layanan terkelola tidak dihentikan atau direstart, sehingga Gateway yang berjalan mungkin tetap menggunakan kode lama hingga Anda me-restart-nya secara manual.

## Alur checkout git

### Pemilihan kanal

  * `stable`: checkout tag non-beta terbaru, lalu build dan doctor.
  * `beta`: utamakan tag `-beta` terbaru, tetapi fallback ke tag stable terbaru saat beta hilang atau lebih lama.
  * `dev`: checkout `main`, lalu fetch dan rebase.


### Langkah pembaruan

* ### Verifikasi worktree bersih

Memerlukan tidak ada perubahan yang belum di-commit.

* ### Beralih kanal

Beralih ke kanal yang dipilih (tag atau branch).

* ### Fetch upstream

Khusus dev.

* ### Build preflight (khusus dev)

Menjalankan build TypeScript di worktree sementara. Jika tip gagal, mundur hingga 10 commit untuk menemukan commit terbaru yang dapat di-build. Tetapkan `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` untuk juga menjalankan lint selama preflight ini; lint berjalan dalam mode serial terbatas karena host pembaruan pengguna sering kali lebih kecil daripada runner CI.

* ### Rebase

Melakukan rebase ke commit yang dipilih (khusus dev).

* ### Instal dependensi

Menggunakan pengelola paket repo. Untuk checkout pnpm, updater melakukan bootstrap `pnpm` sesuai kebutuhan (melalui `corepack` terlebih dahulu, lalu fallback sementara `npm install pnpm@11`) alih-alih menjalankan `npm run build` di dalam workspace pnpm.

* ### Build Control UI

Mem-build gateway dan Control UI.

* ### Jalankan doctor

`openclaw doctor` berjalan sebagai pemeriksaan pembaruan aman terakhir.

* ### Sinkronkan plugin

Menyinkronkan plugin ke kanal aktif. Dev menggunakan plugin yang dibundel; stable dan beta menggunakan npm. Memperbarui instalasi plugin yang dilacak.

Pada kanal pembaruan beta, instalasi plugin npm dan ClawHub yang dilacak yang mengikuti baris default/latest mencoba rilis plugin `@beta` terlebih dahulu. Jika plugin tidak memiliki rilis beta, OpenClaw fallback ke spec default/latest yang direkam dan melaporkan hal itu sebagai peringatan. Untuk plugin npm, OpenClaw juga fallback saat paket beta ada tetapi gagal validasi instalasi. Peringatan fallback plugin ini tidak membuat pembaruan core gagal. Versi persis dan tag eksplisit tidak ditulis ulang.

## Singkatan `--update`

`openclaw --update` ditulis ulang menjadi `openclaw update` (berguna untuk shell dan skrip launcher).

## Terkait

  * `openclaw doctor` (menawarkan untuk menjalankan update terlebih dahulu pada checkout git)
  * [Kanal pengembangan](</id/install/development-channels>)
  * [Memperbarui](</id/install/updating>)
  * [Referensi CLI](</id/cli>)


Was this useful?YesNo