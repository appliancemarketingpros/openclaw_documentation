---
title: Plugin lokakarya keterampilan
source_url: https://docs.openclaw.ai/id/plugins/skill-workshop
scraped_at: 2026-05-25
---

Skill Workshop bersifat **eksperimental**. Fitur ini dinonaktifkan secara default, heuristik capture dan prompt reviewer-nya dapat berubah antar-rilis, dan penulisan otomatis sebaiknya hanya digunakan di workspace tepercaya setelah meninjau output pending-mode terlebih dahulu.

Skill Workshop adalah memori prosedural untuk Skills workspace. Fitur ini memungkinkan agen mengubah alur kerja yang dapat digunakan ulang, koreksi pengguna, perbaikan yang sulit diperoleh, dan jebakan yang berulang menjadi file `SKILL.md` di bawah:

textCopy code
[code]
    <workspace>/skills/<skill-name>/SKILL.md
[/code]

Ini berbeda dari memori jangka panjang:

  * **Memory** menyimpan fakta, preferensi, entitas, dan konteks masa lalu.
  * **Skills** menyimpan prosedur yang dapat digunakan ulang yang harus diikuti agen pada tugas mendatang.
  * **Skill Workshop** adalah jembatan dari giliran yang berguna ke skill workspace yang tahan lama, dengan pemeriksaan keamanan dan persetujuan opsional.


Skill Workshop berguna ketika agen mempelajari prosedur seperti:

  * cara memvalidasi aset GIF animasi yang bersumber dari eksternal
  * cara mengganti aset screenshot dan memverifikasi dimensi
  * cara menjalankan skenario QA khusus repo
  * cara men-debug kegagalan provider yang berulang
  * cara memperbaiki catatan alur kerja lokal yang basi


Fitur ini tidak ditujukan untuk:

  * fakta seperti "pengguna menyukai biru"
  * memori autobiografis yang luas
  * pengarsipan transkrip mentah
  * rahasia, kredensial, atau teks prompt tersembunyi
  * instruksi sekali pakai yang tidak akan berulang


## Status default

Plugin bawaan ini **eksperimental** dan **dinonaktifkan secara default** kecuali diaktifkan secara eksplisit di `plugins.entries.skill-workshop`.

Manifest plugin tidak menetapkan `enabledByDefault: true`. Default `enabled: true` di dalam skema konfigurasi plugin hanya berlaku setelah entri plugin sudah dipilih dan dimuat.

Eksperimental berarti:

  * plugin didukung secukupnya untuk pengujian opt-in dan dogfooding
  * penyimpanan proposal, ambang reviewer, dan heuristik capture dapat berkembang
  * persetujuan tertunda adalah mode awal yang direkomendasikan
  * auto apply ditujukan untuk setup personal/workspace tepercaya, bukan lingkungan bersama atau lingkungan dengan banyak input yang tidak tepercaya


## Mengaktifkan

Konfigurasi aman minimal:

json5Copy code
[code]
    {  plugins: {    entries: {      "skill-workshop": {        enabled: true,        config: {          autoCapture: true,          approvalPolicy: "pending",          reviewMode: "hybrid",        },      },    },  },}
[/code]

Dengan konfigurasi ini:

  * tool `skill_workshop` tersedia
  * koreksi eksplisit yang dapat digunakan ulang diantrekan sebagai proposal tertunda
  * pass reviewer berbasis ambang dapat mengusulkan pembaruan skill
  * tidak ada file skill yang ditulis hingga proposal tertunda diterapkan


Gunakan penulisan otomatis hanya di workspace tepercaya:

json5Copy code
[code]
    {  plugins: {    entries: {      "skill-workshop": {        enabled: true,        config: {          autoCapture: true,          approvalPolicy: "auto",          reviewMode: "hybrid",        },      },    },  },}
[/code]

`approvalPolicy: "auto"` tetap menggunakan scanner dan jalur karantina yang sama. Ini tidak menerapkan proposal dengan temuan kritis.

## Konfigurasi

Kunci | Default | Rentang / nilai | Makna  
---|---|---|---  
`enabled` | `true` | boolean | Mengaktifkan plugin setelah entri plugin dimuat.  
`autoCapture` | `true` | boolean | Mengaktifkan capture/review pasca-giliran pada giliran agen yang berhasil.  
`approvalPolicy` | `"pending"` | `"pending"`, `"auto"` | Mengantrekan proposal atau menulis proposal aman secara otomatis.  
`reviewMode` | `"hybrid"` | `"off"`, `"heuristic"`, `"llm"`, `"hybrid"` | Memilih capture koreksi eksplisit, reviewer LLM, keduanya, atau tidak keduanya.  
`reviewInterval` | `15` | `1..200` | Menjalankan reviewer setelah jumlah giliran berhasil ini.  
`reviewMinToolCalls` | `8` | `1..500` | Menjalankan reviewer setelah jumlah tool call yang diamati ini.  
`reviewTimeoutMs` | `45000` | `5000..180000` | Timeout untuk proses reviewer tertanam.  
`maxPending` | `50` | `1..200` | Proposal tertunda/terkarantina maksimum yang disimpan per workspace.  
`maxSkillBytes` | `40000` | `1024..200000` | Ukuran maksimum file skill/pendukung yang dihasilkan.  
  
Profil yang direkomendasikan:

json5Copy code
[code]
    // Conservative: explicit tool use only, no automatic capture.{  autoCapture: false,  approvalPolicy: "pending",  reviewMode: "off",}
[/code]

json5Copy code
[code]
    // Review-first: capture automatically, but require approval.{  autoCapture: true,  approvalPolicy: "pending",  reviewMode: "hybrid",}
[/code]

json5Copy code
[code]
    // Trusted automation: write safe proposals immediately.{  autoCapture: true,  approvalPolicy: "auto",  reviewMode: "hybrid",}
[/code]

json5Copy code
[code]
    // Low-cost: no reviewer LLM call, only explicit correction phrases.{  autoCapture: true,  approvalPolicy: "pending",  reviewMode: "heuristic",}
[/code]

## Jalur capture

Skill Workshop memiliki tiga jalur capture.

### Saran tool

Model dapat memanggil `skill_workshop` secara langsung ketika melihat prosedur yang dapat digunakan ulang atau ketika pengguna memintanya menyimpan/memperbarui skill.

Ini adalah jalur yang paling eksplisit dan tetap berfungsi bahkan dengan `autoCapture: false`.

### Capture heuristik

Ketika `autoCapture` diaktifkan dan `reviewMode` adalah `heuristic` atau `hybrid`, plugin memindai giliran yang berhasil untuk frasa koreksi pengguna yang eksplisit:

  * `next time`
  * `from now on`
  * `remember to`
  * `make sure to`
  * `always ... use/check/verify/record/save/prefer`
  * `prefer ... when/for/instead/use`
  * `when asked`


Heuristik membuat proposal dari instruksi pengguna terbaru yang cocok. Ini menggunakan petunjuk topik untuk memilih nama skill bagi alur kerja umum:

  * tugas GIF animasi -> `animated-gif-workflow`
  * tugas screenshot atau aset -> `screenshot-asset-workflow`
  * tugas QA atau skenario -> `qa-scenario-workflow`
  * tugas PR GitHub -> `github-pr-workflow`
  * fallback -> `learned-workflows`


Capture heuristik sengaja dibuat sempit. Ini ditujukan untuk koreksi yang jelas dan catatan proses yang dapat diulang, bukan untuk peringkasan transkrip umum.

### Reviewer LLM

Ketika `autoCapture` diaktifkan dan `reviewMode` adalah `llm` atau `hybrid`, plugin menjalankan reviewer tertanam ringkas setelah ambang tercapai.

Reviewer menerima:

  * teks transkrip terbaru, dibatasi hingga 12.000 karakter terakhir
  * hingga 12 skill workspace yang ada
  * hingga 2.000 karakter dari setiap skill yang ada
  * instruksi khusus JSON


