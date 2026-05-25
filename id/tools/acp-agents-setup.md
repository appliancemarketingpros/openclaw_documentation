---
title: Agen ACP — penyiapan
source_url: https://docs.openclaw.ai/id/tools/acp-agents-setup
scraped_at: 2026-05-25
---

Untuk ikhtisar, runbook operator, dan konsep, lihat [agen ACP](</id/tools/acp-agents>).

Bagian di bawah ini mencakup konfigurasi harness acpx, penyiapan plugin untuk bridge MCP, dan konfigurasi izin.

Gunakan halaman ini hanya saat Anda menyiapkan rute ACP/acpx. Untuk konfigurasi runtime app-server Codex native, gunakan [harness Codex](</id/plugins/codex-harness>). Untuk kunci OpenAI API atau konfigurasi penyedia model OAuth Codex, gunakan [OpenAI](</id/providers/openai>).

Codex memiliki dua rute OpenClaw:

Rute | Konfigurasi/perintah | Halaman penyiapan  
---|---|---  
App-server Codex native | `/codex ...`, ref agen `openai/gpt-*` | [harness Codex](</id/plugins/codex-harness>)  
Adapter ACP Codex eksplisit | `/acp spawn codex`, `runtime: "acp", agentId: "codex"` | Halaman ini  
  
Pilih rute native kecuali Anda secara eksplisit membutuhkan perilaku ACP/acpx.

## Dukungan harness acpx (saat ini)

Alias harness bawaan acpx saat ini:

  * `claude`
  * `codex`
  * `copilot`
  * `cursor` (Cursor CLI: `cursor-agent acp`)
  * `droid`
  * `gemini`
  * `iflow`
  * `kilocode`
  * `kimi`
  * `kiro`
  * `openclaw`
  * `opencode`
  * `pi`
  * `qwen`


Saat OpenClaw menggunakan backend acpx, pilih nilai-nilai ini untuk `agentId` kecuali konfigurasi acpx Anda mendefinisikan alias agen kustom. Jika instalasi Cursor lokal Anda masih mengekspos ACP sebagai `agent acp`, override perintah agen `cursor` di konfigurasi acpx Anda alih-alih mengubah default bawaan.

Penggunaan CLI acpx langsung juga dapat menargetkan adapter arbitrer melalui `--agent <command>`, tetapi escape hatch mentah tersebut adalah fitur CLI acpx (bukan jalur `agentId` OpenClaw normal).

Kontrol model bergantung pada kapabilitas adapter. Ref model ACP Codex dinormalisasi oleh OpenClaw sebelum startup. Harness lain membutuhkan ACP `models` plus dukungan `session/set_model`; jika sebuah harness tidak mengekspos kapabilitas ACP tersebut maupun flag model startup miliknya sendiri, OpenClaw/acpx tidak dapat memaksa pemilihan model.

## Konfigurasi wajib

Baseline inti ACP:

