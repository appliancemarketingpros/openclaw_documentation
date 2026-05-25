---
title: Migreren van Claude
source_url: https://docs.openclaw.ai/nl/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw importeert lokale Claude-status via de gebundelde Claude-migratieprovider. De provider toont elk item vooraf voordat de status wordt gewijzigd, redigeert geheimen in plannen en rapporten, en maakt een geverifieerde back-up vóór het toepassen.

## Twee manieren om te importeren

### Onboardingwizard

De wizard biedt Claude aan wanneer lokale Claude-status wordt gedetecteerd.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Of verwijs naar een specifieke bron:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Gebruik `openclaw migrate` voor gescripte of herhaalbare runs. Zie [`openclaw migrate`](</nl/cli/migrate>) voor de volledige referentie.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Voeg `--from <path>` toe om een specifieke Claude Code-home of projectroot te importeren.

## Wat wordt geïmporteerd

Instructies en geheugen

  * Projectinhoud van `CLAUDE.md` en `.claude/CLAUDE.md` wordt gekopieerd of toegevoegd aan de OpenClaw-agentwerkruimte `AGENTS.md`.
  * Gebruikersinhoud van `~/.claude/CLAUDE.md` wordt toegevoegd aan werkruimte `USER.md`.

MCP-servers

MCP-serverdefinities worden geïmporteerd uit project `.mcp.json`, Claude Code `~/.claude.json` en Claude Desktop `claude_desktop_config.json` wanneer aanwezig.

Skills en commando's

  * Claude Skills met een `SKILL.md`-bestand worden gekopieerd naar de OpenClaw-werkruimte-Skills-directory.
  * Claude Markdown-commandobestanden onder `.claude/commands/` of `~/.claude/commands/` worden omgezet naar OpenClaw Skills met `disable-model-invocation: true`.


## Wat alleen archief blijft

De provider kopieert deze naar het migratierapport voor handmatige beoordeling, maar laadt ze **niet** in live OpenClaw-configuratie:

  * Claude-hooks
  * Claude-machtigingen en brede allowlists voor tools
  * Claude-omgevingsstandaarden
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Claude-subagents onder `.claude/agents/` of `~/.claude/agents/`
  * Claude Code-caches, plannen en projectgeschiedenisdirectory's
  * Claude Desktop-extensies en door het besturingssysteem opgeslagen referenties


OpenClaw weigert hooks uit te voeren, allowlists met machtigingen te vertrouwen, of ondoorzichtige OAuth- en Desktop-referentiestatus automatisch te decoderen. Verplaats wat je nodig hebt handmatig nadat je het archief hebt beoordeeld.

## Bronselectie

Zonder `--from` inspecteert OpenClaw de standaard Claude Code-home op `~/.claude`, het bemonsterde Claude Code-statusbestand `~/.claude.json` en de Claude Desktop MCP-configuratie op macOS.

Wanneer `--from` naar een projectroot verwijst, importeert OpenClaw alleen de Claude-bestanden van dat project, zoals `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` en `.mcp.json`. Het leest je globale Claude-home niet tijdens een projectrootimport.

## Aanbevolen flow

* ### Bekijk het plan vooraf

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Het plan vermeldt alles wat zal veranderen, inclusief conflicten, overgeslagen items en gevoelige waarden die zijn geredigeerd uit geneste MCP-velden `env` of `headers`.

* ### Toepassen met back-up

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw maakt en verifieert een back-up voordat wijzigingen worden toegepast.

* ### Voer doctor uit

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</nl/gateway/doctor>) controleert na de import op configuratie- of statusproblemen.

* ### Herstart en verifieer

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Bevestig dat de Gateway gezond is en dat je geïmporteerde instructies, MCP-servers en Skills zijn geladen.

## Conflictafhandeling

Toepassen weigert door te gaan wanneer het plan conflicten meldt (een bestand of configuratiewaarde bestaat al op het doel).

Voor een nieuwe OpenClaw-installatie zijn conflicten ongebruikelijk. Ze verschijnen meestal wanneer je de import opnieuw uitvoert op een installatie die al gebruikersbewerkingen bevat.

## JSON-uitvoer voor automatisering

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Met `--json` en zonder `--yes` drukt apply het plan af en wijzigt het geen status. Dit is de veiligste modus voor CI en gedeelde scripts.

## Problemen oplossen

Claude-status staat buiten ~/.claude

Geef `--from /actual/path` (CLI) of `--import-source /actual/path` (onboarding) door.

Onboarding weigert te importeren op een bestaande installatie

Onboarding-imports vereisen een nieuwe installatie. Reset de status en doorloop onboarding opnieuw, of gebruik `openclaw migrate apply claude` rechtstreeks, dat `--overwrite` en expliciete back-upcontrole ondersteunt.

MCP-servers uit Claude Desktop zijn niet geïmporteerd

Claude Desktop leest `claude_desktop_config.json` uit een platformspecifiek pad. Verwijs `--from` naar de directory van dat bestand als OpenClaw het niet automatisch heeft gedetecteerd.

Claude-commando's werden Skills met modelaanroep uitgeschakeld

Dit is zo ontworpen. Claude-commando's worden door de gebruiker geactiveerd, dus OpenClaw importeert ze als Skills met `disable-model-invocation: true`. Bewerk de frontmatter van elke Skill als je wilt dat de agent ze automatisch aanroept.

## Gerelateerd

  * [`openclaw migrate`](</nl/cli/migrate>): volledige CLI-referentie, Plugin-contract en JSON-vormen.
  * [Migratiehandleiding](</nl/install/migrating>): alle migratiepaden.
  * [Migreren vanaf Hermes](</nl/install/migrating-hermes>): het andere importsysteem tussen systemen.
  * [Onboarding](</nl/cli/onboard>): wizardflow en niet-interactieve flags.
  * [Doctor](</nl/gateway/doctor>): gezondheidscontrole na migratie.
  * [Agentwerkruimte](</nl/concepts/agent-workspace>): waar `AGENTS.md`, `USER.md` en Skills staan.


Was this useful?YesNo