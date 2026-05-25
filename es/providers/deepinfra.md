---
title: DeepInfra
source_url: https://docs.openclaw.ai/es/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra proporciona una **API unificada** que enruta solicitudes a los modelos de código abierto y de frontera más populares detrás de un único endpoint y una clave de API. Es compatible con OpenAI, por lo que la mayoría de los SDK de OpenAI funcionan cambiando la URL base.

## Obtener una clave de API

  1. Ve a <https://deepinfra.com/>
  2. Inicia sesión o crea una cuenta
  3. Navega a Dashboard / Keys y genera una nueva clave de API o usa la creada automáticamente


## Configuración de CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

O configura la variable de entorno:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Fragmento de configuración

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Superficies de OpenClaw compatibles

El plugin incluido registra todas las superficies de DeepInfra que coinciden con los contratos actuales de proveedor de OpenClaw:

Superficie | Modelo predeterminado | Configuración/herramienta de OpenClaw  
---|---|---  
Chat / proveedor de modelo | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Generación/edición de imágenes | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Comprensión de medios | `moonshotai/Kimi-K2.5` para imágenes | comprensión de imágenes entrantes  
Voz a texto | `openai/whisper-large-v3-turbo` | transcripción de audio entrante  
Texto a voz | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Generación de video | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Embeddings de memoria | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra también expone reranking, clasificación, detección de objetos y otros tipos de modelos nativos. OpenClaw no tiene actualmente contratos de proveedor de primera clase para esas categorías, por lo que este plugin todavía no las registra.

## Modelos disponibles

OpenClaw descubre dinámicamente los modelos de DeepInfra disponibles al inicio. Usa `/models deepinfra` para ver la lista completa de modelos disponibles.

Cualquier modelo disponible en [DeepInfra.com](<https://deepinfra.com/>) se puede usar con el prefijo `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## Notas

  * Las referencias de modelo son `deepinfra/<provider>/<model>` (por ejemplo, `deepinfra/Qwen/Qwen3-Max`).
  * Modelo predeterminado: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * URL base: `https://api.deepinfra.com/v1/openai`
  * La generación de video nativa usa `https://api.deepinfra.com/v1/inference/<model>`.


## Relacionado

  * [Proveedores de modelos](</es/concepts/model-providers>)
  * [Todos los proveedores](</es/providers>)


Was this useful?YesNo