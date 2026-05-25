---
title: Manual de operações do Gateway
source_url: https://docs.openclaw.ai/pt-BR/gateway
scraped_at: 2026-05-25
---

Use esta página para a inicialização do dia 1 e as operações do dia 2 do serviço Gateway.

[**Solução de problemas aprofundada** Diagnósticos orientados por sintoma com sequências exatas de comandos e assinaturas de logs. ](</pt-BR/gateway/troubleshooting>) [**Configuração** Guia de configuração orientado por tarefa + referência completa de configuração. ](</pt-BR/gateway/configuration>) [**Gerenciamento de segredos** Contrato SecretRef, comportamento de snapshot em runtime e operações de migração/recarregamento. ](</pt-BR/gateway/secrets>) [**Contrato do plano de segredos** Regras exatas de destino/caminho de `secrets apply` e comportamento de perfil de autenticação somente por referência. ](</pt-BR/gateway/secrets-plan-contract>)

## Inicialização local em 5 minutos

* ### Inicie o Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Verifique a integridade do serviço

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Linha de base saudável: `Runtime: running`, `Connectivity probe: ok` e `Capability: ...` que corresponde ao que você espera. Use `openclaw gateway status --require-rpc` quando precisar de comprovação de RPC com escopo de leitura, não apenas alcançabilidade.

* ### Valide a prontidão do canal

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Com um Gateway alcançável, isso executa probes de canais por conta ao vivo e auditorias opcionais. Se o Gateway estiver inalcançável, a CLI recorre a resumos de canais somente de configuração em vez da saída de probe ao vivo.

## Modelo de runtime

  * Um processo sempre ativo para roteamento, plano de controle e conexões de canais.
  * Porta única multiplexada para: 
    * Controle/RPC via WebSocket
    * APIs HTTP, compatíveis com OpenAI (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * UI de controle e hooks
  * Modo de bind padrão: `loopback`.
  * A autenticação é exigida por padrão. Configurações com segredo compartilhado usam `gateway.auth.token` / `gateway.auth.password` (ou `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`), e configurações de proxy reverso não loopback podem usar `gateway.auth.mode: "trusted-proxy"`.


## Endpoints compatíveis com OpenAI

A superfície de compatibilidade de maior impacto do OpenClaw agora é:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Por que esse conjunto importa:

  * A maioria das integrações com Open WebUI, LobeChat e LibreChat faz primeiro o probe de `/v1/models`.
  * Muitos pipelines de RAG e memória esperam `/v1/embeddings`.
  * Clientes nativos de agente preferem cada vez mais `/v1/responses`.


Nota de planejamento:

  * `/v1/models` é agent-first: ele retorna `openclaw`, `openclaw/default` e `openclaw/<agentId>`.
  * `openclaw/default` é o alias estável que sempre aponta para o agente padrão configurado.
  * Use `x-openclaw-model` quando quiser substituir o provedor/modelo de backend; caso contrário, o modelo normal e a configuração de embeddings do agente selecionado permanecem no controle.


Todos esses endpoints rodam na porta principal do Gateway e usam o mesmo limite de autenticação de operador confiável que o restante da API HTTP do Gateway.

### Precedência de porta e bind

Configuração | Ordem de resolução  
---|---  
Porta do Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Modo de bind | CLI/sobrescrita → `gateway.bind` → `loopback`  
  
Serviços de Gateway instalados registram o `--port` resolvido nos metadados do supervisor. Depois de alterar `gateway.port`, execute `openclaw doctor --fix` ou `openclaw gateway install --force` para que launchd/systemd/schtasks inicie o processo na nova porta.

A inicialização do Gateway usa a mesma porta efetiva e o mesmo bind quando semeia origens locais da UI de controle para binds não loopback. Por exemplo, `--bind lan --port 3000` semeia `http://localhost:3000` e `http://127.0.0.1:3000` antes da execução da validação de runtime. Adicione explicitamente quaisquer origens de navegador remoto, como URLs de proxy HTTPS, a `gateway.controlUi.allowedOrigins`.

### Modos de recarregamento a quente

`gateway.reload.mode` | Comportamento  
---|---  
`off` | Sem recarregamento de configuração  
`hot` | Aplica somente alterações seguras a quente  
`restart` | Reinicia em alterações que exigem recarregamento  
`hybrid` (padrão) | Aplica a quente quando seguro, reinicia quando necessário  
  
## Conjunto de comandos do operador

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` é para descoberta extra de serviços (LaunchDaemons/unidades systemd do sistema/schtasks), não para um probe de integridade RPC mais profundo.

## Vários gateways (mesmo host)

A maioria das instalações deve executar um Gateway por máquina. Um único Gateway pode hospedar vários agentes e canais.

Você só precisa de vários gateways quando quiser intencionalmente isolamento ou um bot de resgate.

Verificações úteis:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

O que esperar:

  * `gateway status --deep` pode relatar `Other gateway-like services detected (best effort)` e imprimir dicas de limpeza quando instalações obsoletas de launchd/systemd/schtasks ainda existirem.
  * `gateway probe` pode avisar sobre `multiple reachable gateways` quando mais de um destino responde.
  * Se isso for intencional, isole portas, configuração/estado e raízes de workspace por Gateway.


Checklist por instância:

  * `gateway.port` único
  * `OPENCLAW_CONFIG_PATH` único
  * `OPENCLAW_STATE_DIR` único
  * `agents.defaults.workspace` único


Exemplo:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Configuração detalhada: [/gateway/multiple-gateways](</pt-BR/gateway/multiple-gateways>).

## Acesso remoto

Preferido: Tailscale/VPN. Fallback: túnel SSH.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Então conecte clientes localmente a `ws://127.0.0.1:18789`.

Veja: [Gateway remoto](</pt-BR/gateway/remote>), [Autenticação](</pt-BR/gateway/authentication>), [Tailscale](</pt-BR/gateway/tailscale>).

## Supervisão e ciclo de vida do serviço

Use execuções supervisionadas para confiabilidade semelhante à produção.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Use `openclaw gateway restart` para reinicializações. Não encadeie `openclaw gateway stop` e `openclaw gateway start` como substituto de reinicialização.

No macOS, `gateway stop` usa `launchctl bootout` por padrão — isso remove o LaunchAgent da sessão de boot atual sem persistir uma desativação, então a recuperação automática por KeepAlive ainda funciona após falhas inesperadas e `gateway start` reativa tudo de forma limpa. Para suprimir persistentemente o respawn automático entre reinicializações, passe `--disable`: `openclaw gateway stop --disable`.

Os rótulos do LaunchAgent são `ai.openclaw.gateway` (padrão) ou `ai.openclaw.<profile>` (perfil nomeado). `openclaw doctor` audita e repara desvios de configuração do serviço.

### Linux (usuário systemd)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Para persistência após logout, habilite lingering:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Exemplo manual de unidade de usuário quando você precisa de um caminho de instalação personalizado:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (nativo)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

A inicialização gerenciada nativa do Windows usa uma Tarefa Agendada chamada `OpenClaw Gateway` (ou `OpenClaw Gateway (<profile>)` para perfis nomeados). Se a criação da Tarefa Agendada for negada, o OpenClaw recorre a um launcher por usuário na pasta de Inicialização que aponta para `gateway.cmd` dentro do diretório de estado.

### Linux (serviço do sistema)

Use uma unidade do sistema para hosts multiusuário/sempre ativos.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Use o mesmo corpo de serviço da unidade de usuário, mas instale-o em `/etc/systemd/system/openclaw-gateway[-<profile>].service` e ajuste `ExecStart=` se o binário `openclaw` estiver em outro lugar.

Não permita também que `openclaw doctor --fix` instale um serviço de Gateway em nível de usuário para o mesmo perfil/porta. O doctor recusa essa instalação automática quando encontra um serviço de Gateway do OpenClaw em nível de sistema; use `OPENCLAW_SERVICE_REPAIR_POLICY=external` quando a unidade do sistema for dona do ciclo de vida.

## Caminho rápido do perfil de desenvolvimento

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Os padrões incluem estado/configuração isolados e porta base do Gateway `19001`.

## Referência rápida do protocolo (visão do operador)

  * O primeiro frame do cliente deve ser `connect`.
  * O Gateway retorna o snapshot `hello-ok` (`presence`, `health`, `stateVersion`, `uptimeMs`, limites/política).
  * `hello-ok.features.methods` / `events` são uma lista conservadora de descoberta, não um despejo gerado de todas as rotas auxiliares chamáveis.
  * Requisições: `req(method, params)` → `res(ok/payload|error)`.
  * Eventos comuns incluem `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, eventos de ciclo de vida de pareamento/aprovação e `shutdown`.


Execuções de agentes têm duas etapas:

  1. Ack imediato aceito (`status:"accepted"`)
  2. Resposta final de conclusão (`status:"ok"|"error"`), com eventos `agent` transmitidos entre elas.


Veja a documentação completa do protocolo: [Protocolo do Gateway](</pt-BR/gateway/protocol>).

## Verificações operacionais

### Liveness

  * Abra WS e envie `connect`.
  * Espere uma resposta `hello-ok` com snapshot.


### Prontidão

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Recuperação de lacunas

Eventos não são reproduzidos. Em lacunas de sequência, atualize o estado (`health`, `system-presence`) antes de continuar.

## Assinaturas comuns de falha

Assinatura | Problema provável  
---|---  
`refusing to bind gateway ... without auth` | Bind não-loopback sem um caminho de autenticação do Gateway válido  
`another gateway instance is already listening` / `EADDRINUSE` | Conflito de porta  
`Gateway start blocked: set gateway.mode=local` | Configuração definida para modo remoto, ou o carimbo de modo local está ausente de uma configuração danificada  
`unauthorized` during connect | Incompatibilidade de autenticação entre o cliente e o Gateway  
  
Para escadas completas de diagnóstico, use [Solução de problemas do Gateway](</pt-BR/gateway/troubleshooting>).

## Garantias de segurança

  * Clientes do protocolo Gateway falham rapidamente quando o Gateway está indisponível (sem fallback implícito para canal direto).
  * Primeiros frames inválidos/sem conexão são rejeitados e fechados.
  * O encerramento gracioso emite o evento `shutdown` antes do fechamento do socket.


* * *

Relacionado:

  * [Solução de problemas](</pt-BR/gateway/troubleshooting>)
  * [Processo em segundo plano](</pt-BR/gateway/background-process>)
  * [Configuração](</pt-BR/gateway/configuration>)
  * [Integridade](</pt-BR/gateway/health>)
  * [Doctor](</pt-BR/gateway/doctor>)
  * [Autenticação](</pt-BR/gateway/authentication>)


## Relacionado

  * [Configuração](</pt-BR/gateway/configuration>)
  * [Solução de problemas do Gateway](</pt-BR/gateway/troubleshooting>)
  * [Acesso remoto](</pt-BR/gateway/remote>)
  * [Gerenciamento de segredos](</pt-BR/gateway/secrets>)


Was this useful?YesNo