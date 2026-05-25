---
title: Tarefas agendadas
source_url: https://docs.openclaw.ai/pt-BR/automation/cron-jobs
scraped_at: 2026-05-25
---

Cron é o agendador integrado do Gateway. Ele persiste tarefas, acorda o agente no momento certo e pode entregar a saída de volta para um canal de chat ou endpoint de webhook.

## Início rápido

* ### Adicionar um lembrete único

bashCopy code
[code]
    openclaw cron add \  --name "Reminder" \  --at "2026-02-01T16:00:00Z" \  --session main \  --system-event "Reminder: check the cron docs draft" \  --wake now \  --delete-after-run
[/code]

* ### Verificar suas tarefas

bashCopy code
[code]
    openclaw cron listopenclaw cron get <job-id>openclaw cron show <job-id>
[/code]

* ### Ver histórico de execuções

bashCopy code
[code]
    openclaw cron runs --id <job-id>
[/code]

## Como o cron funciona

  * Cron é executado **dentro do processo do Gateway** (não dentro do modelo).
  * As definições de tarefas persistem em `~/.openclaw/cron/jobs.json`, então reinicializações não perdem agendamentos.
  * O estado de execução em runtime persiste ao lado dele em `~/.openclaw/cron/jobs-state.json`. Se você controlar definições de cron no git, controle `jobs.json` e adicione `jobs-state.json` ao gitignore.
  * Após a divisão, versões mais antigas do OpenClaw conseguem ler `jobs.json`, mas podem tratar tarefas como novas porque os campos de runtime agora ficam em `jobs-state.json`.
  * Quando `jobs.json` é editado enquanto o Gateway está em execução ou parado, o OpenClaw compara os campos de agendamento alterados com os metadados de slot de runtime pendentes e limpa valores `nextRunAtMs` obsoletos. Reescritas apenas de formatação ou apenas de ordem de chaves preservam o slot pendente.
  * Todas as execuções de cron criam registros de [tarefa em segundo plano](</pt-BR/automation/tasks>).
  * Na inicialização do Gateway, tarefas atrasadas de turno de agente isolado são reagendadas para fora da janela de conexão do canal em vez de serem reproduzidas imediatamente, para que a inicialização do Discord/Telegram e a configuração de comandos nativos continuem responsivas após reinicializações.
  * Tarefas únicas (`--at`) são excluídas automaticamente após sucesso por padrão.
  * Execuções de cron isoladas fazem um melhor esforço para fechar abas/processos de navegador rastreados para sua sessão `cron:<jobId>` quando a execução termina, para que automações de navegador desacopladas não deixem processos órfãos para trás.
  * Execuções de cron isoladas que recebem a concessão restrita de autolimpeza de cron ainda podem ler o status do agendador, uma lista autofiltrada de sua tarefa atual e o histórico de execuções dessa tarefa, para que verificações de status/Heartbeat possam inspecionar seu próprio agendamento sem obter acesso mais amplo para mutação de cron.
  * Execuções de cron isoladas também se protegem contra respostas de confirmação obsoletas. Se o primeiro resultado for apenas uma atualização de status provisória (`on it`, `pulling everything together` e dicas semelhantes) e nenhuma execução de subagente descendente ainda for responsável pela resposta final, o OpenClaw solicita novamente uma vez o resultado real antes da entrega.
  * Execuções de cron isoladas preferem metadados estruturados de negação de execução da execução incorporada e, em seguida, recorrem a marcadores conhecidos de resumo/saída final, como `SYSTEM_RUN_DENIED` e `INVALID_REQUEST`, para que um comando bloqueado não seja relatado como uma execução verde.
  * Execuções de cron isoladas também tratam falhas de agente no nível da execução como erros da tarefa mesmo quando nenhum payload de resposta é produzido, para que falhas de modelo/provedor incrementem contadores de erro e acionem notificações de falha em vez de limpar a tarefa como bem-sucedida.
  * Quando uma tarefa de turno de agente isolado atinge `timeoutSeconds`, o cron aborta a execução subjacente do agente e dá a ela uma janela curta de limpeza. Se a execução não esvaziar, a limpeza de propriedade do Gateway força a liberação da propriedade de sessão dessa execução antes de o cron registrar o timeout, para que trabalho de chat enfileirado não fique preso atrás de uma sessão de processamento obsoleta.
  * Se um turno de agente isolado travar antes do início do executor ou antes da primeira chamada ao modelo, o cron registra um timeout específico da fase, como `setup timed out before runner start` ou `stalled before first model call (last phase: context-engine)`. Esses watchdogs cobrem provedores incorporados e provedores baseados em CLI antes que o processo externo da CLI seja realmente iniciado, e são limitados independentemente de valores longos de `timeoutSeconds`, para que falhas de inicialização a frio/autenticação/contexto apareçam rapidamente em vez de esperar todo o orçamento da tarefa.


