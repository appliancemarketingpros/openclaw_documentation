---
title: BARIS
source_url: https://docs.openclaw.ai/id/channels/line
scraped_at: 2026-05-25
---

LINE terhubung ke OpenClaw melalui LINE Messaging API. Plugin berjalan sebagai penerima webhook di gateway dan menggunakan token akses saluran + rahasia saluran Anda untuk autentikasi.

Status: plugin yang dapat diunduh. Pesan langsung, obrolan grup, media, lokasi, pesan Flex, pesan template, dan balasan cepat didukung. Reaksi dan utas tidak didukung.

## Instal

Instal LINE sebelum mengonfigurasi saluran:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Checkout lokal (saat berjalan dari repo git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Penyiapan

  1. Buat akun LINE Developers dan buka Console: <https://developers.line.biz/console/>
  2. Buat (atau pilih) Provider dan tambahkan saluran **Messaging API**.
  3. Salin **Channel access token** dan **Channel secret** dari pengaturan saluran.
  4. Aktifkan **Use webhook** di pengaturan Messaging API.
  5. Atur URL webhook ke endpoint gateway Anda (HTTPS wajib):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

Gateway merespons verifikasi webhook LINE (GET) dan peristiwa masuk (POST). Jika Anda memerlukan path khusus, atur `channels.line.webhookPath` atau `channels.line.accounts.<id>.webhookPath` dan perbarui URL sesuai kebutuhan.

Catatan keamanan:

  * Verifikasi tanda tangan LINE bergantung pada body (HMAC atas body mentah), sehingga OpenClaw menerapkan batas body pra-autentikasi yang ketat dan timeout sebelum verifikasi.
  * OpenClaw memproses peristiwa webhook dari byte permintaan mentah yang terverifikasi. Nilai `req.body` yang ditransformasi middleware upstream diabaikan demi keamanan integritas tanda tangan.


## Konfigurasi

Konfigurasi minimal:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Konfigurasi DM publik:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Variabel env (hanya akun default):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


File token/rahasia:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` dan `secretFile` harus menunjuk ke file reguler. Symlink ditolak.

Beberapa akun:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Kontrol akses

Pesan langsung secara default menggunakan pairing. Pengirim yang tidak dikenal menerima kode pairing dan pesan mereka diabaikan sampai disetujui.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Allowlist dan kebijakan:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: ID pengguna LINE yang di-allowlist untuk DM; `dmPolicy: "open"` memerlukan `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: ID pengguna LINE yang di-allowlist untuk grup
  * Override per grup: `channels.line.groups.<groupId>.allowFrom`
  * Grup akses pengirim statis dapat direferensikan dari `allowFrom`, `groupAllowFrom`, dan `allowFrom` per grup dengan `accessGroup:<name>`.
  * Catatan runtime: jika `channels.line` sepenuhnya tidak ada, runtime kembali ke `groupPolicy="allowlist"` untuk pemeriksaan grup (meskipun `channels.defaults.groupPolicy` diatur).


ID LINE peka huruf besar/kecil. ID valid terlihat seperti:

  * Pengguna: `U` \+ 32 karakter hex
  * Grup: `C` \+ 32 karakter hex
  * Room: `R` \+ 32 karakter hex


## Perilaku pesan

  * Teks dipotong menjadi bagian 5000 karakter.
  * Pemformatan Markdown dihapus; blok kode dan tabel dikonversi menjadi kartu Flex jika memungkinkan.
  * Respons streaming dibuffer; LINE menerima bagian lengkap dengan animasi pemuatan saat agen bekerja.
  * Unduhan media dibatasi oleh `channels.line.mediaMaxMb` (default 10).
  * Media masuk disimpan di bawah `~/.openclaw/media/inbound/` sebelum diteruskan ke agen, sesuai dengan penyimpanan media bersama yang digunakan oleh plugin saluran bawaan lainnya.


## Data saluran (pesan kaya)

Gunakan `channelData.line` untuk mengirim balasan cepat, lokasi, kartu Flex, atau pesan template.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

Plugin LINE juga menyertakan perintah `/card` untuk preset pesan Flex:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## Dukungan ACP

LINE mendukung binding percakapan ACP (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` mengikat obrolan LINE saat ini ke sesi ACP tanpa membuat utas anak.
  * Binding ACP yang dikonfigurasi dan sesi ACP aktif yang terikat percakapan berfungsi di LINE seperti saluran percakapan lainnya.


Lihat [agen ACP](</id/tools/acp-agents>) untuk detail.

## Media keluar

Plugin LINE mendukung pengiriman gambar, video, dan file audio melalui alat pesan agen. Media dikirim melalui path pengiriman khusus LINE dengan penanganan pratinjau dan pelacakan yang sesuai:

  * **Gambar** : dikirim sebagai pesan gambar LINE dengan pembuatan pratinjau otomatis.
  * **Video** : dikirim dengan penanganan pratinjau eksplisit dan content-type.
  * **Audio** : dikirim sebagai pesan audio LINE.


URL media keluar harus berupa URL HTTPS publik. OpenClaw memvalidasi hostname target sebelum menyerahkan URL ke LINE dan menolak target loopback, link-local, dan jaringan privat.

Pengiriman media generik fallback ke rute khusus gambar yang sudah ada saat path khusus LINE tidak tersedia.

## Pemecahan masalah

  * **Verifikasi webhook gagal:** pastikan URL webhook menggunakan HTTPS dan `channelSecret` cocok dengan console LINE.
  * **Tidak ada peristiwa masuk:** pastikan path webhook cocok dengan `channels.line.webhookPath` dan gateway dapat dijangkau dari LINE.
  * **Kesalahan unduhan media:** naikkan `channels.line.mediaMaxMb` jika media melebihi batas default.


## Terkait

  * [Ikhtisar Saluran](</id/channels>) — semua saluran yang didukung
  * [Pairing](</id/channels/pairing>) — autentikasi DM dan alur pairing
  * [Grup](</id/channels/groups>) — perilaku obrolan grup dan gating mention
  * [Perutean Saluran](</id/channels/channel-routing>) — perutean sesi untuk pesan
  * [Keamanan](</id/gateway/security>) — model akses dan hardening


Was this useful?YesNo