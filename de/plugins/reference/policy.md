---
title: Richtlinien-Plugin
source_url: https://docs.openclaw.ai/de/plugins/reference/policy
scraped_at: 2026-06-29
---

Get started

# Policy-Plugin

Fügt richtliniengestützte Doctor-Prüfungen für die Workspace-Konformität hinzu.

## Distribution

  * Paket: `@openclaw/policy`
  * Installationsweg: in OpenClaw enthalten


## Oberfläche

Plugin

## Verhalten

Das Policy-Plugin stellt Doctor-Integritätsprüfungen für richtlinienverwaltete OpenClaw-Einstellungen und regulierte Workspace-Deklarationen bereit. Policy deckt derzeit Channel-Konformität, regulierte Tool-Metadaten, MCP-Serverstatus, Modell-Provider-Status, Status des Zugriffs auf private Netzwerke, Gateway-Expositionsstatus, Agent-Workspace-/Tool-Status, konfigurierten globalen und agentenspezifischen Tool-Status, konfigurierten Sandbox-Runtime-Status, Ingress-/Channel-Zugriffsstatus, Datenverarbeitungsstatus sowie den Secret-Provider-/Auth-Profilstatus der OpenClaw-Konfiguration ab.

Policy speichert verfasste Anforderungen in `policy.jsonc`, beobachtet vorhandene OpenClaw-Einstellungen und Workspace-Deklarationen als Nachweis und meldet Abweichungen über `openclaw policy check` und `openclaw doctor --lint`. Eine saubere Policy-Prüfung gibt Policy-, Nachweis-, Befund- und Attestierungs-Hashes aus, die Betreiber für Audits aufzeichnen können.

`openclaw policy compare --baseline <file>` vergleicht eine Policy-Datei mit einer anderen Policy-Datei. Dies ist ausschließlich Konformität auf Konfigurationsebene: Es verwendet Policy-Regelmetadaten, um zu prüfen, dass der geprüften Policy nichts fehlt und sie nicht schwächer ist als die verfasste Baseline, und es untersucht weder Runtime-Zustand noch Anmeldedaten oder Secret-Werte.

Tool-Statusregeln können genehmigte Profile, reine Workspace-Dateisystem-Tools, begrenzte exec-Sicherheits-/ask-/host-Einstellungen, deaktivierten Elevated Mode, exakte `alsoAllow`-Einträge und erforderliche Tool-Deny-Einträge verlangen. Die Nachweise erfassen zusätzliche `alsoAllow`-Einträge, weil sie den effektiven Tool-Status erweitern können. Diese Prüfungen beobachten nur die Konfigurationskonformität; sie lesen keinen Runtime-Genehmigungszustand und fügen keine Runtime-Durchsetzung hinzu.

Sandbox-Statusregeln können genehmigte Sandbox-Modi/-Backends verlangen, Host-Container-Netzwerke verbieten, Container-Namespace-Joins verbieten, schreibgeschützte Container-Mounts verlangen, Container-Runtime-Socket-Mounts und unbeschränkte Container-Profile verbieten und Sandbox-Browser-CDP-Quellbereiche verlangen. Diese Prüfungen beobachten nur die Konfigurationskonformität; sie lesen keinen Runtime-Genehmigungszustand, untersuchen keine Live-Container und fügen keine Runtime-Durchsetzung hinzu.

Datenverarbeitungsregeln können die Schwärzung sensibler Protokollierung verlangen, Telemetrie-Inhaltserfassung verbieten, Wartung der Sitzungsaufbewahrung verlangen und Speicherindexierung von Sitzungstranskripten verbieten. Diese Prüfungen beobachten nur die Konfigurationskonformität; sie untersuchen keine Rohprotokolle, Telemetrie-Exporte, Transkripte, Speicherdateien, Secrets oder personenbezogenen Daten.

Benannte Policy-Geltungsbereiche unter `scopes.<scopeName>` können strengere normale Policy-Abschnitte für den Selektor hinzufügen, den sie auflisten. `agentIds` unterstützt `tools`, `agents.workspace`, `sandbox` und `dataHandling.memory`; `channelIds` unterstützt `ingress.channels`. Runtime-Agent-IDs, die nicht ausdrücklich in `agents.list[]` aufgeführt sind, werden gegen den geerbten globalen/standardmäßigen Status geprüft, statt ohne Nachweis stillschweigend zu bestehen. Jeder in `policy.jsonc` vorhandene Geltungsbereich muss für seinen Selektor gültig und durchsetzbar sein. Overlay-Regeln sind zusätzliche Aussagen, daher schwächen sie die Top-Level-Policy nicht ab und können eigene Befunde erzeugen, wenn dieselbe beobachtete Konfiguration gegen beide Geltungsbereiche verstößt.

## Zugehörige Dokumentation

  * [Policy](</de/cli/policy>)


Was this useful?YesNo

Open issue