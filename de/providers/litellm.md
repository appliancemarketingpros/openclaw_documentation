---
title: LiteLLM
source_url: https://docs.openclaw.ai/de/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) ist ein Open-Source-LLM-Gateway, das eine einheitliche API für mehr als 100 Modell-Provider bereitstellt. Leiten Sie OpenClaw über LiteLLM, um zentrale Kostenerfassung, Logging und die Flexibilität zu erhalten, Backends zu wechseln, ohne Ihre OpenClaw-Konfiguration zu ändern.

## Schnellstart

### Onboarding (empfohlen)

**Am besten geeignet für:** den schnellsten Weg zu einer funktionierenden LiteLLM-Einrichtung.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Für eine nicht interaktive Einrichtung mit einem Remote-Proxy übergeben Sie die Proxy-URL explizit:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manuelle Einrichtung

**Am besten geeignet für:** vollständige Kontrolle über Installation und Konfiguration.

* ### LiteLLM-Proxy starten

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### OpenClaw auf LiteLLM ausrichten

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Das war's. OpenClaw leitet jetzt über LiteLLM weiter.

## Konfiguration

### Umgebungsvariablen

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Konfigurationsdatei

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Erweiterte Konfiguration

### Bilderzeugung

LiteLLM kann auch das Tool `image_generate` über OpenAI-kompatible `/images/generations`\- und `/images/edits`-Routen für OpenClaw bereitstellen. Konfigurieren Sie ein LiteLLM-Bildmodell unter `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Loopback-LiteLLM-URLs wie `http://localhost:4000` funktionieren ohne globale Private-Network-Überschreibung. Legen Sie für einen im LAN gehosteten Proxy `models.providers.litellm.request.allowPrivateNetwork: true` fest, da der API-Schlüssel an den konfigurierten Proxy-Host gesendet wird.

Virtuelle Schlüssel

Erstellen Sie einen dedizierten Schlüssel für OpenClaw mit Ausgabenlimits:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Verwenden Sie den generierten Schlüssel als `LITELLM_API_KEY`.

Modell-Routing

LiteLLM kann Modellanfragen an verschiedene Backends weiterleiten. Konfigurieren Sie dies in Ihrer LiteLLM-`config.yaml`:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw fordert weiterhin `claude-opus-4-6` an — LiteLLM übernimmt das Routing.

Nutzung anzeigen

Prüfen Sie das Dashboard oder die API von LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Hinweise zum Proxy-Verhalten

  * LiteLLM läuft standardmäßig auf `http://localhost:4000`
  * OpenClaw verbindet sich über den Proxy-artigen OpenAI-kompatiblen `/v1`-Endpunkt von LiteLLM
  * Reine native OpenAI-Anfrageformung gilt nicht über LiteLLM: kein `service_tier`, kein Responses-`store`, keine Prompt-Cache-Hinweise und keine OpenAI-Reasoning-Kompatibilitäts-Payload-Formung
  * Verdeckte OpenClaw-Attributions-Header (`originator`, `version`, `User-Agent`) werden bei benutzerdefinierten LiteLLM-Basis-URLs nicht eingefügt


## Verwandte Themen

[**LiteLLM-Dokumentation** Offizielle LiteLLM-Dokumentation und API-Referenz. ](<https://docs.litellm.ai>) [**Modellauswahl** Überblick über alle Provider, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Konfiguration** Vollständige Konfigurationsreferenz. ](</de/gateway/configuration>) [**Modellauswahl** So wählen und konfigurieren Sie Modelle. ](</de/concepts/models>)

Was this useful?YesNo