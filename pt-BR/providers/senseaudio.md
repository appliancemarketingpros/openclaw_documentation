---
title: SenseAudio
source_url: https://docs.openclaw.ai/pt-BR/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio pode transcrever anexos de áudio de entrada e notas de voz pelo pipeline compartilhado `tools.media.audio` do OpenClaw. O OpenClaw publica áudio multipart no endpoint de transcrição compatível com OpenAI e injeta o texto retornado como `{{Transcript}}`, além de um bloco `[Audio]`.

Propriedade | Valor  
---|---  
ID do provedor | `senseaudio`  
Plugin | incluído, `enabledByDefault: true`  
Contrato | `mediaUnderstandingProviders` (áudio)  
Var. de ambiente de autenticação | `SENSEAUDIO_API_KEY`  
Modelo padrão | `senseaudio-asr-pro-1.5-260319`  
URL padrão | `https://api.senseaudio.cn/v1`  
Site | [senseaudio.cn](<https://senseaudio.cn>)  
Documentação | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Primeiros passos

* ### Defina sua chave de API

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Ative o provedor de áudio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Envie uma nota de voz

Envie uma mensagem de áudio por qualquer canal conectado. O OpenClaw envia o áudio para o SenseAudio e usa a transcrição no pipeline de resposta.

## Opções

Opção | Caminho | Descrição  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID do modelo ASR do SenseAudio  
`language` | `tools.media.audio.models[].language` | Dica opcional de idioma  
`prompt` | `tools.media.audio.prompt` | Prompt opcional de transcrição  
`baseUrl` | `tools.media.audio.baseUrl` ou modelo | Substitui a base compatível com OpenAI  
`headers` | `tools.media.audio.request.headers` | Cabeçalhos extras da solicitação  
  
## Relacionados

  * [Entendimento de mídia (áudio)](</pt-BR/nodes/audio>)
  * [Provedores de modelos](</pt-BR/concepts/model-providers>)


Was this useful?YesNo