json5Copy code
[code]
    {  acp: {    enabled: true,    // Optional. Default is true; set false to pause ACP dispatch while keeping /acp controls.    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "codex",    allowedAgents: [      "claude",      "codex",      "copilot",      "cursor",      "droid",      "gemini",      "iflow",      "kilocode",      "kimi",      "kiro",      "openclaw",      "opencode",      "pi",      "qwen",    ],    maxConcurrentSessions: 8,    stream: {      coalesceIdleMs: 300,      maxChunkChars: 1200,    },    runtime: {      ttlMinutes: 120,    },  },}
[/code]

Konfigurasi pengikatan thread bersifat spesifik per adapter channel. Contoh untuk Discord:

json5Copy code
[code]
    {  session: {    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },  },  channels: {    discord: {      threadBindings: {        enabled: true,        spawnSessions: true,      },    },  },}
[/code]

Jika spawn ACP yang terikat thread tidak berfungsi, verifikasi flag fitur adapter terlebih dahulu:

  * Discord: `channels.discord.threadBindings.spawnSessions=true`


Bind percakapan saat ini tidak membutuhkan pembuatan thread anak. Bind tersebut membutuhkan konteks percakapan aktif dan adapter channel yang mengekspos pengikatan percakapan ACP.

Lihat [Referensi Konfigurasi](</id/gateway/configuration-reference>).

## Penyiapan plugin untuk backend acpx

Instalasi paket menggunakan plugin runtime resmi `@openclaw/acpx` untuk ACP. Instal dan aktifkan sebelum menggunakan sesi harness ACP:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Checkout source juga dapat menggunakan plugin workspace lokal setelah `pnpm install`.

Mulai dengan:

textCopy code
[code]
    /acp doctor
[/code]

Jika Anda menonaktifkan `acpx`, menolaknya melalui `plugins.allow` / `plugins.deny`, atau ingin beralih kembali ke plugin paket, gunakan path paket eksplisit:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Instalasi workspace lokal selama pengembangan:

bashCopy code
[code]
    openclaw plugins install ./path/to/local/acpx-plugin
[/code]

Lalu verifikasi kesehatan backend:

textCopy code
[code]
    /acp doctor
[/code]

### Konfigurasi perintah dan versi acpx

Secara default, plugin `acpx` mem-probe backend ACP tertanam selama startup Gateway dan menunggu probe tersebut sebelum sinyal gateway `ready`. Setel `OPENCLAW_ACPX_RUNTIME_STARTUP_PROBE=0` untuk melewati probe startup dan mendaftarkan backend secara lazy. Jalankan `/acp doctor` untuk probe eksplisit sesuai permintaan.

Override perintah atau versi di konfigurasi plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "command": "../acpx/dist/cli.js",          "expectedVersion": "any"        }      }    }  }}
[/code]

  * `command` menerima path absolut, path relatif (di-resolve dari workspace OpenClaw), atau nama perintah.
  * `expectedVersion: "any"` menonaktifkan pencocokan versi ketat.
  * Path `command` kustom menonaktifkan instal otomatis lokal plugin.


Override perintah agen ACP individual dengan argumen terstruktur saat path atau nilai flag harus tetap menjadi satu token argv:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "agents": {            "claude": {              "command": "node",              "args": ["/path/to/custom adapter.mjs", "--verbose"]            }          }        }      }    }  }}
[/code]

  * `agents.<id>.command` adalah executable atau string perintah yang sudah ada untuk agen ACP tersebut.
  * `agents.<id>.args` bersifat opsional. Setiap item array diberi shell-quote sebelum OpenClaw meneruskannya melalui registry string perintah acpx saat ini.


Lihat [Plugin](</id/tools/plugin>).

### Instalasi dependensi otomatis

Saat Anda menginstal OpenClaw secara global dengan `npm install -g openclaw`, dependensi runtime acpx (biner spesifik platform) diinstal otomatis melalui hook postinstall. Jika instalasi otomatis gagal, gateway tetap berjalan normal dan melaporkan dependensi yang hilang melalui `openclaw acp doctor`.

### Bridge MCP tools plugin

Secara default, sesi ACPX **tidak** mengekspos tools yang didaftarkan plugin OpenClaw ke harness ACP.

Jika Anda ingin agen ACP seperti Codex atau Claude Code memanggil tools plugin OpenClaw yang terinstal seperti recall/store memori, aktifkan bridge khusus:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.pluginToolsMcpBridge true
[/code]

Yang dilakukan ini:

  * Menginjeksikan server MCP bawaan bernama `openclaw-plugin-tools` ke bootstrap sesi ACPX.
  * Mengekspos tools plugin yang sudah didaftarkan oleh plugin OpenClaw yang terinstal dan aktif.
  * Menjaga fitur ini tetap eksplisit dan default-nonaktif.


Catatan keamanan dan kepercayaan:

  * Ini memperluas permukaan tool harness ACP.
  * Agen ACP hanya mendapatkan akses ke tools plugin yang sudah aktif di gateway.
  * Perlakukan ini sebagai batas kepercayaan yang sama dengan mengizinkan plugin tersebut dieksekusi di OpenClaw itu sendiri.
  * Tinjau plugin yang terinstal sebelum mengaktifkannya.


`mcpServers` kustom tetap berfungsi seperti sebelumnya. Bridge plugin-tools bawaan adalah kemudahan opt-in tambahan, bukan pengganti konfigurasi server MCP generik.

### Bridge MCP tools OpenClaw

Secara default, sesi ACPX juga **tidak** mengekspos tools bawaan OpenClaw melalui MCP. Aktifkan bridge core-tools terpisah saat agen ACP membutuhkan tools bawaan tertentu seperti `cron`:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.openClawToolsMcpBridge true
[/code]

Yang dilakukan ini:

  * Menginjeksikan server MCP bawaan bernama `openclaw-tools` ke bootstrap sesi ACPX.
  * Mengekspos tools bawaan OpenClaw tertentu. Server awal mengekspos `cron`.
  * Menjaga eksposur core-tool tetap eksplisit dan default-nonaktif.


### Konfigurasi timeout runtime

Plugin `acpx` menetapkan default turn runtime tertanam ke timeout 120 detik. Ini memberi harness yang lebih lambat seperti Gemini CLI waktu yang cukup untuk menyelesaikan startup dan inisialisasi ACP. Override jika host Anda membutuhkan batas runtime yang berbeda:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.timeoutSeconds 180
[/code]

Restart gateway setelah mengubah nilai ini.

### Konfigurasi agen probe kesehatan

Saat `/acp doctor` atau probe startup memeriksa backend, plugin `acpx` bawaan mem-probe satu agen harness. Jika `acp.allowedAgents` disetel, default-nya adalah agen pertama yang diizinkan; jika tidak, default-nya adalah `codex`. Jika deployment Anda membutuhkan agen ACP yang berbeda untuk health check, setel agen probe secara eksplisit:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.probeAgent claude
[/code]

Restart gateway setelah mengubah nilai ini.

## Konfigurasi izin

Sesi ACP berjalan non-interaktif — tidak ada TTY untuk menyetujui atau menolak prompt izin file-write dan shell-exec. Plugin acpx menyediakan dua kunci konfigurasi yang mengontrol cara izin ditangani:

Izin harness ACPX ini terpisah dari persetujuan exec OpenClaw dan terpisah dari flag bypass vendor backend CLI seperti Claude CLI `--permission-mode bypassPermissions`. ACPX `approve-all` adalah switch darurat tingkat harness untuk sesi ACP.

### `permissionMode`

Mengontrol operasi mana yang dapat dilakukan agen harness tanpa prompt.

Nilai | Perilaku  
---|---  
`approve-all` | Setujui otomatis semua penulisan file dan perintah shell.  
`approve-reads` | Setujui otomatis hanya pembacaan; penulisan dan exec membutuhkan prompt.  
`deny-all` | Tolak semua prompt izin.  
  
### `nonInteractivePermissions`

Mengontrol apa yang terjadi saat prompt izin akan ditampilkan tetapi tidak ada TTY interaktif yang tersedia (yang selalu terjadi untuk sesi ACP).

Nilai | Perilaku  
---|---  
`fail` | Batalkan sesi dengan `AcpRuntimeError`. **(default)**  
`deny` | Tolak izin secara diam-diam dan lanjutkan (degradasi gracefully).  
  
### Konfigurasi

Setel melalui konfigurasi plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
[/code]

Restart gateway setelah mengubah nilai-nilai ini.

## Terkait

  * [agen ACP](</id/tools/acp-agents>) — ikhtisar, runbook operator, konsep
  * [Sub-agen](</id/tools/subagents>)
  * [Routing multi-agen](</id/concepts/multi-agent>)


Was this useful?YesNo