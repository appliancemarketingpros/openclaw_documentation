---
title: Feuerwerk
source_url: https://docs.openclaw.ai/de/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) stellt Open-Weight- und geroutete Modelle über eine OpenAI-kompatible API bereit. OpenClaw enthält ein gebündeltes Fireworks-Provider-Plugin, das mit zwei vorkatalogisierten Kimi-Modellen ausgeliefert wird und zur Laufzeit jede Fireworks-Modell- oder Router-ID akzeptiert.

Eigenschaft | Wert  
---|---  
Provider-ID | `fireworks` (Alias: `fireworks-ai`)  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Env-Var | `FIREWORKS_API_KEY`  
Einrichtungs-Flag | `--auth-choice fireworks-api-key`  
Direktes CLI-Flag | `--fireworks-api-key <key>`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.fireworks.ai/inference/v1`  
Standardmodell | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Standardalias | `Kimi K2.5 Turbo`  
  
## Erste Schritte

* ### Fireworks-API-Schlüssel festlegen

EinrichtungCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direktes FlagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Nur EnvCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Die Einrichtung speichert den Schlüssel für den `fireworks`-Provider in Ihren Auth-Profilen und legt den **Fire Pass** -Router Kimi K2.5 Turbo als Standardmodell fest.

* ### Verfügbarkeit des Modells prüfen

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Die Liste sollte `Kimi K2.6` und `Kimi K2.5 Turbo (Fire Pass)` enthalten. Wenn `FIREWORKS_API_KEY` nicht aufgelöst wird, meldet `openclaw models status --json` die fehlenden Zugangsdaten unter `auth.unusableProfiles`.

## Nicht interaktive Einrichtung

Für skriptgesteuerte oder CI-Installationen übergeben Sie alles über die Befehlszeile:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Integrierter Katalog

Modellreferenz | Name | Eingabe | Kontext | Maximale Ausgabe | Denken  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | Text + Bild | 262,144 | 262,144 | Erzwungen deaktiviert  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | Text + Bild | 256,000 | 256,000 | Erzwungen deaktiviert (Standard)  
  
## Benutzerdefinierte Fireworks-Modell-IDs

OpenClaw akzeptiert zur Laufzeit jede Fireworks-Modell- oder Router-ID. Verwenden Sie die exakte von Fireworks angezeigte ID und stellen Sie ihr `fireworks/` voran. Die dynamische Auflösung klont die Fire-Pass-Vorlage (Text- und Bildeingabe, OpenAI-kompatible API, Standardkosten null) und deaktiviert das Denken automatisch, wenn die ID dem Kimi-Muster entspricht.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

So funktioniert das Voranstellen des Modell-ID-Präfixes

Jede Fireworks-Modellreferenz in OpenClaw beginnt mit `fireworks/`, gefolgt von der exakten ID oder dem Router-Pfad von der Fireworks-Plattform. Beispiel:

  * Router-Modell: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Direktes Modell: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw entfernt beim Erstellen der API-Anfrage das Präfix `fireworks/` und sendet den verbleibenden Pfad als OpenAI-kompatibles Feld `model` an den Fireworks-Endpunkt.

Warum Denken für Kimi erzwungen deaktiviert ist

Fireworks K2.6 gibt einen 400-Fehler zurück, wenn die Anfrage `reasoning_*`-Parameter enthält, obwohl Kimi Denken über Moonshots eigene API unterstützt. Die gebündelte Richtlinie (`extensions/fireworks/thinking-policy.ts`) weist für Kimi-Modell-IDs nur die Denklstufe `off` aus, sodass manuelle `/think`-Wechsel und Provider-Richtlinienoberflächen mit dem Laufzeitvertrag abgestimmt bleiben.

Um Kimi-Reasoning durchgängig zu verwenden, konfigurieren Sie den [Moonshot-Provider](</de/providers/moonshot>) und routen Sie dasselbe Modell darüber.

Umgebungsverfügbarkeit für den Daemon

Wenn der Gateway als verwalteter Dienst läuft (launchd, systemd, Docker), muss der Fireworks-Schlüssel für diesen Prozess sichtbar sein, nicht nur für Ihre interaktive Shell.

Unter macOS bindet `openclaw gateway install` `~/.openclaw/.env` bereits in die LaunchAgent-Umgebungsdatei ein. Führen Sie die Installation nach dem Rotieren des Schlüssels erneut aus (oder `openclaw doctor --fix`).

## Verwandte Themen

[**Modell-Provider** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Denkmodi** `/think`-Stufen, Provider-Richtlinien und Routing von Reasoning-fähigen Modellen. ](</de/tools/thinking>) [**Moonshot** Führen Sie Kimi mit nativer Denkausgabe über Moonshots eigene API aus. ](</de/providers/moonshot>) [**Fehlerbehebung** Allgemeine Fehlerbehebung und FAQ. ](</de/help/troubleshooting>)

Was this useful?YesNo