---
title: Matrix-pushregels voor stille voorvertoningen
source_url: https://docs.openclaw.ai/nl/channels/matrix-push-rules
scraped_at: 2026-05-25
---

Wanneer `channels.matrix.streaming` `"quiet"` is, bewerkt OpenClaw een enkel voorbeeld-event op zijn plaats en markeert de definitieve bewerking met een aangepaste contentvlag. Matrix-clients melden de definitieve bewerking alleen als een pushregel per gebruiker overeenkomt met die vlag. Deze pagina is bedoeld voor operators die Matrix zelf hosten en die regel voor elk ontvangend account willen installeren.

Als je alleen standaard Matrix-meldingsgedrag wilt, gebruik dan `streaming: "partial"` of laat streaming uit. Zie [Matrix-kanaalconfiguratie](</nl/channels/matrix#streaming-previews>).

## Vereisten

  * ontvangende gebruiker = de persoon die de melding moet ontvangen
  * botgebruiker = het OpenClaw Matrix-account dat het antwoord verzendt
  * gebruik de toegangstoken van de ontvangende gebruiker voor de API-aanroepen hieronder
  * laat `sender` in de pushregel overeenkomen met de volledige MXID van de botgebruiker
  * het ontvangende account moet al werkende pushers hebben — regels voor stille voorbeelden werken alleen wanneer normale Matrix-pushbezorging gezond is


## Stappen

* ### Stille voorbeelden configureren

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### De toegangstoken van de ontvanger ophalen

Hergebruik waar mogelijk een bestaande clientsessietoken. Om een nieuwe aan te maken:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Controleren of pushers bestaan

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Als er geen pushers terugkomen, herstel dan eerst de normale Matrix-pushbezorging voor dit account voordat je verdergaat.

* ### De overschrijvende pushregel installeren

OpenClaw markeert definitieve tekst-only voorbeeldbewerkingen met `content["com.openclaw.finalized_preview"] = true`. Installeer een regel die overeenkomt met die markering plus de bot-MXID als afzender:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Vervang vóór het uitvoeren:

  * `https://matrix.example.org`: de basis-URL van je homeserver
  * `$USER_ACCESS_TOKEN`: de toegangstoken van de ontvangende gebruiker
  * `openclaw-finalized-preview-botname`: een regel-ID die uniek is per bot per ontvanger (patroon: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: je OpenClaw bot-MXID, niet die van de ontvanger


* ### Controleren

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Test daarna een gestreamd antwoord. In stille modus toont de ruimte een stil conceptvoorbeeld en wordt er één melding verzonden zodra het blok of de beurt is voltooid.

Om de regel later te verwijderen, gebruik je `DELETE` op dezelfde regel-URL met de token van de ontvanger.

## Opmerkingen voor meerdere bots

Pushregels worden gesleuteld op `ruleId`: het opnieuw uitvoeren van `PUT` op dezelfde ID werkt één regel bij. Voor meerdere OpenClaw-bots die dezelfde ontvanger melden, maak je één regel per bot met een afzonderlijke afzendermatch.

Nieuwe door de gebruiker gedefinieerde `override`-regels worden vóór standaard onderdrukkingsregels ingevoegd, dus er is geen extra volgordeparameter nodig. De regel heeft alleen invloed op tekst-only voorbeeldbewerkingen die op hun plaats kunnen worden afgerond; mediafallbacks en fallbacks voor verouderde voorbeelden gebruiken normale Matrix-bezorging.

## Homeserver-opmerkingen

Synapse

Er is geen speciale wijziging in `homeserver.yaml` vereist. Als normale Matrix-meldingen deze gebruiker al bereiken, is de ontvangertoken plus de `pushrules`-aanroep hierboven de belangrijkste configuratiestap.

Als je Synapse achter een reverse proxy of workers draait, zorg er dan voor dat `/_matrix/client/.../pushrules/` Synapse correct bereikt. Pushbezorging wordt afgehandeld door het hoofdproces of `synapse.app.pusher` / geconfigureerde pusher-workers — zorg dat die gezond zijn.

De regel gebruikt de pushregelvoorwaarde `event_property_is` (MSC3758, pushregel v1.10), die in 2023 aan Synapse is toegevoegd. Oudere Synapse-releases accepteren de aanroep `PUT pushrules/...`, maar laten de voorwaarde stilzwijgend nooit overeenkomen — upgrade Synapse als er geen melding aankomt bij een definitieve voorbeeldbewerking.

Tuwunel

Dezelfde flow als Synapse; er is geen Tuwunel-specifieke configuratie nodig voor de definitieve voorbeeldmarkering.

Als meldingen verdwijnen terwijl de gebruiker actief is op een ander apparaat, controleer dan of `suppress_push_when_active` is ingeschakeld. Tuwunel heeft deze optie toegevoegd in 1.4.2 (september 2025) en deze kan pushes naar andere apparaten bewust onderdrukken terwijl één apparaat actief is.

## Gerelateerd

  * [Matrix-kanaalconfiguratie](</nl/channels/matrix>)
  * [Streaming-concepten](</nl/concepts/streaming>)


Was this useful?YesNo