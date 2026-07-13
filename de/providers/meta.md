---
title: Metadaten
source_url: https://docs.openclaw.ai/de/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

Die **Meta API** verwendet die OpenAI-kompatible **Responses API** (`POST /v1/responses`) für das Reasoning-Modell `muse-spark-1.1`. Der Provider wird als gebündeltes OpenClaw- Plugin ausgeliefert.

Eigenschaft | Wert  
---|---  
Provider-ID | `meta`  
Plugin | gebündelter Provider  
Authentifizierungs-Umgebungsvariable | `MODEL_API_KEY`  
Onboarding-Flag | `--auth-choice meta-api-key`  
Direktes CLI-Flag | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Basis-URL | `https://api.meta.ai/v1`  
Standardmodell | `meta/muse-spark-1.1`  
Standard-Reasoning | `high` (`reasoning.effort`)  
  
## Erste Schritte

* ### API-Schlüssel festlegen

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direktes FlagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Nur UmgebungsvariableCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verfügbarkeit der Modelle überprüfen

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Listet den statischen Katalogeintrag `muse-spark-1.1` auf. Wenn `MODEL_API_KEY` nicht aufgelöst werden kann, meldet `openclaw models status --json` die fehlenden Anmeldedaten unter `auth.unusableProfiles`.

## Nicht interaktive Einrichtung

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Integrierter Katalog

Modellreferenz | Name | Reasoning | Kontextfenster | Maximale Ausgabe  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | ja | 1.048.576 | 131.072  
  
Funktionen:

  * Text- und Bildeingabe
  * Tool-Aufrufe und Streaming
  * Reasoning-Aufwand: `minimal`, `low`, `medium`, `high`, `xhigh` (Standard: `high`)
  * Zustandslose Wiedergabe verschlüsselter Reasoning-Inhalte (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Manuelle Konfiguration

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Smoke-Test

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Live-Tests verwenden `muse-spark-1.1` mit `POST /v1/responses`.

## Verwandte Themen

[**Modell-Provider** Auswahl von Providern, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Denkmodi** Stufen des Reasoning-Aufwands für muse-spark-1.1. ](</de/tools/thinking>) [**Konfigurationsreferenz** Agent-Standardeinstellungen und Modellkonfiguration. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue