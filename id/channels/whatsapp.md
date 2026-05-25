---
title: WhatsApp
source_url: https://docs.openclaw.ai/id/channels/whatsapp
scraped_at: 2026-05-25
---

Status: siap produksi melalui WhatsApp Web (Baileys). Gateway memiliki sesi tertaut.

## Instal (sesuai kebutuhan)

  * Onboarding (`openclaw onboard`) dan `openclaw channels add --channel whatsapp` meminta untuk memasang Plugin WhatsApp saat pertama kali Anda memilihnya.
  * `openclaw channels login --channel whatsapp` juga menawarkan alur instal saat Plugin belum tersedia.
  * Kanal dev + checkout git: default ke jalur Plugin lokal.
  * Stabil/Beta: menggunakan paket npm `@openclaw/whatsapp` pada tag rilis resmi saat ini.


Instal manual tetap tersedia:

bashCopy code
[code]
    openclaw plugins install @openclaw/whatsapp
[/code]

Gunakan paket bare untuk mengikuti tag rilis resmi saat ini. Pin versi yang tepat hanya saat Anda membutuhkan instal yang dapat direproduksi.

Di Windows, Plugin WhatsApp membutuhkan Git pada `PATH` selama instal npm karena salah satu dependensi Baileys/libsignal diambil dari URL git. Instal Git for Windows, lalu mulai ulang shell dan jalankan ulang instal:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git juga berfungsi jika direktori `bin`-nya ada di `PATH`.

[**Pairing** Kebijakan DM default adalah pairing untuk pengirim yang tidak dikenal. ](</id/channels/pairing>) [**Channel troubleshooting** Diagnostik lintas kanal dan playbook perbaikan. ](</id/channels/troubleshooting>) [**Gateway configuration** Pola dan contoh konfigurasi kanal lengkap. ](</id/gateway/configuration>)

## Penyiapan cepat

* ### Configure WhatsApp access policy

json5Copy code
[code]
    {channels: {whatsapp: {  dmPolicy: "pairing",  allowFrom: ["+15551234567"],  groupPolicy: "allowlist",  groupAllowFrom: ["+15551234567"],},},}
[/code]

* ### Link WhatsApp (QR)

bashCopy code
[code]
    openclaw channels login --channel whatsapp
[/code]

Untuk akun tertentu:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

Untuk melampirkan direktori auth WhatsApp Web yang sudah ada/kustom sebelum login:

bashCopy code
[code]
    openclaw channels add --channel whatsapp --account work --auth-dir /path/to/wa-authopenclaw channels login --channel whatsapp --account work
[/code]

* ### Start the gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Approve first pairing request (if using pairing mode)

bashCopy code
[code]
    openclaw pairing list whatsappopenclaw pairing approve whatsapp &lt;CODE&gt;
[/code]

Permintaan pairing kedaluwarsa setelah 1 jam. Permintaan tertunda dibatasi hingga 3 per kanal.

## Pola deployment

Dedicated number (recommended)

Ini adalah mode operasional yang paling bersih:

  * identitas WhatsApp terpisah untuk OpenClaw
  * allowlist DM dan batas routing yang lebih jelas
  * peluang kebingungan self-chat lebih rendah


Pola kebijakan minimal:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },  },}
[/code]

Personal-number fallback

Onboarding mendukung mode nomor pribadi dan menulis baseline yang ramah self-chat:

  * `dmPolicy: "allowlist"`
  * `allowFrom` menyertakan nomor pribadi Anda
  * `selfChatMode: true`


Saat runtime, perlindungan self-chat didasarkan pada nomor diri yang tertaut dan `allowFrom`.

WhatsApp Web-only channel scope

Kanal platform pesan didasarkan pada WhatsApp Web (`Baileys`) dalam arsitektur kanal OpenClaw saat ini.

Tidak ada kanal pesan Twilio WhatsApp terpisah dalam registry kanal chat bawaan.

