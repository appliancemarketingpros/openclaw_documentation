---
title: OpenProse
source_url: https://docs.openclaw.ai/nl/prose
scraped_at: 2026-05-25
---

OpenProse is een draagbare, markdown-first workflowindeling voor het orkestreren van AI-sessies. In OpenClaw wordt het geleverd als een Plugin die een OpenProse Skills-pakket plus een `/prose` slashopdracht installeert. Programma's staan in `.prose`-bestanden en kunnen meerdere sub-agents starten met expliciete besturingsstroom.

Officiële site: <https://www.prose.md>

## Wat het kan doen

  * Onderzoek met meerdere agents + synthese met expliciet parallellisme.
  * Herhaalbare workflows met veilige goedkeuringen (codereview, incidenttriage, contentpijplijnen).
  * Herbruikbare `.prose`-programma's die je kunt uitvoeren in ondersteunde agent-runtimes.


## Installeren + inschakelen

Gebundelde Plugins zijn standaard uitgeschakeld. Schakel OpenProse in:

bashCopy code
[code]
    openclaw plugins enable open-prose
[/code]

Herstart de Gateway nadat je de Plugin hebt ingeschakeld.

Dev/lokale checkout: `openclaw plugins install ./path/to/local/open-prose-plugin`

Gerelateerde docs: [Plugins](</nl/tools/plugin>), [Plugin-manifest](</nl/plugins/manifest>), [Skills](</nl/tools/skills>).

## Slashopdracht

OpenProse registreert `/prose` als een door de gebruiker aanroepbare Skills-opdracht. Deze routeert naar de instructies van de OpenProse-VM en gebruikt onder de motorkap OpenClaw-tools.

Veelgebruikte opdrachten:

CodeCopy code
[code]
    /prose help/prose run <file.prose>/prose run <handle/slug>/prose run <https://example.com/file.prose>/prose compile <file.prose>/prose examples/prose update
[/code]

## Voorbeeld: een eenvoudig `.prose`-bestand

proseCopy code
[code]
    # Research + synthesis with two agents running in parallel. input topic: "What should we research?" agent researcher:  model: sonnet  prompt: "You research thoroughly and cite sources." agent writer:  model: opus  prompt: "You write a concise summary." parallel:  findings = session: researcher    prompt: "Research {topic}."  draft = session: writer    prompt: "Summarize {topic}." session "Merge the findings + draft into a final answer."context: { findings, draft }
[/code]

## Bestandslocaties

OpenProse bewaart status onder `.prose/` in je workspace:

CodeCopy code
[code]
    .prose/├── .env├── runs/│   └── {YYYYMMDD}-{HHMMSS}-{random}/│       ├── program.prose│       ├── state.md│       ├── bindings/│       └── agents/└── agents/
[/code]

Persistente agents op gebruikersniveau staan in:

CodeCopy code
[code]
    ~/.prose/agents/
[/code]

## Statusmodi

OpenProse ondersteunt meerdere statusbackends:

  * **filesystem** (standaard): `.prose/runs/...`
  * **in-context** : tijdelijk, voor kleine programma's
  * **sqlite** (experimenteel): vereist de binary `sqlite3`
  * **postgres** (experimenteel): vereist `psql` en een verbindingsreeks


Opmerkingen:

  * sqlite/postgres zijn opt-in en experimenteel.
  * postgres-referenties komen terecht in subagent-logs; gebruik een toegewezen DB met minimale rechten.


## Externe programma's

`/prose run <handle/slug>` wordt omgezet naar `https://p.prose.md/<handle>/<slug>`. Directe URL's worden ongewijzigd opgehaald. Dit gebruikt de tool `web_fetch` (of `exec` voor POST).

## OpenClaw-runtimekoppeling

OpenProse-programma's worden gekoppeld aan OpenClaw-primitieven:

OpenProse-concept | OpenClaw-tool  
---|---  
Sessie starten / Task-tool | `sessions_spawn`  
Bestand lezen/schrijven | `read` / `write`  
Web ophalen | `web_fetch`  
  
Als je tool-allowlist deze tools blokkeert, mislukken OpenProse-programma's. Zie [Skills-configuratie](</nl/tools/skills-config>).

## Beveiliging + goedkeuringen

Behandel `.prose`-bestanden als code. Review ze voordat je ze uitvoert. Gebruik OpenClaw-tool-allowlists en goedkeuringspoorten om neveneffecten te beheersen.

Voor deterministische workflows met goedkeuringspoorten, vergelijk met [Lobster](</nl/tools/lobster>).

## Gerelateerd

  * [Tekst-naar-spraak](</nl/tools/tts>)
  * [Markdown-opmaak](</nl/concepts/markdown-formatting>)


Was this useful?YesNo