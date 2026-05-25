---
title: Webhooks-Plugin
source_url: https://docs.openclaw.ai/nl/plugins/webhooks
scraped_at: 2026-05-25
---

De Webhooks Plugin voegt geverifieerde HTTP-routes toe die externe automatisering aan OpenClaw TaskFlows koppelen.

Gebruik het wanneer je wilt dat een vertrouwd systeem zoals Zapier, n8n, een CI-taak of een interne service beheerde TaskFlows maakt en aanstuurt zonder eerst een aangepaste Plugin te schrijven.

## Waar het draait

De Webhooks Plugin draait binnen het Gateway-proces.

Als je Gateway op een andere machine draait, installeer en configureer je de Plugin op die Gateway-host en start je daarna de Gateway opnieuw.

## Routes configureren

Stel de configuratie in onder `plugins.entries.webhooks.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Routevelden:

  * `enabled`: optioneel, standaard `true`
  * `path`: optioneel, standaard `/plugins/webhooks/<routeId>`
  * `sessionKey`: vereiste sessie die eigenaar is van de gekoppelde TaskFlows
  * `secret`: vereist gedeeld geheim of SecretRef
  * `controllerId`: optionele controller-id voor gemaakte beheerde flows
  * `description`: optionele operatornotitie


Ondersteunde `secret`-invoer:

  * Platte tekenreeks
  * SecretRef met `source: "env" | "file" | "exec"`


Als een route met een geheim het geheim bij het opstarten niet kan ophalen, slaat de Plugin die route over en logt een waarschuwing in plaats van een kapot eindpunt bloot te stellen.

## Beveiligingsmodel

Elke route wordt vertrouwd om te handelen met de TaskFlow-bevoegdheid van de geconfigureerde `sessionKey`.

Dit betekent dat de route TaskFlows van die sessie kan inspecteren en wijzigen, dus je moet:

  * Een sterk uniek geheim per route gebruiken
  * Geheimverwijzingen verkiezen boven inline plaintext-geheimen
  * Routes koppelen aan de smalste sessie die bij de workflow past
  * Alleen het specifieke Webhook-pad blootstellen dat je nodig hebt


De Plugin past toe:

  * Verificatie met gedeeld geheim
  * Bewaking van grootte van requestbody en time-outs
  * Rate limiting met vast venster
  * Beperking van gelijktijdige actieve requests
  * Eigenaarsgebonden TaskFlow-toegang via `api.runtime.tasks.managedFlows.bindSession(...)`


## Requestindeling

Stuur `POST`-requests met:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` of `x-openclaw-webhook-secret: <secret>`


Voorbeeld:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Ondersteunde acties

De Plugin accepteert momenteel deze JSON-waarden voor `action`:

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

Maakt een beheerde TaskFlow voor de gekoppelde sessie van de route.

Voorbeeld:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Maakt een beheerde child task binnen een bestaande beheerde TaskFlow.

Toegestane runtimes zijn:

  * `subagent`
  * `acp`


Voorbeeld:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Responsvorm

Geslaagde responses retourneren:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Geweigerde requests retourneren:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

De Plugin verwijdert bewust eigenaars-/sessiemetadata uit Webhook-responses.

## Gerelateerde documentatie

  * [Plugin runtime SDK](</nl/plugins/sdk-runtime>)
  * [Overzicht van hooks en Webhooks](</nl/automation/hooks>)
  * [CLI-Webhooks](</nl/cli/webhooks>)


Was this useful?YesNo