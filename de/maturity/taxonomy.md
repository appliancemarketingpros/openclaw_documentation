---
title: Reifegrad-Taxonomie
source_url: https://docs.openclaw.ai/de/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Reifegrad-Taxonomie

das Modell hinter der Scorecard

Oberflächen > Kategorien > Fähigkeiten > Nachweise.

50 Oberflächen, gruppiert in 4 Familien, wobei jede Kategorie auf kanonische Dokumentation und QA-Abdeckungs-IDs zurückgeführt wird.

Produktbereiche durchsuchen / Detaillierte Taxonomie öffnen / [Bewertungen anzeigen](</de/maturity/scorecard>)

## So lesen Sie diese Seite

Eine Oberfläche ist ein Produktbereich wie Gateway-Laufzeit, Discord oder die macOS-App. Jede Oberfläche enthält Kategorien, und jede Kategorie enthält Prüfungen auf Fähigkeitsebene, die von QA-Szenarien abgedeckt werden. Verwenden Sie die Scorecard für Bewertungen auf Release-Ebene; verwenden Sie diese Seite, um das zugrunde liegende Modell zu prüfen.

## Reifegrade

M0GeplantDie Richtung ist bekannt, aber es gibt keinen unterstützten Nutzerpfad.Hochstufung: Design-Issue, Owner und Zieloberfläche existieren.

M1ExperimentellImplementiert mit Einschränkungen, Flags, Source-Builds oder nur für Maintainer vorgesehenen Abläufen.Hochstufung: Maintainer können das Szenario auf dem aktuellen main ausführen.

M2AlphaEchte Nutzer können es ausprobieren, aber breaking changes und unvollständige UX sind zu erwarten.Hochstufung: Dokumentierte Einrichtung, grundlegende Tests, bekannte Einschränkungen und mindestens ein Nachweis in einer realen Umgebung.

M3BetaEin öffentlicher Pfad existiert, und der Hauptworkflow ist mit begrenzten Einschränkungen nutzbar.Hochstufung: Installations-/Update-Dokumentation, Regressionstests, Support-Runbook und erfolgreicher Szenario-Nachweis in der erwarteten Umgebung.

M4StabilEmpfohlener Pfad für normale Nutzer. Fehler werden als Regressionen behandelt.Hochstufung: Release-Gate, Doctor-/Troubleshooting-Pfad, umfassende Dokumentation und wiederholte Nachweise aus der Praxis.

M5ClawesomeAusgereift, angenehm nutzbar, gut instrumentiert und konkurrenzfähig mit dem besten vergleichbaren Workflow.Hochstufung: Stabil plus bestandene Nutzer-Scorecard über repräsentative Nutzer hinweg.

## Produktbereiche

### Kern

CLI M4Stabil7 Bereiche - 90 % abgeschlossen Gateway-Laufzeit M4Stabil13 Bereiche - 89 % abgeschlossen Agent-Laufzeit M3Beta9 Bereiche - 79 % abgeschlossen Sitzungs-, Speicher- und Kontext-Engine M3Beta9 Bereiche - 79 % abgeschlossen Channel-Framework M3Beta8 Bereiche - 79 % abgeschlossen Observability M3Beta5 Bereiche - 79 % abgeschlossen Gateway-Web-App M3Beta6 Bereiche - 79 % abgeschlossen Plugins M3Beta9 Bereiche - 79 % abgeschlossen Sicherheit, Authentifizierung, Pairing und Secrets M3Beta6 Bereiche - 79 % abgeschlossen Automatisierung: Cron, Hooks, Aufgaben, Polling M3Beta6 Bereiche - 79 % abgeschlossen Medienverständnis und Mediengenerierung M2Alpha6 Bereiche - 68 % abgeschlossen Sprache und Echtzeitgespräch M2Alpha6 Bereiche - 68 % abgeschlossen TUI M2Alpha5 Bereiche - 66 % abgeschlossen ClawHub M2Alpha4 Bereiche - 62 % abgeschlossen OpenClaw App SDK M2Alpha6 Bereiche - 53 % abgeschlossen

### Plattform

Linux-Gateway-Host M4Stabil5 Bereiche - 89 % abgeschlossen macOS-Gateway-Host M4Stabil7 Bereiche - 88 % abgeschlossen Docker- und Podman-Hosting M3Beta4 Bereiche - 79 % abgeschlossen Windows über WSL2 M3Beta6 Bereiche - 79 % abgeschlossen Raspberry Pi und kleine Linux-Geräte M3Beta4 Bereiche - 79 % abgeschlossen macOS-Begleit-App M3Beta8 Bereiche - 78 % abgeschlossen Android-App M2Alpha7 Bereiche - 66 % abgeschlossen Natives Windows M2Alpha4 Bereiche - 66% abgeschlossen Kubernetes-Hosting M2Alpha4 Bereiche - 61% abgeschlossen iOS-App M1Experimentell8 Bereiche - 44% abgeschlossen Nix-Installationspfad M1Experimentell5 Bereiche - 44% abgeschlossen watchOS-Begleitoberflächen M1Experimentell5 Bereiche - 44% abgeschlossen Linux-Begleit-App M0Geplant5 Bereiche - 21% abgeschlossen Native Windows-Begleit-App M0Geplant5 Bereiche - 21% abgeschlossen

### Kanal

Discord M4Stabil6 Bereiche - 87% abgeschlossen Telegram M3Beta5 Bereiche - 78% abgeschlossen Slack M3Beta5 Bereiche - 78% abgeschlossen iMessage und BlueBubbles M3Beta5 Bereiche - 78% abgeschlossen WhatsApp M3Beta5 Bereiche - 78% abgeschlossen Matrix M2Alpha6 Bereiche - 67% abgeschlossen Google Chat M2Alpha5 Bereiche - 66% abgeschlossen Microsoft Teams M2Alpha5 Bereiche - 66% abgeschlossen Signal M2Alpha5 Bereiche - 66% abgeschlossen Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale Kanäle M2Alpha4 Bereiche - 58% abgeschlossen Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 Bereiche - 54% abgeschlossen Sprachanrufkanal M1Experimentell5 Bereiche - 44% abgeschlossen

### Provider und Tool

Browserautomatisierung, exec und Sandbox-Tools M3Beta3 Bereiche - 79% abgeschlossen OpenAI- und Codex-Provider-Pfad M3Beta5 Bereiche - 79% abgeschlossen Websuche-Tools M3Beta4 Bereiche - 79% abgeschlossen Anthropic-Provider-Pfad M3Beta5 Bereiche - 78% abgeschlossen Google-Provider-Pfad M3Beta5 Bereiche - 78% abgeschlossen OpenRouter-Provider-Pfad M3Beta4 Bereiche - 78% abgeschlossen Tools zur Bild-, Video- und Musikgenerierung M2Alpha5 Bereiche - 68% abgeschlossen Lokale Modell-Provider: Ollama, vLLM, SGLang, LM Studio M2Alpha5 Bereiche - 68% abgeschlossen Gehostete Long-Tail-Provider M2Alpha3 Bereiche - 68% abgeschlossen

## Details

### Kern

CLI - M4 Stabil - 7 Bereiche

Normale Einrichtungs- und Reparaturpfade sind in den Installations-, CLI- und Gateway-Dokumenten dokumentiert. Plattformspezifische Windows-Pfade werden in den Zeilen „Windows über WSL2“ und „Natives Windows“ verfolgt.

Abdeckung Experimentell - 4%Qualität Stabil - 83%Vollständigkeit Stabil - 90%Teilweise - 6

CLI-Einrichtung 6 Funktionen / LTS-unterstützt

Experimentell17%

Stabil89%

Stabil90%

[Index](</de/install>), [Installationsprogramm](</de/install/installer>), [Node](</de/install/node>), [Aktualisierung](</de/install/updating>)

Onboarding und Auth-Einrichtung 5 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Onboarding](</de/cli/onboard>), [Konfigurieren](</de/cli/configure>), [Onboarding-Überblick](</de/start/onboarding-overview>)

Plugin- und Kanaleinrichtung 5 Funktionen

Experimentell0%

Beta75%

Stabil89%

[Onboarding](</de/cli/onboard>), [Plugins](</de/cli/plugins>), [Kanäle](</de/cli/channels>)

Gateway-Dienstverwaltung 5 Funktionen / LTS-unterstützt

Experimentell14%

Stabil87%

Stabil90%

[Gateway](</de/cli/gateway>), [Aktualisierung](</de/install/updating>), [Fehlerbehebung](</de/gateway/troubleshooting>)

CLI-Beobachtbarkeit 5 Funktionen / LTS-unterstützt

Experimentell0%

Stabil89%

Stabil90%

[Status](</de/cli/status>), [Integrität](</de/cli/health>), [Protokolle](</de/cli/logs>), [Diagnose](</de/gateway/diagnostics>)

Doctor 10 Funktionen / LTS-unterstützt

Experimentell0%

Stabil89%

Stabil90%

[Doctor](</de/cli/doctor>), [Doctor](</de/gateway/doctor>), [Geheimnisse](</de/gateway/secrets>), [Fehlerbehebung](</de/gateway/troubleshooting>)

Updates und Upgrades 5 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Aktualisierung](</de/install/updating>), [Update](</de/cli/update>), [Fehlerbehebung](</de/gateway/troubleshooting>)

Gateway-Laufzeit - M4 Stabil - 13 Bereiche

Kernarchitektur, Auth, Kopplung, Protokolldokumentation, Daemon-Dokumentation und CLI-Runbooks sind umfassend und aktuell.

Abdeckung Experimentell - 6%Qualität Stabil - 81%Vollständigkeit Stabil - 89%Teilweise - 12

Genehmigungen und Remote-Ausführung 6 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Protokoll](</de/gateway/protocol>), [Index](</de/gateway/security>)

HTTP-APIs 4 Funktionen / LTS-unterstützt

Experimentell25%

Stabil90%

Stabil90%

[Index](</de/gateway>), [OpenAI-HTTP-API](</de/gateway/openai-http-api>), [Openresponses-HTTP-API](</de/gateway/openresponses-http-api>), [HTTP-API für Tool-Aufrufe](</de/gateway/tools-invoke-http-api>), [Hooks](</de/automation/hooks>), [Index](</de/web>)

Gehostete Web-Oberfläche 4 Funktionen / LTS-unterstützt

Experimentell0%

Stabil89%

Stabil90%

[Index](</de/gateway>), [Architektur](</de/concepts/architecture>), [Control-UI](</de/web/control-ui>), [Webchat](</de/web/webchat>), [Canvas](</de/refactor/canvas>)

Gateway-RPC-APIs und Ereignisse 20 Funktionen / LTS-unterstützt

Experimentell9%

Stabil90%

Stabil90%

[Protokoll](</de/gateway/protocol>), [Index](</de/gateway>), [Architektur](</de/concepts/architecture>)

Geräteauthentifizierung und Pairing 10 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Protokoll](</de/gateway/protocol>), [Pairing](</de/gateway/pairing>), [Index](</de/gateway/security>)

Netzwerkzugriff und Discovery 6 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Index](</de/gateway>), [Discovery](</de/gateway/discovery>), [Protokoll](</de/gateway/protocol>)

Nodes und Remote-Funktionen 8 Funktionen

Experimentell0%

Beta75%

Stabil89%

[Protokoll](</de/gateway/protocol>), [Architektur](</de/concepts/architecture>), [Index](</de/nodes>)

Zustand, Diagnose und Reparatur 7 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Index](</de/gateway>), [Diagnose](</de/gateway/diagnostics>), [Doctor](</de/gateway/doctor>)

Protokollkompatibilität 7 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Protokoll](</de/gateway/protocol>), [Architektur](</de/concepts/architecture>), [Typebox](</de/concepts/typebox>), [Bridge-Protokoll](</de/gateway/bridge-protocol>)

Rollen und Berechtigungen 5 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Protokoll](</de/gateway/protocol>), [Index](</de/gateway/security>)

Gateway-Lebenszyklus 7 Funktionen / LTS-unterstützt

Experimentell33%

Stabil90%

Stabil90%

[Index](</de/gateway>), [Architektur](</de/concepts/architecture>)

Sicherheitskontrollen 6 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Index](</de/gateway/security>), [Protokoll](</de/gateway/protocol>), [Discovery](</de/gateway/discovery>)

WebSocket-Verbindung 8 Funktionen / LTS-unterstützt

Experimentell13%

Stabil90%

Stabil90%

[Protokoll](</de/gateway/protocol>), [Architektur](</de/concepts/architecture>)

Agent Runtime - M3 Beta - 9 Bereiche

Main Loop, Modelle, Provider-Routing und Tool-Streaming sind erstklassig unterstützt, aber das Provider-Verhalten ändert sich wöchentlich und erfordert Szenario-Nachweise pro Release.

Abdeckung experimentell - 33%Qualität Beta - 78%Vollständigkeit Beta - 79%Teilweise - 6

Agent-Turn-Ausführung 3 Fähigkeiten / LTS-unterstützt

Experimentell29%

Beta79%

Beta79%

[Agenten-Loop](</de/concepts/agent-loop>), [Agent](</de/cli/agent>), [Agent-Runtimes](</de/concepts/agent-runtimes>)

Externe Runtimes und Subagenten 4 Fähigkeiten

Experimentell30%

Beta79%

Beta79%

[Agent-Runtimes](</de/concepts/agent-runtimes>), [Anthropic](</de/providers/anthropic>), [Google](</de/providers/google>), [Subagenten](</de/tools/subagents>)

Ausführung über gehostete Provider 5 Fähigkeiten / LTS-unterstützt

Experimentell20%

Beta79%

Beta79%

[Openai](</de/providers/openai>), [Anthropic](</de/providers/anthropic>), [Google](</de/providers/google>), [Modelle](</de/concepts/models>)

Lokale und selbst gehostete Provider 5 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Ollama](</de/providers/ollama>), [Modelle](</de/concepts/models>), [Agent](</de/cli/agent>)

Modell- und Runtime-Auswahl 4 Fähigkeiten / LTS-unterstützt

Experimentell25%

Beta79%

Beta79%

[Modelle](</de/concepts/models>), [Modelle](</de/cli/models>), [Openai](</de/providers/openai>), [Agent-Runtimes](</de/concepts/agent-runtimes>)

Provider-Authentifizierung 10 Fähigkeiten / LTS-unterstützt

Experimentell24%

Beta79%

Beta79%

[Modelle](</de/concepts/models>), [Agent](</de/cli/agent>), [Modelle](</de/cli/models>), [Openai](</de/providers/openai>), [Anthropic](</de/providers/anthropic>), [Google](</de/providers/google>), [Subagenten](</de/tools/subagents>)

Streaming und Fortschritt 2 Fähigkeiten

Alpha56%

Beta79%

Beta79%

[Streaming](</de/concepts/streaming>), [Agenten-Loop](</de/concepts/agent-loop>)

Tool-Aufrufe und Antwortverarbeitung 3 Fähigkeiten / LTS-unterstützt

Alpha65%

Beta79%

Beta79%

[Agenten-Loop](</de/concepts/agent-loop>), [Ollama](</de/providers/ollama>)

Steuerung der Tool-Ausführung 6 Funktionen / LTS-unterstützt

Alpha50%

Beta79%

Beta79%

[Sandbox vs. Tool-Richtlinie vs. Erhöht](</de/gateway/sandbox-vs-tool-policy-vs-elevated>), [Agent-Loop](</de/concepts/agent-loop>), [Subagents](</de/tools/subagents>)

Sitzung, Speicher und Kontext-Engine - M3 Beta - 9 Bereiche

Solide Dokumentation und aktive Implementierung. Die Reife hängt von der Dauerhaftigkeit der Transkripte, der Qualität der Compaction und der Parität über Clients hinweg ab.

Abdeckung experimentell - 30%Qualität Beta - 77%Vollständigkeit Beta - 79%Teilweise - 6

CLI-Sitzungs- und Transkriptverwaltung 2 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Sitzung](</de/concepts/session>), [Sitzungsverwaltung mit Compaction](</de/reference/session-management-compaction>), [Sitzungen](</de/cli/sessions>)

Token-Verwaltung 3 Funktionen / LTS-unterstützt

Experimentell20%

Beta79%

Beta79%

[Compaction](</de/concepts/compaction>), [Kontext](</de/concepts/context>), [Sitzungsverwaltung mit Compaction](</de/reference/session-management-compaction>)

Kontext-Engine 2 Funktionen / LTS-unterstützt

Alpha57%

Beta79%

Beta79%

[Kontext](</de/concepts/context>), [Kontext-Engine](</de/concepts/context-engine>), [Codex-Kontext-Engine-Harness](</de/plan/codex-context-engine-harness>)

Clientübergreifender Verlauf und Sitzungsparität 2 Funktionen

Experimentell40%

Beta79%

Beta79%

[Webchat](</de/web/webchat>), [Android](</de/platforms/android>), [Kanalrouting](</de/channels/channel-routing>)

Diagnose, Wartung und Wiederherstellung 3 Funktionen

Experimentell40%

Beta79%

Beta79%

[Diagnose](</de/gateway/diagnostics>), [Sitzungsverwaltung mit Compaction](</de/reference/session-management-compaction>), [Flags](</de/diagnostics/flags>)

Kern-Prompts und Kontext 2 Funktionen / LTS-unterstützt

Experimentell38%

Beta79%

Beta79%

[Kontext](</de/concepts/context>), [Transkript-Hygiene](</de/reference/transcript-hygiene>), [Discord](</de/channels/discord>)

Speicher 5 Funktionen

Experimentell46%

Beta79%

Beta79%

[Speicherkonfiguration](</de/reference/memory-config>), [Memory Qmd](</de/concepts/memory-qmd>), [Speicher](</de/concepts/memory>), [Discord](</de/channels/discord>)

Sitzungsrouting 2 Funktionen / LTS-unterstützt

Experimentell25%

Beta79%

Beta79%

[Sitzung](</de/concepts/session>), [Kanalrouting](</de/channels/channel-routing>), [Discord](</de/channels/discord>)

Persistenz von Transkripten 2 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Sitzungsverwaltung: Compaction](</de/reference/session-management-compaction>), [Transkripthygiene](</de/reference/transcript-hygiene>)

Channel-Framework - M3 Beta - 8 Bereiche

Viele Kanäle teilen Gateway-Zustellungs- und Routing-Verträge, aber das Kanalverhalten variiert je nach Upstream-API und Einschränkungen durch Kontorichtlinien.

Abdeckung experimentell - 13%Qualität Beta - 76%Vollständigkeit Beta - 79%Teilweise - 5

Kanalaktionsbefehle und Genehmigungen 5 Funktionen

Experimentell0%

Beta79%

Beta79%

[Gruppen](</de/channels/groups>), [Discord](</de/channels/discord>), [Google Chat](</de/channels/googlechat>), [Signal](</de/channels/signal>), [Matrix](</de/channels/matrix>)

Kanaleinrichtung 5 Funktionen / LTS-unterstützt

Experimentell14%

Beta79%

Beta79%

[Index](</de/channels>), [Kopplung](</de/channels/pairing>), [Fehlerbehebung](</de/channels/troubleshooting>), [SDK-Kanal-Plugins](</de/plugins/sdk-channel-plugins>)

Gruppen-Threads und Verhalten in Ambient Rooms 5 Funktionen

Experimentell36%

Beta79%

Beta79%

[Gruppen](</de/channels/groups>), [Gruppennachrichten](</de/channels/group-messages>), [Ambient-Room-Ereignisse](</de/channels/ambient-room-events>), [Broadcast-Gruppen](</de/channels/broadcast-groups>), [Discord](</de/channels/discord>)

Eingehender Zugriff und Identitäts-Gates 5 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Zugriffsgruppen](</de/channels/access-groups>), [Gruppen](</de/channels/groups>), [Discord](</de/channels/discord>), [LINE](</de/channels/line>)

Medienanhänge und umfangreiche Kanaldaten 4 Funktionen

Experimentell0%

Alpha68%

Beta79%

[LINE](</de/channels/line>), [Signal](</de/channels/signal>), [Google Chat](</de/channels/googlechat>), [Matrix](</de/channels/matrix>), [Discord](</de/channels/discord>)

Ausgehende Zustellung und Antwort-Pipeline 4 Funktionen / LTS-unterstützt

Experimentell38%

Beta79%

Beta79%

[Gruppen](</de/channels/groups>), [Ambient-Room-Ereignisse](</de/channels/ambient-room-events>), [Discord](</de/channels/discord>), [Matrix](</de/channels/matrix>), [Konfigurationskanäle](</de/gateway/config-channels>)

Konversationsrouting und Zustellung 10 Funktionen / LTS-unterstützt

Experimentell19%

Beta79%

Beta79%

[Kanalrouting](</de/channels/channel-routing>), [Gruppen](</de/channels/groups>), [Discord](</de/channels/discord>), [Matrix](</de/channels/matrix>), [Fehlerbehebung](</de/channels/troubleshooting>), [Konfigurationsreferenz](</de/gateway/configuration-reference>)

Statuszustand und Operator-Steuerungen 4 Funktionen / LTS-unterstützt

Experimentell0%

Beta79%

Beta79%

[Status](</de/gateway/health>), [Konfigurationsreferenz](</de/gateway/configuration-reference>), [Fehlerbehebung](</de/channels/troubleshooting>), [Discord](</de/channels/discord>)

Observability - M3 Beta - 5 areas

Dokumentation zu OTel, Prometheus, Logging und Diagnose ist vorhanden. Benötigt einen öffentlichen Reifegrad-Durchlauf dazu, „worauf Betreiber zuerst achten sollten“.

Abdeckung Experimental - 18%Qualität Beta - 75%Vollständigkeit Beta - 79%Teilweise - 3

Zustand und Reparatur 12 Funktionen / LTS-unterstützt

Experimental28%

Beta79%

Beta79%

[Zustand](</de/gateway/health>), [Telegram](</de/channels/telegram>), [Doctor](</de/cli/doctor>), [Doctor](</de/gateway/doctor>), [SDK-Unterpfade](</de/plugins/sdk-subpaths>), [Zustand](</de/cli/health>), [Protokoll](</de/gateway/protocol>)

Protokollierung 5 Funktionen / LTS-unterstützt

Experimental0%

Alpha68%

Beta79%

[Protokollierung](</de/logging>), [Protokollierung](</de/gateway/logging>), [Protokolle](</de/cli/logs>)

Diagnosesammlung 8 Funktionen

Experimental30%

Beta79%

Beta79%

[Diagnosen](</de/gateway/diagnostics>), [Zustand](</de/gateway/health>), [Codex Harness](</de/plugins/codex-harness>), [Protokoll](</de/gateway/protocol>)

Telemetry-Export 13 Funktionen

Experimental33%

Beta79%

Beta79%

[Hooks](</de/plugins/hooks>), [Opentelemetry](</de/gateway/opentelemetry>), [Protokollierung](</de/logging>), [SDK-Unterpfade](</de/plugins/sdk-subpaths>), [Diagnostics Otel](</de/plugins/reference/diagnostics-otel>), [Prometheus](</de/gateway/prometheus>), [Diagnostics Prometheus](</de/plugins/reference/diagnostics-prometheus>)

Sitzungsdiagnosen 4 Funktionen / LTS-unterstützt

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</de/gateway/opentelemetry>), [Prometheus](</de/gateway/prometheus>), [Diagnosen](</de/gateway/diagnostics>), [Protokoll](</de/gateway/protocol>)

Gateway-Web-App - M3 Beta - 6 Bereiche

Die Web-UI ist mit Pairing-, Chat-, PWA-, Talk-, Push- und Remote-Gateway-Flows dokumentiert. Nach Cross-Browser- und Mobil-PWA-Scorecards hochstufen.

Abdeckung Experimental - 4%Qualität Beta - 74%Vollständigkeit Beta - 79%Keine

Browser-Echtzeitgespräch 5 Funktionen

Experimentell0%

Alpha68%

Beta79%

[Control UI](</de/web/control-ui>), [Protokoll](</de/gateway/protocol>), [Talk](</de/nodes/talk>)

Browser-Zugriff und Vertrauen 5 Funktionen

Experimentell0%

Alpha68%

Beta79%

[Control UI](</de/web/control-ui>), [Dashboard](</de/web/dashboard>), [Tailscale](</de/gateway/tailscale>), [Remote](</de/gateway/remote>)

Konfiguration 5 Funktionen

Experimentell0%

Alpha68%

Beta79%

[Control UI](</de/web/control-ui>), [Konfiguration](</de/gateway/configuration>)

Browser-UI 10 Funktionen

Experimentell8%

Beta79%

Beta79%

[Control UI](</de/web/control-ui>), [Index](</de/web>), [Dashboard](</de/web/dashboard>), [Protokoll](</de/gateway/protocol>)

WebChat-Unterhaltungen 15 Funktionen

Experimentell10%

Beta79%

Beta79%

[Control UI](</de/web/control-ui>), [Webchat](</de/web/webchat>), [Erste Schritte](</de/start/getting-started>), [Channel-Routing](</de/channels/channel-routing>), [Sichere Dateioperationen](</de/gateway/security/secure-file-operations>)

Operator-Konsole 10 Funktionen

Experimentell8%

Beta79%

Beta79%

[Control UI](</de/web/control-ui>), [Integrität](</de/gateway/health>), [Protokoll](</de/gateway/protocol>), [Dashboard](</de/web/dashboard>)

Plugins - M3 Beta - 9 Bereiche

Umfassende Dokumentation und starke interne Runtime-Nachweise liegen über Manifeste, Discovery, Laden, Provider-/Tool-Architektur und Freigabegrenzen hinweg vor. Belassen Sie die Zeile auf Beta, bis die öffentliche SDK-API/-Unterpfade und Nachweise für externe Distribution stärker sind.

Abdeckung Experimentell - 12%Qualität Beta - 72%Vollständigkeit Beta - 79%Teilweise - 7

Erstellen und Paketieren von Plugins 8 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Plugins erstellen](</de/plugins/building-plugins>), [SDK-Übersicht](</de/plugins/sdk-overview>), [SDK-Einstiegspunkte](</de/plugins/sdk-entrypoints>), [SDK-Unterpfade](</de/plugins/sdk-subpaths>), [Manifest](</de/plugins/manifest>), [Referenz](</de/plugins/reference>)

Gebündelte Plugins 5 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Plugin-Bestand](</de/plugins/plugin-inventory>), [Plugins](</de/cli/plugins>), [Architektur-Interna](</de/plugins/architecture-internals>)

Canvas-Plugin 6 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Canvas](</de/plugins/reference/canvas>), [Canvas](</de/refactor/canvas>), [Konfigurationsreferenz](</de/gateway/configuration-reference>)

Installieren und Ausführen von Plugins 6 Fähigkeiten / LTS-unterstützt

Experimentell35%

Beta79%

Beta79%

[Architektur](</de/plugins/architecture>), [Architektur-Interna](</de/plugins/architecture-internals>), [Plugins](</de/cli/plugins>)

Channel-Plugins 5 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[SDK-Channel-Plugins](</de/plugins/sdk-channel-plugins>), [SDK-Channel-Eingang](</de/plugins/sdk-channel-inbound>), [SDK-Channel-Ausgang](</de/plugins/sdk-channel-outbound>)

Provider- und Tool-Plugins 6 Fähigkeiten / LTS-unterstützt

Experimentell43%

Beta79%

Beta79%

[SDK-Provider-Plugins](</de/plugins/sdk-provider-plugins>), [Tool-Plugins](</de/plugins/tool-plugins>), [Fähigkeiten hinzufügen](</de/plugins/adding-capabilities>)

Plugin-Genehmigungen 6 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Plugin-Berechtigungsanfragen](</de/plugins/plugin-permission-requests>), [Exec-Genehmigungen](</de/tools/exec-approvals>), [SDK-Channel-Plugins](</de/plugins/sdk-channel-plugins>)

Veröffentlichen von Plugins 6 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Plugins](</de/cli/plugins>), [Kompatibilität](</de/plugins/compatibility>), [Veröffentlichung](</de/clawhub/publishing>)

Plugins testen 6 Fähigkeiten

Experimentell27%

Beta79%

Beta79%

[SDK-Tests](</de/plugins/sdk-testing>), [SDK-Einrichtung](</de/plugins/sdk-setup>), [Codex Harness](</de/plugins/codex-harness>)

Sicherheit, Authentifizierung, Pairing und Secrets - M3 Beta - 6 Bereiche

Gute Dokumentation und Härtungsflächen sind vorhanden. Nach regelmäßigen Upgrade- und Sicherheitsszenario-Läufen hochstufen, wenn diese keine Setup-Regressionen nachweisen.

Abdeckung Experimentell - 16%Qualität Beta - 72%Vollständigkeit Beta - 79%Teilweise - 5

Genehmigungsrichtlinie und Tool-Schutzmaßnahmen 2 Funktionen / LTS-unterstützt

Alpha50%

Beta79%

Beta79%

[Exec-Genehmigungen](</de/tools/exec-approvals>), [Genehmigungen](</de/cli/approvals>), [Plugin-Berechtigungsanfragen](</de/plugins/plugin-permission-requests>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Gateway-Authentifizierung und Remote-Zugriff 9 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Index](</de/gateway/security>), [Exposure-Runbook](</de/gateway/security/exposure-runbook>), [Trusted Proxy Auth](</de/gateway/trusted-proxy-auth>), [Tailscale](</de/gateway/tailscale>), [Remote](</de/gateway/remote>), [Konfigurationsreferenz](</de/gateway/configuration-reference>), [Gateway](</de/cli/gateway>), [Doctor](</de/cli/doctor>), [Control UI](</de/web/control-ui>), [Browsersteuerung](</de/tools/browser-control>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Channel-Zugriffskontrolle 3 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Pairing](</de/channels/pairing>), [Telegram](</de/channels/telegram>), [Zugriffsgruppen](</de/channels/access-groups>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Geräte- und Node-Pairing 11 Funktionen / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Protokoll](</de/gateway/protocol>), [Geräte](</de/cli/devices>), [Pairing](</de/channels/pairing>), [Pairing](</de/gateway/pairing>), [Operator-Bereiche](</de/gateway/operator-scopes>), [Control UI](</de/web/control-ui>), [Webchat](</de/web/webchat>), [Genehmigungen](</de/cli/approvals>)

Plugin-Vertrauen 2 Funktionen

Experimentell0%

Alpha68%

Beta79%

[Manifest](</de/plugins/manifest>), [Plugin-Berechtigungsanfragen](</de/plugins/plugin-permission-requests>), [Plugins verwalten](</de/plugins/manage-plugins>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Hygiene für Zugangsdaten und Secrets 5 Funktionen / LTS-unterstützt

Experimentell46%

Beta79%

Beta79%

[Authentifizierung](</de/gateway/authentication>), [Modelle](</de/cli/models>), [OpenAI](</de/providers/openai>), [OAuth](</de/concepts/oauth>), [Secrets](</de/gateway/secrets>), [Secrets](</de/cli/secrets>), [Secretref-Zugangsdatenfläche](</de/reference/secretref-credential-surface>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Automatisierung: Cron, Hooks, Aufgaben, Polling - M3 Beta - 6 Bereiche

Dokumentiert und nutzbar, aber Szenarionachweise sollten unbeaufsichtigte Zustellung, Wiederholungen und Sichtbarkeit von Fehlern abdecken.

Abdeckung Experimentell - 2%Qualität Beta - 72%Vollständigkeit Beta - 79%Keine

Cron-Jobs 15 Fähigkeiten

Experimentell0%

Beta79%

Beta79%

[Cron-Jobs](</de/automation/cron-jobs>), [Cron](</de/cli/cron>), [Protokoll](</de/gateway/protocol>), [Aufgaben](</de/automation/tasks>), [Discord](</de/channels/discord>)

Eingehende Ereignisse 15 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Telegram](</de/channels/telegram>), [Zalo](</de/channels/zalo>), [Fehlerbehebung](</de/channels/troubleshooting>), [iMessage von BlueBubbles](</de/channels/imessage-from-bluebubbles>), [Gmail-Pub/Sub-Integration](</de/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</de/automation/cron-jobs>), [Webhooks](</de/cli/webhooks>), [Webhooks](</de/automation/cron-jobs#webhooks>), [Webhook](</de/automation/cron-jobs>)

Automatisierungs-Hooks 11 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Hooks](</de/automation/hooks>), [Hooks](</de/cli/hooks>), [Hooks](</de/plugins/hooks>), [Plugin-Berechtigungsanfragen](</de/plugins/plugin-permission-requests>), [SDK-Unterpfade](</de/plugins/sdk-subpaths>)

Hintergrundaufgaben und Abläufe 10 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Aufgaben](</de/automation/tasks>), [Index](</de/automation>), [Aufgaben](</de/cli/tasks>), [TaskFlow](</de/automation/taskflow>), [SDK-Laufzeit](</de/plugins/sdk-runtime>)

Heartbeat 5 Fähigkeiten

Experimentell14%

Beta79%

Beta79%

[Index](</de/automation>), [Heartbeat](</de/gateway/heartbeat>), [Verpflichtungen](</de/concepts/commitments>)

Polling-Steuerung 10 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Poll](</de/cli/message>), [Nachricht](</de/cli/message>), [Telegram](</de/channels/telegram>), [Msteams](</de/channels/msteams>), [Hintergrundprozess](</de/gateway/background-process>)

Medienverständnis und Mediengenerierung - M2 Alpha - 6 Bereiche

Eine breite Fähigkeitsoberfläche ist vorhanden, aber Provider-Unterschiede, Dateibeschränkungen und Parität zwischen Node und App machen dies noch nicht stabil.

Abdeckung Experimentell - 2%Qualität Alpha - 64%Vollständigkeit Alpha - 68%Keine

Medienaufnahme und -zugriff 8 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Medienübersicht](</de/tools/media-overview>), [Medienverständnis](</de/nodes/media-understanding>), [Sichere Dateioperationen](</de/gateway/security/secure-file-operations>), [PDF](</de/tools/pdf>), [Bildgenerierung](</de/tools/image-generation>), [QR](</de/cli/qr>), [LINE](</de/channels/line>), [WhatsApp](</de/channels/whatsapp>)

Medienverarbeitung in Kanälen 5 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Bilder](</de/nodes/images>), [Medienübersicht](</de/tools/media-overview>), [Discord](</de/channels/discord>)

Medienkonfiguration 1 Funktion

Experimentell0%

Alpha61%

Alpha68%

[Medienübersicht](</de/tools/media-overview>), [Bildgenerierung](</de/tools/image-generation>), [Manifest](</de/plugins/manifest>), [Codex-Harness](</de/plugins/codex-harness>)

Text-to-Speech-Bereitstellung 2 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[TTS](</de/tools/tts>), [Medienübersicht](</de/tools/media-overview>), [Discord](</de/channels/discord>)

Medienverständnis 12 Funktionen

Experimentell7%

Alpha69%

Alpha69%

[Audio](</de/nodes/audio>), [Medienverständnis](</de/nodes/media-understanding>), [Medienübersicht](</de/tools/media-overview>), [WhatsApp](</de/channels/whatsapp>), [Bilder](</de/nodes/images>), [Infer](</de/cli/infer>), [PDF](</de/tools/pdf>)

Mediengenerierung 17 Funktionen

Experimentell5%

Alpha69%

Alpha69%

[Bildgenerierung](</de/tools/image-generation>), [Medienübersicht](</de/tools/media-overview>), [Skills](</de/tools/skills>), [Musikgenerierung](</de/tools/music-generation>), [Videogenerierung](</de/tools/video-generation>)

Sprache und Echtzeitgespräch - M2 Alpha - 6 Bereiche

Es gibt mehrere Implementierungen in Control UI, Apps und bei Providern. Vor der Beta sind Scorecards für Latenz, Fehlermodi und Einrichtung erforderlich.

Abdeckung Experimentell - 0%Qualität Alpha - 61%Vollständigkeit Alpha - 68%Keine

Talk-Provider 7 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Openai](</de/providers/openai>), [Google](</de/providers/google>), [SDK-Provider-Plugins](</de/plugins/sdk-provider-plugins>), [Talk](</de/nodes/talk>), [Steuerungs-UI](</de/web/control-ui>)

Echtzeit-Talk-Sitzungen 11 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Talk](</de/nodes/talk>), [Steuerungs-UI](</de/web/control-ui>)

Sprache und Transkription 5 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Talk](</de/nodes/talk>), [Openai](</de/providers/openai>), [Google](</de/providers/google>)

Talk in nativen Apps 4 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Talk](</de/nodes/talk>), [Voicewake](</de/platforms/mac/voicewake>)

Sprachaktivierung und Routing 4 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Voicewake](</de/nodes/voicewake>), [Voicewake](</de/platforms/mac/voicewake>), [Sprach-Overlay](</de/platforms/mac/voice-overlay>)

Talk-Beobachtbarkeit 5 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Steuerungs-UI](</de/web/control-ui>), [Sprach-Overlay](</de/platforms/mac/voice-overlay>), [Talk](</de/nodes/talk>)

TUI - M2 Alpha - 5 Bereiche

In Dokumentation und Quellcode vorhanden, aber als primärer Benutzerworkflow weniger sichtbar. Benötigt eine explizite Szenariodefinition.

Abdeckung Experimentell - 0%Qualität Alpha - 59%Vollständigkeit Alpha - 66%Keine

Laufzeitmodi 14 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[TUI](</de/cli/tui>), [TUI](</de/web/tui>), [Index](</de/cli>)

Eingabe und Befehle 8 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[TUI](</de/web/tui>)

Sitzungsverwaltung 3 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[TUI](</de/web/tui>), [Sitzungen](</de/cli/sessions>)

Lokale Shell-Ausführung 4 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[TUI](</de/web/tui>), [TUI](</de/cli/tui>)

Rendering und Ausgabesicherheit 4 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[TUI](</de/web/tui>), [QR](</de/cli/qr>), [Protokolle](</de/cli/logs>), [Vervollständigung](</de/cli/completion>)

ClawHub - M2 Alpha - 4 Bereiche

Öffentliche Dokumentation und Ökosystemkonzept existieren. Installation, Vertrauen, Aktualisierung, Rollback und Kompatibilitäts-Scorecards werden benötigt.

Abdeckung Experimentell - 0%Qualität Alpha - 58%Vollständigkeit Alpha - 62%Keine

Veröffentlichung 7 Funktionen

Experimentell0%

Alpha54%

Alpha55%

[Veröffentlichung](</de/clawhub/publishing>), [Skills erstellen](</de/tools/creating-skills>), [Gemeinschaft](</de/plugins/community>)

Katalogerkennung 5 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Plugin](</de/tools/plugin>), [Plugins](</de/cli/plugins>), [Skills](</de/cli/skills>), [Skills](</de/tools/skills>), [Gemeinschaft](</de/plugins/community>)

Kompatibilität und Vertrauen 12 Funktionen

Experimentell0%

Alpha55%

Alpha56%

[Plugin](</de/tools/plugin>), [Plugins](</de/cli/plugins>), [Kompatibilität](</de/plugins/compatibility>), [Plugin-Inventar](</de/plugins/plugin-inventory>), [Veröffentlichung](</de/clawhub/publishing>), [Skills](</de/tools/skills>), [Skills-Konfiguration](</de/tools/skills-config>)

Plugin-Lebenszyklus und Zustand 26 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Plugin](</de/tools/plugin>), [Plugins](</de/cli/plugins>), [Skills](</de/cli/skills>), [Skills](</de/tools/skills>), [Protokoll](</de/gateway/protocol>), [Bündel](</de/plugins/bundles>), [Abhängigkeitsauflösung](</de/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 Bereiche

OpenClaw App SDK ist ein eigenständiger externer App-Vertrag, getrennt von Gateway-Laufzeit und Plugin SDK. Die aktuelle Bewertung zeigt einen realen `@openclaw/sdk`-Pfad mit Lücken bei öffentlicher Paketierung, automatischer Erkennung, Genehmigungen, Hilfsfunktionen und Kompatibilität.

Abdeckung experimentell - 3%Qualität Alpha - 54%Vollständigkeit Alpha - 53%Keine

Client-API 4 Fähigkeiten

Experimentell0%

Alpha51%

Alpha50%

[Openclaw SDK](</de/gateway/external-apps>), [Openclaw-SDK-API-Design](</de/gateway/external-apps>)

Gateway-Zugriff 5 Fähigkeiten

Experimentell0%

Alpha53%

Alpha54%

[Openclaw SDK](</de/gateway/external-apps>), [Openclaw-SDK-API-Design](</de/gateway/external-apps>), [Protokoll](</de/gateway/protocol>), [Index](</de/gateway/security>)

Agenten-Konversationen 6 Fähigkeiten

Experimentell0%

Alpha52%

Alpha52%

[Openclaw SDK](</de/gateway/external-apps>), [Openclaw-SDK-API-Design](</de/gateway/external-apps>), [Protokoll](</de/gateway/protocol>)

Ereignisse und Genehmigungen 5 Fähigkeiten

Experimentell0%

Alpha52%

Alpha52%

[Openclaw SDK](</de/gateway/external-apps>), [Openclaw-SDK-API-Design](</de/gateway/external-apps>), [Protokoll](</de/gateway/protocol>)

Ressourcen-Hilfsfunktionen 5 Fähigkeiten

Experimentell17%

Alpha62%

Alpha53%

[Openclaw SDK](</de/gateway/external-apps>), [Openclaw-SDK-API-Design](</de/gateway/external-apps>)

Kompatibilität 5 Fähigkeiten

Experimentell0%

Alpha54%

Alpha55%

[Openclaw-SDK-API-Design](</de/gateway/external-apps>), [Typebox](</de/concepts/typebox>), [Protokoll](</de/gateway/protocol>)

### Plattform

Linux-Gateway-Host - M4 Stabil - 5 Bereiche

Node-Laufzeit wird empfohlen, systemd-Benutzerdienst ist dokumentiert, und VPS-/Container-Anleitung ist breit angelegt.

Abdeckung Experimentell - 0%Qualität Beta - 75%Vollständigkeit Stabil - 89%Teilweise - 4

Host-Einrichtung und Updates 4 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Index](</de/install>), [Aktualisieren](</de/install/updating>), [Linux](</de/platforms/linux>), [Index](</de/platforms>)

Gateway-Laufzeit und Dienststeuerung 6 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Index](</de/gateway>), [Gateway](</de/cli/gateway>), [Linux](</de/platforms/linux>), [VPS](</de/vps>)

Remotezugriff und Sicherheit 6 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Remote](</de/gateway/remote>), [Tailscale](</de/gateway/tailscale>), [Exposure-Runbook](</de/gateway/security/exposure-runbook>), [Authentifizierung](</de/gateway/authentication>), [Secrets](</de/gateway/secrets>)

Diagnose und Reparatur 4 Funktionen / LTS-unterstützt

Experimentell0%

Beta75%

Stabil89%

[Status](</de/cli/status>), [Logs](</de/cli/logs>), [Doctor](</de/cli/doctor>), [Diagnose](</de/gateway/diagnostics>), [Index](</de/gateway>)

Bereitstellungsziele 3 Funktionen

Experimentell0%

Beta75%

Stabil89%

[VPS](</de/vps>), [Docker](</de/install/docker>), [Hetzner](</de/install/hetzner>), [DigitalOcean](</de/install/digitalocean>), [Kubernetes](</de/install/kubernetes>), [Podman](</de/install/podman>)

macOS-Gateway-Host - M4 Stabil - 7 Bereiche

LaunchAgent-Dienstpfad, lokale/Remote-Gateway-Modi, CLI-Installation und App-Integration sind dokumentiert.

Abdeckung Experimentell - 0%Qualität Beta - 74%Vollständigkeit Stabil - 88%Keine

CLI-Einrichtung 4 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Macos](</de/platforms/macos>), [Gebündeltes Gateway](</de/platforms/mac/bundled-gateway>), [Installer](</de/install/installer>), [Node](</de/install/node>)

Lokale Gateway-Integration 9 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Macos](</de/platforms/macos>), [Gebündeltes Gateway](</de/platforms/mac/bundled-gateway>), [Remote](</de/platforms/mac/remote>), [Index](</de/gateway>), [Gateway](</de/cli/gateway>), [Bonjour](</de/gateway/bonjour>)

Remote-Gateway-Modus 5 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Remote](</de/platforms/mac/remote>), [Remote](</de/gateway/remote>), [Tailscale](</de/gateway/tailscale>)

Lebenszyklus des Gateway-Dienstes 10 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Macos](</de/platforms/macos>), [Gebündeltes Gateway](</de/platforms/mac/bundled-gateway>), [Gateway](</de/cli/gateway>), [Index](</de/gateway>), [Aktualisierung](</de/cli/update>), [Aktualisieren](</de/install/updating>), [Deinstallation](</de/install/uninstall>), [Fehlerbehebung](</de/gateway/troubleshooting>)

Diagnose und Beobachtbarkeit 4 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Gebündeltes Gateway](</de/platforms/mac/bundled-gateway>), [Macos](</de/platforms/macos>), [Gateway](</de/cli/gateway>), [Doctor](</de/gateway/doctor>), [Fehlerbehebung](</de/gateway/troubleshooting>)

Berechtigungen und native Funktionen 4 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Macos](</de/platforms/macos>), [Remote](</de/platforms/mac/remote>)

Profile und Isolation 5 Funktionen

Experimentell0%

Beta74%

Stabil88%

[Mehrere Gateways](</de/gateway/multiple-gateways>), [Index](</de/gateway>), [Gateway](</de/cli/gateway>)

Hosting mit Docker und Podman - M3 Beta - 4 Bereiche

