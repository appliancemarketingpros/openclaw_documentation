---
title: Skills
source_url: https://docs.openclaw.ai/id/tools/skills
scraped_at: 2026-05-25
---

OpenClaw menggunakan folder skill yang **kompatibel dengan[AgentSkills](<https://agentskills.io>)** untuk mengajari agen cara menggunakan alat. Setiap skill adalah direktori yang berisi `SKILL.md` dengan frontmatter YAML dan instruksi. OpenClaw memuat skill bawaan beserta override lokal opsional, dan memfilternya pada waktu pemuatan berdasarkan lingkungan, konfigurasi, serta keberadaan biner.

## Lokasi dan prioritas

OpenClaw memuat skill dari sumber berikut, **prioritas tertinggi terlebih dahulu** :

# | Sumber | Jalur  
---|---|---  
1 | Skill workspace | `<workspace>/skills`  
2 | Skill agen proyek | `<workspace>/.agents/skills`  
3 | Skill agen pribadi | `~/.agents/skills`  
4 | Skill terkelola/lokal | `~/.openclaw/skills`  
5 | Skill bawaan | dikirim bersama instalasi  
6 | Folder skill ekstra | `skills.load.extraDirs` (config)  
  
Jika nama skill berbenturan, sumber tertinggi yang menang.

Direktori native `$CODEX_HOME/skills` milik Codex CLI bukan salah satu root skill OpenClaw ini. Dalam mode harness Codex, peluncuran app-server lokal menggunakan home Codex per agen yang terisolasi, sehingga skill pribadi Codex CLI tidak dimuat secara implisit. Gunakan `openclaw migrate codex --dry-run` untuk menginventarisasinya dan `openclaw migrate codex` untuk memilih direktori skill dengan prompt kotak centang interaktif sebelum menyalinnya ke workspace agen OpenClaw saat ini. Untuk eksekusi noninteraktif, ulangi `--skill <name>` untuk skill persis yang akan disalin.

## Skill per agen vs bersama

Dalam setup **multi-agen** , setiap agen memiliki workspace-nya sendiri:

Cakupan | Jalur | Terlihat oleh  
---|---|---  
Per agen | `<workspace>/skills` | Hanya agen tersebut  
Agen proyek | `<workspace>/.agents/skills` | Hanya agen workspace tersebut  
Agen pribadi | `~/.agents/skills` | Semua agen di mesin tersebut  
Terkelola/lokal bersama | `~/.openclaw/skills` | Semua agen di mesin tersebut  
Direktori ekstra bersama | `skills.load.extraDirs` (prioritas terendah) | Semua agen di mesin tersebut  
  
Nama yang sama di beberapa tempat → sumber tertinggi yang menang. Workspace mengalahkan agen proyek, mengalahkan agen pribadi, mengalahkan terkelola/lokal, mengalahkan bawaan, mengalahkan direktori ekstra.

## Allowlist skill agen

**Lokasi** skill dan **visibilitas** skill adalah kontrol yang terpisah. Lokasi/prioritas menentukan salinan mana dari skill bernama sama yang menang; allowlist agen menentukan skill mana yang benar-benar dapat digunakan oleh agen.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // mewarisi github, weather      { id: "docs", skills: ["docs-search"] }, // menggantikan default      { id: "locked-down", skills: [] }, // tanpa skill    ],  },}
[/code]

Aturan allowlist

  * Hilangkan `agents.defaults.skills` agar skill tidak dibatasi secara default.
  * Hilangkan `agents.list[].skills` untuk mewarisi `agents.defaults.skills`.
  * Tetapkan `agents.list[].skills: []` untuk tanpa skill.
  * Daftar `agents.list[].skills` yang tidak kosong adalah set **final** untuk agen tersebut - tidak digabungkan dengan default.
  * Allowlist efektif diterapkan di seluruh pembuatan prompt, penemuan slash-command skill, sinkronisasi sandbox, dan snapshot skill.


## Plugin dan skill

Plugin dapat mengirim skill-nya sendiri dengan mencantumkan direktori `skills` di `openclaw.plugin.json` (jalur relatif terhadap root plugin). Skill plugin dimuat saat plugin diaktifkan. Ini adalah tempat yang tepat untuk panduan operasional khusus alat yang terlalu panjang untuk deskripsi alat tetapi harus tersedia setiap kali plugin terpasang - misalnya, plugin browser mengirim skill `browser-automation` untuk kontrol browser multi-langkah.

Direktori skill plugin digabungkan ke jalur berprioritas rendah yang sama seperti `skills.load.extraDirs`, sehingga skill bawaan, terkelola, agen, atau workspace dengan nama yang sama akan menimpanya. Anda dapat membatasinya melalui `metadata.openclaw.requires.config` pada entri konfigurasi plugin.

Lihat [Plugin](</id/tools/plugin>) untuk penemuan/konfigurasi dan [Alat](</id/tools>) untuk permukaan alat yang diajarkan skill tersebut.

## Skill Workshop

Plugin **Skill Workshop** opsional dan eksperimental dapat membuat atau memperbarui skill workspace dari prosedur yang dapat digunakan ulang yang diamati selama pekerjaan agen. Plugin ini dinonaktifkan secara default dan harus diaktifkan secara eksplisit melalui `plugins.entries.skill-workshop`.

Skill Workshop hanya menulis ke `<workspace>/skills`, memindai konten yang dihasilkan, mendukung persetujuan tertunda atau penulisan aman otomatis, mengarantina proposal yang tidak aman, dan menyegarkan snapshot skill setelah penulisan berhasil sehingga skill baru tersedia tanpa restart Gateway.

Gunakan untuk koreksi seperti _"lain kali, verifikasi atribusi GIF"_ atau workflow yang diperoleh dengan susah payah seperti checklist QA media. Mulai dengan persetujuan tertunda; gunakan penulisan otomatis hanya di workspace tepercaya setelah meninjau proposalnya. Panduan lengkap: [Plugin Skill Workshop](</id/plugins/skill-workshop>).

## ClawHub (instal dan sinkronisasi)

[ClawHub](<https://clawhub.ai>) adalah registri skill publik untuk OpenClaw. Gunakan perintah native `openclaw skills` untuk menemukan/menginstal/memperbarui, atau CLI `clawhub` terpisah untuk workflow publikasi/sinkronisasi. Panduan lengkap: [ClawHub](</id/clawhub>).

Tindakan | Perintah  
---|---  
Instal skill ke workspace | `openclaw skills install <skill-slug>`  
Perbarui semua skill terinstal | `openclaw skills update --all`  
Sinkronisasi (pindai + publikasikan pembaruan) | `clawhub sync --all`  
  
`openclaw skills install` native menginstal ke direktori `skills/` workspace aktif. CLI `clawhub` terpisah juga menginstal ke `./skills` di bawah direktori kerja Anda saat ini (atau fallback ke workspace OpenClaw yang dikonfigurasi). OpenClaw mengambilnya sebagai `<workspace>/skills` pada sesi berikutnya. Root skill yang dikonfigurasi juga mendukung satu tingkat pengelompokan, seperti `skills/<group>/<skill>/SKILL.md`, sehingga skill pihak ketiga yang terkait dapat disimpan di bawah folder bersama tanpa pemindaian rekursif luas.

Klien Gateway yang membutuhkan pengiriman privat non-ClawHub dapat menyiapkan arsip skill zip dengan `skills.upload.begin`, `skills.upload.chunk`, dan `skills.upload.commit`, lalu menginstal unggahan yang sudah di-commit dengan `skills.install({ source: "upload", uploadId, slug, force?, sha256? })`. Ini adalah jalur unggahan admin eksplisit untuk klien tepercaya, bukan alur normal `openclaw skills install <slug>` atau instalasi ClawHub. Jalur ini nonaktif secara default dan hanya berfungsi saat `skills.install.allowUploadedArchives: true` ditetapkan di `openclaw.json`. Mode unggahan tetap menginstal ke direktori `skills/<slug>` workspace agen default; nama folder internal arsip diabaikan untuk target instalasi akhir.

Halaman skill ClawHub menampilkan status pemindaian keamanan terbaru sebelum instalasi, dengan halaman detail pemindai untuk VirusTotal, ClawScan, dan analisis statis. `openclaw skills install <slug>` tetap hanya menjadi jalur instalasi; penerbit memulihkan false positive melalui dashboard ClawHub atau `clawhub skill rescan <slug>`.

## Keamanan

  * Penemuan skill workspace dan direktori ekstra hanya menerima root skill dan file `SKILL.md` yang realpath terselesaikannya tetap berada di dalam root yang dikonfigurasi.
  * Instalasi arsip privat Gateway nonaktif secara default. Saat diaktifkan secara eksplisit, instalasi ini memerlukan unggahan zip yang sudah di-commit berisi `SKILL.md` dan menggunakan kembali perlindungan ekstraksi arsip, path traversal, symlink, force, dan rollback yang sama seperti instalasi skill ClawHub. Instalasi ini dibatasi oleh `skills.install.allowUploadedArchives`; instalasi ClawHub normal tidak memerlukan pengaturan tersebut.
  * Instalasi dependensi skill yang didukung Gateway (`skills.install`, onboarding, dan UI pengaturan Skills) menjalankan pemindai kode berbahaya bawaan sebelum mengeksekusi metadata installer. Temuan `critical` memblokir secara default kecuali pemanggil menetapkan override berbahaya secara eksplisit; temuan mencurigakan tetap hanya memberi peringatan.
  * `openclaw skills install <slug>` berbeda - perintah ini mengunduh folder skill ClawHub ke workspace dan tidak menggunakan jalur metadata-installer di atas.
  * `skills.entries.*.env` dan `skills.entries.*.apiKey` menyuntikkan rahasia ke proses **host** untuk giliran agen tersebut (bukan sandbox). Jauhkan rahasia dari prompt dan log.


Untuk model ancaman dan checklist yang lebih luas, lihat [Keamanan](</id/gateway/security>).

## Format [SKILL.md](<http://SKILL.md>)

`SKILL.md` harus menyertakan setidaknya:

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflow---
[/code]

OpenClaw mengikuti spesifikasi AgentSkills untuk tata letak/tujuan. Parser yang digunakan oleh agen tertanam hanya mendukung kunci frontmatter **satu baris** ; `metadata` harus berupa **objek JSON satu baris**. Gunakan `{baseDir}` dalam instruksi untuk merujuk jalur folder skill.

### Kunci frontmatter opsional

URL yang ditampilkan sebagai "Situs web" di UI Skills macOS. Juga didukung melalui `metadata.openclaw.homepage`.

Saat `true`, skill diekspos sebagai slash command pengguna.

Saat `true`, OpenClaw menjauhkan instruksi skill dari prompt normal agen. Skill tetap terinstal dan masih dapat dijalankan secara eksplisit sebagai slash command saat `user-invocable` juga `true`.

Saat disetel ke `tool`, slash command melewati model dan mengirim langsung ke alat.

Nama alat yang akan dipanggil saat `command-dispatch: tool` disetel.

Untuk dispatch alat, meneruskan string arg mentah ke alat (tanpa parsing core). Alat dipanggil dengan `{ command: "<raw args>", commandName: "<slash command>", skillName: "<skill name>" }`.

## Gating (filter waktu pemuatan)

OpenClaw memfilter skill pada waktu pemuatan menggunakan `metadata` (JSON satu baris):

markdownCopy code
[code]
    ---name: image-labdescription: Generate or edit images via a provider-backed image workflowmetadata:  {    "openclaw":      {        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"], "config": ["browser.enabled"] },        "primaryEnv": "GEMINI_API_KEY",      },  }---
[/code]

Bidang di bawah `metadata.openclaw`:

Jika `true`, selalu sertakan skill (lewati gate lain).

Emoji opsional yang digunakan oleh UI Skills macOS.

URL opsional yang ditampilkan sebagai "Situs web" di UI Skills macOS.

Daftar platform opsional. Jika ditetapkan, skill hanya memenuhi syarat pada OS tersebut.

Masing-masing harus ada di `PATH`.

Setidaknya satu harus ada di `PATH`.

Variabel env harus ada atau disediakan dalam konfigurasi.

Daftar path `openclaw.json` yang harus bernilai truthy.

Nama variabel env yang terkait dengan `skills.entries.<name>.apiKey`.

Spesifikasi penginstal opsional yang digunakan oleh UI Skills macOS (brew/node/go/uv/download).

Jika tidak ada `metadata.openclaw`, skill selalu memenuhi syarat (kecuali dinonaktifkan dalam konfigurasi atau diblokir oleh `skills.allowBundled` untuk skill bawaan).

### Catatan sandboxing

  * `requires.bins` diperiksa di **host** saat skill dimuat.
  * Jika agen berada dalam sandbox, binary juga harus ada **di dalam container**. Instal melalui `agents.defaults.sandbox.docker.setupCommand` (atau image khusus). `setupCommand` berjalan sekali setelah container dibuat. Instalasi paket juga memerlukan egress jaringan, root FS yang dapat ditulis, dan pengguna root di sandbox.
  * Contoh: skill `summarize` (`skills/summarize/SKILL.md`) memerlukan CLI `summarize` di container sandbox agar dapat berjalan di sana.


### Spesifikasi penginstal

markdownCopy code
[code]
    ---name: geminidescription: Use Gemini CLI for coding assistance and Google search lookups.metadata:  {    "openclaw":      {        "emoji": "♊️",        "requires": { "bins": ["gemini"] },        "install":          [            {              "id": "brew",              "kind": "brew",              "formula": "gemini-cli",              "bins": ["gemini"],              "label": "Install Gemini CLI (brew)",            },          ],      },  }---
[/code]

Aturan pemilihan penginstal

  * Jika beberapa penginstal dicantumkan, Gateway memilih satu opsi pilihan (brew jika tersedia, jika tidak node).
  * Jika semua penginstal adalah `download`, OpenClaw mencantumkan setiap entri sehingga Anda dapat melihat artefak yang tersedia.
  * Spesifikasi penginstal dapat menyertakan `os: ["darwin"|"linux"|"win32"]` untuk memfilter opsi menurut platform.
  * Instalasi Node mengikuti `skills.install.nodeManager` di `openclaw.json` (default: npm; opsi: npm/pnpm/yarn/bun). Ini hanya memengaruhi instalasi skill; runtime Gateway tetap sebaiknya Node - Bun tidak direkomendasikan untuk WhatsApp/Telegram.
  * Pemilihan penginstal berbasis Gateway didorong oleh preferensi: ketika spesifikasi instalasi mencampur jenis, OpenClaw lebih memilih Homebrew saat `skills.install.preferBrew` diaktifkan dan `brew` ada, lalu `uv`, lalu pengelola node yang dikonfigurasi, lalu fallback lain seperti `go` atau `download`.
  * Jika setiap spesifikasi instalasi adalah `download`, OpenClaw menampilkan semua opsi unduhan alih-alih meringkasnya menjadi satu penginstal pilihan.

Detail per penginstal

  * **Instalasi Go:** jika `go` tidak ada dan `brew` tersedia, Gateway menginstal Go melalui Homebrew terlebih dahulu dan mengatur `GOBIN` ke `bin` milik Homebrew jika memungkinkan.
  * **Instalasi unduhan:** `url` (wajib), `archive` (`tar.gz` | `tar.bz2` | `zip`), `extract` (default: otomatis saat arsip terdeteksi), `stripComponents`, `targetDir` (default: `~/.openclaw/tools/<skillKey>`).


## Override konfigurasi

Skill bawaan dan terkelola dapat diaktifkan/dinonaktifkan serta diberi nilai env di bawah `skills.entries` dalam `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  skills: {    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: {          GEMINI_API_KEY: "GEMINI_KEY_HERE",        },        config: {          endpoint: "https://example.invalid",          model: "nano-pro",        },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

`false` menonaktifkan skill meskipun skill tersebut bawaan atau terinstal. Skill bawaan `coding-agent` bersifat opt-in: atur `skills.entries.coding-agent.enabled: true` sebelum mengeksposnya kepada agen, lalu pastikan salah satu dari `claude`, `codex`, `opencode`, atau `pi` terinstal dan terautentikasi untuk CLI-nya sendiri.

Kemudahan untuk skill yang mendeklarasikan `metadata.openclaw.primaryEnv`. Mendukung plaintext atau SecretRef.

Wadah opsional untuk field khusus per skill. Key khusus harus berada di sini.

Allowlist opsional hanya untuk skill **bawaan**. Jika ditetapkan, hanya skill bawaan dalam daftar yang memenuhi syarat (skill terkelola/workspace tidak terpengaruh).

Jika nama skill berisi tanda hubung, beri tanda kutip pada key (JSON5 mengizinkan key yang dikutip). Key konfigurasi secara default cocok dengan **nama skill** \- jika sebuah skill mendefinisikan `metadata.openclaw.skillKey`, gunakan key tersebut di bawah `skills.entries`.

## Injeksi lingkungan

Ketika run agen dimulai, OpenClaw:

  1. Membaca metadata skill.
  2. Menerapkan `skills.entries.<key>.env` dan `skills.entries.<key>.apiKey` ke `process.env`.
  3. Membangun prompt sistem dengan skill yang **memenuhi syarat**.
  4. Memulihkan lingkungan asli setelah run berakhir.


Injeksi lingkungan **dibatasi pada run agen** , bukan lingkungan shell global.

Untuk backend bawaan `claude-cli`, OpenClaw juga mewujudkan snapshot memenuhi syarat yang sama sebagai Plugin Claude Code sementara dan meneruskannya dengan `--plugin-dir`. Claude Code kemudian dapat menggunakan resolver skill native-nya sementara OpenClaw tetap memiliki presedensi, allowlist per agen, gating, dan injeksi env/API key `skills.entries.*`. Backend CLI lain hanya menggunakan katalog prompt.

## Snapshot dan penyegaran

OpenClaw mengambil snapshot skill yang memenuhi syarat **saat sesi dimulai** dan menggunakan kembali daftar tersebut untuk giliran berikutnya dalam sesi yang sama. Perubahan pada skill atau konfigurasi berlaku pada sesi baru berikutnya.

Skill dapat disegarkan di tengah sesi dalam dua kasus:

  * Watcher skill diaktifkan.
  * Node jarak jauh baru yang memenuhi syarat muncul.


Anggap ini sebagai **hot reload** : daftar yang disegarkan akan digunakan pada giliran agen berikutnya. Jika allowlist skill agen efektif berubah untuk sesi tersebut, OpenClaw menyegarkan snapshot agar skill yang terlihat tetap selaras dengan agen saat ini.

### Watcher Skills

Secara default, OpenClaw mengawasi folder skill dan menaikkan snapshot skill ketika file `SKILL.md` berubah. Konfigurasikan di bawah `skills.load`:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/agent-scripts/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },  },}
[/code]

Gunakan `allowSymlinkTargets` untuk layout repo saudara yang disengaja ketika root skill bawaan berisi symlink, misalnya `~/.agents/skills/manager -> ~/Projects/manager/skills`. Daftar target dicocokkan setelah resolusi realpath dan sebaiknya tetap sempit.

### Node macOS jarak jauh (Gateway Linux)

Jika Gateway berjalan di Linux tetapi **node macOS** terhubung dengan `system.run` diizinkan (keamanan persetujuan Exec tidak diatur ke `deny`), OpenClaw dapat memperlakukan skill khusus macOS sebagai memenuhi syarat ketika binary yang diperlukan ada di node tersebut. Agen harus menjalankan skill tersebut melalui alat `exec` dengan `host=node`.

Ini bergantung pada node yang melaporkan dukungan perintahnya dan pada probe bin melalui `system.which` atau `system.run`. Node offline **tidak** membuat skill khusus jarak jauh terlihat. Jika node terhubung berhenti menjawab probe bin, OpenClaw menghapus kecocokan bin yang di-cache sehingga agen tidak lagi melihat skill yang saat ini tidak dapat berjalan di sana.

## Dampak token

Ketika skill memenuhi syarat, OpenClaw menyuntikkan daftar XML ringkas berisi skill yang tersedia ke dalam prompt sistem (melalui `formatSkillsForPrompt` di `pi-coding-agent`). Biayanya deterministik:

  * **Overhead dasar** (hanya ketika ≥1 skill): 195 karakter.
  * **Per skill:** 97 karakter + panjang nilai `<name>`, `<description>`, dan `<location>` yang sudah di-escape XML.


Rumus (karakter):

textCopy code
[code]
    total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
[/code]

Escaping XML memperluas `& < > " '` menjadi entitas (`&amp;`, `&lt;`, dll.), sehingga panjang bertambah. Jumlah token bervariasi menurut tokenizer model. Estimasi kasar gaya OpenAI adalah ~4 karakter/token, jadi **97 karakter ≈ 24 token** per skill ditambah panjang field aktual Anda.

## Siklus hidup skill terkelola

OpenClaw mengirimkan sekumpulan baseline skill sebagai **skill bawaan** bersama instalasi (paket npm atau OpenClaw.app). `~/.openclaw/skills` tersedia untuk override lokal - misalnya, menyematkan atau mem-patch skill tanpa mengubah salinan bawaan. Skill workspace dimiliki pengguna dan mengoverride keduanya jika terjadi konflik nama.

## Mencari skill lainnya?

Jelajahi <https://clawhub.ai>. Skema konfigurasi lengkap: [Konfigurasi Skills](</id/tools/skills-config>).

## Terkait

  * [ClawHub](</id/clawhub>) \- registri skill publik
  * [Membuat skill](</id/tools/creating-skills>) \- membangun skill khusus
  * [Plugin](</id/tools/plugin>) \- ikhtisar sistem Plugin
  * [Plugin Skill Workshop](</id/plugins/skill-workshop>) \- menghasilkan skill dari pekerjaan agen
  * [Konfigurasi Skills](</id/tools/skills-config>) \- referensi konfigurasi skill
  * [Perintah slash](</id/tools/slash-commands>) \- semua perintah slash yang tersedia


Was this useful?YesNo