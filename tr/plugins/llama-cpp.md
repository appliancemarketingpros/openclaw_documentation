---
title: llama.cpp Sağlayıcısı
source_url: https://docs.openclaw.ai/tr/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp`, yerel GGUF gömmeleri için resmi harici sağlayıcı Plugin'idir. `memorySearch.provider: "local"` tarafından kullanılan `node-llama-cpp` çalışma zamanı bağımlılığının sahibidir.

Yerel bellek gömmelerini kullanmadan önce yükleyin:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Ana `openclaw` npm paketi `node-llama-cpp` içermez. Yerel bağımlılığın bu Plugin içinde tutulması, normal OpenClaw npm güncellemelerinin OpenClaw paket dizini içinde elle yüklenmiş bir çalışma zamanını silmesini önler.

## Yapılandırma

Bellek arama sağlayıcısını `local` olarak ayarlayın:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Varsayılan model `embeddinggemma-300m-qat-Q8_0.gguf` şeklindedir. `local.modelPath` değerini yerel bir `.gguf` dosyasına da yönlendirebilirsiniz.

## Yerel Çalışma Zamanı

En sorunsuz yerel kurulum yolu için Node 24 kullanın. pnpm kullanan kaynak checkout'larının yerel bağımlılığı onaylaması ve yeniden derlemesi gerekebilir:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Daha az sorunlu yerel gömmeler için bunun yerine Ollama veya LM Studio gibi yerel bir hizmet sağlayıcısı kullanın.

Was this useful?YesNo

Open issue