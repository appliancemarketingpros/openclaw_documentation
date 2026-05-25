---
title: Penelusuran Kesalahan
source_url: https://docs.openclaw.ai/id/help/debugging
scraped_at: 2026-05-25
---

Pembantu debugging untuk output streaming, terutama ketika provider mencampur reasoning ke dalam teks normal.

## Override debug runtime

Gunakan `/debug` dalam chat untuk menetapkan override konfigurasi **khusus runtime** (memori, bukan disk). `/debug` dinonaktifkan secara default; aktifkan dengan `commands.debug: true`. Ini berguna ketika Anda perlu mengaktifkan atau menonaktifkan pengaturan yang kurang umum tanpa mengedit `openclaw.json`.

Contoh:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` menghapus semua override dan kembali ke konfigurasi di disk.

## Output trace sesi

Gunakan `/trace` ketika Anda ingin melihat baris trace/debug milik plugin dalam satu sesi tanpa mengaktifkan mode verbose penuh.

Contoh:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Gunakan `/trace` untuk diagnostik plugin seperti ringkasan debug Active Memory. Tetap gunakan `/verbose` untuk status/output tool verbose normal, dan tetap gunakan `/debug` untuk override konfigurasi khusus runtime.

## Trace siklus hidup Plugin

Gunakan `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` ketika perintah siklus hidup plugin terasa lambat dan Anda memerlukan rincian fase bawaan untuk metadata plugin, penemuan, registry, mirror runtime, mutasi konfigurasi, dan pekerjaan refresh. Trace ini opt-in dan menulis ke stderr, sehingga output perintah JSON tetap dapat diurai.

Contoh:

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

Contoh output:

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

Gunakan ini untuk investigasi siklus hidup plugin sebelum memakai profiler CPU. Jika perintah berjalan dari source checkout, sebaiknya ukur runtime hasil build dengan `node dist/entry.js ...` setelah `pnpm build`; `pnpm openclaw ...` juga mengukur overhead source-runner.

## Startup CLI dan profiling perintah

Gunakan benchmark startup yang sudah disertakan ketika sebuah perintah terasa lambat:

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

Untuk profiling sekali jalan melalui source runner normal, tetapkan `OPENCLAW_RUN_NODE_CPU_PROF_DIR`:

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

Source runner menambahkan flag profil CPU Node dan menulis `.cpuprofile` untuk perintah tersebut. Gunakan ini sebelum menambahkan instrumentasi sementara ke kode perintah.

Untuk hambatan startup yang tampak seperti pekerjaan filesystem sinkron atau module-loader, tambahkan flag trace I/O sinkron Node melalui source runner:

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch` membiarkan flag ini dinonaktifkan secara default untuk child Gateway yang dipantau. Tetapkan `OPENCLAW_TRACE_SYNC_IO=1` ketika Anda secara eksplisit menginginkan output trace I/O sinkron Node dalam mode watch.

## Mode watch Gateway

Untuk iterasi cepat, jalankan gateway di bawah file watcher:

bashCopy code
[code]
    pnpm gateway:watch
[/code]

Secara default, ini memulai atau memulai ulang sesi tmux bernama `openclaw-gateway-watch-main` (atau varian spesifik profil/port seperti `openclaw-gateway-watch-dev-19001`) dan otomatis melampirkan dari terminal interaktif. Shell noninteraktif, CI, dan panggilan exec agen tetap detached dan mencetak instruksi attach sebagai gantinya. Attach secara manual bila diperlukan:

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

Pane tmux menjalankan watcher mentah:

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

Gunakan mode foreground ketika tmux tidak diinginkan:

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

Nonaktifkan auto-attach sambil tetap mempertahankan manajemen tmux:

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

Profilkan waktu CPU Gateway yang dipantau ketika men-debug hotspot startup/runtime:

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

Wrapper watch memakai `--benchmark` sebelum memanggil Gateway dan menulis satu `.cpuprofile` V8 per child Gateway yang keluar di bawah `.artifacts/gateway-watch-profiles/`. Hentikan atau mulai ulang gateway yang dipantau untuk mem-flush profil saat ini, lalu buka dengan Chrome DevTools atau Speedscope:

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

