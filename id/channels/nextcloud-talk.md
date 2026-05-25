---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/id/channels/nextcloud-talk
scraped_at: 2026-05-25
---

Status: Plugin bawaan (bot Webhook). Pesan langsung, ruang, reaksi, dan pesan markdown didukung.

## Plugin bawaan

Nextcloud Talk disertakan sebagai Plugin bawaan dalam rilis OpenClaw saat ini, sehingga build paket normal tidak memerlukan instalasi terpisah.

Jika Anda menggunakan build lama atau instalasi kustom yang mengecualikan Nextcloud Talk, instal paket npm secara langsung:

Instal melalui CLI (registri npm):

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

Gunakan paket polos untuk mengikuti tag rilis resmi saat ini. Sematkan versi yang tepat hanya saat Anda memerlukan instalasi yang dapat direproduksi.

Checkout lokal (saat menjalankan dari repo git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

Detail: [Plugin](</id/tools/plugin>)

## Penyiapan cepat (pemula)

  1. Pastikan Plugin Nextcloud Talk tersedia.

     * Rilis paket OpenClaw saat ini sudah menyertakannya.
     * Instalasi lama/kustom dapat menambahkannya secara manual dengan perintah di atas.
  2. Di server Nextcloud Anda, buat bot:

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. Aktifkan bot di pengaturan ruang target.

  4. Konfigurasikan OpenClaw:

     * Konfigurasi: `channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * Atau env: `NEXTCLOUD_TALK_BOT_SECRET` (hanya akun default)

Penyiapan CLI:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

Field eksplisit yang setara:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

Rahasia berbasis file:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. Mulai ulang Gateway (atau selesaikan penyiapan).


Konfigurasi minimal:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## Catatan

  * Bot tidak dapat memulai DM. Pengguna harus mengirim pesan ke bot terlebih dahulu.
  * URL Webhook harus dapat dijangkau oleh Gateway; tetapkan `webhookPublicUrl` jika berada di belakang proxy.
  * Unggahan media tidak didukung oleh API bot; media dikirim sebagai URL.
  * Payload Webhook tidak membedakan DM dan ruang; tetapkan `apiUser` \+ `apiPassword` untuk mengaktifkan pencarian tipe ruang (jika tidak, DM diperlakukan sebagai ruang).


## Kontrol akses (DM)

  * Default: `channels.nextcloud-talk.dmPolicy = "pairing"`. Pengirim yang tidak dikenal mendapatkan kode pairing.
  * Setujui melalui: 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * DM publik: `channels.nextcloud-talk.dmPolicy="open"` plus `channels.nextcloud-talk.allowFrom=["*"]`.
  * `allowFrom` hanya mencocokkan ID pengguna Nextcloud; nama tampilan diabaikan.


## Ruang (grup)

  * Default: `channels.nextcloud-talk.groupPolicy = "allowlist"` (dibatasi penyebutan).
  * Izinkan ruang dengan `channels.nextcloud-talk.rooms`:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * Untuk tidak mengizinkan ruang apa pun, biarkan allowlist kosong atau tetapkan `channels.nextcloud-talk.groupPolicy="disabled"`.


## Kapabilitas

Fitur | Status  
---|---  
Pesan langsung | Didukung  
Ruang | Didukung  
Thread | Tidak didukung  
Media | Hanya URL  
Reaksi | Didukung  
Perintah native | Tidak didukung  
  
## Referensi konfigurasi (Nextcloud Talk)

Konfigurasi lengkap: [Konfigurasi](</id/gateway/configuration>)

Opsi penyedia:

  * `channels.nextcloud-talk.enabled`: aktifkan/nonaktifkan startup saluran.
  * `channels.nextcloud-talk.baseUrl`: URL instance Nextcloud.
  * `channels.nextcloud-talk.botSecret`: rahasia bersama bot.
  * `channels.nextcloud-talk.botSecretFile`: path rahasia file reguler. Symlink ditolak.
  * `channels.nextcloud-talk.apiUser`: pengguna API untuk pencarian ruang (deteksi DM).
  * `channels.nextcloud-talk.apiPassword`: kata sandi API/aplikasi untuk pencarian ruang.
  * `channels.nextcloud-talk.apiPasswordFile`: path file kata sandi API.
  * `channels.nextcloud-talk.webhookPort`: port listener Webhook (default: 8788).
  * `channels.nextcloud-talk.webhookHost`: host Webhook (default: 0.0.0.0).
  * `channels.nextcloud-talk.webhookPath`: path Webhook (default: /nextcloud-talk-webhook).
  * `channels.nextcloud-talk.webhookPublicUrl`: URL Webhook yang dapat dijangkau secara eksternal.
  * `channels.nextcloud-talk.dmPolicy`: `pairing | allowlist | open | disabled`.
  * `channels.nextcloud-talk.allowFrom`: allowlist DM (ID pengguna). `open` memerlukan `"*"`.
  * `channels.nextcloud-talk.groupPolicy`: `allowlist | open | disabled`.
  * `channels.nextcloud-talk.groupAllowFrom`: allowlist grup (ID pengguna).
  * `channels.nextcloud-talk.rooms`: pengaturan per ruang dan allowlist.
  * Grup akses pengirim statis dapat direferensikan dari `allowFrom` dan `groupAllowFrom` dengan `accessGroup:<name>`.
  * `channels.nextcloud-talk.historyLimit`: batas riwayat grup (0 menonaktifkan).
  * `channels.nextcloud-talk.dmHistoryLimit`: batas riwayat DM (0 menonaktifkan).
  * `channels.nextcloud-talk.dms`: override per DM (historyLimit).
  * `channels.nextcloud-talk.textChunkLimit`: ukuran chunk teks keluar (karakter).
  * `channels.nextcloud-talk.chunkMode`: `length` (default) atau `newline` untuk memisahkan pada baris kosong (batas paragraf) sebelum chunking berdasarkan panjang.
  * `channels.nextcloud-talk.blockStreaming`: nonaktifkan streaming blok untuk saluran ini.
  * `channels.nextcloud-talk.blockStreamingCoalesce`: penyesuaian coalesce streaming blok.
  * `channels.nextcloud-talk.mediaMaxMb`: batas media masuk (MB).


## Terkait

  * [Ikhtisar Saluran](</id/channels>) — semua saluran yang didukung
  * [Pairing](</id/channels/pairing>) — autentikasi DM dan alur pairing
  * [Grup](</id/channels/groups>) — perilaku chat grup dan pembatasan penyebutan
  * [Perutean Saluran](</id/channels/channel-routing>) — perutean sesi untuk pesan
  * [Keamanan](</id/gateway/security>) — model akses dan hardening


Was this useful?YesNo