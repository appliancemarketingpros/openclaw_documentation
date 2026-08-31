---
title: Incidentrespons
source_url: https://docs.openclaw.ai/nl/security/incident-response
scraped_at: 2026-08-31
---

Get started

## 1\. Detectie en triage

Beveiligingssignalen zijn afkomstig van:

  * GitHub Security Advisories (GHSA) en privé gemelde kwetsbaarheden.
  * Openbare GitHub-issues/-discussies wanneer meldingen niet gevoelig zijn.
  * Geautomatiseerde signalen: Dependabot, CodeQL, npm-adviezen, secretscanning.


Eerste triage:

  1. Bevestig het getroffen onderdeel, de versie en de gevolgen voor de vertrouwensgrens.
  2. Classificeer het als beveiligingsprobleem of als hardening/geen actie, met behulp van de regels voor wat wel en niet binnen de reikwijdte van `SECURITY.md` valt.
  3. Een incidenteigenaar reageert dienovereenkomstig.


## 2\. Ernst

Ernst | Definitie  
---|---  
Kritiek | Compromittering van een pakket, release of repository, actieve uitbuiting of het zonder authenticatie omzeilen van een vertrouwensgrens, met ingrijpende controle of blootstelling van gegevens.  
Hoog | Geverifieerde omzeiling van een vertrouwensgrens waarvoor beperkte voorwaarden gelden (bijvoorbeeld een geauthenticeerde maar niet-geautoriseerde ingrijpende actie), of blootstelling van gevoelige OpenClaw-inloggegevens.  
Gemiddeld | Aanzienlijke beveiligingszwakte met praktische gevolgen, maar beperkte mogelijkheden tot uitbuiting of aanzienlijke vereisten vooraf.  
Laag | Bevindingen voor gelaagde beveiliging, een nauw afgebakende denial-of-service of hiaten in hardening/pariteit zonder aangetoonde omzeiling van een vertrouwensgrens.  
  
## 3\. Respons

  1. Bevestig de ontvangst aan de melder (privé wanneer de melding gevoelig is).
  2. Reproduceer het probleem op ondersteunde releases en de nieuwste `main`, implementeer en valideer vervolgens een patch met regressiedekking.
  3. Kritiek/hoog: bereid zo snel als praktisch mogelijk gepatchte release(s) voor.
  4. Gemiddeld/laag: neem de patch op in de normale releaseflow en documenteer richtlijnen voor risicobeperking.


## 4\. Communicatie en openbaarmaking

Communiceer via GitHub Security Advisories in de getroffen repository, releaseopmerkingen/changelog-items voor gecorrigeerde versies en rechtstreekse opvolging met de melder over de status en oplossing.

Bij kritieke/hoog-risico-incidenten vindt gecoördineerde openbaarmaking plaats, waarbij indien passend een CVE wordt uitgegeven. Hardeningbevindingen met een laag risico kunnen, afhankelijk van de gevolgen en blootstelling van gebruikers, zonder CVE worden gedocumenteerd in releaseopmerkingen of adviezen.

## 5\. Herstel en opvolging

Na het uitbrengen van de oplossing:

  1. Verifieer de herstelmaatregelen in CI en releaseartefacten.
  2. Voer een korte evaluatie na het incident uit: tijdlijn, hoofdoorzaak, tekortkoming in de detectie, preventieplan.
  3. Voeg opvolgtaken voor hardening/tests/documentatie toe en volg deze tot voltooiing.


## Gerelateerd

  * [Beveiligingsbeleid](<https://github.com/openclaw/openclaw/blob/main/SECURITY.md>) — reikwijdte van meldingen en vertrouwensmodel.
  * [Dreigingsmodel](</nl/security/THREAT-MODEL-ATLAS>)


Was this useful?YesNo

Open issue