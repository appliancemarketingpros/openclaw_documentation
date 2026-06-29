---
title: Cohere
source_url: https://docs.openclaw.ai/id/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) menyediakan inferensi yang kompatibel dengan OpenAI melalui Compatibility API-nya. OpenClaw menyertakan penyedia Cohere selama transisi eksternalisasinya dan juga menerbitkannya sebagai plugin eksternal resmi dengan katalog model Command A.

Properti | Nilai  
---|---  
ID penyedia | `cohere`  
Plugin | dibundel selama transisi; paket eksternal resmi  
Variabel env auth | `COHERE_API_KEY`  
Flag orientasi awal | `--auth-choice cohere-api-key`  
Flag CLI langsung | `--cohere-api-key <key>`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.cohere.ai/compatibility/v1`  
Model default | `cohere/command-a-03-2025`  
  
## Mulai

  1. Cohere disertakan dalam paket OpenClaw saat ini. Jika tidak tersedia, instal paket eksternal dan mulai ulang Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Buat kunci API Cohere.
  3. Jalankan orientasi awal:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Konfirmasi bahwa katalog tersedia:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Model default hanya ditetapkan jika belum ada model utama yang dikonfigurasi.

## Penyiapan hanya lingkungan

Buat `COHERE_API_KEY` tersedia untuk proses Gateway, lalu pilih model Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Terkait

  * [Penyedia model](</id/concepts/model-providers>)
  * [CLI model](</id/cli/models>)
  * [Direktori penyedia](</id/providers>)


Was this useful?YesNo

Open issue