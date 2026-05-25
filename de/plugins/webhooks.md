---
title: Webhooks-Plugin
source_url: https://docs.openclaw.ai/de/plugins/webhooks
scraped_at: 2026-05-25
---

Das Webhooks-Plugin fügt authentifizierte HTTP-Routen hinzu, die externe Automatisierung an OpenClaw TaskFlows binden.

Verwenden Sie es, wenn ein vertrauenswürdiges System wie Zapier, n8n, ein CI-Job oder ein interner Dienst verwaltete TaskFlows erstellen und steuern soll, ohne zuerst ein eigenes Plugin schreiben zu müssen.

## Wo es ausgeführt wird

Das Webhooks-Plugin wird im Gateway-Prozess ausgeführt.

Wenn Ihr Gateway auf einem anderen Computer läuft, installieren und konfigurieren Sie das Plugin auf diesem Gateway-Host und starten Sie anschließend das Gateway neu.

## Routen konfigurieren

Legen Sie die Konfiguration unter `plugins.entries.webhooks.config` fest:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Routenfelder:

  * `enabled`: optional, Standardwert ist `true`
  * `path`: optional, Standardwert ist `/plugins/webhooks/<routeId>`
  * `sessionKey`: erforderliche Sitzung, der die gebundenen TaskFlows gehören
  * `secret`: erforderliches gemeinsames Secret oder SecretRef
  * `controllerId`: optionale Controller-ID für erstellte verwaltete Flows
  * `description`: optionale Betreibernotiz


Unterstützte `secret`-Eingaben:

  * Klartextzeichenfolge
  * SecretRef mit `source: "env" | "file" | "exec"`


Wenn eine Secret-gestützte Route ihr Secret beim Start nicht auflösen kann, überspringt das Plugin diese Route und protokolliert eine Warnung, statt einen fehlerhaften Endpunkt offenzulegen.

## Sicherheitsmodell

Jede Route gilt als vertrauenswürdig, mit der TaskFlow-Autorität ihres konfigurierten `sessionKey` zu handeln.

Das bedeutet, dass die Route TaskFlows prüfen und ändern kann, die dieser Sitzung gehören. Daher sollten Sie:

  * Pro Route ein starkes eindeutiges Secret verwenden
  * Secret-Referenzen gegenüber Inline-Klartext-Secrets bevorzugen
  * Routen an die engste Sitzung binden, die zum Workflow passt
  * Nur den spezifischen Webhook-Pfad freigeben, den Sie benötigen


Das Plugin wendet Folgendes an:

  * Authentifizierung über gemeinsames Secret
  * Schutzmechanismen für Größe und Timeout des Anfragebodys
  * Ratenbegrenzung mit festem Zeitfenster
  * Begrenzung paralleler laufender Anfragen
  * Eigentümergebundener TaskFlow-Zugriff über `api.runtime.tasks.managedFlows.bindSession(...)`


## Anfrageformat

Senden Sie `POST`-Anfragen mit:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` oder `x-openclaw-webhook-secret: <secret>`


Beispiel:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Unterstützte Aktionen

Das Plugin akzeptiert derzeit diese JSON-`action`-Werte:

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

Erstellt einen verwalteten TaskFlow für die gebundene Sitzung der Route.

Beispiel:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Erstellt eine verwaltete untergeordnete Aufgabe innerhalb eines vorhandenen verwalteten TaskFlow.

Zulässige Laufzeitumgebungen sind:

  * `subagent`
  * `acp`


Beispiel:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Antwortform

Erfolgreiche Antworten geben zurück:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Abgelehnte Anfragen geben zurück:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

Das Plugin entfernt absichtlich Eigentümer- und Sitzungsmetadaten aus Webhook-Antworten.

## Verwandte Dokumentation

  * [Plugin-Laufzeit-SDK](</de/plugins/sdk-runtime>)
  * [Übersicht über Hooks und Webhooks](</de/automation/hooks>)
  * [CLI-Webhooks](</de/cli/webhooks>)


Was this useful?YesNo