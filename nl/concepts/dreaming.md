---
title: Dreaming
source_url: https://docs.openclaw.ai/nl/concepts/dreaming
scraped_at: 2026-05-25
---

Dreaming is het achtergrondgeheugenconsolidatiesysteem in `memory-core`. Het helpt OpenClaw sterke kortetermijnsignalen naar duurzaam geheugen te verplaatsen, terwijl het proces uitlegbaar en controleerbaar blijft.

## Wat Dreaming schrijft

Dreaming bewaart twee soorten uitvoer:

  * **Machinestatus** in `memory/.dreams/` (recall-opslag, fasesignalen, opnamecheckpoints, locks).
  * **Menselijk leesbare uitvoer** in `DREAMS.md` (of bestaande `dreams.md`) en optionele faserapportbestanden onder `memory/dreaming/<phase>/YYYY-MM-DD.md`.


Langetermijnpromotie schrijft nog steeds alleen naar `MEMORY.md`.

## Fasemodel

Dreaming gebruikt drie samenwerkende fases:

Fase | Doel | Duurzame schrijfactie  
---|---|---  
Licht | Recent kortetermijnmateriaal sorteren en klaarzetten | Nee  
Diep | Duurzame kandidaten scoren en promoveren | Ja (`MEMORY.md`)  
REM | Reflecteren op thema's en terugkerende ideeën | Nee  
  
Deze fases zijn interne implementatiedetails, geen afzonderlijke door gebruikers geconfigureerde "modi."

Lichte fase

De lichte fase neemt recente dagelijkse geheugensignalen en recall-sporen op, ontdubbelt ze en zet kandidaatregels klaar.

  * Leest uit kortetermijn-recallstatus, recente dagelijkse geheugenbestanden en geredigeerde sessietranscripten wanneer beschikbaar.
  * Schrijft een beheerd `## Light Sleep`-blok wanneer opslag inline-uitvoer bevat.
  * Registreert versterkingssignalen voor latere diepe ranking.
  * Schrijft nooit naar `MEMORY.md`.

Diepe fase

De diepe fase bepaalt wat langetermijngeheugen wordt.

  * Rangschikt kandidaten met gewogen scoring en drempelpoorten.
  * Vereist dat `minScore`, `minRecallCount` en `minUniqueQueries` slagen.
  * Hydrateert fragmenten opnieuw uit live dagelijkse bestanden voordat er wordt geschreven, zodat verouderde/verwijderde fragmenten worden overgeslagen.
  * Voegt gepromoveerde vermeldingen toe aan `MEMORY.md`.
  * Schrijft een `## Deep Sleep`-samenvatting naar `DREAMS.md` en schrijft optioneel `memory/dreaming/deep/YYYY-MM-DD.md`.

REM-fase

De REM-fase extraheert patronen en reflectieve signalen.

  * Bouwt thema- en reflectiesamenvattingen uit recente kortetermijnsporen.
  * Schrijft een beheerd `## REM Sleep`-blok wanneer opslag inline-uitvoer bevat.
  * Registreert REM-versterkingssignalen die door diepe ranking worden gebruikt.
  * Schrijft nooit naar `MEMORY.md`.


## Opname van sessietranscripten

Dreaming kan geredigeerde sessietranscripten opnemen in de Dreaming-corpus. Wanneer transcripten beschikbaar zijn, worden ze samen met dagelijkse geheugensignalen en recall-sporen aan de lichte fase doorgegeven. Persoonlijke en gevoelige inhoud wordt vóór opname geredigeerd.

## Droomdagboek

Dreaming houdt ook een verhalend **Droomdagboek** bij in `DREAMS.md`. Nadat elke fase genoeg materiaal heeft, voert `memory-core` een best-effort subagentbeurt op de achtergrond uit en voegt het een korte dagboekvermelding toe. Het gebruikt het standaard runtimemodel, tenzij `dreaming.model` is geconfigureerd. Als het geconfigureerde model niet beschikbaar is, probeert Droomdagboek het één keer opnieuw met het standaardsessiemodel.

Er is ook een onderbouwde historische backfill-lane voor beoordelings- en herstelwerk:

Backfill-opdrachten

  * `memory rem-harness --path ... --grounded` toont een voorbeeld van onderbouwde dagboekuitvoer uit historische `YYYY-MM-DD.md`-notities.
  * `memory rem-backfill --path ...` schrijft omkeerbare onderbouwde dagboekvermeldingen naar `DREAMS.md`.
  * `memory rem-backfill --path ... --stage-short-term` zet onderbouwde duurzame kandidaten klaar in dezelfde kortetermijnbewijzopslag die de normale diepe fase al gebruikt.
  * `memory rem-backfill --rollback` en `--rollback-short-term` verwijderen die klaargezette backfill-artefacten zonder gewone dagboekvermeldingen of live kortetermijn-recall aan te raken.


