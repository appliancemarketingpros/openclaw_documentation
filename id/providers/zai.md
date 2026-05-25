---
title: Z.AI
source_url: https://docs.openclaw.ai/id/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) adalah platform API untuk model **GLM**. Platform ini menyediakan API REST untuk GLM dan menggunakan kunci API untuk autentikasi. Buat kunci API Anda di konsol [Z.AI](<http://Z.AI>). OpenClaw menggunakan provider `zai` dengan kunci API [Z.AI](<http://Z.AI>).

  * Provider: `zai`
  * Autentikasi: `ZAI_API_KEY`
  * API: Chat Completions [Z.AI](<http://Z.AI>) (autentikasi Bearer)


## Memulai

### Auto-detect endpoint

**Paling cocok untuk:** sebagian besar pengguna. OpenClaw mendeteksi endpoint [Z.AI](<http://Z.AI>) yang sesuai dari kunci dan menerapkan URL dasar yang benar secara otomatis.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Explicit regional endpoint

**Paling cocok untuk:** pengguna yang ingin memaksa Coding Plan atau permukaan API umum tertentu.

* ### Pick the right onboarding choice

bashCopy code
[code]
    # Coding Plan Global (disarankan untuk pengguna Coding Plan)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (wilayah China)openclaw onboard --auth-choice zai-coding-cn # API umumopenclaw onboard --auth-choice zai-global # API umum CN (wilayah China)openclaw onboard --auth-choice zai-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Katalog bawaan

OpenClaw menyertakan katalog provider `zai` terpaket di manifest Plugin, sehingga pencantuman hanya-baca dapat menampilkan baris GLM yang dikenal tanpa memuat runtime provider:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Katalog berbasis manifest saat ini mencakup:

Ref model | Catatan  
---|---  
`zai/glm-5.1` | Model default  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Konfigurasi lanjutan

Forward-resolving unknown GLM-5 models

Id `glm-5*` yang tidak dikenal tetap di-resolve ke depan pada jalur provider terpaket dengan menyintesis metadata milik provider dari templat `glm-4.7` saat id tersebut cocok dengan bentuk keluarga GLM-5 saat ini.

Tool-call streaming

`tool_stream` diaktifkan secara default untuk streaming tool-call [Z.AI](<http://Z.AI>). Untuk menonaktifkannya:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking and preserved thinking

Thinking [Z.AI](<http://Z.AI>) mengikuti kontrol `/think` OpenClaw. Dengan thinking nonaktif, OpenClaw mengirim `thinking: { type: "disabled" }` untuk menghindari respons yang menghabiskan anggaran keluaran pada `reasoning_content` sebelum teks yang terlihat.

Thinking yang dipertahankan bersifat opt-in karena [Z.AI](<http://Z.AI>) mewajibkan seluruh riwayat `reasoning_content` diputar ulang, yang meningkatkan token prompt. Aktifkan per model:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Saat diaktifkan dan thinking aktif, OpenClaw mengirim `thinking: { type: "enabled", clear_thinking: false }` dan memutar ulang `reasoning_content` sebelumnya untuk transkrip kompatibel OpenAI yang sama.

Pengguna tingkat lanjut tetap dapat mengganti payload provider persisnya dengan `params.extra_body.thinking`.

Image understanding

Plugin [Z.AI](<http://Z.AI>) terpaket mendaftarkan pemahaman gambar.

Properti | Nilai  
---|---  
Model | `glm-4.6v`  
  
Pemahaman gambar di-resolve otomatis dari autentikasi [Z.AI](<http://Z.AI>) yang dikonfigurasi — tidak diperlukan konfigurasi tambahan.

Auth details

  * [Z.AI](<http://Z.AI>) menggunakan autentikasi Bearer dengan kunci API Anda.
  * Pilihan onboarding `zai-api-key` otomatis mendeteksi endpoint [Z.AI](<http://Z.AI>) yang sesuai dari prefiks kunci.
  * Gunakan pilihan regional eksplisit (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) saat Anda ingin memaksa permukaan API tertentu.


## Terkait

[**GLM model family** Ikhtisar keluarga model untuk GLM. ](</id/providers/glm>) [**Model selection** Memilih provider, ref model, dan perilaku failover. ](</id/concepts/model-providers>)

Was this useful?YesNo