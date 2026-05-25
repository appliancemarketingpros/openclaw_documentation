---
title: Membangun Plugin backend CLI
source_url: https://docs.openclaw.ai/id/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

Plugin backend CLI memungkinkan OpenClaw memanggil CLI AI lokal sebagai backend inferensi teks. Backend muncul sebagai prefiks penyedia dalam referensi model:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Gunakan backend CLI ketika integrasi upstream sudah diekspos sebagai perintah lokal, ketika CLI memiliki status login lokal, atau ketika CLI berguna sebagai fallback jika penyedia API tidak tersedia.

## Yang dimiliki Plugin

Plugin backend CLI memiliki tiga kontrak:

Kontrak | File | Tujuan  
---|---|---  
Entri paket | `package.json` | Mengarahkan OpenClaw ke modul runtime Plugin  
Kepemilikan manifest | `openclaw.plugin.json` | Mendeklarasikan id backend sebelum runtime dimuat  
Pendaftaran runtime | `index.ts` | Memanggil `api.registerCliBackend(...)` dengan default perintah  
  
Manifest adalah metadata penemuan. Manifest tidak menjalankan CLI dan tidak mendaftarkan perilaku runtime. Perilaku runtime dimulai saat entri Plugin memanggil `api.registerCliBackend(...)`.

## Plugin backend minimal

* ### Buat metadata paket

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Paket yang dipublikasikan harus menyertakan file runtime JavaScript yang sudah dibangun. Jika entri sumber Anda adalah `./src/index.ts`, tambahkan `openclaw.runtimeExtensions` yang menunjuk ke peer JavaScript yang sudah dibangun. Lihat [Titik entri](</id/plugins/sdk-entrypoints>).

* ### Deklarasikan kepemilikan backend

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` adalah daftar kepemilikan runtime. Ini memungkinkan OpenClaw memuat Plugin secara otomatis ketika konfigurasi atau pemilihan model menyebut `acme-cli/...`.

`setup.cliBackends` adalah permukaan setup berbasis deskriptor terlebih dahulu. Tambahkan ini ketika penemuan model, onboarding, atau status harus mengenali backend tanpa memuat runtime Plugin. Gunakan `requiresRuntime: false` hanya ketika deskriptor statis tersebut cukup untuk setup.

* ### Daftarkan backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

Id backend harus cocok dengan entri `cliBackends` manifest. `config` yang didaftarkan hanya default; konfigurasi pengguna di bawah `agents.defaults.cliBackends.acme-cli` digabungkan di atasnya saat runtime.

## Bentuk konfigurasi

`CliBackendConfig` menjelaskan bagaimana OpenClaw harus meluncurkan dan mengurai CLI:

Bidang | Penggunaan  
---|---  
`command` | Nama biner atau path perintah absolut  
`args` | argv dasar untuk eksekusi baru  
`resumeArgs` | argv alternatif untuk sesi yang dilanjutkan; mendukung `{sessionId}`  
`output` / `resumeOutput` | Parser: `json`, `jsonl`, atau `text`  
`input` | Transport prompt: `arg` atau `stdin`  
`modelArg` | Flag yang digunakan sebelum id model  
`modelAliases` | Memetakan id model OpenClaw ke id native CLI  
`sessionArg` / `sessionArgs` | Cara meneruskan id sesi  
`sessionMode` | `always`, `existing`, atau `none`  
`sessionIdFields` | Bidang JSON yang dibaca OpenClaw dari output CLI  
`systemPromptArg` / `systemPromptFileArg` | Transport prompt sistem  
`systemPromptWhen` | `first`, `always`, atau `never`  
`imageArg` / `imageMode` | Dukungan path gambar  
`serialize` | Menjaga eksekusi backend yang sama tetap berurutan  
`reliability.watchdog` | Penyesuaian timeout tanpa output  
  
Pilih konfigurasi statis terkecil yang cocok dengan CLI. Tambahkan callback Plugin hanya untuk perilaku yang benar-benar menjadi milik backend.

## Hook backend lanjutan

`CliBackendPlugin` juga dapat mendefinisikan:

Hook | Penggunaan  
---|---  
`normalizeConfig(config, context)` | Menulis ulang konfigurasi pengguna lama setelah merge  
`resolveExecutionArgs(ctx)` | Menambahkan flag berlingkup permintaan seperti effort berpikir  
`prepareExecution(ctx)` | Membuat jembatan autentikasi atau konfigurasi sementara sebelum peluncuran  
`transformSystemPrompt(ctx)` | Menerapkan transformasi prompt sistem akhir yang spesifik CLI  
`textTransforms` | Penggantian prompt/output dua arah  
`defaultAuthProfileId` | Memilih profil autentikasi OpenClaw tertentu  
`authEpochMode` | Menentukan bagaimana perubahan autentikasi membatalkan sesi CLI tersimpan  
`nativeToolMode` | Mendeklarasikan apakah CLI memiliki alat native yang selalu aktif  
`bundleMcp` / `bundleMcpMode` | Mengikutsertakan jembatan alat MCP loopback OpenClaw  
  
Jaga agar hook ini tetap dimiliki penyedia. Jangan menambahkan cabang spesifik CLI ke core ketika hook backend dapat mengekspresikan perilaku tersebut.

## Jembatan alat MCP

Backend CLI tidak menerima alat OpenClaw secara default. Jika CLI dapat mengonsumsi konfigurasi MCP, ikut sertakan secara eksplisit:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Mode jembatan yang didukung adalah:

Mode | Penggunaan  
---|---  
`claude-config-file` | CLI yang menerima file konfigurasi MCP  
`codex-config-overrides` | CLI yang menerima override konfigurasi pada argv  
`gemini-system-settings` | CLI yang membaca pengaturan MCP dari direktori pengaturan sistemnya  
  
Aktifkan jembatan hanya ketika CLI benar-benar dapat mengonsumsinya. Jika CLI memiliki lapisan alat bawaan sendiri yang tidak dapat dinonaktifkan, tetapkan `nativeToolMode: "always-on"` agar OpenClaw dapat gagal secara tertutup ketika pemanggil mensyaratkan tidak ada alat native.

## Konfigurasi pengguna

Pengguna dapat menimpa default backend apa pun:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Dokumentasikan override minimum yang kemungkinan dibutuhkan pengguna. Biasanya itu hanya `command` ketika biner berada di luar `PATH`.

## Verifikasi

Untuk Plugin yang dibundel, tambahkan pengujian terfokus di sekitar builder dan pendaftaran setup, lalu jalankan lane pengujian tertarget milik Plugin:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Untuk Plugin lokal atau terpasang, verifikasi penemuan dan satu eksekusi model nyata:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Jika backend mendukung gambar atau MCP, tambahkan smoke langsung yang membuktikan path tersebut dengan CLI nyata. Jangan mengandalkan inspeksi statis untuk perilaku prompt, gambar, MCP, atau lanjutkan-sesi.

## Checklist

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` memiliki `openclaw.extensions` dan entri runtime yang sudah dibangun untuk paket yang dipublikasikan OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` mendeklarasikan `cliBackends` dan `activation.onStartup` yang disengaja OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` hadir ketika setup/penemuan model harus melihat backend dalam keadaan dingin OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` menggunakan id backend yang sama dengan manifest OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Override pengguna di bawah `agents.defaults.cliBackends.<id>` tetap menang OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo