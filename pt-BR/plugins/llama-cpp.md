---
title: Provedor llama.cpp
source_url: https://docs.openclaw.ai/pt-BR/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` é o Plugin provedor externo oficial para embeddings GGUF locais. Ele possui a dependência de runtime `node-llama-cpp` usada por `memorySearch.provider: "local"`.

Instale-o antes de usar embeddings de memória locais:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

O pacote npm principal `openclaw` não inclui `node-llama-cpp`. Manter a dependência nativa neste Plugin impede que atualizações npm normais do OpenClaw excluam um runtime instalado manualmente dentro do diretório do pacote OpenClaw.

## Configuração

Defina o provedor de busca de memória como `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

O modelo padrão é `embeddinggemma-300m-qat-Q8_0.gguf`. Você também pode apontar `local.modelPath` para um arquivo `.gguf` local.

## Runtime Nativo

Use Node 24 para o caminho de instalação nativa mais tranquilo. Checkouts de código-fonte usando pnpm podem precisar aprovar e reconstruir a dependência nativa:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Para embeddings locais com menos atrito, use um provedor de serviço local, como Ollama ou LM Studio.

Was this useful?YesNo

Open issue