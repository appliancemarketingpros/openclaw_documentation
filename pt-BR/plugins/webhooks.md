---
title: Plugin de Webhooks
source_url: https://docs.openclaw.ai/pt-BR/plugins/webhooks
scraped_at: 2026-05-25
---

O Plugin Webhooks adiciona rotas HTTP autenticadas que vinculam automações externas a TaskFlows do OpenClaw.

Use-o quando quiser que um sistema confiável, como Zapier, n8n, um job de CI ou um serviço interno, crie e conduza TaskFlows gerenciados sem escrever primeiro um Plugin personalizado.

## Onde ele é executado

O Plugin Webhooks é executado dentro do processo Gateway.

Se o seu Gateway for executado em outra máquina, instale e configure o Plugin nesse host do Gateway e, em seguida, reinicie o Gateway.

## Configurar rotas

Defina a configuração em `plugins.entries.webhooks.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Campos da rota:

  * `enabled`: opcional, o padrão é `true`
  * `path`: opcional, o padrão é `/plugins/webhooks/<routeId>`
  * `sessionKey`: sessão obrigatória proprietária dos TaskFlows vinculados
  * `secret`: segredo compartilhado obrigatório ou SecretRef
  * `controllerId`: id de controlador opcional para fluxos gerenciados criados
  * `description`: observação opcional para o operador


Entradas de `secret` compatíveis:

  * String simples
  * SecretRef com `source: "env" | "file" | "exec"`


Se uma rota baseada em segredo não conseguir resolver seu segredo na inicialização, o Plugin ignora essa rota e registra um aviso em vez de expor um endpoint quebrado.

## Modelo de segurança

Cada rota é confiável para agir com a autoridade de TaskFlow de seu `sessionKey` configurado.

Isso significa que a rota pode inspecionar e modificar TaskFlows pertencentes a essa sessão, portanto você deve:

  * Usar um segredo forte e exclusivo por rota
  * Preferir referências de segredo a segredos em texto simples inline
  * Vincular rotas à sessão mais restrita que se ajuste ao fluxo de trabalho
  * Expor apenas o caminho de Webhook específico de que você precisa


O Plugin aplica:

  * Autenticação por segredo compartilhado
  * Proteções de tamanho e timeout do corpo da solicitação
  * Limitação de taxa por janela fixa
  * Limitação de solicitações em andamento
  * Acesso a TaskFlow vinculado ao proprietário por meio de `api.runtime.tasks.managedFlows.bindSession(...)`


## Formato da solicitação

Envie solicitações `POST` com:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` ou `x-openclaw-webhook-secret: <secret>`


Exemplo:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Ações compatíveis

Atualmente, o Plugin aceita estes valores JSON de `action`:

  * `create_flow`
  * `get_flow`
  * `list_flows`
  * `find_latest_flow`
  * `resolve_flow`
  * `get_task_summary`
  * `set_waiting`
  * `resume_flow`
  * `finish_flow`
  * `fail_flow`
  * `request_cancel`
  * `cancel_flow`
  * `run_task`


### `create_flow`

Cria um TaskFlow gerenciado para a sessão vinculada à rota.

Exemplo:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Cria uma tarefa filha gerenciada dentro de um TaskFlow gerenciado existente.

Os runtimes permitidos são:

  * `subagent`
  * `acp`


Exemplo:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Formato da resposta

Respostas bem-sucedidas retornam:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Solicitações rejeitadas retornam:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

O Plugin remove intencionalmente metadados de proprietário/sessão das respostas de Webhook.

## Documentação relacionada

  * [SDK de runtime de Plugin](</pt-BR/plugins/sdk-runtime>)
  * [Visão geral de hooks e webhooks](</pt-BR/automation/hooks>)
  * [Webhooks da CLI](</pt-BR/cli/webhooks>)


Was this useful?YesNo