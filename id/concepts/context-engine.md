---
title: Mesin konteks
source_url: https://docs.openclaw.ai/id/concepts/context-engine
scraped_at: 2026-05-25
---

Sebuah **mesin konteks** mengontrol bagaimana OpenClaw membangun konteks model untuk setiap proses: pesan mana yang disertakan, bagaimana meringkas riwayat lama, dan bagaimana mengelola konteks lintas batas subagent.

OpenClaw dilengkapi mesin bawaan `legacy` dan menggunakannya secara default - sebagian besar pengguna tidak perlu mengubah ini. Instal dan pilih mesin Plugin hanya ketika Anda menginginkan perilaku assembly, Compaction, atau pengingatan lintas-sesi yang berbeda.

## Mulai cepat

* ### Periksa mesin mana yang aktif

bashCopy code
[code]
    openclaw doctor# or inspect config directly:cat ~/.openclaw/openclaw.json | jq '.plugins.slots.contextEngine'
[/code]

* ### Instal mesin Plugin

Plugin mesin konteks diinstal seperti Plugin OpenClaw lainnya.

### Dari npm

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### Dari path lokal

bashCopy code
[code]
    openclaw plugins install -l ./my-context-engine
[/code]

* ### Aktifkan dan pilih mesin

json5Copy code
[code]
    // openclaw.json{  plugins: {    slots: {      contextEngine: "lossless-claw", // must match the plugin's registered engine id    },    entries: {      "lossless-claw": {        enabled: true,        // Plugin-specific config goes here (see the plugin's docs)      },    },  },}
[/code]

Mulai ulang gateway setelah menginstal dan mengonfigurasi.

* ### Beralih kembali ke legacy (opsional)

Atur `contextEngine` ke `"legacy"` (atau hapus kunci sepenuhnya - `"legacy"` adalah default).

## Cara kerjanya

Setiap kali OpenClaw menjalankan prompt model, mesin konteks berpartisipasi pada empat titik siklus hidup:

1\. Ingest

Dipanggil ketika pesan baru ditambahkan ke sesi. Mesin dapat menyimpan atau mengindeks pesan dalam penyimpanan datanya sendiri.

2\. Assemble

Dipanggil sebelum setiap proses model. Mesin mengembalikan sekumpulan pesan berurutan (dan `systemPromptAddition` opsional) yang sesuai dengan anggaran token.

3\. Compact

Dipanggil ketika jendela konteks penuh, atau ketika pengguna menjalankan `/compact`. Mesin meringkas riwayat lama untuk mengosongkan ruang.

4\. Setelah giliran

Dipanggil setelah proses selesai. Mesin dapat mempertahankan status, memicu Compaction latar belakang, atau memperbarui indeks.

Untuk harness Codex non-ACP bawaan, OpenClaw menerapkan siklus hidup yang sama dengan memproyeksikan konteks yang telah dirakit ke dalam instruksi developer Codex dan prompt giliran saat ini. Codex tetap memiliki riwayat thread native dan compactor native-nya sendiri.

### Siklus hidup subagent (opsional)

OpenClaw memanggil dua hook siklus hidup subagent opsional:

Siapkan status konteks bersama sebelum proses turunan dimulai. Hook menerima kunci sesi induk/turunan, `contextMode` (`isolated` atau `fork`), id/file transkrip yang tersedia, dan TTL opsional. Jika mengembalikan handle rollback, OpenClaw memanggilnya ketika spawn gagal setelah persiapan berhasil.

Bersihkan saat sesi subagent selesai atau disapu.

### Penambahan prompt sistem

Metode `assemble` dapat mengembalikan string `systemPromptAddition`. OpenClaw menambahkannya di awal prompt sistem untuk proses tersebut. Ini memungkinkan mesin menyuntikkan panduan pengingatan dinamis, instruksi retrieval, atau petunjuk sadar-konteks tanpa memerlukan file workspace statis.

## Mesin legacy

Mesin `legacy` bawaan mempertahankan perilaku asli OpenClaw:

  * **Ingest** : no-op (manajer sesi menangani persistensi pesan secara langsung).
  * **Assemble** : pass-through (pipeline sanitize → validate → limit yang ada di runtime menangani assembly konteks).
  * **Compact** : mendelegasikan ke Compaction peringkasan bawaan, yang membuat satu ringkasan pesan lama dan menjaga pesan terbaru tetap utuh.
  * **Setelah giliran** : no-op.


