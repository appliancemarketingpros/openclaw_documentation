---
title: SenseAudio
source_url: https://docs.openclaw.ai/es/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio puede transcribir adjuntos de audio entrante y notas de voz mediante la canalización compartida `tools.media.audio` de OpenClaw. OpenClaw publica audio multiparte en el endpoint de transcripción compatible con OpenAI e inyecta el texto devuelto como `{{Transcript}}` más un bloque `[Audio]`.

Propiedad | Valor  
---|---  
Id. del proveedor | `senseaudio`  
Plugin | incluido, `enabledByDefault: true`  
Contrato | `mediaUnderstandingProviders` (audio)  
Variable de entorno de autenticación | `SENSEAUDIO_API_KEY`  
Modelo predeterminado | `senseaudio-asr-pro-1.5-260319`  
URL predeterminada | `https://api.senseaudio.cn/v1`  
Sitio web | [senseaudio.cn](<https://senseaudio.cn>)  
Documentación | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Primeros pasos

* ### Set your API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Send a voice note

Envía un mensaje de audio a través de cualquier canal conectado. OpenClaw sube el audio a SenseAudio y usa la transcripción en la canalización de respuesta.

## Opciones

Opción | Ruta | Descripción  
---|---|---  
`model` | `tools.media.audio.models[].model` | Id. del modelo ASR de SenseAudio  
`language` | `tools.media.audio.models[].language` | Indicio de idioma opcional  
`prompt` | `tools.media.audio.prompt` | Prompt de transcripción opcional  
`baseUrl` | `tools.media.audio.baseUrl` o modelo | Sobrescribe la base compatible con OpenAI  
`headers` | `tools.media.audio.request.headers` | Encabezados de solicitud adicionales  
  
## Relacionado

  * [Comprensión de medios (audio)](</es/nodes/audio>)
  * [Proveedores de modelos](</es/concepts/model-providers>)


Was this useful?YesNo