---
title: Jalur
source_url: https://docs.openclaw.ai/id/cli/path
scraped_at: 2026-05-25
---

# `openclaw path`

Akses shell yang disediakan Plugin ke substrat pengalamatan `oc://`: satu skema path yang dikirim berdasarkan jenis untuk memeriksa dan mengedit file workspace yang dapat dialamatkan (markdown, jsonc, jsonl). Self-hoster, penulis Plugin, dan ekstensi editor menggunakannya untuk membaca, menemukan, atau memperbarui lokasi sempit tanpa membuat parser per file sendiri.

CLI mencerminkan verba publik substrat:

  * `resolve` bersifat konkret dan cocok tunggal.
  * `find` adalah verba cocok jamak untuk wildcard, union, predikat, dan ekspansi posisional.
  * `set` hanya menerima path konkret atau penanda penyisipan; pola wildcard ditolak sebelum penulisan.


`path` disediakan oleh Plugin opsional bawaan `oc-path`. Aktifkan sebelum penggunaan pertama:

bashCopy code
[code]
    openclaw plugins enable oc-path
[/code]

## Mengapa menggunakannya

State OpenClaw tersebar di markdown yang diedit manusia, konfigurasi JSONC berkomentar, dan log JSONL append-only. Skrip shell, hook, dan agen sering memerlukan satu nilai kecil dari file-file tersebut: kunci frontmatter, setelan Plugin, field rekaman log, atau item bullet di bawah bagian bernama.

`openclaw path` memberi pemanggil tersebut alamat stabil alih-alih grep, regex, atau parser sekali pakai untuk setiap jenis file. Path `oc://` yang sama dapat divalidasi, di-resolve, dicari, dijalankan dry-run, dan ditulis dari terminal, yang membuat otomatisasi sempit lebih mudah ditinjau dan lebih aman diputar ulang. Ini sangat berguna ketika Anda ingin memperbarui satu leaf sambil mempertahankan komentar, akhir baris, dan pemformatan sekitar dari sisa file.

Gunakan saat hal yang Anda inginkan memiliki alamat logis, tetapi bentuk file fisiknya bervariasi:

  * Hook ingin membaca satu setelan dari JSONC berkomentar tanpa kehilangan komentar saat menulis nilainya kembali.
  * Skrip pemeliharaan ingin menemukan setiap field event yang cocok dalam log JSONL tanpa memuat seluruh log ke parser kustom.
  * Ekstensi editor ingin melompat ke bagian markdown atau item bullet berdasarkan slug, lalu merender baris persis yang di-resolve.
  * Agen ingin menjalankan dry-run edit workspace kecil sebelum menerapkannya, dengan byte yang berubah terlihat dalam tinjauan.


Anda mungkin tidak memerlukan `openclaw path` untuk edit seluruh file biasa, migrasi konfigurasi kaya, atau penulisan khusus memori. Itu sebaiknya menggunakan perintah atau Plugin pemilik. `path` ditujukan untuk operasi file kecil yang dapat dialamatkan, ketika perintah terminal yang dapat diulang lebih jelas daripada parser khusus lain.

## Cara menggunakannya

Baca satu nilai dari file konfigurasi yang diedit manusia:

bashCopy code
[code]
    openclaw path resolve 'oc://config.jsonc/plugins/github/enabled'
[/code]

Pratinjau penulisan tanpa menyentuh disk:

bashCopy code
[code]
    openclaw path set 'oc://config.jsonc/plugins/github/enabled' 'true' --dry-run
[/code]

Temukan rekaman yang cocok dalam log JSONL append-only:

bashCopy code
[code]
    openclaw path find 'oc://session.jsonl/[event=tool_call]/name'
[/code]

Alamatkan instruksi dalam markdown berdasarkan bagian dan item, bukan nomor baris:

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/runtime-safety/openclaw-gateway'
[/code]

Validasi path di CI atau skrip preflight sebelum skrip membaca atau menulis:

bashCopy code
[code]
    openclaw path validate 'oc://AGENTS.md/tools/$last/risk'
[/code]

Perintah-perintah tersebut dimaksudkan agar dapat disalin ke skrip shell. Gunakan `--json` saat pemanggil memerlukan output terstruktur dan `--human` saat seseorang sedang memeriksa hasilnya.

## Cara kerjanya

`openclaw path` melakukan empat hal:

  1. Mengurai alamat `oc://` menjadi slot: file, bagian, item, field, dan sesi opsional.
  2. Memilih adapter jenis file dari ekstensi target (`.md`, `.jsonc`, `.jsonl`, dan alias terkait).
  3. Me-resolve slot terhadap AST jenis file tersebut: heading/item markdown, kunci objek/indeks array JSONC, atau rekaman baris JSONL.
  4. Untuk `set`, menghasilkan byte yang diedit melalui adapter yang sama agar bagian file yang tidak disentuh mempertahankan komentar, akhir baris, dan pemformatan terdekat di tempat yang didukung jenis tersebut.


`resolve` dan `set` memerlukan satu target konkret. `find` adalah verba eksploratif: ia memperluas wildcard, union, predikat, dan ordinal menjadi kecocokan konkret yang dapat Anda periksa sebelum memilih satu untuk ditulis.

## Subperintah

Subperintah | Tujuan  
---|---  
`resolve <oc-path>` | Cetak kecocokan konkret pada path (atau "tidak ditemukan").  
`find <pattern>` | Enumerasi kecocokan untuk path wildcard / union / predikat.  
`set <oc-path> <value>` | Tulis leaf atau target penyisipan pada path konkret. Mendukung `--dry-run`.  
`validate <oc-path>` | Hanya mengurai; cetak uraian struktural (file / bagian / item / field).  
`emit <file>` | Round-trip file melalui `parseXxx` \+ `emitXxx` (diagnostik fidelitas byte).  
  
## Flag global

Flag | Tujuan  
---|---  
`--cwd <dir>` | Resolve slot file terhadap direktori ini (default: `process.cwd()`).  
`--file <path>` | Timpa path hasil resolve slot file (akses absolut).  
`--json` | Paksa output JSON (default saat stdout bukan TTY).  
`--human` | Paksa output manusia (default saat stdout adalah TTY).  
`--dry-run` | (hanya pada `set`) cetak byte yang akan ditulis tanpa menulis.  
  
## Sintaks `oc://`

CodeCopy code
[code]
    oc://FILE/SECTION/ITEM/FIELD?session=SCOPE
[/code]

Aturan slot: `field` memerlukan `item`, dan `item` memerlukan `section`. Di semua empat slot:

  * **Segmen yang dikutip** — `"a/b.c"` tetap bertahan melewati pemisah `/` dan `.`. Konten bersifat byte-literal; `"` dan `\` tidak diizinkan di dalam kutipan. Slot file juga peka kutipan: `oc://"skills/email-drafter"/Tools/$last` memperlakukan `skills/email-drafter` sebagai satu path file.
  * **Predikat** — `[k=v]`, `[k!=v]`, `[k<v]`, `[k<=v]`, `[k>v]`, `[k>=v]`. Operasi numerik mengharuskan kedua sisi dapat dikonversi menjadi angka hingga.
  * **Union** — `{a,b,c}` cocok dengan salah satu alternatif.
  * **Wildcard** — `*` (satu sub-segmen) dan `**` (nol-atau-lebih, rekursif). `find` menerima ini; `resolve` dan `set` menolaknya karena ambigu.
  * **Posisional** — `$last` di-resolve ke indeks terakhir / kunci terakhir yang dideklarasikan.
  * **Ordinal** — `#N` untuk kecocokan ke-N berdasarkan urutan dokumen.
  * **Penanda penyisipan** — `+`, `+key`, `+nnn` untuk penyisipan berkunci / berindeks (gunakan dengan `set`).
  * **Cakupan sesi** — `?session=cron-daily` dll. Ortogonal terhadap penyarangan slot. Nilai sesi bersifat mentah, tidak di-decode persen; tidak boleh berisi karakter kontrol atau pemisah query yang dicadangkan (`?`, `&`, `%`).