Installationsdokumentation ist vorhanden und umfasst gängige Bereitstellungspfade. Hochstufen, nachdem wiederkehrende Release-Smokes Upgrade- und Volume-Verhalten erfassen.

Abdeckung Experimentell - 7%Qualität Beta - 71%Vollständigkeit Beta - 79%Keine

Container-Einrichtung 6 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Docker](</de/install/docker>), [Podman](</de/install/podman>)

Container-Betrieb 11 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Podman](</de/install/podman>), [Docker-VM-Runtime](</de/install/docker-vm-runtime>), [Docker](</de/install/docker>), [Hetzner](</de/install/hetzner>), [Hostinger](</de/install/hostinger>)

Image-Release und Validierung 5 Fähigkeiten

Experimentell29%

Beta79%

Beta79%

[Docker](</de/install/docker>), [Docker-VM-Runtime](</de/install/docker-vm-runtime>), [Vollständige Release-Validierung](</de/reference/full-release-validation>)

Agent-Sandbox und Tooling 3 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Docker](</de/install/docker>), [Docker-VM-Runtime](</de/install/docker-vm-runtime>)

Windows über WSL2 - M3 Beta - 6 Bereiche

Empfohlener Windows-Pfad mit systemd-/Benutzerdienst-Anleitung und Boot-Chain-Dokumentation. Nach wiederholten Installations-/Update-Scorecards hochstufen.

Abdeckung Experimentell - 6%Qualität Alpha - 69%Vollständigkeit Beta - 79%Teilweise - 5

WSL-Einrichtung 6 Funktionen / LTS-unterstützt

Experimentell0%

Alpha67%

Beta79%

[Windows](</de/platforms/windows>), [Erste Schritte](</de/start/getting-started>)

CLI 8 Funktionen / LTS-unterstützt

Experimentell0%

Alpha67%

Beta79%

[Windows](</de/platforms/windows>), [Erste Schritte](</de/start/getting-started>), [Aktualisieren](</de/install/updating>), [Onboarding](</de/cli/onboard>), [Doctor](</de/cli/doctor>), [Status](</de/cli/status>), [Protokolle](</de/cli/logs>)

Gateway-Dienstlebenszyklus 10 Funktionen / LTS-unterstützt

Experimentell0%

Alpha67%

Beta79%

[Windows](</de/platforms/windows>), [Index](</de/gateway>), [Doctor](</de/gateway/doctor>)

Gateway-Zugriff und -Exposition 11 Funktionen / LTS-unterstützt

Experimentell0%

Alpha67%

Beta79%

[Authentifizierung](</de/gateway/authentication>), [Secrets](</de/gateway/secrets>), [Remote](</de/gateway/remote>), [Expositions-Runbook](</de/gateway/security/exposure-runbook>), [Windows](</de/platforms/windows>)

Diagnose und Reparatur 6 Funktionen / LTS-unterstützt

Experimentell38%

Beta79%

Beta79%

[Windows](</de/platforms/windows>), [Status](</de/cli/status>), [Protokolle](</de/cli/logs>), [Doctor](</de/cli/doctor>), [Doctor](</de/gateway/doctor>)

Browser und Control UI 6 Funktionen

Experimentell0%

Alpha67%

Beta79%

[Problembehandlung für Browser WSL2 Windows Remote CDP](</de/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Browser](</de/tools/browser>), [Control UI](</de/web/control-ui>)

Raspberry Pi und kleine Linux-Geräte - M3 Beta - 4 Bereiche

Plattformdokumentation ist vorhanden, und der Gateway-Pfad basiert auf Linux. Erfordert hardwarebezogenen Release-Smoke-Proof, um höher eingestuft zu werden.

Abdeckung Experimentell - 0%Qualität Alpha - 67%Vollständigkeit Beta - 79%Keine

Einrichtung und Kompatibilität 12 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Raspberry Pi](</de/install/raspberry-pi>), [Index](</de/install>), [FAQ zum ersten Start](</de/help/faq-first-run>), [FAQ](</de/help/faq>), [Linux](</de/platforms/linux>), [Installationsprogramm](</de/install/installer>)

Remotezugriff und Authentifizierung 9 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Raspberry Pi](</de/install/raspberry-pi>), [Authentifizierung](</de/gateway/authentication>), [Geheime Daten](</de/gateway/secrets>), [Kopplung](</de/gateway/pairing>), [Geräte](</de/cli/devices>), [Remotezugriff](</de/gateway/remote>), [Tailscale](</de/gateway/tailscale>)

Gateway-Laufzeit 10 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Index](</de/gateway>), [Gateway](</de/cli/gateway>), [Raspberry Pi](</de/install/raspberry-pi>), [Linux](</de/platforms/linux>), [VPS](</de/vps>)

Leistung und Diagnose 5 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Raspberry Pi](</de/install/raspberry-pi>), [Linux](</de/platforms/linux>), [Integrität](</de/gateway/health>), [Diagnose](</de/gateway/diagnostics>)

macOS-Begleit-App - M3 Beta - 8 Bereiche

Eine umfangreiche Menüleisten-App, Berechtigungen, Node-Modus, Canvas, Sprachaktivierung, WebChat und Remote-Modus sind vorhanden. Sie entwickelt sich noch schnell genug, um Stable zu vermeiden.

Abdeckung Experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Keine

Canvas 4 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Canvas](</de/platforms/mac/canvas>), [Macos](</de/platforms/macos>), [Webchat](</de/web/webchat>)

Lokale Einrichtung 7 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Gebündeltes Gateway](</de/platforms/mac/bundled-gateway>), [Macos](</de/platforms/macos>), [Child-Prozess](</de/platforms/mac/child-process>), [Entwicklungs-Setup](</de/platforms/mac/dev-setup>)

Status und Einstellungen 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Menüleiste](</de/platforms/mac/menu-bar>), [Symbol](</de/platforms/mac/icon>), [Macos](</de/platforms/macos>), [Zustand](</de/platforms/mac/health>), [Protokollierung](</de/platforms/mac/logging>), [Remote](</de/platforms/mac/remote>)

Native Funktionen 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Macos](</de/platforms/macos>), [Xpc](</de/platforms/mac/xpc>), [Berechtigungen](</de/platforms/mac/permissions>), [Signierung](</de/platforms/mac/signing>), [Peekaboo](</de/platforms/mac/peekaboo>)

Remote-Verbindungen 3 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Remote](</de/platforms/mac/remote>), [Macos](</de/platforms/macos>), [Remote](</de/gateway/remote>)

Sprache und Talk 3 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Voicewake](</de/platforms/mac/voicewake>), [Sprach-Overlay](</de/platforms/mac/voice-overlay>), [Talk](</de/nodes/talk>), [Macos](</de/platforms/macos>)

WebChat 3 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Webchat](</de/platforms/mac/webchat>), [Macos](</de/platforms/macos>), [Webchat](</de/web/webchat>)

Remote-WebChat 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Webchat](</de/platforms/mac/webchat>), [Remote](</de/gateway/remote>), [Remote](</de/platforms/mac/remote>)

Android-App - M2 Alpha - 7 Bereiche

Öffentlicher Google Play-Pfad existiert, aber die App-Dokumentation beschreibt den Rebuild weiterhin als extrem Alpha und weist auf Arbeiten zur Release-Härtung hin.

Abdeckung Experimentell - 0%Qualität Alpha - 59%Vollständigkeit Alpha - 66%Keine

Medienaufnahme 1 Funktion

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>), [Kamera](</de/nodes/camera>)

Mobiler Chat 1 Funktion

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>)

Verbindungseinrichtung 1 Funktion

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>), [Bonjour](</de/gateway/bonjour>), [Kopplung](</de/gateway/pairing>)

Verteilung 3 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>)

Einstellungen 1 Funktion

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>)

Sprache 1 Funktion

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>), [Sprechen](</de/nodes/talk>)

Geräte-Runtime 2 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Android](</de/platforms/android>), [Fehlerbehebung](</de/nodes/troubleshooting>), [Protokoll](</de/gateway/protocol>)

Natives Windows - M2 Alpha - 4 Bereiche

Die zentralen CLI-/Gateway-Abläufe funktionieren, aber die Dokumentation empfiehlt weiterhin WSL2 für die vollständige Nutzung und führt native Einschränkungen auf.

Abdeckung Experimentell - 0%Qualität Alpha - 58%Vollständigkeit Alpha - 66%Teilweise - 1

CLI 9 Funktionen / LTS-unterstützt

Experimentell0%

Alpha54%

Alpha64%

[Index](</de/install>), [Installer](</de/install/installer>), [Windows](</de/platforms/windows>), [Erste Schritte](</de/start/getting-started>), [Onboarding](</de/cli/onboard>)

Gateway-Verwaltung 11 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Windows](</de/platforms/windows>), [Index](</de/gateway>), [Gateway](</de/cli/gateway>), [Doctor](</de/cli/doctor>)

Netzwerk 4 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Windows](</de/platforms/windows>), [Index](</de/gateway>), [Gateway](</de/cli/gateway>)

Aktualisierungen 4 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Aktualisierung](</de/install/updating>), [CI](</de/ci>)

Kubernetes-Hosting - M2 Alpha - 4 Bereiche

Kubernetes-Hosting ist ein eigenständiger, Kustomize-basierter Deployment-Pfad für Cluster. Die aktuelle Bewertung zeigt einen echten minimalen Deployment-Pfad mit Lücken bei Kubernetes-spezifischer CI, ingress/TLS/NetworkPolicy-Paketierung, Backup/Wiederherstellung und Härtung der Produktionsfreigabe.

Abdeckung Experimentell - 0%Qualität Alpha - 55%Vollständigkeit Alpha - 61%Keine

Deployment-Einrichtung 5 Funktionen

Experimentell0%

Alpha55%

Alpha61%

[Kubernetes](</de/install/kubernetes>), [Index](</de/install>)

Konfiguration und Secrets 5 Funktionen

Experimentell0%

Alpha55%

Alpha61%

[Kubernetes](</de/install/kubernetes>), [Secrets](</de/gateway/secrets>), [Umgebung](</de/help/environment>)

Zugriff und Exposition 5 Funktionen

Experimentell0%

Alpha55%

Alpha61%

[Kubernetes](</de/install/kubernetes>), [Authentifizierung](</de/gateway/authentication>), [Remote](</de/gateway/remote>), [Expositions-Runbook](</de/gateway/security/exposure-runbook>)

Cluster-Lebenszyklus 5 Funktionen

Experimentell0%

Alpha55%

Alpha61%

[Kubernetes](</de/install/kubernetes>), [Index](</de/gateway>)

iOS-App - M1 Experimentell - 8 Bereiche

Interne Vorschau / Super-Alpha. TestFlight- und Relay-gestützte Push-Abläufe existieren, aber es gibt noch keine öffentliche Verteilung.

Abdeckung Experimentell - 0%Qualität Experimentell - 41%Vollständigkeit Experimentell - 44%Keine

Medien und Teilen 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Kamera](</de/nodes/camera>)

Canvas und Bildschirm 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Canvas](</de/plugins/reference/canvas>)

Chat und Sitzungen 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Webchat](</de/web/webchat>), [Protokoll](</de/gateway/protocol>)

Gateway-Einrichtung und Diagnose 7 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Kopplung](</de/channels/pairing>)

Verteilung 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>)

Gerätebefehle 2 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Protokoll](</de/gateway/protocol>)

Benachrichtigungen und Hintergrund 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Konfiguration](</de/gateway/configuration>)

Sprache 1 Fähigkeit

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>), [Talk](</de/nodes/talk>)

