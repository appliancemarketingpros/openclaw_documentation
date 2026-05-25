---
title: Kait
source_url: https://docs.openclaw.ai/id/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Kelola pengait agen (otomasi berbasis peristiwa untuk perintah seperti `/new`, `/reset`, dan startup Gateway).

Menjalankan `openclaw hooks` tanpa subperintah setara dengan `openclaw hooks list`.

Terkait:

  * Pengait: [Pengait](</id/automation/hooks>)
  * Pengait Plugin: [Pengait Plugin](</id/plugins/hooks>)


## Cantumkan semua pengait

bashCopy code
[code]
    openclaw hooks list
[/code]

Cantumkan semua pengait yang ditemukan dari direktori workspace, terkelola, tambahan, dan bawaan. Startup Gateway tidak memuat handler pengait internal hingga setidaknya satu pengait internal dikonfigurasi.

**Opsi:**

  * `--eligible`: Tampilkan hanya pengait yang memenuhi syarat (persyaratan terpenuhi)
  * `--json`: Keluarkan sebagai JSON
  * `-v, --verbose`: Tampilkan informasi terperinci termasuk persyaratan yang belum terpenuhi


**Contoh output:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Contoh (verbose):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Menampilkan persyaratan yang belum terpenuhi untuk pengait yang tidak memenuhi syarat.

**Contoh (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Mengembalikan JSON terstruktur untuk penggunaan terprogram.

## Dapatkan informasi pengait

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Tampilkan informasi terperinci tentang pengait tertentu.

**Argumen:**

  * `<name>`: Nama pengait atau kunci pengait (misalnya, `session-memory`)


**Opsi:**

  * `--json`: Keluarkan sebagai JSON


**Contoh:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Output:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Periksa kelayakan pengait

bashCopy code
[code]
    openclaw hooks check
[/code]

Tampilkan ringkasan status kelayakan pengait (berapa banyak yang siap dibandingkan yang belum siap).

**Opsi:**

  * `--json`: Keluarkan sebagai JSON


**Contoh output:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Aktifkan Pengait

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Aktifkan pengait tertentu dengan menambahkannya ke konfigurasi Anda (`~/.openclaw/openclaw.json` secara default).

**Catatan:** Pengait workspace dinonaktifkan secara default hingga diaktifkan di sini atau dalam konfigurasi. Pengait yang dikelola oleh plugin menampilkan `plugin:<id>` di `openclaw hooks list` dan tidak dapat diaktifkan/dinonaktifkan di sini. Aktifkan/nonaktifkan plugin-nya sebagai gantinya.

**Argumen:**

  * `<name>`: Nama pengait (misalnya, `session-memory`)


**Contoh:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Yang dilakukannya:**

  * Memeriksa apakah pengait ada dan memenuhi syarat
  * Memperbarui `hooks.internal.entries.<name>.enabled = true` dalam konfigurasi Anda
  * Menyimpan konfigurasi ke disk


Jika pengait berasal dari `<workspace>/hooks/`, langkah opt-in ini diperlukan sebelum Gateway akan memuatnya.

**Setelah mengaktifkan:**

  * Mulai ulang gateway agar pengait dimuat ulang (mulai ulang aplikasi bilah menu di macOS, atau mulai ulang proses gateway Anda dalam dev).


## Nonaktifkan Pengait

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Nonaktifkan pengait tertentu dengan memperbarui konfigurasi Anda.

**Argumen:**

  * `<name>`: Nama pengait (misalnya, `command-logger`)


**Contoh:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Output:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Setelah menonaktifkan:**

  * Mulai ulang gateway agar pengait dimuat ulang


## Catatan

  * `openclaw hooks list --json`, `info --json`, dan `check --json` menulis JSON terstruktur langsung ke stdout.
  * Pengait yang dikelola Plugin tidak dapat diaktifkan atau dinonaktifkan di sini; aktifkan atau nonaktifkan plugin pemiliknya sebagai gantinya.


## Pasang paket pengait

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Pasang paket pengait melalui pemasang plugin terpadu.

`openclaw hooks install` masih berfungsi sebagai alias kompatibilitas, tetapi mencetak peringatan penghentian dan meneruskan ke `openclaw plugins install`.

Spesifikasi npm bersifat **hanya-registry** (nama paket + **versi persis** opsional atau **dist-tag**). Spesifikasi Git/URL/file dan rentang semver ditolak. Pemasangan dependensi berjalan lokal-proyek dengan `--ignore-scripts` demi keamanan, bahkan ketika shell Anda memiliki pengaturan pemasangan npm global.

Spesifikasi polos dan `@latest` tetap berada di jalur stabil. Jika npm menyelesaikan salah satu dari itu ke prarilis, OpenClaw berhenti dan meminta Anda ikut serta secara eksplisit dengan tag prarilis seperti `@beta`/`@rc` atau versi prarilis persis.

**Yang dilakukannya:**

  * Menyalin paket pengait ke `~/.openclaw/hooks/<id>`
  * Mengaktifkan pengait yang dipasang di `hooks.internal.entries.*`
  * Mencatat pemasangan di bawah `hooks.internal.installs`


**Opsi:**

  * `-l, --link`: Tautkan direktori lokal alih-alih menyalin (menambahkannya ke `hooks.internal.load.extraDirs`)
  * `--pin`: Catat pemasangan npm sebagai `name@version` hasil penyelesaian persis di `hooks.internal.installs`


**Arsip yang didukung:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Contoh:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Paket pengait tertaut diperlakukan sebagai pengait terkelola dari direktori yang dikonfigurasi operator, bukan sebagai pengait workspace.

## Perbarui paket pengait

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Perbarui paket pengait berbasis npm yang dilacak melalui pembaru plugin terpadu.

`openclaw hooks update` masih berfungsi sebagai alias kompatibilitas, tetapi mencetak peringatan penghentian dan meneruskan ke `openclaw plugins update`.

**Opsi:**

  * `--all`: Perbarui semua paket pengait yang dilacak
  * `--dry-run`: Tampilkan apa yang akan berubah tanpa menulis


Ketika hash integritas tersimpan ada dan hash artefak yang diambil berubah, OpenClaw mencetak peringatan dan meminta konfirmasi sebelum melanjutkan. Gunakan `--yes` global untuk melewati prompt dalam CI/proses noninteraktif.

## Pengait bawaan

### session-memory

Menyimpan konteks sesi ke memori saat Anda mengeluarkan `/new` atau `/reset`.

**Aktifkan:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` secara default. Tetapkan `hooks.internal.entries.session-memory.llmSlug: true` untuk slug nama file yang dibuat model.

**Lihat:** [dokumentasi session-memory](</id/automation/hooks#session-memory>)

### bootstrap-extra-files

Menyuntikkan file bootstrap tambahan (misalnya `AGENTS.md` / `TOOLS.md` lokal-monorepo) selama `agent:bootstrap`.

**Aktifkan:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Lihat:** [dokumentasi bootstrap-extra-files](</id/automation/hooks#bootstrap-extra-files>)

### command-logger

Mencatat semua peristiwa perintah ke file audit terpusat.

**Aktifkan:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Output:** `~/.openclaw/logs/commands.log`

**Lihat log:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Lihat:** [dokumentasi command-logger](</id/automation/hooks#command-logger>)

### boot-md

Menjalankan `BOOT.md` saat gateway dimulai (setelah channel dimulai).

**Peristiwa** : `gateway:startup`

**Aktifkan** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Lihat:** [dokumentasi boot-md](</id/automation/hooks#boot-md>)

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Pengait otomasi](</id/automation/hooks>)


Was this useful?YesNo