Karakter yang dicadangkan (`?`, `&`, `%`) di luar segmen yang dikutip, predikat, atau union ditolak. Karakter kontrol (U+0000-U+001F, U+007F) ditolak di mana pun, termasuk nilai query `session`.

`formatOcPath(parseOcPath(path)) === path` dijamin untuk path kanonis. Parameter query nonkanonis diabaikan kecuali nilai `session=` nonkosong pertama.

## Pengalamatan berdasarkan jenis file

Jenis | Model pengalamatan  
---|---  
Markdown | Bagian H2 berdasarkan slug, item bullet berdasarkan slug atau `#N`, frontmatter via `[frontmatter]`.  
JSONC/JSON | Kunci objek dan indeks array; titik memisahkan sub-segmen bertingkat kecuali dikutip.  
JSONL | Alamat baris tingkat atas (`L1`, `L2`, `$last`), lalu penurunan gaya JSONC di dalam baris.  
  
`resolve` mengembalikan kecocokan terstruktur: `root`, `node`, `leaf`, atau `insertion-point`, dengan nomor baris berbasis 1. Nilai leaf ditampilkan sebagai teks plus `leafType` sehingga penulis Plugin dapat merender pratinjau tanpa bergantung pada bentuk AST per jenis.

## Kontrak mutasi

`set` menulis satu target konkret:

  * Nilai frontmatter markdown dan field item `- key: value` adalah leaf string. Penyisipan markdown menambahkan bagian, kunci frontmatter, atau item bagian dan merender bentuk markdown kanonis untuk file yang berubah.
  * Penulisan leaf JSONC mengonversi nilai string ke tipe leaf yang ada (`string`, `number` hingga, `true`/`false`, atau `null`). Penyisipan objek dan array JSONC mengurai `<value>` sebagai JSON dan menggunakan jalur edit `jsonc-parser` untuk penulisan leaf biasa, sambil mempertahankan komentar dan pemformatan terdekat.
  * Penulisan leaf JSONL mengonversi seperti JSONC di dalam baris. Penggantian dan append seluruh baris mengurai `<value>` sebagai JSON. JSONL yang dirender mempertahankan konvensi akhir baris dominan file, LF/CRLF.


Gunakan `--dry-run` sebelum penulisan yang terlihat pengguna ketika byte persis penting. Substrat mempertahankan output identik byte untuk round-trip parse/emit, tetapi mutasi dapat mengkanoniskan wilayah yang diedit atau file tergantung jenisnya.

## Contoh

bashCopy code
[code]
    # Validate a path (no filesystem access)openclaw path validate 'oc://AGENTS.md/Tools/$last/risk' # Read a leafopenclaw path resolve 'oc://gateway.jsonc/version' # Wildcard searchopenclaw path find 'oc://session.jsonl/*/event' --file ./logs/session.jsonl # Dry-run a writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-run # Apply the writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' # Byte-fidelity round-trip (diagnostic)openclaw path emit ./AGENTS.md
[/code]

Contoh tata bahasa lainnya:

bashCopy code
[code]
    # Quote keys containing / or .openclaw path resolve 'oc://config.jsonc/agents.defaults.models/"anthropic/claude-opus-4-7"/alias' # Predicate search over JSONC childrenopenclaw path find 'oc://config.jsonc/plugins/[enabled=true]/id' # Insert into a JSONC arrayopenclaw path set 'oc://config.jsonc/items/+1' '{"id":"new","enabled":true}' --dry-run # Insert a JSONC object keyopenclaw path set 'oc://config.jsonc/plugins/+github' '{"enabled":true}' --dry-run # Append a JSONL eventopenclaw path set 'oc://session.jsonl/+' '{"event":"checkpoint","ok":true}' --file ./logs/session.jsonl # Resolve the last JSONL value lineopenclaw path resolve 'oc://session.jsonl/$last/event' --file ./logs/session.jsonl # Address markdown frontmatteropenclaw path resolve 'oc://AGENTS.md/[frontmatter]/name' # Insert markdown frontmatteropenclaw path set 'oc://AGENTS.md/[frontmatter]/+description' 'Agent instructions' --dry-run # Find markdown item fieldsopenclaw path find 'oc://SKILL.md/Tools/*/send_email' # Validate a session-scoped pathopenclaw path validate 'oc://AGENTS.md/Tools/$last/risk?session=cron-daily'
[/code]

## Resep berdasarkan jenis file

Lima verba yang sama bekerja lintas jenis; skema pengalamatan dikirim berdasarkan ekstensi file. Contoh di bawah menggunakan fixture dari deskripsi PR.

### Markdown

textCopy code
[code]
    <!-- frontmatter.md -->---name: drafterdescription: email drafting agenttier: core---## Tools- gh: GitHub CLI- curl: HTTP client- send_email: enabled
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://x.md/[frontmatter]/tier' --file frontmatter.md --humanleaf @ L4: "core" (string) $ openclaw path resolve 'oc://x.md/tools/gh/gh' --file frontmatter.md --humanleaf @ L9: "GitHub CLI" (string) $ openclaw path find 'oc://x.md/tools/*' --file frontmatter.md --human3 matches for oc://x.md/tools/*:  oc://x.md/tools/gh           →  node @ L9 [md-item]  oc://x.md/tools/curl         →  node @ L10 [md-item]  oc://x.md/tools/send-email   →  node @ L11 [md-item]
[/code]

Predikat `[frontmatter]` mengalamatkan blok frontmatter YAML; `tools` mencocokkan heading `## Tools` melalui slug, dan leaf item mempertahankan bentuk slug-nya bahkan ketika sumber menggunakan underscore (`send_email` → `send-email`).

### JSONC

textCopy code
[code]
    // config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": false, "role": "chat"}  }}
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://config.jsonc/plugins/github/enabled' --file config.jsonc --humanleaf @ L4: "true" (boolean) $ openclaw path set 'oc://config.jsonc/plugins/slack/enabled' 'true' --file config.jsonc --dry-run--dry-run: would write 142 bytes to /…/config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": true, "role": "chat"}  }}
[/code]

Pengeditan JSONC melewati `jsonc-parser`, sehingga komentar dan spasi kosong tetap bertahan setelah `set`. Jalankan dengan `--dry-run` terlebih dahulu untuk memeriksa byte sebelum melakukan commit.

### JSONL

textCopy code
[code]
    {"event":"start","userId":"u1","ts":1}{"event":"action","userId":"u1","ts":2}{"event":"end","userId":"u1","ts":3}
[/code]

bashCopy code
[code]
    $ openclaw path find 'oc://session.jsonl/[event=action]/userId' --file session.jsonl --human1 match for oc://session.jsonl/[event=action]/userId:  oc://session.jsonl/L2/userId  →  leaf @ L2: "u1" (string) $ openclaw path resolve 'oc://session.jsonl/L2/ts' --file session.jsonl --humanleaf @ L2: "2" (number)
[/code]

Setiap baris adalah sebuah rekaman. Alamatkan berdasarkan predikat (`[event=action]`) saat Anda tidak mengetahui nomor baris, atau berdasarkan segmen `LN` kanonis saat Anda mengetahuinya.

## Referensi subperintah

### `resolve <oc-path>`

Baca satu daun atau simpul. Wildcard ditolak — gunakan `find` untuk itu. Keluar dengan `0` pada kecocokan, `1` pada kegagalan bersih, `2` pada kesalahan penguraian atau pola yang ditolak.

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/tools/gh/risk' --humanopenclaw path resolve 'oc://gateway.jsonc/server/port' --json
[/code]

### `find <pattern>`

