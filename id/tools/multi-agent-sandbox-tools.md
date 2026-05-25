---
title: Sandbox dan alat multi-agent
source_url: https://docs.openclaw.ai/id/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Setiap agen dalam penyiapan multi-agen dapat menimpa kebijakan sandbox dan alat global. Halaman ini membahas konfigurasi per agen, aturan prioritas, dan contoh.

[**Sandboxing** Backend dan mode — referensi sandbox lengkap. ](</id/gateway/sandboxing>) [**Sandbox vs tool policy vs elevated** Debug "mengapa ini diblokir?" ](</id/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Elevated mode** Exec elevated untuk pengirim tepercaya. ](</id/tools/elevated>)

* * *

## Contoh konfigurasi

Example 1: Personal + restricted family agent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Hasil:**

  * Agen `main`: berjalan di host, akses alat penuh.
  * Agen `family`: berjalan di Docker (satu kontainer per agen), hanya pengiriman pesan `read` dan percakapan saat ini.

Example 2: Work agent with shared sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Example 2b: Global coding profile + messaging-only agent jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Hasil:**

  * agen default mendapatkan alat coding.
  * agen `support` hanya untuk perpesanan (+ alat Slack).

Example 3: Different sandbox modes per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Prioritas konfigurasi

Ketika konfigurasi global (`agents.defaults.*`) dan konfigurasi khusus agen (`agents.list[].*`) sama-sama ada:

### Konfigurasi sandbox

Pengaturan khusus agen menimpa global:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Pembatasan alat

Urutan pemfilterannya adalah:

* ### Tool profile

`tools.profile` atau `agents.list[].tools.profile`.

* ### Provider tool profile

`tools.byProvider[provider].profile` atau `agents.list[].tools.byProvider[provider].profile`.

* ### Global tool policy

`tools.allow` / `tools.deny`.

* ### Provider tool policy

`tools.byProvider[provider].allow/deny`.

* ### Agent-specific tool policy

`agents.list[].tools.allow/deny`.

* ### Agent provider policy

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Sandbox tool policy

`tools.sandbox.tools` atau `agents.list[].tools.sandbox.tools`.

* ### Subagent tool policy

`tools.subagents.tools`, jika berlaku.

Precedence rules

  * Setiap tingkat dapat semakin membatasi alat, tetapi tidak dapat mengaktifkan kembali alat yang telah ditolak dari tingkat sebelumnya.
  * Jika `agents.list[].tools.sandbox.tools` ditetapkan, nilai itu menggantikan `tools.sandbox.tools` untuk agen tersebut.
  * Jika `agents.list[].tools.profile` ditetapkan, nilai itu menimpa `tools.profile` untuk agen tersebut.
  * Kunci alat penyedia menerima `provider` (misalnya `google-antigravity`) atau `provider/model` (misalnya `openai/gpt-5.4`).

Empty allowlist behavior

Jika allowlist eksplisit apa pun dalam rantai tersebut membuat proses berjalan tanpa alat yang dapat dipanggil, OpenClaw berhenti sebelum mengirimkan prompt ke model. Ini disengaja: agen yang dikonfigurasi dengan alat yang hilang seperti `agents.list[].tools.allow: ["query_db"]` harus gagal dengan jelas sampai Plugin yang mendaftarkan `query_db` diaktifkan, bukan berlanjut sebagai agen teks saja.

Kebijakan alat mendukung singkatan `group:*` yang diperluas menjadi beberapa alat. Lihat [Grup alat](</id/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) untuk daftar lengkapnya.

Timpa elevated per agen (`agents.list[].tools.elevated`) dapat semakin membatasi exec elevated untuk agen tertentu. Lihat [Mode elevated](</id/tools/elevated>) untuk detail.

* * *

## Migrasi dari agen tunggal

### Sebelum (agen tunggal)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Sesudah (multi-agen)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Contoh pembatasan alat

### Agen hanya-baca

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Eksekusi shell dengan alat sistem file dinonaktifkan

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Hanya komunikasi

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` dalam profil ini tetap mengembalikan tampilan ingatan yang terbatas dan telah disanitasi, bukan dump transkrip mentah. Ingatan asisten menghapus tag berpikir, scaffolding `<relevant-memories>`, payload XML pemanggilan alat teks biasa (termasuk `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>`, dan blok pemanggilan alat yang terpotong), scaffolding pemanggilan alat yang diturunkan, token kontrol model ASCII/lebar-penuh yang bocor, dan XML pemanggilan alat MiniMax yang tidak valid sebelum redaksi/pemotongan.

* * *

## Kekeliruan umum: "non-main"

* * *

## Pengujian

Setelah mengonfigurasi sandbox dan alat multi-agen:

* ### Periksa resolusi agen

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verifikasi kontainer sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Uji pembatasan alat

  * Kirim pesan yang memerlukan alat terbatas.
  * Verifikasi bahwa agen tidak dapat menggunakan alat yang ditolak.


* ### Pantau log

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Pemecahan masalah

Agen tidak disandbox meskipun `mode: 'all'`

  * Periksa apakah ada `agents.defaults.sandbox.mode` global yang menimpanya.
  * Konfigurasi khusus agen memiliki prioritas, jadi atur `agents.list[].sandbox.mode: "all"`.

Alat masih tersedia meskipun ada daftar penolakan

  * Periksa urutan pemfilteran alat: global → agen → sandbox → subagen.
  * Setiap tingkat hanya dapat membatasi lebih lanjut, bukan memberikan kembali.
  * Verifikasi dengan log: `[tools] filtering tools for agent:${agentId}`.

Kontainer tidak diisolasi per agen

  * Atur `scope: "agent"` dalam konfigurasi sandbox khusus agen.
  * Default-nya adalah `"session"` yang membuat satu kontainer per sesi.


* * *

## Terkait

  * [Mode elevated](</id/tools/elevated>)
  * [Perutean multi-agent](</id/concepts/multi-agent>)
  * [Konfigurasi sandbox](</id/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox vs kebijakan alat vs elevated](</id/gateway/sandbox-vs-tool-policy-vs-elevated>) — men-debug "mengapa ini diblokir?"
  * [Sandboxing](</id/gateway/sandboxing>) — referensi sandbox lengkap (mode, cakupan, backend, image)
  * [Manajemen sesi](</id/concepts/session>)


Was this useful?YesNo