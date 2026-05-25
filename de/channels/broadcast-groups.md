---
title: Broadcast-Gruppen
source_url: https://docs.openclaw.ai/de/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Überblick

Broadcast Groups ermöglichen es mehreren Agenten, dieselbe Nachricht gleichzeitig zu verarbeiten und darauf zu antworten. So können Sie spezialisierte Agententeams erstellen, die in einer einzelnen WhatsApp-Gruppe oder DM zusammenarbeiten — alle mit einer Telefonnummer.

Aktueller Umfang: **nur WhatsApp** (Webkanal).

Broadcast Groups werden nach Kanal-Allowlists und Regeln zur Gruppenaktivierung ausgewertet. In WhatsApp-Gruppen bedeutet dies, dass Broadcasts erfolgen, wenn OpenClaw normalerweise antworten würde (zum Beispiel: bei Erwähnung, abhängig von Ihren Gruppeneinstellungen).

## Anwendungsfälle

1\. Specialized agent teams

Stellen Sie mehrere Agenten mit klar abgegrenzten, fokussierten Verantwortlichkeiten bereit:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Jeder Agent verarbeitet dieselbe Nachricht und liefert seine spezialisierte Perspektive.

2\. Multi-language support CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Quality assurance workflows CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Task automation CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Konfiguration

### Grundlegende Einrichtung

Fügen Sie einen `broadcast`-Abschnitt auf oberster Ebene hinzu (neben `bindings`). Schlüssel sind WhatsApp-Peer-IDs:

  * Gruppenchats: Gruppen-JID (z. B. `120363403215116621@g.us`)
  * DMs: E.164-Telefonnummer (z. B. `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Ergebnis:** Wenn OpenClaw in diesem Chat antworten würde, führt es alle drei Agenten aus.

### Verarbeitungsstrategie

Steuern Sie, wie Agenten Nachrichten verarbeiten:

### parallel (default)

Alle Agenten verarbeiten gleichzeitig:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Agenten verarbeiten der Reihe nach (einer wartet, bis der vorherige fertig ist):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Vollständiges Beispiel

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Funktionsweise

### Nachrichtenfluss

* ### Incoming message arrives

Eine WhatsApp-Gruppen- oder DM-Nachricht trifft ein.

* ### Broadcast check

Das System prüft, ob die Peer-ID in `broadcast` enthalten ist.

* ### If in broadcast list

  * Alle aufgeführten Agenten verarbeiten die Nachricht.
  * Jeder Agent hat seinen eigenen Sitzungsschlüssel und isolierten Kontext.
  * Agenten verarbeiten parallel (Standard) oder sequenziell.


* ### If not in broadcast list

Es gilt das normale Routing (erstes passendes Binding).

### Sitzungsisolation

Jeder Agent in einer Broadcast Group verwaltet vollständig separate:

  * **Sitzungsschlüssel** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Unterhaltungsverlauf** (der Agent sieht die Nachrichten anderer Agenten nicht)
  * **Workspace** (separate Sandboxes, falls konfiguriert)
  * **Toolzugriff** (unterschiedliche Allow-/Deny-Listen)
  * **Memory/Kontext** (separate [IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>) usw.)
  * **Gruppenkontextpuffer** (aktuelle Gruppennachrichten, die als Kontext verwendet werden) wird pro Peer gemeinsam genutzt, sodass alle Broadcast-Agenten beim Auslösen denselben Kontext sehen


Dadurch kann jeder Agent Folgendes haben:

  * Unterschiedliche Persönlichkeiten
  * Unterschiedlichen Toolzugriff (z. B. schreibgeschützt vs. Lesen/Schreiben)
  * Unterschiedliche Modelle (z. B. opus vs. sonnet)
  * Unterschiedliche installierte Skills


### Beispiel: isolierte Sitzungen

In Gruppe `120363403215116621@g.us` mit Agenten `["alfred", "baerbel"]`:

### Alfred's context

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Bärbel's context

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Bewährte Vorgehensweisen

1\. Keep agents focused

Entwerfen Sie jeden Agenten mit einer einzelnen, klaren Verantwortung:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Gut:** Jeder Agent hat eine Aufgabe. ❌ **Schlecht:** Ein generischer "dev-helper"-Agent.

2\. Use descriptive names

Machen Sie klar, was jeder Agent tut:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configure different tool access

Geben Sie Agenten nur die Tools, die sie benötigen:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` ist schreibgeschützt. `fixer` kann lesen und schreiben.

4\. Monitor performance

Bei vielen Agenten sollten Sie Folgendes erwägen:

  * `"strategy": "parallel"` (Standard) für Geschwindigkeit verwenden
  * Broadcast Groups auf 5-10 Agenten begrenzen
  * Schnellere Modelle für einfachere Agenten verwenden

5\. Handle failures gracefully

Agenten schlagen unabhängig voneinander fehl. Der Fehler eines Agenten blockiert andere nicht:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Kompatibilität

### Provider

Broadcast Groups funktionieren derzeit mit:

  * ✅ WhatsApp (implementiert)
  * 🚧 Telegram (geplant)
  * 🚧 Discord (geplant)
  * 🚧 Slack (geplant)


### Routing

Broadcast Groups funktionieren zusammen mit vorhandenem Routing:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Nur alfred antwortet (normales Routing).
  * `GROUP_B`: agent1 UND agent2 antworten (Broadcast).


## Fehlerbehebung

Agents not responding

**Prüfen:**

  1. Agenten-IDs existieren in `agents.list`.
  2. Das Peer-ID-Format ist korrekt (z. B. `120363403215116621@g.us`).
  3. Agenten befinden sich nicht in Deny-Listen.


**Debug:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Only one agent responding

**Ursache:** Die Peer-ID könnte in `bindings`, aber nicht in `broadcast` enthalten sein.

**Behebung:** Zur Broadcast-Konfiguration hinzufügen oder aus Bindings entfernen.

Performance issues

Wenn es mit vielen Agenten langsam ist:

  * Reduzieren Sie die Anzahl der Agenten pro Gruppe.
  * Verwenden Sie leichtere Modelle (sonnet statt opus).
  * Prüfen Sie die Sandbox-Startzeit.


## Beispiele

Example 1: Code review team jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Benutzer sendet:** Codeausschnitt.

**Antworten:**

  * code-formatter: "Einrückung korrigiert und Typhinweise hinzugefügt"
  * security-scanner: "⚠️ SQL-Injection-Schwachstelle in Zeile 12"
  * test-coverage: "Abdeckung liegt bei 45 %, Tests für Fehlerfälle fehlen"
  * docs-checker: "Fehlender Docstring für Funktion `process_data`"

Example 2: Multi-language support jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## API-Referenz

### Konfigurationsschema

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Felder

Wie Agenten verarbeitet werden. `parallel` führt alle Agenten gleichzeitig aus; `sequential` führt sie in Array-Reihenfolge aus.

WhatsApp-Gruppen-JID, E.164-Nummer oder andere Peer-ID. Der Wert ist das Array der Agenten-IDs, die Nachrichten verarbeiten sollen.

## Einschränkungen

  1. **Max. Agenten:** Keine harte Begrenzung, aber mehr als 10 Agenten können langsam sein.
  2. **Gemeinsamer Kontext:** Agenten sehen die Antworten der jeweils anderen nicht (absichtlich).
  3. **Nachrichtenreihenfolge:** Parallele Antworten können in beliebiger Reihenfolge eintreffen.
  4. **Ratenlimits:** Alle Agenten zählen zu den WhatsApp-Ratenlimits.


## Zukünftige Verbesserungen

Geplante Funktionen:

  * [ ] Modus mit gemeinsamem Kontext (Agenten sehen die Antworten der jeweils anderen)
  * [ ] Agentenkoordination (Agenten können einander Signale senden)
  * [ ] Dynamische Agentenauswahl (Agenten basierend auf Nachrichteninhalt auswählen)
  * [ ] Agentenprioritäten (einige Agenten antworten vor anderen)


## Verwandte Themen

  * [Kanalrouting](</de/channels/channel-routing>)
  * [Gruppen](</de/channels/groups>)
  * [Multi-Agent-Sandbox-Tools](</de/tools/multi-agent-sandbox-tools>)
  * [Kopplung](</de/channels/pairing>)
  * [Sitzungsverwaltung](</de/concepts/session>)


Was this useful?YesNo