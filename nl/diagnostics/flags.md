---
title: Diagnosevlaggen
source_url: https://docs.openclaw.ai/nl/diagnostics/flags
scraped_at: 2026-05-25
---

Met diagnostische vlaggen kun je gerichte debuglogs inschakelen zonder overal uitgebreide logging aan te zetten. Vlaggen zijn opt-in en hebben geen effect tenzij een subsysteem ze controleert.

## Hoe het werkt

  * Vlaggen zijn tekenreeksen (niet hoofdlettergevoelig).
  * Je kunt vlaggen inschakelen in de configuratie of via een env-override.
  * Wildcards worden ondersteund: 
    * `telegram.*` komt overeen met `telegram.http`
    * `*` schakelt alle vlaggen in


## Inschakelen via configuratie

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Meerdere vlaggen:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Herstart de Gateway nadat je vlaggen hebt gewijzigd.

## Env-override (eenmalig)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Alle vlaggen uitschakelen:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Timeline-artefacten

De vlag `timeline` schrijft gestructureerde timinggebeurtenissen bij opstarten en tijdens runtime voor externe QA-harnassen:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Je kunt deze ook inschakelen in de configuratie:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Het pad naar het timeline-bestand komt nog steeds uit `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Wanneer `timeline` alleen via configuratie is ingeschakeld, worden de vroegste spans voor het laden van de configuratie niet uitgezonden, omdat OpenClaw de configuratie nog niet heeft gelezen; daaropvolgende opstartspans gebruiken de configuratievlag.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` en `OPENCLAW_DIAGNOSTICS=*` schakelen ook de timeline in, omdat ze elke diagnostische vlag inschakelen. Geef de voorkeur aan `timeline` wanneer je alleen het JSONL-timingartefact wilt.

Timeline-records gebruiken de envelop `openclaw.diagnostics.v1`. Gebeurtenissen kunnen proces-id's, fasenamen, spannamen, duurwaarden, Plugin-id's, aantallen afhankelijkheden, event-loop-vertragingssamples, namen van providerbewerkingen, exitstatus van child-processen en namen/berichten van opstartfouten bevatten. Behandel timeline-bestanden als lokale diagnostische artefacten; controleer ze voordat je ze buiten je machine deelt.

## Waar logs naartoe gaan

Vlaggen schrijven logs naar het standaard diagnostische logbestand. Standaard:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Als je `logging.file` instelt, gebruik dan in plaats daarvan dat pad. Logs zijn JSONL (één JSON-object per regel). Redactie blijft van toepassing op basis van `logging.redactSensitive`.

## Logs extraheren

Kies het nieuwste logbestand:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filter op Telegram HTTP-diagnostiek:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filter op Brave Search HTTP-diagnostiek:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Of volg de logs tijdens het reproduceren:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Voor externe Gateways kun je ook `openclaw logs --follow` gebruiken (zie [/cli/logs](</nl/cli/logs>)).

## Opmerkingen

  * Als `logging.level` hoger is ingesteld dan `warn`, kunnen deze logs worden onderdrukt. De standaardwaarde `info` is prima.
  * `brave.http` logt Brave Search-aanvraag-URL's/queryparameters, responsstatus/timing en gebeurtenissen voor cache-hit/miss/write. Het logt geen API-sleutels of responsbodies, maar zoekopdrachten kunnen gevoelig zijn.
  * Vlaggen kunnen veilig ingeschakeld blijven; ze beïnvloeden alleen het logvolume voor het specifieke subsysteem.
  * Gebruik [/logging](</nl/logging>) om logbestemmingen, niveaus en redactie te wijzigen.


## Gerelateerd

  * [Gateway-diagnostiek](</nl/gateway/diagnostics>)
  * [Gateway-probleemoplossing](</nl/gateway/troubleshooting>)


Was this useful?YesNo