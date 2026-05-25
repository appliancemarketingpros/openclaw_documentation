---
title: OC Path Plugin
source_url: https://docs.openclaw.ai/id/plugins/oc-path
scraped_at: 2026-05-25
---

Plugin `oc-path` bawaan menambahkan CLI [`openclaw path`](</id/cli/path>) untuk skema pengalamatan file-ruang kerja `oc://`. Plugin ini dikirim di repo OpenClaw di bawah `extensions/oc-path/` tetapi bersifat opt-in — install/build membiarkannya tidak aktif sampai Anda mengaktifkannya.

Alamat `oc://` menunjuk ke satu leaf (atau kumpulan leaf wildcard) di dalam file ruang kerja. Saat ini plugin memahami tiga jenis file:

  * **markdown** (`.md`, `.mdx`): frontmatter, section, item, field
  * **jsonc** (`.jsonc`, `.json5`, `.json`): komentar dan pemformatan dipertahankan
  * **jsonl** (`.jsonl`, `.ndjson`): record berorientasi baris


Self-hoster dan ekstensi editor menggunakan CLI untuk membaca atau menulis satu leaf tanpa membuat skrip langsung terhadap SDK; agen dan hook memperlakukannya sebagai substrat deterministik sehingga round-trip dengan fidelitas byte dan penjaga sentinel redaksi berlaku seragam di semua jenis.

## Mengapa mengaktifkannya

Aktifkan `oc-path` saat Anda ingin skrip, hook, atau tooling agen lokal menunjuk ke bagian state ruang kerja yang presisi tanpa menciptakan parser untuk tiap bentuk file. Satu alamat `oc://` dapat menamai kunci frontmatter markdown, item section, leaf konfigurasi JSONC, atau field event JSONL.

Itu penting untuk workflow maintainer ketika perubahan harus kecil, dapat diaudit, dan dapat diulang: periksa satu nilai, temukan record yang cocok, jalankan dry-run untuk penulisan, lalu terapkan hanya leaf tersebut sambil membiarkan komentar, line ending, dan pemformatan di sekitarnya tetap apa adanya. Menjaga ini sebagai plugin opt-in memberi power user substrat pengalamatan tanpa memasukkan dependensi parser atau surface CLI ke core untuk install yang tidak pernah membutuhkannya.

Alasan umum untuk mengaktifkannya:

  * **Otomasi lokal** : skrip shell dapat me-resolve atau memperbarui satu nilai ruang kerja dengan `openclaw path … --json` alih-alih membawa kode parsing markdown, JSONC, dan JSONL yang terpisah.
  * **Edit yang terlihat agen** : agen dapat menampilkan diff dry-run untuk satu leaf beralamat sebelum menulis, yang lebih mudah ditinjau daripada penulisan ulang file bebas.
  * **Integrasi editor** : editor dapat memetakan `oc://AGENTS.md/tools/gh` ke node markdown dan nomor baris yang tepat tanpa menebak dari teks heading.
  * **Diagnostik** : `emit` melakukan round-trip file melalui parser dan emitter, sehingga Anda dapat memeriksa apakah suatu jenis file stabil secara byte sebelum mengandalkan edit otomatis.


Contoh konkret:

bashCopy code
[code]
    # Is the GitHub plugin enabled in this config?openclaw path resolve 'oc://config.jsonc/plugins/github/enabled' --json # Which tool-call names appear in this session log?openclaw path find 'oc://session.jsonl/[event=tool_call]/name' --json # What bytes would this tiny config edit write?openclaw path set 'oc://config.jsonc/plugins/github/enabled' 'true' --dry-run
[/code]

Plugin ini sengaja bukan pemilik semantik tingkat lebih tinggi. Plugin memori tetap memiliki penulisan memori, perintah konfigurasi tetap memiliki manajemen konfigurasi penuh, dan logika LKG tetap memiliki restore/promosi. `oc-path` adalah lapisan pengalamatan sempit dan operasi file yang mempertahankan byte yang dapat dibangun oleh tool tingkat lebih tinggi tersebut.

## Tempat menjalankannya