Reviewer tidak memiliki tool:

  * `disableTools: true`
  * `toolsAllow: []`
  * `disableMessageTool: true`


Reviewer mengembalikan `{ "action": "none" }` atau satu proposal. Field `action` adalah `create`, `append`, atau `replace` \- pilih `append`/`replace` ketika skill yang relevan sudah ada; gunakan `create` hanya ketika tidak ada skill yang cocok.

Contoh `create`:

jsonCopy code
[code]
    {  "action": "create",  "skillName": "media-asset-qa",  "title": "Media Asset QA",  "reason": "Reusable animated media acceptance workflow",  "description": "Validate externally sourced animated media before product use.",  "body": "## Workflow\n\n- Verify true animation.\n- Record attribution.\n- Store a local approved copy.\n- Verify in product UI before final reply."}
[/code]

`append` menambahkan `section` \+ `body`. `replace` menukar `oldText` dengan `newText` di skill bernama tersebut.

## Siklus hidup proposal

Setiap pembaruan yang dihasilkan menjadi proposal dengan:

  * `id`
  * `createdAt`
  * `updatedAt`
  * `workspaceDir`
  * `agentId` opsional
  * `sessionId` opsional
  * `skillName`
  * `title`
  * `reason`
  * `source`: `tool`, `agent_end`, atau `reviewer`
  * `status`
  * `change`
  * `scanFindings` opsional
  * `quarantineReason` opsional


Status proposal:

  * `pending` \- menunggu persetujuan
  * `applied` \- ditulis ke `<workspace>/skills`
  * `rejected` \- ditolak oleh operator/model
  * `quarantined` \- diblokir oleh temuan scanner kritis


Status disimpan per ruang kerja di bawah direktori status Gateway:

textCopy code
[code]
    <stateDir>/skill-workshop/<workspace-hash>.json
[/code]

Proposal tertunda dan dikarantina dideduplikasi berdasarkan nama skill dan payload perubahan. Penyimpanan mempertahankan proposal tertunda/dikarantina terbaru hingga `maxPending`.

## Referensi alat

Plugin mendaftarkan satu alat agen:

textCopy code
[code]
    skill_workshop
[/code]

### `status`

Hitung proposal berdasarkan status untuk ruang kerja aktif.

jsonCopy code
[code]
    { "action": "status" }
[/code]

Bentuk hasil:

jsonCopy code
[code]
    {  "workspaceDir": "/path/to/workspace",  "pending": 1,  "quarantined": 0,  "applied": 3,  "rejected": 0}
[/code]

### `list_pending`

Cantumkan proposal tertunda.

jsonCopy code
[code]
    { "action": "list_pending" }
[/code]

Untuk mencantumkan status lain:

jsonCopy code
[code]
    { "action": "list_pending", "status": "applied" }
[/code]

Nilai `status` yang valid:

  * `pending`
  * `applied`
  * `rejected`
  * `quarantined`


### `list_quarantine`

Cantumkan proposal yang dikarantina.

jsonCopy code
[code]
    { "action": "list_quarantine" }
[/code]

Gunakan ini ketika penangkapan otomatis tampaknya tidak melakukan apa pun dan log menyebutkan `skill-workshop: quarantined <skill>`.

### `inspect`

Ambil proposal berdasarkan id.

jsonCopy code
[code]
    {  "action": "inspect",  "id": "proposal-id"}
[/code]

### `suggest`

Buat proposal. Dengan `approvalPolicy: "pending"` (default), ini memasukkan ke antrean alih-alih menulis.

jsonCopy code
[code]
    {  "action": "suggest",  "skillName": "animated-gif-workflow",  "title": "Animated GIF Workflow",  "reason": "User established reusable GIF validation rules.",  "description": "Validate animated GIF assets before using them.",  "body": "## Workflow\n\n- Verify the URL resolves to image/gif.\n- Confirm it has multiple frames.\n- Record attribution and license.\n- Avoid hotlinking when a local asset is needed."}
