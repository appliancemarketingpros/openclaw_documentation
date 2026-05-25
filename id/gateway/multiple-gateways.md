---
title: Beberapa Gateway
source_url: https://docs.openclaw.ai/id/gateway/multiple-gateways
scraped_at: 2026-05-25
---

Sebagian besar penyiapan sebaiknya menggunakan satu Gateway karena satu Gateway dapat menangani beberapa koneksi pesan dan agen. Jika Anda membutuhkan isolasi atau redundansi yang lebih kuat (misalnya, bot penyelamat), jalankan Gateway terpisah dengan profil/port yang terisolasi.

## Penyiapan terbaik yang direkomendasikan

Untuk sebagian besar pengguna, penyiapan bot penyelamat yang paling sederhana adalah:

  * pertahankan bot utama pada profil default
  * jalankan bot penyelamat pada `--profile rescue`
  * gunakan bot Telegram yang sepenuhnya terpisah untuk akun penyelamat
  * pertahankan bot penyelamat pada port dasar yang berbeda seperti `19789`


Ini membuat bot penyelamat tetap terisolasi dari bot utama sehingga dapat men-debug atau menerapkan perubahan konfigurasi jika bot utama sedang tidak aktif. Sisakan setidaknya 20 port di antara port dasar agar port browser/canvas/CDP turunan tidak pernah bertabrakan.

## Panduan Cepat Bot Penyelamat

Gunakan ini sebagai jalur default kecuali Anda memiliki alasan kuat untuk melakukan hal lain:

bashCopy code
[code]
    # Rescue bot (separate Telegram bot, separate profile, port 19789)openclaw --profile rescue onboardopenclaw --profile rescue gateway install --port 19789
[/code]

Jika bot utama Anda sudah berjalan, biasanya hanya itu yang Anda butuhkan.

Selama `openclaw --profile rescue onboard`:

  * gunakan token bot Telegram yang terpisah
  * pertahankan profil `rescue`
  * gunakan port dasar setidaknya 20 lebih tinggi dari bot utama
  * terima workspace penyelamat default kecuali Anda sudah mengelolanya sendiri


Jika onboarding sudah memasang layanan penyelamat untuk Anda, perintah akhir `gateway install` tidak diperlukan.

## Mengapa ini bekerja

Bot penyelamat tetap independen karena memiliki miliknya sendiri:

  * profil/konfigurasi
  * direktori status
  * workspace
  * port dasar (ditambah port turunan)
  * token bot Telegram


Untuk sebagian besar penyiapan, gunakan bot Telegram yang sepenuhnya terpisah untuk profil penyelamat:

  * mudah dibuat hanya untuk operator
  * token dan identitas bot terpisah
  * independen dari instalasi kanal/aplikasi bot utama
  * jalur pemulihan berbasis DM yang sederhana saat bot utama rusak


## Apa yang Diubah oleh `--profile rescue onboard`

`openclaw --profile rescue onboard` menggunakan alur onboarding normal, tetapi menulis semuanya ke profil terpisah.

Dalam praktiknya, itu berarti bot penyelamat mendapatkan miliknya sendiri:

  * file konfigurasi
  * direktori status
  * workspace (secara default `~/.openclaw/workspace-rescue`)
  * nama layanan terkelola


Prompt selain itu sama dengan onboarding normal.

## Penyiapan multi-Gateway umum

Tata letak bot penyelamat di atas adalah default termudah, tetapi pola isolasi yang sama berfungsi untuk pasangan atau grup Gateway apa pun pada satu host.

Untuk penyiapan yang lebih umum, berikan setiap Gateway tambahan profil bernamanya sendiri dan port dasarnya sendiri:

bashCopy code
[code]
    # main (default profile)openclaw setupopenclaw gateway --port 18789 # extra gatewayopenclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Jika Anda ingin kedua Gateway menggunakan profil bernama, itu juga berfungsi:

bashCopy code
[code]
    openclaw --profile main setupopenclaw --profile main gateway --port 18789 openclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Layanan mengikuti pola yang sama:

bashCopy code
[code]
    openclaw gateway installopenclaw --profile ops gateway install --port 19789
[/code]

Gunakan panduan cepat bot penyelamat saat Anda menginginkan jalur operator cadangan. Gunakan pola profil umum saat Anda menginginkan beberapa Gateway jangka panjang untuk kanal, penyewa, workspace, atau peran operasional yang berbeda.

## Daftar periksa isolasi

Jaga agar ini unik per instance Gateway:

  * `OPENCLAW_CONFIG_PATH` — file konfigurasi per instance
  * `OPENCLAW_STATE_DIR` — sesi, kredensial, cache per instance
  * `agents.defaults.workspace` — root workspace per instance
  * `gateway.port` (atau `--port`) — unik per instance
  * port browser/canvas/CDP turunan


Jika ini dibagikan, Anda akan mengalami race konfigurasi dan konflik port.

## Pemetaan port (turunan)

Port dasar = `gateway.port` (atau `OPENCLAW_GATEWAY_PORT` / `--port`).

  * port layanan kontrol browser = dasar + 2 (hanya loopback)
  * host canvas disajikan pada server HTTP Gateway (port yang sama dengan `gateway.port`)
  * port CDP profil browser dialokasikan otomatis dari `browser.controlPort + 9 .. + 108`


Jika Anda mengganti salah satu dari ini dalam konfigurasi atau env, Anda harus menjaganya tetap unik per instance.

## Catatan browser/CDP (kesalahan umum)

  * Jangan **pin** `browser.cdpUrl` ke nilai yang sama pada beberapa instance.
  * Setiap instance membutuhkan port kontrol browser dan rentang CDP sendiri (diturunkan dari port gateway-nya).
  * Jika Anda membutuhkan port CDP eksplisit, atur `browser.profiles.<name>.cdpPort` per instance.
  * Chrome jarak jauh: gunakan `browser.profiles.<name>.cdpUrl` (per profil, per instance).


## Contoh env manual

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \OPENCLAW_STATE_DIR=~/.openclaw \openclaw gateway --port 18789 OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \OPENCLAW_STATE_DIR=~/.openclaw-rescue \openclaw gateway --port 19789
[/code]

## Pemeriksaan cepat

bashCopy code
[code]
    openclaw gateway status --deepopenclaw --profile rescue gateway status --deepopenclaw --profile rescue gateway probeopenclaw statusopenclaw --profile rescue statusopenclaw --profile rescue browser status
[/code]

Interpretasi:

  * `gateway status --deep` membantu menangkap layanan launchd/systemd/schtasks usang dari instalasi lama.
  * Teks peringatan `gateway probe` seperti `multiple reachable gateways detected` diharapkan hanya saat Anda sengaja menjalankan lebih dari satu gateway terisolasi.


## Terkait

  * [Runbook Gateway](</id/gateway>)
  * [Kunci Gateway](</id/gateway/gateway-lock>)
  * [Konfigurasi](</id/gateway/configuration>)


Was this useful?YesNo