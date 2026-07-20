---
title: Plugin rapat Zoom
source_url: https://docs.openclaw.ai/id/plugins/zoom-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

Plugin `zoom-meetings` bergabung ke tautan rapat Zoom sebagai tamu melalui Zoom Web App di profil Chrome OpenClaw. Plugin ini menerima tautan rapat di bawah `zoom.us/j/...` dan subdomain akun seperti `example.zoom.us/j/...`. Plugin ini tidak membuat rapat, bergabung melalui panggilan telepon, menggunakan Zoom Meeting SDK, atau merekam rapat.

## Penyiapan

Fitur bicara balik menggunakan prasyarat audio lokal yang sama dengan [plugin Google Meet](</id/plugins/google-meet>): macOS, perangkat audio virtual `BlackHole 2ch`, dan SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Aktifkan plugin, lalu periksa penyiapan:

json5Copy code
[code]
    {  plugins: {    entries: {      "zoom-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw zoommeetings setupopenclaw zoommeetings join 'https://zoom.us/j/1234567890'
[/code]

Gunakan `chromeNode.node` untuk menjalankan Chrome, BlackHole, dan SoX pada node macOS yang dipasangkan. Node harus mengizinkan `zoommeetings.chrome` dan `browser.proxy`.

## Mode

Mode | Perilaku  
---|---  
`agent` | Transkripsi waktu nyata berkonsultasi dengan agen OpenClaw yang dikonfigurasi; TTS memberikan balasan.  
`bidi` | Model suara waktu nyata mendengarkan dan membalas secara langsung.  
`transcribe` | Bergabung hanya untuk mengamati dengan cuplikan transkrip takarir langsung.  
  
Mode transkripsi mengaktifkan takarir langsung Zoom setelah diizinkan masuk dan menangkap tampilan takarir yang dibatasi. Tindakan `transcript` mengembalikan buffer takarir untuk sesi rapat OpenClaw yang aktif.

## Batasan bergabung sebagai tamu

Adaptor peramban memilih **Join from browser** , mengisi nama tamu, mematikan kamera, mengonfigurasi mikrofon untuk mode yang dipilih, lalu mengeklik **Join**. Zoom Web App berjalan di bawah `app.zoom.us`; plugin memberikan izin mikrofon dan pemilihan speaker kepada origin tersebut sebelum navigasi. Status dalam panggilan menggunakan kontrol Leave milik Zoom. Status lobi, masuk, kode sandi, CAPTCHA, dan izin perangkat mengembalikan alasan tindakan manual secara eksplisit.

Kebijakan host dan akun Zoom dapat menonaktifkan bergabung melalui peramban, mewajibkan autentikasi atau verifikasi email, menampilkan CAPTCHA, atau mewajibkan persetujuan masuk dari host. Selesaikan langkah tersebut di profil Chrome OpenClaw, lalu coba lagi pemeriksaan status atau ucapan. Plugin tidak melewati kebijakan Zoom.

Zoom Web App telah divalidasi secara langsung menggunakan rapat pengujian resmi Zoom untuk interstisial aplikasi, entri nama tamu dalam iframe, kontrol mikrofon dan kamera sebelum bergabung, proses bergabung, izin media peramban dan macOS, deteksi dalam panggilan, pengaktifan takarir langsung, serta deteksi rapat yang diakhiri host. Status lobi dan autentikasi bergantung pada kebijakan host dan tetap menggunakan fallback teks ketika tidak tersedia pengidentifikasi DOM yang stabil.

## Permukaan alat dan Gateway

Alat agen `zoom_meetings` mendukung `join`, `leave`, `status`, `transcript`, dan `speak`. Metode Gateway menggunakan prefiks `zoommeetings.*`. Perintah node adalah `zoommeetings.chrome`.

## Terkait

  * [Ikhtisar plugin rapat](</id/plugins/meeting-plugins>)


Was this useful?YesNo

Open issue