Nix-Installationspfad - M1 Experimentell - 5 Bereiche

Optionaler Installationsablauf. Benötigt ein klareres Support-Versprechen vor der Hochstufung zu Alpha/Beta.

Abdeckung Experimentell - 0%Qualität Experimentell - 41%Vollständigkeit Experimentell - 44%Keine

Installationsübergabe 4 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Nix](</de/install/nix>), [Index](</de/install>), [Dokumentationsverzeichnis](</de/start/docs-directory>)

Plugin-Lebenszyklus 4 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Plugins verwalten](</de/plugins/manage-plugins>), [Plugin](</de/tools/plugin>), [Nix](</de/install/nix>)

Aktivierung und App-UX 7 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Nix](</de/install/nix>)

Konfiguration und Zustand 7 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Nix](</de/install/nix>), [Einrichtung](</de/cli/setup>), [Umgebung](</de/help/environment>)

Service-Laufzeit und Schutzmechanismen 8 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Nix](</de/install/nix>), [Einrichtung](</de/cli/setup>), [Doctor](</de/cli/doctor>), [Aktualisierung](</de/cli/update>)

watchOS-Companion-Oberflächen - M1 Experimentell - 5 Bereiche

Die Quelle enthält Watch-App-/Erweiterungsoberflächen; die öffentliche Dokumentation stellt dies noch nicht als Benutzerfunktion dar.

Abdeckung Experimentell - 0%Qualität Experimentell - 41%Vollständigkeit Experimentell - 44%Keine

Zustellung und Wiederherstellung 7 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>)

Ausführungsfreigaben 3 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ausführungsfreigaben](</de/tools/exec-approvals>), [Ios](</de/platforms/ios>)

Distribution und Support 6 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>)

Benachrichtigungen und Antworten 7 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>)

Watch-App-Benutzeroberfläche 3 Fähigkeiten

Experimentell0%

Experimentell41%

Experimentell44%

[Ios](</de/platforms/ios>)

Linux-Begleit-App - M0 Geplant - 5 Bereiche

Laut Dokumentation sind native Linux-Begleit-Apps geplant; Gateway ist derzeit der unterstützte Linux-Pfad.

Abdeckung Experimentell - 0%Qualität Experimentell - 19%Vollständigkeit Experimentell - 21%Keine

App-Verteilung 3 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Linux](</de/platforms/linux>), [Index](</de/platforms>), [Index](</de/install>)

Gateway-Konnektivität 4 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Linux](</de/platforms/linux>), [Index](</de/gateway>), [Kopplung](</de/gateway/pairing>), [Remote](</de/gateway/remote>)

Chat und Sitzungen 3 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Linux](</de/platforms/linux>), [Protokoll](</de/gateway/protocol>), [Webchat](</de/web/webchat>)

Desktop-Funktionen 9 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Linux](</de/platforms/linux>), [Exec-Genehmigungen](</de/tools/exec-approvals>), [Geheimnisse](</de/gateway/secrets>), [Index](</de/nodes>), [Exec](</de/tools/exec>), [Sprechen](</de/nodes/talk>), [Kamera](</de/nodes/camera>)

Status und Diagnose 7 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Linux](</de/platforms/linux>), [OpenClaw](</de/start/openclaw>), [Doctor](</de/gateway/doctor>)

Native Windows-Begleit-App - M0 Geplant - 5 Bereiche

Nur geplant.

Abdeckung experimentell - 0%Qualität experimentell - 19%Vollständigkeit experimentell - 21%Keine

Installation und Updates 4 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Windows](</de/platforms/windows>), [Index](</de/install>)

Gateway-Verbindung 3 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Windows](</de/platforms/windows>), [Index](</de/gateway>), [Kopplung](</de/gateway/pairing>), [Remote](</de/gateway/remote>)

Chat-Sitzungen 2 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Windows](</de/platforms/windows>), [Protokoll](</de/gateway/protocol>)

Status und Reparatur 5 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Windows](</de/platforms/windows>), [Doctor](</de/gateway/doctor>), [Index](</de/gateway>)

Desktop-Tools und Berechtigungen 10 Funktionen

Experimentell0%

Experimentell19%

Experimentell21%

[Windows](</de/platforms/windows>), [Index](</de/nodes>), [Exec](</de/tools/exec>), [Exec-Genehmigungen](</de/tools/exec-approvals>), [Index](</de/gateway/security>)

### Kanal

Discord - M4 Stabil - 6 Bereiche

Ausführliche Docs und breite Funktionsabdeckung. Sprach-/Delegationspfade sollten weiterhin separat als Beta/Alpha bewertet werden.

Abdeckung Experimentell - 0%Qualität Beta - 73%Vollständigkeit Stabil - 87%Teilweise - 4

Einrichtung und Betrieb von Kanälen 10 Fähigkeiten / LTS-unterstützt

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>), [Discord](</de/plugins/reference/discord>), [Fly](</de/install/fly>), [Slash-Befehle](</de/tools/slash-commands>), [Zustand](</de/gateway/health>), [Kanäle](</de/cli/channels>), [Konfigurationskanäle](</de/gateway/config-channels>)

Zugriff und Identität 6 Fähigkeiten / LTS-unterstützt

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>), [Kopplung](</de/channels/pairing>), [Zugriffsgruppen](</de/channels/access-groups>), [Gruppen](</de/channels/groups>)

Konversationsrouting und Zustellung 12 Fähigkeiten / LTS-unterstützt

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>), [Kanalrouting](</de/channels/channel-routing>), [Gruppen](</de/channels/groups>), [Zugriffsgruppen](</de/channels/access-groups>), [ACP-Agenten](</de/tools/acp-agents>), [Subagents](</de/tools/subagents>)

Medien und Rich Content 1 Fähigkeit / LTS-unterstützt

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>)

Native Steuerelemente und Genehmigungen 5 Fähigkeiten

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>), [Slash-Befehle](</de/tools/slash-commands>)

Echtzeit-Sprache und Anrufe 5 Fähigkeiten

Experimentell0%

Beta73%

Stabil87%

[Discord](</de/channels/discord>), [OpenAI](</de/providers/openai>), [ElevenLabs](</de/providers/elevenlabs>), [QA-E2E-Automatisierung](</de/concepts/qa-e2e-automation>), [Konfigurationskanäle](</de/gateway/config-channels>)

Telegram - M3 Beta - 5 Bereiche

Der Kernkanal ist ausgereift genug für die regelmäßige Nutzung, aber stark schwankende UX und Medien-Grenzfälle benötigen wiederkehrende Szenarienachweise.

Abdeckung experimentell - 0%Qualität Alpha - 68%Vollständigkeit Beta - 78%Vollständig - 5

Channel-Einrichtung und Betrieb 10 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Telegram](</de/channels/telegram>), [Config Channels](</de/gateway/config-channels>), [Channels](</de/cli/channels>)

Zugriff und Identität 10 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Telegram](</de/channels/telegram>), [Kopplung](</de/channels/pairing>), [Zugriffsgruppen](</de/channels/access-groups>), [Gruppen](</de/channels/groups>), [Multi Agent](</de/concepts/multi-agent>)

Konversationsrouting und Zustellung 1 Fähigkeit / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Telegram](</de/channels/telegram>), [Gruppen](</de/channels/groups>), [Multi Agent](</de/concepts/multi-agent>)

Medien und Rich Content 1 Fähigkeit / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Telegram](</de/channels/telegram>), [Standort](</de/channels/location>)

Native Steuerungen und Genehmigungen 9 Fähigkeiten / LTS-unterstützt

Experimentell0%

Beta77%

Beta79%

[Telegram](</de/channels/telegram>), [Exec-Genehmigungen](</de/tools/exec-approvals>), [Reaktionen](</de/tools/reactions>)

Slack - M3 Beta - 5 Bereiche

Erstklassige Channel-Dokumentation und Routing-Oberfläche. Benötigt Scorecards für Szenarien zu Workspace-Installation und Administration.

Abdeckung Experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Vollständig - 5

Channel-Einrichtung und Betrieb 10 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Slack](</de/channels/slack>), [Slack](</de/plugins/reference/slack>), [Secrets](</de/gateway/secrets>), [QA-E2E-Automatisierung](</de/concepts/qa-e2e-automation>), [Fehlerbehebung](</de/channels/troubleshooting>)

Zugriff und Identität 1 Fähigkeit / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Slack](</de/channels/slack>), [Kopplung](</de/channels/pairing>)

Konversationsrouting und Zustellung 5 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Slack](</de/channels/slack>), [Bot-Loop-Schutz](</de/channels/bot-loop-protection>), [Kopplung](</de/channels/pairing>)

Medien und Rich Content 1 Fähigkeit / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Slack](</de/channels/slack>), [QA-E2E-Automatisierung](</de/concepts/qa-e2e-automation>)

Native Steuerelemente und Genehmigungen 8 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha66%

Beta78%

[Slack](</de/channels/slack>), [Slash-Befehle](</de/tools/slash-commands>), [Ausführungsgenehmigungen](</de/tools/exec-approvals>)

iMessage und BlueBubbles - M3 Beta - 5 Bereiche

Unterstütztes iMessage läuft über imsg auf einem angemeldeten macOS-Messages-Host; ältere BlueBubbles-Konfigurationen erfordern eine Migration. Halten Sie macOS-Berechtigungen, SSH-Wrapper, SIP/private API und Migrationshinweise sichtbar.

Abdeckung Experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Keine

Channel-Einrichtung und Betrieb 11 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</de/announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</de/channels/imessage-from-bluebubbles>), [Channels konfigurieren](</de/gateway/config-channels>), [Imessage](</de/channels/imessage>)

Zugriff und Identität 6 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Imessage](</de/channels/imessage>), [Imessage From Bluebubbles](</de/channels/imessage-from-bluebubbles>), [Channels konfigurieren](</de/gateway/config-channels>)

Konversationsrouting und Zustellung 4 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Imessage](</de/channels/imessage>)

Medien und Rich Content 7 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Imessage](</de/channels/imessage>), [Imessage From Bluebubbles](</de/channels/imessage-from-bluebubbles>), [Channels konfigurieren](</de/gateway/config-channels>)

Native Steuerelemente und Genehmigungen 3 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Imessage](</de/channels/imessage>)

WhatsApp - M3 Beta - 5 Bereiche

Der Kernpfad ist wichtig und dokumentiert; die Volatilität von Upstream-Baileys/Sitzungen hält ihn unter Stable.

Abdeckung Experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Keine

Channel-Einrichtung und Betrieb 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[WhatsApp](</de/channels/whatsapp>), [Channels konfigurieren](</de/gateway/config-channels>), [WhatsApp](</de/plugins/reference/whatsapp>), [QA-E2E-Automatisierung](</de/concepts/qa-e2e-automation>), [Doctor](</de/gateway/doctor>)

Zugriff und Identität 7 Funktionen

Experimentell0%

Alpha66%

Beta78%

[WhatsApp](</de/channels/whatsapp>), [Channels konfigurieren](</de/gateway/config-channels>), [QA-E2E-Automatisierung](</de/concepts/qa-e2e-automation>), [Koppeln](</de/channels/pairing>)

Konversationsrouting und Zustellung 4 Funktionen

Experimentell0%

Alpha66%

Beta78%

[WhatsApp](</de/channels/whatsapp>), [Gruppennachrichten](</de/channels/group-messages>)

Medien und Rich Content 2 Funktionen

Experimentell0%

Alpha66%

Beta78%

[WhatsApp](</de/channels/whatsapp>)

