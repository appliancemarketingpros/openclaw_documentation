---
title: Hummer
source_url: https://docs.openclaw.ai/de/tools/lobster
scraped_at: 2026-05-25
---

Lobster ist eine Workflow-Shell, mit der OpenClaw mehrstufige Tool-Sequenzen als eine einzelne, deterministische Operation mit expliziten Genehmigungs-Checkpoints ausführen kann.

Lobster ist eine Autorisierungsebene oberhalb abgekoppelter Hintergrundarbeit. Für Flow-Orchestrierung oberhalb einzelner Aufgaben siehe [TaskFlow](</de/automation/taskflow>) (`openclaw tasks flow`). Für das Aktivitäts-Ledger der Aufgaben siehe [`openclaw tasks`](</de/automation/tasks>).

## Hook

Ihr Assistent kann die Tools bauen, die ihn selbst verwalten. Fragen Sie nach einem Workflow, und 30 Minuten später haben Sie eine CLI plus Pipelines, die als ein einziger Aufruf laufen. Lobster ist das fehlende Stück: deterministische Pipelines, explizite Genehmigungen und fortsetzbarer Zustand.

## Warum

Heute erfordern komplexe Workflows viele Tool-Aufrufe mit Hin und Her. Jeder Aufruf kostet Tokens, und das LLM muss jeden Schritt orchestrieren. Lobster verschiebt diese Orchestrierung in eine typisierte Laufzeitumgebung:

  * **Ein Aufruf statt vieler** : OpenClaw führt einen Lobster-Tool-Aufruf aus und erhält ein strukturiertes Ergebnis.
  * **Genehmigungen integriert** : Seiteneffekte (E-Mail senden, Kommentar posten) halten den Workflow an, bis sie explizit genehmigt werden.
  * **Fortsetzbar** : Angehaltene Workflows geben ein Token zurück; genehmigen und fortsetzen, ohne alles erneut auszuführen.


## Warum eine DSL statt gewöhnlicher Programme?

Lobster ist absichtlich klein. Das Ziel ist nicht „eine neue Sprache“, sondern eine vorhersehbare, KI-freundliche Pipeline-Spezifikation mit erstklassigen Genehmigungen und Resume-Tokens.

  * **Genehmigen/Fortsetzen ist integriert** : Ein normales Programm kann einen Menschen um Eingabe bitten, aber es kann nicht mit einem dauerhaften Token _pausieren und fortgesetzt werden_ , ohne dass Sie diese Laufzeitumgebung selbst erfinden.
  * **Determinismus + Auditierbarkeit** : Pipelines sind Daten, daher lassen sie sich leicht protokollieren, vergleichen, wiederholen und prüfen.
  * **Begrenzte Oberfläche für KI** : Eine kleine Grammatik + JSON-Piping reduziert „kreative“ Codepfade und macht Validierung realistisch.
  * **Sicherheitsrichtlinie integriert** : Timeouts, Ausgabegrenzen, Sandbox-Prüfungen und Allowlists werden von der Laufzeitumgebung erzwungen, nicht von jedem Skript.
  * **Trotzdem programmierbar** : Jeder Schritt kann eine beliebige CLI oder ein Skript aufrufen. Wenn Sie JS/TS möchten, generieren Sie `.lobster`-Dateien aus Code.


## Funktionsweise

OpenClaw führt Lobster-Workflows **in-process** mit einem eingebetteten Runner aus. Es wird kein externer CLI-Subprozess gestartet; die Workflow-Engine läuft innerhalb des Gateway-Prozesses und gibt direkt eine JSON-Hülle zurück. Wenn die Pipeline für eine Genehmigung pausiert, gibt das Tool ein `resumeToken` zurück, damit Sie später fortfahren können.

## Muster: kleine CLI + JSON-Pipes + Genehmigungen

Erstellen Sie kleine Befehle, die JSON sprechen, und verketten Sie sie dann zu einem einzigen Lobster-Aufruf. (Die Beispielbefehlsnamen unten können Sie durch eigene ersetzen.)

bashCopy code
[code]
    inbox list --jsoninbox categorize --jsoninbox apply --json
[/code]

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "exec --json --shell 'inbox list --json' | exec --stdin json --shell 'inbox categorize --json' | exec --stdin json --shell 'inbox apply --json' | approve --preview-from-stdin --limit 5 --prompt 'Apply changes?'",  "timeoutMs": 30000}
[/code]

Wenn die Pipeline eine Genehmigung anfordert, setzen Sie sie mit dem Token fort:

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

KI löst den Workflow aus; Lobster führt die Schritte aus. Genehmigungs-Gates halten Seiteneffekte explizit und auditierbar.

Beispiel: Eingabeelemente in Tool-Aufrufe abbilden:

bashCopy code
[code]
    gog.gmail.search --query 'newer_than:1d' \  | openclaw.invoke --tool message --action send --each --item-key message --args-json '{"provider":"telegram","to":"..."}'
[/code]

## Nur-JSON-LLM-Schritte (llm-task)

