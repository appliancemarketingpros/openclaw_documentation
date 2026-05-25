---
title: Pareamento
source_url: https://docs.openclaw.ai/pt-BR/channels/pairing
scraped_at: 2026-05-25
---

"Pareamento" é a etapa explícita de aprovação de acesso do OpenClaw. Ele é usado em dois lugares:

  1. **Pareamento de DM** (quem tem permissão para falar com o bot)
  2. **Pareamento de Node** (quais dispositivos/nós têm permissão para entrar na rede do Gateway)


Contexto de segurança: [Segurança](</pt-BR/gateway/security>)

## 1) Pareamento de DM (acesso de chat de entrada)

Quando um canal é configurado com a política de DM `pairing`, remetentes desconhecidos recebem um código curto e sua mensagem **não é processada** até que você aprove.

As políticas de DM padrão estão documentadas em: [Segurança](</pt-BR/gateway/security>)

`dmPolicy: "open"` é público somente quando a lista de permissões de DM efetiva inclui `"*"`. A configuração e a validação exigem esse curinga para configurações públicas abertas. Se o estado existente contiver `open` com entradas concretas de `allowFrom`, em tempo de execução ainda serão admitidos apenas esses remetentes, e aprovações do armazenamento de pareamento não ampliam o acesso `open`.

Códigos de pareamento:

  * 8 caracteres, maiúsculos, sem caracteres ambíguos (`0O1I`).
  * **Expiram após 1 hora**. O bot só envia a mensagem de pareamento quando uma nova solicitação é criada (aproximadamente uma vez por hora por remetente).
  * Solicitações pendentes de pareamento de DM são limitadas a **3 por canal** por padrão; solicitações adicionais são ignoradas até que uma expire ou seja aprovada.


### Aprovar um remetente

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing approve telegram &lt;CODE&gt;
[/code]

Se nenhum proprietário de comandos ainda estiver configurado, aprovar um código de pareamento de DM também inicializa `commands.ownerAllowFrom` com o remetente aprovado, como `telegram:123456789`. Isso dá às configurações iniciais um proprietário explícito para comandos privilegiados e prompts de aprovação de exec. Depois que um proprietário existe, aprovações de pareamento posteriores apenas concedem acesso de DM; elas não adicionam mais proprietários.

Canais compatíveis: `discord`, `feishu`, `googlechat`, `imessage`, `irc`, `line`, `matrix`, `mattermost`, `msteams`, `nextcloud-talk`, `nostr`, `openclaw-weixin`, `signal`, `slack`, `synology-chat`, `telegram`, `twitch`, `whatsapp`, `zalo`, `zalouser`.

### Grupos de remetentes reutilizáveis

Use `accessGroups` de nível superior quando o mesmo conjunto de remetentes confiáveis deve se aplicar a vários canais de mensagem ou tanto a listas de permissões de DM quanto de grupo.

Grupos estáticos usam `type: "message.senders"` e são referenciados com `accessGroup:<name>` a partir das listas de permissões dos canais:

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        discord: ["discord:123456789012345678"],        telegram: ["987654321"],        whatsapp: ["+15551234567"],      },    },  },  channels: {    telegram: { dmPolicy: "allowlist", allowFrom: ["accessGroup:operators"] },    whatsapp: { groupPolicy: "allowlist", groupAllowFrom: ["accessGroup:operators"] },  },}
[/code]

Grupos de acesso estão documentados em detalhes aqui: [Grupos de acesso](</pt-BR/channels/access-groups>)

### Onde o estado fica

Armazenado em `~/.openclaw/credentials/`:

  * Solicitações pendentes: `<channel>-pairing.json`
  * Armazenamento da lista de permissões aprovada: 
    * Conta padrão: `<channel>-allowFrom.json`
    * Conta não padrão: `<channel>-<accountId>-allowFrom.json`


Comportamento de escopo de conta:

  * Contas não padrão leem/gravam apenas seu arquivo de lista de permissões com escopo.
  * A conta padrão usa o arquivo de lista de permissões sem escopo, com escopo de canal.


Trate esses arquivos como sensíveis (eles controlam o acesso ao seu assistente).

## 2) Pareamento de dispositivo Node (nós iOS/Android/macOS/headless)

Nós se conectam ao Gateway como **dispositivos** com `role: node`. O Gateway cria uma solicitação de pareamento de dispositivo que precisa ser aprovada.

### Parear via Telegram (recomendado para iOS)

