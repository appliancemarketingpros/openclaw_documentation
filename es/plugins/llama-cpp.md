---
title: Proveedor llama.cpp
source_url: https://docs.openclaw.ai/es/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` es el plugin proveedor externo oficial para embeddings GGUF locales. Es propietario de la dependencia de runtime `node-llama-cpp` usada por `memorySearch.provider: "local"`.

Instálalo antes de usar embeddings de memoria local:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

El paquete npm principal `openclaw` no incluye `node-llama-cpp`. Mantener la dependencia nativa en este plugin evita que las actualizaciones npm normales de OpenClaw eliminen un runtime instalado manualmente dentro del directorio del paquete OpenClaw.

## Configuración

Define el proveedor de búsqueda de memoria como `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

El modelo predeterminado es `embeddinggemma-300m-qat-Q8_0.gguf`. También puedes apuntar `local.modelPath` a un archivo `.gguf` local.

## Runtime nativo

Usa Node 24 para la ruta de instalación nativa más fluida. Los checkouts de código fuente que usan pnpm pueden necesitar aprobar y reconstruir la dependencia nativa:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Para embeddings locales con menos fricción, usa en su lugar un proveedor de servicio local como Ollama o LM Studio.

Was this useful?YesNo

Open issue