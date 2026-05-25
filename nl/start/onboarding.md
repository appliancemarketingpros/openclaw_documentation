---
title: Introductie (macOS-app)
source_url: https://docs.openclaw.ai/nl/start/onboarding
scraped_at: 2026-05-25
---

Dit document beschrijft de **huidige** setupflow bij de eerste start. Het doel is een soepele "dag 0"-ervaring: kies waar de Gateway draait, koppel authenticatie, doorloop de wizard en laat de agent zichzelf bootstrappen. Zie [Onboarding-overzicht](</nl/start/onboarding-overview>) voor een algemeen overzicht van onboardingpaden.

* ### macOS-waarschuwing goedkeuren

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Lokale netwerken zoeken goedkeuren

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Welkom en beveiligingsmelding

Lees de weergegeven beveiligingsmelding en beslis dienovereenkomstig ![](/assets/macos-onboarding/03-security-notice.png)

Beveiligingsvertrouwensmodel:

  * Standaard is OpenClaw een persoonlijke agent: één vertrouwde operatorgrens.
  * Gedeelde/multi-user setups vereisen vergrendeling (splits vertrouwensgrenzen, houd tooltoegang minimaal en volg [Beveiliging](</nl/gateway/security>)).
  * Lokale onboarding stelt nieuwe configuraties nu standaard in op `tools.profile: "coding"`, zodat nieuwe lokale setups filesystem-/runtime-tools behouden zonder het onbeperkte profiel `full` af te dwingen.
  * Als hooks/Webhooks of andere niet-vertrouwde contentfeeds zijn ingeschakeld, gebruik dan een sterk modern modelniveau en hanteer strikt toolbeleid/sandboxing.


* ### Lokaal versus extern

![](/assets/macos-onboarding/04-choose-gateway.png)

Waar draait de **Gateway**?

  * **Deze Mac (alleen lokaal):** onboarding kan authenticatie configureren en referenties lokaal wegschrijven.
  * **Extern (via SSH/Tailnet):** onboarding configureert **geen** lokale authenticatie; referenties moeten op de gatewayhost bestaan.
  * **Later configureren:** sla de setup over en laat de app ongeconfigureerd.


* ### Machtigingen

Kies welke machtigingen je OpenClaw wilt geven ![](/assets/macos-onboarding/05-permissions.png)

Onboarding vraagt TCC-machtigingen aan die nodig zijn voor:

  * Automatisering (AppleScript)
  * Meldingen
  * Toegankelijkheid
  * Schermopname
  * Microfoon
  * Spraakherkenning
  * Camera
  * Locatie


* ### CLI

* ### Onboardingchat (speciale sessie)

Na de setup opent de app een speciale onboardingchatsessie, zodat de agent zichzelf kan introduceren en de volgende stappen kan begeleiden. Zo blijft begeleiding bij de eerste start gescheiden van je normale gesprek. Zie [Bootstrapping](</nl/start/bootstrapping>) voor wat er op de gatewayhost gebeurt tijdens de eerste agentrun.

## Gerelateerd

  * [Onboarding-overzicht](</nl/start/onboarding-overview>)
  * [Aan de slag](</nl/start/getting-started>)


Was this useful?YesNo