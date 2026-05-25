---
title: OpenCode
source_url: https://docs.openclaw.ai/de/providers/opencode
scraped_at: 2026-05-25
---

OpenCode stellt in OpenClaw zwei gehostete Kataloge bereit:

Katalog | Präfix | Laufzeitanbieter  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Beide Kataloge verwenden denselben OpenCode-API-Schlüssel. OpenClaw hält die IDs der Laufzeitanbieter getrennt, damit das upstream Routing pro Modell korrekt bleibt, aber Onboarding und Dokumentation behandeln sie als ein gemeinsames OpenCode-Setup.

## Erste Schritte

### Zen catalog

**Am besten geeignet für:** den kuratierten OpenCode-Multimodell-Proxy (Claude, GPT, Gemini).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Oder übergeben Sie den Schlüssel direkt:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Zen model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**Am besten geeignet für:** die von OpenCode gehostete Auswahl von Kimi, GLM und MiniMax.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Oder übergeben Sie den Schlüssel direkt:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Go model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Integrierte Kataloge

### Zen

Eigenschaft | Wert  
---|---  
Laufzeitanbieter | `opencode`  
Beispielmodelle | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Eigenschaft | Wert  
---|---  
Laufzeitanbieter | `opencode-go`  
Beispielmodelle | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Erweiterte Konfiguration

API key aliases

`OPENCODE_ZEN_API_KEY` wird ebenfalls als Alias für `OPENCODE_API_KEY` unterstützt.

Shared credentials

Wenn Sie während der Einrichtung einen OpenCode-Schlüssel eingeben, werden Anmeldedaten für beide Laufzeitanbieter gespeichert. Sie müssen nicht jeden Katalog separat onboarden.

Billing and dashboard

Sie melden sich bei OpenCode an, hinterlegen Abrechnungsdaten und kopieren Ihren API-Schlüssel. Abrechnung und Katalogverfügbarkeit werden über das OpenCode-Dashboard verwaltet.

Gemini replay behavior

Von Gemini unterstützte OpenCode-Referenzen bleiben auf dem Proxy-Gemini-Pfad, daher behält OpenClaw dort die Bereinigung von Gemini-Thought-Signaturen bei, ohne die native Gemini-Replay-Validierung oder Bootstrap-Umschreibungen zu aktivieren.

Non-Gemini replay behavior

OpenCode-Referenzen ohne Gemini behalten die minimale OpenAI-kompatible Replay-Richtlinie bei.

## Verwandt

[**Modellauswahl** Auswahl von Anbietern, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige Konfigurationsreferenz für Agents, Modelle und Anbieter. ](</de/gateway/configuration-reference>)

Was this useful?YesNo