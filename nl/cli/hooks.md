---
title: Haken
source_url: https://docs.openclaw.ai/nl/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Beheer agenthooks (eventgestuurde automatiseringen voor opdrachten zoals `/new`, `/reset` en het starten van de Gateway).

Het uitvoeren van `openclaw hooks` zonder subopdracht is gelijk aan `openclaw hooks list`.

Gerelateerd:

  * Hooks: [Hooks](</nl/automation/hooks>)
  * Plugin-hooks: [Plugin-hooks](</nl/plugins/hooks>)


## Alle hooks weergeven

bashCopy code
[code]
    openclaw hooks list
[/code]

Geef alle gevonden hooks weer uit workspace-, beheerde, extra en gebundelde mappen. Bij het starten van de Gateway worden interne hookhandlers pas geladen zodra er ten minste één interne hook is geconfigureerd.

**Opties:**

  * `--eligible`: Alleen geschikte hooks tonen (vereisten voldaan)
  * `--json`: Uitvoer als JSON
  * `-v, --verbose`: Gedetailleerde informatie tonen, inclusief ontbrekende vereisten


**Voorbeelduitvoer:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Voorbeeld (uitgebreid):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Toont ontbrekende vereisten voor ongeschikte hooks.

**Voorbeeld (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Geeft gestructureerde JSON terug voor programmatisch gebruik.

## Hookinformatie ophalen

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Toon gedetailleerde informatie over een specifieke hook.

**Argumenten:**

  * `<name>`: Hooknaam of hooksleutel (bijv. `session-memory`)


**Opties:**

  * `--json`: Uitvoer als JSON


**Voorbeeld:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Uitvoer:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Geschiktheid van hooks controleren

bashCopy code
[code]
    openclaw hooks check
[/code]

Toon een samenvatting van de geschiktheidsstatus van hooks (hoeveel er klaar zijn tegenover niet klaar).

**Opties:**

  * `--json`: Uitvoer als JSON


**Voorbeelduitvoer:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Een hook inschakelen

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Schakel een specifieke hook in door deze toe te voegen aan je configuratie (standaard `~/.openclaw/openclaw.json`).

**Opmerking:** Workspace-hooks zijn standaard uitgeschakeld totdat ze hier of in de configuratie worden ingeschakeld. Hooks die door plugins worden beheerd tonen `plugin:<id>` in `openclaw hooks list` en kunnen hier niet worden in- of uitgeschakeld. Schakel in plaats daarvan de plugin in of uit.

**Argumenten:**

  * `<name>`: Hooknaam (bijv. `session-memory`)


**Voorbeeld:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Uitvoer:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Wat dit doet:**

  * Controleert of de hook bestaat en geschikt is
  * Werkt `hooks.internal.entries.<name>.enabled = true` bij in je configuratie
  * Slaat de configuratie op schijf op


Als de hook afkomstig is uit `<workspace>/hooks/`, is deze opt-instap vereist voordat de Gateway deze laadt.

**Na inschakelen:**

  * Start de Gateway opnieuw zodat hooks opnieuw worden geladen (herstart de menubalk-app op macOS, of start je Gateway-proces opnieuw in dev).


## Een hook uitschakelen

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Schakel een specifieke hook uit door je configuratie bij te werken.

**Argumenten:**

  * `<name>`: Hooknaam (bijv. `command-logger`)


**Voorbeeld:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Uitvoer:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Na uitschakelen:**

  * Start de Gateway opnieuw zodat hooks opnieuw worden geladen


## Opmerkingen

  * `openclaw hooks list --json`, `info --json` en `check --json` schrijven gestructureerde JSON rechtstreeks naar stdout.
  * Door plugins beheerde hooks kunnen hier niet worden in- of uitgeschakeld; schakel in plaats daarvan de eigenaar-plugin in of uit.


## Hookpakketten installeren

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Installeer hookpakketten via het uniforme installatieprogramma voor plugins.

`openclaw hooks install` werkt nog steeds als compatibiliteitsalias, maar drukt een verouderingswaarschuwing af en stuurt door naar `openclaw plugins install`.

Npm-specificaties zijn **alleen registry** (pakketnaam + optionele **exacte versie** of **dist-tag**). Git-/URL-/bestandsspecificaties en semver-bereiken worden geweigerd. Dependency- installaties worden projectlokaal uitgevoerd met `--ignore-scripts` voor veiligheid, zelfs wanneer je shell globale npm-installatie-instellingen heeft.

Kale specificaties en `@latest` blijven op het stabiele spoor. Als npm een van deze naar een prerelease herleidt, stopt OpenClaw en vraagt het je expliciet in te stemmen met een prerelease-tag zoals `@beta`/`@rc` of een exacte prereleaseversie.

**Wat dit doet:**

  * Kopieert het hookpakket naar `~/.openclaw/hooks/<id>`
  * Schakelt de geïnstalleerde hooks in `hooks.internal.entries.*` in
  * Registreert de installatie onder `hooks.internal.installs`


**Opties:**

  * `-l, --link`: Link een lokale map in plaats van te kopiëren (voegt deze toe aan `hooks.internal.load.extraDirs`)
  * `--pin`: Registreer npm-installaties als exact herleid `name@version` in `hooks.internal.installs`


**Ondersteunde archieven:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Voorbeelden:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Gelinkte hookpakketten worden behandeld als beheerde hooks uit een door de operator geconfigureerde map, niet als workspace-hooks.

## Hookpakketten bijwerken

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Werk bijgehouden npm-gebaseerde hookpakketten bij via de uniforme updater voor plugins.

`openclaw hooks update` werkt nog steeds als compatibiliteitsalias, maar drukt een verouderingswaarschuwing af en stuurt door naar `openclaw plugins update`.

**Opties:**

  * `--all`: Alle bijgehouden hookpakketten bijwerken
  * `--dry-run`: Tonen wat zou veranderen zonder te schrijven


Wanneer een opgeslagen integriteitshash bestaat en de hash van het opgehaalde artefact verandert, drukt OpenClaw een waarschuwing af en vraagt om bevestiging voordat het doorgaat. Gebruik globaal `--yes` om prompts over te slaan in CI-/niet-interactieve uitvoeringen.

## Gebundelde hooks

### session-memory

Slaat sessiecontext op in geheugen wanneer je `/new` of `/reset` uitvoert.

**Inschakelen:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Uitvoer:** standaard `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. Stel `hooks.internal.entries.session-memory.llmSlug: true` in voor door modellen gegenereerde bestandsnaamslugs.

**Zie:** [session-memory-documentatie](</nl/automation/hooks#session-memory>)

### bootstrap-extra-files

Injecteert aanvullende bootstrap-bestanden (bijvoorbeeld monorepo-lokale `AGENTS.md` / `TOOLS.md`) tijdens `agent:bootstrap`.

**Inschakelen:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Zie:** [bootstrap-extra-files-documentatie](</nl/automation/hooks#bootstrap-extra-files>)

### command-logger

Logt alle opdrachtgebeurtenissen naar een gecentraliseerd auditbestand.

**Inschakelen:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Uitvoer:** `~/.openclaw/logs/commands.log`

**Logs bekijken:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Zie:** [command-logger-documentatie](</nl/automation/hooks#command-logger>)

### boot-md

Voert `BOOT.md` uit wanneer de Gateway start (nadat kanalen zijn gestart).

**Gebeurtenissen** : `gateway:startup`

**Inschakelen** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Zie:** [boot-md-documentatie](</nl/automation/hooks#boot-md>)

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Automatiseringshooks](</nl/automation/hooks>)


Was this useful?YesNo