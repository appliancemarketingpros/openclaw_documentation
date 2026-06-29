---
title: Gateway-Integrationen für externe Apps
source_url: https://docs.openclaw.ai/de/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Externe Apps sollten heute über das Gateway-Protokoll mit OpenClaw kommunizieren. Verwenden Sie Gateway WebSocket und RPC-Methoden, wenn ein Skript, Dashboard, CI-Job, eine IDE- Erweiterung oder ein anderer Prozess Agent-Läufe starten, Ereignisse streamen, auf Ergebnisse warten, Arbeit abbrechen oder Gateway-Ressourcen prüfen möchte.

## Was heute verfügbar ist

Oberfläche | Status | Verwenden Sie sie für  
---|---|---  
[Gateway-Protokoll](</de/gateway/protocol>) | Bereit | WebSocket-Transport, Connect-Handshake, Auth-Bereiche, Protokollversionierung und Ereignisse.  
[Gateway-RPC-Referenz](</de/reference/rpc>) | Bereit | Aktuelle Gateway-Methoden für Agents, Sitzungen, Aufgaben, Modelle, Tools, Artefakte und Genehmigungen.  
[`openclaw agent`](</de/cli/agent>) | Bereit | Einmalige Skriptintegration, wenn der Aufruf über die CLI ausreicht.  
[`openclaw message`](</de/cli/message>) | Bereit | Senden von Nachrichten oder Channel-Aktionen aus Skripten.  
  
Der Quellbaum enthält interne Paketarbeit für eine zukünftige Clientbibliothek, aber das ist keine öffentliche Installationsoberfläche. Behandeln Sie sie als Vorschau- Implementierungsdetail, bis die Pakete veröffentlicht und versioniert sind.

## Empfohlener Weg

  1. Führen Sie ein Gateway aus oder ermitteln Sie eines.
  2. Stellen Sie eine Verbindung über das [Gateway-Protokoll](</de/gateway/protocol>) her.
  3. Rufen Sie dokumentierte RPC-Methoden aus der [Gateway-RPC-Referenz](</de/reference/rpc>) auf.
  4. Pinnen Sie die OpenClaw-Version, gegen die Sie testen.
  5. Prüfen Sie die RPC-Referenz erneut, wenn Sie OpenClaw aktualisieren.


Für Agent-Läufe beginnen Sie mit dem `agent`-RPC und kombinieren ihn mit `agent.wait`, wenn Sie ein terminales Ergebnis benötigen. Für dauerhaften Konversationszustand verwenden Sie die `sessions.*`-Methoden. Für UI-Integrationen abonnieren Sie Gateway-Ereignisse und rendern nur die Ereignisfamilien, die Ihre App versteht.

## App-Code vs. Plugin-Code

Verwenden Sie Gateway-RPC, wenn Code außerhalb von OpenClaw lebt:

  * Node-Skripte, die Agent-Läufe starten oder beobachten
  * CI-Jobs, die ein Gateway aufrufen
  * Dashboards und Admin-Panels
  * IDE-Erweiterungen
  * externe Bridges, die nicht zu Channel-Plugins werden müssen
  * Integrationstests mit gefälschten oder echten Gateway-Transporten


Verwenden Sie das Plugin SDK, wenn Code innerhalb von OpenClaw ausgeführt wird:

  * Provider-Plugins
  * Channel-Plugins
  * Tool- oder Lifecycle-Hooks
  * Agent-Harness-Plugins
  * vertrauenswürdige Runtime-Hilfsfunktionen


Externe Apps sollten `openclaw/plugin-sdk/*` nicht importieren; diese Unterpfade sind für Plugins, die von OpenClaw geladen werden.

## Verwandt

  * [Gateway-Protokoll](</de/gateway/protocol>)
  * [Gateway-RPC-Referenz](</de/reference/rpc>)
  * [CLI-Agent-Befehl](</de/cli/agent>)
  * [CLI-Nachrichtenbefehl](</de/cli/message>)
  * [Agent-Loop](</de/concepts/agent-loop>)
  * [Agent-Runtimes](</de/concepts/agent-runtimes>)
  * [Sitzungen](</de/concepts/session>)
  * [Hintergrundaufgaben](</de/automation/tasks>)
  * [ACP-Agents](</de/tools/acp-agents>)
  * [Plugin SDK-Übersicht](</de/plugins/sdk-overview>)


Was this useful?YesNo

Open issue