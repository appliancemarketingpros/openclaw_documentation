---
title: Aturan push Matrix untuk pratinjau senyap
source_url: https://docs.openclaw.ai/id/channels/matrix-push-rules
scraped_at: 2026-05-25
---

Saat `channels.matrix.streaming` bernilai `"quiet"`, OpenClaw mengedit satu event pratinjau di tempat dan menandai edit final dengan flag konten khusus. Klien Matrix memberi notifikasi pada edit final hanya jika aturan push per pengguna cocok dengan flag tersebut. Halaman ini ditujukan untuk operator yang meng-host Matrix sendiri dan ingin memasang aturan tersebut untuk setiap akun penerima.

Jika Anda hanya menginginkan perilaku notifikasi Matrix bawaan, gunakan `streaming: "partial"` atau biarkan streaming nonaktif. Lihat [Penyiapan channel Matrix](</id/channels/matrix#streaming-previews>).

## Prasyarat

  * pengguna penerima = orang yang harus menerima notifikasi
  * pengguna bot = akun Matrix OpenClaw yang mengirim balasan
  * gunakan token akses pengguna penerima untuk panggilan API di bawah ini
  * cocokkan `sender` dalam aturan push dengan MXID lengkap pengguna bot
  * akun penerima harus sudah memiliki pusher yang berfungsi — aturan pratinjau senyap hanya berfungsi ketika pengiriman push Matrix normal sehat


## Langkah-langkah

* ### Konfigurasikan pratinjau senyap

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Dapatkan token akses penerima

Gunakan kembali token sesi klien yang sudah ada jika memungkinkan. Untuk membuat yang baru:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Verifikasi pusher ada

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Jika tidak ada pusher yang kembali, perbaiki pengiriman push Matrix normal untuk akun ini sebelum melanjutkan.

* ### Pasang aturan push override

OpenClaw menandai edit pratinjau final khusus teks dengan `content["com.openclaw.finalized_preview"] = true`. Pasang aturan yang mencocokkan penanda tersebut beserta MXID bot sebagai pengirim:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Ganti sebelum menjalankan:

  * `https://matrix.example.org`: URL dasar homeserver Anda
  * `$USER_ACCESS_TOKEN`: token akses pengguna penerima
  * `openclaw-finalized-preview-botname`: ID aturan yang unik per bot per penerima (pola: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: MXID bot OpenClaw Anda, bukan milik penerima


* ### Verifikasi

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Lalu uji balasan yang di-stream. Dalam mode senyap, room menampilkan pratinjau draf senyap dan memberi notifikasi setelah blok atau giliran selesai.

Untuk menghapus aturan nanti, lakukan `DELETE` pada URL aturan yang sama dengan token penerima.

## Catatan multi-bot

Aturan push dikunci berdasarkan `ruleId`: menjalankan ulang `PUT` terhadap ID yang sama memperbarui satu aturan. Untuk beberapa bot OpenClaw yang memberi notifikasi ke penerima yang sama, buat satu aturan per bot dengan pencocokan pengirim yang berbeda.

Aturan `override` baru yang ditentukan pengguna disisipkan sebelum aturan penekanan default, jadi tidak diperlukan parameter pengurutan tambahan. Aturan ini hanya memengaruhi edit pratinjau khusus teks yang dapat difinalisasi di tempat; fallback media dan fallback pratinjau usang menggunakan pengiriman Matrix normal.

## Catatan homeserver

Synapse

Tidak diperlukan perubahan khusus pada `homeserver.yaml`. Jika notifikasi Matrix normal sudah sampai ke pengguna ini, token penerima + panggilan `pushrules` di atas adalah langkah penyiapan utama.

Jika Anda menjalankan Synapse di belakang reverse proxy atau worker, pastikan `/_matrix/client/.../pushrules/` mencapai Synapse dengan benar. Pengiriman push ditangani oleh proses utama atau `synapse.app.pusher` / worker pusher yang dikonfigurasi — pastikan semuanya sehat.

Aturan ini menggunakan kondisi aturan push `event_property_is` (MSC3758, aturan push v1.10), yang ditambahkan ke Synapse pada 2023. Rilis Synapse yang lebih lama menerima panggilan `PUT pushrules/...` tetapi diam-diam tidak pernah mencocokkan kondisi tersebut — tingkatkan Synapse jika tidak ada notifikasi yang tiba pada edit pratinjau final.

Tuwunel

Alur yang sama seperti Synapse; tidak diperlukan konfigurasi khusus Tuwunel untuk penanda pratinjau final.

Jika notifikasi menghilang saat pengguna aktif di perangkat lain, periksa apakah `suppress_push_when_active` diaktifkan. Tuwunel menambahkan opsi ini pada 1.4.2 (September 2025) dan opsi ini dapat dengan sengaja menekan push ke perangkat lain saat satu perangkat aktif.

## Terkait

  * [Penyiapan channel Matrix](</id/channels/matrix>)
  * [Konsep streaming](</id/concepts/streaming>)


Was this useful?YesNo