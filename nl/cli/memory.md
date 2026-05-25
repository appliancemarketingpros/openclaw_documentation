---
title: Geheugen
source_url: https://docs.openclaw.ai/nl/cli/memory
scraped_at: 2026-05-25
---

# `openclaw memory`

Beheer semantische geheugenindexering en zoeken. Geleverd door de actieve geheugen-Plugin (standaard: `memory-core`; stel `plugins.slots.memory = "none"` in om uit te schakelen).

Gerelateerd:

  * Geheugenconcept: [Geheugen](</nl/concepts/memory>)
  * Geheugenwiki: [Geheugenwiki](</nl/plugins/memory-wiki>)
  * Wiki-CLI: [wiki](</nl/cli/wiki>)
  * Plugins: [Plugins](</nl/tools/plugin>)


## Voorbeelden

bashCopy code
[code]
    openclaw memory statusopenclaw memory status --deepopenclaw memory status --fixopenclaw memory index --forceopenclaw memory search "meeting notes"openclaw memory search --query "deployment" --max-results 20openclaw memory promote --limit 10 --min-score 0.75openclaw memory promote --applyopenclaw memory promote --json --min-recall-count 0 --min-unique-queries 0openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --jsonopenclaw memory rem-harnessopenclaw memory rem-harness --jsonopenclaw memory status --jsonopenclaw memory status --deep --indexopenclaw memory status --deep --index --verboseopenclaw memory status --agent mainopenclaw memory index --agent main --verbose
[/code]

## Opties

`memory status` en `memory index`:

  * `--agent <id>`: beperk tot één agent. Zonder deze optie worden deze opdrachten uitgevoerd voor elke geconfigureerde agent; als er geen agentlijst is geconfigureerd, vallen ze terug op de standaardagent.
  * `--verbose`: geef gedetailleerde logboeken weer tijdens probes en indexering.


`memory status`:

  * `--deep`: probe lokale gereedheid van de vector-store, gereedheid van de embedding-provider en gereedheid van semantisch zoeken met vectoren. Gewoon `memory status` blijft snel en voert geen live embedding- of provider-detectiewerk uit; een onbekende vector-store- of semantische-vectorstatus betekent dat deze in die opdracht niet is geprobed. QMD lexical `searchMode: "search"` slaat semantische vectorprobes en embedding-onderhoud over, zelfs met `--deep`.
  * `--index`: voer een herindexering uit als de store dirty is (impliceert `--deep`).
  * `--fix`: herstel verouderde recall-locks en normaliseer promotiemetadata.
  * `--json`: druk JSON-uitvoer af.


