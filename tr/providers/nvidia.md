---
title: NVIDIA
source_url: https://docs.openclaw.ai/tr/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA, açık modeller için ücretsiz olarak `https://integrate.api.nvidia.com/v1` adresinde OpenAI uyumlu bir API sağlar. [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) üzerinden alınan bir API anahtarıyla kimlik doğrulaması yapın.

## Başlarken

* ### Get your API key

[build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) adresinde bir API anahtarı oluşturun.

* ### Export the key and run onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Set an NVIDIA model

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Etkileşimsiz kurulum için anahtarı doğrudan da geçirebilirsiniz:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Yerleşik katalog

Model ref | Ad | Bağlam | Maksimum çıktı  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Gelişmiş yapılandırma

Auto-enable behavior

Sağlayıcı, `NVIDIA_API_KEY` ortam değişkeni ayarlandığında otomatik etkinleşir. Anahtar dışında açık bir sağlayıcı yapılandırması gerekmez.

Catalog and pricing

Paketlenmiş katalog statiktir. NVIDIA listelenen modeller için şu anda ücretsiz API erişimi sunduğundan, maliyetler kaynakta varsayılan olarak `0` olur.

OpenAI-compatible endpoint

NVIDIA standart `/v1` tamamlama uç noktasını kullanır. OpenAI uyumlu herhangi bir araç, NVIDIA temel URL'siyle kutudan çıktığı gibi çalışmalıdır.

Slow custom provider responses

NVIDIA üzerinde barındırılan bazı özel modeller, ilk yanıt parçasını yaymadan önce varsayılan model boşta kalma watchdog süresinden daha uzun sürebilir. Özel NVIDIA sağlayıcı girdileri için, tüm agent çalışma zamanı zaman aşımını artırmak yerine sağlayıcı zaman aşımını yükseltin:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## İlgili

[**Model selection** Sağlayıcıları, model ref değerlerini ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**Configuration reference** Agent, modeller ve sağlayıcılar için tam yapılandırma referansı. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo