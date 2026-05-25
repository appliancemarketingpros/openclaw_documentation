---
title: Solução de problemas
source_url: https://docs.openclaw.ai/pt-BR/gateway/troubleshooting
scraped_at: 2026-05-25
---

Esta página é o runbook detalhado. Comece em [/help/troubleshooting](</pt-BR/help/troubleshooting>) se quiser primeiro o fluxo rápido de triagem.

## Escada de comandos

Execute estes primeiro, nesta ordem:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

Sinais esperados de integridade:

  * `openclaw gateway status` mostra `Runtime: running`, `Connectivity probe: ok` e uma linha `Capability: ...`.
  * `openclaw doctor` não relata problemas bloqueantes de configuração/serviço.
  * `openclaw channels status --probe` mostra o status de transporte ativo por conta e, quando compatível, resultados de sondagem/auditoria como `works` ou `audit ok`.


## Instalações split brain e proteção de configuração mais nova

Use isto quando um serviço Gateway parar inesperadamente após uma atualização, ou quando os logs mostrarem que um binário `openclaw` é mais antigo que a versão que gravou `openclaw.json` pela última vez.

O OpenClaw marca gravações de configuração com `meta.lastTouchedVersion`. Comandos somente leitura ainda podem inspecionar uma configuração gravada por um OpenClaw mais novo, mas mutações de processo e serviço se recusam a continuar a partir de um binário mais antigo. As ações bloqueadas incluem iniciar, parar, reiniciar e desinstalar o serviço Gateway, reinstalação forçada de serviço, inicialização do Gateway em modo de serviço e limpeza de porta com `gateway --force`.

bashCopy code
[code]
    which openclawopenclaw --versionopenclaw gateway status --deepopenclaw config get meta.lastTouchedVersion
[/code]

* ### Corrigir PATH

Corrija `PATH` para que `openclaw` resolva para a instalação mais nova e, em seguida, execute novamente a ação.

* ### Reinstalar o serviço Gateway

Reinstale o serviço Gateway pretendido a partir da instalação mais nova:

bashCopy code
[code]
    openclaw gateway install --forceopenclaw gateway restart
[/code]

* ### Remover wrappers obsoletos

Remova pacotes de sistema obsoletos ou entradas antigas de wrapper que ainda apontem para um binário `openclaw` antigo.

## Symlink de Skill ignorado como escape de caminho

Use isto quando os logs incluírem:

textCopy code
[code]
    Skipping escaped skill path outside its configured root: ... reason=symlink-escape
[/code]

O OpenClaw trata toda raiz de skill como um limite de contenção. Um symlink em `~/.agents/skills`, `<workspace>/.agents/skills`, `<workspace>/skills` ou `~/.openclaw/skills` é ignorado quando seu destino real é resolvido para fora dessa raiz, a menos que o destino seja explicitamente confiável.

Inspecione o link:

bashCopy code
[code]
    ls -l ~/.agents/skills/<name>realpath ~/.agents/skills/<name>openclaw config get skills.load
[/code]

Se o destino for intencional, configure tanto a raiz direta da skill quanto o destino de symlink permitido:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/manager/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },  },}
[/code]

Então inicie uma nova sessão ou aguarde o observador de Skills atualizar. Reinicie o Gateway se o processo em execução for anterior à alteração de configuração.

Não use destinos amplos como `~`, `/` ou uma pasta inteira de projeto sincronizado. Mantenha `allowSymlinkTargets` restrito à raiz real de skills que contém diretórios `SKILL.md` confiáveis.

Relacionado:

  * [Configuração de Skills](</pt-BR/tools/skills-config#symlinked-sibling-repos>)
  * [Exemplos de configuração](</pt-BR/gateway/configuration-examples#symlinked-sibling-skill-repo>)


## Uso extra da Anthropic 429 necessário para contexto longo

Use isto quando logs/erros incluírem: `HTTP 429: rate_limit_error: Extra usage is required for long context requests`.

bashCopy code
[code]
    openclaw logs --followopenclaw models statusopenclaw config get agents.defaults.models
[/code]

Procure por:

  * O modelo Anthropic Opus/Sonnet selecionado tem `params.context1m: true`.
  * A credencial Anthropic atual não é elegível para uso de contexto longo.
  * As solicitações falham apenas em sessões longas/execuções de modelo que precisam do caminho beta de 1M.


Opções de correção:

* ### Desabilitar context1m

Desabilite `context1m` para esse modelo para voltar à janela de contexto normal.

* ### Usar uma credencial elegível

Use uma credencial Anthropic elegível para solicitações de contexto longo ou mude para uma chave de API Anthropic.

* ### Configurar modelos de fallback

Configure modelos de fallback para que as execuções continuem quando solicitações de contexto longo da Anthropic forem rejeitadas.

Relacionado:

  * [Anthropic](</pt-BR/providers/anthropic>)
  * [Uso de tokens e custos](</pt-BR/reference/token-use>)
  * [Por que estou vendo HTTP 429 da Anthropic?](</pt-BR/help/faq-first-run#why-am-i-seeing-http-429-ratelimiterror-from-anthropic>)


## Backend local compatível com OpenAI passa em sondagens diretas, mas execuções de agente falham

Use isto quando:

  * `curl ... /v1/models` funciona
  * chamadas diretas pequenas a `/v1/chat/completions` funcionam
  * execuções de modelo do OpenClaw falham apenas em turnos normais do agente

bashCopy code
[code]
    curl http://127.0.0.1:1234/v1/modelscurl http://127.0.0.1:1234/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"<id>","messages":[{"role":"user","content":"hi"}],"stream":false}'openclaw infer model run --model <provider/model> --prompt "hi" --jsonopenclaw logs --follow
[/code]

Procure por:

  * chamadas diretas pequenas têm sucesso, mas execuções do OpenClaw falham apenas em prompts maiores
  * erros `model_not_found` ou 404 mesmo que chamadas diretas a `/v1/chat/completions` funcionem com o mesmo id de modelo simples
  * erros do backend sobre `messages[].content` esperar uma string
  * avisos intermitentes `incomplete turn detected ... stopReason=stop payloads=0` com um backend local compatível com OpenAI
  * falhas do backend que aparecem apenas com contagens maiores de tokens de prompt ou prompts completos do runtime do agente


Assinaturas comuns

  * `model_not_found` com um servidor local no estilo MLX/vLLM → verifique se `baseUrl` inclui `/v1`, se `api` é `"openai-completions"` para backends `/v1/chat/completions` e se `models.providers.<provider>.models[].id` é o id simples local do provedor. Selecione-o uma vez com o prefixo do provedor, por exemplo `mlx/mlx-community/Qwen3-30B-A3B-6bit`; mantenha a entrada do catálogo como `mlx-community/Qwen3-30B-A3B-6bit`.
  * `messages[...].content: invalid type: sequence, expected a string` → o backend rejeita partes de conteúdo estruturado do Chat Completions. Correção: defina `models.providers.<provider>.models[].compat.requiresStringContent: true`.
  * `validation.keys` ou chaves de mensagem permitidas como `["role","content"]` → o backend rejeita metadados de replay no estilo OpenAI em mensagens do Chat Completions. Correção: defina `models.providers.<provider>.models[].compat.strictMessageKeys: true`.
  * `incomplete turn detected ... stopReason=stop payloads=0` → o backend concluiu a solicitação do Chat Completions, mas não retornou texto de assistente visível ao usuário para esse turno. O OpenClaw tenta novamente uma vez turnos vazios compatíveis com OpenAI seguros para replay; falhas persistentes geralmente significam que o backend está emitindo conteúdo vazio/não textual ou suprimindo texto de resposta final.
  * solicitações diretas pequenas têm sucesso, mas execuções de agente do OpenClaw falham com travamentos do backend/modelo (por exemplo, Gemma em algumas builds `inferrs`) → o transporte do OpenClaw provavelmente já está correto; o backend está falhando no formato maior de prompt do runtime do agente.
  * as falhas diminuem após desabilitar ferramentas, mas não desaparecem → esquemas de ferramentas faziam parte da pressão, mas o problema restante ainda é capacidade do modelo/servidor upstream ou um bug do backend.

Opções de correção

  1. Defina `compat.requiresStringContent: true` para backends Chat Completions que aceitam apenas strings.
  2. Defina `compat.strictMessageKeys: true` para backends Chat Completions estritos que aceitam apenas `role` e `content` em cada mensagem.
  3. Defina `compat.supportsTools: false` para modelos/backends que não conseguem lidar de forma confiável com a superfície de esquema de ferramentas do OpenClaw.
  4. Reduza a pressão do prompt quando possível: bootstrap menor do workspace, histórico de sessão mais curto, modelo local mais leve ou um backend com suporte mais forte a contexto longo.
  5. Se solicitações diretas pequenas continuarem passando enquanto turnos de agente do OpenClaw ainda travarem dentro do backend, trate isso como uma limitação upstream do servidor/modelo e registre uma reprodução lá com o formato de payload aceito.


Relacionado:

  * [Configuração](</pt-BR/gateway/configuration>)
  * [Modelos locais](</pt-BR/gateway/local-models>)
  * [Endpoints compatíveis com OpenAI](</pt-BR/gateway/configuration-reference#openai-compatible-endpoints>)


## Sem respostas

Se os canais estiverem ativos, mas nada responder, verifique roteamento e política antes de reconectar qualquer coisa.

bashCopy code
[code]
    openclaw statusopenclaw channels status --probeopenclaw pairing list --channel <channel> [--account <id>]openclaw config get channelsopenclaw logs --follow
[/code]

Procure por:

  * Pareamento pendente para remetentes de DM.
  * Controle de menção em grupo (`requireMention`, `mentionPatterns`).
  * Divergências de allowlist de canal/grupo.


Assinaturas comuns:

  * `drop guild message (mention required` → mensagem de grupo ignorada até menção.
  * `pairing request` → remetente precisa de aprovação.
  * `blocked` / `allowlist` → remetente/canal foi filtrado por política.


Relacionado:

  * [Solução de problemas de canais](</pt-BR/channels/troubleshooting>)
  * [Grupos](</pt-BR/channels/groups>)
  * [Pareamento](</pt-BR/channels/pairing>)


## Conectividade da interface de controle do dashboard

Quando a interface de controle/dashboard não conectar, valide URL, modo de autenticação e pressupostos de contexto seguro.

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --followopenclaw doctoropenclaw gateway status --json
[/code]

Procure por:

  * URL de sondagem e URL do dashboard corretas.
  * Divergência de modo/token de autenticação entre cliente e Gateway.
  * Uso de HTTP onde identidade do dispositivo é necessária.


Assinaturas de conexão/autenticação

  * `device identity required` → contexto não seguro ou autenticação de dispositivo ausente.
  * `origin not allowed` → o `Origin` do navegador não está em `gateway.controlUi.allowedOrigins` (ou você está conectando a partir de uma origem de navegador que não é loopback sem uma allowlist explícita).
  * `device nonce required` / `device nonce mismatch` → o cliente não está concluindo o fluxo de autenticação de dispositivo baseado em desafio (`connect.challenge` \+ `device.nonce`).
  * `device signature invalid` / `device signature expired` → o cliente assinou o payload errado (ou timestamp obsoleto) para o handshake atual.
  * `AUTH_TOKEN_MISMATCH` com `canRetryWithDeviceToken=true` → o cliente pode fazer uma nova tentativa confiável com o token de dispositivo em cache.
  * Essa nova tentativa com token em cache reutiliza o conjunto de escopos em cache armazenado com o token de dispositivo pareado. Chamadores com `deviceToken` explícito / `scopes` explícitos mantêm o conjunto de escopos solicitado.
  * `AUTH_SCOPE_MISMATCH` → o token de dispositivo foi reconhecido, mas seus escopos aprovados não cobrem esta solicitação de conexão; refaça o pareamento ou aprove o contrato de escopo solicitado em vez de rotacionar um token Gateway compartilhado.
  * Fora desse caminho de nova tentativa, a precedência de autenticação de conexão é token/senha compartilhado explícito primeiro, depois `deviceToken` explícito, depois token de dispositivo armazenado, depois token de bootstrap.
  * No caminho assíncrono da interface de controle do Tailscale Serve, tentativas malsucedidas para o mesmo `{scope, ip}` são serializadas antes que o limitador registre a falha. Portanto, duas novas tentativas concorrentes inválidas do mesmo cliente podem expor `retry later` na segunda tentativa em vez de duas divergências simples.
  * `too many failed authentication attempts (retry later)` de um cliente loopback com origem de navegador → falhas repetidas dessa mesma `Origin` normalizada são bloqueadas temporariamente; outra origem localhost usa um bucket separado.
  * `unauthorized` repetido após essa nova tentativa → divergência de token compartilhado/token de dispositivo; atualize a configuração do token e aprove novamente/rotacione o token de dispositivo se necessário.
  * `gateway connect failed:` → alvo de host/porta/url errado.


### Mapa rápido de códigos de detalhe de autenticação

Use `error.details.code` da resposta `connect` com falha para escolher a próxima ação:

Código de detalhe | Significado | Ação recomendada  
---|---|---  
`AUTH_TOKEN_MISSING` | O cliente não enviou um token compartilhado obrigatório. | Cole/defina o token no cliente e tente novamente. Para caminhos do painel: `openclaw config get gateway.auth.token` e então cole nas configurações da interface de controle.  
`AUTH_TOKEN_MISMATCH` | O token compartilhado não correspondeu ao token de autenticação do Gateway. | Se `canRetryWithDeviceToken=true`, permita uma nova tentativa confiável. Novas tentativas com token em cache reutilizam escopos aprovados armazenados; chamadores explícitos de `deviceToken` / `scopes` mantêm os escopos solicitados. Se ainda falhar, execute a [lista de verificação de recuperação de desvio de token](</pt-BR/cli/devices#token-drift-recovery-checklist>).  
`AUTH_DEVICE_TOKEN_MISMATCH` | O token por dispositivo em cache está obsoleto ou foi revogado. | Rotacione/reaprove o token do dispositivo usando a [CLI de dispositivos](</pt-BR/cli/devices>), então reconecte.  
`AUTH_SCOPE_MISMATCH` | O token do dispositivo é válido, mas sua função/escopos aprovados não cobrem esta solicitação de conexão. | Repareie o dispositivo ou aprove o contrato de escopo solicitado; não trate isso como desvio do token compartilhado.  
`PAIRING_REQUIRED` | A identidade do dispositivo precisa de aprovação. Verifique `error.details.reason` para `not-paired`, `scope-upgrade`, `role-upgrade` ou `metadata-upgrade`, e use `requestId` / `remediationHint` quando presentes. | Aprove a solicitação pendente: `openclaw devices list` e então `openclaw devices approve <requestId>`. Atualizações de escopo/função usam o mesmo fluxo depois que você revisar o acesso solicitado.  
  
Verificação da migração de autenticação de dispositivo v2:

bashCopy code
[code]
    openclaw --versionopenclaw doctoropenclaw gateway status
[/code]

Se os logs mostrarem erros de nonce/assinatura, atualize o cliente de conexão e verifique-o:

* ### Aguardar connect.challenge

O cliente aguarda o `connect.challenge` emitido pelo Gateway.

* ### Assinar o payload

O cliente assina o payload vinculado ao desafio.

* ### Enviar o nonce do dispositivo

O cliente envia `connect.params.device.nonce` com o mesmo nonce do desafio.

Se `openclaw devices rotate` / `revoke` / `remove` for negado inesperadamente:

  * sessões de token de dispositivo pareado podem gerenciar apenas **seu próprio** dispositivo, a menos que o chamador também tenha `operator.admin`
  * `openclaw devices rotate --scope ...` só pode solicitar escopos de operador que a sessão do chamador já possui


Relacionado:

  * [Configuração](</pt-BR/gateway/configuration>) (modos de autenticação do Gateway)
  * [Interface de controle](</pt-BR/web/control-ui>)
  * [Dispositivos](</pt-BR/cli/devices>)
  * [Acesso remoto](</pt-BR/gateway/remote>)
  * [Autenticação de proxy confiável](</pt-BR/gateway/trusted-proxy-auth>)


## Serviço do Gateway não está em execução

Use isto quando o serviço está instalado, mas o processo não permanece ativo.

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --followopenclaw doctoropenclaw gateway status --deep   # also scan system-level services
[/code]

Procure por:

  * `Runtime: stopped` com dicas de saída.
  * Incompatibilidade de configuração do serviço (`Config (cli)` vs `Config (service)`).
  * Conflitos de porta/listener.
  * Instalações extras de launchd/systemd/schtasks quando `--deep` é usado.
  * Dicas de limpeza de `Other gateway-like services detected (best effort)`.


Assinaturas comuns

  * `Gateway start blocked: set gateway.mode=local` ou `existing config is missing gateway.mode` → o modo de Gateway local não está habilitado, ou o arquivo de configuração foi sobrescrito e perdeu `gateway.mode`. Correção: defina `gateway.mode="local"` na sua configuração ou execute novamente `openclaw onboard --mode local` / `openclaw setup` para remarcar a configuração de modo local esperada. Se você estiver executando o OpenClaw via Podman, o caminho de configuração padrão é `~/.openclaw/openclaw.json`.
  * `refusing to bind gateway ... without auth` → bind fora de loopback sem um caminho de autenticação do Gateway válido (token/senha, ou proxy confiável quando configurado).
  * `another gateway instance is already listening` / `EADDRINUSE` → conflito de porta.
  * `Other gateway-like services detected (best effort)` → unidades launchd/systemd/schtasks obsoletas ou paralelas existem. A maioria das configurações deve manter um Gateway por máquina; se você realmente precisar de mais de um, isole portas + configuração/estado/workspace. Consulte [/gateway#multiple-gateways-same-host](</pt-BR/gateway#multiple-gateways-same-host>).
  * `System-level OpenClaw gateway service detected` do doctor → existe uma unidade de sistema systemd enquanto o serviço em nível de usuário está ausente. Remova ou desabilite a duplicata antes de permitir que o doctor instale um serviço de usuário, ou defina `OPENCLAW_SERVICE_REPAIR_POLICY=external` se a unidade de sistema for o supervisor pretendido.
  * `Gateway service port does not match current gateway config` → o supervisor instalado ainda fixa o `--port` antigo. Execute `openclaw doctor --fix` ou `openclaw gateway install --force`, então reinicie o serviço do Gateway.


Relacionado:

  * [Execução em segundo plano e ferramenta de processo](</pt-BR/gateway/background-process>)
  * [Configuração](</pt-BR/gateway/configuration>)
  * [Doctor](</pt-BR/gateway/doctor>)


## Gateway rejeitou configuração inválida

Use isto quando a inicialização do Gateway falhar com `Invalid config` ou os logs de recarregamento dinâmico disserem que uma edição inválida foi ignorada.

bashCopy code
[code]
    openclaw logs --followopenclaw config fileopenclaw config validateopenclaw doctor
[/code]

Procure por:

  * `Invalid config at ...`
  * `config reload skipped (invalid config): ...`
  * `Config write rejected: ...`
  * Um arquivo `openclaw.json.rejected.*` com carimbo de data/hora ao lado da configuração ativa
  * Um arquivo `openclaw.json.clobbered.*` com carimbo de data/hora se `doctor --fix` reparou uma edição direta quebrada


O que aconteceu

  * A configuração não foi validada durante a inicialização, o recarregamento dinâmico ou uma gravação pertencente ao OpenClaw.
  * A inicialização do Gateway falha fechada em vez de reescrever `openclaw.json`.
  * O recarregamento dinâmico ignora edições externas inválidas e mantém a configuração de runtime atual ativa.
  * Gravações pertencentes ao OpenClaw rejeitam payloads inválidos/destrutivos antes do commit e salvam `.rejected.*`.
  * `openclaw doctor --fix` é responsável pelo reparo. Ele pode remover prefixos não JSON ou restaurar a última cópia válida conhecida preservando o payload rejeitado como `.clobbered.*`.

Inspecionar e reparar bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".clobbered.* "$CONFIG".rejected.* 2>/dev/null | headdiff -u "$CONFIG" "$(ls -t "$CONFIG".clobbered.* 2>/dev/null | head -n 1)"openclaw config validateopenclaw doctor
[/code]

Assinaturas comuns

  * `.clobbered.*` existe → o doctor preservou uma edição externa quebrada enquanto reparava a configuração ativa.
  * `.rejected.*` existe → uma gravação de configuração pertencente ao OpenClaw falhou em verificações de esquema ou sobrescrita antes do commit.
  * `Config write rejected:` → a gravação tentou remover a forma obrigatória, reduzir o arquivo drasticamente ou persistir uma configuração inválida.
  * `config reload skipped (invalid config):` → uma edição direta falhou na validação e foi ignorada pelo Gateway em execução.
  * `Invalid config at ...` → a inicialização falhou antes dos serviços do Gateway iniciarem.
  * `missing-meta-vs-last-good`, `gateway-mode-missing-vs-last-good` ou `size-drop-vs-last-good:*` → uma gravação pertencente ao OpenClaw foi rejeitada porque perdeu campos ou tamanho em comparação com o último backup válido conhecido.
  * `Config last-known-good promotion skipped` → o candidato continha placeholders de segredos redigidos, como `***`.

Opções de correção

  1. Execute `openclaw doctor --fix` para deixar o doctor reparar configuração prefixada/sobrescrita ou restaurar a última versão válida conhecida.
  2. Copie apenas as chaves pretendidas de `.clobbered.*` ou `.rejected.*`, então aplique-as com `openclaw config set` ou `config.patch`.
  3. Execute `openclaw config validate` antes de reiniciar.
  4. Se você editar manualmente, mantenha a configuração JSON5 completa, não apenas o objeto parcial que queria alterar.


Relacionado:

  * [Config](</pt-BR/cli/config>)
  * [Configuração: recarregamento dinâmico](</pt-BR/gateway/configuration#config-hot-reload>)
  * [Configuração: validação estrita](</pt-BR/gateway/configuration#strict-validation>)
  * [Doctor](</pt-BR/gateway/doctor>)


## Avisos de probe do Gateway

Use isto quando `openclaw gateway probe` alcança algo, mas ainda imprime um bloco de aviso.

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --jsonopenclaw gateway probe --ssh user@gateway-host
[/code]

Procure por:

  * `warnings[].code` e `primaryTargetId` na saída JSON.
  * Se o aviso é sobre fallback de SSH, múltiplos Gateways, escopos ausentes ou refs de autenticação não resolvidas.


Assinaturas comuns:

  * `SSH tunnel failed to start; falling back to direct probes.` → a configuração de SSH falhou, mas o comando ainda tentou alvos diretos configurados/loopback.
  * `multiple reachable gateways detected` → mais de um alvo respondeu. Normalmente, isso significa uma configuração multi-Gateway intencional ou listeners obsoletos/duplicados.
  * `Read-probe diagnostics are limited by gateway scopes (missing operator.read)` → a conexão funcionou, mas a RPC de detalhes é limitada por escopo; pareie a identidade do dispositivo ou use credenciais com `operator.read`.
  * `Gateway accepted the WebSocket connection, but follow-up read diagnostics failed` → a conexão funcionou, mas o conjunto completo de RPCs diagnósticas atingiu timeout ou falhou. Trate isso como um Gateway alcançável com diagnósticos degradados; compare `connect.ok` e `connect.rpcOk` na saída de `--json`.
  * `Capability: pairing-pending` ou `gateway closed (1008): pairing required` → o Gateway respondeu, mas este cliente ainda precisa de pareamento/aprovação antes do acesso normal de operador.
  * texto de aviso de SecretRef `gateway.auth.*` / `gateway.remote.*` não resolvido → o material de autenticação não estava disponível neste caminho de comando para o alvo com falha.


Relacionado:

  * [Gateway](</pt-BR/cli/gateway>)
  * [Vários gateways no mesmo host](</pt-BR/gateway#multiple-gateways-same-host>)
  * [Acesso remoto](</pt-BR/gateway/remote>)


## Canal conectado, mensagens não fluem

Se o estado do canal está conectado, mas o fluxo de mensagens parou, concentre-se em política, permissões e regras de entrega específicas do canal.

bashCopy code
[code]
    openclaw channels status --probeopenclaw pairing list --channel <channel> [--account <id>]openclaw status --deepopenclaw logs --followopenclaw config get channels
[/code]

Procure por:

  * Política de DM (`pairing`, `allowlist`, `open`, `disabled`).
  * Lista de permissões de grupos e requisitos de menção.
  * Permissões/escopos ausentes da API do canal.


Assinaturas comuns:

  * `mention required` → mensagem ignorada pela política de menção em grupo.
  * `pairing` / rastros de aprovação pendente → remetente não aprovado.
  * `missing_scope`, `not_in_channel`, `Forbidden`, `401/403` → problema de autenticação/permissões do canal.


Relacionado:

  * [Solução de problemas de canal](</pt-BR/channels/troubleshooting>)
  * [Discord](</pt-BR/channels/discord>)
  * [Telegram](</pt-BR/channels/telegram>)
  * [WhatsApp](</pt-BR/channels/whatsapp>)


## Entrega de Cron e Heartbeat

Se o Cron ou Heartbeat não executou ou não entregou, verifique primeiro o estado do agendador e depois o destino de entrega.

bashCopy code
[code]
    openclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --follow
[/code]

Procure por:

  * Cron habilitado e próximo despertar presente.
  * Status do histórico de execução do job (`ok`, `skipped`, `error`).
  * Motivos de salto do Heartbeat (`quiet-hours`, `requests-in-flight`, `cron-in-progress`, `lanes-busy`, `alerts-disabled`, `empty-heartbeat-file`, `no-tasks-due`).


Assinaturas comuns

  * `cron: scheduler disabled; jobs will not run automatically` → cron desabilitado.
  * `cron: timer tick failed` → tick do agendador falhou; verifique erros de arquivo/log/runtime.
  * `heartbeat skipped` with `reason=quiet-hours` → fora da janela de horas ativas.
  * `heartbeat skipped` with `reason=empty-heartbeat-file` → `HEARTBEAT.md` existe, mas contém apenas linhas em branco / cabeçalhos markdown, então o OpenClaw pula a chamada ao modelo.
  * `heartbeat skipped` with `reason=no-tasks-due` → `HEARTBEAT.md` contém um bloco `tasks:`, mas nenhuma das tarefas vence neste tick.
  * `heartbeat: unknown accountId` → ID de conta inválido para o destino de entrega do Heartbeat.
  * `heartbeat skipped` with `reason=dm-blocked` → o destino do Heartbeat foi resolvido para um destino estilo DM enquanto `agents.defaults.heartbeat.directPolicy` (ou substituição por agente) está definido como `block`.


Relacionado:

  * [Heartbeat](</pt-BR/gateway/heartbeat>)
  * [Tarefas agendadas](</pt-BR/automation/cron-jobs>)
  * [Tarefas agendadas: solução de problemas](</pt-BR/automation/cron-jobs#troubleshooting>)


## Node pareado, ferramenta falha

Se um Node está pareado, mas as ferramentas falham, isole estado de primeiro plano, permissão e aprovação.

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --followopenclaw status
[/code]

Procure por:

  * Node online com os recursos esperados.
  * Concessões de permissão do SO para câmera/microfone/localização/tela.
  * Aprovações de execução e estado da lista de permissões.


Assinaturas comuns:

  * `NODE_BACKGROUND_UNAVAILABLE` → o app do Node deve estar em primeiro plano.
  * `*_PERMISSION_REQUIRED` / `LOCATION_PERMISSION_REQUIRED` → permissão do SO ausente.
  * `SYSTEM_RUN_DENIED: approval required` → aprovação de execução pendente.
  * `SYSTEM_RUN_DENIED: allowlist miss` → comando bloqueado pela lista de permissões.


Relacionado:

  * [Aprovações de execução](</pt-BR/tools/exec-approvals>)
  * [Solução de problemas de Node](</pt-BR/nodes/troubleshooting>)
  * [Nodes](</pt-BR/nodes>)


## Ferramenta de navegador falha

Use isto quando ações da ferramenta de navegador falharem mesmo que o Gateway em si esteja saudável.

bashCopy code
[code]
    openclaw browser statusopenclaw browser start --browser-profile openclawopenclaw browser profilesopenclaw logs --followopenclaw doctor
[/code]

Procure por:

  * Se `plugins.allow` está definido e inclui `browser`.
  * Caminho válido do executável do navegador.
  * Acessibilidade do perfil CDP.
  * Disponibilidade local do Chrome para perfis `existing-session` / `user`.


Assinaturas de Plugin / executável

  * `unknown command "browser"` or `unknown command 'browser'` → o Plugin de navegador incluído foi excluído por `plugins.allow`.
  * browser tool missing / unavailable while `browser.enabled=true` → `plugins.allow` exclui `browser`, então o Plugin nunca foi carregado.
  * `Failed to start Chrome CDP on port` → o processo do navegador falhou ao iniciar.
  * `browser.executablePath not found` → o caminho configurado é inválido.
  * `browser.cdpUrl must be http(s) or ws(s)` → a URL CDP configurada usa um esquema sem suporte, como `file:` ou `ftp:`.
  * `browser.cdpUrl has invalid port` → a URL CDP configurada tem uma porta inválida ou fora do intervalo.
  * `Playwright is not available in this gateway build; '<feature>' is unsupported.` → a instalação atual do Gateway não tem a dependência principal de runtime do navegador; reinstale ou atualize o OpenClaw e reinicie o Gateway. Snapshots ARIA e capturas de tela básicas de página ainda podem funcionar, mas navegação, snapshots de IA, capturas de tela de elementos por seletor CSS e exportação de PDF permanecem indisponíveis.

Assinaturas de Chrome MCP / existing-session

  * `Could not find DevToolsActivePort for chrome` → a sessão existente do Chrome MCP ainda não conseguiu se anexar ao diretório de dados do navegador selecionado. Abra a página de inspeção do navegador, habilite a depuração remota, mantenha o navegador aberto, aprove o primeiro prompt de anexação e tente novamente. Se o estado com login não for necessário, prefira o perfil gerenciado `openclaw`.
  * `No Chrome tabs found for profile="user"` → o perfil de anexação do Chrome MCP não tem abas locais do Chrome abertas.
  * `Remote CDP for profile "<name>" is not reachable` → o endpoint CDP remoto configurado não está acessível a partir do host do Gateway.
  * `Browser attachOnly is enabled ... not reachable` or `Browser attachOnly is enabled and CDP websocket ... is not reachable` → o perfil somente de anexação não tem um alvo acessível, ou o endpoint HTTP respondeu, mas o WebSocket CDP ainda não pôde ser aberto.

Assinaturas de elemento / captura de tela / upload

  * `fullPage is not supported for element screenshots` → a solicitação de captura de tela misturou `--full-page` com `--ref` ou `--element`.
  * `element screenshots are not supported for existing-session profiles; use ref from snapshot.` → chamadas de captura de tela do Chrome MCP / `existing-session` devem usar captura de página ou um `--ref` de snapshot, não CSS `--element`.
  * `existing-session file uploads do not support element selectors; use ref/inputRef.` → hooks de upload do Chrome MCP precisam de refs de snapshot, não seletores CSS.
  * `existing-session file uploads currently support one file at a time.` → envie um upload por chamada em perfis Chrome MCP.
  * `existing-session dialog handling does not support timeoutMs.` → hooks de diálogo em perfis Chrome MCP não oferecem suporte a substituições de timeout.
  * `existing-session type does not support timeoutMs overrides.` → omita `timeoutMs` para `act:type` em perfis `profile="user"` / Chrome MCP existing-session, ou use um perfil de navegador gerenciado/CDP quando um timeout personalizado for necessário.
  * `existing-session evaluate does not support timeoutMs overrides.` → omita `timeoutMs` para `act:evaluate` em perfis `profile="user"` / Chrome MCP existing-session, ou use um perfil de navegador gerenciado/CDP quando um timeout personalizado for necessário.
  * `response body is not supported for existing-session profiles yet.` → `responsebody` ainda exige um navegador gerenciado ou perfil CDP bruto.
  * substituições antigas de viewport / modo escuro / localidade / offline em perfis somente de anexação ou CDP remoto → execute `openclaw browser stop --browser-profile <name>` para fechar a sessão de controle ativa e liberar o estado de emulação Playwright/CDP sem reiniciar todo o Gateway.


Relacionado:

  * [Navegador (gerenciado pelo OpenClaw)](</pt-BR/tools/browser>)
  * [Solução de problemas do navegador no Linux](</pt-BR/tools/browser-linux-troubleshooting>)


## Se você atualizou e algo quebrou de repente

A maior parte das falhas pós-atualização é desvio de configuração ou padrões mais rigorosos agora sendo aplicados.

1\. O comportamento de autenticação e substituição de URL mudou bashCopy code
[code]
    openclaw gateway statusopenclaw config get gateway.modeopenclaw config get gateway.remote.urlopenclaw config get gateway.auth.mode
[/code]

O que verificar:

  * Se `gateway.mode=remote`, chamadas da CLI podem estar direcionando para o remoto enquanto seu serviço local está funcionando.
  * Chamadas explícitas com `--url` não recorrem a credenciais armazenadas.


Assinaturas comuns:

  * `gateway connect failed:` → destino de URL incorreto.
  * `unauthorized` → endpoint acessível, mas autenticação incorreta.

2\. Guardrails de bind e autenticação estão mais rigorosos bashCopy code
[code]
    openclaw config get gateway.bindopenclaw config get gateway.auth.modeopenclaw config get gateway.auth.tokenopenclaw gateway statusopenclaw logs --follow
[/code]

O que verificar:

  * Binds não loopback (`lan`, `tailnet`, `custom`) precisam de um caminho válido de autenticação do Gateway: autenticação por token/senha compartilhados ou uma implantação `trusted-proxy` não loopback configurada corretamente.
  * Chaves antigas como `gateway.token` não substituem `gateway.auth.token`.


Assinaturas comuns:

  * `refusing to bind gateway ... without auth` → bind não loopback sem um caminho válido de autenticação do Gateway.
  * `Connectivity probe: failed` enquanto o runtime está em execução → Gateway ativo, mas inacessível com a autenticação/URL atual.

3\. O estado de pareamento e identidade do dispositivo mudou bashCopy code
[code]
    openclaw devices listopenclaw pairing list --channel <channel> [--account <id>]openclaw logs --followopenclaw doctor
[/code]

O que verificar:

  * Aprovações de dispositivo pendentes para dashboard/nodes.
  * Aprovações de pareamento por DM pendentes após mudanças de política ou identidade.


Assinaturas comuns:

  * `device identity required` → autenticação do dispositivo não satisfeita.
  * `pairing required` → remetente/dispositivo deve ser aprovado.


Se a configuração do serviço e o runtime ainda discordarem após as verificações, reinstale os metadados do serviço a partir do mesmo diretório de perfil/estado:

bashCopy code
[code]
    openclaw gateway install --forceopenclaw gateway restart
[/code]

Relacionado:

  * [Autenticação](</pt-BR/gateway/authentication>)
  * [Execução em segundo plano e ferramenta de processo](</pt-BR/gateway/background-process>)
  * [Pareamento pertencente ao Gateway](</pt-BR/gateway/pairing>)


## Relacionado

  * [Doctor](</pt-BR/gateway/doctor>)
  * [FAQ](</pt-BR/help/faq>)
  * [Runbook do Gateway](</pt-BR/gateway>)


Was this useful?YesNo