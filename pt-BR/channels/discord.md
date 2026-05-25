---
title: Discord
source_url: https://docs.openclaw.ai/pt-BR/channels/discord
scraped_at: 2026-05-25
---

Pronto para DMs e canais de guilda por meio do Gateway oficial do Discord.

[**Emparelhamento** As DMs do Discord usam o modo de emparelhamento por padrão. ](</pt-BR/channels/pairing>) [**Comandos de barra** Comportamento nativo de comandos e catálogo de comandos. ](</pt-BR/tools/slash-commands>) [**Solução de problemas de canais** Diagnósticos entre canais e fluxo de reparo. ](</pt-BR/channels/troubleshooting>)

## Configuração rápida

Você precisará criar uma nova aplicação com um bot, adicionar o bot ao seu servidor e emparelhá-lo com o OpenClaw. Recomendamos adicionar o bot ao seu próprio servidor privado. Se você ainda não tiver um, [crie um primeiro](<https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server>) (escolha **Criar o meu próprio > Para mim e meus amigos**).

* ### Crie uma aplicação e um bot do Discord

Acesse o [Portal de Desenvolvedores do Discord](<https://discord.com/developers/applications>) e clique em **Nova aplicação**. Dê a ela um nome como "OpenClaw".

Clique em **Bot** na barra lateral. Defina o **Nome de usuário** como o nome que você usa para o seu agente OpenClaw.

* ### Ative intenções privilegiadas

Ainda na página **Bot** , role para baixo até **Intenções privilegiadas do Gateway** e ative:

  * **Intenção de conteúdo da mensagem** (obrigatória)
  * **Intenção de membros do servidor** (recomendada; obrigatória para listas de permissões de função e correspondência de nome para ID)
  * **Intenção de presença** (opcional; necessária apenas para atualizações de presença)


* ### Copie o token do seu bot

Role de volta para cima na página **Bot** e clique em **Redefinir token**.

Copie o token e salve-o em algum lugar. Este é seu **Token do Bot** e você precisará dele em breve.

* ### Gere uma URL de convite e adicione o bot ao seu servidor

Clique em **OAuth2** na barra lateral. Você gerará uma URL de convite com as permissões corretas para adicionar o bot ao seu servidor.

Role para baixo até **Gerador de URL OAuth2** e ative:

  * `bot`
  * `applications.commands`


Uma seção **Permissões do Bot** aparecerá abaixo. Ative pelo menos:

**Permissões gerais**

  * Ver canais **Permissões de texto**
  * Enviar mensagens
  * Ler histórico de mensagens
  * Incorporar links
  * Anexar arquivos
  * Adicionar reações (opcional)


Este é o conjunto básico para canais de texto normais. Se você planeja postar em threads do Discord, incluindo fluxos de trabalho de fórum ou canal de mídia que criam ou continuam uma thread, também ative **Enviar mensagens em threads**. Copie a URL gerada na parte inferior, cole-a no navegador, selecione seu servidor e clique em **Continuar** para conectar. Agora você deve ver seu bot no servidor Discord.

* ### Ative o Modo de Desenvolvedor e colete seus IDs

De volta ao aplicativo Discord, você precisa ativar o Modo de Desenvolvedor para poder copiar IDs internos.

  1. Clique em **Configurações do usuário** (ícone de engrenagem ao lado do seu avatar) → **Avançado** → ative **Modo de Desenvolvedor**
  2. Clique com o botão direito no **ícone do servidor** na barra lateral → **Copiar ID do Servidor**
  3. Clique com o botão direito no **seu próprio avatar** → **Copiar ID do Usuário**


Salve seu **ID do Servidor** e **ID do Usuário** junto com seu Token do Bot — você enviará os três para o OpenClaw na próxima etapa.

* ### Permita DMs de membros do servidor

Para que o emparelhamento funcione, o Discord precisa permitir que seu bot envie DM para você. Clique com o botão direito no **ícone do servidor** → **Configurações de privacidade** → ative **Mensagens diretas**.

Isso permite que membros do servidor (incluindo bots) enviem DMs para você. Mantenha isso ativado se quiser usar DMs do Discord com o OpenClaw. Se você pretende usar apenas canais de guilda, pode desativar as DMs depois do emparelhamento.

* ### Configure o token do seu bot com segurança (não o envie no chat)

O token do seu bot do Discord é um segredo (como uma senha). Configure-o na máquina que executa o OpenClaw antes de enviar mensagens ao seu agente.

bashCopy code
[code]
    export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN"cat > discord.patch.json5 <<'JSON5'{channels: {discord: {  enabled: true,  token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },},},}JSON5openclaw config patch --file ./discord.patch.json5 --dry-runopenclaw config patch --file ./discord.patch.json5openclaw gateway
[/code]

Se o OpenClaw já estiver em execução como serviço em segundo plano, reinicie-o pelo aplicativo OpenClaw para Mac ou parando e reiniciando o processo `openclaw gateway run`. Para instalações de serviço gerenciado, execute `openclaw gateway install` em um shell onde `DISCORD_BOT_TOKEN` esteja presente, ou armazene a variável em `~/.openclaw/.env`, para que o serviço possa resolver a SecretRef de env após a reinicialização. Se seu host estiver bloqueado ou com limitação de taxa pela consulta de aplicação na inicialização do Discord, configure o ID da aplicação/cliente do Discord no Portal de Desenvolvedores para que a inicialização possa ignorar essa chamada REST. Use `channels.discord.applicationId` para a conta padrão, ou `channels.discord.accounts.<accountId>.applicationId` quando você executar vários bots do Discord.

* ### Configure o OpenClaw e emparelhe

### Pergunte ao seu agente

Converse com seu agente OpenClaw em qualquer canal existente (por exemplo, Telegram) e informe-o. Se o Discord for seu primeiro canal, use a aba CLI / configuração.

> "Já configurei meu token de bot do Discord na configuração. Conclua a configuração do Discord com o ID do Usuário `<user_id>` e o ID do Servidor `<server_id>`."

### CLI / configuração

Se você preferir configuração baseada em arquivo, defina:

json5Copy code
[code]
    {channels: {discord: {enabled: true,token: {source: "env",provider: "default",id: "DISCORD_BOT_TOKEN",},},},}
[/code]

Fallback de env para a conta padrão:

bashCopy code
[code]
    DISCORD_BOT_TOKEN=...
[/code]

Para configuração roteirizada ou remota, grave o mesmo bloco JSON5 com `openclaw config patch --file ./discord.patch.json5 --dry-run` e depois execute novamente sem `--dry-run`. Valores `token` em texto simples são compatíveis. Valores SecretRef também são compatíveis para `channels.discord.token` entre provedores env/file/exec. Consulte [Gerenciamento de segredos](</pt-BR/gateway/secrets>).

Para vários bots do Discord, mantenha cada token de bot e ID de aplicação na respectiva conta. Um `channels.discord.applicationId` de nível superior é herdado pelas contas, então configure-o ali somente quando todas as contas devem usar o mesmo ID de aplicação.

json5Copy code
[code]
    {channels: {discord: {enabled: true,accounts: {personal: {  token: { source: "env", provider: "default", id: "DISCORD_PERSONAL_TOKEN" },  applicationId: "111111111111111111",},work: {  token: { source: "env", provider: "default", id: "DISCORD_WORK_TOKEN" },  applicationId: "222222222222222222",},},},},}
[/code]

* ### Aprove o primeiro emparelhamento por DM

Espere até que o Gateway esteja em execução e então envie uma DM ao seu bot no Discord. Ele responderá com um código de emparelhamento.

### Pergunte ao seu agente

Envie o código de emparelhamento para o seu agente no canal existente:

> "Aprove este código de emparelhamento do Discord: `&lt;CODE&gt;`"

### CLI

bashCopy code
[code]
    openclaw pairing list discordopenclaw pairing approve discord &lt;CODE&gt;
[/code]

Códigos de emparelhamento expiram após 1 hora.

Agora você deve conseguir conversar com seu agente no Discord via DM.

## Recomendado: configure um workspace de guilda

Depois que as DMs estiverem funcionando, você pode configurar seu servidor Discord como um workspace completo em que cada canal recebe sua própria sessão de agente com seu próprio contexto. Isso é recomendado para servidores privados onde há apenas você e seu bot.

* ### Adicione seu servidor à lista de permissões de guildas

Isso permite que seu agente responda em qualquer canal no seu servidor, não apenas em DMs.

### Pergunte ao seu agente

> "Adicione meu ID do Servidor Discord `<server_id>` à lista de permissões de guildas"

### Configuração

json5Copy code
[code]
    {channels: {discord: {groupPolicy: "allowlist",guilds: {YOUR_SERVER_ID: {  requireMention: true,  users: ["YOUR_USER_ID"],},},},},}
[/code]

* ### Permita respostas sem @mention

Por padrão, seu agente só responde em canais de guilda quando é mencionado com @. Para um servidor privado, você provavelmente quer que ele responda a todas as mensagens.

Em canais de guilda, as respostas finais normais do assistente permanecem privadas por padrão. A saída visível no Discord deve ser enviada explicitamente com a ferramenta `message`, para que o agente possa observar por padrão e só postar quando decidir que uma resposta no canal é útil.

Isso significa que o modelo selecionado deve chamar ferramentas de forma confiável. Se o Discord mostrar digitação e os logs mostrarem uso de tokens, mas nenhuma mensagem postada, verifique o log da sessão em busca de texto do assistente com `didSendViaMessagingTool: false`. Isso significa que o modelo produziu uma resposta final privada em vez de chamar `message(action=send)`. Troque para um modelo mais forte em chamadas de ferramentas, ou use a configuração abaixo para restaurar respostas finais automáticas legadas.

### Pergunte ao seu agente

> "Permita que meu agente responda neste servidor sem precisar ser mencionado com @"

### Configuração

Defina `requireMention: false` na sua configuração de guilda:

json5Copy code
[code]
    {channels: {discord: {guilds: {YOUR_SERVER_ID: {  requireMention: false,},},},},}
[/code]

Para restaurar respostas finais automáticas legadas para salas de grupo/canal, defina `messages.groupChat.visibleReplies: "automatic"`.

* ### Planeje memória em canais de guilda

Por padrão, a memória de longo prazo ([MEMORY.md](<http://MEMORY.md>)) só é carregada em sessões de DM. Canais de guilda não carregam [MEMORY.md](<http://MEMORY.md>) automaticamente.

### Pergunte ao seu agente

> "Quando eu fizer perguntas em canais do Discord, use memory_search ou memory_get se precisar de contexto de longo prazo de [MEMORY.md](<http://MEMORY.md>)."

### Manual

Se você precisa de contexto compartilhado em todos os canais, coloque as instruções estáveis em `AGENTS.md` ou `USER.md` (elas são injetadas em todas as sessões). Mantenha notas de longo prazo em `MEMORY.md` e acesse-as sob demanda com ferramentas de memória.

Agora crie alguns canais no seu servidor Discord e comece a conversar. Seu agente pode ver o nome do canal, e cada canal recebe sua própria sessão isolada — então você pode configurar `#coding`, `#home`, `#research` ou o que se encaixar no seu fluxo de trabalho.

## Modelo de runtime

  * O Gateway é dono da conexão do Discord.
  * O roteamento de respostas é determinístico: respostas recebidas do Discord voltam para o Discord.
  * Metadados de guilda/canal do Discord são adicionados ao prompt do modelo como contexto não confiável, não como prefixo de resposta visível ao usuário. Se um modelo copiar esse envelope de volta, o OpenClaw remove os metadados copiados das respostas enviadas e do contexto de reprodução futuro.
  * Por padrão (`session.dmScope=main`), conversas diretas compartilham a sessão principal do agente (`agent:main:main`).
  * Canais de guilda são chaves de sessão isoladas (`agent:<agentId>:discord:channel:<channelId>`).
  * DMs em grupo são ignoradas por padrão (`channels.discord.dm.groupEnabled=false`).
  * Comandos slash nativos executam em sessões de comando isoladas (`agent:<agentId>:discord:slash:<userId>`), enquanto ainda carregam `CommandTargetSessionKey` para a sessão de conversa roteada.
  * A entrega de anúncios de cron/heartbeat somente texto ao Discord usa a resposta final visível ao assistente uma vez. Payloads de mídia e componentes estruturados permanecem com várias mensagens quando o agente emite múltiplos payloads entregáveis.


## Canais de fórum

Canais de fórum e mídia do Discord aceitam apenas publicações em threads. O OpenClaw oferece suporte a duas formas de criá-las:

  * Envie uma mensagem ao fórum pai (`channel:<forumId>`) para criar uma thread automaticamente. O título da thread usa a primeira linha não vazia da sua mensagem.
  * Use `openclaw message thread create` para criar uma thread diretamente. Não passe `--message-id` para canais de fórum.


Exemplo: enviar ao fórum pai para criar uma thread

bashCopy code
[code]
    openclaw message send --channel discord --target channel:<forumId> \  --message "Topic title\nBody of the post"
[/code]

Exemplo: criar uma thread de fórum explicitamente

bashCopy code
[code]
    openclaw message thread create --channel discord --target channel:<forumId> \  --thread-name "Topic title" --message "Body of the post"
[/code]

Fóruns pais não aceitam componentes do Discord. Se você precisar de componentes, envie para a própria thread (`channel:<threadId>`).

## Componentes interativos

O OpenClaw oferece suporte a contêineres de componentes v2 do Discord para mensagens de agentes. Use a ferramenta de mensagens com um payload `components`. Resultados de interação são roteados de volta ao agente como mensagens recebidas normais e seguem as configurações existentes de `replyToMode` do Discord.

Blocos compatíveis:

  * `text`, `section`, `separator`, `actions`, `media-gallery`, `file`
  * Linhas de ações permitem até 5 botões ou um único menu de seleção
  * Tipos de seleção: `string`, `user`, `role`, `mentionable`, `channel`


Por padrão, componentes são de uso único. Defina `components.reusable=true` para permitir que botões, seletores e formulários sejam usados várias vezes até expirarem.

Para restringir quem pode clicar em um botão, defina `allowedUsers` nesse botão (IDs de usuário do Discord, tags ou `*`). Quando configurado, usuários sem correspondência recebem uma negação efêmera.

Os comandos slash `/model` e `/models` abrem um seletor de modelo interativo com menus suspensos de provedor, modelo e runtime compatível, além de uma etapa de Enviar. `/models add` está obsoleto e agora retorna uma mensagem de obsolescência em vez de registrar modelos pelo chat. A resposta do seletor é efêmera e somente o usuário que a invocou pode usá-la. Menus de seleção do Discord são limitados a 25 opções, então adicione entradas `provider/*` a `agents.defaults.models` quando quiser que o seletor mostre modelos descobertos dinamicamente apenas para provedores selecionados, como `openai-codex` ou `vllm`.

Anexos de arquivo:

  * Blocos `file` devem apontar para uma referência de anexo (`attachment://<filename>`)
  * Forneça o anexo via `media`/`path`/`filePath` (arquivo único); use `media-gallery` para múltiplos arquivos
  * Use `filename` para substituir o nome de upload quando ele deve corresponder à referência do anexo


Formulários modais:

  * Adicione `components.modal` com até 5 campos
  * Tipos de campo: `text`, `checkbox`, `radio`, `select`, `role-select`, `user-select`
  * O OpenClaw adiciona automaticamente um botão de acionamento


Exemplo:

json5Copy code
[code]
    {  channel: "discord",  action: "send",  to: "channel:123456789012345678",  message: "Optional fallback text",  components: {    reusable: true,    text: "Choose a path",    blocks: [      {        type: "actions",        buttons: [          {            label: "Approve",            style: "success",            allowedUsers: ["123456789012345678"],          },          { label: "Decline", style: "danger" },        ],      },      {        type: "actions",        select: {          type: "string",          placeholder: "Pick an option",          options: [            { label: "Option A", value: "a" },            { label: "Option B", value: "b" },          ],        },      },    ],    modal: {      title: "Details",      triggerLabel: "Open form",      fields: [        { type: "text", label: "Requester" },        {          type: "select",          label: "Priority",          options: [            { label: "Low", value: "low" },            { label: "High", value: "high" },          ],        },      ],    },  },}
[/code]

## Controle de acesso e roteamento

### DM policy

`channels.discord.dmPolicy` controla o acesso por DM. `channels.discord.allowFrom` é a lista de permissão canônica de DM.

  * `pairing` (padrão)
  * `allowlist`
  * `open` (requer que `channels.discord.allowFrom` inclua `"*"`)
  * `disabled`


Se a política de DM não estiver aberta, usuários desconhecidos são bloqueados (ou solicitados a fazer pareamento no modo `pairing`).

Precedência de múltiplas contas:

  * `channels.discord.accounts.default.allowFrom` aplica-se apenas à conta `default`.
  * Para uma conta, `allowFrom` tem precedência sobre o `dm.allowFrom` legado.
  * Contas nomeadas herdam `channels.discord.allowFrom` quando seus próprios `allowFrom` e `dm.allowFrom` legado não estão definidos.
  * Contas nomeadas não herdam `channels.discord.accounts.default.allowFrom`.


`channels.discord.dm.policy` e `channels.discord.dm.allowFrom` legados ainda são lidos para compatibilidade. `openclaw doctor --fix` os migra para `dmPolicy` e `allowFrom` quando pode fazer isso sem alterar o acesso.

Formato de alvo de DM para entrega:

  * `user:<id>`
  * menção `<@id>`


IDs numéricos simples normalmente são resolvidos como IDs de canal quando um canal padrão está ativo, mas IDs listados no `allowFrom` efetivo de DM da conta são tratados como alvos de DM de usuário para compatibilidade.

### Access groups

DMs do Discord e autorização de comandos de texto podem usar entradas dinâmicas `accessGroup:<name>` em `channels.discord.allowFrom`.

Nomes de grupos de acesso são compartilhados entre canais de mensagem. Use `type: "message.senders"` para um grupo estático cujos membros são expressos na sintaxe `allowFrom` normal de cada canal, ou `type: "discord.channelAudience"` quando o público atual com `ViewChannel` de um canal do Discord deve definir a associação dinamicamente. O comportamento compartilhado de grupos de acesso está documentado aqui: [Grupos de acesso](</pt-BR/channels/access-groups>).

json5Copy code
[code]
    {accessGroups: {operators: {  type: "message.senders",  members: {    "*": ["global-owner-id"],    discord: ["discord:123456789012345678"],    telegram: ["987654321"],  },},},channels: {discord: {  dmPolicy: "allowlist",  allowFrom: ["accessGroup:operators"],},},}
[/code]

Um canal de texto do Discord não tem lista de membros separada. `type: "discord.channelAudience"` modela a associação assim: o remetente da DM é membro da guilda configurada e tem atualmente permissão efetiva `ViewChannel` no canal configurado depois que sobrescritas de função e canal são aplicadas.

Exemplo: permitir que qualquer pessoa que possa ver `#maintainers` envie DM ao bot, mantendo DMs fechadas para todos os demais.

json5Copy code
[code]
    {accessGroups: {maintainers: {  type: "discord.channelAudience",  guildId: "1456350064065904867",  channelId: "1456744319972282449",  membership: "canViewChannel",},},channels: {discord: {  dmPolicy: "allowlist",  allowFrom: ["accessGroup:maintainers"],},},}
[/code]

Você pode misturar entradas dinâmicas e estáticas:

json5Copy code
[code]
    {accessGroups: {maintainers: {  type: "discord.channelAudience",  guildId: "1456350064065904867",  channelId: "1456744319972282449",},},channels: {discord: {  dmPolicy: "allowlist",  allowFrom: ["accessGroup:maintainers", "discord:123456789012345678"],},},}
[/code]

Consultas falham fechadas. Se o Discord retornar `Missing Access`, a consulta de membro falhar, ou o canal pertencer a uma guilda diferente, o remetente da DM é tratado como não autorizado.

Habilite o **Server Members Intent** no Portal do Desenvolvedor do Discord para o bot ao usar grupos de acesso por público de canal. DMs não incluem estado de membro de guilda, então o OpenClaw resolve o membro pela REST do Discord no momento da autorização.

### Guild policy

O tratamento de guildas é controlado por `channels.discord.groupPolicy`:

  * `open`
  * `allowlist`
  * `disabled`


A linha de base segura quando `channels.discord` existe é `allowlist`.

Comportamento de `allowlist`:

  * a guilda deve corresponder a `channels.discord.guilds` (`id` preferido, slug aceito)
  * listas de permissão opcionais de remetentes: `users` (IDs estáveis recomendados) e `roles` (somente IDs de função); se qualquer uma for configurada, remetentes são permitidos quando correspondem a `users` OU `roles`
  * correspondência direta de nome/tag é desabilitada por padrão; habilite `channels.discord.dangerouslyAllowNameMatching: true` apenas como modo de compatibilidade emergencial
  * nomes/tags são compatíveis com `users`, mas IDs são mais seguros; `openclaw security audit` alerta quando entradas de nome/tag são usadas
  * se uma guilda tiver `channels` configurado, canais não listados serão negados
  * se uma guilda não tiver bloco `channels`, todos os canais nessa guilda permitida serão permitidos


Exemplo:

json5Copy code
[code]
    {channels: {discord: {  groupPolicy: "allowlist",  guilds: {    "123456789012345678": {      requireMention: true,      ignoreOtherMentions: true,      users: ["987654321098765432"],      roles: ["123456789012345678"],      channels: {        general: { allow: true },        help: { allow: true, requireMention: true },      },    },  },},},}
[/code]

Se você definir apenas `DISCORD_BOT_TOKEN` e não criar um bloco `channels.discord`, o fallback em runtime é `groupPolicy="allowlist"` (com um aviso nos logs), mesmo que `channels.defaults.groupPolicy` seja `open`.

### Mentions and group DMs

Mensagens de guilda exigem menção por padrão.

A detecção de menções inclui:

  * menção explícita ao bot
  * padrões de menção configurados (`agents.list[].groupChat.mentionPatterns`, fallback `messages.groupChat.mentionPatterns`)
  * comportamento implícito de resposta ao bot em casos compatíveis


Ao escrever mensagens de saída do Discord, use a sintaxe canônica de menção: `<@USER_ID>` para usuários, `<#CHANNEL_ID>` para canais e `<@&ROLE_ID>` para funções. Não use a forma legada de menção de apelido `<@!USER_ID>`.

`requireMention` é configurado por guilda/canal (`channels.discord.guilds...`). `ignoreOtherMentions` opcionalmente descarta mensagens que mencionam outro usuário/função, mas não o bot (excluindo @everyone/@here).

DMs em grupo:

  * padrão: ignoradas (`dm.groupEnabled=false`)
  * lista de permissão opcional via `dm.groupChannels` (IDs de canal ou slugs)


### Roteamento de agente baseado em funções

Use `bindings[].match.roles` para rotear membros de guildas do Discord para diferentes agentes por ID de função. Bindings baseados em função aceitam apenas IDs de função e são avaliados depois de bindings de par ou par pai e antes de bindings somente de guilda. Se um binding também definir outros campos de correspondência (por exemplo, `peer` \+ `guildId` \+ `roles`), todos os campos configurados devem corresponder.

json5Copy code
[code]
    {  bindings: [    {      agentId: "opus",      match: {        channel: "discord",        guildId: "123456789012345678",        roles: ["111111111111111111"],      },    },    {      agentId: "sonnet",      match: {        channel: "discord",        guildId: "123456789012345678",      },    },  ],}
[/code]

## Comandos nativos e autenticação de comandos

  * `commands.native` usa `"auto"` como padrão e é habilitado para Discord.
  * Substituição por canal: `channels.discord.commands.native`.
  * `commands.native=false` ignora o registro e a limpeza de comandos de barra do Discord durante a inicialização. Comandos registrados anteriormente podem permanecer visíveis no Discord até que você os remova do app do Discord.
  * A autenticação de comandos nativos usa as mesmas listas de permissão/políticas do Discord que o processamento normal de mensagens.
  * Os comandos ainda podem ficar visíveis na interface do Discord para usuários que não estão autorizados; a execução ainda aplica a autenticação do OpenClaw e retorna "não autorizado".


Consulte [Comandos de barra](</pt-BR/tools/slash-commands>) para o catálogo e o comportamento dos comandos.

Configurações padrão de comandos de barra:

  * `ephemeral: true`


## Detalhes do recurso

Tags de resposta e respostas nativas

O Discord oferece suporte a tags de resposta na saída do agente:

  * `[[reply_to_current]]`
  * `[[reply_to:<id>]]`


Controlado por `channels.discord.replyToMode`:

  * `off` (padrão)
  * `first`
  * `all`
  * `batched`


Observação: `off` desabilita o encadeamento implícito de respostas. Tags explícitas `[[reply_to_*]]` ainda são respeitadas. `first` sempre anexa a referência implícita de resposta nativa à primeira mensagem de saída do Discord no turno. `batched` só anexa a referência implícita de resposta nativa do Discord quando o turno de entrada foi um lote com debounce de várias mensagens. Isso é útil quando você quer respostas nativas principalmente para conversas ambíguas em rajadas, não para cada turno de mensagem única.

IDs de mensagem são expostos no contexto/histórico para que agentes possam direcionar mensagens específicas.

Prévia de transmissão ao vivo

O OpenClaw pode transmitir rascunhos de respostas enviando uma mensagem temporária e editando-a conforme o texto chega. `channels.discord.streaming` aceita `off` | `partial` | `block` | `progress` (padrão). `progress` mantém um rascunho de status editável e o atualiza com o progresso das ferramentas até a entrega final; o rótulo inicial compartilhado é uma linha rotativa, então ele rola para fora como o restante quando trabalho suficiente aparece. `streamMode` é um alias legado de runtime. Execute `openclaw doctor --fix` para reescrever a configuração persistida para a chave canônica.

Defina `channels.discord.streaming.mode` como `off` para desabilitar edições de prévia no Discord. Se a transmissão em blocos do Discord estiver explicitamente habilitada, o OpenClaw ignora a transmissão de prévia para evitar transmissão dupla.

json5Copy code
[code]
    {channels: {discord: {  streaming: {    mode: "progress",    progress: {      label: "auto",      maxLines: 8,      toolProgress: true,    },  },},},}
[/code]

  * `partial` edita uma única mensagem de prévia conforme tokens chegam.
  * `block` emite partes do tamanho de rascunho (use `draftChunk` para ajustar tamanho e pontos de quebra, limitado por `textChunkLimit`).
  * Finais com mídia, erro e resposta explícita cancelam edições de prévia pendentes.
  * `streaming.preview.toolProgress` (padrão `true`) controla se atualizações de ferramenta/progresso reutilizam a mensagem de prévia.
  * Linhas de ferramenta/progresso são renderizadas como emoji compacto + título + detalhe quando disponível, por exemplo `🛠️ Bash: run tests` ou `🔎 Web Search: for "query"`.
  * `streaming.preview.commandText` / `streaming.progress.commandText` controla detalhes de comando/exec em linhas compactas de progresso: `raw` (padrão) ou `status` (somente rótulo da ferramenta).


Oculte texto bruto de comando/exec mantendo linhas compactas de progresso:

jsonCopy code
[code]
    {  "channels": {    "discord": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

A transmissão de prévia é somente texto; respostas com mídia voltam para a entrega normal. Quando a transmissão `block` está explicitamente habilitada, o OpenClaw ignora a transmissão de prévia para evitar transmissão dupla.

Histórico, contexto e comportamento de threads

Contexto de histórico de servidor:

  * `channels.discord.historyLimit` padrão `20`
  * fallback: `messages.groupChat.historyLimit`
  * `0` desabilita


Controles de histórico de DM:

  * `channels.discord.dmHistoryLimit`
  * `channels.discord.dms["<user_id>"].historyLimit`


Comportamento de threads:

  * Threads do Discord são roteadas como sessões de canal e herdam a configuração do canal pai, salvo substituição.
  * Sessões de thread herdam a seleção `/model` em nível de sessão do canal pai como fallback somente de modelo; seleções `/model` locais da thread ainda têm precedência e o histórico da transcrição pai não é copiado, a menos que a herança de transcrição esteja habilitada.
  * `channels.discord.thread.inheritParent` (padrão `false`) faz novas auto-threads iniciarem com base na transcrição pai. Substituições por conta ficam em `channels.discord.accounts.<id>.thread.inheritParent`.
  * Reações de ferramenta de mensagem podem resolver alvos de DM `user:<id>`.
  * `guilds.<guild>.channels.<channel>.requireMention: false` é preservado durante o fallback de ativação no estágio de resposta.


Tópicos de canal são injetados como contexto **não confiável**. Listas de permissão controlam quem pode acionar o agente, não são um limite completo de redação de contexto suplementar.

Sessões vinculadas a threads para subagentes

O Discord pode vincular uma thread a um alvo de sessão para que mensagens subsequentes nessa thread continuem sendo roteadas para a mesma sessão (incluindo sessões de subagente).

Comandos:

  * `/focus <target>` vincula a thread atual/nova a um alvo de subagente/sessão
  * `/unfocus` remove o vínculo da thread atual
  * `/agents` mostra execuções ativas e estado de vínculo
  * `/session idle <duration|off>` inspeciona/atualiza o auto-desfoque por inatividade para vínculos focados
  * `/session max-age <duration|off>` inspeciona/atualiza a idade máxima rígida para vínculos focados


Configuração:

json5Copy code
[code]
    {session: {threadBindings: {  enabled: true,  idleHours: 24,  maxAgeHours: 0,},},channels: {discord: {  threadBindings: {    enabled: true,    idleHours: 24,    maxAgeHours: 0,    spawnSessions: true,    defaultSpawnContext: "fork",  },},},}
[/code]

Observações:

  * `session.threadBindings.*` define padrões globais.
  * `channels.discord.threadBindings.*` substitui o comportamento do Discord.
  * `spawnSessions` controla criação/vínculo automático de threads para `sessions_spawn({ thread: true })` e criações de thread ACP. Padrão: `true`.
  * `defaultSpawnContext` controla o contexto nativo de subagente para criações vinculadas a thread. Padrão: `"fork"`.
  * Chaves obsoletas `spawnSubagentSessions`/`spawnAcpSessions` são migradas por `openclaw doctor --fix`.
  * Se vínculos de thread estiverem desabilitados para uma conta, `/focus` e operações relacionadas de vínculo de thread ficam indisponíveis.


Consulte [Subagentes](</pt-BR/tools/subagents>), [Agentes ACP](</pt-BR/tools/acp-agents>) e [Referência de configuração](</pt-BR/gateway/configuration-reference>).

Vínculos persistentes de canal ACP

Para espaços de trabalho ACP estáveis e "sempre ativos", configure vínculos ACP tipados de nível superior direcionados a conversas do Discord.

Caminho de configuração:

  * `bindings[]` com `type: "acp"` e `match.channel: "discord"`


Exemplo:

json5Copy code
[code]
    {agents: {list: [  {    id: "codex",    runtime: {      type: "acp",      acp: {        agent: "codex",        backend: "acpx",        mode: "persistent",        cwd: "/workspace/openclaw",      },    },  },],},bindings: [{  type: "acp",  agentId: "codex",  match: {    channel: "discord",    accountId: "default",    peer: { kind: "channel", id: "222222222222222222" },  },  acp: { label: "codex-main" },},],channels: {discord: {  guilds: {    "111111111111111111": {      channels: {        "222222222222222222": {          requireMention: false,        },      },    },  },},},}
[/code]

Observações:

  * `/acp spawn codex --bind here` vincula o canal ou a thread atual no local e mantém mensagens futuras na mesma sessão ACP. Mensagens de thread herdam o vínculo do canal pai.
  * Em um canal ou thread vinculado, `/new` e `/reset` redefinem a mesma sessão ACP no local. Vínculos temporários de thread podem substituir a resolução de alvo enquanto ativos.
  * `spawnSessions` controla a criação/vínculo de threads filhas via `--thread auto|here`.


Consulte [Agentes ACP](</pt-BR/tools/acp-agents>) para detalhes do comportamento de vínculo.

Notificações de reação

Modo de notificação de reação por servidor:

  * `off`
  * `own` (padrão)
  * `all`
  * `allowlist` (usa `guilds.<id>.users`)


Eventos de reação são transformados em eventos de sistema e anexados à sessão do Discord roteada.

Reações de confirmação

`ackReaction` envia um emoji de confirmação enquanto o OpenClaw processa uma mensagem de entrada.

Ordem de resolução:

  * `channels.discord.accounts.<accountId>.ackReaction`
  * `channels.discord.ackReaction`
  * `messages.ackReaction`
  * fallback de emoji da identidade do agente (`agents.list[].identity.emoji`, senão "👀")


Observações:

  * O Discord aceita emoji unicode ou nomes de emoji personalizados.
  * Use `""` para desabilitar a reação para um canal ou conta.

Gravações de configuração

Gravações de configuração iniciadas pelo canal são habilitadas por padrão.

Isso afeta fluxos `/config set|unset` (quando os recursos de comando estão habilitados).

Desabilitar:

json5Copy code
[code]
    {channels: {discord: {  configWrites: false,},},}
[/code]

Proxy do Gateway

Roteie tráfego WebSocket do Gateway do Discord e consultas REST de inicialização (ID do aplicativo + resolução de lista de permissão) por meio de um proxy HTTP(S) com `channels.discord.proxy`.

json5Copy code
[code]
    {channels: {discord: {  proxy: "http://proxy.example:8080",},},}
[/code]

Substituição por conta:

json5Copy code
[code]
    {channels: {discord: {  accounts: {    primary: {      proxy: "http://proxy.example:8080",    },  },},},}
[/code]

Suporte a PluralKit

Habilite a resolução do PluralKit para mapear mensagens com proxy para a identidade de membro do sistema:

json5Copy code
[code]
    {channels: {discord: {  pluralkit: {    enabled: true,    token: "pk_live_...", // optional; needed for private systems  },},},}
[/code]

Observações:

  * listas de permissão podem usar `pk:<memberId>`
  * nomes de exibição de membros são correspondidos por nome/slug somente quando `channels.discord.dangerouslyAllowNameMatching: true`
  * consultas usam o ID da mensagem original e são restritas por janela de tempo
  * se a consulta falhar, mensagens com proxy são tratadas como mensagens de bot e descartadas, a menos que `allowBots=true`

Aliases de menção de saída

Use `mentionAliases` quando agentes precisarem de menções de saída determinísticas para usuários conhecidos do Discord. Chaves são identificadores sem o `@` inicial; valores são IDs de usuário do Discord. Identificadores desconhecidos, `@everyone`, `@here` e menções dentro de spans de código Markdown são deixados inalterados.

json5Copy code
[code]
    {channels: {discord: {  mentionAliases: {    Vladislava: "123456789012345678",  },  accounts: {    ops: {      mentionAliases: {        OpsLead: "234567890123456789",      },    },  },},},}
[/code]

Configuração de presença

Atualizações de presença são aplicadas quando você define um campo de status ou atividade, ou quando habilita presença automática.

Exemplo somente de status:

json5Copy code
[code]
    {channels: {discord: {  status: "idle",},},}
[/code]

Exemplo de atividade (status personalizado é o tipo de atividade padrão):

json5Copy code
[code]
    {channels: {discord: {  activity: "Focus time",  activityType: 4,},},}
[/code]

Exemplo de transmissão:

json5Copy code
[code]
    {channels: {discord: {  activity: "Live coding",  activityType: 1,  activityUrl: "https://twitch.tv/openclaw",},},}
[/code]

Mapa de tipos de atividade:

  * 0: Jogando
  * 1: Transmitindo (requer `activityUrl`)
  * 2: Ouvindo
  * 3: Assistindo
  * 4: Personalizado (usa o texto da atividade como o estado do status; emoji é opcional)
  * 5: Competindo


Exemplo de presença automática (sinal de integridade em tempo de execução):

json5Copy code
[code]
    {channels: {discord: {  autoPresence: {    enabled: true,    intervalMs: 30000,    minUpdateIntervalMs: 15000,    exhaustedText: "token exhausted",  },},},}
[/code]

A presença automática mapeia a disponibilidade em tempo de execução para o status do Discord: íntegro => online, degradado ou desconhecido => idle, esgotado ou indisponível => dnd. Substituições de texto opcionais:

  * `autoPresence.healthyText`
  * `autoPresence.degradedText`
  * `autoPresence.exhaustedText` (compatível com o placeholder `{reason}`)

Aprovações no Discord

O Discord oferece suporte ao tratamento de aprovações baseado em botões em DMs e pode, opcionalmente, publicar solicitações de aprovação no canal de origem.

Caminho de configuração:

  * `channels.discord.execApprovals.enabled`
  * `channels.discord.execApprovals.approvers` (opcional; recorre a `commands.ownerAllowFrom` quando possível)
  * `channels.discord.execApprovals.target` (`dm` | `channel` | `both`, padrão: `dm`)
  * `agentFilter`, `sessionFilter`, `cleanupAfterResolve`


O Discord habilita automaticamente aprovações de execução nativas quando `enabled` não está definido ou é `"auto"` e pelo menos um aprovador pode ser resolvido, seja por `execApprovals.approvers` ou por `commands.ownerAllowFrom`. O Discord não infere aprovadores de execução a partir de `allowFrom` do canal, `dm.allowFrom` legado ou `defaultTo` de mensagem direta. Defina `enabled: false` para desabilitar explicitamente o Discord como cliente de aprovação nativo.

Para comandos de grupo confidenciais restritos ao proprietário, como `/diagnostics` e `/export-trajectory`, o OpenClaw envia solicitações de aprovação e resultados finais de forma privada. Ele tenta primeiro a DM do Discord quando o proprietário que invocou o comando tem uma rota de proprietário do Discord; se isso não estiver disponível, recorre à primeira rota de proprietário disponível em `commands.ownerAllowFrom`, como Telegram.

Quando `target` é `channel` ou `both`, a solicitação de aprovação fica visível no canal. Apenas aprovadores resolvidos podem usar os botões; outros usuários recebem uma negação efêmera. As solicitações de aprovação incluem o texto do comando, portanto habilite a entrega no canal apenas em canais confiáveis. Se o ID do canal não puder ser derivado da chave da sessão, o OpenClaw recorre à entrega por DM.

O Discord também renderiza os botões de aprovação compartilhados usados por outros canais de chat. O adaptador nativo do Discord adiciona principalmente roteamento de DMs para aprovadores e distribuição para canais. Quando esses botões estão presentes, eles são a UX de aprovação principal; o OpenClaw deve incluir um comando manual `/approve` somente quando o resultado da ferramenta indicar que aprovações por chat estão indisponíveis ou que a aprovação manual é o único caminho. Se o runtime de aprovação nativa do Discord não estiver ativo, o OpenClaw mantém o prompt determinístico local `/approve <id> <decision>` visível. Se o runtime estiver ativo, mas um cartão nativo não puder ser entregue a nenhum destino, o OpenClaw envia um aviso de fallback no mesmo chat com o comando `/approve` exato da aprovação pendente.

A autenticação do Gateway e a resolução de aprovações seguem o contrato compartilhado do cliente Gateway (IDs `plugin:` são resolvidos por `plugin.approval.resolve`; outros IDs por `exec.approval.resolve`). As aprovações expiram após 30 minutos por padrão.

Consulte [Aprovações de execução](</pt-BR/tools/exec-approvals>).

## Ferramentas e barreiras de ação

As ações de mensagem do Discord incluem ações de mensagens, administração de canais, moderação, presença e metadados.

Exemplos principais:

  * mensagens: `sendMessage`, `readMessages`, `editMessage`, `deleteMessage`, `threadReply`
  * reações: `react`, `reactions`, `emojiList`
  * moderação: `timeout`, `kick`, `ban`
  * presença: `setPresence`


A ação `event-create` aceita um parâmetro opcional `image` (URL ou caminho de arquivo local) para definir a imagem de capa do evento agendado.

As barreiras de ação ficam em `channels.discord.actions.*`.

Comportamento padrão das barreiras:

Grupo de ações | Padrão  
---|---  
reactions, messages, threads, pins, polls, search, memberInfo, roleInfo, channelInfo, channels, voiceStatus, events, stickers, emojiUploads, stickerUploads, permissions | habilitado  
roles | desabilitado  
moderation | desabilitado  
presence | desabilitado  
  
## UI de componentes v2

O OpenClaw usa componentes v2 do Discord para aprovações de execução e marcadores entre contextos. As ações de mensagem do Discord também podem aceitar `components` para UI personalizada (avançado; requer a construção de um payload de componente pela ferramenta discord), enquanto `embeds` legados continuam disponíveis, mas não são recomendados.

  * `channels.discord.ui.components.accentColor` define a cor de destaque usada pelos contêineres de componentes do Discord (hex).
  * Defina por conta com `channels.discord.accounts.<id>.ui.components.accentColor`.
  * `embeds` são ignorados quando componentes v2 estão presentes.


Exemplo:

json5Copy code
[code]
    {  channels: {    discord: {      ui: {        components: {          accentColor: "#5865F2",        },      },    },  },}
[/code]

## Voz

O Discord tem duas superfícies de voz distintas: **canais de voz** em tempo real (conversas contínuas) e **anexos de mensagem de voz** (o formato de prévia com forma de onda). O Gateway oferece suporte a ambas.

### Canais de voz

Checklist de configuração:

  1. Habilite Message Content Intent no Discord Developer Portal.
  2. Habilite Server Members Intent quando listas de permissão de funções/usuários forem usadas.
  3. Convide o bot com os escopos `bot` e `applications.commands`.
  4. Conceda Connect, Speak, Send Messages e Read Message History no canal de voz de destino.
  5. Habilite comandos nativos (`commands.native` ou `channels.discord.commands.native`).
  6. Configure `channels.discord.voice`.


Use `/vc join|leave|status` para controlar sessões. O comando usa o agente padrão da conta e segue as mesmas regras de lista de permissão e política de grupo que outros comandos do Discord.

bashCopy code
[code]
    /vc join channel:<voice-channel-id>/vc status/vc leave
[/code]

Para inspecionar as permissões efetivas do bot antes de entrar, execute:

bashCopy code
[code]
    openclaw channels capabilities --channel discord --target channel:<voice-channel-id>
[/code]

Exemplo de entrada automática:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        model: "openai-codex/gpt-5.5",        autoJoin: [          {            guildId: "123456789012345678",            channelId: "234567890123456789",          },        ],        allowedChannels: [          {            guildId: "123456789012345678",            channelId: "234567890123456789",          },        ],        daveEncryption: true,        decryptionFailureTolerance: 24,        connectTimeoutMs: 30000,        reconnectGraceMs: 15000,        realtime: {          provider: "openai",          model: "gpt-realtime-2",          voice: "cedar",        },      },    },  },}
[/code]

Observações:

  * `voice.tts` substitui `messages.tts` apenas para reprodução de voz `stt-tts`. Modos em tempo real usam `voice.realtime.voice`.
  * `voice.mode` controla o caminho da conversa. O padrão é `agent-proxy`: um front-end de voz em tempo real gerencia temporização de turno, interrupção e reprodução, delega o trabalho substantivo ao agente OpenClaw roteado por meio de `openclaw_agent_consult` e trata o resultado como um prompt digitado no Discord por aquele falante. `stt-tts` mantém o fluxo em lote mais antigo de STT mais TTS. `bidi` permite que o modelo em tempo real converse diretamente enquanto expõe `openclaw_agent_consult` para o cérebro do OpenClaw.
  * `voice.agentSession` controla qual conversa do OpenClaw recebe turnos de voz. Deixe-o sem definir para a sessão própria do canal de voz, ou defina `{ mode: "target", target: "channel:<text-channel-id>" }` para fazer o canal de voz atuar como a extensão de microfone/alto-falante de uma sessão existente de canal de texto do Discord, como `#maintainers`.
  * `voice.model` substitui o cérebro do agente OpenClaw para respostas de voz do Discord e consultas em tempo real. Deixe-o sem definir para herdar o modelo do agente roteado. Ele é separado de `voice.realtime.model`.
  * `agent-proxy` roteia fala por `discord-voice`, que preserva a autorização normal de proprietário/ferramenta para o falante e a sessão de destino, mas oculta a ferramenta `tts` do agente porque a voz do Discord é responsável pela reprodução. Por padrão, `agent-proxy` concede à consulta acesso total a ferramentas equivalente ao de proprietário para falantes proprietários (`voice.realtime.toolPolicy: "owner"`) e prefere fortemente consultar o agente OpenClaw antes de respostas substantivas (`voice.realtime.consultPolicy: "always"`). Nesse modo padrão `always`, a camada em tempo real não fala automaticamente preenchimentos antes da resposta da consulta; ela captura e transcreve a fala, então fala a resposta roteada do OpenClaw. Se várias respostas de consulta forçada terminarem enquanto o Discord ainda estiver reproduzindo a primeira resposta, respostas posteriores de fala exata serão enfileiradas até a reprodução ficar ociosa, em vez de substituir a fala no meio da frase.
  * No modo `stt-tts`, STT usa `tools.media.audio`; `voice.model` não afeta a transcrição.
  * Em modos em tempo real, `voice.realtime.provider`, `voice.realtime.model` e `voice.realtime.voice` configuram a sessão de áudio em tempo real. Para OpenAI Realtime 2 mais o cérebro Codex, use `voice.realtime.model: "gpt-realtime-2"` e `voice.model: "openai-codex/gpt-5.5"`.
  * O provedor em tempo real da OpenAI aceita os nomes de evento atuais do Realtime 2 e aliases legados compatíveis com Codex para eventos de áudio de saída e transcrição, para que snapshots compatíveis do provedor possam divergir sem descartar áudio do assistente.
  * `voice.realtime.bargeIn` controla se eventos de início de fala do Discord interrompem reprodução ativa em tempo real. Se não definido, ele segue a configuração de interrupção de áudio de entrada do provedor em tempo real.
  * `voice.realtime.minBargeInAudioEndMs` controla a duração mínima da reprodução do assistente antes que um barge-in em tempo real da OpenAI trunque o áudio. Padrão: `250`. Defina `0` para interrupção imediata em salas com pouco eco, ou aumente para configurações de alto-falantes com muito eco.
  * Para uma voz OpenAI na reprodução do Discord, defina `voice.tts.provider: "openai"` e escolha uma voz de conversão de texto em fala em `voice.tts.openai.voice` ou `voice.tts.providers.openai.voice`. `cedar` é uma boa escolha com som masculino no modelo TTS atual da OpenAI.
  * Substituições de `systemPrompt` do Discord por canal se aplicam a turnos de transcrição de voz para esse canal de voz.
  * Turnos de transcrição de voz derivam o status de proprietário de `allowFrom` do Discord (ou `dm.allowFrom`); falantes não proprietários não podem acessar ferramentas exclusivas de proprietário (por exemplo, `gateway` e `cron`).
  * Voz do Discord é opcional para configurações apenas de texto; defina `channels.discord.voice.enabled=true` (ou mantenha um bloco existente `channels.discord.voice`) para habilitar comandos `/vc`, o runtime de voz e a intenção de Gateway `GuildVoiceStates`.
  * `channels.discord.intents.voiceStates` pode substituir explicitamente a assinatura de intenção de estado de voz. Deixe-o sem definir para que a intenção siga a ativação efetiva de voz.
  * Se `voice.autoJoin` tiver várias entradas para o mesmo servidor, o OpenClaw entrará no último canal configurado para esse servidor.
  * `voice.allowedChannels` é uma allowlist opcional de residência. Deixe-o sem definir para permitir `/vc join` em qualquer canal de voz autorizado do Discord. Quando definido, `/vc join`, entrada automática na inicialização e movimentos de estado de voz do bot são restritos às entradas `{ guildId, channelId }` listadas. Defina como um array vazio para negar todas as entradas em voz do Discord. Se o Discord mover o bot para fora da allowlist, o OpenClaw sai desse canal e entra novamente no destino de entrada automática configurado quando houver um disponível.
  * `voice.daveEncryption` e `voice.decryptionFailureTolerance` são repassados para as opções de entrada de `@discordjs/voice`.
  * Os padrões de `@discordjs/voice` são `daveEncryption=true` e `decryptionFailureTolerance=24` se não definidos.
  * O OpenClaw usa por padrão o decodificador `opusscript` em JS puro para recebimento de voz do Discord. O pacote nativo opcional `@discordjs/opus` é ignorado pela política de instalação pnpm do repositório para que instalações normais, lanes Docker e testes não relacionados não compilem um addon nativo. Hosts dedicados a desempenho de voz podem optar por usá-lo com `OPENCLAW_DISCORD_OPUS_DECODER=native` após instalar o addon nativo.
  * `voice.connectTimeoutMs` controla a espera inicial por Ready do `@discordjs/voice` para tentativas de `/vc join` e entrada automática. Padrão: `30000`.
  * `voice.reconnectGraceMs` controla por quanto tempo o OpenClaw espera que uma sessão de voz desconectada comece a reconectar antes de destruí-la. Padrão: `15000`.
  * No modo `stt-tts`, a reprodução de voz não para só porque outro usuário começou a falar. Para evitar loops de feedback, o OpenClaw ignora nova captura de voz enquanto o TTS está sendo reproduzido; fale após a reprodução terminar para o próximo turno. Modos em tempo real encaminham inícios de fala como sinais de barge-in para o provedor em tempo real.
  * Em modos em tempo real, eco de alto-falantes em um microfone aberto pode parecer barge-in e interromper a reprodução. Para salas do Discord com muito eco, defina `voice.realtime.providers.openai.interruptResponseOnInputAudio: false` para impedir que a OpenAI interrompa automaticamente com áudio de entrada. Adicione `voice.realtime.bargeIn: true` se você ainda quiser que eventos de início de fala do Discord interrompam a reprodução ativa. A ponte em tempo real da OpenAI ignora truncamentos de reprodução menores que `voice.realtime.minBargeInAudioEndMs` como provável eco/ruído e os registra como ignorados em vez de limpar a reprodução do Discord.
  * `voice.captureSilenceGraceMs` controla por quanto tempo o OpenClaw espera depois que o Discord informa que um falante parou antes de finalizar esse segmento de áudio para STT. Padrão: `2500`; aumente isso se o Discord dividir pausas normais em transcrições parciais fragmentadas.
  * Quando ElevenLabs é o provedor TTS selecionado, a reprodução de voz do Discord usa TTS em streaming e começa a partir do stream de resposta do provedor. Provedores sem suporte a streaming fazem fallback para o caminho de arquivo temporário sintetizado.
  * O OpenClaw também monitora falhas de descriptografia de recebimento e se recupera automaticamente saindo e entrando novamente no canal de voz após falhas repetidas em uma janela curta.
  * Se logs de recebimento mostrarem repetidamente `DecryptionFailed(UnencryptedWhenPassthroughDisabled)` após atualizar, colete um relatório de dependências e logs. A linha `@discordjs/voice` incluída contém a correção upstream de preenchimento do PR #11449 do discord.js, que fechou a issue #11419 do discord.js.
  * Eventos de recebimento `The operation was aborted` são esperados quando o OpenClaw finaliza um segmento de falante capturado; são diagnósticos verbosos, não avisos.
  * Logs verbosos de voz do Discord incluem uma prévia limitada de uma linha da transcrição STT para cada segmento de falante aceito, então a depuração mostra tanto o lado do usuário quanto o lado da resposta do agente sem despejar texto de transcrição ilimitado.
  * No modo `agent-proxy`, o fallback de consulta forçada ignora fragmentos de transcrição provavelmente incompletos, como texto terminando em `...` ou um conector final como `and`, além de encerramentos obviamente não acionáveis como “já volto” ou “tchau”. Os logs mostram `forced agent consult skipped reason=...` quando isso impede uma resposta enfileirada obsoleta.


Configuração nativa do opus para checkouts de código-fonte:

bashCopy code
[code]
    pnpm installmise exec node@22 -- pnpm discord:opus:install
[/code]

Use Node 22 para o Gateway quando quiser o addon nativo precompilado upstream para macOS arm64. Se você usar outro runtime Node, o instalador opcional pode precisar de uma cadeia de ferramentas local de build a partir do código-fonte com `node-gyp`.

Após instalar o addon nativo, inicie o Gateway com:

bashCopy code
[code]
    OPENCLAW_DISCORD_OPUS_DECODER=native pnpm gateway:watch
[/code]

Logs verbosos de voz devem mostrar `discord voice: opus decoder: @discordjs/opus`. Sem a opção por env, ou se o addon nativo estiver ausente ou não puder ser carregado no host, o OpenClaw registra `discord voice: opus decoder: opusscript` e continua recebendo voz pelo fallback em JS puro.

Pipeline STT mais TTS:

  * A captura PCM do Discord é convertida em um arquivo temporário WAV.
  * `tools.media.audio` lida com STT, por exemplo `openai/gpt-4o-mini-transcribe`.
  * A transcrição é enviada pelo ingresso e roteamento do Discord enquanto o LLM de resposta executa com uma política de saída de voz que oculta a ferramenta `tts` do agente e solicita texto retornado, porque a voz do Discord é responsável pela reprodução final de TTS.
  * `voice.model`, quando definido, substitui apenas o LLM de resposta para este turno de canal de voz.
  * `voice.tts` é mesclado sobre `messages.tts`; provedores compatíveis com streaming alimentam o player diretamente, caso contrário o arquivo de áudio resultante é reproduzido no canal conectado.


Exemplo de sessão de canal de voz agent-proxy padrão:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        model: "openai-codex/gpt-5.5",        realtime: {          provider: "openai",          model: "gpt-realtime-2",          voice: "cedar",        },      },    },  },}
[/code]

Sem bloco `voice.agentSession`, cada canal de voz recebe sua própria sessão roteada do OpenClaw. Por exemplo, `/vc join channel:234567890123456789` fala com a sessão desse canal de voz do Discord. O modelo em tempo real é apenas o front-end de voz; solicitações substantivas são entregues ao agente OpenClaw configurado. Se o modelo em tempo real produzir uma transcrição final sem chamar a ferramenta de consulta, o OpenClaw força a consulta como fallback para que o padrão ainda se comporte como falar com o agente.

Exemplo legado de STT mais TTS:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        mode: "stt-tts",        model: "openai/gpt-5.4-mini",        tts: {          provider: "openai",          openai: {            model: "gpt-4o-mini-tts",            voice: "cedar",          },        },      },    },  },}
[/code]

Exemplo bidi em tempo real:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        mode: "bidi",        model: "openai-codex/gpt-5.5",        realtime: {          provider: "openai",          model: "gpt-realtime-2",          voice: "cedar",          toolPolicy: "safe-read-only",          consultPolicy: "always",        },      },    },  },}
[/code]

Voz como extensão de uma sessão de canal existente do Discord:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        mode: "agent-proxy",        model: "openai-codex/gpt-5.5",        agentSession: {          mode: "target",          target: "channel:123456789012345678",        },        realtime: {          provider: "openai",          model: "gpt-realtime-2",          voice: "cedar",        },      },    },  },}
[/code]

No modo `agent-proxy`, o bot entra no canal de voz configurado, mas os turnos do agente OpenClaw usam a sessão roteada normal e o agente do canal de destino. A sessão de voz em tempo real fala o resultado retornado de volta no canal de voz. O agente supervisor ainda pode usar ferramentas normais de mensagem de acordo com sua política de ferramentas, incluindo enviar uma mensagem separada no Discord se essa for a ação correta.

Formas de destino úteis:

  * `target: "channel:123456789012345678"` roteia por uma sessão de canal de texto do Discord.
  * `target: "123456789012345678"` é tratado como um destino de canal.
  * `target: "dm:123456789012345678"` ou `target: "user:123456789012345678"` roteia por essa sessão de mensagem direta.