Se você usa o Plugin `device-pair`, pode fazer o pareamento inicial de dispositivo inteiramente pelo Telegram:

  1. No Telegram, envie uma mensagem ao seu bot: `/pair`
  2. O bot responde com duas mensagens: uma mensagem de instruções e uma mensagem separada de **código de configuração** (fácil de copiar/colar no Telegram).
  3. No seu telefone, abra o app OpenClaw para iOS → Settings → Gateway.
  4. Escaneie o código QR ou cole o código de configuração e conecte.
  5. De volta ao Telegram: `/pair pending` (revise IDs de solicitação, função e escopos), depois aprove.


O código de configuração é uma carga útil JSON codificada em base64 que contém:

  * `url`: a URL WebSocket do Gateway (`ws://...` ou `wss://...`)
  * `bootstrapToken`: um token de bootstrap de curta duração para um único dispositivo usado no handshake inicial de pareamento


Esse token de bootstrap carrega o perfil integrado de bootstrap de pareamento:

  * o token `node` primário entregue permanece com `scopes: []`
  * qualquer token `operator` entregue permanece limitado à lista de permissões de bootstrap: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`
  * verificações de escopo de bootstrap têm prefixo de função, não um único pool plano de escopos: entradas de escopo de operador só satisfazem solicitações de operador, e funções não operadoras ainda precisam solicitar escopos sob seu próprio prefixo de função
  * rotação/revogação posterior de tokens permanece limitada tanto pelo contrato de função aprovado do dispositivo quanto pelos escopos de operador da sessão chamadora


Trate o código de configuração como uma senha enquanto ele estiver válido.

Para pareamento móvel remoto via Tailscale, público ou outro, use Tailscale Serve/Funnel ou outra URL `wss://` do Gateway. Códigos de configuração em texto claro `ws://` são aceitos somente para loopback, endereços de LAN privada, hosts Bonjour `.local` e o host do emulador Android. Endereços CGNAT da tailnet, nomes `.ts.net` e hosts públicos ainda falham de forma fechada antes da emissão de QR/código de configuração.

### Aprovar um dispositivo Node

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw devices reject <requestId>
[/code]

Quando uma aprovação explícita é negada porque a sessão de dispositivo pareado aprovadora foi aberta com escopo apenas de pareamento, a CLI tenta a mesma solicitação novamente com `operator.admin`. Isso permite que um dispositivo pareado existente com capacidade de admin recupere um novo pareamento da Control UI/navegador sem editar `devices/paired.json` manualmente. O Gateway ainda valida a conexão tentada novamente; tokens que não conseguem autenticar com `operator.admin` permanecem bloqueados.

Se o mesmo dispositivo tentar novamente com detalhes de autenticação diferentes (por exemplo, outra função/escopos/chave pública), a solicitação pendente anterior será substituída e um novo `requestId` será criado.

### Aprovação automática opcional de Node por CIDR confiável

O pareamento de dispositivo permanece manual por padrão. Para redes de nós rigidamente controladas, você pode optar pela aprovação automática de Node no primeiro uso com CIDRs explícitos ou IPs exatos:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

Isso se aplica somente a solicitações novas de pareamento `role: node` sem escopos solicitados. Clientes de operador, navegador, Control UI e WebChat ainda exigem aprovação manual. Alterações de função, escopo, metadados e chave pública ainda exigem aprovação manual.

### Armazenamento do estado de pareamento de Node

Armazenado em `~/.openclaw/devices/`:

  * `pending.json` (curta duração; solicitações pendentes expiram)
  * `paired.json` (dispositivos pareados + tokens)


### Observações

  * A API legada `node.pair.*` (CLI: `openclaw nodes pending|approve|reject|remove|rename`) é um armazenamento de pareamento separado de propriedade do gateway. Nós WS ainda exigem pareamento de dispositivo.
  * O registro de pareamento é a fonte durável da verdade para funções aprovadas. Tokens de dispositivo ativos permanecem limitados a esse conjunto de funções aprovado; uma entrada de token avulsa fora das funções aprovadas não cria novo acesso.


## Documentos relacionados

  * Modelo de segurança + injeção de prompt: [Segurança](</pt-BR/gateway/security>)
  * Atualização segura (execute doctor): [Atualização](</pt-BR/install/updating>)
  * Configurações de canal: 
    * Telegram: [Telegram](</pt-BR/channels/telegram>)
    * WhatsApp: [WhatsApp](</pt-BR/channels/whatsapp>)
    * Signal: [Signal](</pt-BR/channels/signal>)
    * iMessage: [iMessage](</pt-BR/channels/imessage>)
    * Discord: [Discord](</pt-BR/channels/discord>)
    * Slack: [Slack](</pt-BR/channels/slack>)


Was this useful?YesNo