Plugin berjalan **dalam proses di dalam CLI`openclaw`** pada host tempat Anda memanggil perintah. Plugin ini tidak memerlukan Gateway yang sedang berjalan dan tidak membuka socket jaringan apa pun — setiap verb adalah transformasi murni atas file yang Anda tunjuk.

Metadata plugin berada di `extensions/oc-path/openclaw.plugin.json`:

jsonCopy code
[code]
    {  "id": "oc-path",  "name": "OC Path",  "activation": {    "onStartup": false,    "onCommands": ["path"]  },  "commandAliases": [{ "name": "path", "kind": "cli" }]}
[/code]

`onStartup: false` menjaga plugin tetap di luar hot path Gateway. `onCommands: ["path"]` memberi tahu CLI untuk memuat plugin secara lazy saat pertama kali Anda menjalankan `openclaw path …`, sehingga install yang tidak pernah menggunakan verb tersebut tidak membayar biaya apa pun.

## Mengaktifkan

bashCopy code
[code]
    openclaw plugins enable oc-path
[/code]

Restart Gateway (jika Anda menjalankannya) agar snapshot manifest mengambil state baru. Pemanggilan `openclaw path` biasa langsung berfungsi pada host yang sama — CLI memuat plugin sesuai kebutuhan.

Nonaktifkan dengan:

bashCopy code
[code]
    openclaw plugins disable oc-path
[/code]

## Dependensi

Semua dependensi parser bersifat lokal plugin — mengaktifkan `oc-path` tidak menarik paket baru ke runtime core:

Dependensi | Tujuan  
---|---  
`commander` | Pengawatan subcommand untuk `resolve`, `find`, `set`, `validate`, `emit`.  
`jsonc-parser` | Parse JSONC + edit leaf dengan komentar dan trailing comma tetap dipertahankan.  
`markdown-it` | Tokenisasi Markdown untuk model section / item / field.  
  
JSONL tetap dibuat sendiri — parsing berorientasi baris lebih sederhana daripada dependensi apa pun, dan parse JSONC per baris sudah melalui `jsonc-parser`.

## Yang disediakannya

Surface | Disediakan oleh  
---|---  
CLI `openclaw path` | `extensions/oc-path/cli-registration.ts`  
Parser / formatter `oc://` | `extensions/oc-path/src/oc-path/oc-path.ts`  
Parse / emit / edit per jenis | `extensions/oc-path/src/oc-path/{md,jsonc,jsonl}`  
Universal resolve / find / set | `extensions/oc-path/src/oc-path/{resolve,find,edit}.ts`  
Penjaga sentinel redaksi | `extensions/oc-path/src/oc-path/sentinel.ts`  
  
CLI adalah satu-satunya surface publik saat ini. Verb substrat bersifat privat untuk plugin; konsumen menggunakan CLI (atau membangun plugin mereka sendiri terhadap SDK).

## Hubungan dengan plugin lain

  * **`memory-*`** : penulisan memori berjalan melalui plugin memori, bukan `oc-path`. `oc-path` adalah substrat file generik; plugin memori melapiskan semantiknya sendiri di atasnya.
  * **LKG** : `path` tidak tahu tentang restore konfigurasi Last-Known-Good. Jika suatu file dilacak LKG, panggilan `observe` berikutnya memutuskan apakah akan mempromosikan atau memulihkan; `set --batch` untuk multi-set atomik melalui lifecycle promosi/pemulihan LKG direncanakan bersama substrat pemulihan LKG.


## Keselamatan

`set` menulis byte mentah melalui jalur emit substrat, yang menerapkan penjaga sentinel redaksi secara otomatis. Leaf yang membawa `__OPENCLAW_REDACTED__` (verbatim atau sebagai substring) ditolak saat penulisan dengan `OC_EMIT_SENTINEL`. CLI juga membersihkan sentinel literal dari output manusia atau JSON apa pun yang dicetaknya, menggantinya dengan `[REDACTED]` sehingga tangkapan terminal dan pipeline tidak pernah membocorkan marker tersebut.

## Terkait

  * [Referensi CLI `openclaw path`](</id/cli/path>)
  * [Mengelola plugin](</id/plugins/manage-plugins>)
  * [Membangun plugin](</id/plugins/building-plugins>)


Was this useful?YesNo