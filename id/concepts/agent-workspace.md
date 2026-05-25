---
title: Ruang kerja agen
source_url: https://docs.openclaw.ai/id/concepts/agent-workspace
scraped_at: 2026-05-25
---

Workspace adalah rumah agen. Ini adalah satu-satunya direktori kerja yang digunakan untuk alat file dan konteks workspace. Jaga agar tetap privat dan perlakukan sebagai memori.

Ini terpisah dari `~/.openclaw/`, yang menyimpan konfigurasi, kredensial, dan sesi.

## Lokasi default

  * Default: `~/.openclaw/workspace`
  * Jika `OPENCLAW_PROFILE` disetel dan bukan `"default"`, default menjadi `~/.openclaw/workspace-<profile>`.
  * Timpa di `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure`, atau `openclaw setup` akan membuat workspace dan mengisi file bootstrap jika belum ada.

Jika Anda sudah mengelola file workspace sendiri, Anda dapat menonaktifkan pembuatan file bootstrap:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Folder workspace tambahan

Instalasi lama mungkin telah membuat `~/openclaw`. Menyimpan beberapa direktori workspace dapat menyebabkan auth atau state drift yang membingungkan, karena hanya satu workspace yang aktif pada satu waktu.

## Peta file workspace

Berikut adalah file standar yang diharapkan OpenClaw di dalam workspace:

AGENTS.md - instruksi operasional

Instruksi operasional untuk agen dan cara agen harus menggunakan memori. Dimuat pada awal setiap sesi. Tempat yang baik untuk aturan, prioritas, dan detail "cara berperilaku".

SOUL.md - persona dan nada

Persona, nada, dan batasan. Dimuat setiap sesi. Panduan: [panduan kepribadian SOUL.md](</id/concepts/soul>).

USER.md - siapa pengguna

Siapa pengguna dan cara menyapa mereka. Dimuat setiap sesi.

IDENTITY.md - nama, vibe, emoji

Nama, vibe, dan emoji agen. Dibuat/diperbarui selama ritual bootstrap.

TOOLS.md - konvensi alat lokal

Catatan tentang alat dan konvensi lokal Anda. Tidak mengontrol ketersediaan alat; ini hanya panduan.

HEARTBEAT.md - daftar periksa Heartbeat

Daftar periksa kecil opsional untuk proses Heartbeat. Jaga tetap singkat untuk menghindari pemborosan token.

BOOT.md - daftar periksa startup

Daftar periksa startup opsional yang dijalankan otomatis saat Gateway dimulai ulang (ketika [hook internal](</id/automation/hooks>) diaktifkan). Jaga tetap singkat; gunakan alat pesan untuk pengiriman keluar.

BOOTSTRAP.md - ritual proses pertama

Ritual sekali untuk proses pertama. Hanya dibuat untuk workspace yang benar-benar baru. Hapus setelah ritual selesai.

memory/YYYY-MM-DD.md - log memori harian

Log memori harian (satu file per hari). Disarankan untuk membaca hari ini + kemarin saat sesi dimulai.

MEMORY.md - memori jangka panjang terkurasi (opsional)

Memori jangka panjang terkurasi: fakta, preferensi, keputusan, dan ringkasan singkat yang tahan lama. Simpan log terperinci di `memory/YYYY-MM-DD.md` agar alat memori dapat mengambilnya saat diperlukan tanpa menyuntikkannya ke setiap prompt. Muat `MEMORY.md` hanya di sesi utama yang privat (bukan konteks bersama/grup). Lihat [Memori](</id/concepts/memory>) untuk alur kerja dan flush memori otomatis.

skills/ - Skills workspace (opsional)

Skills khusus workspace. Lokasi skill dengan prioritas tertinggi untuk workspace tersebut. Mengesampingkan Skills agen proyek, Skills agen personal, Skills terkelola, Skills bawaan, dan `skills.load.extraDirs` saat nama bertabrakan.

canvas/ - file UI Canvas (opsional)

File UI Canvas untuk tampilan node (misalnya `canvas/index.html`).

## Yang TIDAK ada di workspace

Ini berada di bawah `~/.openclaw/` dan TIDAK boleh di-commit ke repo workspace:

  * `~/.openclaw/openclaw.json` (konfigurasi)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (profil auth model: OAuth + kunci API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (akun runtime Codex per agen, konfigurasi, Skills, plugin, dan state thread native)
  * `~/.openclaw/credentials/` (state channel/provider plus data impor OAuth lama)
  * `~/.openclaw/agents/<agentId>/sessions/` (transkrip sesi + metadata)
  * `~/.openclaw/skills/` (Skills terkelola)


Jika Anda perlu memigrasikan sesi atau konfigurasi, salin secara terpisah dan jauhkan dari kontrol versi.

## Backup Git (disarankan, privat)

Perlakukan workspace sebagai memori privat. Masukkan ke repo git **privat** agar dicadangkan dan dapat dipulihkan.

Jalankan langkah-langkah ini di mesin tempat Gateway berjalan (di situlah workspace berada).

* ### Inisialisasi repo

Jika git terinstal, workspace yang benar-benar baru diinisialisasi secara otomatis. Jika workspace ini belum menjadi repo, jalankan:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Tambahkan remote privat

### UI web GitHub

  1. Buat repositori **privat** baru di GitHub.
  2. Jangan inisialisasi dengan README (menghindari konflik merge).
  3. Salin URL remote HTTPS.
  4. Tambahkan remote dan push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### UI web GitLab

  1. Buat repositori **privat** baru di GitLab.
  2. Jangan inisialisasi dengan README (menghindari konflik merge).
  3. Salin URL remote HTTPS.
  4. Tambahkan remote dan push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Pembaruan berkelanjutan

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Jangan commit rahasia

Starter `.gitignore` yang disarankan:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Memindahkan workspace ke mesin baru

* ### Clone repo

Clone repo ke jalur yang diinginkan (default `~/.openclaw/workspace`).

* ### Perbarui konfigurasi

Setel `agents.defaults.workspace` ke jalur tersebut di `~/.openclaw/openclaw.json`.

* ### Seed file yang hilang

Jalankan `openclaw setup --workspace <path>` untuk mengisi file yang hilang.

* ### Salin sesi (opsional)

Jika Anda memerlukan sesi, salin `~/.openclaw/agents/<agentId>/sessions/` dari mesin lama secara terpisah.

## Catatan lanjutan

  * Routing multi-agen dapat menggunakan workspace berbeda per agen. Lihat [Routing channel](</id/channels/channel-routing>) untuk konfigurasi routing.
  * Jika `agents.defaults.sandbox` diaktifkan, sesi non-utama dapat menggunakan workspace sandbox per sesi di bawah `agents.defaults.sandbox.workspaceRoot`.


## Terkait

  * [Heartbeat](</id/gateway/heartbeat>) \- file workspace [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</id/gateway/sandboxing>) \- akses workspace di lingkungan tersandbox
  * [Sesi](</id/concepts/session>) \- jalur penyimpanan sesi
  * [Standing orders](</id/automation/standing-orders>) \- instruksi persisten dalam file workspace


Was this useful?YesNo