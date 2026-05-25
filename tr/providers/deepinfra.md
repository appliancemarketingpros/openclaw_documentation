---
title: DeepInfra
source_url: https://docs.openclaw.ai/tr/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra, istekleri tek bir uç nokta ve API anahtarının arkasındaki en popüler açık kaynak ve öncü modellere yönlendiren **birleşik API** sağlar. OpenAI uyumludur, bu nedenle çoğu OpenAI SDK'sı temel URL değiştirilerek çalışır.

## API anahtarı alma

  1. <https://deepinfra.com/> adresine gidin
  2. Oturum açın veya bir hesap oluşturun
  3. Dashboard / Keys bölümüne gidin ve yeni bir API anahtarı oluşturun ya da otomatik oluşturulanı kullanın


## CLI kurulumu

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Veya ortam değişkenini ayarlayın:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Yapılandırma parçacığı

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Desteklenen OpenClaw yüzeyleri

Paketle gelen Plugin, güncel OpenClaw sağlayıcı sözleşmeleriyle eşleşen tüm DeepInfra yüzeylerini kaydeder:

Yüzey | Varsayılan model | OpenClaw yapılandırması/aracı  
---|---|---  
Sohbet / model sağlayıcısı | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Görsel oluşturma/düzenleme | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Medya anlama | görseller için `moonshotai/Kimi-K2.5` | gelen görsel anlama  
Konuşmadan metne | `openai/whisper-large-v3-turbo` | gelen ses transkripsiyonu  
Metinden konuşmaya | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Video oluşturma | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Bellek embedding'leri | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra ayrıca yeniden sıralama, sınıflandırma, nesne algılama ve diğer yerel model türlerini de sunar. OpenClaw şu anda bu kategoriler için birinci sınıf sağlayıcı sözleşmelerine sahip değildir, bu nedenle bu Plugin bunları henüz kaydetmez.

## Kullanılabilir modeller

OpenClaw, başlangıçta kullanılabilir DeepInfra modellerini dinamik olarak keşfeder. Kullanılabilir modellerin tam listesini görmek için `/models deepinfra` kullanın.

[DeepInfra.com](<https://deepinfra.com/>) üzerinde kullanılabilen herhangi bir model `deepinfra/` önekiyle kullanılabilir:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...ve daha fazlası
[/code]

## Notlar

  * Model referansları `deepinfra/<provider>/<model>` biçimindedir (örn. `deepinfra/Qwen/Qwen3-Max`).
  * Varsayılan model: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Temel URL: `https://api.deepinfra.com/v1/openai`
  * Yerel video oluşturma `https://api.deepinfra.com/v1/inference/<model>` kullanır.


## İlgili

  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Tüm sağlayıcılar](</tr/providers>)


Was this useful?YesNo