---
title: Transcripten-CLI
source_url: https://docs.openclaw.ai/nl/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

Inspecteer transcripties die zijn geschreven door OpenClaw's kern-tool `transcripts`. Deze CLI is alleen-lezen; vastleggen, importeren en samenvatten zijn eigendom van de agenttool en geconfigureerde automatisch startende bronnen.

Gebruik de CLI wanneer je de notities van gisteren wilt vinden, het Markdown-bestand in een editor wilt openen, een transcriptie aan een ander hulpmiddel wilt doorgeven, of wilt debuggen waar een sessie op schijf is beland. De CLI start of stopt het vastleggen niet.

Artefacten staan onder de OpenClaw-statusmap:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

De standaard statusmap is `~/.openclaw`; stel `OPENCLAW_STATE_DIR` in om een andere te gebruiken. De datummap komt van de starttijd van de sessie, en de sessiemap is een veilig bestandssysteemsegment dat is afgeleid van de sessie-id.

## Opdrachten

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: toon opgeslagen sessies, datumgekwalificeerde selector, starttijd, titel en pad naar `summary.md`.
  * `show <session>`: druk de opgeslagen `summary.md` af.
  * `path <session>`: druk het pad naar `summary.md` af.
  * `path <session> --dir`: druk de sessiemap af.
  * `path <session> --metadata`: druk `metadata.json` af.
  * `path <session> --transcript`: druk `transcript.jsonl` af.
  * `--json`: druk machineleesbare uitvoer af.


Wanneer een menselijke sessie-id op meerdere dagen voorkomt, gebruik je de datumgekwalificeerde selector uit `list`, bijvoorbeeld `openclaw transcripts show 2026-05-22/standup`. Standaard sessie-id's bevatten een tijdstempel en willekeurig achtervoegsel; configureer vaste sessie-id's alleen wanneer ze binnen de dag uniek zijn.

## Uitvoer

`list` drukt één sessie per regel af:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

De uitvoer is door tabs gescheiden. De kolommen zijn selector, starttijd, titel en samenvattingspad. De selector is de veiligste waarde om terug te geven aan `show` of `path`.

`list --json` drukt objecten af met:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` retourneert de opgeslagen sessiemetadata, selector, sessiemap, samenvattingspad en Markdown-tekst van de samenvatting. `path --json` retourneert het geselecteerde pad en of dat bestand bestaat.

## Veel vergaderingen per dag

Transcripts groepeert sessies op datum en vervolgens op sessie-id. Tien vergaderingen op één dag worden tien naast elkaar liggende mappen:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

Gebruik standaard gegenereerde id's voor de meeste automatisering. Gebruik een vaste id zoals `standup` alleen wanneer dezelfde id niet twee keer op dezelfde datum wordt gebruikt.

## Ontbrekende samenvattingen

Live sessies schrijven `summary.md` wanneer de sessie stopt. Geïmporteerde transcripties schrijven `summary.md` direct na import. Een sessie kan nog steeds in `list` verschijnen zonder samenvatting wanneer vastleggen actief is, een provider tijdens het stoppen is mislukt, of metadata is geschreven voordat er uitingen binnenkwamen.

Gebruik `path <session> --transcript` om de append-only transcriptie te inspecteren, en gebruik de toolactie `summarize` van `transcripts` om de Markdown-samenvatting opnieuw te genereren.

## Configuratie

Transcriptievastlegging is opt-in omdat live bronnen kunnen deelnemen aan vergaderingen en audio kunnen opnemen. Schakel de tool in met top-level `transcripts.enabled`:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

Configureer automatisch startende bronnen met `transcripts.autoStart` in `openclaw.json`. Elke vermelding wordt ingeschakeld doordat deze aanwezig is; laat een vermelding weg om die bron uit te schakelen.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue