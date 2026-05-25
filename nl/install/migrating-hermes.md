---
title: Migreren vanuit Hermes
source_url: https://docs.openclaw.ai/nl/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importeert Hermes-status via een gebundelde migratieprovider. De provider toont een voorbeeld van alles voordat de status wordt gewijzigd, redigeert geheimen in plannen en rapporten, en maakt een geverifieerde back-up voordat wijzigingen worden toegepast.

## Twee manieren om te importeren

### Onboardingwizard

De snelste route. De wizard detecteert Hermes op `~/.hermes` en toont een voorbeeld voordat wijzigingen worden toegepast.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Of wijs naar een specifieke bron:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Gebruik `openclaw migrate` voor gescripte of herhaalbare runs. Zie [`openclaw migrate`](</nl/cli/migrate>) voor de volledige referentie.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Voeg `--from <path>` toe wanneer Hermes buiten `~/.hermes` staat.

## Wat wordt geïmporteerd

Modelconfiguratie

  * Standaardmodelselectie uit Hermes `config.yaml`.
  * Geconfigureerde modelproviders en aangepaste OpenAI-compatibele eindpunten uit `providers` en `custom_providers`.

MCP-servers

MCP-serverdefinities uit `mcp_servers` of `mcp.servers`.

Werkruimtebestanden

  * `SOUL.md` en `AGENTS.md` worden naar de OpenClaw-agentwerkruimte gekopieerd.
  * `memories/MEMORY.md` en `memories/USER.md` worden **toegevoegd** aan de overeenkomende OpenClaw-geheugenbestanden in plaats van ze te overschrijven.

Geheugenconfiguratie

Standaardwaarden voor geheugenconfiguratie voor OpenClaw-bestandsgeheugen. Externe geheugenproviders zoals Honcho worden vastgelegd als archief- of handmatige-reviewitems, zodat je ze bewust kunt verplaatsen.

Skills

Skills met een `SKILL.md`-bestand onder `skills/<name>/` worden gekopieerd, samen met configuratiewaarden per Skill uit `skills.config`.

API-sleutels (opt-in)

Stel `--include-secrets` in om ondersteunde `.env`-sleutels te importeren: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Zonder de vlag worden geheimen nooit gekopieerd.

## Wat alleen archief blijft

De provider kopieert deze naar de migratierapportmap voor handmatige review, maar laadt ze **niet** in live OpenClaw-configuratie of referenties:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw weigert deze status automatisch uit te voeren of te vertrouwen, omdat de indelingen en vertrouwensaannames tussen systemen kunnen verschillen. Verplaats wat je nodig hebt handmatig nadat je het archief hebt bekeken.

## Aanbevolen workflow

* ### Bekijk het plan

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Het plan vermeldt alles wat wordt gewijzigd, inclusief conflicten, overgeslagen items en eventuele gevoelige items. Planuitvoer redigeert geneste sleutels die op geheimen lijken.

* ### Toepassen met back-up

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw maakt en verifieert een back-up voordat wijzigingen worden toegepast. Als je API-sleutels moet importeren, voeg dan `--include-secrets` toe.

* ### Voer doctor uit

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</nl/gateway/doctor>) past eventuele openstaande configuratiemigraties opnieuw toe en controleert op problemen die tijdens de import zijn geïntroduceerd.

* ### Herstart en verifieer

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Bevestig dat de Gateway gezond is en dat je geïmporteerde model, geheugen en Skills zijn geladen.

## Conflictafhandeling

Apply weigert door te gaan wanneer het plan conflicten meldt (een bestand of configuratiewaarde bestaat al op het doel).

Voor een nieuwe OpenClaw-installatie zijn conflicten ongebruikelijk. Ze verschijnen meestal wanneer je de import opnieuw uitvoert op een setup die al gebruikersbewerkingen bevat.

Als er midden tijdens apply een conflict optreedt (bijvoorbeeld een onverwachte race op een configuratiebestand), markeert Hermes resterende afhankelijke configuratie-items als `skipped` met reden `blocked by earlier apply conflict` in plaats van ze gedeeltelijk te schrijven. Het migratierapport registreert elk geblokkeerd item, zodat je het oorspronkelijke conflict kunt oplossen en de import opnieuw kunt uitvoeren.

## Geheimen

Geheimen worden standaard nooit geïmporteerd.

  * Voer eerst `openclaw migrate apply hermes --yes` uit om niet-geheime status te importeren.
  * Als je ook ondersteunde `.env`-sleutels wilt kopiëren, voer dan opnieuw uit met `--include-secrets`.
  * Voor door SecretRef beheerde referenties configureer je de SecretRef-bron nadat de import is voltooid.


## JSON-uitvoer voor automatisering

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Met `--json` en zonder `--yes` drukt apply het plan af en muteert het geen status. Dit is de veiligste modus voor CI en gedeelde scripts.

## Probleemoplossing

Apply weigert met conflicten

Inspecteer de planuitvoer. Elk conflict identificeert het bronpad en het bestaande doel. Bepaal per item of je wilt overslaan, het doel wilt bewerken, of opnieuw wilt uitvoeren met `--overwrite`.

Hermes staat buiten ~/.hermes

Geef `--from /actual/path` (CLI) of `--import-source /actual/path` (onboarding) door.

Onboarding weigert te importeren op een bestaande setup

Onboardingimports vereisen een nieuwe setup. Reset de status en onboard opnieuw, of gebruik `openclaw migrate apply hermes` rechtstreeks, dat `--overwrite` en expliciete back-upcontrole ondersteunt.

API-sleutels zijn niet geïmporteerd

`--include-secrets` is vereist, en alleen de hierboven vermelde sleutels worden herkend. Andere variabelen in `.env` worden genegeerd.

## Gerelateerd

  * [`openclaw migrate`](</nl/cli/migrate>): volledige CLI-referentie, Plugin-contract en JSON-vormen.
  * [Onboarding](</nl/cli/onboard>): wizardworkflow en niet-interactieve vlaggen.
  * [Migreren](</nl/install/migrating>): verplaats een OpenClaw-installatie tussen machines.
  * [Doctor](</nl/gateway/doctor>): gezondheidscontrole na migratie.
  * [Agentwerkruimte](</nl/concepts/agent-workspace>): waar `SOUL.md`, `AGENTS.md` en geheugenbestanden staan.


Was this useful?YesNo