## Tipos de agendamento

Tipo | Flag da CLI | Descrição  
---|---|---  
`at` | `--at` | Timestamp único (ISO 8601 ou relativo, como `20m`)  
`every` | `--every` | Intervalo fixo  
`cron` | `--cron` | Expressão cron de 5 ou 6 campos com `--tz` opcional  
  
Timestamps sem fuso horário são tratados como UTC. Adicione `--tz America/New_York` para agendamento por horário local de relógio.

Expressões recorrentes no início da hora são automaticamente escalonadas em até 5 minutos para reduzir picos de carga. Use `--exact` para forçar temporização precisa ou `--stagger 30s` para uma janela explícita.

### Dia do mês e dia da semana usam lógica OR

Expressões cron são analisadas pelo [croner](<https://github.com/Hexagon/croner>). Quando os campos de dia do mês e dia da semana não são curingas, o croner corresponde quando **qualquer um** dos campos corresponde — não ambos. Esse é o comportamento padrão do cron Vixie.

CodeCopy code
[code]
    # Intended: "9 AM on the 15th, only if it's a Monday"# Actual:   "9 AM on every 15th, AND 9 AM on every Monday"0 9 15 * 1
[/code]

Isso dispara cerca de 5 a 6 vezes por mês em vez de 0 a 1 vez por mês. O OpenClaw usa aqui o comportamento OR padrão do Croner. Para exigir ambas as condições, use o modificador de dia da semana `+` do Croner (`0 9 15 * +1`) ou agende em um campo e proteja o outro no prompt ou comando da tarefa.

## Estilos de execução

Estilo | Valor de `--session` | Executa em | Melhor para  
---|---|---|---  
Sessão principal | `main` | Próximo turno de Heartbeat | Lembretes, eventos de sistema  
Isolada | `isolated` | `cron:<jobId>` dedicada | Relatórios, tarefas em segundo plano  
Sessão atual | `current` | Vinculada no momento da criação | Trabalho recorrente com contexto  
Sessão personalizada | `session:custom-id` | Sessão nomeada persistente | Workflows que se baseiam no histórico  
  
Sessão principal vs isolada vs personalizada

Tarefas de **sessão principal** enfileiram um evento de sistema e, opcionalmente, acordam o Heartbeat (`--wake now` ou `--wake next-heartbeat`). Esses eventos de sistema não estendem a atualização de redefinição diária/ociosa para a sessão de destino. Tarefas **isoladas** executam um turno de agente dedicado com uma sessão nova. **Sessões personalizadas** (`session:xxx`) persistem contexto entre execuções, permitindo workflows como standups diários que se baseiam em resumos anteriores.

O que 'sessão nova' significa para tarefas isoladas

Para tarefas isoladas, "sessão nova" significa um novo id de transcrição/sessão para cada execução. O OpenClaw pode carregar preferências seguras, como configurações de pensamento/rápido/verboso, rótulos e substituições explícitas de modelo/autenticação selecionadas pelo usuário, mas não herda contexto de conversa ambiente de uma linha de cron mais antiga: roteamento de canal/grupo, política de envio ou fila, elevação, origem ou vinculação de runtime ACP. Use `current` ou `session:<id>` quando uma tarefa recorrente deve deliberadamente se basear no mesmo contexto de conversa.

Limpeza de runtime

Para tarefas isoladas, o encerramento de runtime agora inclui limpeza de navegador por melhor esforço para essa sessão de cron. Falhas de limpeza são ignoradas para que o resultado real do cron ainda prevaleça.

Execuções de cron isoladas também descartam quaisquer instâncias de runtime MCP incluídas que tenham sido criadas para a tarefa por meio do caminho compartilhado de limpeza de runtime. Isso corresponde à forma como clientes MCP de sessão principal e sessão personalizada são encerrados, para que tarefas de cron isoladas não vazem processos filhos stdio ou conexões MCP de longa duração entre execuções.

Entrega de subagente e Discord

Quando execuções de cron isoladas orquestram subagentes, a entrega também prefere a saída final descendente em vez de texto provisório obsoleto do pai. Se descendentes ainda estiverem em execução, o OpenClaw suprime essa atualização parcial do pai em vez de anunciá-la.

Para destinos de anúncio do Discord somente texto, o OpenClaw envia o texto final canônico do assistente uma vez, em vez de reproduzir tanto payloads de texto transmitidos/intermediários quanto a resposta final. Payloads de mídia e payloads estruturados do Discord ainda são entregues como payloads separados para que anexos e componentes não sejam descartados.

### Opções de payload para tarefas isoladas

Texto do prompt (obrigatório para isoladas).

Substituição de modelo; usa o modelo permitido selecionado para a tarefa.

Substituição do nível de pensamento.

Ignora a injeção de arquivo de bootstrap do workspace.

Restringe quais ferramentas a tarefa pode usar, por exemplo `--tools exec,read`.

`--model` usa o modelo permitido selecionado como o modelo principal dessa tarefa. Não é o mesmo que uma substituição `/model` de sessão de chat: cadeias de fallback configuradas ainda se aplicam quando o modelo principal da tarefa falha. Se o modelo solicitado não for permitido ou não puder ser resolvido, o cron falha a execução com um erro de validação explícito em vez de recorrer silenciosamente à seleção de modelo do agente/padrão da tarefa.

Tarefas de cron também podem carregar `fallbacks` no nível do payload. Quando presente, essa lista substitui a cadeia de fallback configurada para a tarefa. Use `fallbacks: []` no payload/API da tarefa quando você quiser uma execução de cron estrita que tente apenas o modelo selecionado. Se uma tarefa tiver `--model`, mas não tiver fallbacks no payload nem configurados, o OpenClaw passa uma substituição explícita de fallback vazia para que o principal do agente não seja anexado como um destino extra oculto de nova tentativa.

A precedência de seleção de modelo para tarefas isoladas é:

  1. Substituição de modelo do hook do Gmail (quando a execução veio do Gmail e essa substituição é permitida)
  2. `model` do payload por tarefa
  3. Substituição armazenada de modelo da sessão de cron selecionada pelo usuário
  4. Seleção de modelo do agente/padrão


O modo rápido também segue a seleção ao vivo resolvida. Se a configuração do modelo selecionado tiver `params.fastMode`, o cron isolado usa isso por padrão. Uma substituição `fastMode` de sessão armazenada ainda prevalece sobre a configuração em qualquer direção.

Se uma execução isolada atingir uma transferência de troca de modelo ao vivo, o cron tenta novamente com o provedor/modelo trocado e persiste essa seleção ao vivo para a execução ativa antes de tentar novamente. Quando a troca também carrega um novo perfil de autenticação, o cron persiste essa substituição de perfil de autenticação para a execução ativa também. As novas tentativas são limitadas: após a tentativa inicial mais 2 novas tentativas de troca, o cron aborta em vez de entrar em loop para sempre.

Antes que uma execução cron isolada entre no executor do agente, o OpenClaw verifica endpoints de provedores locais alcançáveis configurados para provedores `api: "ollama"` e `api: "openai-completions"` cujo `baseUrl` seja loopback, rede privada ou `.local`. Se esse endpoint estiver indisponível, a execução é registrada como `skipped` com um erro claro de provedor/modelo em vez de iniciar uma chamada ao modelo. O resultado do endpoint é armazenado em cache por 5 minutos, então muitos jobs vencidos usando o mesmo servidor local Ollama, vLLM, SGLang ou LM Studio indisponível compartilham uma pequena sondagem em vez de criar uma tempestade de requisições. Execuções ignoradas pela pré-verificação de provedor não incrementam o backoff de erro de execução; habilite `failureAlert.includeSkipped` quando quiser notificações repetidas de ignorados.

## Entrega e saída

Modo | O que acontece  
---|---  
`announce` | Entrega de fallback do texto final ao destino se o agente não enviou  
`webhook` | Faz POST do payload do evento concluído para uma URL  
`none` | Sem entrega de fallback do executor  
  
Use `--announce --channel telegram --to "-1001234567890"` para entrega em canal. Para tópicos de fórum do Telegram, use `-1001234567890:topic:123`; chamadores diretos de RPC/config também podem passar `delivery.threadId` como string ou número. Destinos Slack/Discord/Mattermost devem usar prefixos explícitos (`channel:<id>`, `user:<id>`). IDs de sala Matrix diferenciam maiúsculas de minúsculas; use o ID exato da sala ou a forma `room:!room:server` do Matrix.

Quando a entrega de anúncio usa `channel: "last"` ou omite `channel`, um destino com prefixo de provedor como `telegram:123` pode selecionar o canal antes que o cron recorra ao histórico da sessão ou a um único canal configurado. Somente prefixos anunciados pelo Plugin carregado são seletores de provedor. Se `delivery.channel` for explícito, o prefixo do destino deve nomear o mesmo provedor; por exemplo, `channel: "whatsapp"` com `to: "telegram:123"` é rejeitado em vez de permitir que o WhatsApp interprete o ID do Telegram como um número de telefone. Prefixos de tipo de destino e serviço, como `channel:<id>`, `user:<id>`, `imessage:<handle>` e `sms:<number>`, continuam sendo sintaxe de destino pertencente ao canal, não seletores de provedor.

Para jobs isolados, a entrega de chat é compartilhada. Se uma rota de chat estiver disponível, o agente pode usar a ferramenta `message` mesmo quando o job usa `--no-deliver`. Se o agente enviar para o destino configurado/atual, o OpenClaw ignora o anúncio de fallback. Caso contrário, `announce`, `webhook` e `none` controlam apenas o que o executor faz com a resposta final após o turno do agente.

Quando um agente cria um lembrete isolado a partir de um chat ativo, o OpenClaw armazena o destino de entrega ao vivo preservado para a rota de anúncio de fallback. Chaves de sessão internas podem estar em minúsculas; destinos de entrega de provedor não são reconstruídos a partir dessas chaves quando o contexto de chat atual está disponível.

A entrega de anúncio implícita usa listas de permissão de canais configuradas para validar e redirecionar destinos obsoletos. Aprovações do armazenamento de pareamento de DM não são destinatários de automação de fallback; defina `delivery.to` ou configure a entrada `allowFrom` do canal quando um job agendado deve enviar proativamente para uma DM.

Notificações de falha seguem um caminho de destino separado:

  * `cron.failureDestination` define um padrão global para notificações de falha.
  * `job.delivery.failureDestination` substitui isso por job.
  * Se nenhum deles estiver definido e o job já entregar via `announce`, as notificações de falha agora recorrem a esse destino principal de anúncio.
  * `delivery.failureDestination` só é compatível com jobs `sessionTarget="isolated"`, a menos que o modo de entrega principal seja `webhook`.
  * `failureAlert.includeSkipped: true` inclui um job ou política global de alerta cron em alertas repetidos de execuções ignoradas. Execuções ignoradas mantêm um contador consecutivo separado de ignorados, então não afetam o backoff de erro de execução.


## Exemplos da CLI

### Lembrete único

bashCopy code
[code]
    openclaw cron add \  --name "Calendar check" \  --at "20m" \  --session main \  --system-event "Next heartbeat: check calendar." \  --wake now
[/code]

### Job isolado recorrente

bashCopy code
[code]
    openclaw cron add \  --name "Morning brief" \  --cron "0 7 * * *" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Summarize overnight updates." \  --announce \  --channel slack \  --to "channel:C1234567890"
[/code]

### Substituição de modelo e raciocínio

bashCopy code
[code]
    openclaw cron add \  --name "Deep analysis" \  --cron "0 6 * * 1" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Weekly deep analysis of project progress." \  --model "opus" \  --thinking high \  --announce
[/code]

## Webhooks

Gateway pode expor endpoints HTTP de Webhook para acionadores externos. Habilite na configuração:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",  },}
[/code]

### Autenticação

Toda requisição deve incluir o token do hook via cabeçalho:

  * `Authorization: Bearer <token>` (recomendado)
  * `x-openclaw-token: <token>`


Tokens em query string são rejeitados.

POST /hooks/wake

Enfileire um evento de sistema para a sessão principal:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/wake \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"text":"New email received","mode":"now"}'
[/code]

