---
title: Deepgram
source_url: https://docs.openclaw.ai/es/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram es una API de conversión de voz a texto. En OpenClaw se usa para la transcripción de audio/notas de voz entrantes mediante `tools.media.audio` y para la STT en tiempo real de Voice Call mediante `plugins.entries.voice-call.config.streaming`.

Para la transcripción por lotes, OpenClaw sube el archivo de audio completo a Deepgram e inyecta la transcripción en el flujo de respuesta (`{{Transcript}}` \+ bloque `[Audio]`). Para la STT en tiempo real de Voice Call, OpenClaw reenvía tramas G.711 u-law en vivo a través del endpoint WebSocket `listen` de Deepgram y emite transcripciones parciales o finales a medida que Deepgram las devuelve.

Detalle | Valor  
---|---  
Sitio web | [deepgram.com](<https://deepgram.com>)  
Documentación | [developers.deepgram.com](<https://developers.deepgram.com>)  
Autenticación | `DEEPGRAM_API_KEY`  
Modelo predeterminado | `nova-3`  
  
## Primeros pasos

* ### Configura tu clave de API

Añade tu clave de API de Deepgram al entorno:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Habilita el proveedor de audio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Envía una nota de voz

Envía un mensaje de audio a través de cualquier canal conectado. OpenClaw lo transcribe mediante Deepgram e inyecta la transcripción en el flujo de respuesta.

## Opciones de configuración

Opción | Ruta | Descripción  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID del modelo de Deepgram (predeterminado: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Indicación de idioma (opcional)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Habilita la detección de idioma (opcional)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Habilita la puntuación (opcional)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Habilita el formateo inteligente (opcional)  
  
### Con indicación de idioma

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Con opciones de Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT en tiempo real de Voice Call

El Plugin `deepgram` incluido también registra un proveedor de transcripción en tiempo real para el Plugin Voice Call.

Configuración | Ruta de configuración | Predeterminado  
---|---|---  
Clave de API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Usa `DEEPGRAM_API_KEY` como respaldo  
Modelo | `...deepgram.model` | `nova-3`  
Idioma | `...deepgram.language` | (sin configurar)  
Codificación | `...deepgram.encoding` | `mulaw`  
Frecuencia de muestreo | `...deepgram.sampleRate` | `8000`  
Detección de fin de enunciado | `...deepgram.endpointingMs` | `800`  
Resultados provisionales | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Notas

Autenticación

La autenticación sigue el orden estándar de autenticación de proveedores. `DEEPGRAM_API_KEY` es la ruta más sencilla.

Proxy y endpoints personalizados

Sustituye los endpoints o encabezados con `tools.media.audio.baseUrl` y `tools.media.audio.headers` cuando uses un proxy.

Comportamiento de la salida

La salida sigue las mismas reglas de audio que otros proveedores (límites de tamaño, tiempos de espera, inyección de transcripción).

## Relacionado

[**Herramientas multimedia** Descripción general del flujo de procesamiento de audio, imágenes y video. ](</es/tools/media-overview>) [**Configuración** Referencia completa de configuración, incluida la de las herramientas multimedia. ](</es/gateway/configuration>) [**Resolución de problemas** Problemas comunes y pasos de depuración. ](</es/help/troubleshooting>) [**Preguntas frecuentes** Preguntas frecuentes sobre la configuración de OpenClaw. ](</es/help/faq>)

Was this useful?YesNo