Native Steuerelemente und Genehmigungen 2 Funktionen

Experimentell0%

Alpha66%

Beta78%

[WhatsApp](</de/channels/whatsapp>)

Matrix - M2 Alpha - 6 Bereiche

Unterstützt über gebündeltes Plugin. Benötigt Scorecards für Bridge, Authentifizierung und Raum-Lifecycle.

Abdeckung Experimentell - 0%Qualität Alpha - 60%Vollständigkeit Alpha - 67%Keine

Kanaleinrichtung und Betrieb 5 Funktionen

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>), [Matrix-Migration](</de/channels/matrix-migration>)

Zugriff und Identität 7 Funktionen

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>), [Gruppen](</de/channels/groups>), [Bot-Loop-Schutz](</de/channels/bot-loop-protection>)

Konversationsrouting und Zustellung 1 Funktion

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>)

Medien und Rich Content 1 Funktion

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>)

Native Steuerelemente und Genehmigungen 6 Funktionen

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>)

Verschlüsselung und Verifizierung 3 Funktionen

Experimentell0%

Alpha60%

Alpha67%

[Matrix](</de/channels/matrix>), [Matrix-Migration](</de/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 Bereiche

Dokumentierter Kanal, aber die Einrichtung für Unternehmen/Administratoren erhöht das Reiferisiko.

Abdeckung Experimentell - 0%Qualität Alpha - 59%Vollständigkeit Alpha - 66%Keine

Kanaleinrichtung und Betrieb 16 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Google Chat](</de/channels/googlechat>), [Google Chat](</de/plugins/reference/googlechat>), [Kanäle konfigurieren](</de/gateway/config-channels>), [Wizard-CLI-Referenz](</de/start/wizard-cli-reference>), [Secrets](</de/gateway/secrets>), [Secretref-Anmeldedatenoberfläche](</de/reference/secretref-credential-surface>), [Zustand](</de/gateway/health>), [Plugin-Bestand](</de/plugins/plugin-inventory>), [Index](</de/channels>)

Zugriff und Identität 11 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Google Chat](</de/channels/googlechat>), [Kopplung](</de/channels/pairing>), [Zugriffsgruppen](</de/channels/access-groups>), [Kanäle konfigurieren](</de/gateway/config-channels>), [Bot-Loop-Schutz](</de/channels/bot-loop-protection>), [Kanalrouting](</de/channels/channel-routing>)

Konversationsrouting und Zustellung 1 Fähigkeit

Experimentell0%

Alpha59%

Alpha66%

[Google Chat](</de/channels/googlechat>), [Bot-Loop-Schutz](</de/channels/bot-loop-protection>), [Zugriffsgruppen](</de/channels/access-groups>), [Kanalrouting](</de/channels/channel-routing>)

Medien und Rich Content 1 Fähigkeit

Experimentell0%

Alpha59%

Alpha66%

[Google Chat](</de/channels/googlechat>), [Nachricht](</de/cli/message>), [Medienverständnis](</de/nodes/media-understanding>), [Secretref-Anmeldedatenoberfläche](</de/reference/secretref-credential-surface>)

Native Steuerelemente und Genehmigungen 16 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Google Chat](</de/channels/googlechat>), [Nachricht](</de/cli/message>), [Medienverständnis](</de/nodes/media-understanding>), [Secretref-Anmeldedatenoberfläche](</de/reference/secretref-credential-surface>), [Reaktionen](</de/tools/reactions>), [Slash-Befehle](</de/tools/slash-commands>), [Agents konfigurieren](</de/gateway/config-agents>), [Refaktorierung des Nachrichtenlebenszyklus](</de/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 Bereiche

Enterprise-Auth-/Admin-Abläufe benötigen expliziten Szenariennachweis.

Abdeckung Experimentell - 0%Qualität Alpha - 59%Vollständigkeit Alpha - 66%Keine

Kanaleinrichtung und Betrieb 9 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Msteams](</de/channels/msteams>), [Msteams](</de/plugins/reference/msteams>), [Kanäle konfigurieren](</de/gateway/config-channels>), [Status](</de/gateway/health>)

Zugriff und Identität 9 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Msteams](</de/channels/msteams>), [Kopplung](</de/channels/pairing>), [Zugriffsgruppen](</de/channels/access-groups>)

Konversationsrouting und Zustellung 5 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Msteams](</de/channels/msteams>), [Gruppen](</de/channels/groups>), [Kanalrouting](</de/channels/channel-routing>)

Medien und Rich Content 5 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Msteams](</de/channels/msteams>)

Native Steuerelemente und Genehmigungen 5 Funktionen

Experimentell0%

Alpha59%

Alpha66%

[Msteams](</de/channels/msteams>), [Erweiterte Exec-Genehmigungen](</de/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 Bereiche

Unterstützende Kanaldokumentation ist vorhanden; es sind stärkere Nachweise für Installation und erneute Verbindung erforderlich.

Abdeckung Experimentell - 0%Qualität Alpha - 59%Vollständigkeit Alpha - 66%Keine

Kanaleinrichtung und Betrieb 7 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Signal](</de/channels/signal>), [Signal](</de/plugins/reference/signal>)

Zugriff und Identität 6 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Signal](</de/channels/signal>)

Konversationsrouting und Zustellung 1 Fähigkeit

Experimentell0%

Alpha59%

Alpha66%

[Signal](</de/channels/signal>)

Medien und Rich Content 7 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Signal](</de/channels/signal>)

Native Steuerelemente und Genehmigungen 3 Fähigkeiten

Experimentell0%

Alpha59%

Alpha66%

[Signal](</de/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale Kanäle - M2 Alpha - 4 Bereiche

Wichtige regionale Abdeckung, aber das öffentliche Supportniveau sollte je nach Kontotyp, Upstream-Genehmigung und Maintainer-Nachweis kalibriert werden.

Abdeckung Experimentell - 0%Qualität Alpha - 55%Vollständigkeit Alpha - 58%Keine

Kanaleinrichtung und Betrieb 6 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Index](</de/channels>), [Kopplung](</de/channels/pairing>), [Feishu](</de/plugins/reference/feishu>), [Architektur-Interna](</de/plugins/architecture-internals>)

Zugriff und Identität 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Konversationsrouting und Zustellung 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Medien und Rich Content 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 Bereiche

Unterstützte Oberflächen existieren, aber die Reife variiert wahrscheinlich je nach Upstream und Maintainer-Abdeckung. Später einzeln bewerten.

Abdeckung experimentell - 0%Qualität Alpha - 53%Vollständigkeit Alpha - 54%Keine

Kanaleinrichtung und Betrieb 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Zugriff und Identität 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Konversationsrouting und Zustellung 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Medien und Rich Content 1 Funktion

Experimentell0%

Alpha53%

Alpha54%

Keine verknüpfte Dokumentation

Sprachanrufkanal - M1 Experimentell - 5 Bereiche

Optionaler/Plugin-Pfad mit komplexem Echtzeitverhalten. Benötigt vor der öffentlichen Beta eine Szenario-Scorecard.

Abdeckung Experimentell - 0%Qualität Experimentell - 41%Vollständigkeit Experimentell - 44%Keine

Kanaleinrichtung und Betrieb 2 Funktionen

Experimentell0%

Experimentell41%

Experimentell44%

[Sprachanruf](</de/cli/voicecall>), [Sprachanruf](</de/plugins/voice-call>), [Protokoll](</de/gateway/protocol>)

Zugriff und Identität 1 Funktion

Experimentell0%

Experimentell41%

Experimentell44%

[Sprachanruf](</de/plugins/voice-call>), [Sprachanruf](</de/cli/voicecall>)

Konversationsrouting und Zustellung 1 Funktion

Experimentell0%

Experimentell41%

Experimentell44%

[Sprachanruf](</de/plugins/voice-call>)

Medien und Rich Content 2 Funktionen

Experimentell0%

Experimentell41%

Experimentell44%

[Sprachanruf](</de/plugins/voice-call>), [Plugin-Inventar](</de/plugins/plugin-inventory>)

Echtzeit-Sprache und Anrufe 2 Funktionen

Experimentell0%

Experimentell41%

Experimentell44%

[Sprachanruf](</de/plugins/voice-call>)

### Provider und Werkzeug

Browserautomatisierung, exec und Sandbox-Werkzeuge - M3 Beta - 3 Bereiche

Kernwerkzeuge sind dokumentiert, aber Hostsicherheit und Berechtigungs-UX sollten weiterhin aktiv im Scorecard-Review bleiben.

Abdeckung Experimentell - 21%Qualität Beta - 75%Vollständigkeit Beta - 79%Teilweise - 2

Browser-Automatisierung 8 Fähigkeiten

Experimentell13%

Beta79%

Beta79%

[Browser-Steuerung](</de/tools/browser-control>), [Testen](</de/help/testing>), [Browser](</de/tools/browser>), [Index](</de/gateway/security>), [Audit-Prüfungen](</de/gateway/security/audit-checks>)

Tool-Aufruf und -Ausführung 6 Fähigkeiten / LTS-unterstützt

Alpha50%

Beta79%

Beta79%

[Exec](</de/tools/exec>), [Hintergrundprozess](</de/gateway/background-process>), [Tools-Invoke-HTTP-API](</de/gateway/tools-invoke-http-api>), [Operator-Scopes](</de/gateway/operator-scopes>), [Protokoll](</de/gateway/protocol>), [Exec-Genehmigungen](</de/tools/exec-approvals>), [Erweiterte Exec-Genehmigungen](</de/tools/exec-approvals-advanced>), [Erhöht](</de/tools/elevated>)

Sandbox- und Tool-Richtlinie 6 Fähigkeiten / LTS-unterstützt

Experimentell0%

Alpha68%

Beta79%

[Sandboxing](</de/gateway/sandboxing>), [Sandbox vs. Tool-Richtlinie vs. Erhöht](</de/gateway/sandbox-vs-tool-policy-vs-elevated>), [Multi-Agent-Sandbox-Tools](</de/tools/multi-agent-sandbox-tools>), [Codex-Harness-Referenz](</de/plugins/codex-harness-reference>), [Konfigurations-Tools](</de/gateway/config-tools>)

OpenAI- und Codex-Provider-Pfad - M3 Beta - 5 Bereiche

Ausführliche Dokumentation, OAuth-/Abonnementpfad, Echtzeit-Sprache, Bild und Kompatibilitätsverhalten. Provider-Wechsel verhindern ohne Release-Scorecard-Nachweis eine Einstufung als Stable.

Abdeckung Experimentell - 26%Qualität Beta - 74%Vollständigkeit Beta - 79%Teilweise - 3

Modell und Auth 6 Fähigkeiten / LTS-unterstützt

Experimentell44%

Beta79%

Beta79%

[Openai](</de/providers/openai>), [Codex Harness](</de/plugins/codex-harness>), [Modelle](</de/concepts/models>), [OAuth](</de/concepts/oauth>), [Codex-Harness-Referenz](</de/plugins/codex-harness-reference>), [Auth-Überwachung](</de/gateway/authentication>)

Responses- und Tool-Kompatibilität 4 Fähigkeiten / LTS-unterstützt

Experimentell40%

Beta79%

Beta79%

[Openai](</de/providers/openai>), [Openresponses-HTTP-API](</de/gateway/openresponses-http-api>), [Openai-HTTP-API](</de/gateway/openai-http-api>), [Native Codex-Plugins](</de/plugins/codex-native-plugins>)

Nativer Codex Harness 2 Fähigkeiten / LTS-unterstützt

Experimentell44%

Beta79%

Beta79%

