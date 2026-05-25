---
title: Mistral
source_url: https://docs.openclaw.ai/es/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw incluye un Plugin de Mistral integrado que registra cuatro contratos: completaciones de chat, comprensión multimedia (transcripción por lotes de Voxtral), STT en tiempo real para llamada de voz (Voxtral Realtime) e incrustaciones de memoria (`mistral-embed`).

Propiedad | Valor  
---|---  
Id. de proveedor | `mistral`  
Plugin | integrado, `enabledByDefault: true`  
Var. env. de autenticación | `MISTRAL_API_KEY`  
Marca de incorporación | `--auth-choice mistral-api-key`  
Marca directa de CLI | `--mistral-api-key <key>`  
API | compatible con OpenAI (`openai-completions`)  
URL base | `https://api.mistral.ai/v1`  
Modelo predeterminado | `mistral/mistral-large-latest`  
Modelo de incrustaciones | `mistral-embed`  
Lote de Voxtral | `voxtral-mini-latest` (transcripción de audio)  
Voxtral en tiempo real | `voxtral-mini-transcribe-realtime-2602`  
  
## Primeros pasos

* ### Obtén tu clave de API

Crea una clave de API en la [Consola de Mistral](<https://console.mistral.ai/>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Define un modelo predeterminado

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Catálogo de LLM integrado

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) es el modelo Medium combinado actual en el catálogo integrado: 128B de pesos densos, entrada de texto e imagen, contexto de 256K, llamadas a funciones, salida estructurada, programación y razonamiento ajustable mediante la API Chat Completions. Usa `mistral/mistral-medium-3-5` cuando quieras el modelo unificado más nuevo de Mistral para agentes y programación en lugar del predeterminado `mistral/mistral-large-latest`.

OpenClaw actualmente distribuye este catálogo de Mistral integrado:

Ref. de modelo | Entrada | Contexto | Salida máx. | Notas  
---|---|---|---|---  
`mistral/mistral-large-latest` | texto, imagen | 262,144 | 16,384 | Modelo predeterminado  
`mistral/mistral-medium-2508` | texto, imagen | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | texto, imagen | 262,144 | 8,192 | Mistral Medium 3.5; razonamiento ajustable  
`mistral/mistral-small-latest` | texto, imagen | 128,000 | 16,384 | Mistral Small 4; razonamiento ajustable mediante la API `reasoning_effort`  
`mistral/pixtral-large-latest` | texto, imagen | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | texto | 256,000 | 4,096 | Programación  
`mistral/devstral-medium-latest` | texto | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | texto | 128,000 | 40,000 | Con razonamiento habilitado  
  
Después de la incorporación, haz una prueba rápida de Medium 3.5 sin iniciar el Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Para explorar la fila del catálogo integrado antes de cambiar la configuración:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Transcripción de audio (Voxtral)

Usa Voxtral para la transcripción de audio por lotes mediante la canalización de comprensión multimedia.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT en streaming para llamada de voz

El Plugin `mistral` integrado registra Voxtral Realtime como proveedor de STT en streaming para llamada de voz.

Ajuste | Ruta de configuración | Predeterminado  
---|---|---  
Clave de API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Recurre a `MISTRAL_API_KEY`  
Modelo | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Codificación | `...mistral.encoding` | `pcm_mulaw`  
Frecuencia de muestreo | `...mistral.sampleRate` | `8000`  
Retardo objetivo | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Configuración avanzada

Razonamiento ajustable

`mistral/mistral-small-latest` (Mistral Small 4) y `mistral/mistral-medium-3-5` admiten [razonamiento ajustable](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) en la API Chat Completions mediante `reasoning_effort` (`none` minimiza el pensamiento extra en la salida; `high` muestra trazas completas de pensamiento antes de la respuesta final). Mistral recomienda `reasoning_effort="high"` para casos de uso de Medium 3.5 con agentes y código.

OpenClaw asigna el nivel de **thinking** de la sesión a la API de Mistral:

Nivel de thinking de OpenClaw | `reasoning_effort` de Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Configuración de ejemplo limitada al modelo para el razonamiento de Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Incrustaciones de memoria

Mistral puede servir incrustaciones de memoria mediante `/v1/embeddings` (modelo predeterminado: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Autenticación y URL base

  * La autenticación de Mistral usa `MISTRAL_API_KEY` (encabezado Bearer).
  * La URL base del proveedor usa por defecto `https://api.mistral.ai/v1` y acepta la forma de solicitud estándar de completaciones de chat compatible con OpenAI.
  * El modelo predeterminado de incorporación es `mistral/mistral-large-latest`.
  * Sobrescribe la URL base en `models.providers.mistral.baseUrl` solo cuando Mistral publique explícitamente un endpoint regional que necesites.


## Relacionado

[**Selección de modelo** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Comprensión multimedia** Configuración de transcripción de audio y selección de proveedor. ](</es/nodes/media-understanding>)

Was this useful?YesNo