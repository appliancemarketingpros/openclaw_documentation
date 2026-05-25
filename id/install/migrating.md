---
title: Panduan migrasi
source_url: https://docs.openclaw.ai/id/install/migrating
scraped_at: 2026-05-25
---

OpenClaw mendukung tiga jalur migrasi: mengimpor dari sistem agen lain, memindahkan instalasi yang sudah ada ke mesin baru, dan memutakhirkan Plugin di tempat.

## Impor dari sistem agen lain

Gunakan penyedia migrasi bawaan untuk membawa instruksi, server MCP, Skills, konfigurasi model, dan (opsional) kunci API ke OpenClaw. Rencana dipratinjau sebelum perubahan apa pun, rahasia disunting dalam laporan, dan penerapan didukung oleh cadangan terverifikasi.

[**Migrasi dari Claude** Impor status Claude Code dan Claude Desktop, termasuk `CLAUDE.md`, server MCP, Skills, dan perintah proyek. ](</id/install/migrating-claude>) [**Migrasi dari Hermes** Impor konfigurasi Hermes, penyedia, server MCP, memori, Skills, dan kunci `.env` yang didukung. ](</id/install/migrating-hermes>)

Titik masuk CLI adalah [`openclaw migrate`](</id/cli/migrate>). Onboarding juga dapat menawarkan migrasi saat mendeteksi sumber yang dikenal (`openclaw onboard --flow import`).

## Pindahkan OpenClaw ke mesin baru

Salin **direktori status** (`~/.openclaw/` secara default) dan **workspace** Anda untuk mempertahankan:

  * **Konfigurasi** — `openclaw.json` dan semua pengaturan Gateway.
  * **Autentikasi** — `auth-profiles.json` per agen (kunci API plus OAuth), serta status channel atau penyedia apa pun di bawah `credentials/`.
  * **Sesi** — riwayat percakapan dan status agen.
  * **Status channel** — login WhatsApp, sesi Telegram, dan yang serupa.
  * **File workspace** — `MEMORY.md`, `USER.md`, Skills, dan prompt.


### Langkah migrasi

* ### Hentikan gateway dan buat cadangan

Di mesin **lama** , hentikan Gateway agar file tidak berubah saat penyalinan berlangsung, lalu arsipkan:

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

Jika Anda menggunakan beberapa profil (misalnya `~/.openclaw-work`), arsipkan masing-masing secara terpisah.

* ### Instal OpenClaw di mesin baru

[Instal](</id/install>) CLI (dan Node jika diperlukan) di mesin baru. Tidak masalah jika onboarding membuat `~/.openclaw/` baru. Anda akan menimpanya berikutnya.

* ### Salin direktori status dan workspace

Transfer arsip melalui `scp`, `rsync -a`, atau drive eksternal, lalu ekstrak:

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

Pastikan direktori tersembunyi disertakan dan kepemilikan file sesuai dengan pengguna yang akan menjalankan Gateway.

* ### Jalankan doctor dan verifikasi

Di mesin baru, jalankan [Doctor](</id/gateway/doctor>) untuk menerapkan migrasi konfigurasi dan memperbaiki layanan:

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

Jika Telegram atau Discord menggunakan fallback env default (`TELEGRAM_BOT_TOKEN` atau `DISCORD_BOT_TOKEN`), verifikasi bahwa `.env` direktori status yang dimigrasikan berisi kunci tersebut tanpa mencetak nilai rahasianya:

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` juga memperingatkan saat akun Telegram atau Discord default yang diaktifkan tidak memiliki token yang dikonfigurasi dan variabel env yang cocok tidak tersedia untuk proses doctor.

### Kendala umum

Ketidakcocokan profil atau state-dir

Jika Gateway lama menggunakan `--profile` atau `OPENCLAW_STATE_DIR` dan yang baru tidak, channel akan tampak keluar dan sesi akan kosong. Jalankan Gateway dengan profil atau state-dir **yang sama** dengan yang Anda migrasikan, lalu jalankan ulang `openclaw doctor`.

Hanya menyalin openclaw.json

File konfigurasi saja tidak cukup. Profil autentikasi model berada di bawah `agents/<agentId>/agent/auth-profiles.json`, dan status channel serta penyedia berada di bawah `credentials/`. Selalu migrasikan direktori status **secara keseluruhan**.

Izin dan kepemilikan

Jika Anda menyalin sebagai root atau beralih pengguna, Gateway mungkin gagal membaca kredensial. Pastikan direktori status dan workspace dimiliki oleh pengguna yang menjalankan Gateway.

Mode jarak jauh

Jika UI Anda mengarah ke Gateway **jarak jauh** , host jarak jauh memiliki sesi dan workspace. Migrasikan host Gateway itu sendiri, bukan laptop lokal Anda. Lihat [FAQ](</id/help/faq#where-things-live-on-disk>).

Rahasia dalam cadangan

Direktori status berisi profil autentikasi, kredensial channel, dan status penyedia lainnya. Simpan cadangan secara terenkripsi, hindari channel transfer yang tidak aman, dan rotasi kunci jika Anda mencurigai adanya paparan.

### Daftar periksa verifikasi

Di mesin baru, konfirmasikan:

  * [ ] `openclaw status` menunjukkan Gateway berjalan.
  * [ ] Channel masih tersambung (tidak perlu pairing ulang).
  * [ ] Dasbor terbuka dan menampilkan sesi yang sudah ada.
  * [ ] File workspace (memori, konfigurasi) tersedia.


## Mutakhirkan Plugin di tempat

Pemutakhiran Plugin di tempat mempertahankan id Plugin dan kunci konfigurasi yang sama, tetapi dapat memindahkan status di disk ke tata letak saat ini. Panduan pemutakhiran khusus Plugin berada bersama channel-nya:

  * [Migrasi Matrix](</id/channels/matrix-migration>): batas pemulihan status terenkripsi, perilaku snapshot otomatis, dan perintah pemulihan manual.


## Terkait

  * [`openclaw migrate`](</id/cli/migrate>): referensi CLI untuk impor lintas sistem.
  * [Ringkasan instalasi](</id/install>): semua metode instalasi.
  * [Doctor](</id/gateway/doctor>): pemeriksaan kesehatan pascamigrasi.
  * [Uninstall](</id/install/uninstall>): menghapus OpenClaw dengan bersih.


Was this useful?YesNo