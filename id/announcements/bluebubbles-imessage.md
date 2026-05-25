---
title: Penghapusan BlueBubbles dan jalur iMessage imsg
source_url: https://docs.openclaw.ai/id/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Penghapusan BlueBubbles dan jalur iMessage imsg

OpenClaw tidak lagi menyertakan saluran BlueBubbles. Dukungan iMessage kini berjalan melalui Plugin `imessage` bawaan, yang menjalankan [`imsg`](<https://github.com/steipete/imsg>) secara lokal atau melalui pembungkus SSH dan berkomunikasi menggunakan JSON-RPC melalui stdin/stdout.

Jika konfigurasi Anda masih berisi `channels.bluebubbles`, migrasikan ke `channels.imessage`. URL dokumentasi lama `/channels/bluebubbles` mengalihkan ke [Beralih dari BlueBubbles](</id/channels/imessage-from-bluebubbles>), yang memiliki tabel lengkap penerjemahan konfigurasi dan daftar periksa cutover.

## Yang berubah

  * Tidak ada server HTTP BlueBubbles, rute Webhook, kata sandi REST, atau runtime Plugin BlueBubbles dalam jalur iMessage OpenClaw yang didukung.
  * OpenClaw membaca dan memantau Messages melalui `imsg` pada Mac tempat Messages.app sudah masuk.
  * Pengiriman, penerimaan, riwayat, dan media dasar menggunakan surface `imsg` normal dan izin macOS.
  * Tindakan lanjutan seperti balasan berutas, tapback, edit, batal kirim, efek, tanda terima baca, indikator mengetik, dan manajemen grup memerlukan `imsg launch` dengan bridge API privat yang tersedia.
  * Gateway Linux dan Windows masih dapat menggunakan iMessage dengan mengatur `channels.imessage.cliPath` ke pembungkus SSH yang menjalankan `imsg` pada Mac yang sudah masuk.


## Yang perlu dilakukan

  1. Instal dan verifikasi `imsg` pada Mac Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Berikan izin Full Disk Access dan Automation ke konteks proses yang menjalankan `imsg` dan OpenClaw.

  3. Terjemahkan konfigurasi lama:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Mulai ulang Gateway dan verifikasi:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Uji DM, grup, lampiran, dan tindakan API privat apa pun yang Anda andalkan sebelum menghapus server BlueBubbles lama Anda.


## Catatan migrasi

  * `channels.bluebubbles.serverUrl` dan `channels.bluebubbles.password` tidak memiliki padanan iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, root lampiran, batas ukuran media, chunking, dan toggle tindakan memiliki padanan iMessage.
  * `channels.imessage.includeAttachments` tetap nonaktif secara default. Atur secara eksplisit jika Anda mengharapkan foto, memo suara, video, atau file masuk mencapai agen.
  * Dengan `groupPolicy: "allowlist"`, salin blok `groups` lama, termasuk entri wildcard `"*"` apa pun. Daftar yang diizinkan pengirim grup dan registri grup adalah gate terpisah.
  * Binding ACP yang cocok dengan `channel: "bluebubbles"` harus diubah menjadi `channel: "imessage"`.
  * Kunci sesi BlueBubbles lama tidak menjadi kunci sesi iMessage. Persetujuan pairing terbawa berdasarkan handle, tetapi riwayat percakapan di bawah kunci sesi BlueBubbles tidak.


## Lihat juga

  * [Beralih dari BlueBubbles](</id/channels/imessage-from-bluebubbles>)
  * [iMessage](</id/channels/imessage>)
  * [Referensi konfigurasi - iMessage](</id/gateway/config-channels#imessage>)


Was this useful?YesNo