[/code]

Minta penulisan segera dalam mode otomatis (apply: true) jsonCopy code
[code]
    {"action": "suggest","apply": true,"skillName": "animated-gif-workflow","description": "Validate animated GIF assets before using them.","body": "## Workflow\n\n- Verify true animation.\n- Record attribution."}
[/code]

Dengan `approvalPolicy: "pending"`, `apply: true` tetap mengantrekan proposal. Tinjau, lalu gunakan tindakan `apply` setelah persetujuan.

Paksa tertunda di bawah kebijakan otomatis (apply: false) jsonCopy code
[code]
    {"action": "suggest","apply": false,"skillName": "screenshot-asset-workflow","description": "Screenshot replacement workflow.","body": "## Workflow\n\n- Verify dimensions.\n- Optimize the PNG.\n- Run the relevant gate."}
[/code]

Tambahkan ke bagian bernama jsonCopy code
[code]
    {"action": "suggest","skillName": "qa-scenario-workflow","section": "Workflow","description": "QA scenario workflow.","body": "- For media QA, verify generated assets render and pass final assertions."}
[/code]

Ganti teks persis jsonCopy code
[code]
    {"action": "suggest","skillName": "github-pr-workflow","oldText": "- Check the PR.","newText": "- Check unresolved review threads, CI status, linked issues, and changed files before deciding."}
[/code]

### `apply`

Terapkan proposal tertunda.

Dengan `approvalPolicy: "pending"`, tindakan ini meminta persetujuan operator sebelum menulis skill ruang kerja.

jsonCopy code
[code]
    {  "action": "apply",  "id": "proposal-id"}
[/code]

`apply` menolak proposal yang dikarantina:

textCopy code
[code]
    quarantined proposal cannot be applied
[/code]

### `reject`

Tandai proposal sebagai ditolak.

jsonCopy code
[code]
    {  "action": "reject",  "id": "proposal-id"}
[/code]

### `write_support_file`

Tulis file pendukung di dalam direktori skill yang sudah ada atau yang diusulkan.

Direktori pendukung tingkat atas yang diizinkan:

  * `references/`
  * `templates/`
  * `scripts/`
  * `assets/`


Contoh:

jsonCopy code
[code]
    {  "action": "write_support_file",  "skillName": "release-workflow",  "relativePath": "references/checklist.md",  "body": "# Release Checklist\n\n- Run release docs.\n- Verify changelog.\n"}
[/code]

File dukungan bercakupan ruang kerja, jalurnya diperiksa, dibatasi byte oleh `maxSkillBytes`, dipindai, dan ditulis secara atomik.

## Penulisan skill

Skill Workshop hanya menulis di bawah:

textCopy code
[code]
    <workspace>/skills/<normalized-skill-name>/
[/code]

Nama skill dinormalisasi:

  * dibuat huruf kecil
  * rangkaian non `[a-z0-9_-]` menjadi `-`
  * non-alfanumerik di awal/akhir dihapus
  * panjang maksimum 80 karakter
  * nama akhir harus cocok dengan `[a-z0-9][a-z0-9_-]{1,79}`


Untuk `create`:

  * jika skill belum ada, Skill Workshop menulis `SKILL.md` baru
  * jika sudah ada, Skill Workshop menambahkan body ke `## Workflow`


Untuk `append`:

  * jika skill ada, Skill Workshop menambahkan ke bagian yang diminta
  * jika belum ada, Skill Workshop membuat skill minimal lalu menambahkan


Untuk `replace`:

  * skill harus sudah ada
  * `oldText` harus ada persis
  * hanya kecocokan persis pertama yang diganti


Semua penulisan bersifat atomik dan langsung menyegarkan snapshot skill dalam memori, sehingga skill baru atau yang diperbarui dapat terlihat tanpa memulai ulang Gateway.

## Model keamanan