Exemplo OpenAI Realtime com muito eco:

json5Copy code
[code]
    {  channels: {    discord: {      voice: {        enabled: true,        mode: "bidi",        model: "openai-codex/gpt-5.5",        realtime: {          provider: "openai",          model: "gpt-realtime-2",          voice: "cedar",          bargeIn: true,          minBargeInAudioEndMs: 500,          consultPolicy: "always",          providers: {            openai: {              interruptResponseOnInputAudio: false,            },          },        },      },    },  },}
[/code]

Use isto quando o modelo escuta a própria reprodução do Discord por um microfone aberto, mas você ainda quer interrompê-lo falando. O OpenClaw impede que a OpenAI interrompa automaticamente com áudio de entrada bruto, enquanto `bargeIn: true` permite que eventos de início de fala do Discord e áudio de falante já ativo cancelem respostas em tempo real ativas antes que o próximo turno capturado chegue à OpenAI. Sinais de interrupção por fala muito iniciais com `audioEndMs` abaixo de `minBargeInAudioEndMs` são tratados como provável eco/ruído e ignorados para que o modelo não seja cortado no primeiro quadro de reprodução.

Logs de voz esperados:

  * Ao entrar: `discord voice: joining ... voiceSession=... supervisorSession=... agentSessionMode=... voiceModel=... realtimeModel=...`
  * Ao iniciar o tempo real: `discord voice: realtime bridge starting ... autoRespond=false interruptResponse=false bargeIn=false minBargeInAudioEndMs=...`
  * Em áudio do falante: `discord voice: realtime speaker turn opened ...`, `discord voice: realtime input audio started ... outputAudioMs=... outputActive=...` e `discord voice: realtime speaker turn closed ... chunks=... discordBytes=... realtimeBytes=... interruptedPlayback=...`
  * Em fala obsoleta ignorada: `discord voice: realtime forced agent consult skipped reason=incomplete-transcript ...` ou `reason=non-actionable-closing ...`
  * Na conclusão da resposta em tempo real: `discord voice: realtime audio playback finishing reason=response.done ... audioMs=... chunks=...`
  * Na parada/redefinição da reprodução: `discord voice: realtime audio playback stopped reason=... audioMs=... elapsedMs=... chunks=...`
  * Na consulta em tempo real: `discord voice: realtime consult requested ... voiceSession=... supervisorSession=... question=...`
  * Na resposta do agente: `discord voice: agent turn answer ...`
  * Em fala exata enfileirada: `discord voice: realtime exact speech queued ... queued=... outputAudioMs=... outputActive=...`, seguido por `discord voice: realtime exact speech dequeued reason=player-idle ...`
  * Na detecção de interrupção por fala: `discord voice: realtime barge-in detected source=speaker-start ...` ou `discord voice: realtime barge-in detected source=active-speaker-audio ...`, seguido por `discord voice: realtime barge-in requested reason=... outputAudioMs=... outputActive=...`
  * Na interrupção em tempo real: `discord voice: realtime model interrupt requested client:response.cancel reason=barge-in`, seguido por `discord voice: realtime model audio truncated client:conversation.item.truncate reason=barge-in audioEndMs=...` ou `discord voice: realtime model interrupt confirmed server:response.done status=cancelled ...`
  * Em eco/ruído ignorado: `discord voice: realtime model interrupt ignored client:conversation.item.truncate.skipped reason=barge-in audioEndMs=0 minAudioEndMs=250`
  * Com interrupção por fala desativada: `discord voice: realtime capture ignored during playback (barge-in disabled) ...`
  * Em reprodução ociosa: `discord voice: realtime barge-in ignored reason=... outputActive=false ... playbackChunks=0`


Para depurar áudio cortado, leia os logs de voz em tempo real como uma linha do tempo:

  1. `realtime audio playback started` significa que o Discord começou a reproduzir o áudio do assistente. A ponte começa a contar os blocos de saída do assistente, os bytes PCM do Discord, os bytes em tempo real do provedor e a duração do áudio sintetizado a partir desse ponto.
  2. `realtime speaker turn opened` marca um falante do Discord ficando ativo. Se a reprodução já estiver ativa e `bargeIn` estiver habilitado, isso pode ser seguido por `barge-in detected source=speaker-start`.
  3. `realtime input audio started` marca o primeiro quadro de áudio real recebido para esse turno do falante. `outputActive=true` ou um `outputAudioMs` diferente de zero aqui significa que o microfone está enviando entrada enquanto a reprodução do assistente ainda está ativa.
  4. `barge-in detected source=active-speaker-audio` significa que o OpenClaw viu áudio de falante ao vivo enquanto a reprodução do assistente estava ativa. Isso é útil para distinguir uma interrupção real de um evento de início de fala do Discord sem áudio útil.
  5. `barge-in requested reason=...` significa que o OpenClaw pediu ao provedor em tempo real para cancelar ou truncar a resposta ativa. Ele inclui `outputAudioMs`, `outputActive` e `playbackChunks` para que você possa ver quanto áudio do assistente realmente tinha sido reproduzido antes da interrupção.
  6. `realtime audio playback stopped reason=...` é o ponto local de redefinição da reprodução do Discord. O motivo diz quem parou a reprodução: `barge-in`, `player-idle`, `provider-clear-audio`, `forced-agent-consult`, `stream-close` ou `session-close`.
  7. `realtime speaker turn closed` resume o turno de entrada capturado. `chunks=0` ou `hasAudio=false` significa que o turno do falante abriu, mas nenhum áudio utilizável chegou à ponte em tempo real. `interruptedPlayback=true` significa que esse turno de entrada se sobrepôs à saída do assistente e acionou a lógica de interrupção por fala.


