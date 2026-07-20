---
title: Plugin rapat Microsoft Teams
source_url: https://docs.openclaw.ai/id/plugins/teams-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

Plugin `teams-meetings` bergabung ke tautan Microsoft Teams sebagai tamu di profil Chrome OpenClaw. Plugin ini menerima tautan kerja di bawah `teams.microsoft.com/l/meetup-join/...` dan tautan konsumen di bawah `teams.live.com/meet/...`. Plugin ini tidak membuat rapat, bergabung melalui panggilan telepon, memanggil Microsoft Graph, atau merekam rapat.

## Penyiapan

Fitur balasan suara menggunakan prasyarat audio lokal yang sama dengan [Plugin Google Meet](</id/plugins/google-meet>): macOS, perangkat audio virtual `BlackHole 2ch`, dan SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Aktifkan Plugin, lalu periksa penyiapan:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

Gunakan `chromeNode.node` untuk menjalankan Chrome, BlackHole, dan SoX pada node macOS yang dipasangkan. Node tersebut harus mengizinkan `teamsmeetings.chrome` dan `browser.proxy`.

## Mode

Mode | Perilaku  
---|---  
`agent` | Transkripsi waktu nyata berkonsultasi dengan agen OpenClaw yang dikonfigurasi; TTS membalas.  
`bidi` | Model suara waktu nyata mendengarkan dan membalas secara langsung.  
`transcribe` | Bergabung hanya untuk mengamati dengan cuplikan transkrip teks langsung.  
  
Mode transkripsi mengaktifkan teks langsung Teams setelah diizinkan masuk dan menangkap baris teks yang mencantumkan pembicara. Tindakan `transcript` mengembalikan buffer teks terbatas untuk sesi rapat OpenClaw yang aktif.

## Batas bergabung sebagai tamu

Adaptor peramban menutup halaman perantara aplikasi, mengisi nama tamu, mematikan kamera, mengonfigurasi mikrofon untuk mode yang dipilih, dan mengeklik tombol bergabung. Status dalam panggilan menggunakan kontrol untuk mengakhiri panggilan; status lobi, masuk ke penyewa, dan izin perangkat mengembalikan alasan eksplisit yang memerlukan tindakan manual. Pengalihan peluncur rapat konsumen dan label `BlackHole 2ch (Virtual)` yang ditampilkan oleh Chrome didukung.

Kebijakan penyewa Teams dapat mewajibkan proses masuk, verifikasi email, atau izin masuk dari penyelenggara. Selesaikan langkah tersebut di profil Chrome OpenClaw, lalu coba lagi pemeriksaan status atau fungsi bicara. Plugin ini tidak melewati kebijakan penyewa.

Klien web Teams konsumen telah divalidasi secara langsung untuk halaman perantara aplikasi, pengisian nama tamu, tombol mikrofon/kamera sebelum bergabung, proses bergabung, izin masuk dari lobi, izin media, deteksi dalam panggilan, teks langsung, perutean masukan/keluaran BlackHole, keluar, dan deteksi setelah panggilan. Penyewa kerja dapat memberlakukan kebijakan yang berbeda untuk proses masuk, verifikasi email, izin masuk, dan konfirmasi keluar; selesaikan setiap tindakan manual yang dilaporkan di profil Chrome OpenClaw.

## Permukaan alat dan Gateway

Alat agen `teams_meetings` mendukung `join`, `leave`, `status`, `transcript`, dan `speak`. Metode Gateway menggunakan prefiks `teamsmeetings.*`. Perintah node adalah `teamsmeetings.chrome`.

## Terkait

  * [Ikhtisar Plugin rapat](</id/plugins/meeting-plugins>)
  * [Saluran Microsoft Teams](</id/channels/msteams>)


Was this useful?YesNo

Open issue