Mesin legacy tidak mendaftarkan alat atau menyediakan `systemPromptAddition`.

Ketika tidak ada `plugins.slots.contextEngine` yang ditetapkan (atau diatur ke `"legacy"`), mesin ini digunakan secara otomatis.

## Mesin Plugin

Sebuah Plugin dapat mendaftarkan mesin konteks menggunakan API Plugin:

tsCopy code
[code]
     export default function register(api) {  api.registerContextEngine("my-engine", (ctx) => ({    info: {      id: "my-engine",      name: "My Context Engine",      ownsCompaction: true,    },     async ingest({ sessionId, message, isHeartbeat }) {      // Store the message in your data store      return { ingested: true };    },     async assemble({ sessionId, messages, tokenBudget, availableTools, citationsMode }) {      // Return messages that fit the budget      return {        messages: buildContext(messages, tokenBudget),        estimatedTokens: countTokens(messages),        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },     async compact({ sessionId, force }) {      // Summarize older context      return { ok: true, compacted: true };    },  }));}
[/code]

Factory `ctx` mencakup nilai `config`, `agentDir`, dan `workspaceDir` opsional sehingga Plugin dapat menginisialisasi status per-agen atau per-workspace sebelum hook siklus hidup pertama berjalan.

Lalu aktifkan di config:

json5Copy code
[code]
    {  plugins: {    slots: {      contextEngine: "my-engine",    },    entries: {      "my-engine": {        enabled: true,      },    },  },}
[/code]

### Antarmuka ContextEngine

Anggota wajib:

Anggota | Jenis | Tujuan  
---|---|---  
`info` | Properti | Id mesin, nama, versi, dan apakah mesin memiliki Compaction  
`ingest(params)` | Metode | Menyimpan satu pesan  
`assemble(params)` | Metode | Membangun konteks untuk proses model (mengembalikan `AssembleResult`)  
`compact(params)` | Metode | Meringkas/mengurangi konteks  
  
`assemble` mengembalikan `AssembleResult` dengan:

Pesan berurutan yang akan dikirim ke model.

Perkiraan mesin atas total token dalam konteks yang dirakit. OpenClaw menggunakan ini untuk keputusan ambang Compaction dan pelaporan diagnostik.

Ditambahkan di awal prompt sistem.

Mengontrol estimasi token mana yang digunakan runner untuk precheck overflow preventif. Default-nya `"assembled"`, yang berarti hanya estimasi prompt yang telah dirakit yang diperiksa - sesuai untuk mesin yang mengembalikan konteks berjendela dan mandiri. Atur ke `"preassembly_may_overflow"` hanya ketika tampilan rakitan Anda dapat menyembunyikan risiko overflow dalam transkrip yang mendasarinya; runner kemudian mengambil maksimum dari estimasi rakitan dan estimasi riwayat sesi pra-assembly (tanpa jendela) saat memutuskan apakah akan melakukan Compaction secara preventif. Bagaimanapun, pesan yang Anda kembalikan tetap yang dilihat model - `promptAuthority` hanya memengaruhi precheck.

`compact` mengembalikan `CompactResult`. Ketika Compaction merotasi transkrip aktif, `result.sessionId` dan `result.sessionFile` mengidentifikasi sesi penerus yang harus digunakan oleh percobaan ulang atau giliran berikutnya.

Anggota opsional:

Anggota | Jenis | Tujuan  
---|---|---  
`bootstrap(params)` | Metode | Menginisialisasi status mesin untuk sesi. Dipanggil sekali saat mesin pertama kali melihat sesi (misalnya, impor riwayat).  
`ingestBatch(params)` | Metode | Mengingest giliran yang selesai sebagai batch. Dipanggil setelah proses selesai, dengan semua pesan dari giliran tersebut sekaligus.  
`afterTurn(params)` | Metode | Pekerjaan siklus hidup pasca-proses (mempertahankan status, memicu Compaction latar belakang).  
`prepareSubagentSpawn(params)` | Metode | Menyiapkan status bersama untuk sesi turunan sebelum dimulai.  
`onSubagentEnded(params)` | Metode | Membersihkan setelah subagent berakhir.  
`dispose()` | Metode | Melepaskan resource. Dipanggil saat gateway dimatikan atau Plugin dimuat ulang - bukan per sesi.  
  
### ownsCompaction

`ownsCompaction` mengontrol apakah auto-compaction bawaan dalam-percobaan milik Pi tetap aktif untuk proses tersebut:

ownsCompaction: true

Mesin memiliki perilaku Compaction. OpenClaw menonaktifkan auto-compaction bawaan Pi untuk proses tersebut, dan implementasi `compact()` milik mesin bertanggung jawab atas `/compact`, Compaction pemulihan overflow, dan Compaction proaktif apa pun yang ingin dilakukan di `afterTurn()`. OpenClaw mungkin masih menjalankan pengaman overflow pra-prompt; ketika memprediksi seluruh transkrip akan overflow, jalur pemulihan memanggil `compact()` milik mesin aktif sebelum mengirim prompt lain.

ownsCompaction: false atau tidak ditetapkan

Auto-compaction bawaan Pi mungkin masih berjalan selama eksekusi prompt, tetapi metode `compact()` milik mesin aktif tetap dipanggil untuk `/compact` dan pemulihan overflow.

Itu berarti ada dua pola Plugin yang valid:

### Mode memiliki

Implementasikan algoritma Compaction Anda sendiri dan tetapkan `ownsCompaction: true`.

### Mode delegasi

Tetapkan `ownsCompaction: false` dan buat `compact()` memanggil `delegateCompactionToRuntime(...)` dari `openclaw/plugin-sdk/core` untuk menggunakan perilaku Compaction bawaan OpenClaw.

`compact()` no-op tidak aman untuk mesin non-owning aktif karena menonaktifkan jalur Compaction normal `/compact` dan pemulihan overflow untuk slot mesin tersebut.

## Referensi konfigurasi

json5Copy code
[code]
    {  plugins: {    slots: {      // Select the active context engine. Default: "legacy".      // Set to a plugin id to use a plugin engine.      contextEngine: "legacy",    },  },}
[/code]

## Hubungan dengan Compaction dan memori

Compaction

Compaction adalah salah satu tanggung jawab mesin konteks. Mesin lama mendelegasikan ke peringkasan bawaan OpenClaw. Mesin Plugin dapat menerapkan strategi Compaction apa pun (ringkasan DAG, pengambilan vektor, dll.).

Plugin memori

Plugin memori (`plugins.slots.memory`) terpisah dari mesin konteks. Plugin memori menyediakan pencarian/pengambilan; mesin konteks mengontrol apa yang dilihat model. Keduanya dapat bekerja bersama - mesin konteks mungkin menggunakan data Plugin memori selama perakitan. Mesin Plugin yang menginginkan jalur prompt memori aktif sebaiknya menggunakan `buildMemorySystemPromptAddition(...)` dari `openclaw/plugin-sdk/core`, yang mengonversi bagian prompt memori aktif menjadi `systemPromptAddition` yang siap ditambahkan di awal. Jika sebuah mesin membutuhkan kontrol tingkat lebih rendah, mesin itu tetap dapat mengambil baris mentah dari `openclaw/plugin-sdk/memory-host-core` melalui `buildActiveMemoryPromptSection(...)`.

Pemangkasan sesi

Pemotongan hasil alat lama di memori tetap berjalan terlepas dari mesin konteks mana yang aktif.

## Tips

  * Gunakan `openclaw doctor` untuk memverifikasi mesin Anda dimuat dengan benar.
  * Jika beralih mesin, sesi yang ada terus berjalan dengan riwayatnya saat ini. Mesin baru mengambil alih untuk eksekusi berikutnya.
  * Kesalahan mesin dicatat dan ditampilkan dalam diagnostik. Jika mesin Plugin gagal didaftarkan atau id mesin yang dipilih tidak dapat diselesaikan, OpenClaw tidak otomatis beralih ke cadangan; eksekusi gagal sampai Anda memperbaiki Plugin atau mengalihkan `plugins.slots.contextEngine` kembali ke `"legacy"`.
  * Untuk pengembangan, gunakan `openclaw plugins install -l ./my-engine` untuk menautkan direktori Plugin lokal tanpa menyalin.


## Terkait

  * [Compaction](</id/concepts/compaction>) \- meringkas percakapan panjang
  * [Konteks](</id/concepts/context>) \- cara konteks dibangun untuk giliran agen
  * [Arsitektur Plugin](</id/plugins/architecture>) \- mendaftarkan Plugin mesin konteks
  * [Manifes Plugin](</id/plugins/manifest>) \- kolom manifes Plugin
  * [Plugin](</id/tools/plugin>) \- ikhtisar Plugin


Was this useful?YesNo