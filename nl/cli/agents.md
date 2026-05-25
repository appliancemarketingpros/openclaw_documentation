---
title: Agenten
source_url: https://docs.openclaw.ai/nl/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

Beheer geïsoleerde agents (werkruimten + auth + routering).

Gerelateerd:

  * [Multi-agentroutering](</nl/concepts/multi-agent>)
  * [Agentwerkruimte](</nl/concepts/agent-workspace>)
  * [Skills-configuratie](</nl/tools/skills-config>): configuratie voor zichtbaarheid van Skills.


## Voorbeelden

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Routeringsbindings

Gebruik routeringsbindings om inkomend kanaalverkeer aan een specifieke agent vast te pinnen.

Als je ook verschillende zichtbare Skills per agent wilt, configureer dan `agents.defaults.skills` en `agents.list[].skills` in `openclaw.json`. Zie [Skills-configuratie](</nl/tools/skills-config>) en [Configuratiereferentie](</nl/gateway/config-agents#agents-defaults-skills>).

Bindings weergeven:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

Bindings toevoegen:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

Als je `accountId` weglaat (`--bind <channel>`), lost OpenClaw dit op vanuit kanaalstandaardwaarden en Plugin-installatiehooks wanneer die beschikbaar zijn.

Als je `--agent` weglaat voor `bind` of `unbind`, richt OpenClaw zich op de huidige standaardagent.

### Gedrag van bindingsbereik

  * Een binding zonder `accountId` komt alleen overeen met het standaardaccount van het kanaal.
  * `accountId: "*"` is de kanaalbrede fallback (alle accounts) en is minder specifiek dan een expliciete accountbinding.
  * Als dezelfde agent al een overeenkomende kanaalbinding zonder `accountId` heeft, en je later bindt met een expliciete of opgeloste `accountId`, werkt OpenClaw die bestaande binding ter plekke bij in plaats van een duplicaat toe te voegen.


Voorbeeld:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

Na de upgrade is routering voor die binding beperkt tot `telegram:ops`. Als je ook routering voor het standaardaccount wilt, voeg die dan expliciet toe (bijvoorbeeld `--bind telegram:default`).

Bindings verwijderen:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` accepteert ofwel `--all` of een of meer `--bind`-waarden, niet beide.

## Commandosurface

### `agents`

Het uitvoeren van `openclaw agents` zonder subcommando is gelijk aan `openclaw agents list`.

### `agents list`

Opties:

  * `--json`
  * `--bindings`: volledige routeringsregels opnemen, niet alleen aantallen/samenvattingen per agent


### `agents add [name]`

Opties:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (herhaalbaar)
  * `--non-interactive`
  * `--json`


Opmerkingen:

  * Het doorgeven van expliciete add-flags schakelt de opdracht over naar het niet-interactieve pad.
  * Niet-interactieve modus vereist zowel een agentnaam als `--workspace`.
  * `main` is gereserveerd en kan niet worden gebruikt als de nieuwe agent-id.
  * In interactieve modus kopieert auth-seeding alleen draagbare statische profielen (`api_key` en standaard statische `token`). OAuth-profielen met vernieuwingstokens blijven alleen beschikbaar via read-through-overerving vanuit de echte `main`-agentstore. Als de geconfigureerde standaardagent niet `main` is, meld je dan apart aan voor OAuth- profielen op de nieuwe agent.


### `agents bindings`

Opties:

  * `--agent <id>`
  * `--json`


### `agents bind`

Opties:

  * `--agent <id>` (standaard de huidige standaardagent)
  * `--bind <channel[:accountId]>` (herhaalbaar)
  * `--json`


### `agents unbind`

Opties:

  * `--agent <id>` (standaard de huidige standaardagent)
  * `--bind <channel[:accountId]>` (herhaalbaar)
  * `--all`
  * `--json`


### `agents delete <id>`

Opties:

  * `--force`
  * `--json`


Opmerkingen:

  * `main` kan niet worden verwijderd.
  * Zonder `--force` is interactieve bevestiging vereist.
  * Werkruimte-, agentstatus- en sessietranscriptmappen worden naar de prullenmand verplaatst, niet hard verwijderd.
  * Wanneer de Gateway bereikbaar is, wordt verwijdering via de Gateway verzonden, zodat config- en session-store-opschoning dezelfde writer gebruiken als runtimeverkeer. Als de Gateway niet bereikbaar is, valt de CLI terug op het offline lokale pad.
  * Als de werkruimte van een andere agent hetzelfde pad is, binnen deze werkruimte ligt, of deze werkruimte bevat, blijft de werkruimte behouden en rapporteert `--json` `workspaceRetained`, `workspaceRetainedReason` en `workspaceSharedWith`.


## Identiteitsbestanden

Elke agentwerkruimte kan een `IDENTITY.md` bevatten in de root van de werkruimte:

  * Voorbeeldpad: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` leest vanuit de root van de werkruimte (of een expliciet `--identity-file`)


Avatarpaden worden relatief aan de root van de werkruimte opgelost.

## Identiteit instellen

`set-identity` schrijft velden naar `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (werkruimte-relatief pad, http(s)-URL of data-URI)


Opties:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


Opmerkingen:

  * `--agent` of `--workspace` kan worden gebruikt om de doelagent te selecteren.
  * Als je vertrouwt op `--workspace` en meerdere agents die werkruimte delen, mislukt de opdracht en wordt je gevraagd `--agent` door te geven.
  * Wanneer er geen expliciete identiteitsvelden worden opgegeven, leest de opdracht identiteitsgegevens uit `IDENTITY.md`.


Laden vanuit `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

Velden expliciet overschrijven:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Config-voorbeeld:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Multi-agentroutering](</nl/concepts/multi-agent>)
  * [Agentwerkruimte](</nl/concepts/agent-workspace>)


Was this useful?YesNo