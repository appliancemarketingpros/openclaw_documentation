---
title: Anthropic
source_url: https://docs.openclaw.ai/de/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic entwickelt die **Claude** -Modellfamilie. OpenClaw unterstützt zwei Authentifizierungswege:

  * **API-Schlüssel** — direkter Anthropic-API-Zugriff mit nutzungsbasierter Abrechnung (`anthropic/*`-Modelle)
  * **Claude CLI** — eine vorhandene Claude CLI-Anmeldung auf demselben Host wiederverwenden


## Erste Schritte

### API-Schlüssel

**Am besten geeignet für:** Standard-API-Zugriff und nutzungsbasierte Abrechnung.

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel in der [Anthropic Console](<https://console.anthropic.com/>).

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Oder übergeben Sie den Schlüssel direkt:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Am besten geeignet für:** Wiederverwendung einer vorhandenen Claude CLI-Anmeldung ohne separaten API-Schlüssel.

* ### Sicherstellen, dass Claude CLI installiert und angemeldet ist

Prüfen Sie dies mit:

bashCopy code
[code]
    claude --version
[/code]

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw erkennt die vorhandenen Claude CLI-Anmeldedaten und verwendet sie wieder.

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Konfigurationsbeispiel

Bevorzugen Sie die kanonische Anthropic-Modellreferenz plus eine CLI-Laufzeitüberschreibung:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Legacy-Modellreferenzen vom Typ `claude-cli/claude-opus-4-7` funktionieren aus Kompatibilitätsgründen weiterhin, neue Konfiguration sollte die Provider-/Modellauswahl jedoch als `anthropic/*` beibehalten und das Ausführungs-Backend in der Provider-/Modell-Laufzeitrichtlinie festlegen.

## Thinking-Standardwerte (Claude 4.6)

Claude 4.6-Modelle verwenden in OpenClaw standardmäßig `adaptive` Thinking, wenn keine explizite Thinking-Stufe gesetzt ist.

Überschreiben Sie dies pro Nachricht mit `/think:<level>` oder in Modellparametern:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Prompt-Caching

OpenClaw unterstützt Anthropics Prompt-Caching-Funktion für Authentifizierung per API-Schlüssel.

Wert | Cache-Dauer | Beschreibung  
---|---|---  
`"short"` (Standard) | 5 Minuten | Wird für API-Schlüssel-Authentifizierung automatisch angewendet  
`"long"` | 1 Stunde | Erweiterter Cache  
`"none"` | Kein Caching | Prompt-Caching deaktivieren  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Cache-Überschreibungen pro Agent

Verwenden Sie Modellparameter als Basis und überschreiben Sie anschließend bestimmte Agents über `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Reihenfolge beim Zusammenführen der Konfiguration:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (passende `id`, Überschreibung nach Schlüssel)


Dadurch kann ein Agent einen langlebigen Cache behalten, während ein anderer Agent auf demselben Modell das Caching für stoßartigen Traffic mit geringer Wiederverwendung deaktiviert.

Hinweise zu Bedrock Claude

  * Anthropic Claude-Modelle auf Bedrock (`amazon-bedrock/*anthropic.claude*`) akzeptieren konfiguriert eine `cacheRetention`-Durchleitung.
  * Nicht-Anthropic-Bedrock-Modelle werden zur Laufzeit auf `cacheRetention: "none"` gezwungen.
  * Intelligente Standardwerte für API-Schlüssel setzen außerdem `cacheRetention: "short"` für Claude-on-Bedrock-Referenzen, wenn kein expliziter Wert festgelegt ist.


## Erweiterte Konfiguration

Schneller Modus

Der gemeinsame `/fast`-Schalter von OpenClaw unterstützt direkten Anthropic-Traffic (API-Schlüssel und OAuth zu `api.anthropic.com`).

Befehl | Wird zugeordnet zu  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Medienverständnis (Bild und PDF)

Das gebündelte Anthropic-Plugin registriert Bild- und PDF-Verständnis. OpenClaw löst Medienfunktionen automatisch aus der konfigurierten Anthropic-Authentifizierung auf — es ist keine zusätzliche Konfiguration erforderlich.

Eigenschaft | Wert  
---|---  
Standardmodell | `claude-opus-4-7`  
Unterstützte Eingabe | Bilder, PDF-Dokumente  
  
Wenn ein Bild oder eine PDF an eine Unterhaltung angehängt wird, leitet OpenClaw sie automatisch über den Anthropic-Provider für Medienverständnis weiter.

1M-Kontextfenster (Beta)

Anthropics 1M-Kontextfenster ist Beta-gesteuert. Aktivieren Sie es pro Modell:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw ordnet dies bei Anfragen `anthropic-beta: context-1m-2025-08-07` zu.

`params.context1m: true` gilt auch für das Claude CLI-Backend (`claude-cli/*`) für berechtigte Opus- und Sonnet-Modelle und erweitert das Laufzeit- Kontextfenster dieser CLI-Sitzungen so, dass es dem direkten API-Verhalten entspricht.

Claude Opus 4.7 1M-Kontext

`anthropic/claude-opus-4.7` und seine `claude-cli`-Variante haben standardmäßig ein 1M-Kontextfenster — kein `params.context1m: true` erforderlich.

## Fehlerbehebung

401-Fehler / Token plötzlich ungültig

Anthropic-Token-Authentifizierung läuft ab und kann widerrufen werden. Verwenden Sie für neue Einrichtungen stattdessen einen Anthropic-API-Schlüssel.

Kein API-Schlüssel für Provider "anthropic" gefunden

Anthropic-Authentifizierung ist **pro Agent** — neue Agents erben die Schlüssel des Haupt-Agents nicht. Führen Sie das Onboarding für diesen Agent erneut aus (oder konfigurieren Sie einen API-Schlüssel auf dem Gateway-Host) und prüfen Sie anschließend mit `openclaw models status`.

Keine Anmeldedaten für Profil "anthropic:default" gefunden

Führen Sie `openclaw models status` aus, um zu sehen, welches Authentifizierungsprofil aktiv ist. Führen Sie das Onboarding erneut aus oder konfigurieren Sie einen API-Schlüssel für diesen Profilpfad.

Kein verfügbares Authentifizierungsprofil (alle in Cooldown)

Prüfen Sie `openclaw models status --json` auf `auth.unusableProfiles`. Anthropic-Rate-Limit-Cooldowns können modellspezifisch sein, daher kann ein benachbartes Anthropic-Modell weiterhin nutzbar sein. Fügen Sie ein weiteres Anthropic-Profil hinzu oder warten Sie den Cooldown ab.

## Verwandt

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**CLI-Backends** Einrichtung des Claude CLI-Backends und Laufzeitdetails. ](</de/gateway/cli-backends>) [**Prompt-Caching** Wie Prompt-Caching über Provider hinweg funktioniert. ](</de/reference/prompt-caching>) [**OAuth und Authentifizierung** Authentifizierungsdetails und Regeln zur Wiederverwendung von Anmeldedaten. ](</de/gateway/authentication>)

Was this useful?YesNo