De Control-UI biedt dezelfde dagboek-backfill-/resetstroom, zodat je resultaten in de Dromen-scène kunt inspecteren voordat je beslist of de onderbouwde kandidaten promotie verdienen. De scène toont ook een afzonderlijke onderbouwde lane, zodat je kunt zien welke klaargezette kortetermijnvermeldingen uit historische herhaling kwamen, welke gepromoveerde items door onderbouwing werden geleid, en alleen onderbouwde klaargezette vermeldingen kunt wissen zonder de gewone live kortetermijnstatus aan te raken.

## Signalen voor diepe ranking

Diepe ranking gebruikt zes gewogen basissignalen plus faseversterking:

Signaal | Gewicht | Beschrijving  
---|---|---  
Frequentie | 0.24 | Hoeveel kortetermijnsignalen de vermelding heeft verzameld  
Relevantie | 0.30 | Gemiddelde ophaalkwaliteit voor de vermelding  
Querydiversiteit | 0.15 | Afzonderlijke query-/dagcontexten waarin deze naar voren kwam  
Recentheid | 0.15 | Tijdvervallen versheidsscore  
Consolidatie | 0.10 | Sterkte van herhaling over meerdere dagen  
Conceptuele rijkdom | 0.06 | Dichtheid van concepttags uit fragment/pad  
  
Treffers in de lichte en REM-fase voegen een kleine recentheidsvervallen boost toe uit `memory/.dreams/phase-signals.json`.

## Planning

Wanneer ingeschakeld, beheert `memory-core` automatisch één cronjob voor een volledige Dreaming-sweep. Elke sweep voert fases op volgorde uit: licht → REM → diep.

De sweep omvat de primaire runtimewerkruimte en alle geconfigureerde agentwerkruimtes, ontdubbeld op pad, zodat subagentwerkruimte-fan-out de `DREAMS.md` en geheugenstatus van de hoofdagent niet uitsluit.

Standaard cadansgedrag:

Instelling | Standaard  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | standaardmodel  
  
## Snel aan de slag

### Dreaming inschakelen

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Aangepaste sweep-cadans

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Slash-opdracht

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## CLI-workflow

### Promotievoorbeeld / toepassen

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

Handmatige `memory promote` gebruikt standaard drempels van de diepe fase, tenzij overschreven met CLI-vlaggen.

### Promotie uitleggen

Leg uit waarom een specifieke kandidaat wel of niet zou worden gepromoveerd:

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### Voorbeeld met REM-harness

Bekijk een voorbeeld van REM-reflecties, kandidaatwaarheden en diepe promotie-uitvoer zonder iets te schrijven:

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Belangrijke standaardwaarden

Alle instellingen staan onder `plugins.entries.memory-core.config.dreaming`.

Schakel de Dreaming-sweep in of uit.

Cron-cadans voor de volledige Dreaming-sweep.

Optionele modeloverschrijving voor de Droomdagboek-subagent. Gebruik een canonieke `provider/model`-waarde wanneer je ook een subagent-allowlist `allowedModels` instelt.

## Dromen-UI

Wanneer ingeschakeld, toont het Gateway-tabblad **Dromen** :

  * huidige ingeschakelde status van Dreaming
  * status op faseniveau en aanwezigheid van beheerde sweep
  * aantallen kortetermijn-, onderbouwde, signaal- en vandaag gepromoveerde items
  * timing van de volgende geplande uitvoering
  * een afzonderlijke onderbouwde scène-lane voor klaargezette historische replay-vermeldingen
  * een uitvouwbare Droomdagboek-lezer ondersteund door `doctor.memory.dreamDiary`


## Dreaming start nooit: status toont geblokkeerd

Als `openclaw memory status` `Dreaming status: blocked` rapporteert, bestaat de beheerde cron, maar vuurt de standaardagent-Heartbeat niet. Controleer of Heartbeat is ingeschakeld voor de standaardagent en of het doel niet `none` is, en voer daarna na het volgende Heartbeat-interval opnieuw `openclaw memory status --deep` uit.

## Gerelateerd

  * [Geheugen](</nl/concepts/memory>)
  * [Geheugen-CLI](</nl/cli/memory>)
  * [Referentie voor geheugenconfiguratie](</nl/reference/memory-config>)
  * [Geheugen zoeken](</nl/concepts/memory-search>)


Was this useful?YesNo