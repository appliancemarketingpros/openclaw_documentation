---
title: ClickClack
source_url: https://docs.openclaw.ai/id/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack menghubungkan OpenClaw ke ruang kerja ClickClack yang di-host sendiri melalui token bot ClickClack kelas satu.

Gunakan ini saat Anda ingin agen OpenClaw muncul sebagai pengguna bot ClickClack. ClickClack mendukung bot layanan independen dan bot milik pengguna; bot milik pengguna mempertahankan `owner_user_id` dan hanya menerima cakupan token yang Anda berikan.

## Penyiapan cepat

Buat token bot di ClickClack:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Untuk bot milik pengguna, tambahkan `--owner <user_id>`.

Konfigurasikan OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Lalu jalankan:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## Beberapa bot

Setiap akun membuka koneksi realtime ClickClack miliknya sendiri dan menggunakan token bot miliknya sendiri.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` menggunakan `api.runtime.llm.complete` secara langsung untuk balasan bot singkat. Saat sebuah akun menetapkan `agentId`, OpenClaw mewajibkan bit kepercayaan eksplisit `plugins.entries.clickclack.llm.allowAgentIdOverride` agar Plugin dapat menjalankan completion untuk agen bot tersebut. Biarkan nonaktif jika Anda hanya menggunakan rute agen default.

## Target

  * `channel:<name-or-id>` mengirim ke kanal ruang kerja. Target polos secara default menjadi `channel:`.
  * `dm:<user_id>` membuat atau menggunakan kembali percakapan langsung dengan pengguna tersebut.
  * `thread:<message_id>` membalas di thread yang sudah ada.


Contoh:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Izin

Cakupan token ClickClack diberlakukan oleh API ClickClack.

  * `bot:read`: membaca data ruang kerja/kanal/pesan/thread/DM/realtime/profil.
  * `bot:write`: `bot:read` ditambah pesan kanal, balasan thread, DM, dan unggahan.
  * `bot:admin`: `bot:write` ditambah pembuatan kanal.


OpenClaw hanya memerlukan `bot:write` untuk chat agen normal.

## Pemecahan masalah

  * `ClickClack is not configured`: tetapkan `channels.clickclack.token` atau `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found`: tetapkan `workspace` ke id atau slug ruang kerja yang dikembalikan oleh ClickClack.
  * Tidak ada balasan masuk: pastikan token memiliki akses baca realtime dan bot tidak membalas pesannya sendiri.
  * Pengiriman kanal gagal: verifikasi bahwa bot adalah anggota ruang kerja dan memiliki `bot:write`.


Was this useful?YesNo