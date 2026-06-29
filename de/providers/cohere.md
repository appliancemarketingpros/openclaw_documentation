---
title: Cohere
source_url: https://docs.openclaw.ai/de/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) stellt OpenAI-kompatible Inferenz über seine Compatibility API bereit. OpenClaw liefert den Cohere-Provider während seiner Externalisierungsphase mit und veröffentlicht ihn außerdem als offizielles externes Plugin mit dem Command A-Modellkatalog.

Eigenschaft | Wert  
---|---  
Provider-ID | `cohere`  
Plugin | während der Übergangsphase gebündelt; offizielles externes Paket  
Auth-Umgebungsvariable | `COHERE_API_KEY`  
Onboarding-Flag | `--auth-choice cohere-api-key`  
Direkte CLI-Flag | `--cohere-api-key <key>`  
API | OpenAI-kompatibel (`openai-completions`)  
Basis-URL | `https://api.cohere.ai/compatibility/v1`  
Standardmodell | `cohere/command-a-03-2025`  
  
## Erste Schritte

  1. Cohere ist in aktuellen OpenClaw-Paketen enthalten. Falls es nicht verfügbar ist, installieren Sie das externe Paket und starten Sie den Gateway neu:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Erstellen Sie einen Cohere-API-Schlüssel.
  3. Führen Sie das Onboarding aus:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Bestätigen Sie, dass der Katalog verfügbar ist:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Das Standardmodell wird nur festgelegt, wenn noch kein primäres Modell konfiguriert ist.

## Einrichtung nur über Umgebung

Machen Sie `COHERE_API_KEY` für den Gateway-Prozess verfügbar, und wählen Sie dann das Cohere-Modell aus:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Verwandte Themen

  * [Modell-Provider](</de/concepts/model-providers>)
  * [Modelle-CLI](</de/cli/models>)
  * [Provider-Verzeichnis](</de/providers>)


Was this useful?YesNo

Open issue