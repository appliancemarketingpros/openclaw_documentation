---
title: Northflank
source_url: https://docs.openclaw.ai/id/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Deploy OpenClaw di Northflank dengan template sekali klik dan akses melalui Control UI web. Ini adalah jalur termudah “tanpa terminal di server”: Northflank menjalankan Gateway untuk Anda.

## Cara memulai

  1. Klik [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) untuk membuka template.
  2. Buat [akun di Northflank](<https://app.northflank.com/signup>) jika Anda belum memilikinya.
  3. Klik **Deploy OpenClaw now**.
  4. Setel variabel environment yang wajib: `OPENCLAW_GATEWAY_TOKEN` (gunakan nilai acak yang kuat).
  5. Klik **Deploy stack** untuk membangun dan menjalankan template OpenClaw.
  6. Tunggu hingga deployment selesai, lalu klik **View resources**.
  7. Buka layanan OpenClaw.
  8. Buka URL OpenClaw publik di `/openclaw` dan hubungkan menggunakan shared secret yang telah dikonfigurasi. Template ini menggunakan `OPENCLAW_GATEWAY_TOKEN` secara default; jika Anda menggantinya dengan auth password, gunakan password tersebut.


## Yang Anda dapatkan

  * Gateway OpenClaw + Control UI yang di-host
  * Penyimpanan persisten melalui Northflank Volume (`/data`) sehingga `openclaw.json`, `auth-profiles.json` per agent, state saluran/provider, sesi, dan workspace tetap bertahan setelah redeploy


## Hubungkan saluran

Gunakan Control UI di `/openclaw` atau jalankan `openclaw onboard` melalui SSH untuk instruksi penyiapan saluran:

  * [Telegram](</id/channels/telegram>) (paling cepat — cukup token bot)
  * [Discord](</id/channels/discord>)
  * [Semua saluran](</id/channels>)


## Langkah berikutnya

  * Siapkan saluran pesan: [Saluran](</id/channels>)
  * Konfigurasikan Gateway: [Konfigurasi Gateway](</id/gateway/configuration>)
  * Jaga OpenClaw tetap terbaru: [Memperbarui](</id/install/updating>)


Was this useful?YesNo