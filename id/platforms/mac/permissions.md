---
title: Izin macOS
source_url: https://docs.openclaw.ai/id/platforms/mac/permissions
scraped_at: 2026-05-25
---

Pemberian izin macOS bersifat rapuh. TCC mengaitkan pemberian izin dengan signature kode aplikasi, bundle identifier, dan path di disk. Jika salah satu dari itu berubah, macOS memperlakukan aplikasi sebagai aplikasi baru dan dapat menghapus atau menyembunyikan prompt.

## Persyaratan untuk izin yang stabil

  * Path yang sama: jalankan aplikasi dari lokasi tetap (untuk OpenClaw, `dist/OpenClaw.app`).
  * Bundle identifier yang sama: mengubah bundle ID membuat identitas izin baru.
  * Aplikasi yang ditandatangani: build yang tidak ditandatangani atau ditandatangani ad-hoc tidak mempertahankan izin.
  * Signature yang konsisten: gunakan sertifikat Apple Development atau Developer ID yang nyata agar signature tetap stabil di beberapa build ulang.


Signature ad-hoc menghasilkan identitas baru pada setiap build. macOS akan melupakan pemberian izin sebelumnya, dan prompt bisa hilang sepenuhnya sampai entri usang dibersihkan.

## Checklist pemulihan saat prompt menghilang

  1. Keluar dari aplikasi.
  2. Hapus entri aplikasi di System Settings -> Privacy & Security.
  3. Luncurkan ulang aplikasi dari path yang sama dan berikan izin lagi.
  4. Jika prompt tetap tidak muncul, reset entri TCC dengan `tccutil` lalu coba lagi.
  5. Beberapa izin baru muncul kembali setelah restart macOS penuh.


Contoh reset (ganti bundle ID sesuai kebutuhan):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Izin file dan folder (Desktop/Documents/Downloads)

macOS juga dapat membatasi Desktop, Documents, dan Downloads untuk proses terminal/latar belakang. Jika pembacaan file atau listing direktori macet, berikan akses ke konteks proses yang sama yang melakukan operasi file (misalnya Terminal/iTerm, aplikasi yang diluncurkan LaunchAgent, atau proses SSH).

Solusi sementara: pindahkan file ke workspace OpenClaw (`~/.openclaw/workspace`) jika Anda ingin menghindari pemberian izin per folder.

Jika Anda sedang menguji izin, selalu tandatangani dengan sertifikat yang nyata. Build ad-hoc hanya dapat diterima untuk run lokal cepat saat izin tidak penting.

## Terkait

  * [Aplikasi macOS](</id/platforms/macos>)
  * [Penandatanganan macOS](</id/platforms/mac/signing>)


Was this useful?YesNo