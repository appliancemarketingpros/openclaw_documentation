---
title: Pemeriksaan kesehatan (macOS)
source_url: https://docs.openclaw.ai/id/platforms/mac/health
scraped_at: 2026-05-25
---

# Pemeriksaan Kesehatan di macOS

Cara melihat apakah saluran yang terhubung dalam keadaan sehat dari aplikasi menu bar.

## Menu bar

  * Titik status sekarang mencerminkan kesehatan Baileys: 
    * Hijau: tertaut + socket baru saja dibuka.
    * Oranye: sedang menghubungkan/mencoba ulang.
    * Merah: logout atau probe gagal.
  * Baris sekunder berbunyi "linked · auth 12m" atau menampilkan alasan kegagalan.
  * Item menu "Run Health Check" memicu probe sesuai permintaan.


## Pengaturan

  * Tab General mendapatkan kartu Health yang menampilkan: usia auth tertaut, path/jumlah session-store, waktu pemeriksaan terakhir, error/status code terakhir, serta tombol Run Health Check / Reveal Logs.
  * Menggunakan snapshot cache sehingga UI dimuat seketika dan fallback dengan baik saat offline.
  * **Tab Channels** menampilkan status saluran + kontrol untuk WhatsApp/Telegram (QR login, logout, probe, disconnect/error terakhir).


## Cara kerja probe

  * Aplikasi menjalankan `openclaw health --json` melalui `ShellExecutor` setiap ~60 detik dan sesuai permintaan. Probe memuat kredensial dan melaporkan status tanpa mengirim pesan.
  * Cache snapshot baik terakhir dan error terakhir secara terpisah untuk menghindari flicker; tampilkan stempel waktu masing-masing.


## Saat ragu

  * Anda tetap dapat menggunakan alur CLI di [Kesehatan Gateway](</id/gateway/health>) (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) dan melakukan tail pada `/tmp/openclaw/openclaw-*.log` untuk `web-heartbeat` / `web-reconnect`.


## Terkait

  * [Kesehatan Gateway](</id/gateway/health>)
  * [Aplikasi macOS](</id/platforms/macos>)


Was this useful?YesNo