Enumerasikan setiap kecocokan untuk pola wildcard / predikat / gabungan. Keluar dengan `0` jika ada setidaknya satu kecocokan, `1` jika nol. Wildcard slot berkas ditolak dengan `OC_PATH_FILE_WILDCARD_UNSUPPORTED` — berikan berkas konkret (globbing multi-berkas adalah fitur lanjutan).

bashCopy code
[code]
    openclaw path find 'oc://AGENTS.md/tools/**/risk'openclaw path find 'oc://session.jsonl/[event=action]/userId'openclaw path find 'oc://config.jsonc/plugins/{github,slack}/enabled'
[/code]

### `set <oc-path> <value>`

Tulis sebuah daun. Pasangkan dengan `--dry-run` untuk meninjau byte yang akan ditulis tanpa menyentuh berkas. Keluar dengan `0` pada penulisan yang berhasil, `1` jika substrat menolak (misalnya, penjaga sentinel terkena), `2` pada kesalahan penguraian.

bashCopy code
[code]
    openclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-runopenclaw path set 'oc://gateway.jsonc/version' '2.0'openclaw path set 'oc://AGENTS.md/Tools/+gh/risk' 'low'
[/code]

Marker penyisipan `+key` membuat child bernama jika belum ada; `+nnn` dan `+` polos masing-masing berfungsi untuk penyisipan berindeks dan penyisipan append.

### `validate <oc-path>`

Pemeriksaan hanya parse. Tidak ada akses filesystem. Berguna ketika Anda ingin mengonfirmasi bahwa path template berbentuk benar sebelum mengganti variabel, atau ketika Anda menginginkan penguraian struktural untuk debugging:

bashCopy code
[code]
    $ openclaw path validate 'oc://AGENTS.md/tools/gh' --humanvalid: oc://AGENTS.md/tools/gh  file:    AGENTS.md  section: tools  item:    gh
[/code]

Keluar dengan `0` saat valid, `1` saat tidak valid (dengan `code` dan `message` terstruktur), `2` pada kesalahan argumen.

### `emit <file>`

Melakukan round-trip file melalui parser dan emitter per jenis. Keluaran seharusnya identik byte demi byte dengan masukan pada file yang valid — perbedaan menunjukkan bug parser atau sentinel yang terpicu. Berguna untuk debugging perilaku substrate pada masukan dunia nyata.

bashCopy code
[code]
    openclaw path emit ./AGENTS.mdopenclaw path emit ./gateway.jsonc --json
[/code]

## Kode keluar

Kode | Makna  
---|---  
`0` | Berhasil. (`resolve` / `find`: setidaknya satu kecocokan. `set`: penulisan berhasil.)  
`1` | Tidak ada kecocokan, atau `set` ditolak oleh substrate (tidak ada kesalahan tingkat sistem).  
`2` | Kesalahan argumen atau parse.  
  
## Mode keluaran

`openclaw path` peka terhadap TTY: keluaran yang dapat dibaca manusia di terminal, JSON ketika stdout disalurkan atau dialihkan. `--json` dan `--human` menggantikan deteksi otomatis.

## Catatan

  * `set` menulis byte melalui path emit milik substrate, yang menerapkan penjaga sentinel redaksi secara otomatis. Leaf yang membawa `__OPENCLAW_REDACTED__` (verbatim atau sebagai substring) ditolak pada waktu tulis.
  * Parsing JSONC dan pengeditan leaf menggunakan dependensi `jsonc-parser` lokal Plugin, sehingga komentar dan pemformatan dipertahankan pada penulisan leaf biasa alih-alih melalui path parser/render ulang buatan sendiri.
  * `path` tidak mengetahui LKG. Jika file dilacak oleh LKG, panggilan observe berikutnya memutuskan apakah akan mempromosikan / memulihkan. `set --batch` untuk multi-set atomik melalui siklus hidup promosi/pemulihan LKG direncanakan bersama substrate pemulihan LKG.


## Terkait

  * [Referensi CLI](</id/cli>)


Was this useful?YesNo