## Model runtime

  * Gateway memiliki socket WhatsApp dan loop sambung ulang.
  * Watchdog sambung ulang menggunakan aktivitas transport WhatsApp Web, bukan hanya volume pesan aplikasi masuk, sehingga sesi perangkat tertaut yang sepi tidak dimulai ulang hanya karena belum ada yang mengirim pesan baru-baru ini. Batas kesunyian aplikasi yang lebih panjang tetap memaksa sambung ulang jika frame transport terus datang tetapi tidak ada pesan aplikasi yang ditangani selama jendela watchdog; setelah sambung ulang sementara untuk sesi yang baru aktif, pemeriksaan kesunyian aplikasi tersebut menggunakan timeout pesan normal untuk jendela pemulihan pertama.
  * Timing socket Baileys eksplisit di bawah `web.whatsapp.*`: `keepAliveIntervalMs` mengontrol ping aplikasi WhatsApp Web, `connectTimeoutMs` mengontrol timeout handshake pembuka, dan `defaultQueryTimeoutMs` mengontrol timeout kueri Baileys.
  * Pengiriman keluar membutuhkan listener WhatsApp aktif untuk akun target.
  * Pengiriman grup melampirkan metadata mention native untuk token `@+<digits>` dan `@<digits>` dalam teks dan caption media saat token cocok dengan metadata peserta WhatsApp saat ini, termasuk grup berbasis LID.
  * Chat status dan broadcast diabaikan (`@status`, `@broadcast`).
  * Watchdog sambung ulang mengikuti aktivitas transport WhatsApp Web, bukan hanya volume pesan aplikasi masuk: sesi perangkat tertaut yang sepi tetap aktif selama frame transport berlanjut, tetapi transport yang macet memaksa sambung ulang jauh sebelum jalur pemutusan jarak jauh yang lebih lambat.
  * Chat langsung menggunakan aturan sesi DM (`session.dmScope`; default `main` menggabungkan DM ke sesi utama agen).
  * Sesi grup diisolasi (`agent:<agentId>:whatsapp:group:<jid>`).
  * WhatsApp Channels/Newsletters dapat menjadi target keluar eksplisit dengan JID native `@newsletter`. Pengiriman newsletter keluar menggunakan metadata sesi kanal (`agent:<agentId>:whatsapp:channel:<jid>`) alih-alih semantik sesi DM.
  * Transport WhatsApp Web menghormati variabel lingkungan proxy standar pada host gateway (`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY` / varian huruf kecil). Lebih baik gunakan konfigurasi proxy tingkat host daripada pengaturan proxy WhatsApp khusus kanal.
  * Saat `messages.removeAckAfterReply` diaktifkan, OpenClaw menghapus reaksi ack WhatsApp setelah balasan yang terlihat terkirim.


## Hook Plugin dan privasi

Pesan masuk WhatsApp dapat berisi konten pesan pribadi, nomor telepon, pengidentifikasi grup, nama pengirim, dan kolom korelasi sesi. Karena itu, WhatsApp tidak menyiarkan payload hook `message_received` masuk ke Plugin kecuali Anda secara eksplisit memilih ikut:

json5Copy code
[code]
    {  channels: {    whatsapp: {      pluginHooks: {        messageReceived: true,      },    },  },}
[/code]

Anda dapat membatasi pilihan ikut ke satu akun:

json5Copy code
[code]
    {  channels: {    whatsapp: {      accounts: {        work: {          pluginHooks: {            messageReceived: true,          },        },      },    },  },}
[/code]

Aktifkan ini hanya untuk Plugin yang Anda percayai untuk menerima konten pesan WhatsApp masuk dan pengidentifikasi.

## Kontrol akses dan aktivasi

### DM policy

`channels.whatsapp.dmPolicy` mengontrol akses chat langsung:

  * `pairing` (default)
  * `allowlist`
  * `open` (membutuhkan `allowFrom` untuk menyertakan `"*"`)
  * `disabled`


`allowFrom` menerima nomor bergaya E.164 (dinormalisasi secara internal).