Als `memory status` `Dreaming status: blocked` toont, is de beheerde dreaming-Cron ingeschakeld, maar de Heartbeat die deze aanstuurt wordt niet uitgevoerd voor de standaardagent. Zie [Dreaming wordt nooit uitgevoerd](</nl/concepts/dreaming#dreaming-never-runs-status-shows-blocked>) voor de twee veelvoorkomende oorzaken.

`memory index`:

  * `--force`: forceer een volledige herindexering.


`memory search`:

  * Query-invoer: geef ofwel positioneel `[query]` door of `--query <text>`.
  * Als beide zijn opgegeven, wint `--query`.
  * Als geen van beide is opgegeven, sluit de opdracht af met een fout.
  * `--agent <id>`: beperk tot één agent (standaard: de standaardagent).
  * `--max-results <n>`: beperk het aantal geretourneerde resultaten.
  * `--min-score <n>`: filter matches met een lage score weg.
  * `--json`: druk JSON-resultaten af.


`memory promote`:

Bekijk korte-termijngeheugenpromoties vooraf en pas ze toe.

bashCopy code
[code]
    openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
[/code]

  * `--apply` \-- schrijf promoties naar `MEMORY.md` (standaard: alleen preview).
  * `--limit <n>` \-- beperk het aantal getoonde kandidaten.
  * `--include-promoted` \-- neem vermeldingen op die al in eerdere cycli zijn gepromoveerd.


Volledige opties:

  * Rangschikt korte-termijnkandidaten uit `memory/YYYY-MM-DD.md` met gewogen promotiesignalen (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
  * Gebruikt korte-termijnsignalen van zowel geheugenrecalls als dagelijkse ingestierondes, plus light/REM-faseversterkingssignalen.
  * Wanneer Dreaming is ingeschakeld, beheert `memory-core` automatisch één Cron-taak die op de achtergrond een volledige sweep uitvoert (`light -> REM -> deep`) (geen handmatige `openclaw cron add` vereist).
  * `--agent <id>`: beperk tot één agent (standaard: de standaardagent).
  * `--limit <n>`: maximaal aantal kandidaten om te retourneren/toe te passen.
  * `--min-score <n>`: minimale gewogen promotiescore.
  * `--min-recall-count <n>`: minimaal aantal recalls dat vereist is voor een kandidaat.
  * `--min-unique-queries <n>`: minimaal aantal afzonderlijke queries dat vereist is voor een kandidaat.
  * `--apply`: voeg geselecteerde kandidaten toe aan `MEMORY.md` en markeer ze als gepromoveerd.
  * `--include-promoted`: neem al gepromoveerde kandidaten op in de uitvoer.
  * `--json`: druk JSON-uitvoer af.


`memory promote-explain`:

Leg een specifieke promotiekandidaat en de score-uitsplitsing uit.

bashCopy code
[code]
    openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
[/code]

  * `<selector>`: kandidaatsleutel, padfragment of snippetfragment om op te zoeken.
  * `--agent <id>`: beperk tot één agent (standaard: de standaardagent).
  * `--include-promoted`: neem al gepromoveerde kandidaten op.
  * `--json`: druk JSON-uitvoer af.


`memory rem-harness`:

Bekijk REM-reflecties, kandidaatwaarheden en diepe promotie-uitvoer vooraf zonder iets te schrijven.

bashCopy code
[code]
    openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
[/code]

  * `--agent <id>`: beperk tot één agent (standaard: de standaardagent).
  * `--include-promoted`: neem al gepromoveerde diepe kandidaten op.
  * `--json`: druk JSON-uitvoer af.


## Dreaming

Dreaming is het achtergrondgeheugenconsolidatiesysteem met drie samenwerkende fasen: **light** (korte-termijnmateriaal sorteren/stagen), **deep** (duurzame feiten naar `MEMORY.md` promoveren) en **REM** (reflecteren en thema's naar voren brengen).

  * Schakel in met `plugins.entries.memory-core.config.dreaming.enabled: true`.
  * Schakel vanuit chat met `/dreaming on|off` (of inspecteer met `/dreaming status`).
  * Dreaming draait volgens één beheerd sweepschema (`dreaming.frequency`) en voert fasen in volgorde uit: light, REM, deep.
  * Alleen de deep-fase schrijft duurzaam geheugen naar `MEMORY.md`.
  * Menselijk leesbare fase-uitvoer en dagboekvermeldingen worden geschreven naar `DREAMS.md` (of bestaande `dreams.md`), met optionele rapporten per fase in `memory/dreaming/<phase>/YYYY-MM-DD.md`.
  * Rangschikking gebruikt gewogen signalen: recall-frequentie, retrieval-relevantie, querydiversiteit, temporele recentheid, consolidatie over dagen heen en afgeleide conceptrijkdom.
  * Promotie leest de live dagelijkse notitie opnieuw voordat naar `MEMORY.md` wordt geschreven, zodat bewerkte of verwijderde korte-termijnsnippets niet worden gepromoveerd vanuit verouderde recall-store-snapshots.
  * Geplande en handmatige `memory promote`-runs delen dezelfde standaardwaarden voor de deep-fase, tenzij je CLI-drempeloverschrijvingen doorgeeft.
  * Automatische runs waaieren uit over geconfigureerde geheugenwerkruimten.


Standaardplanning:

  * **Sweep-cadans** : `dreaming.frequency = 0 3 * * *`
  * **Deep-drempels** : `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`


Voorbeeld:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

Notities:

  * `memory index --verbose` drukt details per fase af (provider, model, bronnen, batchactiviteit).
  * `memory status` bevat alle extra paden die via `memorySearch.extraPaths` zijn geconfigureerd.
  * Als effectief actieve remote-API-sleutelvelden voor geheugen zijn geconfigureerd als SecretRefs, lost de opdracht die waarden op vanuit de actieve Gateway-snapshot. Als de Gateway niet beschikbaar is, faalt de opdracht snel.
  * Opmerking over Gateway-versieverschil: dit opdrachtpad vereist een Gateway die `secrets.resolve` ondersteunt; oudere gateways geven een fout voor een onbekende methode terug.
  * Stem de geplande sweep-cadans af met `dreaming.frequency`. Het beleid voor deep-promotie is verder intern; gebruik CLI-vlaggen op `memory promote` wanneer je eenmalige handmatige overschrijvingen nodig hebt.
  * `memory rem-harness --path <file-or-dir> --grounded` toont vooraf onderbouwde `Wat is er gebeurd`, `Reflecties` en `Mogelijke blijvende updates` uit historische dagelijkse notities zonder iets te schrijven.
  * `memory rem-backfill --path <file-or-dir>` schrijft omkeerbare, onderbouwde dagboekvermeldingen naar `DREAMS.md` voor UI-beoordeling.
  * `memory rem-backfill --path <file-or-dir> --stage-short-term` seedt ook onderbouwde duurzame kandidaten in de live korte-termijnpromotiestore, zodat de normale deep-fase ze kan rangschikken.
  * `memory rem-backfill --rollback` verwijdert eerder geschreven onderbouwde dagboekvermeldingen, en `memory rem-backfill --rollback-short-term` verwijdert eerder gestagede onderbouwde korte-termijnkandidaten.
  * Zie [Dreaming](</nl/concepts/dreaming>) voor volledige fasebeschrijvingen en configuratiereferentie.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Geheugenoverzicht](</nl/concepts/memory>)


Was this useful?YesNo