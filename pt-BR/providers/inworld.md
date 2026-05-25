---
title: Inworld
source_url: https://docs.openclaw.ai/pt-BR/providers/inworld
scraped_at: 2026-05-25
---

Inworld é um provedor de texto para fala (TTS) por streaming. No OpenClaw, ele sintetiza o áudio de respostas de saída (MP3 por padrão, OGG_OPUS para notas de voz) e áudio PCM para canais de telefonia, como Chamada de voz.

O OpenClaw envia requisições para o endpoint de TTS por streaming da Inworld, concatena os fragmentos de áudio em base64 retornados em um único buffer e entrega o resultado ao pipeline padrão de áudio de resposta.

Propriedade | Valor  
---|---  
ID do provedor | `inworld`  
Plugin | incluído, `enabledByDefault: true`  
Contrato | `speechProviders` (somente TTS)  
Variável de ambiente de autenticação | `INWORLD_API_KEY` (HTTP Basic, credencial Base64 do painel)  
URL base | `https://api.inworld.ai`  
Voz padrão | `Sarah`  
Modelo padrão | `inworld-tts-1.5-max`  
Saída | MP3 (padrão), OGG_OPUS (notas de voz), PCM 22050 Hz (telefonia)  
Site | [inworld.ai](<https://inworld.ai>)  
Documentação | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Primeiros passos

* ### Defina sua chave de API

Copie a credencial do seu painel da Inworld (Workspace > API Keys) e defina-a como uma variável de ambiente. O valor é enviado literalmente como a credencial HTTP Basic, portanto não o codifique em Base64 novamente nem o converta em um token bearer.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Selecione Inworld em messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Envie uma mensagem

Envie uma resposta por qualquer canal conectado. O OpenClaw sintetiza o áudio com a Inworld e o entrega como MP3 (ou OGG_OPUS quando o canal espera uma nota de voz).

## Opções de configuração

Opção | Caminho | Descrição  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Credencial Base64 do painel. Usa `INWORLD_API_KEY` como fallback.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Substitui a URL base da API da Inworld (padrão `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Identificador de voz (padrão `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | ID do modelo TTS (padrão `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Temperatura de amostragem `0..2` (opcional).  
  
## Observações

Autenticação

A Inworld usa autenticação HTTP Basic com uma única string de credencial codificada em Base64. Copie-a literalmente do painel da Inworld. O provedor a envia como `Authorization: Basic <apiKey>` sem nenhuma codificação adicional, portanto não a codifique em Base64 você mesmo e não passe um token no estilo bearer. Consulte [observações de autenticação de TTS](</pt-BR/tools/tts#inworld-primary>) para o mesmo destaque.

Modelos

IDs de modelo compatíveis: `inworld-tts-1.5-max` (padrão), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Saídas de áudio

As respostas usam MP3 por padrão. Quando o destino do canal é `voice-note`, o OpenClaw solicita `OGG_OPUS` à Inworld para que o áudio seja reproduzido como uma bolha de voz nativa. A síntese de telefonia usa `PCM` bruto a 22050 Hz para alimentar a ponte de telefonia.

Endpoints personalizados

Substitua o host da API com `messages.tts.providers.inworld.baseUrl`. Barras finais são removidas antes do envio das requisições.

## Relacionado

[**Texto para fala** Visão geral de TTS, provedores e configuração de `messages.tts`. ](</pt-BR/tools/tts>) [**Configuração** Referência completa de configuração, incluindo definições de `messages.tts`. ](</pt-BR/gateway/configuration>) [**Provedores** Todos os provedores incluídos do OpenClaw. ](</pt-BR/providers>) [**Solução de problemas** Problemas comuns e etapas de depuração. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo