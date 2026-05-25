---
title: LINHA
source_url: https://docs.openclaw.ai/pt-BR/channels/line
scraped_at: 2026-05-25
---

LINE se conecta ao OpenClaw via LINE Messaging API. O Plugin é executado como um receptor de webhook no gateway e usa seu token de acesso do canal + segredo do canal para autenticação.

Status: Plugin baixável. Mensagens diretas, chats em grupo, mídia, localizações, mensagens Flex, mensagens de modelo e respostas rápidas são compatíveis. Reações e threads não são compatíveis.

## Instalar

Instale o LINE antes de configurar o canal:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Checkout local (ao executar a partir de um repositório git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Configuração

  1. Crie uma conta LINE Developers e abra o Console: <https://developers.line.biz/console/>
  2. Crie (ou escolha) um Provider e adicione um canal **Messaging API**.
  3. Copie o **Channel access token** e o **Channel secret** das configurações do canal.
  4. Ative **Use webhook** nas configurações da Messaging API.
  5. Defina a URL do webhook para o endpoint do seu gateway (HTTPS obrigatório):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

O gateway responde à verificação de webhook do LINE (GET) e a eventos recebidos (POST). Se precisar de um caminho personalizado, defina `channels.line.webhookPath` ou `channels.line.accounts.<id>.webhookPath` e atualize a URL conforme necessário.

Observação de segurança:

  * A verificação de assinatura do LINE depende do corpo (HMAC sobre o corpo bruto), então o OpenClaw aplica limites estritos de corpo pré-autenticação e timeout antes da verificação.
  * O OpenClaw processa eventos de webhook a partir dos bytes brutos verificados da solicitação. Valores de `req.body` transformados por middleware upstream são ignorados para segurança da integridade da assinatura.


## Configurar

Configuração mínima:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Configuração de DM pública:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Variáveis de ambiente (somente conta padrão):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Arquivos de token/segredo:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` e `secretFile` devem apontar para arquivos regulares. Symlinks são rejeitados.

Várias contas:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Controle de acesso

Mensagens diretas usam pareamento por padrão. Remetentes desconhecidos recebem um código de pareamento e suas mensagens são ignoradas até serem aprovados.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Listas de permissão e políticas:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: IDs de usuário LINE permitidos para DMs; `dmPolicy: "open"` exige `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: IDs de usuário LINE permitidos para grupos
  * Substituições por grupo: `channels.line.groups.<groupId>.allowFrom`
  * Grupos estáticos de acesso de remetente podem ser referenciados de `allowFrom`, `groupAllowFrom` e `allowFrom` por grupo com `accessGroup:<name>`.
  * Observação de runtime: se `channels.line` estiver completamente ausente, o runtime recorre a `groupPolicy="allowlist"` para verificações de grupo (mesmo que `channels.defaults.groupPolicy` esteja definido).


IDs LINE diferenciam maiúsculas de minúsculas. IDs válidos se parecem com:

  * Usuário: `U` \+ 32 caracteres hexadecimais
  * Grupo: `C` \+ 32 caracteres hexadecimais
  * Sala: `R` \+ 32 caracteres hexadecimais


## Comportamento de mensagens

  * Texto é dividido em partes de 5000 caracteres.
  * A formatação Markdown é removida; blocos de código e tabelas são convertidos em cartões Flex quando possível.
  * Respostas em streaming são armazenadas em buffer; o LINE recebe partes completas com uma animação de carregamento enquanto o agente trabalha.
  * Downloads de mídia são limitados por `channels.line.mediaMaxMb` (padrão 10).
  * Mídia recebida é salva em `~/.openclaw/media/inbound/` antes de ser passada para o agente, correspondendo ao armazenamento de mídia compartilhado usado por outros plugins de canal incluídos.


## Dados do canal (mensagens ricas)

Use `channelData.line` para enviar respostas rápidas, localizações, cartões Flex ou mensagens de modelo.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

O Plugin LINE também inclui um comando `/card` para predefinições de mensagens Flex:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## Suporte a ACP

LINE é compatível com vinculações de conversa ACP (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` vincula o chat LINE atual a uma sessão ACP sem criar uma thread filha.
  * Vinculações ACP configuradas e sessões ACP ativas vinculadas a conversas funcionam no LINE como em outros canais de conversa.


Consulte [agentes ACP](</pt-BR/tools/acp-agents>) para obter detalhes.

## Mídia de saída

O Plugin LINE é compatível com o envio de imagens, vídeos e arquivos de áudio por meio da ferramenta de mensagens do agente. A mídia é enviada pela rota de entrega específica do LINE com tratamento adequado de pré-visualização e rastreamento:

  * **Imagens** : enviadas como mensagens de imagem LINE com geração automática de pré-visualização.
  * **Vídeos** : enviados com tratamento explícito de pré-visualização e tipo de conteúdo.
  * **Áudio** : enviado como mensagens de áudio LINE.


URLs de mídia de saída devem ser URLs HTTPS públicas. O OpenClaw valida o hostname de destino antes de entregar a URL ao LINE e rejeita destinos de loopback, link-local e rede privada.

Envios genéricos de mídia recorrem à rota existente apenas para imagens quando uma rota específica do LINE não está disponível.

## Solução de problemas

  * **A verificação do webhook falha:** verifique se a URL do webhook é HTTPS e se o `channelSecret` corresponde ao console LINE.
  * **Nenhum evento recebido:** confirme que o caminho do webhook corresponde a `channels.line.webhookPath` e que o gateway está acessível pelo LINE.
  * **Erros de download de mídia:** aumente `channels.line.mediaMaxMb` se a mídia exceder o limite padrão.


## Relacionado

  * [Visão geral dos canais](</pt-BR/channels>) — todos os canais compatíveis
  * [Pareamento](</pt-BR/channels/pairing>) — autenticação de DM e fluxo de pareamento
  * [Grupos](</pt-BR/channels/groups>) — comportamento de chat em grupo e controle de menções
  * [Roteamento de canais](</pt-BR/channels/channel-routing>) — roteamento de sessão para mensagens
  * [Segurança](</pt-BR/gateway/security>) — modelo de acesso e hardening


Was this useful?YesNo