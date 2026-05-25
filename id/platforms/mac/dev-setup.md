---
title: Penyiapan pengembangan macOS
source_url: https://docs.openclaw.ai/id/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# Penyiapan pengembang macOS

Bangun dan jalankan aplikasi macOS OpenClaw dari sumber.

## Prasyarat

Sebelum membangun aplikasi, pastikan Anda telah menginstal yang berikut:

  1. **Xcode 26.2+** : Diperlukan untuk pengembangan Swift.
  2. **Node.js 24 & pnpm**: Direkomendasikan untuk Gateway, CLI, dan skrip pengemasan. Node 22 LTS, saat ini `22.16+`, tetap didukung untuk kompatibilitas.


## 1\. Instal Dependensi

Instal dependensi seluruh proyek:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Bangun dan Kemas Aplikasi

Untuk membangun aplikasi macOS dan mengemasnya ke dalam `dist/OpenClaw.app`, jalankan:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Jika Anda tidak memiliki sertifikat Apple Developer ID, skrip akan otomatis menggunakan **penandatanganan ad-hoc** (`-`).

Untuk mode jalankan dev, flag penandatanganan, dan pemecahan masalah Team ID, lihat README aplikasi macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Catatan** : Aplikasi yang ditandatangani ad-hoc dapat memicu prompt keamanan. Jika aplikasi langsung crash dengan "Abort trap 6", lihat bagian Pemecahan Masalah.

## 3\. Instal CLI

Aplikasi macOS mengharapkan instalasi CLI `openclaw` global untuk mengelola tugas latar belakang.

**Untuk menginstalnya (direkomendasikan):**

  1. Buka aplikasi OpenClaw.
  2. Buka tab pengaturan **General**.
  3. Klik **"Install CLI"**.


Sebagai alternatif, instal secara manual:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` dan `bun add -g openclaw@<version>` juga berfungsi. Untuk runtime Gateway, Node tetap menjadi jalur yang direkomendasikan.

## Pemecahan Masalah

### Build gagal: toolchain atau SDK tidak cocok

Build aplikasi macOS mengharapkan SDK macOS terbaru dan toolchain Swift 6.2.

**Dependensi sistem (wajib):**

  * **Versi macOS terbaru yang tersedia di Software Update** (diwajibkan oleh SDK Xcode 26.2)
  * **Xcode 26.2** (toolchain Swift 6.2)


**Pemeriksaan:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Jika versi tidak cocok, perbarui macOS/Xcode dan jalankan ulang build.

### Aplikasi crash saat pemberian izin

Jika aplikasi crash ketika Anda mencoba mengizinkan akses **Speech Recognition** atau **Microphone** , ini mungkin disebabkan oleh cache TCC yang rusak atau ketidakcocokan tanda tangan.

**Perbaikan:**

  1. Reset izin TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Jika gagal, ubah `BUNDLE_ID` sementara di [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) untuk memaksa "clean slate" dari macOS.


### Gateway "Starting..." tanpa henti

Jika status Gateway tetap di "Starting...", periksa apakah ada proses zombie yang menahan port:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Jika proses manual menahan port, hentikan proses tersebut (Ctrl+C). Sebagai upaya terakhir, hentikan paksa PID yang Anda temukan di atas.

## Terkait

  * [Aplikasi macOS](</id/platforms/macos>)
  * [Ikhtisar instalasi](</id/install>)


Was this useful?YesNo