Campos úteis:

  * `outputAudioMs`: duração do áudio do assistente gerado pelo provedor em tempo real antes da linha de log.
  * `audioMs`: duração do áudio do assistente que o OpenClaw contou antes da reprodução parar.
  * `elapsedMs`: tempo decorrido de relógio entre abrir e fechar o fluxo de reprodução ou o turno do falante.
  * `discordBytes`: bytes PCM estéreo de 48 kHz enviados para ou recebidos da voz do Discord.
  * `realtimeBytes`: bytes PCM no formato do provedor enviados para ou recebidos do provedor em tempo real.
  * `playbackChunks`: blocos de áudio do assistente encaminhados para o Discord para a resposta ativa.
  * `sinceLastAudioMs`: intervalo entre o último quadro de áudio do falante capturado e o fechamento do turno do falante.


Padrões comuns:

  * Corte imediato com `source=active-speaker-audio`, `outputAudioMs` pequeno e o mesmo usuário por perto geralmente indica eco do alto-falante entrando no microfone. Aumente `voice.realtime.minBargeInAudioEndMs`, reduza o volume do alto-falante, use fones de ouvido ou defina `voice.realtime.providers.openai.interruptResponseOnInputAudio: false`.
  * `source=speaker-start` seguido por `speaker turn closed ... hasAudio=false` significa que o Discord relatou um início de fala, mas nenhum áudio chegou ao OpenClaw. Isso pode ser um evento transitório de voz do Discord, comportamento de porta de ruído ou um cliente acionando brevemente o microfone.
  * `audio playback stopped reason=stream-close` sem uma interrupção por fala próxima ou `provider-clear-audio` significa que o fluxo local de reprodução do Discord terminou inesperadamente. Verifique os logs anteriores do provedor e do player do Discord.
  * `capture ignored during playback (barge-in disabled)` significa que o OpenClaw descartou intencionalmente a entrada enquanto o áudio do assistente estava ativo. Habilite `voice.realtime.bargeIn` se quiser que a fala interrompa a reprodução.
  * `barge-in ignored ... outputActive=false` significa que o VAD do Discord ou do provedor relatou fala, mas o OpenClaw não tinha reprodução ativa para interromper. Isso não deve cortar o áudio.


As credenciais são resolvidas por componente: autenticação da rota LLM para `voice.model`, autenticação STT para `tools.media.audio`, autenticação TTS para `messages.tts`/`voice.tts` e autenticação do provedor em tempo real para `voice.realtime.providers` ou a configuração normal de autenticação do provedor.

### Mensagens de voz

Mensagens de voz do Discord mostram uma prévia de forma de onda e exigem áudio OGG/Opus. O OpenClaw gera a forma de onda automaticamente, mas precisa de `ffmpeg` e `ffprobe` no host do gateway para inspecionar e converter.

  * Forneça um **caminho de arquivo local** (URLs são rejeitadas).
  * Omita o conteúdo de texto (o Discord rejeita texto + mensagem de voz na mesma carga).
  * Qualquer formato de áudio é aceito; o OpenClaw converte para OGG/Opus conforme necessário.

bashCopy code
[code]
    message(action="send", channel="discord", target="channel:123", path="/path/to/audio.mp3", asVoice=true)
[/code]

## Solução de problemas

Intents não permitidas usadas ou bot não vê mensagens da guilda

  * habilite Message Content Intent
  * habilite Server Members Intent quando você depender da resolução de usuário/membro
  * reinicie o gateway depois de alterar intents

Mensagens da guilda bloqueadas inesperadamente

  * verifique `groupPolicy`
  * verifique a lista de permissões de guildas em `channels.discord.guilds`
  * se o mapa `channels` da guilda existir, apenas os canais listados serão permitidos
  * verifique o comportamento de `requireMention` e os padrões de menção