`allowFrom` adalah daftar kontrol akses pengirim DM. Ini tidak membatasi pengiriman keluar eksplisit ke JID grup WhatsApp atau JID kanal `@newsletter`.

Override multi-akun: `channels.whatsapp.accounts.<id>.dmPolicy` (dan `allowFrom`) lebih diprioritaskan daripada default tingkat kanal untuk akun tersebut.

Detail perilaku runtime:

  * pairing dipersistenkan dalam allow-store kanal dan digabungkan dengan `allowFrom` yang dikonfigurasi
  * otomatisasi terjadwal dan fallback penerima Heartbeat menggunakan target pengiriman eksplisit atau `allowFrom` yang dikonfigurasi; persetujuan pairing DM bukan penerima Cron atau Heartbeat implisit
  * jika tidak ada allowlist yang dikonfigurasi, nomor diri tertaut diizinkan secara default
  * OpenClaw tidak pernah melakukan auto-pair DM `fromMe` keluar (pesan yang Anda kirim kepada diri sendiri dari perangkat tertaut)


### Group policy + allowlists

Akses grup memiliki dua lapisan:

  1. **Allowlist keanggotaan grup** (`channels.whatsapp.groups`)

     * jika `groups` dihilangkan, semua grup memenuhi syarat
     * jika `groups` ada, ini bertindak sebagai allowlist grup (`"*"` diizinkan)
  2. **Kebijakan pengirim grup** (`channels.whatsapp.groupPolicy` \+ `groupAllowFrom`)

     * `open`: allowlist pengirim dilewati
     * `allowlist`: pengirim harus cocok dengan `groupAllowFrom` (atau `*`)
     * `disabled`: blokir semua grup masuk


Fallback allowlist pengirim:

  * jika `groupAllowFrom` tidak disetel, runtime fallback ke `allowFrom` bila tersedia
  * allowlist pengirim dievaluasi sebelum aktivasi mention/balasan


Catatan: jika blok `channels.whatsapp` sama sekali tidak ada, fallback kebijakan grup runtime adalah `allowlist` (dengan log peringatan), bahkan jika `channels.defaults.groupPolicy` disetel.

### Mentions + /activation

Balasan grup membutuhkan mention secara default.

Deteksi mention mencakup:

  * mention WhatsApp eksplisit atas identitas bot
  * pola regex mention yang dikonfigurasi (`agents.list[].groupChat.mentionPatterns`, fallback `messages.groupChat.mentionPatterns`)
  * transkrip voice-note masuk untuk pesan grup yang diotorisasi
  * deteksi balasan-ke-bot implisit (pengirim balasan cocok dengan identitas bot)


Catatan keamanan:

  * kutipan/balasan hanya memenuhi gerbang mention; itu **tidak** memberikan otorisasi pengirim
  * dengan `groupPolicy: "allowlist"`, pengirim yang tidak ada dalam allowlist tetap diblokir bahkan jika mereka membalas pesan pengguna yang ada dalam allowlist


Perintah aktivasi tingkat sesi:

  * `/activation mention`
  * `/activation always`


`activation` memperbarui status sesi (bukan konfigurasi global). Ini dibatasi oleh pemilik.

## Perilaku nomor pribadi dan self-chat

Saat nomor diri tertaut juga ada di `allowFrom`, pengaman self-chat WhatsApp aktif:

  * lewati tanda terima baca untuk giliran self-chat
  * abaikan perilaku pemicu otomatis mention-JID yang jika tidak akan melakukan ping ke diri sendiri
  * jika `messages.responsePrefix` tidak disetel, balasan self-chat default ke `[{identity.name}]` atau `[openclaw]`


## Normalisasi pesan dan konteks

Inbound envelope + reply context

Pesan WhatsApp masuk dibungkus dalam envelope masuk bersama.

Jika balasan yang dikutip ada, konteks ditambahkan dalam bentuk ini:

textCopy code
[code]
    [Replying to <sender> id:<stanzaId>]<quoted body or media placeholder>[/Replying]
[/code]

Kolom metadata balasan juga diisi bila tersedia (`ReplyToId`, `ReplyToBody`, `ReplyToSender`, JID/E.164 pengirim). Saat target balasan yang dikutip adalah media yang dapat diunduh, OpenClaw menyimpannya melalui penyimpanan media masuk normal dan mengeksposnya sebagai `MediaPath`/`MediaType` sehingga agen dapat memeriksa gambar yang dirujuk alih-alih hanya melihat `<media:image>`.

Media placeholders and location/contact extraction

Pesan masuk khusus media dinormalisasi dengan placeholder seperti:

  * `<media:image>`
  * `<media:video>`
  * `<media:audio>`
  * `<media:document>`
  * `<media:sticker>`


Voice note grup yang diotorisasi ditranskripsikan sebelum gerbang mention saat isi hanya `<media:audio>`, sehingga menyebut mention bot dalam voice note dapat memicu balasan. Jika transkrip masih tidak menyebut bot, transkrip disimpan dalam riwayat grup tertunda alih-alih placeholder mentah.

Isi lokasi menggunakan teks koordinat ringkas. Label/komentar lokasi dan detail kontak/vCard dirender sebagai metadata tidak tepercaya berpagar, bukan teks prompt inline.

Pending group history injection

Untuk grup, pesan yang belum diproses dapat dibuffer dan disuntikkan sebagai konteks saat bot akhirnya dipicu.

  * batas default: `50`
  * config: `channels.whatsapp.historyLimit`
  * fallback: `messages.groupChat.historyLimit`
  * `0` menonaktifkan


Penanda injeksi:

  * `[Pesan chat sejak balasan terakhir Anda - untuk konteks]`
  * `[Pesan saat ini - tanggapi ini]`

Tanda dibaca

Tanda dibaca diaktifkan secara default untuk pesan WhatsApp masuk yang diterima.

Nonaktifkan secara global:

json5Copy code
[code]
    {  channels: {    whatsapp: {      sendReadReceipts: false,    },  },}
[/code]

Override per akun:

json5Copy code
[code]
    {  channels: {    whatsapp: {      accounts: {        work: {          sendReadReceipts: false,        },      },    },  },}
[/code]

Giliran chat dengan diri sendiri melewati tanda dibaca meskipun diaktifkan secara global.

## Pengiriman, pemotongan, dan media

Pemotongan teks

  * batas potongan default: `channels.whatsapp.textChunkLimit = 4000`
  * `channels.whatsapp.chunkMode = "length" | "newline"`
  * mode `newline` mengutamakan batas paragraf (baris kosong), lalu fallback ke pemotongan aman berdasarkan panjang

Perilaku media keluar

  * mendukung payload gambar, video, audio (catatan suara PTT), dan dokumen
  * media audio dikirim melalui payload `audio` Baileys dengan `ptt: true`, sehingga klien WhatsApp merendernya sebagai catatan suara push-to-talk
  * payload balasan mempertahankan `audioAsVoice`; output catatan suara TTS untuk WhatsApp tetap menggunakan jalur PTT ini meskipun provider mengembalikan MP3 atau WebM
  * audio Ogg/Opus native dikirim sebagai `audio/ogg; codecs=opus` untuk kompatibilitas catatan suara
  * audio non-Ogg, termasuk output TTS MP3/WebM Microsoft Edge, ditranskode dengan `ffmpeg` ke Ogg/Opus mono 48 kHz sebelum pengiriman PTT
  * `/tts latest` mengirim balasan asisten terbaru sebagai satu catatan suara dan menekan pengiriman berulang untuk balasan yang sama; `/tts chat on|off|default` mengontrol TTS otomatis untuk chat WhatsApp saat ini
  * pemutaran GIF animasi didukung melalui `gifPlayback: true` pada pengiriman video
  * caption diterapkan ke item media pertama saat mengirim payload balasan multi-media, kecuali catatan suara PTT mengirim audio terlebih dahulu dan teks yang terlihat secara terpisah karena klien WhatsApp tidak merender caption catatan suara secara konsisten
  * sumber media dapat berupa HTTP(S), `file://`, atau path lokal

Batas ukuran media dan perilaku fallback

  * batas simpan media masuk: `channels.whatsapp.mediaMaxMb` (default `50`)
  * batas kirim media keluar: `channels.whatsapp.mediaMaxMb` (default `50`)
  * override per akun menggunakan `channels.whatsapp.accounts.<accountId>.mediaMaxMb`
  * gambar dioptimalkan otomatis (resize/penyesuaian kualitas) agar sesuai batas
  * saat pengiriman media gagal, fallback item pertama mengirim peringatan teks alih-alih membuang respons secara diam-diam


## Kutipan balasan

WhatsApp mendukung kutipan balasan native, di mana balasan keluar menampilkan kutipan pesan masuk. Kontrol dengan `channels.whatsapp.replyToMode`.

Nilai | Perilaku  
---|---  
`"off"` | Jangan pernah mengutip; kirim sebagai pesan biasa  
`"first"` | Kutip hanya potongan balasan keluar pertama  
`"all"` | Kutip setiap potongan balasan keluar  
`"batched"` | Kutip balasan antrean berbentuk batch sambil membiarkan balasan langsung tanpa kutipan  
  
Default adalah `"off"`. Override per akun menggunakan `channels.whatsapp.accounts.<id>.replyToMode`.

json5Copy code
[code]
    {  channels: {    whatsapp: {      replyToMode: "first",    },  },}
[/code]

## Level reaksi

`channels.whatsapp.reactionLevel` mengontrol seberapa luas agen menggunakan reaksi emoji di WhatsApp:

Level | Reaksi ack | Reaksi yang dimulai agen | Deskripsi  
---|---|---|---  
`"off"` | Tidak | Tidak | Tidak ada reaksi sama sekali  
`"ack"` | Ya | Tidak | Hanya reaksi ack (tanda terima pra-balasan)  
`"minimal"` | Ya | Ya (konservatif) | Ack + reaksi agen dengan panduan konservatif  
`"extensive"` | Ya | Ya (dianjurkan) | Ack + reaksi agen dengan panduan yang dianjurkan  
  
Default: `"minimal"`.

Override per akun menggunakan `channels.whatsapp.accounts.<id>.reactionLevel`.

json5Copy code
[code]
    {  channels: {    whatsapp: {      reactionLevel: "ack",    },  },}
[/code]

## Reaksi pengakuan

WhatsApp mendukung reaksi ack langsung pada tanda terima masuk melalui `channels.whatsapp.ackReaction`. Reaksi ack dibatasi oleh `reactionLevel` — reaksi ditekan saat `reactionLevel` adalah `"off"`.

json5Copy code
[code]
    {  channels: {    whatsapp: {      ackReaction: {        emoji: "👀",        direct: true,        group: "mentions", // always | mentions | never      },    },  },}
[/code]

Catatan perilaku:

  * dikirim segera setelah pesan masuk diterima (pra-balasan)
  * kegagalan dicatat di log tetapi tidak memblokir pengiriman balasan normal
  * mode grup `mentions` bereaksi pada giliran yang dipicu mention; aktivasi grup `always` bertindak sebagai bypass untuk pemeriksaan ini
  * WhatsApp menggunakan `channels.whatsapp.ackReaction` (`messages.ackReaction` legacy tidak digunakan di sini)


## Multi-akun dan kredensial

Pemilihan akun dan default

  * id akun berasal dari `channels.whatsapp.accounts`
  * pemilihan akun default: `default` jika ada, jika tidak id akun pertama yang dikonfigurasi (diurutkan)
  * id akun dinormalisasi secara internal untuk pencarian

Path kredensial dan kompatibilitas legacy

  * path auth saat ini: `~/.openclaw/credentials/whatsapp/<accountId>/creds.json`
  * file cadangan: `creds.json.bak`
  * auth default legacy di `~/.openclaw/credentials/` masih dikenali/dimigrasikan untuk alur akun default

Perilaku logout

`openclaw channels logout --channel whatsapp [--account <id>]` menghapus status auth WhatsApp untuk akun tersebut.

Saat Gateway dapat dijangkau, logout terlebih dahulu menghentikan listener WhatsApp live untuk akun yang dipilih sehingga sesi tertaut tidak terus menerima pesan hingga restart berikutnya. `openclaw channels remove --channel whatsapp` juga menghentikan listener live sebelum menonaktifkan atau menghapus config akun.

Di direktori auth legacy, `oauth.json` dipertahankan sementara file auth Baileys dihapus.

## Tool, tindakan, dan penulisan config

  * Dukungan tool agen mencakup tindakan reaksi WhatsApp (`react`).
  * Gerbang tindakan: 
    * `channels.whatsapp.actions.reactions`
    * `channels.whatsapp.actions.polls`
  * Penulisan config yang dimulai channel diaktifkan secara default (nonaktifkan melalui `channels.whatsapp.configWrites=false`).


## Pemecahan masalah

Tidak tertaut (QR diperlukan)

Gejala: status channel melaporkan tidak tertaut.

Perbaikan:

bashCopy code
[code]
    openclaw channels login --channel whatsappopenclaw channels status
[/code]

Tertaut tetapi terputus / loop sambung ulang

Gejala: akun tertaut dengan pemutusan berulang atau percobaan sambung ulang.

Akun yang sepi dapat tetap tersambung melewati timeout pesan normal; watchdog melakukan restart saat aktivitas transport WhatsApp Web berhenti, socket tertutup, atau aktivitas tingkat aplikasi tetap senyap melewati jendela keselamatan yang lebih panjang.

Jika log menampilkan `status=408 Request Time-out Connection was lost` berulang, sesuaikan timing socket Baileys di bawah `web.whatsapp`. Mulailah dengan memendekkan `keepAliveIntervalMs` di bawah timeout idle jaringan Anda dan meningkatkan `connectTimeoutMs` pada koneksi yang lambat atau sering kehilangan paket:

json5Copy code
[code]
    {  web: {    whatsapp: {      keepAliveIntervalMs: 15000,      connectTimeoutMs: 60000,      defaultQueryTimeoutMs: 60000,    },  },}
[/code]

Perbaikan:

bashCopy code
[code]
    openclaw doctoropenclaw logs --follow
[/code]

Jika `~/.openclaw/logs/whatsapp-health.log` mengatakan `Gateway inactive` tetapi `openclaw gateway status` dan `openclaw channels status --probe` menunjukkan bahwa gateway dan WhatsApp sehat, jalankan `openclaw doctor`. Di Linux, doctor memperingatkan tentang entri crontab legacy yang masih memanggil `~/.openclaw/bin/ensure-whatsapp.sh`; hapus entri usang tersebut dengan `crontab -e` karena cron dapat tidak memiliki lingkungan user-bus systemd dan membuat skrip lama itu salah melaporkan kesehatan gateway.

Jika diperlukan, tautkan ulang dengan `channels login`.

Login QR timeout di balik proxy

Gejala: `openclaw channels login --channel whatsapp` gagal sebelum menampilkan kode QR yang dapat digunakan dengan `status=408 Request Time-out` atau pemutusan socket TLS.

Login WhatsApp Web menggunakan lingkungan proxy standar host gateway (`HTTPS_PROXY`, `HTTP_PROXY`, varian huruf kecil, dan `NO_PROXY`). Verifikasi bahwa proses gateway mewarisi env proxy dan `NO_PROXY` tidak cocok dengan `mmg.whatsapp.net`.

Tidak ada listener aktif saat mengirim

Pengiriman keluar gagal cepat saat tidak ada listener gateway aktif untuk akun target.

Pastikan gateway berjalan dan akun tertaut.

Balasan muncul di transkrip tetapi tidak di WhatsApp

Baris transkrip mencatat apa yang dihasilkan agen. Pengiriman WhatsApp diperiksa secara terpisah: OpenClaw hanya menganggap auto-reply telah terkirim setelah Baileys mengembalikan id pesan keluar untuk setidaknya satu pengiriman teks atau media yang terlihat.

Reaksi ack adalah tanda terima pra-balasan yang independen. Reaksi yang berhasil tidak membuktikan bahwa balasan teks atau media berikutnya diterima oleh WhatsApp.

Periksa log gateway untuk `auto-reply delivery failed` atau `auto-reply was not accepted by WhatsApp provider`.

Pesan grup diabaikan secara tidak terduga

Periksa dalam urutan ini:

  * `groupPolicy`
  * `groupAllowFrom` / `allowFrom`
  * entri allowlist `groups`
  * gating mention (`requireMention` \+ pola mention)
  * kunci duplikat di `openclaw.json` (JSON5): entri yang lebih baru menimpa entri sebelumnya, jadi pertahankan satu `groupPolicy` per cakupan

Peringatan runtime Bun

Runtime gateway WhatsApp sebaiknya menggunakan Node. Bun ditandai sebagai tidak kompatibel untuk operasi gateway WhatsApp/Telegram yang stabil.

## Prompt sistem

WhatsApp mendukung prompt sistem bergaya Telegram untuk grup dan chat langsung melalui map `groups` dan `direct`.

Hierarki resolusi untuk pesan grup:

Map `groups` efektif ditentukan terlebih dahulu: jika akun mendefinisikan `groups` sendiri, map tersebut sepenuhnya menggantikan map `groups` root (tanpa deep merge). Pencarian prompt kemudian berjalan pada satu map yang dihasilkan:

  1. **Prompt sistem khusus grup** (`groups["<groupId>"].systemPrompt`): digunakan saat entri grup spesifik ada di map **dan** kunci `systemPrompt`-nya didefinisikan. Jika `systemPrompt` adalah string kosong (`""`), wildcard ditekan dan tidak ada prompt sistem yang diterapkan.
  2. **Prompt sistem wildcard grup** (`groups["*"].systemPrompt`): digunakan saat entri grup spesifik sama sekali tidak ada dari map, atau saat entri tersebut ada tetapi tidak mendefinisikan kunci `systemPrompt`.


Hierarki resolusi untuk pesan langsung:

Map `direct` efektif ditentukan terlebih dahulu: jika akun mendefinisikan `direct` sendiri, map tersebut sepenuhnya menggantikan map `direct` root (tanpa deep merge). Pencarian prompt kemudian berjalan pada satu map yang dihasilkan:

  1. **Prompt sistem khusus direct** (`direct["<peerId>"].systemPrompt`): digunakan ketika entri peer tertentu ada di map **dan** kunci `systemPrompt`-nya didefinisikan. Jika `systemPrompt` berupa string kosong (`""`), wildcard ditekan dan tidak ada prompt sistem yang diterapkan.
  2. **Prompt sistem wildcard direct** (`direct["*"].systemPrompt`): digunakan ketika entri peer tertentu sama sekali tidak ada di map, atau ketika entri itu ada tetapi tidak mendefinisikan kunci `systemPrompt`.


**Perbedaan dari perilaku multi-akun Telegram:** Di Telegram, root `groups` sengaja ditekan untuk semua akun dalam penyiapan multi-akun — bahkan akun yang tidak mendefinisikan `groups` sendiri — untuk mencegah bot menerima pesan grup untuk grup yang tidak diikutinya. WhatsApp tidak menerapkan pelindung ini: root `groups` dan root `direct` selalu diwarisi oleh akun yang tidak mendefinisikan override tingkat akun, terlepas dari berapa banyak akun yang dikonfigurasi. Dalam penyiapan WhatsApp multi-akun, jika Anda menginginkan prompt grup atau direct per akun, definisikan map lengkap di bawah setiap akun secara eksplisit alih-alih mengandalkan default tingkat root.

Perilaku penting:

  * `channels.whatsapp.groups` adalah map konfigurasi per grup sekaligus allowlist grup tingkat chat. Pada cakupan root maupun akun, `groups["*"]` berarti "semua grup diterima" untuk cakupan tersebut.
  * Tambahkan wildcard grup `systemPrompt` hanya ketika Anda memang ingin cakupan tersebut menerima semua grup. Jika Anda masih ingin hanya sekumpulan ID grup tetap yang memenuhi syarat, jangan gunakan `groups["*"]` untuk default prompt. Sebagai gantinya, ulangi prompt pada setiap entri grup yang di-allowlist secara eksplisit.
  * Penerimaan grup dan otorisasi pengirim adalah pemeriksaan terpisah. `groups["*"]` memperluas kumpulan grup yang dapat mencapai penanganan grup, tetapi itu sendiri tidak mengotorisasi setiap pengirim di grup tersebut. Akses pengirim tetap dikendalikan secara terpisah oleh `channels.whatsapp.groupPolicy` dan `channels.whatsapp.groupAllowFrom`.
  * `channels.whatsapp.direct` tidak memiliki efek samping yang sama untuk DM. `direct["*"]` hanya menyediakan konfigurasi chat direct default setelah DM sudah diterima oleh `dmPolicy` plus `allowFrom` atau aturan pairing-store.


Contoh:

json5Copy code
[code]
    {  channels: {    whatsapp: {      groups: {        // Use only if all groups should be admitted at the root scope.        // Applies to all accounts that do not define their own groups map.        "*": { systemPrompt: "Default prompt for all groups." },      },      direct: {        // Applies to all accounts that do not define their own direct map.        "*": { systemPrompt: "Default prompt for all direct chats." },      },      accounts: {        work: {          groups: {            // This account defines its own groups, so root groups are fully            // replaced. To keep a wildcard, define "*" explicitly here too.            "120363406415684625@g.us": {              requireMention: false,              systemPrompt: "Focus on project management.",            },            // Use only if all groups should be admitted in this account.            "*": { systemPrompt: "Default prompt for work groups." },          },          direct: {            // This account defines its own direct map, so root direct entries are            // fully replaced. To keep a wildcard, define "*" explicitly here too.            "+15551234567": { systemPrompt: "Prompt for a specific work direct chat." },            "*": { systemPrompt: "Default prompt for work direct chats." },          },        },      },    },  },}
[/code]

## Penunjuk referensi konfigurasi

Referensi utama:

  * [Referensi konfigurasi - WhatsApp](</id/gateway/config-channels#whatsapp>)


Field WhatsApp bernilai tinggi:

  * akses: `dmPolicy`, `allowFrom`, `groupPolicy`, `groupAllowFrom`, `groups`
  * pengiriman: `textChunkLimit`, `chunkMode`, `mediaMaxMb`, `sendReadReceipts`, `ackReaction`, `reactionLevel`
  * multi-akun: `accounts.<id>.enabled`, `accounts.<id>.authDir`, override tingkat akun
  * operasi: `configWrites`, `debounceMs`, `web.enabled`, `web.heartbeatSeconds`, `web.reconnect.*`, `web.whatsapp.*`
  * perilaku sesi: `session.dmScope`, `historyLimit`, `dmHistoryLimit`, `dms.<id>.historyLimit`
  * prompt: `groups.<id>.systemPrompt`, `groups["*"].systemPrompt`, `direct.<id>.systemPrompt`, `direct["*"].systemPrompt`


## Terkait

  * [Pairing](</id/channels/pairing>)
  * [Grup](</id/channels/groups>)
  * [Keamanan](</id/gateway/security>)
  * [Perutean channel](</id/channels/channel-routing>)
  * [Perutean multi-agent](</id/concepts/multi-agent>)
  * [Pemecahan masalah](</id/channels/troubleshooting>)


Was this useful?YesNo