Gunakan `--benchmark-dir <path>` ketika Anda menginginkan profil di tempat lain. Gunakan `--benchmark-no-force` ketika Anda ingin child yang di-benchmark melewati pembersihan port default `--force` dan gagal cepat jika port Gateway sudah digunakan. Mode benchmark menekan spam trace sync-I/O secara default. Tetapkan `OPENCLAW_TRACE_SYNC_IO=1` dengan `--benchmark` ketika Anda secara eksplisit menginginkan profil CPU dan stack trace sync-I/O Node. Dalam mode benchmark, blok trace tersebut ditulis ke `gateway-watch-output.log` di bawah direktori benchmark dan difilter dari pane terminal; log Gateway normal tetap terlihat.

Wrapper tmux membawa selector runtime non-rahasia umum seperti `OPENCLAW_PROFILE`, `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, `OPENCLAW_GATEWAY_PORT`, dan `OPENCLAW_SKIP_CHANNELS` ke dalam pane. Letakkan kredensial provider dalam profil/konfigurasi normal Anda, atau gunakan mode foreground mentah untuk rahasia ephemeral sekali pakai. Jika Gateway yang dipantau keluar selama startup, watcher menjalankan `openclaw doctor --fix --non-interactive` sekali dan memulai ulang child Gateway. Gunakan `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0` ketika Anda menginginkan kegagalan startup asli tanpa pass perbaikan khusus dev. Pane tmux terkelola juga default ke log Gateway berwarna agar mudah dibaca; tetapkan `FORCE_COLOR=0` saat memulai `pnpm gateway:watch` untuk menonaktifkan output ANSI.

Watcher memulai ulang pada file yang relevan untuk build di bawah `src/`, file sumber extension, metadata `package.json` dan `openclaw.plugin.json` extension, `tsconfig.json`, `package.json`, dan `tsdown.config.ts`. Perubahan metadata extension memulai ulang gateway tanpa memaksa rebuild `tsdown`; perubahan sumber dan konfigurasi tetap membangun ulang `dist` terlebih dahulu.

Tambahkan flag CLI gateway apa pun setelah `gateway:watch` dan flag itu akan diteruskan pada setiap restart. Menjalankan ulang perintah watch yang sama akan mem-spawn ulang pane tmux bernama tersebut, dan watcher mentah tetap menjaga lock single-watcher-nya sehingga parent watcher duplikat diganti, bukan menumpuk.

## Profil dev + gateway dev (--dev)

Gunakan profil dev untuk mengisolasi state dan menjalankan setup aman yang dapat dibuang untuk debugging. Ada **dua** flag `--dev`:

  * **Global`--dev` (profil):** mengisolasi state di bawah `~/.openclaw-dev` dan menetapkan port gateway default ke `19001` (port turunan ikut bergeser).
  * **`gateway --dev`: memberi tahu Gateway untuk otomatis membuat konfigurasi default + workspace** ketika belum ada (dan melewati [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).


Alur yang direkomendasikan (profil dev + bootstrap dev):

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

Jika Anda belum memiliki instalasi global, jalankan CLI melalui `pnpm openclaw ...`.

Yang dilakukan ini:

  1. **Isolasi profil** (global `--dev`)

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (browser/canvas bergeser sesuai itu)
  2. **Bootstrap dev** (`gateway --dev`)

     * Menulis konfigurasi minimal jika belum ada (`gateway.mode=local`, bind loopback).
     * Menetapkan `agent.workspace` ke workspace dev.
     * Menetapkan `agent.skipBootstrap=true` (tanpa [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).
     * Menyemai file workspace jika belum ada: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Identitas default: **C3-PO** (droid protokol).
     * Melewati provider channel dalam mode dev (`OPENCLAW_SKIP_CHANNELS=1`).


Alur reset (mulai baru):

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset` menghapus konfigurasi, kredensial, sesi, dan workspace dev (menggunakan `trash`, bukan `rm`), lalu membuat ulang setup dev default.

## Logging stream mentah (OpenClaw)

OpenClaw dapat mencatat **stream assistant mentah** sebelum filtering/formatting apa pun. Ini adalah cara terbaik untuk melihat apakah reasoning tiba sebagai delta teks biasa (atau sebagai blok berpikir terpisah).

Aktifkan melalui CLI:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

Override path opsional:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

Env var ekuivalen:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

File default:

`~/.openclaw/logs/raw-stream.jsonl`

## Logging chunk mentah (pi-mono)

Untuk menangkap **chunk kompatibel OpenAI mentah** sebelum diurai menjadi blok, pi-mono mengekspos logger terpisah:

bashCopy code
[code]
    PI_RAW_STREAM=1
[/code]

Path opsional:

bashCopy code
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
[/code]

File default:

`~/.pi-mono/logs/raw-openai-completions.jsonl`

> Catatan: ini hanya dikeluarkan oleh proses yang menggunakan provider `openai-completions` milik pi-mono.

## Catatan keamanan

  * Log stream mentah dapat menyertakan prompt lengkap, output tool, dan data pengguna.
  * Simpan log secara lokal dan hapus setelah debugging.
  * Jika Anda membagikan log, bersihkan rahasia dan PII terlebih dahulu.


## Debugging di VSCode

Source map diperlukan untuk mengaktifkan debugging di IDE berbasis VSCode karena banyak file yang dihasilkan berakhir dengan nama hash sebagai bagian dari proses build. Konfigurasi `launch.json` yang disertakan menargetkan layanan Gateway, tetapi dapat diadaptasi dengan cepat untuk tujuan lain:

  1. **Rebuild and Debug Gateway** \- Men-debug layanan Gateway setelah membuat build baru
  2. **Debug Gateway** \- Men-debug layanan Gateway dari build yang sudah ada


### Setup

Konfigurasi default **Rebuild and Debug Gateway** sudah lengkap, konfigurasi ini akan otomatis menghapus folder `/dist` dan membangun ulang proyek dengan debugging diaktifkan:

  1. Buka panel **Run and Debug** dari Activity Bar atau tekan `Ctrl`+`Shift`+`D`
  2. Di IDE, pastikan **Rebuild and Debug Gateway** dipilih di dropdown konfigurasi lalu tekan tombol **Start Debugging**


Alternatifnya - jika Anda lebih suka mengelola proses build dan debug secara manual:

  1. Buka terminal dan aktifkan source map: 
     * **Linux/macOS** : `export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** : `$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** : `set OUTPUT_SOURCE_MAPS=1`
  2. Di terminal yang sama, build ulang proyek: `pnpm clean:dist && pnpm build`
  3. Di IDE, pilih opsi **Debug Gateway** di dropdown konfigurasi **Run and Debug** lalu tekan tombol **Start Debugging**


Sekarang Anda dapat menetapkan breakpoint di file sumber TypeScript Anda (direktori `src/`) dan debugger akan memetakan breakpoint dengan benar ke JavaScript terkompilasi melalui source map. Anda akan dapat memeriksa variabel, melangkah melalui kode, dan memeriksa call stack sesuai harapan.

### Catatan

  * Jika menggunakan opsi **"Rebuild and Debug Gateway"** \- setiap kali debugger diluncurkan, folder `/dist` akan dihapus sepenuhnya dan `pnpm build` penuh dengan source map aktif akan dijalankan sebelum memulai Gateway
  * Jika menggunakan opsi **"Debug Gateway"** \- sesi debug dapat dimulai dan dihentikan kapan saja tanpa memengaruhi folder `/dist`, tetapi Anda harus menggunakan proses terminal terpisah untuk mengaktifkan debugging sekaligus mengelola siklus build
  * Ubah pengaturan `launch.json` untuk `args` guna men-debug bagian lain dari proyek
  * Jika Anda perlu menggunakan CLI OpenClaw hasil build untuk tugas lain (misalnya `dashboard --no-open` jika sesi debug Anda memunculkan token auth baru), Anda dapat menjalankannya di terminal lain sebagai `node ./openclaw.mjs` atau membuat alias shell seperti `alias openclaw-build="node $(pwd)/openclaw.mjs"`


## Terkait

  * [Pemecahan masalah](</id/help/troubleshooting>)
  * [FAQ](</id/help/faq>)


Was this useful?YesNo