Für Workflows, die einen **strukturierten LLM-Schritt** benötigen, aktivieren Sie das optionale Plugin-Tool `llm-task` und rufen Sie es aus Lobster auf. Dadurch bleibt der Workflow deterministisch, während Sie weiterhin mit einem Modell klassifizieren, zusammenfassen oder entwerfen können.

Aktivieren Sie das Tool:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  },  "agents": {    "list": [      {        "id": "main",        "tools": { "alsoAllow": ["llm-task"] }      }    ]  }}
[/code]

### Wichtige Einschränkung: eingebettetes Lobster vs. `openclaw.invoke`

Das gebündelte Lobster-Plugin führt Workflows **in-process** innerhalb des Gateways aus. In diesem eingebetteten Modus erbt `openclaw.invoke` **nicht** automatisch eine Gateway-URL oder einen Authentifizierungskontext für verschachtelte OpenClaw-CLI-Tool-Aufrufe.

Das bedeutet, dass dieses Muster **im eingebetteten Runner derzeit nicht zuverlässig ist** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Verwenden Sie das folgende Beispiel nur, wenn Sie die **eigenständige Lobster-CLI** in einer Umgebung ausführen, in der `openclaw.invoke` bereits mit dem richtigen Gateway-/Authentifizierungskontext konfiguriert ist.

Verwenden Sie es in einer eigenständigen Lobster-CLI-Pipeline:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": { "subject": "Hello", "body": "Can you help?" },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

Wenn Sie heute das eingebettete Lobster-Plugin verwenden, bevorzugen Sie entweder:

  * einen direkten `llm-task`-Tool-Aufruf außerhalb von Lobster oder
  * Nicht-`openclaw.invoke`-Schritte innerhalb der Lobster-Pipeline, bis eine unterstützte eingebettete Bridge hinzugefügt wurde.


Weitere Details und Konfigurationsoptionen finden Sie unter [LLM Task](</de/tools/llm-task>).

## Workflow-Dateien (.lobster)

Lobster kann YAML-/JSON-Workflow-Dateien mit den Feldern `name`, `args`, `steps`, `env`, `condition` und `approval` ausführen. Setzen Sie in OpenClaw-Tool-Aufrufen `pipeline` auf den Dateipfad.

yamlCopy code
[code]
    name: inbox-triageargs:  tag:    default: "family"steps:  - id: collect    command: inbox list --json  - id: categorize    command: inbox categorize --json    stdin: $collect.stdout  - id: approve    command: inbox apply --approve    stdin: $categorize.stdout    approval: required  - id: execute    command: inbox apply --execute    stdin: $categorize.stdout    condition: $approve.approved
[/code]

Hinweise:

  * `stdin: $step.stdout` und `stdin: $step.json` übergeben die Ausgabe eines vorherigen Schritts.
  * `condition` (oder `when`) kann Schritte anhand von `$step.approved` steuern.


## Lobster installieren

Gebündelte Lobster-Workflows laufen in-process; es ist keine separate `lobster`-Binärdatei erforderlich. Der eingebettete Runner wird mit dem Lobster-Plugin ausgeliefert.

Wenn Sie die eigenständige Lobster-CLI für Entwicklung oder externe Pipelines benötigen, installieren Sie sie aus dem [Lobster-Repo](<https://github.com/openclaw/lobster>) und stellen Sie sicher, dass `lobster` in `PATH` liegt.

## Tool aktivieren

Lobster ist ein **optionales** Plugin-Tool (standardmäßig nicht aktiviert).

Empfohlen (additiv, sicher):

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["lobster"]  }}
[/code]

Oder pro Agent:

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "tools": {          "alsoAllow": ["lobster"]        }      }    ]  }}
[/code]

Vermeiden Sie `tools.allow: ["lobster"]`, es sei denn, Sie möchten im restriktiven Allowlist-Modus laufen.

## Beispiel: E-Mail-Triage

Ohne Lobster:

CodeCopy code
[code]
    User: "Check my email and draft replies"→ openclaw calls gmail.list→ LLM summarizes→ User: "draft replies to #2 and #5"→ LLM drafts→ User: "send #2"→ openclaw calls gmail.send(repeat daily, no memory of what was triaged)
[/code]

Mit Lobster:

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "email.triage --limit 20",  "timeoutMs": 30000}
[/code]

Gibt eine JSON-Hülle zurück (gekürzt):

jsonCopy code
[code]
    {  "ok": true,  "status": "needs_approval",  "output": [{ "summary": "5 need replies, 2 need action" }],  "requiresApproval": {    "type": "approval_request",    "prompt": "Send 2 draft replies?",    "items": [],    "resumeToken": "..."  }}
[/code]

Benutzer genehmigt → fortsetzen:

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

Ein Workflow. Deterministisch. Sicher.

## Tool-Parameter

### `run`

Führt eine Pipeline im Tool-Modus aus.

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "gog.gmail.search --query 'newer_than:1d' | email.triage",  "cwd": "workspace",  "timeoutMs": 30000,  "maxStdoutBytes": 512000}
[/code]

Eine Workflow-Datei mit Argumenten ausführen:

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "/path/to/inbox-triage.lobster",  "argsJson": "{\"tag\":\"family\"}"}
[/code]

### `resume`

Einen angehaltenen Workflow nach Genehmigung fortsetzen.

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

### Optionale Eingaben

  * `cwd`: Relatives Arbeitsverzeichnis für die Pipeline (muss innerhalb des Gateway-Arbeitsverzeichnisses bleiben).
  * `timeoutMs`: Bricht den Workflow ab, wenn er diese Dauer überschreitet (Standard: 20000).
  * `maxStdoutBytes`: Bricht den Workflow ab, wenn die Ausgabe diese Größe überschreitet (Standard: 512000).
  * `argsJson`: JSON-String, der an `lobster run --args-json` übergeben wird (nur Workflow-Dateien).


## Ausgabehülle

Lobster gibt eine JSON-Hülle mit einem von drei Status zurück:

  * `ok` → erfolgreich abgeschlossen
  * `needs_approval` → pausiert; `requiresApproval.resumeToken` ist zum Fortsetzen erforderlich
  * `cancelled` → explizit abgelehnt oder abgebrochen


Das Tool stellt die Hülle sowohl in `content` (formatierte JSON) als auch in `details` (Rohobjekt) bereit.

## Genehmigungen

Wenn `requiresApproval` vorhanden ist, prüfen Sie die Eingabeaufforderung und entscheiden Sie:

  * `approve: true` → fortsetzen und Seiteneffekte ausführen
  * `approve: false` → abbrechen und den Workflow abschließen


Verwenden Sie `approve --preview-from-stdin --limit N`, um Genehmigungsanfragen ohne eigenes jq-/heredoc-Glue eine JSON-Vorschau anzuhängen. Resume-Tokens sind jetzt kompakt: Lobster speichert den Workflow-Fortsetzungszustand in seinem Zustandsverzeichnis und gibt einen kleinen Token-Schlüssel zurück.

## OpenProse

OpenProse passt gut zu Lobster: Verwenden Sie `/prose`, um Multi-Agent-Vorbereitung zu orchestrieren, und führen Sie dann eine Lobster-Pipeline für deterministische Genehmigungen aus. Wenn ein Prose-Programm Lobster benötigt, erlauben Sie das `lobster`-Tool für Sub-Agents über `tools.subagents.tools`. Siehe [OpenProse](</de/prose>).

## Sicherheit

  * **Nur lokal in-process** \- Workflows werden innerhalb des Gateway-Prozesses ausgeführt; keine Netzwerkaufrufe durch das Plugin selbst.
  * **Keine Geheimnisse** \- Lobster verwaltet kein OAuth; es ruft OpenClaw-Tools auf, die dies tun.
  * **Sandbox-aware** \- deaktiviert, wenn der Tool-Kontext sandboxed ist.
  * **Gehärtet** \- Timeouts und Ausgabegrenzen werden vom eingebetteten Runner erzwungen.


## Fehlerbehebung

  * **`lobster timed out`** → erhöhen Sie `timeoutMs` oder teilen Sie eine lange Pipeline auf.
  * **`lobster output exceeded maxStdoutBytes`** → erhöhen Sie `maxStdoutBytes` oder reduzieren Sie die Ausgabegröße.
  * **`lobster returned invalid JSON`** → stellen Sie sicher, dass die Pipeline im Tool-Modus läuft und nur JSON ausgibt.
  * **`lobster failed`** → prüfen Sie die Gateway-Logs auf Fehlerdetails des eingebetteten Runners.


## Mehr erfahren

  * [Plugins](</de/tools/plugin>)
  * [Plugin-Tool-Autorisierung](</de/plugins/building-plugins#registering-agent-tools>)


## Fallstudie: Community-Workflows

Ein öffentliches Beispiel: eine „Second Brain“-CLI + Lobster-Pipelines, die drei Markdown-Vaults verwalten (persönlich, Partner, gemeinsam). Die CLI gibt JSON für Statistiken, Inbox-Listen und Scans auf veraltete Inhalte aus; Lobster verkettet diese Befehle zu Workflows wie `weekly-review`, `inbox-triage`, `memory-consolidation` und `shared-task-sync`, jeweils mit Genehmigungs-Gates. KI übernimmt Beurteilung (Kategorisierung), wenn verfügbar, und fällt andernfalls auf deterministische Regeln zurück.

  * Thread: <https://x.com/plattenschieber/status/2014508656335770033>
  * Repo: <https://github.com/bloomedai/brain-cli>


## Verwandt

  * [Automatisierung](</de/automation>) \- Lobster-Workflows planen
  * [Automatisierungsübersicht](</de/automation>) \- alle Automatisierungsmechanismen
  * [Tools-Übersicht](</de/tools>) \- alle verfügbaren Agent-Tools


Was this useful?YesNo