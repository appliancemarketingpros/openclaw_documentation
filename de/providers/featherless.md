---
title: Featherless AI
source_url: https://docs.openclaw.ai/de/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) stellt offene Modelle über eine OpenAI-kompatible API bereit. OpenClaw installiert Featherless als offizielles externes Provider-Plugin und hält den integrierten Katalog klein, während zur Laufzeit exakte Modell-IDs von Featherless akzeptiert werden.

Eigenschaft | Wert  
---|---  
Provider-ID | `featherless`  
Paket | `@openclaw/featherless-provider`  
Umgebungsvariable für Authentifizierung | `FEATHERLESS_API_KEY`  
Onboarding-Flag | `--auth-choice featherless-api-key`  
Direktes CLI-Flag | `--featherless-api-key <key>`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.featherless.ai/v1`  
Standardmodell | `featherless/Qwen/Qwen3-32B`  
  
## Einrichtung

Installieren Sie das Plugin und starten Sie den Gateway neu:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

Führen Sie das Onboarding aus:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Für die nicht interaktive Einrichtung:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Alternativ können Sie den Schlüssel für den Gateway-Prozess bereitstellen:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Überprüfen Sie den Provider:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Standardmodell

Das Plugin verwendet `Qwen/Qwen3-32B` als Standardmodell für die Einrichtung, weil Featherless native Werkzeugaufrufe für die Qwen-3-Familie dokumentiert. OpenClaw konfiguriert das Kontextfenster mit 32.768 Token, ein konservatives Ausgabelimit von 4.096 Token und die Denksteuerung der Qwen-Chatvorlage.

Die Kostenfelder des Katalogs sind null, da Featherless mehrere Abrechnungsmodelle unterstützt und OpenClaw keine kontospezifischen Tarife oder Preise pro Anfrage hinterlegt.

## Weitere Featherless-Modelle

Verwenden Sie nach dem Provider-Präfix `featherless/` die exakte Featherless-Modell-ID:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw übernimmt den vollständigen öffentlichen Modellindex von Featherless bewusst nicht in die Auswahl. Der Index ist umfangreich und stellt nicht genügend strukturierte Metadaten zu den Fähigkeiten bereit, um jedes Text-, Bildverarbeitungs-, Einbettungs- und Reasoning-Modell sicher zu klassifizieren. Unbekannte IDs werden daher mit konservativen Standardwerten für reine Textverarbeitung ohne Reasoning aufgelöst: einem Kontextfenster mit 4.096 Token und einem Ausgabelimit von 1.024 Token.

Fügen Sie einen expliziten Provider-Modelleintrag hinzu, wenn ein Modell abweichende Metadaten benötigt:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Prüfen Sie vor dem Hinzufügen benutzerdefinierter Metadaten im Modellkatalog von Featherless die aktuelle Verfügbarkeit der Modelle und deren Fähigkeitskennzeichnungen.

## Fehlerbehebung

  * `401` oder `403`: Stellen Sie sicher, dass `FEATHERLESS_API_KEY` für den Gateway- Prozess sichtbar ist, oder führen Sie das Onboarding erneut aus.
  * Unbekanntes Modell: Verwenden Sie nach dem Präfix `featherless/` die exakte, die Groß- und Kleinschreibung berücksichtigende ID von Featherless.
  * Werkzeugaufrufe werden als Text zurückgegeben: Wählen Sie eine Modellfamilie, für die Featherless native Funktionsaufrufe dokumentiert, beispielsweise Qwen 3.
  * Verwalteter Gateway kann nicht auf den Schlüssel zugreifen: Hinterlegen Sie ihn in `~/.openclaw/.env` oder einer anderen vom Dienst geladenen Umgebungsquelle und starten Sie anschließend den Gateway neu.


## Verwandte Themen

  * [Modell-Provider](</de/concepts/model-providers>)
  * [Alle Provider](</de/providers>)
  * [Denkmodi](</de/tools/thinking>)


Was this useful?YesNo

Open issue