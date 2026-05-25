---
title: Cerebras
source_url: https://docs.openclaw.ai/de/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) bietet schnelle OpenAI-kompatible Inferenz auf spezieller Inferenzhardware. OpenClaw enthält ein gebündeltes Cerebras-Provider-Plugin mit einem statischen Katalog aus vier Modellen.

Eigenschaft | Wert  
---|---  
Provider-ID | `cerebras`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Umgebungsvariable | `CEREBRAS_API_KEY`  
Onboarding-Flag | `--auth-choice cerebras-api-key`  
Direktes CLI-Flag | `--cerebras-api-key <key>`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.cerebras.ai/v1`  
Standardmodell | `cerebras/zai-glm-4.7`  
  
## Erste Schritte

* ### API-Schlüssel abrufen

Erstellen Sie einen API-Schlüssel in der [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Onboarding ausführen

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Prüfen, ob Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Die Liste sollte alle vier gebündelten Modelle enthalten. Wenn `CEREBRAS_API_KEY` nicht aufgelöst werden kann, meldet `openclaw models status --json` die fehlende Anmeldeinformation unter `auth.unusableProfiles`.

## Nicht interaktive Einrichtung

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Integrierter Katalog

OpenClaw liefert einen statischen Cerebras-Katalog aus, der den öffentlichen OpenAI-kompatiblen Endpunkt widerspiegelt. Alle vier Modelle teilen sich einen Kontext von 128k und maximal 8.192 Ausgabetoken.

Modellreferenz | Name | Reasoning | Hinweise  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | ja | Standardmodell; Reasoning-Vorschaumodell  
`cerebras/gpt-oss-120b` | GPT OSS 120B | ja | Produktions-Reasoning-Modell  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | nein | Vorschaumodell ohne Reasoning  
`cerebras/llama3.1-8b` | Llama 3.1 8B | nein | Produktivmodell mit Fokus auf Geschwindigkeit  
  
## Manuelle Konfiguration

Das gebündelte Plugin bedeutet normalerweise, dass Sie nur den API-Schlüssel benötigen. Verwenden Sie eine explizite `models.providers.cerebras`-Konfiguration, wenn Sie Modellmetadaten überschreiben oder mit `mode: "merge"` gegen den statischen Katalog ausführen möchten:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Verwandte Themen

[**Modell-Provider** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Denkmodi** Reasoning-Aufwandsstufen für die zwei Reasoning-fähigen Cerebras-Modelle. ](</de/tools/thinking>) [**Konfigurationsreferenz** Agent-Standardeinstellungen und Modellkonfiguration. ](</de/gateway/config-agents#agent-defaults>) [**Modelle-FAQ** Auth-Profile, Modelle wechseln und „no profile“-Fehler beheben. ](</de/help/faq-models>)

Was this useful?YesNo