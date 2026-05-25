---
title: Inworld
source_url: https://docs.openclaw.ai/es/providers/inworld
scraped_at: 2026-05-25
---

Inworld es un proveedor de texto a voz (TTS) en streaming. En OpenClaw sintetiza audio de respuesta saliente (MP3 de forma predeterminada, OGG_OPUS para notas de voz) y audio PCM para canales de telefonía como Voice Call.

OpenClaw publica en el endpoint de TTS en streaming de Inworld, concatena los fragmentos de audio base64 devueltos en un único búfer y pasa el resultado al pipeline estándar de audio de respuesta.

Propiedad | Valor  
---|---  
ID del proveedor | `inworld`  
Plugin | incluido, `enabledByDefault: true`  
Contrato | `speechProviders` (solo TTS)  
Variable de entorno de autenticación | `INWORLD_API_KEY` (HTTP Basic, credencial Base64 del panel)  
URL base | `https://api.inworld.ai`  
Voz predeterminada | `Sarah`  
Modelo predeterminado | `inworld-tts-1.5-max`  
Salida | MP3 (predeterminado), OGG_OPUS (notas de voz), PCM 22050 Hz (telefonía)  
Sitio web | [inworld.ai](<https://inworld.ai>)  
Documentación | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Primeros pasos

* ### Configura tu clave de API

Copia la credencial desde tu panel de Inworld (Workspace > API Keys) y configúrala como una variable de entorno. El valor se envía literalmente como la credencial HTTP Basic, así que no vuelvas a codificarlo en Base64 ni lo conviertas en un token bearer.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Selecciona Inworld en messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Envía un mensaje

Envía una respuesta a través de cualquier canal conectado. OpenClaw sintetiza el audio con Inworld y lo entrega como MP3 (u OGG_OPUS cuando el canal espera una nota de voz).

## Opciones de configuración

Opción | Ruta | Descripción  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Credencial Base64 del panel. Recurre a `INWORLD_API_KEY` si no está configurada.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Sobrescribe la URL base de la API de Inworld (predeterminada `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Identificador de voz (predeterminado `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | ID del modelo TTS (predeterminado `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Temperatura de muestreo `0..2` (opcional).  
  
## Notas

Autenticación

Inworld usa autenticación HTTP Basic con una única cadena de credencial codificada en Base64. Cópiala literalmente desde el panel de Inworld. El proveedor la envía como `Authorization: Basic <apiKey>` sin ninguna codificación adicional, así que no la codifiques en Base64 tú mismo y no pases un token de estilo bearer. Consulta [notas de autenticación de TTS](</es/tools/tts#inworld-primary>) para ver el mismo aviso.

Modelos

IDs de modelo admitidos: `inworld-tts-1.5-max` (predeterminado), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Salidas de audio

Las respuestas usan MP3 de forma predeterminada. Cuando el destino del canal es `voice-note`, OpenClaw solicita a Inworld `OGG_OPUS` para que el audio se reproduzca como una burbuja de voz nativa. La síntesis de telefonía usa `PCM` sin procesar a 22050 Hz para alimentar el puente de telefonía.

Endpoints personalizados

Sobrescribe el host de la API con `messages.tts.providers.inworld.baseUrl`. Las barras finales se eliminan antes de enviar las solicitudes.

## Relacionado

[**Texto a voz** Resumen de TTS, proveedores y configuración de `messages.tts`. ](</es/tools/tts>) [**Configuración** Referencia completa de configuración, incluidos los ajustes de `messages.tts`. ](</es/gateway/configuration>) [**Proveedores** Todos los proveedores incluidos de OpenClaw. ](</es/providers>) [**Solución de problemas** Problemas comunes y pasos de depuración. ](</es/help/troubleshooting>)

Was this useful?YesNo