---
title: SMS
source_url: https://docs.openclaw.ai/id/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw dapat menerima dan mengirim SMS melalui nomor telepon Twilio atau Messaging Service. Gateway mendaftarkan rute webhook masuk, memvalidasi tanda tangan permintaan Twilio secara default, dan mengirim balasan kembali melalui Messages API milik Twilio.

[**Pairing** Kebijakan DM default untuk SMS adalah pairing. ](</id/channels/pairing>) [**Gateway security** Tinjau paparan webhook dan kontrol akses pengirim. ](</id/gateway/security>) [**Channel troubleshooting** Diagnostik lintas channel dan panduan perbaikan. ](</id/channels/troubleshooting>)

## Sebelum Anda mulai

Anda memerlukan:

  * Plugin SMS resmi yang diinstal dengan `openclaw plugins install @openclaw/sms`.
  * Akun Twilio dengan nomor telepon yang mendukung SMS, atau Twilio Messaging Service.
  * Twilio Account SID dan Auth Token.
  * URL HTTPS publik yang mencapai OpenClaw Gateway Anda.
  * Pilihan kebijakan pengirim: `pairing` untuk penggunaan pribadi, `allowlist` untuk nomor telepon yang sudah disetujui, atau `open` hanya untuk akses SMS yang memang sengaja dibuat publik.


Gunakan satu nomor Twilio untuk SMS dan Voice Call jika nomor tersebut memiliki kedua kapabilitas. Konfigurasikan webhook SMS dan webhook Voice secara terpisah di Twilio; halaman ini hanya membahas webhook SMS.

## Penyiapan Cepat

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Create or choose a Twilio sender

Di Twilio, buka **Phone Numbers > Manage > Active numbers** dan pilih nomor yang mendukung SMS. Simpan:

  * Account SID, misalnya `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Nomor telepon pengirim, misalnya `+15551234567`


Jika Anda menggunakan Messaging Service alih-alih nomor pengirim tetap, simpan Messaging Service SID, misalnya `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Configure the SMS channel

Simpan ini sebagai `sms.patch.json5` dan ubah placeholder-nya:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Terapkan:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Point Twilio at the Gateway webhook

Di pengaturan nomor telepon Twilio, buka **Messaging** dan atur **A message comes in** ke:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Gunakan HTTP `POST`. Path lokal default adalah `/webhooks/sms`; ubah `channels.sms.webhookPath` jika Anda memerlukan rute berbeda.

* ### Expose the exact SMS webhook path

URL publik Anda harus merutekan path SMS ke proses Gateway. Jika Anda menggunakan Tailscale Funnel untuk pengujian lokal, ekspos `/webhooks/sms` secara eksplisit:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Voice Call dan SMS menggunakan path webhook terpisah. Jika nomor Twilio yang sama menangani keduanya, pertahankan kedua rute tetap dikonfigurasi di Twilio dan di tunnel Anda.

* ### Start the Gateway and approve first sender

bashCopy code
[code]
    openclaw gateway
[/code]

Kirim pesan teks ke nomor Twilio. Pesan pertama membuat permintaan pairing. Setujui:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Kode pairing kedaluwarsa setelah 1 jam.

## Contoh Konfigurasi

### File konfigurasi

Gunakan penyiapan file konfigurasi ketika Anda ingin definisi channel ikut bersama konfigurasi Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Variabel lingkungan

Gunakan penyiapan env untuk deployment akun tunggal saat rahasia berasal dari lingkungan host:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Lalu aktifkan channel dalam konfigurasi:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` diterima sebagai alias untuk `TWILIO_PHONE_NUMBER`. Gunakan `TWILIO_MESSAGING_SERVICE_SID` alih-alih pengirim nomor telepon saat Twilio harus memilih pengirim dari Messaging Service.

### Token autentikasi SecretRef

`authToken` dapat berupa SecretRef. Gunakan ini ketika Gateway harus menyelesaikan Twilio Auth Token dari runtime rahasia OpenClaw alih-alih menyimpan konfigurasi plaintext:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Variabel lingkungan atau penyedia rahasia yang dirujuk harus terlihat oleh runtime Gateway. Mulai ulang proses Gateway terkelola setelah mengubah variabel lingkungan host.

### Nomor privat khusus allowlist

Gunakan `allowlist` ketika hanya nomor telepon yang dikenal yang boleh berbicara dengan agen:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Pengirim Messaging Service

Gunakan `messagingServiceSid` alih-alih `fromNumber` saat Twilio harus memilih pengirim melalui Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Jika `fromNumber` dan `messagingServiceSid` sama-sama ada setelah penyelesaian konfigurasi dan env, `fromNumber` digunakan.

### Target outbound default

Atur `defaultTo` ketika otomasi atau pengiriman yang diinisiasi agen harus memiliki tujuan default jika alur pengiriman tidak mencantumkan target eksplisit:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Kontrol akses

`channels.sms.dmPolicy` mengontrol akses SMS langsung:

  * `pairing` (default)
  * `allowlist` (memerlukan setidaknya satu pengirim di `allowFrom`)
  * `open` (memerlukan `allowFrom` menyertakan `"*"`)
  * `disabled`


Entri `allowFrom` harus berupa nomor telepon E.164 seperti `+15551234567`. Prefiks `sms:` diterima dan dinormalisasi. Untuk asisten privat, pilih `dmPolicy: "allowlist"` dengan nomor telepon eksplisit.

## Mengirim SMS

Target SMS outbound menggunakan prefiks layanan `sms:` dengan channel SMS yang dipilih:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Ketika pemilihan channel bersifat implisit, `twilio-sms:+15551234567` memilih channel ini tanpa mengambil alih prefiks layanan `sms:` milik channel yang sudah ada dan digunakan oleh iMessage.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

CLI memerlukan `--target` eksplisit. `defaultTo` digunakan untuk jalur otomasi dan pengiriman yang diinisiasi agen ketika target dapat diselesaikan dari konfigurasi channel.

Balasan agen dari percakapan SMS masuk otomatis dikirim kembali ke pengirim melalui pengirim Twilio yang dikonfigurasi.

Output SMS berupa teks biasa. OpenClaw menghapus markdown, meratakan blok kode berpagar, mempertahankan tautan yang mudah dibaca, dan memecah balasan panjang sebelum mengirimkannya melalui Twilio.

## Verifikasi Penyiapan

Setelah Gateway dimulai:

  1. Pastikan log Gateway menampilkan rute webhook SMS.
  2. Jalankan probe dari sisi Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Kirim SMS ke nomor Twilio dari telepon Anda.
  4. Jalankan `openclaw pairing list sms`.
  5. Setujui kode pairing dengan `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Kirim SMS lain dan pastikan agen membalas.


Untuk pengujian khusus outbound, gunakan:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### Pengujian end-to-end dari macOS iMessage/SMS

Di Mac yang dapat mengirim SMS operator melalui Messages, Anda dapat menggunakan `imsg` untuk menjalankan sisi pengirim tanpa menyentuh telepon Anda:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Pesan pertama seharusnya membuat permintaan pairing. Pesan kedua seharusnya menerima balasan agen melalui Twilio.

## Keamanan webhook

Secara default, OpenClaw memvalidasi `X-Twilio-Signature` menggunakan `publicWebhookUrl` dan `authToken`. Pastikan `publicWebhookUrl` selaras byte demi byte dengan URL yang dikonfigurasi di Twilio, termasuk skema, host, path, dan string kueri.

Hanya untuk pengujian tunnel lokal, Anda dapat mengatur:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Jangan gunakan validasi tanda tangan yang dinonaktifkan pada Gateway publik.

## Konfigurasi multi-akun

Gunakan `accounts` ketika Anda mengoperasikan lebih dari satu nomor Twilio:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Setiap akun harus menggunakan `webhookPath` yang berbeda.

## Pemecahan masalah

### Twilio mengembalikan 403 atau OpenClaw menolak webhook

Periksa bahwa `publicWebhookUrl` sama persis dengan URL yang dikonfigurasi di Twilio, termasuk skema, host, path, dan string kueri. Twilio menandatangani string URL publik, jadi penulisan ulang proxy dan nama host alternatif dapat merusak validasi tanda tangan.

### Tidak ada permintaan pairing yang muncul

Periksa URL dan metode webhook **Messaging** milik nomor Twilio. Itu harus mengarah ke URL webhook SMS dan menggunakan `POST`. Pastikan juga Gateway dapat dijangkau dari internet publik atau melalui tunnel Anda.

Jika log pesan Twilio menampilkan error `11200`, Twilio menerima SMS masuk tetapi tidak dapat mencapai webhook Anda. Periksa:

  * Twilio **Messaging > A message comes in** mengarah ke `publicWebhookUrl`.
  * Metodenya adalah `POST`.
  * Tunnel atau reverse proxy mengekspos `webhookPath` yang tepat; untuk Tailscale Funnel, jalankan `tailscale funnel status` dan pastikan `/webhooks/sms` tercantum.
  * `publicWebhookUrl` menggunakan skema, host, path, dan string kueri yang sama dengan yang dikirim Twilio, sehingga validasi tanda tangan dapat mereproduksi URL yang ditandatangani.


### Pengiriman outbound gagal

Pastikan `accountSid`, `authToken`, dan salah satu dari `fromNumber` atau `messagingServiceSid` terselesaikan. Jika Anda menggunakan akun uji coba Twilio, nomor tujuan mungkin perlu diverifikasi di Twilio sebelum SMS outbound dapat dikirim.

### Pesan masuk tetapi agen tidak menjawab

Periksa `dmPolicy` dan `allowFrom`. Dengan kebijakan `pairing` default, pengirim harus disetujui sebelum giliran agen normal diproses.

Was this useful?YesNo

Open issue