Skill Workshop memiliki pemindai keamanan pada konten `SKILL.md` yang dihasilkan dan file dukungan.

Temuan kritis mengarantina proposal:

ID aturan | Memblokir konten yang...  
---|---  
`prompt-injection-ignore-instructions` | menyuruh agen mengabaikan instruksi sebelumnya/lebih tinggi  
`prompt-injection-system` | merujuk prompt sistem, pesan developer, atau instruksi tersembunyi  
`prompt-injection-tool` | mendorong pelewatan izin/persetujuan alat  
`shell-pipe-to-shell` | menyertakan `curl`/`wget` yang disalurkan ke `sh`, `bash`, atau `zsh`  
`secret-exfiltration` | tampak mengirim data env/env proses melalui jaringan  
  
Temuan peringatan dipertahankan tetapi tidak memblokir dengan sendirinya:

ID aturan | Memperingatkan pada...  
---|---  
`destructive-delete` | perintah luas bergaya `rm -rf`  
`unsafe-permissions` | penggunaan izin bergaya `chmod 777`  
  
Proposal yang dikarantina:

  * menyimpan `scanFindings`
  * menyimpan `quarantineReason`
  * muncul di `list_quarantine`
  * tidak dapat diterapkan melalui `apply`


Untuk memulihkan dari proposal yang dikarantina, buat proposal aman baru dengan konten tidak aman dihapus. Jangan mengedit JSON penyimpanan secara manual.

## Panduan prompt

Saat diaktifkan, Skill Workshop menyuntikkan bagian prompt singkat yang menyuruh agen menggunakan `skill_workshop` untuk memori prosedural yang tahan lama.

Panduan menekankan:

  * prosedur, bukan fakta/preferensi
  * koreksi pengguna
  * prosedur berhasil yang tidak jelas
  * jebakan berulang
  * perbaikan skill yang basi/tipis/salah melalui append/replace
  * menyimpan prosedur yang dapat digunakan ulang setelah loop alat panjang atau perbaikan sulit
  * teks skill imperatif yang singkat
  * tanpa dump transkrip


Teks mode tulis berubah sesuai `approvalPolicy`:

  * mode pending: antrekan saran; gunakan `apply` setelah persetujuan eksplisit
  * mode otomatis: terapkan pembaruan skill ruang kerja yang aman kecuali `apply: false` justru mengantrekan


## Biaya dan perilaku runtime

Penangkapan heuristik tidak memanggil model.

Tinjauan LLM menggunakan run tertanam pada model agen aktif/default. Ini berbasis ambang sehingga secara default tidak berjalan pada setiap giliran.

Reviewer:

  * menggunakan konteks provider/model terkonfigurasi yang sama jika tersedia
  * fallback ke default agen runtime
  * memiliki `reviewTimeoutMs`
  * menggunakan konteks bootstrap ringan
  * tidak memiliki alat
  * tidak menulis apa pun secara langsung
  * hanya dapat memancarkan proposal yang melewati pemindai normal dan jalur persetujuan/karantina


Jika reviewer gagal, waktu habis, atau mengembalikan JSON tidak valid, Plugin mencatat pesan peringatan/debug dan melewati lintasan tinjauan tersebut.

## Pola operasi

Gunakan Skill Workshop saat pengguna berkata:

  * "next time, do X"
  * "from now on, prefer Y"
  * "make sure to verify Z"
  * "save this as a workflow"
  * "this took a while; remember the process"
  * "update the local skill for this"


Teks skill yang baik:

markdownCopy code
[code]
    ## Workflow - Verify the GIF URL resolves to `image/gif`.- Confirm the file has multiple frames.- Record source URL, license, and attribution.- Store a local copy when the asset will ship with the product.- Verify the local asset renders in the target UI before final reply.
[/code]

Teks skill yang buruk:

markdownCopy code
[code]
    The user asked about a GIF and I searched two websites. Then one was blocked byCloudflare. The final answer said to check attribution.
[/code]

