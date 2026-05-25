---
title: IRC
source_url: https://docs.openclaw.ai/id/channels/irc
scraped_at: 2026-05-25
---

Gunakan IRC saat Anda ingin OpenClaw tersedia di channel klasik (`#room`) dan pesan langsung. IRC dikirim sebagai Plugin bawaan, tetapi dikonfigurasi di config utama pada `channels.irc`.

## Mulai cepat

  1. Aktifkan config IRC di `~/.openclaw/openclaw.json`.
  2. Tetapkan setidaknya:

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

Utamakan server IRC privat untuk koordinasi bot. Jika Anda sengaja menggunakan jaringan IRC publik, pilihan umum meliputi Libera.Chat, OFTC, dan Snoonet. Hindari channel publik yang mudah ditebak untuk lalu lintas backchannel bot atau swarm.

  3. Mulai/mulai ulang Gateway:

bashCopy code
[code]
    openclaw gateway run
[/code]

## Default keamanan

  * IRC menggunakan soket TCP/TLS mentah di luar routing forward proxy yang dikelola operator OpenClaw. Dalam deployment yang mewajibkan semua egress melalui forward proxy tersebut, tetapkan `channels.irc.enabled=false` kecuali egress IRC langsung disetujui secara eksplisit.
  * `channels.irc.dmPolicy` default ke `"pairing"`.
  * `channels.irc.groupPolicy` default ke `"allowlist"`.
  * Dengan `groupPolicy="allowlist"`, tetapkan `channels.irc.groups` untuk menentukan channel yang diizinkan.
  * Gunakan TLS (`channels.irc.tls=true`) kecuali Anda sengaja menerima transport plaintext.


## Kontrol akses

Ada dua "gerbang" terpisah untuk channel IRC:

  1. **Akses channel** (`groupPolicy` \+ `groups`): apakah bot menerima pesan dari suatu channel sama sekali.
  2. **Akses pengirim** (`groupAllowFrom` / per-channel `groups["#channel"].allowFrom`): siapa yang diizinkan memicu bot di dalam channel tersebut.


Kunci config:

  * Allowlist DM (akses pengirim DM): `channels.irc.allowFrom`
  * Allowlist pengirim grup (akses pengirim channel): `channels.irc.groupAllowFrom`
  * Kontrol per-channel (aturan channel + pengirim + mention): `channels.irc.groups["#channel"]`
  * `channels.irc.groupPolicy="open"` mengizinkan channel yang tidak dikonfigurasi (**tetap dibatasi mention secara default**)


Entri allowlist sebaiknya menggunakan identitas pengirim yang stabil (`nick!user@host`). Pencocokan nick polos dapat berubah dan hanya diaktifkan saat `channels.irc.dangerouslyAllowNameMatching: true`.

### Hal umum yang sering keliru: `allowFrom` untuk DM, bukan channel

Jika Anda melihat log seperti:

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


...itu berarti pengirim tidak diizinkan untuk pesan **grup/channel**. Perbaiki dengan salah satu cara berikut:

  * menetapkan `channels.irc.groupAllowFrom` (global untuk semua channel), atau
  * menetapkan allowlist pengirim per-channel: `channels.irc.groups["#channel"].allowFrom`


Contoh (izinkan siapa pun di `#tuirc-dev` berbicara dengan bot):

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## Pemicu balasan (mention)

Meskipun sebuah channel diizinkan (melalui `groupPolicy` \+ `groups`) dan pengirim diizinkan, OpenClaw secara default menerapkan **pembatasan mention** dalam konteks grup.

Ini berarti Anda mungkin melihat log seperti `drop channel … (missing-mention)` kecuali pesan menyertakan pola mention yang cocok dengan bot.

Agar bot membalas di channel IRC **tanpa perlu mention** , nonaktifkan pembatasan mention untuk channel tersebut:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

Atau untuk mengizinkan **semua** channel IRC (tanpa allowlist per-channel) dan tetap membalas tanpa mention:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## Catatan keamanan (direkomendasikan untuk channel publik)

Jika Anda mengizinkan `allowFrom: ["*"]` di channel publik, siapa pun dapat memberi prompt ke bot. Untuk mengurangi risiko, batasi tool untuk channel tersebut.

### Tool yang sama untuk semua orang di channel

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### Tool berbeda per pengirim (pemilik mendapatkan lebih banyak kuasa)

Gunakan `toolsBySender` untuk menerapkan kebijakan yang lebih ketat pada `"*"` dan yang lebih longgar pada nick Anda:

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

Catatan:

  * Kunci `toolsBySender` sebaiknya menggunakan `id:` untuk nilai identitas pengirim IRC: `id:eigen` atau `id:eigen!~eigen@174.127.248.171` untuk pencocokan yang lebih kuat.
  * Kunci lama tanpa prefiks masih diterima dan dicocokkan hanya sebagai `id:`.
  * Kebijakan pengirim pertama yang cocok akan berlaku; `"*"` adalah fallback wildcard.


Untuk informasi lebih lanjut tentang akses grup dibandingkan pembatasan mention (dan bagaimana keduanya berinteraksi), lihat: [/channels/groups](</id/channels/groups>).

## NickServ

Untuk mengidentifikasi dengan NickServ setelah terhubung:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

Pendaftaran satu kali opsional saat terhubung:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

Nonaktifkan `register` setelah nick terdaftar untuk menghindari percobaan REGISTER berulang.

## Variabel lingkungan

Akun default mendukung:

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS` (dipisahkan koma)
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


`IRC_HOST` tidak dapat ditetapkan dari `.env` workspace; lihat [File `.env` workspace](</id/gateway/security>).

## Pemecahan masalah

  * Jika bot terhubung tetapi tidak pernah membalas di channel, verifikasi `channels.irc.groups` **dan** apakah pembatasan mention menjatuhkan pesan (`missing-mention`). Jika Anda ingin bot membalas tanpa ping, tetapkan `requireMention:false` untuk channel tersebut.
  * Jika login gagal, verifikasi ketersediaan nick dan kata sandi server.
  * Jika TLS gagal pada jaringan khusus, verifikasi host/port dan penyiapan sertifikat.


## Terkait

  * [Ringkasan Channel](</id/channels>) — semua channel yang didukung
  * [Pairing](</id/channels/pairing>) — autentikasi DM dan alur pairing
  * [Grup](</id/channels/groups>) — perilaku chat grup dan pembatasan mention
  * [Routing Channel](</id/channels/channel-routing>) — routing sesi untuk pesan
  * [Keamanan](</id/gateway/security>) — model akses dan hardening


Was this useful?YesNo