Verificações úteis:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probeopenclaw logs --follow
[/code]

Require mention false, mas ainda bloqueado

Causas comuns:

  * `groupPolicy="allowlist"` sem lista de permissões de guilda/canal correspondente
  * `requireMention` configurado no lugar errado (deve ficar em `channels.discord.guilds` ou na entrada do canal)
  * remetente bloqueado pela lista de permissões `users` da guilda/canal

Turnos longos do Discord ou respostas duplicadas

Logs típicos:

  * `Slow listener detected ...`
  * `stuck session: sessionKey=agent:...:discord:... state=processing ...`


Ajustes da fila do Gateway do Discord:

  * conta única: `channels.discord.eventQueue.listenerTimeout`
  * várias contas: `channels.discord.accounts.<accountId>.eventQueue.listenerTimeout`
  * isso controla apenas o trabalho do listener do Gateway do Discord, não a duração do turno do agente


O Discord não aplica um tempo limite pertencente ao canal a turnos de agente enfileirados. Listeners de mensagem repassam imediatamente, e execuções enfileiradas do Discord preservam a ordenação por sessão até que o ciclo de vida de sessão/ferramenta/runtime conclua ou aborte o trabalho.

json5Copy code
[code]
    {channels: {discord: {  accounts: {    default: {      eventQueue: {        listenerTimeout: 120000,      },    },  },},},}
