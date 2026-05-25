---
title: Mode dengan hak istimewa tinggi
source_url: https://docs.openclaw.ai/id/tools/elevated
scraped_at: 2026-05-25
---

Saat agen berjalan di dalam lingkungan terisolasi, perintah `exec`-nya dibatasi pada lingkungan terisolasi tersebut. **Mode elevated** memungkinkan agen keluar dan menjalankan perintah di luar lingkungan terisolasi, dengan gerbang persetujuan yang dapat dikonfigurasi.

## Direktif

Kendalikan mode elevated per sesi dengan perintah slash:

Direktif | Fungsinya  
---|---  
`/elevated on` | Jalankan di luar sandbox pada jalur host yang dikonfigurasi, pertahankan persetujuan  
`/elevated ask` | Sama seperti `on` (alias)  
`/elevated full` | Jalankan di luar sandbox pada jalur host yang dikonfigurasi dan lewati persetujuan  
`/elevated off` | Kembali ke eksekusi yang dibatasi sandbox  
  
Juga tersedia sebagai `/elev on|off|ask|full`.

Kirim `/elevated` tanpa argumen untuk melihat level saat ini.

## Cara kerjanya

* ### Periksa ketersediaan

Elevated harus diaktifkan di konfigurasi dan pengirim harus ada di allowlist:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Atur level

Kirim pesan yang hanya berisi direktif untuk mengatur default sesi:

CodeCopy code
[code]
    /elevated full
[/code]

Atau gunakan secara inline (hanya berlaku untuk pesan tersebut):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Perintah berjalan di luar sandbox

Dengan elevated aktif, panggilan `exec` keluar dari sandbox. Host efektif adalah `gateway` secara default, atau `node` saat target exec yang dikonfigurasi/sesi adalah `node`. Dalam mode `full`, persetujuan exec dilewati. Dalam mode `on`/`ask`, aturan persetujuan yang dikonfigurasi tetap berlaku.

## Urutan resolusi

  1. **Direktif inline** pada pesan (hanya berlaku untuk pesan tersebut)
  2. **Override sesi** (diatur dengan mengirim pesan yang hanya berisi direktif)
  3. **Default global** (`agents.defaults.elevatedDefault` di konfigurasi)


## Ketersediaan dan allowlist

  * **Gerbang global** : `tools.elevated.enabled` (harus `true`)
  * **Allowlist pengirim** : `tools.elevated.allowFrom` dengan daftar per kanal
  * **Gerbang per agen** : `agents.list[].tools.elevated.enabled` (hanya dapat semakin membatasi)
  * **Allowlist per agen** : `agents.list[].tools.elevated.allowFrom` (pengirim harus cocok dengan global + per agen)
  * **Fallback Discord** : jika `tools.elevated.allowFrom.discord` dihilangkan, `channels.discord.allowFrom` digunakan sebagai fallback
  * **Semua gerbang harus lolos** ; jika tidak, elevated dianggap tidak tersedia


Format entri allowlist:

Prefiks | Cocok dengan  
---|---  
(tidak ada) | ID pengirim, E.164, atau kolom From  
`name:` | Nama tampilan pengirim  
`username:` | Nama pengguna pengirim  
`tag:` | Tag pengirim  
`id:`, `from:`, `e164:` | Penargetan identitas eksplisit  
  
## Yang tidak dikendalikan elevated

  * **Kebijakan tool** : jika `exec` ditolak oleh kebijakan tool, elevated tidak dapat menimpanya.
  * **Kebijakan pemilihan host** : elevated tidak mengubah `auto` menjadi override lintas-host bebas. Elevated menggunakan aturan target exec yang dikonfigurasi/sesi, memilih `node` hanya saat target sudah `node`.
  * **Terpisah dari`/exec`**: direktif `/exec` menyesuaikan default exec per sesi untuk pengirim resmi dan tidak memerlukan mode elevated.


## Terkait

[**Tool exec** Eksekusi perintah shell dari agen. ](</id/tools/exec>) [**Persetujuan exec** Sistem persetujuan dan allowlist untuk `exec`. ](</id/tools/exec-approvals>) [**Sandboxing** Konfigurasi sandbox tingkat Gateway. ](</id/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Cara ketiga gerbang tersusun selama panggilan tool. ](</id/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo