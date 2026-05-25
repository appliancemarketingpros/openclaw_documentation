---
title: Deepgram
source_url: https://docs.openclaw.ai/pt-BR/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram é uma API de speech-to-text. No OpenClaw, ela é usada para transcrição de áudio/notas de voz de entrada por meio de `tools.media.audio` e para STT em streaming do Voice Call por meio de `plugins.entries.voice-call.config.streaming`.

Para transcrição em lote, o OpenClaw faz upload do arquivo de áudio completo para a Deepgram e injeta a transcrição no pipeline de resposta (`{{Transcript}}` \+ bloco `[Audio]`). Para STT em streaming do Voice Call, o OpenClaw encaminha frames ao vivo G.711 u-law pelo endpoint WebSocket `listen` da Deepgram e emite transcrições parciais ou finais conforme a Deepgram as retorna.

Detalhe | Valor  
---|---  
Site | [deepgram.com](<https://deepgram.com>)  
Documentação | [developers.deepgram.com](<https://developers.deepgram.com>)  
Auth | `DEEPGRAM_API_KEY`  
Modelo padrão | `nova-3`  
  
## Primeiros passos

* ### Defina sua chave de API

Adicione sua chave de API da Deepgram ao ambiente:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Ative o provedor de áudio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Envie uma nota de voz

Envie uma mensagem de áudio por qualquer canal conectado. O OpenClaw a transcreve pela Deepgram e injeta a transcrição no pipeline de resposta.

## Opções de configuração

Opção | Caminho | Descrição  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID do modelo da Deepgram (padrão: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Dica de idioma (opcional)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Ativa detecção de idioma (opcional)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Ativa pontuação (opcional)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Ativa formatação inteligente (opcional)  
  
### Com dica de idioma

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Com opções da Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT em streaming do Voice Call

O Plugin empacotado `deepgram` também registra um provedor de transcrição em tempo real para o Plugin Voice Call.

Configuração | Caminho de configuração | Padrão  
---|---|---  
Chave de API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Usa `DEEPGRAM_API_KEY` como fallback  
Modelo | `...deepgram.model` | `nova-3`  
Idioma | `...deepgram.language` | (não definido)  
Codificação | `...deepgram.encoding` | `mulaw`  
Taxa de amostra | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Resultados parciais | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Observações

Autenticação

A autenticação segue a ordem padrão de autenticação de provedor. `DEEPGRAM_API_KEY` é o caminho mais simples.

Proxy e endpoints personalizados

Substitua endpoints ou cabeçalhos com `tools.media.audio.baseUrl` e `tools.media.audio.headers` ao usar um proxy.

Comportamento da saída

A saída segue as mesmas regras de áudio dos outros provedores (limites de tamanho, timeouts, injeção de transcrição).

## Relacionado

[**Media tools** Visão geral do pipeline de processamento de áudio, imagem e vídeo. ](</pt-BR/tools/media-overview>) [**Configuration** Referência completa de configuração, incluindo ajustes de ferramentas de mídia. ](</pt-BR/gateway/configuration>) [**Troubleshooting** Problemas comuns e etapas de depuração. ](</pt-BR/help/troubleshooting>) [**FAQ** Perguntas frequentes sobre a configuração do OpenClaw. ](</pt-BR/help/faq>)

Was this useful?YesNo