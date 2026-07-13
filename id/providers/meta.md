---
title: Meta
source_url: https://docs.openclaw.ai/id/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** menggunakan **Responses API** yang kompatibel dengan OpenAI (`POST /v1/responses`) untuk model penalaran `muse-spark-1.1`. Penyedia ini disertakan sebagai plugin OpenClaw bawaan.

Properti | Nilai  
---|---  
ID penyedia | `meta`  
Plugin | penyedia bawaan  
Variabel lingkungan autentikasi | `MODEL_API_KEY`  
Flag orientasi awal | `--auth-choice meta-api-key`  
Flag CLI langsung | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
URL dasar | `https://api.meta.ai/v1`  
Model default | `meta/muse-spark-1.1`  
Penalaran default | `high` (`reasoning.effort`)  
  
## Memulai

* ### Tetapkan kunci API

Orientasi awalCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Flag langsungCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Hanya variabel lingkunganCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Menampilkan entri katalog statis `muse-spark-1.1`. Jika `MODEL_API_KEY` tidak dapat ditemukan, `openclaw models status --json` melaporkan kredensial yang tidak tersedia di bawah `auth.unusableProfiles`.

## Penyiapan noninteraktif

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Katalog bawaan

Referensi model | Nama | Penalaran | Jendela konteks | Keluaran maks.  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | ya | 1,048,576 | 131,072  
  
Kemampuan:

  * Masukan teks + gambar
  * Pemanggilan alat dan streaming
  * Tingkat upaya penalaran: `minimal`, `low`, `medium`, `high`, `xhigh` (default: `high`)
  * Pemutaran ulang penalaran terenkripsi tanpa status (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Konfigurasi manual

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Uji cepat

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Pengujian langsung menggunakan `muse-spark-1.1` terhadap `POST /v1/responses`.

## Terkait

[**Penyedia model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Mode berpikir** Tingkat upaya penalaran untuk muse-spark-1.1. ](</id/tools/thinking>) [**Referensi konfigurasi** Default agen dan konfigurasi model. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue