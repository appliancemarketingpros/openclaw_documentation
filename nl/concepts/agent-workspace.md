---
title: Agentwerkruimte
source_url: https://docs.openclaw.ai/nl/concepts/agent-workspace
scraped_at: 2026-05-25
---

De werkruimte is de thuisbasis van de agent. Het is de enige werkdirectory die wordt gebruikt voor bestandstools en voor werkruimtecontext. Houd deze privé en behandel deze als geheugen.

Dit staat los van `~/.openclaw/`, waar configuratie, referenties en sessies worden opgeslagen.

## Standaardlocatie

  * Standaard: `~/.openclaw/workspace`
  * Als `OPENCLAW_PROFILE` is ingesteld en niet `"default"` is, wordt de standaard `~/.openclaw/workspace-<profile>`.
  * Overschrijf in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` of `openclaw setup` maakt de werkruimte aan en vult de bootstrapbestanden aan als ze ontbreken.

Als je de werkruimtebestanden al zelf beheert, kun je het aanmaken van bootstrapbestanden uitschakelen:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Extra werkruimtemappen

Oudere installaties hebben mogelijk `~/openclaw` aangemaakt. Meerdere werkruimtedirectories laten staan kan verwarrende auth- of statusdrift veroorzaken, omdat er maar één werkruimte tegelijk actief is.

## Bestandskaart van de werkruimte

Dit zijn de standaardbestanden die OpenClaw binnen de werkruimte verwacht:

AGENTS.md - operating instructions

Bedieningsinstructies voor de agent en hoe deze geheugen moet gebruiken. Geladen aan het begin van elke sessie. Goede plek voor regels, prioriteiten en details over "hoe je je moet gedragen".

SOUL.md - persona and tone

Persona, toon en grenzen. Wordt elke sessie geladen. Gids: [SOUL.md-persoonlijkheidsgids](</nl/concepts/soul>).

USER.md - who the user is

Wie de gebruiker is en hoe deze moet worden aangesproken. Wordt elke sessie geladen.

IDENTITY.md - name, vibe, emoji

De naam, uitstraling en emoji van de agent. Aangemaakt/bijgewerkt tijdens het bootstrapritueel.

TOOLS.md - local tool conventions

Notities over je lokale tools en conventies. Regelt niet welke tools beschikbaar zijn; het is alleen richtlijn.

HEARTBEAT.md - heartbeat checklist

Optionele kleine checklist voor Heartbeat-runs. Houd deze kort om tokenverbruik te beperken.

BOOT.md - startup checklist

Optionele opstartchecklist die automatisch wordt uitgevoerd bij een Gateway-herstart (wanneer [interne hooks](</nl/automation/hooks>) zijn ingeschakeld). Houd deze kort; gebruik de berichttool voor uitgaande verzendingen.

BOOTSTRAP.md - first-run ritual

Eenmalig ritueel voor de eerste run. Alleen aangemaakt voor een gloednieuwe werkruimte. Verwijder het nadat het ritueel is voltooid.

memory/YYYY-MM-DD.md - daily memory log

Dagelijks geheugenlogboek (één bestand per dag). Aanbevolen om vandaag + gisteren te lezen bij het starten van de sessie.

MEMORY.md - curated long-term memory (optional)

Gecureerd langetermijngeheugen: duurzame feiten, voorkeuren, beslissingen en korte samenvattingen. Bewaar gedetailleerde logs in `memory/YYYY-MM-DD.md`, zodat geheugentools ze op aanvraag kunnen ophalen zonder ze in elke prompt te injecteren. Laad `MEMORY.md` alleen in de hoofd-, privésessie (niet in gedeelde/groepscontexten). Zie [Geheugen](</nl/concepts/memory>) voor de workflow en automatische geheugenflush.

skills/ - workspace skills (optional)

Werkruimtespecifieke Skills. Skill-locatie met de hoogste prioriteit voor die werkruimte. Overschrijft projectagentskills, persoonlijke agentskills, beheerde skills, gebundelde skills en `skills.load.extraDirs` wanneer namen botsen.

canvas/ - Canvas UI files (optional)

Canvas-UI-bestanden voor nodeweergaven (bijvoorbeeld `canvas/index.html`).

## Wat NIET in de werkruimte staat

Deze staan onder `~/.openclaw/` en mogen NIET worden gecommit naar de werkruimterepo:

  * `~/.openclaw/openclaw.json` (configuratie)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (modelauthprofielen: OAuth + API-sleutels)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (Codex-runtimeaccount, configuratie, skills, plugins en native threadstatus per agent)
  * `~/.openclaw/credentials/` (kanaal-/providerstatus plus verouderde OAuth-importgegevens)
  * `~/.openclaw/agents/<agentId>/sessions/` (sessietranscripten + metadata)
  * `~/.openclaw/skills/` (beheerde skills)


Als je sessies of configuratie moet migreren, kopieer ze dan afzonderlijk en houd ze buiten versiebeheer.

## Git-back-up (aanbevolen, privé)

Behandel de werkruimte als privégeheugen. Zet deze in een **privé** git-repo zodat er een back-up is en herstel mogelijk is.

Voer deze stappen uit op de machine waarop de Gateway draait (daar bevindt de werkruimte zich).

* ### Initialize the repo

Als git is geïnstalleerd, worden gloednieuwe werkruimten automatisch geïnitialiseerd. Als deze werkruimte nog geen repo is, voer dan uit:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Add a private remote

### GitHub web UI

  1. Maak een nieuwe **privé** repository aan op GitHub.
  2. Initialiseer niet met een README (voorkomt mergeconflicten).
  3. Kopieer de HTTPS-remote-URL.
  4. Voeg de remote toe en push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. Maak een nieuwe **privé** repository aan op GitLab.
  2. Initialiseer niet met een README (voorkomt mergeconflicten).
  3. Kopieer de HTTPS-remote-URL.
  4. Voeg de remote toe en push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Ongoing updates

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Commit geen geheimen

Voorgestelde `.gitignore`-starter:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## De werkruimte naar een nieuwe machine verplaatsen

* ### Clone the repo

Clone de repo naar het gewenste pad (standaard `~/.openclaw/workspace`).

* ### Update config

Stel `agents.defaults.workspace` in op dat pad in `~/.openclaw/openclaw.json`.

* ### Seed missing files

Voer `openclaw setup --workspace <path>` uit om ontbrekende bestanden te seeden.

* ### Copy sessions (optional)

Als je sessies nodig hebt, kopieer dan `~/.openclaw/agents/<agentId>/sessions/` afzonderlijk vanaf de oude machine.

## Geavanceerde opmerkingen

  * Multi-agentrouting kan verschillende werkruimten per agent gebruiken. Zie [Kanaalrouting](</nl/channels/channel-routing>) voor routingconfiguratie.
  * Als `agents.defaults.sandbox` is ingeschakeld, kunnen niet-hoofdsessies sandboxwerkruimten per sessie gebruiken onder `agents.defaults.sandbox.workspaceRoot`.


## Gerelateerd

  * [Heartbeat](</nl/gateway/heartbeat>) \- HEARTBEAT.md-werkruimtebestand
  * [Sandboxing](</nl/gateway/sandboxing>) \- werkruimtetoegang in sandboxomgevingen
  * [Sessie](</nl/concepts/session>) \- opslagpaden voor sessies
  * [Vaste instructies](</nl/automation/standing-orders>) \- persistente instructies in werkruimtebestanden


Was this useful?YesNo