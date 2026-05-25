---
title: Orientasi (aplikasi macOS)
source_url: https://docs.openclaw.ai/id/start/onboarding
scraped_at: 2026-05-25
---

Dokumen ini menjelaskan alur penyiapan pertama kali yang **saat ini** berlaku. Tujuannya adalah pengalaman "hari 0" yang lancar: pilih lokasi Gateway berjalan, hubungkan autentikasi, jalankan wizard, dan biarkan agen melakukan bootstrap sendiri. Untuk gambaran umum tentang jalur onboarding, lihat [Gambaran Umum Onboarding](</id/start/onboarding-overview>).

* ### Setujui peringatan macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Setujui pencarian jaringan lokal

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Sambutan dan pemberitahuan keamanan

Baca pemberitahuan keamanan yang ditampilkan dan putuskan sesuai kebutuhan ![](/assets/macos-onboarding/03-security-notice.png)

Model kepercayaan keamanan:

  * Secara default, OpenClaw adalah agen pribadi: satu batas operator tepercaya.
  * Penyiapan bersama/multi-pengguna memerlukan penguncian (pisahkan batas kepercayaan, pertahankan akses alat seminimal mungkin, dan ikuti [Keamanan](</id/gateway/security>)).
  * Onboarding lokal kini secara default menetapkan konfigurasi baru ke `tools.profile: "coding"` sehingga penyiapan lokal baru tetap memiliki alat filesystem/runtime tanpa memaksa profil `full` yang tidak dibatasi.
  * Jika hook/webhook atau umpan konten tidak tepercaya lainnya diaktifkan, gunakan tingkat model modern yang kuat dan pertahankan kebijakan alat/sandboxing yang ketat.


* ### Lokal vs Jarak Jauh

![](/assets/macos-onboarding/04-choose-gateway.png)

Di mana **Gateway** berjalan?

  * **Mac Ini (Hanya lokal):** onboarding dapat mengonfigurasi autentikasi dan menulis kredensial secara lokal.
  * **Jarak jauh (melalui SSH/Tailnet):** onboarding **tidak** mengonfigurasi autentikasi lokal; kredensial harus ada di host gateway.
  * **Konfigurasi nanti:** lewati penyiapan dan biarkan aplikasi belum dikonfigurasi.


* ### Izin

Pilih izin apa yang ingin Anda berikan kepada OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

Onboarding meminta izin TCC yang diperlukan untuk:

  * Otomasi (AppleScript)
  * Notifikasi
  * Aksesibilitas
  * Perekaman Layar
  * Mikrofon
  * Pengenalan Ucapan
  * Kamera
  * Lokasi


* ### CLI

* ### Chat Onboarding (sesi khusus)

Setelah penyiapan, aplikasi membuka sesi chat onboarding khusus agar agen dapat memperkenalkan diri dan memandu langkah berikutnya. Ini memisahkan panduan pertama kali dari percakapan normal Anda. Lihat [Bootstrapping](</id/start/bootstrapping>) untuk mengetahui apa yang terjadi pada host gateway selama agen pertama kali berjalan.

## Terkait

  * [Gambaran umum onboarding](</id/start/onboarding-overview>)
  * [Memulai](</id/start/getting-started>)


Was this useful?YesNo