---
title: Grup siaran
source_url: https://docs.openclaw.ai/id/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Gambaran umum

Grup Broadcast memungkinkan beberapa agen memproses dan merespons pesan yang sama secara bersamaan. Ini memungkinkan Anda membuat tim agen terspesialisasi yang bekerja bersama dalam satu grup WhatsApp atau DM — semuanya menggunakan satu nomor telepon.

Cakupan saat ini: **hanya WhatsApp** (kanal web).

Grup broadcast dievaluasi setelah daftar izin kanal dan aturan aktivasi grup. Di grup WhatsApp, ini berarti broadcast terjadi ketika OpenClaw biasanya akan membalas (misalnya: saat disebut, bergantung pada pengaturan grup Anda).

## Kasus penggunaan

1\. Tim agen terspesialisasi

Terapkan beberapa agen dengan tanggung jawab yang atomik dan terfokus:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Setiap agen memproses pesan yang sama dan memberikan perspektif terspesialisasinya.

2\. Dukungan multi-bahasa CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Alur kerja jaminan kualitas CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Otomatisasi tugas CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Konfigurasi

### Penyiapan dasar

Tambahkan bagian `broadcast` tingkat atas (di sebelah `bindings`). Kunci adalah ID peer WhatsApp:

  * chat grup: JID grup (mis. `120363403215116621@g.us`)
  * DM: nomor telepon E.164 (mis. `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Hasil:** Ketika OpenClaw akan membalas di chat ini, OpenClaw akan menjalankan ketiga agen.

### Strategi pemrosesan

Kontrol cara agen memproses pesan:

### parallel (default)

Semua agen memproses secara bersamaan:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Agen memproses secara berurutan (satu menunggu yang sebelumnya selesai):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Contoh lengkap

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Cara kerjanya

### Alur pesan

* ### Pesan masuk tiba

Pesan grup WhatsApp atau DM tiba.

* ### Pemeriksaan broadcast

Sistem memeriksa apakah ID peer ada di `broadcast`.

* ### Jika ada dalam daftar broadcast

  * Semua agen yang tercantum memproses pesan.
  * Setiap agen memiliki kunci sesi dan konteks terisolasi sendiri.
  * Agen memproses secara paralel (default) atau berurutan.


* ### Jika tidak ada dalam daftar broadcast

Perutean normal berlaku (binding pertama yang cocok).

### Isolasi sesi

Setiap agen dalam grup broadcast mempertahankan hal-hal yang sepenuhnya terpisah:

  * **Kunci sesi** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Riwayat percakapan** (agen tidak melihat pesan agen lain)
  * **Workspace** (sandbox terpisah jika dikonfigurasi)
  * **Akses alat** (daftar izinkan/tolak yang berbeda)
  * **Memori/konteks** ([IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), dll. terpisah)
  * **Buffer konteks grup** (pesan grup terbaru yang digunakan untuk konteks) dibagikan per peer, sehingga semua agen broadcast melihat konteks yang sama saat dipicu


Ini memungkinkan setiap agen memiliki:

  * Kepribadian berbeda
  * Akses alat berbeda (mis., hanya-baca vs. baca-tulis)
  * Model berbeda (mis., opus vs. sonnet)
  * Skills berbeda yang terinstal


### Contoh: sesi terisolasi

Di grup `120363403215116621@g.us` dengan agen `["alfred", "baerbel"]`:

### Konteks Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Konteks Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Praktik terbaik

1\. Jaga agar agen tetap terfokus

Rancang setiap agen dengan satu tanggung jawab yang jelas:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Baik:** Setiap agen memiliki satu tugas. ❌ **Buruk:** Satu agen generik "dev-helper".

2\. Gunakan nama yang deskriptif

Buat jelas apa yang dilakukan setiap agen:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Konfigurasikan akses alat yang berbeda

Berikan agen hanya alat yang mereka perlukan:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` bersifat hanya-baca. `fixer` dapat membaca dan menulis.

4\. Pantau performa

Dengan banyak agen, pertimbangkan:

  * Menggunakan `"strategy": "parallel"` (default) untuk kecepatan
  * Membatasi grup broadcast hingga 5-10 agen
  * Menggunakan model yang lebih cepat untuk agen yang lebih sederhana

5\. Tangani kegagalan dengan baik

Agen gagal secara independen. Kesalahan satu agen tidak memblokir agen lain:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Kompatibilitas

### Penyedia

Grup broadcast saat ini berfungsi dengan:

  * ✅ WhatsApp (diimplementasikan)
  * 🚧 Telegram (direncanakan)
  * 🚧 Discord (direncanakan)
  * 🚧 Slack (direncanakan)


### Perutean

Grup broadcast bekerja bersama perutean yang sudah ada:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Hanya alfred yang merespons (perutean normal).
  * `GROUP_B`: agent1 DAN agent2 merespons (broadcast).


## Pemecahan masalah

Agen tidak merespons

**Periksa:**

  1. ID agen ada di `agents.list`.
  2. Format ID peer benar (mis., `120363403215116621@g.us`).
  3. Agen tidak ada dalam daftar tolak.


**Debug:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Hanya satu agen yang merespons

**Penyebab:** ID peer mungkin ada di `bindings` tetapi tidak di `broadcast`.

**Perbaikan:** Tambahkan ke konfigurasi broadcast atau hapus dari bindings.

Masalah performa

Jika lambat dengan banyak agen:

  * Kurangi jumlah agen per grup.
  * Gunakan model yang lebih ringan (sonnet alih-alih opus).
  * Periksa waktu startup sandbox.


## Contoh

Contoh 1: Tim peninjauan kode jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Pengguna mengirim:** Cuplikan kode.

**Respons:**

  * code-formatter: "Memperbaiki indentasi dan menambahkan petunjuk tipe"
  * security-scanner: "⚠️ Kerentanan injeksi SQL di baris 12"
  * test-coverage: "Cakupan 45%, kurang pengujian untuk kasus kesalahan"
  * docs-checker: "Docstring hilang untuk fungsi `process_data`"

Contoh 2: Dukungan multi-bahasa jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Referensi API

### Skema konfigurasi

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Bidang

Cara memproses agen. `parallel` menjalankan semua agen secara bersamaan; `sequential` menjalankannya sesuai urutan array.

JID grup WhatsApp, nomor E.164, atau ID peer lain. Nilainya adalah array ID agen yang harus memproses pesan.

## Batasan

  1. **Maks agen:** Tidak ada batas keras, tetapi 10+ agen mungkin lambat.
  2. **Konteks bersama:** Agen tidak melihat respons satu sama lain (sesuai desain).
  3. **Urutan pesan:** Respons paralel dapat tiba dalam urutan apa pun.
  4. **Batas laju:** Semua agen dihitung terhadap batas laju WhatsApp.


## Peningkatan mendatang

Fitur yang direncanakan:

  * [ ] Mode konteks bersama (agen melihat respons satu sama lain)
  * [ ] Koordinasi agen (agen dapat memberi sinyal satu sama lain)
  * [ ] Pemilihan agen dinamis (memilih agen berdasarkan konten pesan)
  * [ ] Prioritas agen (beberapa agen merespons sebelum yang lain)


## Terkait

  * [Perutean saluran](</id/channels/channel-routing>)
  * [Grup](</id/channels/groups>)
  * [Alat sandbox multi-agen](</id/tools/multi-agent-sandbox-tools>)
  * [Penyandingan](</id/channels/pairing>)
  * [Manajemen sesi](</id/concepts/session>)


Was this useful?YesNo