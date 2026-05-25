---
title: Twitch
source_url: https://docs.openclaw.ai/id/channels/twitch
scraped_at: 2026-05-25
---

Dukungan chat Twitch melalui koneksi IRC. OpenClaw terhubung sebagai pengguna Twitch (akun bot) untuk menerima dan mengirim pesan di channel.

## Plugin bawaan

Jika Anda menggunakan build lama atau instalasi kustom yang mengecualikan Twitch, instal paket npm secara langsung:

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Checkout lokal

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Gunakan paket dasar untuk mengikuti tag rilis resmi saat ini. Pin versi persis hanya ketika Anda memerlukan instalasi yang dapat direproduksi.

Detail: [Plugin](</id/tools/plugin>)

## Penyiapan cepat (pemula)

* ### Pastikan Plugin tersedia

Rilis OpenClaw paket saat ini sudah menyertakannya. Instalasi lama/kustom dapat menambahkannya secara manual dengan perintah di atas.

* ### Buat akun bot Twitch

Buat akun Twitch khusus untuk bot (atau gunakan akun yang sudah ada).

* ### Buat kredensial

Gunakan [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Pilih **Bot Token**
  * Pastikan scope `chat:read` dan `chat:write` dipilih
  * Salin **Client ID** dan **Access Token**


* ### Temukan ID pengguna Twitch Anda

Gunakan <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> untuk mengonversi nama pengguna menjadi ID pengguna Twitch.

* ### Konfigurasikan token

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (hanya akun default)
  * Atau config: `channels.twitch.accessToken`


Jika keduanya diatur, config lebih diprioritaskan (fallback env hanya untuk akun default).

* ### Mulai gateway

Mulai gateway dengan channel yang telah dikonfigurasi.

Config minimal:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Apa ini

  * Channel Twitch yang dimiliki oleh Gateway.
  * Perutean deterministik: balasan selalu kembali ke Twitch.
  * Setiap akun dipetakan ke kunci sesi terisolasi `agent:<agentId>:twitch:<accountName>`.
  * `username` adalah akun bot (yang melakukan autentikasi), `channel` adalah ruang chat yang akan dimasuki.


## Penyiapan (terperinci)

### Buat kredensial

Gunakan [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Pilih **Bot Token**
  * Pastikan scope `chat:read` dan `chat:write` dipilih
  * Salin **Client ID** dan **Access Token**


### Konfigurasikan bot

### Variabel env (hanya akun default)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Jika env dan config sama-sama diatur, config lebih diprioritaskan.

### Kontrol akses (direkomendasikan)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Utamakan `allowFrom` untuk allowlist ketat. Gunakan `allowedRoles` sebagai gantinya jika Anda menginginkan akses berbasis peran.

**Peran yang tersedia:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Refresh token (opsional)

Token dari [Twitch Token Generator](<https://twitchtokengenerator.com/>) tidak dapat direfresh secara otomatis - buat ulang saat kedaluwarsa.

Untuk refresh token otomatis, buat aplikasi Twitch Anda sendiri di [Twitch Developer Console](<https://dev.twitch.tv/console>) dan tambahkan ke config:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Bot otomatis merefresh token sebelum kedaluwarsa dan mencatat event refresh.

## Dukungan multi-akun

Gunakan `channels.twitch.accounts` dengan token per akun. Lihat [Konfigurasi](</id/gateway/configuration>) untuk pola bersama.

Contoh (satu akun bot di dua channel):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Kontrol akses

### Allowlist ID pengguna (paling aman)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Berbasis peran

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` adalah allowlist ketat. Ketika diatur, hanya ID pengguna tersebut yang diizinkan. Jika Anda menginginkan akses berbasis peran, biarkan `allowFrom` tidak diatur dan konfigurasikan `allowedRoles` sebagai gantinya.

### Nonaktifkan persyaratan @mention

Secara default, `requireMention` bernilai `true`. Untuk menonaktifkan dan merespons semua pesan:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Pemecahan masalah

Pertama, jalankan perintah diagnostik:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot tidak merespons pesan

  * **Periksa kontrol akses:** Pastikan ID pengguna Anda ada di `allowFrom`, atau hapus `allowFrom` sementara dan atur `allowedRoles: ["all"]` untuk menguji.
  * **Periksa apakah bot berada di channel:** Bot harus masuk ke channel yang ditentukan di `channel`.

Masalah token

"Gagal terhubung" atau error autentikasi:

  * Pastikan `accessToken` adalah nilai token akses OAuth (biasanya dimulai dengan prefiks `oauth:`)
  * Periksa apakah token memiliki scope `chat:read` dan `chat:write`
  * Jika menggunakan refresh token, pastikan `clientSecret` dan `refreshToken` diatur

Refresh token tidak berfungsi

Periksa log untuk event refresh:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Jika Anda melihat "token refresh disabled (no refresh token)":

  * Pastikan `clientSecret` disediakan
  * Pastikan `refreshToken` disediakan


## Config

### Config akun

Nama pengguna bot.

Token akses OAuth dengan `chat:read` dan `chat:write`.

Client ID Twitch (dari Token Generator atau aplikasi Anda).

Channel yang akan dimasuki.

Aktifkan akun ini.

Opsional: untuk refresh token otomatis.

Opsional: untuk refresh token otomatis.

Kedaluwarsa token dalam detik.

Timestamp token diperoleh.

Allowlist ID pengguna.

Memerlukan @mention.

### Opsi provider

  * `channels.twitch.enabled` \- Aktifkan/nonaktifkan startup channel
  * `channels.twitch.username` \- Nama pengguna bot (config satu akun yang disederhanakan)
  * `channels.twitch.accessToken` \- Token akses OAuth (config satu akun yang disederhanakan)
  * `channels.twitch.clientId` \- Client ID Twitch (config satu akun yang disederhanakan)
  * `channels.twitch.channel` \- Channel yang akan dimasuki (config satu akun yang disederhanakan)
  * `channels.twitch.accounts.<accountName>` \- Config multi-akun (semua field akun di atas)


Contoh lengkap:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Tindakan alat

Agent dapat memanggil `twitch` dengan tindakan:

  * `send` \- Kirim pesan ke channel


Contoh:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Keamanan dan ops

  * **Perlakukan token seperti kata sandi** — Jangan pernah commit token ke git.
  * **Gunakan refresh token otomatis** untuk bot yang berjalan lama.
  * **Gunakan allowlist ID pengguna** alih-alih nama pengguna untuk kontrol akses.
  * **Pantau log** untuk event refresh token dan status koneksi.
  * **Batasi scope token seminimal mungkin** — Hanya minta `chat:read` dan `chat:write`.
  * **Jika macet** : Mulai ulang gateway setelah memastikan tidak ada proses lain yang memiliki sesi.


## Batasan

  * **500 karakter** per pesan (dipecah otomatis pada batas kata).
  * Markdown dihapus sebelum pemecahan.
  * Tidak ada pembatasan laju (menggunakan batas laju bawaan Twitch).


## Terkait

  * [Perutean Channel](</id/channels/channel-routing>) — perutean sesi untuk pesan
  * [Ikhtisar Channel](</id/channels>) — semua channel yang didukung
  * [Grup](</id/channels/groups>) — perilaku chat grup dan gating mention
  * [Pairing](</id/channels/pairing>) — autentikasi DM dan alur pairing
  * [Keamanan](</id/gateway/security>) — model akses dan hardening


Was this useful?YesNo