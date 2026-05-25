---
title: Hugging Face (inference)
source_url: https://docs.openclaw.ai/id/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) menawarkan chat completions yang kompatibel dengan OpenAI melalui satu API router. Anda mendapatkan akses ke banyak model (DeepSeek, Llama, dan lainnya) dengan satu token. OpenClaw menggunakan **endpoint yang kompatibel dengan OpenAI** (khusus chat completions); untuk text-to-image, embedding, atau speech gunakan [klien inferensi HF](<https://huggingface.co/docs/api-inference/quicktour>) secara langsung.

  * Provider: `huggingface`
  * Auth: `HUGGINGFACE_HUB_TOKEN` atau `HF_TOKEN` (token fine-grained dengan izin **Make calls to Inference Providers**)
  * API: kompatibel dengan OpenAI (`https://router.huggingface.co/v1`)
  * Billing: Satu token HF; [harga](<https://huggingface.co/docs/inference-providers/pricing>) mengikuti tarif provider dengan tier gratis.


## Memulai

* ### Buat token fine-grained

Buka [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) lalu buat token fine-grained baru.

* ### Jalankan onboarding

Pilih **Hugging Face** di dropdown provider, lalu masukkan API key Anda saat diminta:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Pilih model default

Di dropdown **Default Hugging Face model** , pilih model yang Anda inginkan. Daftar ini dimuat dari Inference API saat Anda memiliki token yang valid; jika tidak, daftar bawaan akan ditampilkan. Pilihan Anda disimpan sebagai model default.

Anda juga dapat mengatur atau mengubah model default nanti di config:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Penyiapan non-interaktif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Ini akan mengatur `huggingface/deepseek-ai/DeepSeek-R1` sebagai model default.

## ID model

Ref model menggunakan bentuk `huggingface/<org>/<model>` (ID gaya Hub). Daftar di bawah ini berasal dari **GET** `https://router.huggingface.co/v1/models`; katalog Anda mungkin mencakup lebih banyak.

Model | Ref (awali dengan `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Konfigurasi lanjutan

Discovery model dan dropdown onboarding

OpenClaw menemukan model dengan memanggil **endpoint Inference secara langsung** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Opsional: kirim `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` atau `$HF_TOKEN` untuk daftar lengkap; beberapa endpoint mengembalikan subset tanpa auth.) Responsnya bergaya OpenAI `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Saat Anda mengonfigurasi API key Hugging Face (melalui onboarding, `HUGGINGFACE_HUB_TOKEN`, atau `HF_TOKEN`), OpenClaw menggunakan GET ini untuk menemukan model chat-completion yang tersedia. Selama **penyiapan interaktif** , setelah Anda memasukkan token, Anda akan melihat dropdown **Default Hugging Face model** yang diisi dari daftar itu (atau katalog bawaan jika permintaan gagal). Saat runtime (misalnya startup Gateway), ketika ada key, OpenClaw kembali memanggil **GET** `https://router.huggingface.co/v1/models` untuk menyegarkan katalog. Daftar ini digabungkan dengan katalog bawaan (untuk metadata seperti jendela konteks dan biaya). Jika permintaan gagal atau tidak ada key yang diatur, hanya katalog bawaan yang digunakan.

Nama model, alias, dan sufiks kebijakan

  * **Nama dari API:** Nama tampilan model **diisi dari GET /v1/models** saat API mengembalikan `name`, `title`, atau `display_name`; jika tidak, nama itu diturunkan dari ID model (misalnya `deepseek-ai/DeepSeek-R1` menjadi "DeepSeek R1").
  * **Ganti nama tampilan:** Anda dapat mengatur label kustom per model di config sehingga model tersebut muncul sesuai keinginan Anda di CLI dan UI:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Sufiks kebijakan:** Dokumentasi dan helper Hugging Face bawaan OpenClaw saat ini memperlakukan dua sufiks ini sebagai varian kebijakan bawaan:

    * **`:fastest`** — throughput tertinggi.
    * **`:cheapest`** — biaya per token output terendah.

Anda dapat menambahkan ini sebagai entri terpisah di `models.providers.huggingface.models` atau mengatur `model.primary` dengan sufiks tersebut. Anda juga dapat mengatur urutan provider default Anda di [Inference Provider settings](<https://hf.co/settings/inference-providers>) (tanpa sufiks = gunakan urutan itu).

  * **Penggabungan config:** Entri yang ada di `models.providers.huggingface.models` (misalnya di `models.json`) dipertahankan saat config digabungkan. Jadi `name`, `alias`, atau opsi model kustom yang Anda atur di sana akan tetap dipertahankan.


Environment dan penyiapan daemon

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `HUGGINGFACE_HUB_TOKEN` atau `HF_TOKEN` tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

Config: DeepSeek R1 dengan fallback Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Config: Qwen dengan varian cheapest dan fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Config: DeepSeek + Llama + GPT-OSS dengan alias json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Config: Banyak Qwen dan DeepSeek dengan sufiks kebijakan json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Terkait

[**Pemilihan model** Ikhtisar semua provider, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pemilihan model** Cara memilih dan mengonfigurasi model. ](</id/concepts/models>) [**Dokumentasi Inference Providers** Dokumentasi resmi Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Konfigurasi** Referensi config lengkap. ](</id/gateway/configuration>)

Was this useful?YesNo