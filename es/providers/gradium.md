---
title: Gradium
source_url: https://docs.openclaw.ai/es/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) es un proveedor de texto a voz incluido para OpenClaw. El Plugin puede generar respuestas de audio normales (WAV), salida Opus compatible con notas de voz y audio u-law de 8 kHz para superficies de telefonía.

Propiedad | Valor  
---|---  
ID del proveedor | `gradium`  
Autenticación | `GRADIUM_API_KEY` o config `apiKey`  
URL base | `https://api.gradium.ai` (predeterminada)  
Voz predeterminada | `Emma` (`YTpq7expH9539ERJ`)  
  
## Configuración

Crea una clave de API de Gradium y luego exponla a OpenClaw con una variable de entorno o la clave de configuración.

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Config key

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

El Plugin comprueba primero la `apiKey` resuelta y recurre a la variable de entorno `GRADIUM_API_KEY`.

## Configuración

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Clave | Tipo | Descripción  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Clave de API resuelta. Admite `${ENV}` y referencias a secretos.  
`messages.tts.providers.gradium.baseUrl` | string | Sobrescribe el origen de la API. Las barras finales se eliminan. El valor predeterminado es `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | ID de voz predeterminado usado cuando no hay ninguna directiva de sobrescritura presente.  
  
El formato de audio de salida se selecciona automáticamente en tiempo de ejecución según la superficie de destino y no se puede configurar desde `openclaw.json`. Consulta Salida a continuación.

## Voces

Nombre | ID de voz  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Voz predeterminada: Emma.

### Sobrescritura de voz por mensaje

Cuando la política de habla activa permite sobrescrituras de voz, puedes cambiar de voz en línea usando un token de directiva. Todos estos se resuelven a la misma sobrescritura de `voiceId`:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Si la política de habla deshabilita las sobrescrituras de voz, la directiva se consume pero se ignora.

## Salida

El runtime elige el formato de salida a partir de la superficie de destino. Actualmente el proveedor no sintetiza otros formatos.

Destino | Formato | Ext. de archivo | Frecuencia de muestreo | Indicador compatible con voz  
---|---|---|---|---  
Audio estándar | `wav` | `.wav` | proveedor | no  
Nota de voz | `opus` | `.opus` | proveedor | sí  
Telefonía | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## Orden de selección automática

Entre los proveedores de TTS configurados, el orden de selección automática de Gradium es `30`. Consulta [Texto a voz](</es/tools/tts>) para saber cómo OpenClaw elige el proveedor activo cuando `messages.tts.provider` no está fijado.

## Relacionado

  * [Texto a voz](</es/tools/tts>)
  * [Descripción general de medios](</es/tools/media-overview>)


Was this useful?YesNo