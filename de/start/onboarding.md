---
title: Onboarding (macOS-App)
source_url: https://docs.openclaw.ai/de/start/onboarding
scraped_at: 2026-05-25
---

Dieses Dokument beschreibt den **aktuellen** Einrichtungsablauf beim ersten Start. Ziel ist eine reibungslose „Tag 0“-Erfahrung: auswählen, wo der Gateway ausgeführt wird, Authentifizierung verbinden, den Assistenten ausführen und den Agenten sich selbst bootstrappen lassen. Eine allgemeine Übersicht über Onboarding-Pfade finden Sie unter [Onboarding-Übersicht](</de/start/onboarding-overview>).

* ### macOS-Warnung bestätigen

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Suche nach lokalen Netzwerken genehmigen

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Willkommen und Sicherheitshinweis

Lesen Sie den angezeigten Sicherheitshinweis und entscheiden Sie entsprechend ![](/assets/macos-onboarding/03-security-notice.png)

Sicherheits-Vertrauensmodell:

  * Standardmäßig ist OpenClaw ein persönlicher Agent: eine vertrauenswürdige Betreibergrenze.
  * Gemeinsame/Mehrbenutzer-Setups erfordern Absicherung (Vertrauensgrenzen trennen, Tool-Zugriff minimal halten und [Sicherheit](</de/gateway/security>) befolgen).
  * Lokales Onboarding setzt neue Konfigurationen jetzt standardmäßig auf `tools.profile: "coding"`, damit frische lokale Setups Dateisystem-/Runtime-Tools behalten, ohne das uneingeschränkte Profil `full` zu erzwingen.
  * Wenn Hooks/Webhooks oder andere Feeds mit nicht vertrauenswürdigen Inhalten aktiviert sind, verwenden Sie eine starke moderne Modellstufe und halten Sie Tool-Richtlinien/Sandboxing streng.


* ### Lokal vs. Remote

![](/assets/macos-onboarding/04-choose-gateway.png)

Wo wird der **Gateway** ausgeführt?

  * **Dieser Mac (nur lokal):** Das Onboarding kann Authentifizierung konfigurieren und Anmeldedaten lokal schreiben.
  * **Remote (über SSH/Tailnet):** Das Onboarding konfiguriert **keine** lokale Authentifizierung; Anmeldedaten müssen auf dem Gateway-Host vorhanden sein.
  * **Später konfigurieren:** Einrichtung überspringen und die App unkonfiguriert lassen.


* ### Berechtigungen

Wählen Sie aus, welche Berechtigungen Sie OpenClaw erteilen möchten ![](/assets/macos-onboarding/05-permissions.png)

Das Onboarding fordert TCC-Berechtigungen an, die benötigt werden für:

  * Automatisierung (AppleScript)
  * Benachrichtigungen
  * Bedienungshilfen
  * Bildschirmaufnahme
  * Mikrofon
  * Spracherkennung
  * Kamera
  * Standort


* ### CLI

* ### Onboarding-Chat (dedizierte Sitzung)

Nach der Einrichtung öffnet die App eine dedizierte Onboarding-Chat-Sitzung, damit der Agent sich vorstellen und durch die nächsten Schritte führen kann. Dadurch bleibt die Anleitung beim ersten Start von Ihrer normalen Unterhaltung getrennt. Unter [Bootstrapping](</de/start/bootstrapping>) erfahren Sie, was beim ersten Agentenlauf auf dem Gateway-Host passiert.

## Verwandt

  * [Onboarding-Übersicht](</de/start/onboarding-overview>)
  * [Erste Schritte](</de/start/getting-started>)


Was this useful?YesNo