---
title: Penyedia llama.cpp
source_url: https://docs.openclaw.ai/id/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` adalah plugin penyedia eksternal resmi untuk embedding GGUF lokal. Plugin ini memiliki dependensi runtime `node-llama-cpp` yang digunakan oleh `memorySearch.provider: "local"`.

Instal sebelum menggunakan embedding memori lokal:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Paket npm utama `openclaw` tidak menyertakan `node-llama-cpp`. Menyimpan dependensi native di plugin ini mencegah pembaruan npm OpenClaw biasa menghapus runtime yang diinstal secara manual di dalam direktori paket OpenClaw.

## Konfigurasi

Atur penyedia pencarian memori ke `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Model default adalah `embeddinggemma-300m-qat-Q8_0.gguf`. Anda juga dapat mengarahkan `local.modelPath` ke file `.gguf` lokal.

## Runtime Native

Gunakan Node 24 untuk jalur instalasi native yang paling lancar. Checkout sumber yang menggunakan pnpm mungkin perlu menyetujui dan membangun ulang dependensi native:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Untuk embedding lokal dengan gesekan lebih rendah, gunakan penyedia layanan lokal seperti Ollama atau LM Studio sebagai gantinya.

Was this useful?YesNo

Open issue