Descrição do evento.

`now` ou `next-heartbeat`.

POST /hooks/agent

Execute um turno de agente isolado:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/agent \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"message":"Summarize inbox","name":"Email","model":"openai/gpt-5.4"}'
[/code]

Campos: `message` (obrigatório), `name`, `agentId`, `wakeMode`, `deliver`, `channel`, `to`, `model`, `fallbacks`, `thinking`, `timeoutSeconds`.

OPENCLAW_DOCS_MARKER:accordionOpen:IHRpdGxlPSJIb29rcyBtYXBlYWRvcyAoUE9TVCAvaG9va3MvPG5hbWU )"> Nomes de hook personalizados são resolvidos via `hooks.mappings` na configuração. Mapeamentos podem transformar payloads arbitrários em ações `wake` ou `agent` com templates ou transformações por código.

## Integração com Gmail PubSub

Conecte acionadores da caixa de entrada do Gmail ao OpenClaw via Google PubSub.

### Configuração pelo assistente (recomendada)

bashCopy code
[code]
    openclaw webhooks gmail setup --account openclaw@gmail.com
[/code]

Isso grava a configuração `hooks.gmail`, habilita o preset do Gmail e usa Tailscale Funnel para o endpoint push.

### Inicialização automática do Gateway

Quando `hooks.enabled=true` e `hooks.gmail.account` está definido, o Gateway inicia `gog gmail watch serve` na inicialização e renova automaticamente o watch. Defina `OPENCLAW_SKIP_GMAIL_WATCHER=1` para desativar.

### Configuração manual única

* ### Selecione o projeto do GCP

Selecione o projeto do GCP que possui o cliente OAuth usado por `gog`:

bashCopy code
[code]
    gcloud auth logingcloud config set project <project-id>gcloud services enable gmail.googleapis.com pubsub.googleapis.com
[/code]

* ### Crie tópico e conceda acesso push ao Gmail

bashCopy code
[code]
    gcloud pubsub topics create gog-gmail-watchgcloud pubsub topics add-iam-policy-binding gog-gmail-watch \  --member=serviceAccount:gmail-api-push@system.gserviceaccount.com \  --role=roles/pubsub.publisher
[/code]

* ### Inicie o watch

bashCopy code
[code]
    gog gmail watch start \  --account openclaw@gmail.com \  --label INBOX \  --topic projects/<project-id>/topics/gog-gmail-watch
[/code]

### Substituição de modelo do Gmail

json5Copy code
[code]
    {  hooks: {    gmail: {      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",      thinking: "off",    },  },}
[/code]

## Gerenciamento de jobs

bashCopy code
[code]
    # List all jobsopenclaw cron list # Get one stored job as JSONopenclaw cron get <jobId> # Show one job, including resolved delivery routeopenclaw cron show <jobId> # Edit a jobopenclaw cron edit <jobId> --message "Updated prompt" --model "opus" # Force run a job nowopenclaw cron run <jobId> # Run only if dueopenclaw cron run <jobId> --due # View run historyopenclaw cron runs --id <jobId> --limit 50 # Delete a jobopenclaw cron remove <jobId> # Agent selection (multi-agent setups)openclaw cron add --name "Ops sweep" --cron "0 6 * * *" --session isolated --message "Check ops queue" --agent opsopenclaw cron edit <jobId> --clear-agent
[/code]

## Configuração

json5Copy code
[code]
    {  cron: {    enabled: true,    store: "~/.openclaw/cron/jobs.json",    maxConcurrentRuns: 1,    retry: {      maxAttempts: 3,      backoffMs: [60000, 120000, 300000],      retryOn: ["rate_limit", "overloaded", "network", "server_error"],    },    webhookToken: "replace-with-dedicated-webhook-token",    sessionRetention: "24h",    runLog: { maxBytes: "2mb", keepLines: 2000 },  },}
[/code]

`maxConcurrentRuns` limita tanto o despacho cron agendado quanto a execução de turnos isolados de agente. Turnos isolados de agentes cron usam internamente a via de execução dedicada `cron-nested` da fila, então aumentar esse valor permite que execuções independentes de LLM por cron avancem em paralelo em vez de apenas iniciar seus wrappers externos de cron. A via compartilhada não cron `nested` não é ampliada por essa configuração.

O sidecar de estado em runtime é derivado de `cron.store`: um armazenamento `.json` como `~/clawd/cron/jobs.json` usa `~/clawd/cron/jobs-state.json`, enquanto um caminho de armazenamento sem sufixo `.json` acrescenta `-state.json`.

Se editar `jobs.json` manualmente, deixe `jobs-state.json` fora do controle de versão. O OpenClaw usa esse sidecar para slots pendentes, marcadores ativos, metadados da última execução e a identidade de agendamento que informa ao scheduler quando um job editado externamente precisa de um novo `nextRunAtMs`.

Desabilite cron: `cron.enabled: false` ou `OPENCLAW_SKIP_CRON=1`.

Comportamento de nova tentativa

**Nova tentativa única** : erros transitórios (limite de taxa, sobrecarga, rede, erro de servidor) tentam novamente até 3 vezes com backoff exponencial. Erros permanentes desabilitam imediatamente.

**Nova tentativa recorrente** : backoff exponencial (30s a 60m) entre tentativas. O backoff é redefinido após a próxima execução bem-sucedida.

Manutenção

`cron.sessionRetention` (padrão `24h`) remove entradas isoladas de sessões de execução. `cron.runLog.maxBytes` / `cron.runLog.keepLines` removem automaticamente arquivos de log de execução.

## Solução de problemas

### Sequência de comandos

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --followopenclaw doctor
[/code]

Cron não dispara

  * Verifique `cron.enabled` e a variável de ambiente `OPENCLAW_SKIP_CRON`.
  * Confirme se o Gateway está em execução continuamente.
  * Para agendamentos `cron`, verifique o fuso horário (`--tz`) em relação ao fuso horário do host.
  * `reason: not-due` na saída de execução significa que a execução manual foi verificada com `openclaw cron run <jobId> --due` e o job ainda não estava vencido.

Cron disparou, mas não houve entrega

  * O modo de entrega `none` significa que nenhum envio de fallback do executor é esperado. O agente ainda pode enviar diretamente com a ferramenta `message` quando uma rota de chat está disponível.
  * Destino de entrega ausente/inválido (`channel`/`to`) significa que a saída foi ignorada.
  * Para Matrix, jobs copiados ou legados com IDs de sala `delivery.to` em minúsculas podem falhar porque IDs de sala do Matrix diferenciam maiúsculas de minúsculas. Edite o job para o valor exato `!room:server` ou `room:!room:server` do Matrix.
  * Erros de autenticação de canal (`unauthorized`, `Forbidden`) significam que a entrega foi bloqueada por credenciais.
  * Se a execução isolada retornar apenas o token silencioso (`NO_REPLY` / `no_reply`), o OpenClaw suprime a entrega direta de saída e também suprime o caminho de resumo enfileirado de fallback, então nada é postado de volta no chat.
  * Se o agente deve enviar mensagem ao usuário por conta própria, verifique se o job tem uma rota utilizável (`channel: "last"` com um chat anterior ou um canal/destino explícito).

Cron ou heartbeat parece impedir a rolagem estilo /new

  * A atualização diária e de redefinição por inatividade não se baseia em `updatedAt`; consulte [Gerenciamento de sessão](</pt-BR/concepts/session#session-lifecycle>).
  * Despertares de Cron, execuções de Heartbeat, notificações de exec e manutenção contábil do Gateway podem atualizar a linha da sessão para roteamento/status, mas não estendem `sessionStartedAt` nem `lastInteractionAt`.
  * Para linhas legadas criadas antes da existência desses campos, o OpenClaw pode recuperar `sessionStartedAt` do cabeçalho de sessão JSONL da transcrição quando o arquivo ainda está disponível. Linhas legadas inativas sem `lastInteractionAt` usam esse horário de início recuperado como sua linha de base de inatividade.

Pegadinhas de fuso horário

  * Cron sem `--tz` usa o fuso horário do host do gateway.
  * Agendamentos `at` sem fuso horário são tratados como UTC.
  * `activeHours` do Heartbeat usa a resolução de fuso horário configurada.


## Relacionado

  * [Automação](</pt-BR/automation>) — todos os mecanismos de automação em um relance
  * [Tarefas em segundo plano](</pt-BR/automation/tasks>) — livro-razão de tarefas para execuções de cron
  * [Heartbeat](</pt-BR/gateway/heartbeat>) — turnos periódicos da sessão principal
  * [Fuso horário](</pt-BR/concepts/timezone>) — configuração de fuso horário


Was this useful?YesNo