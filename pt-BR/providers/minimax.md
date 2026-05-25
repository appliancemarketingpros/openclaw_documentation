---
title: MiniMax
source_url: https://docs.openclaw.ai/pt-BR/providers/minimax
scraped_at: 2026-05-25
---

O provedor MiniMax do OpenClaw usa **MiniMax M2.7** como padrão.

A MiniMax também fornece:

  * Síntese de fala integrada via T2A v2
  * Compreensão de imagens integrada via `MiniMax-VL-01`
  * Geração de música integrada via `music-2.6`
  * `web_search` integrado pela API de busca do MiniMax Token Plan


Divisão por provedor:

ID do provedor | Autenticação | Capacidades  
---|---|---  
`minimax` | Chave de API | Texto, geração de imagens, geração de música, geração de vídeo, compreensão de imagens, fala, busca na web  
`minimax-portal` | OAuth | Texto, geração de imagens, geração de música, geração de vídeo, compreensão de imagens, fala  
  
## Catálogo integrado

Modelo | Tipo | Descrição  
---|---|---  
`MiniMax-M2.7` | Chat (raciocínio) | Modelo de raciocínio hospedado padrão  
`MiniMax-M2.7-highspeed` | Chat (raciocínio) | Camada de raciocínio M2.7 mais rápida  
`MiniMax-VL-01` | Visão | Modelo de compreensão de imagens  
`image-01` | Geração de imagens | Edição de texto para imagem e imagem para imagem  
`music-2.6` | Geração de música | Modelo de música padrão  
`music-2.5` | Geração de música | Camada anterior de geração de música  
`music-2.0` | Geração de música | Camada legada de geração de música  
`MiniMax-Hailuo-2.3` | Geração de vídeo | Fluxos de texto para vídeo e referência de imagem  
  
## Primeiros passos

Escolha seu método de autenticação preferido e siga as etapas de configuração.

### OAuth (Coding Plan)

**Melhor para:** configuração rápida com o MiniMax Coding Plan via OAuth, sem necessidade de chave de API.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-oauth
[/code]

Isso autentica em `api.minimax.io`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-oauth
[/code]

Isso autentica em `api.minimaxi.com`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### API key

**Melhor para:** MiniMax hospedado com API compatível com Anthropic.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-api
[/code]

Isso configura `api.minimax.io` como a URL base.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-api
[/code]

Isso configura `api.minimaxi.com` como a URL base.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### Exemplo de configuração

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "minimax/MiniMax-M2.7" } } },  models: {    mode: "merge",    providers: {      minimax: {        baseUrl: "https://api.minimax.io/anthropic",        apiKey: "${MINIMAX_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "MiniMax-M2.7",            name: "MiniMax M2.7",            reasoning: true,            input: ["text"],            cost: { input: 0.3, output: 1.2, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },          {            id: "MiniMax-M2.7-highspeed",            name: "MiniMax M2.7 Highspeed",            reasoning: true,            input: ["text"],            cost: { input: 0.6, output: 2.4, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },        ],      },    },  },}
[/code]

## Configurar via `openclaw configure`

Use o assistente interativo de configuração para definir a MiniMax sem editar JSON:

* ### Inicie o assistente

bashCopy code
[code]
    openclaw configure
[/code]

* ### Selecione Modelo/autenticação

Escolha **Modelo/autenticação** no menu.

* ### Escolha uma opção de autenticação do MiniMax

Escolha uma das opções disponíveis do MiniMax:

Opção de autenticação | Descrição  
---|---  
`minimax-global-oauth` | OAuth internacional (Plano de Codificação)  
`minimax-cn-oauth` | OAuth da China (Plano de Codificação)  
`minimax-global-api` | Chave de API internacional  
`minimax-cn-api` | Chave de API da China  
* ### Escolha seu modelo padrão

Selecione seu modelo padrão quando solicitado.

## Recursos

### Geração de imagens

O Plugin MiniMax registra o modelo `image-01` para a ferramenta `image_generate`. Ele oferece suporte a:

  * **Geração de texto para imagem** com controle de proporção
  * **Edição de imagem para imagem** (referência de assunto) com controle de proporção
  * Até **9 imagens de saída** por solicitação
  * Até **1 imagem de referência** por solicitação de edição
  * Proporções compatíveis: `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`


Para usar o MiniMax na geração de imagens, defina-o como o provedor de geração de imagens:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "minimax/image-01" },    },  },}
[/code]

