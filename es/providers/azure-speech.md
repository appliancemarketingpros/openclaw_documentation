---
title: Azure Speech
source_url: https://docs.openclaw.ai/es/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech es un proveedor de texto a voz de Azure AI Speech. En OpenClaw sintetiza audio saliente de respuestas como MP3 por defecto, Ogg/Opus nativo para notas de voz y audio mulaw de 8 kHz para canales de telefonía como Voice Call.

OpenClaw usa directamente la API REST de Azure Speech con SSML y envía el formato de salida propiedad del proveedor mediante `X-Microsoft-OutputFormat`.

Detalle | Valor  
---|---  
Sitio web | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Docs | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Autenticación | `AZURE_SPEECH_KEY` más `AZURE_SPEECH_REGION`  
Voz predeterminada | `en-US-JennyNeural`  
Salida de archivo predeterminada | `audio-24khz-48kbitrate-mono-mp3`  
Archivo predeterminado de nota de voz | `ogg-24khz-16bit-mono-opus`  
  
## Primeros pasos

* ### Crear un recurso de Azure Speech

En el portal de Azure, crea un recurso Speech. Copia **KEY 1** desde Resource Management > Keys and Endpoint, y copia la ubicación del recurso, por ejemplo `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Seleccionar Azure Speech en messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Enviar un mensaje

Envía una respuesta a través de cualquier canal conectado. OpenClaw sintetiza el audio con Azure Speech y entrega MP3 para audio estándar, u Ogg/Opus cuando el canal espera una nota de voz.

## Opciones de configuración

Opción | Ruta | Descripción  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Clave del recurso Azure Speech. Usa como respaldo `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` o `SPEECH_KEY`.  
`region` | `messages.tts.providers.azure-speech.region` | Región del recurso Azure Speech. Usa como respaldo `AZURE_SPEECH_REGION` o `SPEECH_REGION`.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Sobrescritura opcional del endpoint/base URL de Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Sobrescritura opcional de la base URL de Azure Speech.  
`voice` | `messages.tts.providers.azure-speech.voice` | ShortName de la voz de Azure (predeterminado `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | Código de idioma SSML (predeterminado `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Formato de salida de archivo de audio (predeterminado `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Formato de salida de nota de voz (predeterminado `ogg-24khz-16bit-mono-opus`).  
  
## Notas

Autenticación

Azure Speech usa una clave de recurso Speech, no una clave de Azure OpenAI. La clave se envía como `Ocp-Apim-Subscription-Key`; OpenClaw deriva `https://<region>.tts.speech.microsoft.com` a partir de `region` salvo que proporciones `endpoint` o `baseUrl`.

Nombres de voz

Usa el valor `ShortName` de la voz de Azure Speech, por ejemplo `en-US-JennyNeural`. El proveedor incluido puede listar voces a través del mismo recurso Speech y filtra las voces marcadas como desaprobadas o retiradas.

Salidas de audio

Azure acepta formatos de salida como `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` y `riff-24khz-16bit-mono-pcm`. OpenClaw solicita Ogg/Opus para destinos `voice-note` para que los canales puedan enviar burbujas de voz nativas sin una conversión adicional desde MP3.

Alias

`azure` se acepta como alias de proveedor para PR existentes y configuración de usuario, pero la configuración nueva debe usar `azure-speech` para evitar confusión con los providers de modelos de Azure OpenAI.

## Relacionado

[**Texto a voz** Resumen de TTS, proveedores y configuración `messages.tts`. ](</es/tools/tts>) [**Configuración** Referencia completa de configuración, incluida `messages.tts`. ](</es/gateway/configuration>) [**Providers** Todos los providers incluidos de OpenClaw. ](</es/providers>) [**Solución de problemas** Problemas comunes y pasos de depuración. ](</es/help/troubleshooting>)

Was this useful?YesNo