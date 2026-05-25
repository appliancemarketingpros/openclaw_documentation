---
title: Gradium
source_url: https://docs.openclaw.ai/pt-BR/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) é um provedor de texto para fala incluído no OpenClaw. O Plugin pode renderizar respostas de áudio normais (WAV), saída Opus compatível com notas de voz e áudio u-law de 8 kHz para superfícies de telefonia.

Propriedade | Valor  
---|---  
ID do provedor | `gradium`  
Autenticação | `GRADIUM_API_KEY` ou config `apiKey`  
URL base | `https://api.gradium.ai` (padrão)  
Voz padrão | `Emma` (`YTpq7expH9539ERJ`)  
  
## Configuração

Crie uma chave de API do Gradium e, em seguida, exponha-a ao OpenClaw com uma variável de ambiente ou com a chave de configuração.

### Variável de ambiente

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Chave de configuração

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

O Plugin verifica primeiro o `apiKey` resolvido e recorre à variável de ambiente `GRADIUM_API_KEY`.

## Configuração

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Chave | Tipo | Descrição  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Chave de API resolvida. Compatível com `${ENV}` e referências de segredo.  
`messages.tts.providers.gradium.baseUrl` | string | Substitui a origem da API. Barras finais são removidas. O padrão é `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | ID de voz padrão usado quando nenhuma substituição por diretiva está presente.  
  
O formato de áudio de saída é selecionado automaticamente pelo runtime com base na superfície de destino e não é configurável em `openclaw.json`. Veja Saída abaixo.

## Vozes

Nome | ID da voz  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Voz padrão: Emma.

### Substituição de voz por mensagem

Quando a política de fala ativa permite substituições de voz, você pode trocar de voz inline usando um token de diretiva. Todas estas opções resolvem para a mesma substituição de `voiceId`:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Se a política de fala desabilitar substituições de voz, a diretiva será consumida, mas ignorada.

## Saída

O runtime escolhe o formato de saída a partir da superfície de destino. Atualmente, o provedor não sintetiza outros formatos.

Destino | Formato | Ext. do arquivo | Taxa de amostragem | Sinalizador compatível com voz  
---|---|---|---|---  
Áudio padrão | `wav` | `.wav` | provedor | não  
Nota de voz | `opus` | `.opus` | provedor | sim  
Telefonia | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## Ordem de seleção automática

Entre os provedores de TTS configurados, a ordem de seleção automática do Gradium é `30`. Veja [Texto para fala](</pt-BR/tools/tts>) para saber como o OpenClaw escolhe o provedor ativo quando `messages.tts.provider` não está fixado.

## Relacionados

  * [Texto para fala](</pt-BR/tools/tts>)
  * [Visão geral de mídia](</pt-BR/tools/media-overview>)


Was this useful?YesNo