O Plugin usa a mesma `MINIMAX_API_KEY` ou autenticação OAuth dos modelos de texto. Nenhuma configuração adicional é necessária se o MiniMax já estiver configurado.

Tanto `minimax` quanto `minimax-portal` registram `image_generate` com o mesmo modelo `image-01`. Configurações com chave de API usam `MINIMAX_API_KEY`; configurações OAuth podem usar o caminho de autenticação `minimax-portal` integrado.

A geração de imagens sempre usa o endpoint de imagem dedicado do MiniMax (`/v1/image_generation`) e ignora `models.providers.minimax.baseUrl`, pois esse campo configura a URL base compatível com chat/Anthropic. Defina `MINIMAX_API_HOST=https://api.minimaxi.com` para rotear a geração de imagens pelo endpoint da CN; o endpoint global padrão é `https://api.minimax.io`.

Quando a integração inicial ou a configuração por chave de API grava entradas explícitas em `models.providers.minimax`, o OpenClaw materializa `MiniMax-M2.7` e `MiniMax-M2.7-highspeed` como modelos de chat somente de texto. A compreensão de imagens é exposta separadamente pelo provedor de mídia `MiniMax-VL-01`, de propriedade do Plugin.

### Texto para fala

O Plugin `minimax` integrado registra o MiniMax T2A v2 como provedor de fala para `messages.tts`.

  * Modelo TTS padrão: `speech-2.8-hd`
  * Voz padrão: `English_expressive_narrator`
  * IDs de modelos integrados compatíveis incluem `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd` e `speech-01-turbo`.
  * A resolução de autenticação é `messages.tts.providers.minimax.apiKey`, depois perfis de autenticação OAuth/token `minimax-portal`, depois chaves de ambiente do Plano de Token (`MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) e, por fim, `MINIMAX_API_KEY`.
  * Se nenhum host TTS estiver configurado, o OpenClaw reutiliza o host OAuth `minimax-portal` configurado e remove sufixos de caminho compatíveis com Anthropic, como `/anthropic`.
  * Anexos de áudio normais permanecem em MP3.
  * Destinos de notas de voz, como Feishu e Telegram, são transcodificados de MP3 do MiniMax para Opus a 48 kHz com `ffmpeg`, porque a API de arquivos do Feishu/Lark só aceita `file_type: "opus"` para mensagens de áudio nativas.
  * O MiniMax T2A aceita `speed` e `vol` fracionários, mas `pitch` é enviado como um inteiro; o OpenClaw trunca valores fracionários de `pitch` antes da solicitação à API.

Configuração | Var de ambiente | Padrão | Descrição  
---|---|---|---  
`messages.tts.providers.minimax.baseUrl` | `MINIMAX_API_HOST` | `https://api.minimax.io` | Host da API MiniMax T2A.  
`messages.tts.providers.minimax.model` | `MINIMAX_TTS_MODEL` | `speech-2.8-hd` | ID do modelo TTS.  
`messages.tts.providers.minimax.voiceId` | `MINIMAX_TTS_VOICE_ID` | `English_expressive_narrator` | ID da voz usada na saída de fala.  
`messages.tts.providers.minimax.speed` |  | `1.0` | Velocidade de reprodução, `0.5..2.0`.  
`messages.tts.providers.minimax.vol` |  | `1.0` | Volume, `(0, 10]`.  
`messages.tts.providers.minimax.pitch` |  | `0` | Deslocamento inteiro de tom, `-12..12`.  
  
### Geração de música

O Plugin MiniMax integrado registra a geração de música por meio da ferramenta compartilhada `music_generate` para `minimax` e `minimax-portal`.

  * Modelo de música padrão: `minimax/music-2.6`
  * Modelo de música OAuth: `minimax-portal/music-2.6`
  * Também oferece suporte a `minimax/music-2.5` e `minimax/music-2.0`
  * Controles de prompt: `lyrics`, `instrumental`, `durationSeconds`
  * Formato de saída: `mp3`
  * Execuções apoiadas por sessão são desanexadas pelo fluxo compartilhado de tarefa/status, incluindo `action: "status"`


Para usar o MiniMax como provedor de música padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "minimax/music-2.6",      },    },  },}
[/code]

### Geração de vídeo

O Plugin MiniMax integrado registra a geração de vídeo por meio da ferramenta compartilhada `video_generate` para `minimax` e `minimax-portal`.

  * Modelo de vídeo padrão: `minimax/MiniMax-Hailuo-2.3`
  * Modelo de vídeo OAuth: `minimax-portal/MiniMax-Hailuo-2.3`
  * Modos: fluxos de texto para vídeo e referência de imagem única
  * Compatível com `aspectRatio` e `resolution`


Para usar o MiniMax como provedor de vídeo padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "minimax/MiniMax-Hailuo-2.3",      },    },  },}
[/code]

### Compreensão de imagem

O Plugin MiniMax registra a compreensão de imagem separadamente do catálogo de texto:

ID do provedor | Modelo de imagem padrão  
---|---  
`minimax` | `MiniMax-VL-01`  
`minimax-portal` | `MiniMax-VL-01`  
  
É por isso que o roteamento automático de mídia pode usar a compreensão de imagem do MiniMax mesmo quando o catálogo de provedor de texto incluído ainda mostra refs de chat M2.7 somente texto.

### Pesquisa na web

O Plugin MiniMax também registra `web_search` por meio da API de pesquisa do MiniMax Token Plan.

  * ID do provedor: `minimax`
  * Resultados estruturados: títulos, URLs, trechos, consultas relacionadas
  * Variável de ambiente preferida: `MINIMAX_CODE_PLAN_KEY`
  * Aliases de ambiente aceitos: `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN`
  * Fallback de compatibilidade: `MINIMAX_API_KEY` quando ela já aponta para uma credencial token-plan
  * Reutilização de região: `plugins.entries.minimax.config.webSearch.region`, depois `MINIMAX_API_HOST`, depois URLs base do provedor MiniMax
  * A pesquisa permanece no ID de provedor `minimax`; a configuração OAuth CN/global pode direcionar a região indiretamente por meio de `models.providers.minimax-portal.baseUrl` e pode fornecer autenticação bearer por meio de `MINIMAX_OAUTH_TOKEN`


A configuração fica em `plugins.entries.minimax.config.webSearch.*`.

## Configuração avançada

Opções de configuração Opção | Descrição  
---|---  
`models.providers.minimax.baseUrl` | Prefira `https://api.minimax.io/anthropic` (compatível com Anthropic); `https://api.minimax.io/v1` é opcional para payloads compatíveis com OpenAI  
`models.providers.minimax.api` | Prefira `anthropic-messages`; `openai-completions` é opcional para payloads compatíveis com OpenAI  
`models.providers.minimax.apiKey` | Chave de API do MiniMax (`MINIMAX_API_KEY`)  
`models.providers.minimax.models` | Defina `id`, `name`, `reasoning`, `contextWindow`, `maxTokens`, `cost`  
`agents.defaults.models` | Crie aliases para modelos que você quer na allowlist  
`models.mode` | Mantenha `merge` se quiser adicionar MiniMax junto aos integrados  
Padrões de thinking

Em `api: "anthropic-messages"`, o OpenClaw injeta `thinking: { type: "disabled" }`, a menos que thinking já esteja explicitamente definido em params/config.

Isso impede que o endpoint de streaming do MiniMax emita `reasoning_content` em chunks delta no estilo OpenAI, o que vazaria raciocínio interno para a saída visível.

Modo rápido

`/fast on` ou `params.fastMode: true` reescreve `MiniMax-M2.7` para `MiniMax-M2.7-highspeed` no caminho de stream compatível com Anthropic.

Exemplo de fallback

**Melhor para:** manter seu modelo de última geração mais forte como primário e fazer failover para MiniMax M2.7. O exemplo abaixo usa Opus como primário concreto; troque pelo seu modelo primário de última geração preferido.

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": { alias: "primary" },        "minimax/MiniMax-M2.7": { alias: "minimax" },      },      model: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["minimax/MiniMax-M2.7"],      },    },  },}
[/code]

Detalhes de uso do Coding Plan

  * API de uso do Coding Plan: `https://api.minimaxi.com/v1/token_plan/remains` ou `https://api.minimax.io/v1/token_plan/remains` (requer uma chave de coding plan).
  * A sondagem de uso deriva o host de `models.providers.minimax-portal.baseUrl` ou `models.providers.minimax.baseUrl` quando configurado, então configurações globais usando `https://api.minimax.io/anthropic` sondam `api.minimax.io`. URLs base ausentes ou malformadas mantêm o fallback CN para compatibilidade.
  * O OpenClaw normaliza o uso do coding-plan do MiniMax para a mesma exibição de `% restante` usada por outros provedores. Os campos brutos `usage_percent` / `usagePercent` do MiniMax são cota restante, não cota consumida, então o OpenClaw os inverte. Campos baseados em contagem vencem quando presentes.
  * Quando a API retorna `model_remains`, o OpenClaw prefere a entrada de modelo de chat, deriva o rótulo da janela de `start_time` / `end_time` quando necessário e inclui o nome do modelo selecionado no rótulo do plano para que as janelas de coding-plan fiquem mais fáceis de distinguir.
  * Snapshots de uso tratam `minimax`, `minimax-cn` e `minimax-portal` como a mesma superfície de cota do MiniMax, e preferem OAuth MiniMax armazenado antes de recorrer a variáveis de ambiente de chave do Coding Plan.


## Observações

  * Refs de modelo seguem o caminho de autenticação: 
    * Configuração por chave de API: `minimax/<model>`
    * Configuração OAuth: `minimax-portal/<model>`
  * Modelo de chat padrão: `MiniMax-M2.7`
  * Modelo de chat alternativo: `MiniMax-M2.7-highspeed`
  * Onboarding e configuração direta por chave de API gravam definições de modelo somente texto para ambas as variantes M2.7
  * A compreensão de imagem usa o provedor de mídia `MiniMax-VL-01` pertencente ao Plugin
  * Atualize os valores de preço em `models.json` se precisar de rastreamento de custo exato
  * Use `openclaw models list` para confirmar o ID de provedor atual, depois alterne com `openclaw models set minimax/MiniMax-M2.7` ou `openclaw models set minimax-portal/MiniMax-M2.7`


## Solução de problemas

"Modelo desconhecido: minimax/MiniMax-M2.7"

Isso geralmente significa que o **provedor MiniMax não está configurado** (nenhuma entrada de provedor correspondente e nenhum perfil de autenticação/chave de ambiente do MiniMax encontrado). Uma correção para essa detecção está em **2026.1.12**. Corrija assim:

  * Atualize para **2026.1.12** (ou execute a partir do código-fonte `main`) e reinicie o Gateway.
  * Execute `openclaw configure` e selecione uma opção de autenticação **MiniMax** , ou
  * Adicione manualmente o bloco `models.providers.minimax` ou `models.providers.minimax-portal` correspondente, ou
  * Defina `MINIMAX_API_KEY`, `MINIMAX_OAUTH_TOKEN` ou um perfil de autenticação MiniMax para que o provedor correspondente possa ser injetado.


Garanta que o ID do modelo diferencie maiúsculas de minúsculas:

  * Caminho por chave de API: `minimax/MiniMax-M2.7` ou `minimax/MiniMax-M2.7-highspeed`
  * Caminho OAuth: `minimax-portal/MiniMax-M2.7` ou `minimax-portal/MiniMax-M2.7-highspeed`


Depois verifique novamente com:

bashCopy code
[code]
    openclaw models list
[/code]

## Relacionados

[**Seleção de modelo** Escolher provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Geração de imagem** Parâmetros compartilhados de ferramenta de imagem e seleção de provedor. ](</pt-BR/tools/image-generation>) [**Geração de música** Parâmetros compartilhados de ferramenta de música e seleção de provedor. ](</pt-BR/tools/music-generation>) [**Geração de vídeo** Parâmetros compartilhados de ferramenta de vídeo e seleção de provedor. ](</pt-BR/tools/video-generation>) [**Pesquisa MiniMax** Configuração de pesquisa na web via MiniMax Token Plan. ](</pt-BR/tools/minimax-search>) [**Solução de problemas** Solução de problemas geral e FAQ. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo