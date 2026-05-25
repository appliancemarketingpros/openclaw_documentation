---
title: Kontext-Engine
source_url: https://docs.openclaw.ai/de/concepts/context-engine
scraped_at: 2026-05-25
---

Eine **Kontext-Engine** steuert, wie OpenClaw den Modellkontext für jede Ausführung erstellt: welche Nachrichten einbezogen werden, wie ältere Historie zusammengefasst wird und wie Kontext über Subagent-Grenzen hinweg verwaltet wird.

OpenClaw wird mit einer integrierten `legacy`-Engine ausgeliefert und verwendet sie standardmäßig - die meisten Benutzer müssen dies nie ändern. Installieren und wählen Sie eine Plugin-Engine nur dann aus, wenn Sie ein anderes Assembly-, Compaction- oder sitzungsübergreifendes Recall-Verhalten wünschen.

## Schnellstart

* ### Prüfen, welche Engine aktiv ist

bashCopy code
[code]
    openclaw doctor# or inspect config directly:cat ~/.openclaw/openclaw.json | jq '.plugins.slots.contextEngine'
[/code]

* ### Eine Plugin-Engine installieren

Kontext-Engine-Plugins werden wie jedes andere OpenClaw-Plugin installiert.

### Von npm

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### Von einem lokalen Pfad

bashCopy code
[code]
    openclaw plugins install -l ./my-context-engine
[/code]

* ### Die Engine aktivieren und auswählen

json5Copy code
[code]
    // openclaw.json{  plugins: {    slots: {      contextEngine: "lossless-claw", // must match the plugin's registered engine id    },    entries: {      "lossless-claw": {        enabled: true,        // Plugin-specific config goes here (see the plugin's docs)      },    },  },}
[/code]

Starten Sie den Gateway nach Installation und Konfiguration neu.

* ### Zurück zu legacy wechseln (optional)

Setzen Sie `contextEngine` auf `"legacy"` (oder entfernen Sie den Schlüssel vollständig - `"legacy"` ist die Standardeinstellung).

## Funktionsweise

Jedes Mal, wenn OpenClaw einen Modell-Prompt ausführt, beteiligt sich die Kontext-Engine an vier Lebenszykluspunkten:

1\. Erfassen

Wird aufgerufen, wenn der Sitzung eine neue Nachricht hinzugefügt wird. Die Engine kann die Nachricht in ihrem eigenen Datenspeicher speichern oder indexieren.

2\. Zusammensetzen

Wird vor jeder Modellausführung aufgerufen. Die Engine gibt eine geordnete Menge von Nachrichten (und eine optionale `systemPromptAddition`) zurück, die in das Token-Budget passen.

3\. Compact

Wird aufgerufen, wenn das Kontextfenster voll ist oder wenn der Benutzer `/compact` ausführt. Die Engine fasst ältere Historie zusammen, um Platz freizugeben.

4\. Nach dem Turn

Wird aufgerufen, nachdem eine Ausführung abgeschlossen ist. Die Engine kann Zustand persistieren, Hintergrund-Compaction auslösen oder Indizes aktualisieren.

Für das gebündelte Nicht-ACP-Codex-Harness wendet OpenClaw denselben Lebenszyklus an, indem zusammengesetzter Kontext in Codex-Developer-Anweisungen und den Prompt des aktuellen Turns projiziert wird. Codex besitzt weiterhin seine native Thread-Historie und seinen nativen Compactor.

### Subagent-Lebenszyklus (optional)

OpenClaw ruft zwei optionale Subagent-Lebenszyklus-Hooks auf:

Bereitet gemeinsamen Kontextzustand vor, bevor eine untergeordnete Ausführung startet. Der Hook erhält Eltern-/Kind-Sitzungsschlüssel, `contextMode` (`isolated` oder `fork`), verfügbare Transkript-IDs/-Dateien und eine optionale TTL. Wenn er ein Rollback-Handle zurückgibt, ruft OpenClaw dieses auf, wenn das Spawn nach erfolgreicher Vorbereitung fehlschlägt.

Bereinigt, wenn eine Subagent-Sitzung abgeschlossen oder bereinigt wird.

### System-Prompt-Ergänzung

Die Methode `assemble` kann eine Zeichenfolge `systemPromptAddition` zurückgeben. OpenClaw stellt diese dem System-Prompt für die Ausführung voran. Dadurch können Engines dynamische Recall-Anweisungen, Retrieval-Anweisungen oder kontextabhängige Hinweise einfügen, ohne statische Workspace-Dateien zu benötigen.

## Die legacy-Engine

Die integrierte `legacy`-Engine bewahrt das ursprüngliche Verhalten von OpenClaw:

  * **Erfassen** : keine Operation (der Sitzungsmanager übernimmt die Nachrichtenpersistenz direkt).
  * **Zusammensetzen** : Durchreichen (die vorhandene Pipeline sanitize → validate → limit in der Runtime übernimmt das Kontext-Assembly).
  * **Compact** : delegiert an die integrierte Zusammenfassungs-Compaction, die eine einzelne Zusammenfassung älterer Nachrichten erstellt und aktuelle Nachrichten unverändert lässt.
  * **Nach dem Turn** : keine Operation.


Die legacy-Engine registriert keine Tools und stellt keine `systemPromptAddition` bereit.

Wenn kein `plugins.slots.contextEngine` gesetzt ist (oder auf `"legacy"` gesetzt ist), wird diese Engine automatisch verwendet.

## Plugin-Engines

Ein Plugin kann über die Plugin-API eine Kontext-Engine registrieren:

tsCopy code
[code]
     export default function register(api) {  api.registerContextEngine("my-engine", (ctx) => ({    info: {      id: "my-engine",      name: "My Context Engine",      ownsCompaction: true,    },     async ingest({ sessionId, message, isHeartbeat }) {      // Store the message in your data store      return { ingested: true };    },     async assemble({ sessionId, messages, tokenBudget, availableTools, citationsMode }) {      // Return messages that fit the budget      return {        messages: buildContext(messages, tokenBudget),        estimatedTokens: countTokens(messages),        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },     async compact({ sessionId, force }) {      // Summarize older context      return { ok: true, compacted: true };    },  }));}
[/code]

Die Factory `ctx` enthält optionale Werte für `config`, `agentDir` und `workspaceDir`, damit Plugins zustand pro Agent oder Workspace initialisieren können, bevor der erste Lebenszyklus-Hook ausgeführt wird.

Aktivieren Sie sie dann in der Konfiguration:

json5Copy code
[code]
    {  plugins: {    slots: {      contextEngine: "my-engine",    },    entries: {      "my-engine": {        enabled: true,      },    },  },}
[/code]

### Die ContextEngine-Schnittstelle

Erforderliche Member:

Member | Art | Zweck  
---|---|---  
`info` | Property | Engine-ID, Name, Version und ob sie Compaction besitzt  
`ingest(params)` | Methode | Eine einzelne Nachricht speichern  
`assemble(params)` | Methode | Kontext für eine Modellausführung erstellen (gibt `AssembleResult` zurück)  
`compact(params)` | Methode | Kontext zusammenfassen/reduzieren  
  
`assemble` gibt ein `AssembleResult` zurück mit:

Die geordneten Nachrichten, die an das Modell gesendet werden sollen.

Die Schätzung der Engine für die Gesamtzahl der Tokens im zusammengesetzten Kontext. OpenClaw verwendet dies für Entscheidungen über Compaction-Schwellenwerte und Diagnoseberichte.

Wird dem System-Prompt vorangestellt.

Steuert, welche Token-Schätzung der Runner für präventive Überlauf-Vorprüfungen verwendet. Standard ist `"assembled"`, was bedeutet, dass nur die Schätzung des zusammengesetzten Prompts geprüft wird - passend für Engines, die einen fensterbasierten, in sich geschlossenen Kontext zurückgeben. Setzen Sie dies nur dann auf `"preassembly_may_overflow"`, wenn Ihre zusammengesetzte Ansicht ein Überlaufrisiko im zugrunde liegenden Transkript verbergen kann; der Runner verwendet dann das Maximum aus der zusammengesetzten Schätzung und der Vor-Assembly-Schätzung (nicht fensterbasiert) der Sitzungshistorie, wenn er entscheidet, ob präventiv Compact ausgeführt werden soll. In jedem Fall sind die Nachrichten, die Sie zurückgeben, weiterhin das, was das Modell sieht - `promptAuthority` beeinflusst nur die Vorprüfung.

`compact` gibt ein `CompactResult` zurück. Wenn Compaction das aktive Transkript rotiert, identifizieren `result.sessionId` und `result.sessionFile` die Nachfolgesitzung, die der nächste Retry oder Turn verwenden muss.

Optionale Member:

Member | Art | Zweck  
---|---|---  
`bootstrap(params)` | Methode | Engine-Zustand für eine Sitzung initialisieren. Wird einmal aufgerufen, wenn die Engine eine Sitzung erstmals sieht (z. B. Historie importieren).  
`ingestBatch(params)` | Methode | Einen abgeschlossenen Turn als Batch erfassen. Wird nach Abschluss einer Ausführung mit allen Nachrichten dieses Turns auf einmal aufgerufen.  
`afterTurn(params)` | Methode | Lebenszyklusarbeit nach der Ausführung (Zustand persistieren, Hintergrund-Compaction auslösen).  
`prepareSubagentSpawn(params)` | Methode | Gemeinsamen Zustand für eine untergeordnete Sitzung einrichten, bevor sie startet.  
`onSubagentEnded(params)` | Methode | Nach dem Ende eines Subagent bereinigen.  
`dispose()` | Methode | Ressourcen freigeben. Wird während des Gateway-Shutdowns oder Plugin-Reloads aufgerufen - nicht pro Sitzung.  
  
### ownsCompaction

`ownsCompaction` steuert, ob Pis integrierte Auto-Compaction innerhalb eines Versuchs für die Ausführung aktiviert bleibt:

ownsCompaction: true

Die Engine besitzt das Compaction-Verhalten. OpenClaw deaktiviert Pis integrierte Auto-Compaction für diese Ausführung, und die `compact()`-Implementierung der Engine ist verantwortlich für `/compact`, Compaction zur Überlaufwiederherstellung und jede proaktive Compaction, die sie in `afterTurn()` durchführen möchte. OpenClaw kann weiterhin die Überlaufabsicherung vor dem Prompt ausführen; wenn sie vorhersagt, dass das vollständige Transkript überlaufen wird, ruft der Wiederherstellungspfad `compact()` der aktiven Engine auf, bevor ein weiterer Prompt übermittelt wird.

ownsCompaction: false oder nicht gesetzt

Pis integrierte Auto-Compaction kann während der Prompt-Ausführung weiterhin laufen, aber die Methode `compact()` der aktiven Engine wird weiterhin für `/compact` und die Überlaufwiederherstellung aufgerufen.

Das bedeutet, dass es zwei gültige Plugin-Muster gibt:

### Besitzender Modus

Implementieren Sie Ihren eigenen Compaction-Algorithmus und setzen Sie `ownsCompaction: true`.

### Delegierender Modus

Setzen Sie `ownsCompaction: false` und lassen Sie `compact()` `delegateCompactionToRuntime(...)` aus `openclaw/plugin-sdk/core` aufrufen, um das integrierte Compaction-Verhalten von OpenClaw zu verwenden.

Ein No-op-`compact()` ist für eine aktive nicht besitzende Engine unsicher, da es den normalen `/compact`\- und Überlaufwiederherstellungs-Compaction-Pfad für diesen Engine-Slot deaktiviert.

## Konfigurationsreferenz

json5Copy code
[code]
    {  plugins: {    slots: {      // Select the active context engine. Default: "legacy".      // Set to a plugin id to use a plugin engine.      contextEngine: "legacy",    },  },}
[/code]

## Beziehung zu Compaction und Memory

Compaction

Compaction ist eine Zuständigkeit der Context Engine. Die Legacy-Engine delegiert an die integrierte Zusammenfassung von OpenClaw. Plugin-Engines können jede Compaction-Strategie implementieren (DAG-Zusammenfassungen, Vektorabruf usw.).

Memory-Plugins

Memory-Plugins (`plugins.slots.memory`) sind von Context Engines getrennt. Memory-Plugins stellen Suche/Abruf bereit; Context Engines steuern, was das Modell sieht. Sie können zusammenarbeiten - eine Context Engine kann Memory-Plugin-Daten während der Zusammenstellung verwenden. Plugin-Engines, die den Active-Memory-Prompt-Pfad nutzen möchten, sollten `buildMemorySystemPromptAddition(...)` aus `openclaw/plugin-sdk/core` bevorzugen; dies konvertiert die Active-Memory-Prompt-Abschnitte in ein voranstellbares `systemPromptAddition`. Wenn eine Engine Kontrolle auf niedrigerer Ebene benötigt, kann sie weiterhin Rohzeilen aus `openclaw/plugin-sdk/memory-host-core` über `buildActiveMemoryPromptSection(...)` abrufen.

Sitzungsbereinigung

Das Kürzen alter Tool-Ergebnisse im Arbeitsspeicher wird weiterhin ausgeführt, unabhängig davon, welche Context Engine aktiv ist.

## Tipps

  * Verwenden Sie `openclaw doctor`, um zu überprüfen, ob Ihre Engine korrekt geladen wird.
  * Wenn Sie Engines wechseln, werden bestehende Sitzungen mit ihrem aktuellen Verlauf fortgesetzt. Die neue Engine übernimmt für zukünftige Ausführungen.
  * Engine-Fehler werden protokolliert und in der Diagnose angezeigt. Wenn eine Plugin-Engine nicht registriert werden kann oder die ausgewählte Engine-ID nicht aufgelöst werden kann, fällt OpenClaw nicht automatisch zurück; Ausführungen schlagen fehl, bis Sie das Plugin reparieren oder `plugins.slots.contextEngine` wieder auf `"legacy"` umstellen.
  * Verwenden Sie für die Entwicklung `openclaw plugins install -l ./my-engine`, um ein lokales Plugin-Verzeichnis zu verknüpfen, ohne es zu kopieren.


## Verwandte Themen

  * [Compaction](</de/concepts/compaction>) \- lange Konversationen zusammenfassen
  * [Kontext](</de/concepts/context>) \- wie Kontext für Agent-Runden aufgebaut wird
  * [Plugin-Architektur](</de/plugins/architecture>) \- Context-Engine-Plugins registrieren
  * [Plugin-Manifest](</de/plugins/manifest>) \- Felder des Plugin-Manifests
  * [Plugins](</de/tools/plugin>) \- Plugin-Übersicht


Was this useful?YesNo