---
title: ds4
source_url: https://docs.openclaw.ai/id/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) menyajikan DeepSeek V4 Flash dari backend Metal lokal dengan API `/v1` yang kompatibel dengan OpenAI. OpenClaw terhubung ke ds4 melalui keluarga penyedia generik `openai-completions`.

ds4 bukan Plugin penyedia OpenClaw bawaan. Konfigurasikan di bawah `models.providers.ds4`, lalu pilih `ds4/deepseek-v4-flash`.

  * Id penyedia: `ds4`
  * Plugin: tidak ada
  * API: Chat Completions yang kompatibel dengan OpenAI (`openai-completions`)
  * URL dasar yang disarankan: `http://127.0.0.1:18000/v1`
  * Id model: `deepseek-v4-flash`
  * Panggilan alat: didukung melalui `tools` dan `tool_calls` bergaya OpenAI
  * Penalaran: `thinking` dan `reasoning_effort` bergaya DeepSeek


## Persyaratan

  * macOS dengan dukungan Metal.
  * Checkout ds4 yang berfungsi dengan `ds4-server` dan berkas GGUF DeepSeek V4 Flash.
  * Memori yang cukup untuk konteks yang Anda pilih. Nilai `--ctx` yang lebih besar mengalokasikan lebih banyak memori KV saat server dimulai.


## Mulai cepat

* ### Start ds4-server

Ganti `&lt;DS4_DIR&gt;` dengan path checkout ds4 Anda.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Respons harus menyertakan `deepseek-v4-flash`.

* ### Add the OpenClaw provider config

Tambahkan konfigurasi dari Konfigurasi lengkap, lalu jalankan pemeriksaan model sekali jalan:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Konfigurasi lengkap

Gunakan konfigurasi ini saat ds4 sudah berjalan di `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Jaga `contextWindow` tetap selaras dengan nilai `ds4-server --ctx`. Jaga `maxTokens` tetap selaras dengan `--tokens` kecuali Anda sengaja ingin OpenClaw meminta output yang lebih sedikit daripada default server.

## Startup sesuai kebutuhan

OpenClaw dapat memulai ds4 hanya saat model `ds4/...` dipilih. Tambahkan `localService` ke entri penyedia yang sama:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` harus berupa path executable absolut. Lookup shell dan ekspansi `~` tidak digunakan. Lihat [Layanan model lokal](</id/gateway/local-model-services>) untuk setiap kolom `localService`.

## Think Max

ds4 menerapkan Think Max hanya saat kedua kondisi benar:

  * `ds4-server` dimulai dengan `--ctx 393216` atau lebih tinggi.
  * Permintaan menggunakan `reasoning_effort: "max"` atau kolom upaya ds4 yang setara.


Jika Anda menjalankan konteks sebesar itu, perbarui flag server dan metadata model OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Uji

Mulai dengan pemeriksaan HTTP langsung:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Lalu uji perutean model OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Untuk smoke penuh agen dan panggilan alat, gunakan konteks setidaknya 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Hasil yang diharapkan:

  * `executionTrace.winnerProvider` adalah `ds4`
  * `executionTrace.winnerModel` adalah `deepseek-v4-flash`
  * `toolSummary.calls` setidaknya `1`
  * `finalAssistantVisibleText` dimulai dengan `tool-ok`


## Pemecahan masalah

curl /v1/models cannot connect

ds4 tidak berjalan atau tidak terikat ke host dan port dalam `baseUrl`. Mulai `ds4-server`, lalu coba lagi:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

`--ctx` yang dikonfigurasi terlalu kecil untuk giliran OpenClaw. Naikkan `ds4-server --ctx`, lalu perbarui `models.providers.ds4.models[].contextWindow` agar cocok. Giliran agen penuh dengan alat membutuhkan konteks yang jauh lebih banyak daripada permintaan curl langsung dengan satu pesan.

Think Max does not activate

ds4 hanya menggunakan Think Max saat `--ctx` setidaknya `393216` dan permintaan meminta `reasoning_effort: "max"`. Konteks yang lebih kecil kembali ke penalaran tinggi.

The first request is slow

ds4 memiliki fase residensi Metal dingin dan pemanasan model. Gunakan `localService.readyTimeoutMs: 300000` saat OpenClaw memulai server sesuai kebutuhan.

## Terkait

[**Local model services** Mulai server model lokal sesuai kebutuhan sebelum permintaan model. ](</id/gateway/local-model-services>) [**Local models** Pilih dan operasikan backend model lokal. ](</id/gateway/local-models>) [**Model providers** Konfigurasikan ref penyedia, auth, dan failover. ](</id/concepts/model-providers>) [**DeepSeek** Perilaku penyedia DeepSeek native dan kontrol thinking. ](</id/providers/deepseek>)

Was this useful?YesNo

Open issue