---
title: ElevenLabs
source_url: https://docs.openclaw.ai/pt-BR/providers/elevenlabs
scraped_at: 2026-05-25
---

OpenClaw usa ElevenLabs para texto para fala, fala para texto em lote com Scribe v2 e STT por streaming com Scribe v2 Realtime.

Recurso | Superfície do OpenClaw | Padrão  
---|---|---  
Texto para fala | `messages.tts` / `talk` | `eleven_multilingual_v2`  
Fala para texto em lote | `tools.media.audio` | `scribe_v2`  
Fala para texto por streaming | streaming de Chamada de voz ou Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## Autenticação

Defina `ELEVENLABS_API_KEY` no ambiente. `XI_API_KEY` também é aceito para compatibilidade com ferramentas existentes da ElevenLabs.

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## Texto para fala

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

Defina `modelId` como `eleven_v3` para usar o TTS v3 da ElevenLabs. OpenClaw mantém `eleven_multilingual_v2` como padrão para instalações existentes.

Os canais de voz do Discord usam o endpoint de TTS por streaming da ElevenLabs quando a ElevenLabs é o provedor `voice.tts`/`messages.tts` selecionado. A reprodução começa a partir do stream de áudio retornado, em vez de esperar o OpenClaw baixar e gravar todo o arquivo de áudio primeiro. `latencyTier` é mapeado para o parâmetro de consulta `optimize_streaming_latency` da ElevenLabs para modelos que o aceitam; o OpenClaw omite esse parâmetro para `eleven_v3`, que o rejeita.

## Fala para texto

Use Scribe v2 para anexos de áudio recebidos e segmentos curtos de voz gravada:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw envia áudio multipart para `/v1/speech-to-text` da ElevenLabs com `model_id: "scribe_v2"`. Dicas de idioma são mapeadas para `language_code` quando presentes.

## STT por streaming

O Plugin `elevenlabs` incluído registra Scribe v2 Realtime para transcrição por streaming da Chamada de voz e do modo de agente do Google Meet.

Configuração | Caminho de configuração | Padrão  
---|---|---  
Chave de API | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | Recorre a `ELEVENLABS_API_KEY` / `XI_API_KEY`  
Modelo | `...elevenlabs.modelId` | `scribe_v2_realtime`  
Formato de áudio | `...elevenlabs.audioFormat` | `ulaw_8000`  
Taxa de amostragem | `...elevenlabs.sampleRate` | `8000`  
Estratégia de commit | `...elevenlabs.commitStrategy` | `vad`  
Idioma | `...elevenlabs.languageCode` | (não definido)  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

Para o modo de agente do Google Meet, defina `plugins.entries.google-meet.config.realtime.transcriptionProvider` como `"elevenlabs"` e configure o mesmo bloco de provedor em `plugins.entries.google-meet.config.realtime.providers.elevenlabs`.

## Relacionados

  * [Texto para fala](</pt-BR/tools/tts>)
  * [Google Meet](</pt-BR/plugins/google-meet>)
  * [Seleção de modelo](</pt-BR/concepts/model-providers>)


Was this useful?YesNo