---
title: Locatiecommando
source_url: https://docs.openclaw.ai/nl/nodes/location-command
scraped_at: 2026-05-25
---

## TL;DR

  * `location.get` is een Node-opdracht (via `node.invoke`).
  * Standaard uitgeschakeld.
  * Android-appinstellingen gebruiken een selector: Uit / Tijdens gebruik.
  * Aparte schakelaar: Nauwkeurige locatie.


## Waarom een selector (niet alleen een schakelaar)

Besturingssysteemmachtigingen hebben meerdere niveaus. We kunnen in de app een selector aanbieden, maar het besturingssysteem bepaalt nog steeds de daadwerkelijke toekenning.

  * iOS/macOS kan **Tijdens gebruik** of **Altijd** tonen in systeemprompts/Instellingen.
  * De Android-app ondersteunt momenteel alleen locatie op de voorgrond.
  * Nauwkeurige locatie is een aparte toekenning (iOS 14+ "Nauwkeurig", Android "fine" vs "coarse").


De selector in de UI bepaalt de modus die wij aanvragen; de daadwerkelijke toekenning bevindt zich in de instellingen van het besturingssysteem.

## Instellingenmodel

Per Node-apparaat:

  * `location.enabledMode`: `off | whileUsing`
  * `location.preciseEnabled`: bool


UI-gedrag:

  * Het selecteren van `whileUsing` vraagt toestemming voor gebruik op de voorgrond.
  * Als het besturingssysteem het gevraagde niveau weigert, val terug naar het hoogste toegekende niveau en toon de status.


## Machtigingstoewijzing (node.permissions)

Optioneel. De macOS-Node rapporteert `location` via de machtigingenmap; iOS/Android kan dit weglaten.

## Opdracht: `location.get`

Aangeroepen via `node.invoke`.

Parameters (voorgesteld):

jsonCopy code
[code]
    {  "timeoutMs": 10000,  "maxAgeMs": 15000,  "desiredAccuracy": "coarse|balanced|precise"}
[/code]

Antwoordpayload:

jsonCopy code
[code]
    {  "lat": 48.20849,  "lon": 16.37208,  "accuracyMeters": 12.5,  "altitudeMeters": 182.0,  "speedMps": 0.0,  "headingDeg": 270.0,  "timestamp": "2026-01-03T12:34:56.000Z",  "isPrecise": true,  "source": "gps|wifi|cell|unknown"}
[/code]

Fouten (stabiele codes):

  * `LOCATION_DISABLED`: selector staat uit.
  * `LOCATION_PERMISSION_REQUIRED`: toestemming ontbreekt voor de gevraagde modus.
  * `LOCATION_BACKGROUND_UNAVAILABLE`: app draait op de achtergrond, maar alleen Tijdens gebruik is toegestaan.
  * `LOCATION_TIMEOUT`: geen positiebepaling op tijd.
  * `LOCATION_UNAVAILABLE`: systeemfout / geen providers.


## Achtergrondgedrag

  * De Android-app weigert `location.get` terwijl deze op de achtergrond draait.
  * Houd OpenClaw open wanneer je locatie op Android opvraagt.
  * Andere Node-platforms kunnen verschillen.


## Model-/toolingintegratie

  * Tooloppervlak: `nodes`-tool voegt de actie `location_get` toe (Node vereist).
  * CLI: `openclaw nodes location get --node <id>`.
  * Agentrichtlijnen: alleen aanroepen wanneer de gebruiker locatie heeft ingeschakeld en de reikwijdte begrijpt.


## UX-tekst (voorgesteld)

  * Uit: "Locatie delen is uitgeschakeld."
  * Tijdens gebruik: "Alleen wanneer OpenClaw open is."
  * Nauwkeurig: "Gebruik nauwkeurige GPS-locatie. Schakel uit om een geschatte locatie te delen."


## Gerelateerd

  * [Locatieparsing voor kanalen](</nl/channels/location>)
  * [Camera-opname](</nl/nodes/camera>)
  * [Praatmodus](</nl/nodes/talk>)


Was this useful?YesNo