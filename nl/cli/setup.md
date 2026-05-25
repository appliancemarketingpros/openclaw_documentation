---
title: Installatie
source_url: https://docs.openclaw.ai/nl/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Initialiseer de basisconfiguratie en agentwerkruimte. Als er een onboarding-vlag aanwezig is, wordt ook de wizard uitgevoerd.

## Opties

Vlag | Beschrijving  
---|---  
`--workspace <dir>` | Agentwerkruimtemap (standaard `~/.openclaw/workspace`; opgeslagen als `agents.defaults.workspace`).  
`--wizard` | Interactieve onboarding uitvoeren.  
`--non-interactive` | Onboarding zonder prompts uitvoeren.  
`--mode <mode>` | Onboardingmodus: `local` of `remote`.  
`--import-from <provider>` | Migratieprovider die tijdens onboarding moet worden uitgevoerd.  
`--import-source <path>` | Bron-agenthome voor `--import-from`.  
`--import-secrets` | Ondersteunde geheimen importeren tijdens onboardingmigratie.  
`--remote-url <url>` | Remote Gateway WebSocket-URL.  
`--remote-token <token>` | Remote Gateway-token (optioneel).  
  
### Automatische wizard-trigger

`openclaw setup` voert de wizard uit wanneer een van deze vlaggen expliciet aanwezig is, zelfs zonder `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Voorbeelden

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Notities

  * Gewone `openclaw setup` initialiseert configuratie en werkruimte zonder de volledige onboarding-flow uit te voeren.
  * Voer na gewone setup `openclaw onboard` uit voor het volledige begeleide traject, `openclaw configure` voor gerichte wijzigingen, of `openclaw channels add` om kanaalaccounts toe te voegen.
  * Als Hermes-status wordt gedetecteerd, kan interactieve onboarding automatisch migratie aanbieden. Import-onboarding vereist een nieuwe setup; gebruik [Migreren](</nl/cli/migrate>) voor dry-run-plannen, back-ups en overschrijfmodus buiten onboarding.


## Verwant

  * [CLI-referentie](</nl/cli>)
  * [Onboarding (CLI)](</nl/start/wizard>)
  * [Aan de slag](</nl/start/getting-started>)
  * [Installatieoverzicht](</nl/install>)


Was this useful?YesNo