[/code]

Avisos de tempo limite na busca de metadados do Gateway

O OpenClaw busca metadados de `/gateway/bot` do Discord antes de conectar. Falhas transitórias voltam para a URL padrão do Gateway do Discord e são limitadas por taxa nos logs.

Ajustes de tempo limite de metadados:

  * conta única: `channels.discord.gatewayInfoTimeoutMs`
  * várias contas: `channels.discord.accounts.<accountId>.gatewayInfoTimeoutMs`
  * fallback de env quando a configuração não está definida: `OPENCLAW_DISCORD_GATEWAY_INFO_TIMEOUT_MS`
  * padrão: `30000` (30 segundos), máximo: `120000`

Reinicializações por tempo limite READY do Gateway

O OpenClaw espera pelo evento `READY` do Gateway do Discord durante a inicialização e após reconexões em runtime. Configurações com várias contas e escalonamento de inicialização podem precisar de uma janela READY de inicialização mais longa que o padrão.

Ajustes de tempo limite READY:

  * inicialização com conta única: `channels.discord.gatewayReadyTimeoutMs`
  * inicialização com várias contas: `channels.discord.accounts.<accountId>.gatewayReadyTimeoutMs`
  * fallback de env na inicialização quando a configuração não está definida: `OPENCLAW_DISCORD_READY_TIMEOUT_MS`
  * padrão de inicialização: `15000` (15 segundos), máximo: `120000`
  * runtime com conta única: `channels.discord.gatewayRuntimeReadyTimeoutMs`
  * runtime com várias contas: `channels.discord.accounts.<accountId>.gatewayRuntimeReadyTimeoutMs`
  * fallback de env em runtime quando a configuração não está definida: `OPENCLAW_DISCORD_RUNTIME_READY_TIMEOUT_MS`
  * padrão de runtime: `30000` (30 segundos), máximo: `120000`

Incompatibilidades na auditoria de permissões

Verificações de permissão de `channels status --probe` só funcionam para IDs numéricos de canal.

Se você usa chaves de slug, a correspondência em runtime ainda pode funcionar, mas a sondagem não consegue verificar totalmente as permissões.

Problemas de DM e pareamento

  * DM desativada: `channels.discord.dm.enabled=false`
  * política de DM desativada: `channels.discord.dmPolicy="disabled"` (legado: `channels.discord.dm.policy`)
  * aguardando aprovação de pareamento no modo `pairing`

Loops de bot para bot

Por padrão, mensagens criadas por bots são ignoradas.

Se você definir `channels.discord.allowBots=true`, use regras rígidas de menção e lista de permissões para evitar comportamento de loop. Prefira `channels.discord.allowBots="mentions"` para aceitar somente mensagens de bots que mencionem o bot.

json5Copy code
[code]
    {channels: {discord: {  accounts: {    mantis: {      // Mantis listens to other bots only when they mention her.      allowBots: "mentions",    },    molty: {      // Molty listens to all bot-authored Discord messages.      allowBots: true,      mentionAliases: {        // Lets Molty write "@Mantis" and send a real Discord mention.        Mantis: "MANTIS_DISCORD_USER_ID",      },    },  },},},}
[/code]

Quedas de STT de voz com DecryptionFailed(...)

  * mantenha o OpenClaw atualizado (`openclaw update`) para que a lógica de recuperação de recebimento de voz do Discord esteja presente
  * confirme `channels.discord.voice.daveEncryption=true` (padrão)
  * comece com `channels.discord.voice.decryptionFailureTolerance=24` (padrão upstream) e ajuste somente se necessário
  * observe os logs para: 
    * `discord voice: DAVE decrypt failures detected`
    * `discord voice: repeated decrypt failures; attempting rejoin`
  * se as falhas continuarem após a reentrada automática, colete logs e compare com o histórico upstream de recebimento DAVE em [discord.js #11419](<https://github.com/discordjs/discord.js/issues/11419>) e [discord.js #11449](<https://github.com/discordjs/discord.js/pull/11449>)


## Referência de configuração

Referência principal: [Referência de configuração - Discord](</pt-BR/gateway/config-channels#discord>).

Campos Discord de alto sinal

  * inicialização/autenticação: `enabled`, `token`, `accounts.*`, `allowBots`
  * política: `groupPolicy`, `dm.*`, `guilds.*`, `guilds.*.channels.*`
  * comando: `commands.native`, `commands.useAccessGroups`, `configWrites`, `slashCommand.*`
  * fila de eventos: `eventQueue.listenerTimeout` (orçamento do listener), `eventQueue.maxQueueSize`, `eventQueue.maxConcurrency`
  * Gateway: `gatewayInfoTimeoutMs`, `gatewayReadyTimeoutMs`, `gatewayRuntimeReadyTimeoutMs`
  * resposta/histórico: `replyToMode`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`
  * entrega: `textChunkLimit`, `chunkMode`, `maxLinesPerMessage`
  * streaming: `streaming` (alias legado: `streamMode`), `streaming.preview.toolProgress`, `draftChunk`, `blockStreaming`, `blockStreamingCoalesce`
  * mídia/tentativa: `mediaMaxMb` (limita uploads de saída do Discord, padrão `100MB`), `retry`
  * ações: `actions.*`
  * presença: `activity`, `status`, `activityType`, `activityUrl`
  * UI: `ui.components.accentColor`
  * recursos: `threadBindings`, `bindings[]` de nível superior (`type: "acp"`), `pluralkit`, `execApprovals`, `intents`, `agentComponents`, `heartbeat`, `responsePrefix`


## Segurança e operações

  * Trate tokens de bot como segredos (`DISCORD_BOT_TOKEN` é preferível em ambientes supervisionados).
  * Conceda permissões do Discord com o menor privilégio necessário.
  * Se a implantação/estado dos comandos estiver obsoleta, reinicie o Gateway e verifique novamente com `openclaw channels status --probe`.


## Relacionados

[**Pareamento** Pareie um usuário do Discord ao Gateway. ](</pt-BR/channels/pairing>) [**Grupos** Comportamento de chat em grupo e lista de permissões. ](</pt-BR/channels/groups>) [**Roteamento de canais** Roteie mensagens de entrada para agentes. ](</pt-BR/channels/channel-routing>) [**Segurança** Modelo de ameaças e hardening. ](</pt-BR/gateway/security>) [**Roteamento multiagente** Mapeie servidores e canais para agentes. ](</pt-BR/concepts/multi-agent>) [**Comandos de barra** Comportamento de comandos nativos. ](</pt-BR/tools/slash-commands>)

Was this useful?YesNo