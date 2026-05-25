---
title: NVIDIA
source_url: https://docs.openclaw.ai/id/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA menyediakan API yang kompatibel dengan OpenAI di `https://integrate.api.nvidia.com/v1` untuk model terbuka secara gratis. Autentikasikan dengan kunci API dari [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Memulai

* ### Dapatkan kunci API Anda

Buat kunci API di [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Ekspor kunci dan jalankan onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Atur model NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Untuk penyiapan noninteraktif, Anda juga dapat meneruskan kunci secara langsung:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Contoh konfigurasi

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Katalog bawaan

Ref model | Nama | Konteks | Output maks  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Konfigurasi lanjutan

Perilaku aktif otomatis

Provider aktif otomatis ketika variabel lingkungan `NVIDIA_API_KEY` ditetapkan. Tidak diperlukan konfigurasi provider eksplisit selain kunci tersebut.

Katalog dan harga

Katalog yang dibundel bersifat statis. Biaya secara default bernilai `0` dalam sumber karena NVIDIA saat ini menawarkan akses API gratis untuk model yang tercantum.

Endpoint yang kompatibel dengan OpenAI

NVIDIA menggunakan endpoint completions `/v1` standar. Tooling apa pun yang kompatibel dengan OpenAI seharusnya langsung berfungsi dengan URL dasar NVIDIA.

Respons provider kustom yang lambat

Beberapa model kustom yang di-hosting NVIDIA dapat memerlukan waktu lebih lama daripada watchdog idle model default sebelum memancarkan potongan respons pertama. Untuk entri provider NVIDIA kustom, naikkan timeout provider alih-alih menaikkan timeout runtime seluruh agent:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Terkait

[**Pemilihan model** Memilih provider, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Referensi konfigurasi lengkap untuk agent, model, dan provider. ](</id/gateway/configuration-reference>)

Was this useful?YesNo