---
title: Modus met verhoogde rechten
source_url: https://docs.openclaw.ai/nl/tools/elevated
scraped_at: 2026-05-25
---

Wanneer een agent binnen een sandbox draait, zijn de `exec`-opdrachten beperkt tot de sandboxomgeving. **Verhoogde modus** laat de agent daaruit breken en in plaats daarvan opdrachten buiten de sandbox uitvoeren, met configureerbare goedkeuringspoorten.

## Richtlijnen

Beheer verhoogde modus per sessie met slash-opdrachten:

Richtlijn | Wat deze doet  
---|---  
`/elevated on` | Buiten de sandbox uitvoeren op het geconfigureerde hostpad, goedkeuringen behouden  
`/elevated ask` | Hetzelfde als `on` (alias)  
`/elevated full` | Buiten de sandbox uitvoeren op het geconfigureerde hostpad en goedkeuringen overslaan  
`/elevated off` | Terugkeren naar uitvoering die tot de sandbox beperkt is  
  
Ook beschikbaar als `/elev on|off|ask|full`.

Stuur `/elevated` zonder argument om het huidige niveau te zien.

## Hoe het werkt

* ### Beschikbaarheid controleren

Verhoogd moet in de configuratie zijn ingeschakeld en de afzender moet op de toegestane lijst staan:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Het niveau instellen

Stuur een bericht dat alleen uit een richtlijn bestaat om de sessiestandaard in te stellen:

CodeCopy code
[code]
    /elevated full
[/code]

Of gebruik het inline (geldt alleen voor dat bericht):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Opdrachten worden buiten de sandbox uitgevoerd

Met verhoogd actief verlaten `exec`-aanroepen de sandbox. De effectieve host is standaard `gateway`, of `node` wanneer het geconfigureerde exec-doel of sessie-exec-doel `node` is. In `full`-modus worden exec-goedkeuringen overgeslagen. In `on`/`ask`-modus blijven geconfigureerde goedkeuringsregels gelden.

## Volgorde van oplossing

  1. **Inline richtlijn** in het bericht (geldt alleen voor dat bericht)
  2. **Sessie-overschrijving** (ingesteld door een bericht te sturen dat alleen uit een richtlijn bestaat)
  3. **Globale standaard** (`agents.defaults.elevatedDefault` in de configuratie)


## Beschikbaarheid en toegestane lijsten

  * **Globale poort** : `tools.elevated.enabled` (moet `true` zijn)
  * **Toegestane lijst voor afzenders** : `tools.elevated.allowFrom` met lijsten per kanaal
  * **Poort per agent** : `agents.list[].tools.elevated.enabled` (kan alleen verder beperken)
  * **Toegestane lijst per agent** : `agents.list[].tools.elevated.allowFrom` (afzender moet zowel globaal als per agent overeenkomen)
  * **Discord-terugval** : als `tools.elevated.allowFrom.discord` is weggelaten, wordt `channels.discord.allowFrom` als terugval gebruikt
  * **Alle poorten moeten slagen** ; anders wordt verhoogd als niet beschikbaar behandeld


Indelingen voor vermeldingen in de toegestane lijst:

Voorvoegsel | Komt overeen met  
---|---  
(geen) | Afzender-ID, E.164 of From-veld  
`name:` | Weergavenaam van afzender  
`username:` | Gebruikersnaam van afzender  
`tag:` | Tag van afzender  
`id:`, `from:`, `e164:` | Expliciete identiteitstargeting  
  
## Wat verhoogd niet beheert

  * **Toolbeleid** : als `exec` door toolbeleid wordt geweigerd, kan verhoogd dat niet overschrijven.
  * **Hostselectiebeleid** : verhoogd verandert `auto` niet in een vrije cross-host-overschrijving. Het gebruikt de geconfigureerde regels of sessieregels voor het exec-doel en kiest alleen `node` wanneer het doel al `node` is.
  * **Los van`/exec`**: de `/exec`-richtlijn past exec-standaarden per sessie aan voor geautoriseerde afzenders en vereist geen verhoogde modus.


## Gerelateerd

[**Exec-tool** Uitvoering van shellopdrachten vanuit de agent. ](</nl/tools/exec>) [**Exec-goedkeuringen** Systeem voor goedkeuringen en toegestane lijsten voor `exec`. ](</nl/tools/exec-approvals>) [**Sandboxing** Sandboxconfiguratie op Gateway-niveau. ](</nl/gateway/sandboxing>) [**Sandbox versus toolbeleid versus verhoogd** Hoe de drie poorten samenwerken tijdens een toolaanroep. ](</nl/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo