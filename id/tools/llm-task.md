---
title: Tugas LLM
source_url: https://docs.openclaw.ai/id/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` adalah **alat Plugin opsional** yang menjalankan tugas LLM khusus JSON dan mengembalikan output terstruktur (opsional divalidasi terhadap JSON Schema).

Ini ideal untuk mesin alur kerja seperti Lobster: Anda dapat menambahkan satu langkah LLM tanpa menulis kode OpenClaw khusus untuk setiap alur kerja.

## Aktifkan Plugin

  1. Aktifkan Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Izinkan alat opsional:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Gunakan `tools.allow` hanya ketika Anda menginginkan mode allowlist yang restriktif.

## Konfigurasi (opsional)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` adalah allowlist string `provider/model`. Jika diatur, setiap permintaan di luar daftar akan ditolak.

## Parameter alat

  * `prompt` (string, wajib)
  * `input` (apa pun, opsional)
  * `schema` (objek, JSON Schema opsional)
  * `provider` (string, opsional)
  * `model` (string, opsional)
  * `thinking` (string, opsional)
  * `authProfileId` (string, opsional)
  * `temperature` (angka, opsional)
  * `maxTokens` (angka, opsional)
  * `timeoutMs` (angka, opsional)


`thinking` menerima preset penalaran OpenClaw standar, seperti `low` atau `medium`.

## Output

Mengembalikan `details.json` yang berisi JSON yang telah diurai (dan memvalidasinya terhadap `schema` jika disediakan).

## Contoh: langkah alur kerja Lobster

### Batasan penting

Contoh di bawah mengasumsikan **CLI Lobster mandiri** berjalan di lingkungan tempat `openclaw.invoke` sudah memiliki URL Gateway/konteks autentikasi yang benar.

Untuk runner Lobster **tersemat** yang dibundel di dalam OpenClaw, pola CLI bersarang ini **saat ini belum andal** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Sampai Lobster tersemat memiliki bridge yang didukung untuk alur ini, sebaiknya gunakan salah satu dari:

  * panggilan alat `llm-task` langsung di luar Lobster, atau
  * langkah Lobster yang tidak bergantung pada panggilan `openclaw.invoke` bersarang.


Contoh CLI Lobster mandiri:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Catatan keamanan

  * Alat ini **khusus JSON** dan menginstruksikan model untuk hanya menghasilkan JSON (tanpa code fence, tanpa komentar).
  * Tidak ada alat yang diekspos ke model untuk eksekusi ini.
  * Perlakukan output sebagai tidak tepercaya kecuali Anda memvalidasinya dengan `schema`.
  * Letakkan persetujuan sebelum langkah apa pun yang memiliki efek samping (kirim, posting, exec).


## Terkait

  * [Tingkat thinking](</id/tools/thinking>)
  * [Sub-agen](</id/tools/subagents>)
  * [Perintah slash](</id/tools/slash-commands>)


Was this useful?YesNo