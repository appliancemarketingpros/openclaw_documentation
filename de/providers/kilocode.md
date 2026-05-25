---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/de/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway stellt eine **einheitliche API** bereit, die Anfragen hinter einem einzigen Endpunkt und API-Schlüssel an viele Modelle weiterleitet. Sie ist OpenAI-kompatibel, daher funktionieren die meisten OpenAI-SDKs durch Ändern der Basis-URL.

Eigenschaft | Wert  
---|---  
Provider | `kilocode`  
Authentifizierung | `KILOCODE_API_KEY`  
API | OpenAI-kompatibel  
Basis-URL | `https://api.kilo.ai/api/gateway/`  
  
## Erste Schritte

* ### Konto erstellen

Gehen Sie zu [app.kilo.ai](<https://app.kilo.ai>), melden Sie sich an oder erstellen Sie ein Konto, navigieren Sie anschließend zu API Keys und generieren Sie einen neuen Schlüssel.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Oder legen Sie die Umgebungsvariable direkt fest:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Standardmodell

Das Standardmodell ist `kilocode/kilo/auto`, ein Provider-eigenes Smart-Routing- Modell, das von Kilo Gateway verwaltet wird.

## Integrierter Katalog

OpenClaw ermittelt verfügbare Modelle beim Start dynamisch aus dem Kilo Gateway. Verwenden Sie `/models kilocode`, um die vollständige Liste der mit Ihrem Konto verfügbaren Modelle anzuzeigen.

Jedes auf dem Gateway verfügbare Modell kann mit dem Präfix `kilocode/` verwendet werden:

Modellreferenz | Hinweise  
---|---  
`kilocode/kilo/auto` | Standard - Smart Routing  
`kilocode/anthropic/claude-sonnet-4` | Anthropic über Kilo  
`kilocode/openai/gpt-5.5` | OpenAI über Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google über Kilo  
...und viele weitere | Verwenden Sie `/models kilocode`, um alle aufzulisten  
  
## Konfigurationsbeispiel

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport und Kompatibilität

Kilo Gateway ist im Quellcode als OpenRouter-kompatibel dokumentiert, daher bleibt es auf dem Proxy-artigen OpenAI-kompatiblen Pfad statt auf nativer OpenAI-Anfrageformung.

  * Gemini-gestützte Kilo-Referenzen bleiben auf dem Proxy-Gemini-Pfad, daher behält OpenClaw dort die Bereinigung von Gemini-Gedankensignaturen bei, ohne native Gemini- Replay-Validierung oder Bootstrap-Umschreibungen zu aktivieren.
  * Kilo Gateway verwendet intern ein Bearer-Token mit Ihrem API-Schlüssel.

Stream-Wrapper und Reasoning

Kilos gemeinsamer Stream-Wrapper ergänzt den Provider-App-Header und normalisiert Proxy-Reasoning-Payloads für unterstützte konkrete Modellreferenzen.

Fehlerbehebung

  * Wenn die Modellerkennung beim Start fehlschlägt, fällt OpenClaw auf den gebündelten statischen Katalog mit `kilocode/kilo/auto` zurück.
  * Stellen Sie sicher, dass Ihr API-Schlüssel gültig ist und dass für Ihr Kilo-Konto die gewünschten Modelle aktiviert sind.
  * Wenn der Gateway als Daemon läuft, stellen Sie sicher, dass `KILOCODE_API_KEY` für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).


## Verwandte Themen

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständige OpenClaw-Konfigurationsreferenz. ](</de/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway-Dashboard, API-Schlüssel und Kontoverwaltung. ](<https://app.kilo.ai>)

Was this useful?YesNo