Alasan versi buruk tidak sebaiknya disimpan:

  * berbentuk transkrip
  * tidak imperatif
  * menyertakan detail sekali pakai yang berisik
  * tidak memberi tahu agen berikutnya apa yang harus dilakukan


## Debugging

Periksa apakah Plugin dimuat:

bashCopy code
[code]
    openclaw plugins list --enabled
[/code]

Periksa jumlah proposal dari konteks agen/alat:

jsonCopy code
[code]
    { "action": "status" }
[/code]

Periksa proposal pending:

jsonCopy code
[code]
    { "action": "list_pending" }
[/code]

Periksa proposal yang dikarantina:

jsonCopy code
[code]
    { "action": "list_quarantine" }
[/code]

Gejala umum:

Gejala | Kemungkinan penyebab | Pemeriksaan  
---|---|---  
Alat tidak tersedia | Entri Plugin tidak diaktifkan | `plugins.entries.skill-workshop.enabled` dan `openclaw plugins list`  
Tidak ada proposal otomatis muncul | `autoCapture: false`, `reviewMode: "off"`, atau ambang tidak terpenuhi | Konfigurasi, status proposal, log Gateway  
Heuristik tidak menangkap | Susunan kata pengguna tidak cocok dengan pola koreksi | Gunakan `skill_workshop.suggest` eksplisit atau aktifkan reviewer LLM  
Reviewer tidak membuat proposal | Reviewer mengembalikan `none`, JSON tidak valid, atau waktu habis | Log Gateway, `reviewTimeoutMs`, ambang  
Proposal tidak diterapkan | `approvalPolicy: "pending"` | `list_pending`, lalu `apply`  
Proposal hilang dari pending | Proposal duplikat digunakan ulang, pemangkasan pending maksimum, atau sudah diterapkan/ditolak/dikarantina | `status`, `list_pending` dengan filter status, `list_quarantine`  
File skill ada tetapi model melewatkannya | Snapshot skill tidak disegarkan atau gating skill mengecualikannya | status `openclaw skills` dan kelayakan skill ruang kerja  
  
Log relevan:

  * `skill-workshop: queued <skill>`
  * `skill-workshop: applied <skill>`
  * `skill-workshop: quarantined <skill>`
  * `skill-workshop: heuristic capture skipped: ...`
  * `skill-workshop: reviewer skipped: ...`
  * `skill-workshop: reviewer found no update`


## Skenario QA

Skenario QA berbasis repo:

  * `qa/scenarios/plugins/skill-workshop-animated-gif-autocreate.md`
  * `qa/scenarios/plugins/skill-workshop-pending-approval.md`
  * `qa/scenarios/plugins/skill-workshop-reviewer-autonomous.md`


Jalankan cakupan deterministik:

bashCopy code
[code]
    pnpm openclaw qa suite \  --scenario skill-workshop-animated-gif-autocreate \  --scenario skill-workshop-pending-approval \  --concurrency 1
[/code]

Jalankan cakupan reviewer:

bashCopy code
[code]
    pnpm openclaw qa suite \  --scenario skill-workshop-reviewer-autonomous \  --concurrency 1
[/code]

Skenario reviewer sengaja dipisahkan karena mengaktifkan `reviewMode: "llm"` dan melatih lintasan reviewer tertanam.

## Kapan tidak mengaktifkan penerapan otomatis

Hindari `approvalPolicy: "auto"` saat:

  * ruang kerja berisi prosedur sensitif
  * agen sedang menangani input tidak tepercaya
  * skill dibagikan di seluruh tim yang luas
  * Anda masih menyetel prompt atau aturan pemindai
  * model sering menangani konten web/email yang bermusuhan


Gunakan mode pending terlebih dahulu. Beralih ke mode otomatis hanya setelah meninjau jenis skill yang diajukan agen di ruang kerja tersebut.

## Dokumen terkait

  * [Skills](</id/tools/skills>)
  * [Plugins](</id/tools/plugin>)
  * [Pengujian](</id/reference/test>)


Was this useful?YesNo