[Codex Harness](</de/plugins/codex-harness>), [Codex-Harness-Laufzeit](</de/plugins/codex-harness-runtime>), [Codex-Harness-Referenz](</de/plugins/codex-harness-reference>), [Native Codex-Plugins](</de/plugins/codex-native-plugins>)

Bild- und multimodale Eingabe 2 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Openai](</de/providers/openai>), [Bilderzeugung](</de/tools/image-generation>), [Bilder](</de/nodes/images>)

Sprache und Echtzeit-Audio 2 Fähigkeiten

Experimentell0%

Alpha67%

Beta79%

[Openai](</de/providers/openai>), [Discord](</de/channels/discord>), [Sprachanruf](</de/plugins/voice-call>)

Websuch-Tools - M3 Beta - 4 Bereiche

Mehrere Provider und Dokumentationen sind vorhanden. Benötigt Nachweise zu Kontingenten, Fehlern und SSRF pro Provider-Familie.

Abdeckung Experimentell - 9%Qualität Beta - 74%Vollständigkeit Beta - 79%Keine

Such-Provider 19 Fähigkeiten

Experimentell11%

Beta79%

Beta79%

[Web](</de/tools/web>), [Brave Search](</de/tools/brave-search>), [Tavily](</de/tools/tavily>), [Exa Search](</de/tools/exa-search>), [Firecrawl](</de/tools/firecrawl>), [Perplexity Search](</de/tools/perplexity-search>), [Duckduckgo Search](</de/tools/duckduckgo-search>), [Searxng Search](</de/tools/searxng-search>), [Gemini Search](</de/tools/gemini-search>), [Grok Search](</de/tools/grok-search>), [Kimi Search](</de/tools/kimi-search>), [Minimax Search](</de/tools/minimax-search>), [Ollama Search](</de/tools/ollama-search>), [Sdk Subpaths](</de/plugins/sdk-subpaths>), [Sdk Overview](</de/plugins/sdk-overview>), [Manifest](</de/plugins/manifest>)

Einrichtung und Diagnose 9 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Web](</de/tools/web>), [Web Fetch](</de/tools/web-fetch>), [FAQ](</de/help/faq>), [Kosten der API-Nutzung](</de/reference/api-usage-costs>), [Brave Search](</de/tools/brave-search>), [Perplexity Search](</de/tools/perplexity-search>), [Tavily](</de/tools/tavily>), [Firecrawl](</de/tools/firecrawl>)

Netzwerksicherheit 4 Fähigkeiten

Experimentell0%

Alpha68%

Beta79%

[Web](</de/tools/web>), [Web Fetch](</de/tools/web-fetch>), [Firecrawl](</de/tools/firecrawl>), [Searxng Search](</de/tools/searxng-search>)

Tool-Verfügbarkeit und Abruf 11 Fähigkeiten

Experimentell25%

Beta79%

Beta79%

[Konfigurationstools](</de/gateway/config-tools>), [Web Fetch](</de/tools/web-fetch>), [Web](</de/tools/web>), [FAQ](</de/help/faq>)

Anthropic-Provider-Pfad - M3 Beta - 5 Bereiche

Erstklassiger Modell-Provider. Benötigt wiederkehrende Szenario-Nachweise für Authentifizierung, Katalog und Tool-Aufrufe.

Abdeckung Experimentell - 0%Qualität Beta - 71%Vollständigkeit Beta - 78%Keine

Provider-Authentifizierung und Wiederherstellung 9 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Anthropic](</de/providers/anthropic>), [Doctor](</de/gateway/doctor>), [Konfigurationsbeispiele](</de/gateway/configuration-examples>), [Fehlerbehebung](</de/gateway/troubleshooting>), [Prompt-Caching](</de/reference/prompt-caching>)

Modell- und Laufzeitauswahl 10 Fähigkeiten

Experimentell0%

Beta78%

Beta79%

[Anthropic](</de/providers/anthropic>), [Agenten konfigurieren](</de/gateway/config-agents>), [Modelle](</de/concepts/models>), [CLI-Backends](</de/gateway/cli-backends>)

Anfragetransport und Turn-Semantik 10 Fähigkeiten

Experimentell0%

Beta77%

Beta79%

[Anthropic](</de/providers/anthropic>), [Prompt-Caching](</de/reference/prompt-caching>), [Fehlerbehebung](</de/gateway/troubleshooting>), [CLI-Backends](</de/gateway/cli-backends>), [Modell-Provider](</de/concepts/model-providers>)

Prompt-Cache und Kontext 5 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Anthropic](</de/providers/anthropic>), [Prompt-Caching](</de/reference/prompt-caching>), [Fehlerbehebung](</de/gateway/troubleshooting>), [Heartbeat](</de/gateway/heartbeat>)

Medieneingaben 4 Fähigkeiten

Experimentell0%

Alpha66%

Beta78%

[Anthropic](</de/providers/anthropic>), [Agenten konfigurieren](</de/gateway/config-agents>)

Google-Provider-Pfad - M3 Beta - 5 Bereiche

Erstklassiger Provider mit Modell- und Echtzeitoberflächen. Erfordert separate Bewertung für Live/Talk.

Abdeckung experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Keine

Provider-Einrichtung und Zugangsdaten 10 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Google](</de/providers/google>), [Modell-Provider](</de/concepts/model-providers>)

Modell-Routing und Endpunkte 10 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Google](</de/providers/google>), [Modell-Provider](</de/concepts/model-providers>), [Google](</de/plugins/reference/google>), [Gemini Search](</de/tools/gemini-search>)

Direkte Gemini-Runtime 9 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Google](</de/providers/google>), [Modell-Provider](</de/concepts/model-providers>), [FAQ zu Modellen](</de/help/faq-models>), [Live-Tests](</de/help/testing-live>)

Medien, Suche und Echtzeit 10 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Google](</de/plugins/reference/google>), [Google](</de/providers/google>)

Prompt-Caching 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Prompt-Caching](</de/reference/prompt-caching>), [Google](</de/providers/google>), [Modell-Provider](</de/concepts/model-providers>), [Token-Nutzung](</de/reference/token-use>)

OpenRouter-Provider-Pfad - M3 Beta - 4 Bereiche

Der einheitliche Provider-Pfad ist dokumentiert und wertvoll, aber modellspezifisches Verhalten variiert.

Abdeckung experimentell - 0%Qualität Alpha - 66%Vollständigkeit Beta - 78%Keine

Provider-Einrichtung und Authentifizierung 14 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Openrouter](</de/providers/openrouter>), [Modell-Provider](</de/concepts/model-providers>), [Konfigurieren](</de/cli/configure>), [Authentifizierung](</de/gateway/authentication>), [Umgebung](</de/help/environment>), [Modelle](</de/cli/models>), [Modelle](</de/concepts/models>)

Chat-Laufzeit und Normalisierung 15 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Openrouter](</de/providers/openrouter>), [Modell-Provider](</de/concepts/model-providers>), [Prompt-Caching](</de/reference/prompt-caching>)

Provider-Wiederherstellung und Diagnose 5 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Modell-Failover](</de/concepts/model-failover>), [Openrouter](</de/providers/openrouter>), [Modelle](</de/cli/models>)

Mediengenerierung und Sprache 7 Funktionen

Experimentell0%

Alpha66%

Beta78%

[Openrouter](</de/providers/openrouter>), [Bildgenerierung](</de/tools/image-generation>), [Musikgenerierung](</de/tools/music-generation>), [Medienübersicht](</de/tools/media-overview>), [Videogenerierung](</de/tools/video-generation>), [Tts](</de/tools/tts>)

Tools für Bild-, Video- und Musikgenerierung - M2 Alpha - 5 Bereiche

Die Funktion ist providerübergreifend vorhanden, aber Qualität, Latenz und Parameterkompatibilität variieren ohne Provider-spezifischen Nachweis zu stark für Beta.

Abdeckung Experimentell - 0%Qualität Alpha - 61%Vollständigkeit Alpha - 68%Keine

Medien-Routing und Discovery 4 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Agenten konfigurieren](</de/gateway/config-agents>), [Bildgenerierung](</de/tools/image-generation>), [Videogenerierung](</de/tools/video-generation>), [Musikgenerierung](</de/tools/music-generation>)

Aufgaben-Lebenszyklus und Zustellung 12 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Medienübersicht](</de/tools/media-overview>), [Bildgenerierung](</de/tools/image-generation>), [Videogenerierung](</de/tools/video-generation>), [Musikgenerierung](</de/tools/music-generation>)

Bildgenerierung 9 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Bildgenerierung](</de/tools/image-generation>), [Infer](</de/cli/infer>), [Medienübersicht](</de/tools/media-overview>)

Videogenerierung 11 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Videogenerierung](</de/tools/video-generation>), [Runway](</de/providers/runway>), [Pixverse](</de/providers/pixverse>), [Fal](</de/providers/fal>), [Openrouter](</de/providers/openrouter>)

Musikgenerierung 6 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Musikgenerierung](</de/tools/music-generation>)

Lokale Modell-Provider: Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 Bereiche

Nützlich und dokumentiert, aber die Umgebungsvarianz ist hoch.

Abdeckung Experimentell - 0%Qualität Alpha - 61%Vollständigkeit Alpha - 68%Keine

Provider-Einrichtung, Lebenszyklus und Diagnose 12 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Lokale Modelle](</de/gateway/local-models>), [Lmstudio](</de/providers/lmstudio>), [Ollama](</de/providers/ollama>), [Vllm](</de/providers/vllm>), [Lokale Modelldienste](</de/gateway/local-model-services>), [Agent-Konfiguration](</de/gateway/config-agents>), [Fehlerbehebung](</de/gateway/troubleshooting>), [Doctor](</de/gateway/doctor>)

Native Provider-Plugins 10 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Ollama](</de/providers/ollama>), [Lmstudio](</de/providers/lmstudio>)

OpenAI-kompatible Runtime-Kompatibilität 8 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Vllm](</de/providers/vllm>), [Sglang](</de/providers/sglang>), [Lokale Modelle](</de/gateway/local-models>), [Lmstudio](</de/providers/lmstudio>)

Lokaler Speicher und Embeddings 5 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Speicher](</de/concepts/memory>), [Doctor](</de/gateway/doctor>)

Netzwerksicherheit und Prompt-Steuerungen 2 Funktionen

Experimentell0%

Alpha61%

Alpha68%

[Index](</de/gateway/security>), [Tool-Konfiguration](</de/gateway/config-tools>), [Lokale Modelle](</de/gateway/local-models>)

Long-Tail-gehostete Provider - M2 Alpha - 3 Bereiche

Es gibt viele Dokumentations- und Referenzseiten; die Bewertung sollte aus Provider-Metadaten plus Live-Smoke-Abdeckung generiert werden.

Abdeckung Experimentell - 0%Qualität Alpha - 61%Vollständigkeit Alpha - 68%Keine

Gehostete LLM-Provider 12 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Index](</de/providers>), [Modell-Provider](</de/concepts/model-providers>), [Live testen](</de/help/testing-live>), [Onboarding](</de/cli/onboard>)

Gehostete Medien-Provider 8 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Manifest](</de/plugins/manifest>), [Live testen](</de/help/testing-live>), [Index](</de/providers>)

Provider-Betrieb 12 Fähigkeiten

Experimentell0%

Alpha61%

Alpha68%

[Index](</de/providers>), [Modell-Provider](</de/concepts/model-providers>), [Manifest](</de/plugins/manifest>), [Live testen](</de/help/testing-live>), [Modelle](</de/cli/models>)

Was this useful?YesNo

Open issue