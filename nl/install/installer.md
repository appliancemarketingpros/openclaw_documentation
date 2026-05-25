---
title: Interne werking van het installatieprogramma
source_url: https://docs.openclaw.ai/nl/install/installer
scraped_at: 2026-05-25
---

OpenClaw levert drie installatiescripts, aangeboden vanaf `openclaw.ai`.

Script | Platform | Wat het doet  
---|---|---  
`install.sh` | macOS / Linux / WSL | Installeert Node indien nodig, installeert OpenClaw via npm (standaard) of git, en kan onboarding uitvoeren.  
`install-cli.sh` | macOS / Linux / WSL | Installeert Node + OpenClaw in een lokale prefix (`~/.openclaw`) met npm- of git-checkoutmodi. Geen root vereist.  
`install.ps1` | Windows (PowerShell) | Installeert Node indien nodig, installeert OpenClaw via npm (standaard) of git, en kan onboarding uitvoeren.  
  
## Snelle opdrachten

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Verloop ([install.sh](<http://install.sh>))

* ### Besturingssysteem detecteren

Ondersteunt macOS en Linux (inclusief WSL). Als macOS wordt gedetecteerd, installeert dit Homebrew als het ontbreekt.

* ### Standaard Node.js 24 garanderen

Controleert de Node-versie en installeert Node 24 indien nodig (Homebrew op macOS, NodeSource-installatiescripts op Linux apt/dnf/yum). OpenClaw ondersteunt nog steeds Node 22 LTS, momenteel `22.16+`, voor compatibiliteit.

* ### Git garanderen

Installeert Git als het ontbreekt.

* ### OpenClaw installeren

  * `npm`-methode (standaard): globale npm-installatie
  * `git`-methode: repo klonen/bijwerken, afhankelijkheden installeren met pnpm, bouwen en daarna wrapper installeren op `~/.local/bin/openclaw`


* ### Taken na installatie

  * Vernieuwt zo goed mogelijk een geladen Gateway-service (`openclaw gateway install --force`, daarna herstarten)
  * Voert `openclaw doctor --non-interactive` uit bij upgrades en git-installaties (zo goed mogelijk)
  * Probeert onboarding wanneer gepast (TTY beschikbaar, onboarding niet uitgeschakeld, en bootstrap-/configuratiecontroles slagen)
  * Stelt standaard `SHARP_IGNORE_GLOBAL_LIBVIPS=1` in


### Broncheckoutdetectie

Als het script wordt uitgevoerd binnen een OpenClaw-checkout (`package.json` \+ `pnpm-workspace.yaml`), biedt het script het volgende aan:

  * checkout gebruiken (`git`), of
  * globale installatie gebruiken (`npm`)


Als er geen TTY beschikbaar is en er geen installatiemethode is ingesteld, wordt standaard `npm` gebruikt en wordt een waarschuwing gegeven.

Het script sluit af met code `2` bij een ongeldige methodeselectie of ongeldige `--install-method`-waarden.

### Voorbeelden ([install.sh](<http://install.sh>))

### Standaard

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Onboarding overslaan

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git-installatie

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub-main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Proefuitvoering

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Referentie voor vlaggen Vlag | Beschrijving  
---|---  
`--install-method npm|git` | Kies de installatiemethode (standaard: `npm`). Alias: `--method`  
`--npm` | Snelkoppeling voor npm-methode  
`--git` | Snelkoppeling voor git-methode. Alias: `--github`  
`--version <version|dist-tag|spec>` | npm-versie, dist-tag of pakketspecificatie (standaard: `latest`)  
`--beta` | Gebruik de beta dist-tag indien beschikbaar, anders terugvallen op `latest`  
`--git-dir <path>` | Checkoutmap (standaard: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Sla `git pull` over voor bestaande checkout  
`--no-prompt` | Schakel prompts uit  
`--no-onboard` | Sla onboarding over  
`--onboard` | Schakel onboarding in  
`--dry-run` | Druk acties af zonder wijzigingen toe te passen  
`--verbose` | Schakel debuguitvoer in (`set -x`, npm notice-level logs)  
`--help` | Toon gebruik (`-h`)  
Referentie voor omgevingsvariabelen Variabele | Beschrijving  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installatiemethode  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | npm-versie, dist-tag of pakketspecificatie  
`OPENCLAW_BETA=0|1` | Gebruik beta indien beschikbaar  
`OPENCLAW_GIT_DIR=<path>` | Checkoutmap  
`OPENCLAW_GIT_UPDATE=0|1` | Git-updates in-/uitschakelen  
`OPENCLAW_NO_PROMPT=1` | Schakel prompts uit  
`OPENCLAW_NO_ONBOARD=1` | Sla onboarding over  
`OPENCLAW_DRY_RUN=1` | Modus voor proefuitvoering  
`OPENCLAW_VERBOSE=1` | Debugmodus  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm-logniveau  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Beheer sharp/libvips-gedrag (standaard: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Verloop ([install-cli.sh](<http://install-cli.sh>))

* ### Lokale Node-runtime installeren

Downloadt een vastgezette ondersteunde Node LTS-tarball (de versie is ingebed in het script en wordt onafhankelijk bijgewerkt) naar `<prefix>/tools/node-v<version>` en verifieert SHA-256.

* ### Git garanderen

Als Git ontbreekt, probeert het installatie via apt/dnf/yum op Linux of Homebrew op macOS.

* ### OpenClaw onder prefix installeren

  * `npm`-methode (standaard): installeert onder de prefix met npm en schrijft daarna de wrapper naar `<prefix>/bin/openclaw`
  * `git`-methode: kloont/werkt een checkout bij (standaard `~/openclaw`) en schrijft nog steeds de wrapper naar `<prefix>/bin/openclaw`


* ### Geladen Gateway-service vernieuwen

Als er al een Gateway-service vanuit diezelfde prefix is geladen, voert het script `openclaw gateway install --force` uit, daarna `openclaw gateway restart`, en controleert het de Gateway-status zo goed mogelijk.

### Voorbeelden ([install-cli.sh](<http://install-cli.sh>))

### Standaard

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Aangepaste prefix + versie

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git-installatie

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### JSON-uitvoer voor automatisering

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Onboarding uitvoeren

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Referentie voor vlaggen Vlag | Beschrijving  
---|---  
`--prefix <path>` | Installatieprefix (standaard: `~/.openclaw`)  
`--install-method npm|git` | Kies de installatiemethode (standaard: `npm`). Alias: `--method`  
`--npm` | Snelkoppeling voor npm-methode  
`--git`, `--github` | Snelkoppeling voor git-methode  
`--git-dir <path>` | Git-checkoutmap (standaard: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | OpenClaw-versie of dist-tag (standaard: `latest`)  
`--node-version <ver>` | Node-versie (standaard: `22.22.0`)  
`--json` | Geef NDJSON-events uit  
`--onboard` | Voer `openclaw onboard` uit na installatie  
`--no-onboard` | Sla onboarding over (standaard)  
`--set-npm-prefix` | Forceer op Linux de npm-prefix naar `~/.npm-global` als de huidige prefix niet schrijfbaar is  
`--help` | Toon gebruik (`-h`)  
Referentie voor omgevingsvariabelen Variabele | Beschrijving  
---|---  
`OPENCLAW_PREFIX=<path>` | Installatieprefix  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installatiemethode  
`OPENCLAW_VERSION=<ver>` | OpenClaw-versie of dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Node-versie  
`OPENCLAW_GIT_DIR=<path>` | Git-checkoutmap voor git-installaties  
`OPENCLAW_GIT_UPDATE=0|1` | Git-updates voor bestaande checkouts in- of uitschakelen  
`OPENCLAW_NO_ONBOARD=1` | Introductie overslaan  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm-logniveau  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips-gedrag beheren (standaard: `1`)  
  
* * *

## install.ps1

### Stroom (install.ps1)

* ### PowerShell + Windows-omgeving controleren

Vereist PowerShell 5+.

* ### Standaard Node.js 24 controleren

Als dit ontbreekt, probeert het installatie via winget, daarna Chocolatey en daarna Scoop. Node 22 LTS, momenteel `22.16+`, blijft ondersteund voor compatibiliteit.

* ### OpenClaw installeren

  * `npm`-methode (standaard): globale npm-installatie met de geselecteerde `-Tag`, gestart vanuit een beschrijfbare tijdelijke installatiemap, zodat shells die zijn geopend in beveiligde mappen zoals `C:\` nog steeds werken
  * `git`-methode: repo klonen/bijwerken, installeren/bouwen met pnpm, en wrapper installeren op `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Taken na installatie

  * Voegt waar mogelijk de benodigde bin-map toe aan de gebruikers-PATH
  * Vernieuwt naar beste kunnen een geladen Gateway-service (`openclaw gateway install --force`, daarna opnieuw starten)
  * Voert `openclaw doctor --non-interactive` uit bij upgrades en git-installaties (naar beste kunnen)


* ### Fouten afhandelen

`iwr ... | iex` en scriptblock-installaties melden een beëindigende fout zonder de huidige PowerShell-sessie te sluiten. Directe installaties met `powershell -File` / `pwsh -File` sluiten nog steeds af met een niet-nulcode voor automatisering.

### Voorbeelden (install.ps1)

### Standaard

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git-installatie

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main via npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Aangepaste git-map

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Proefuitvoering

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Debugtrace

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Flagreferentie Flag | Beschrijving  
---|---  
`-InstallMethod npm|git` | Installatiemethode (standaard: `npm`)  
`-Tag <tag|version|spec>` | npm-dist-tag, versie of pakketspecificatie (standaard: `latest`)  
`-GitDir <path>` | Checkoutmap (standaard: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Introductie overslaan  
`-NoGitUpdate` | `git pull` overslaan  
`-DryRun` | Alleen acties afdrukken  
Referentie voor omgevingsvariabelen Variabele | Beschrijving  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Installatiemethode  
`OPENCLAW_GIT_DIR=<path>` | Checkoutmap  
`OPENCLAW_NO_ONBOARD=1` | Introductie overslaan  
`OPENCLAW_GIT_UPDATE=0` | git pull uitschakelen  
`OPENCLAW_DRY_RUN=1` | Proefuitvoeringsmodus  
  
* * *

## CI en automatisering

Gebruik niet-interactieve flags/omgevingsvariabelen voor voorspelbare uitvoeringen.

### install.sh (niet-interactieve npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (niet-interactieve git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (introductie overslaan)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Probleemoplossing

Waarom is Git vereist?

Git is vereist voor de `git`-installatiemethode. Voor `npm`-installaties wordt Git nog steeds gecontroleerd/geïnstalleerd om fouten met `spawn git ENOENT` te voorkomen wanneer afhankelijkheden git-URL's gebruiken.

Waarom krijgt npm EACCES op Linux?

Sommige Linux-installaties laten de globale npm-prefix naar paden wijzen die eigendom zijn van root. `install.sh` kan de prefix wijzigen naar `~/.npm-global` en PATH-exports toevoegen aan shell-rc-bestanden (wanneer die bestanden bestaan).

sharp/libvips-problemen

De scripts gebruiken standaard `SHARP_IGNORE_GLOBAL_LIBVIPS=1` om te voorkomen dat sharp tegen de systeemversie van libvips bouwt. Overschrijven:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Installeer Git for Windows, open PowerShell opnieuw en voer het installatieprogramma opnieuw uit.

Windows: "openclaw is not recognized"

Voer `npm config get prefix` uit en voeg die map toe aan je gebruikers-PATH (geen `\bin`-achtervoegsel nodig op Windows), en open PowerShell daarna opnieuw.

Windows: uitgebreide installatie-uitvoer krijgen

`install.ps1` biedt momenteel geen `-Verbose`-switch. Gebruik PowerShell-tracing voor diagnostiek op scriptniveau:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw niet gevonden na installatie

Meestal een PATH-probleem. Zie [Node.js-probleemoplossing](</nl/install/node#troubleshooting>).

## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Bijwerken](</nl/install/updating>)
  * [Verwijderen](</nl/install/uninstall>)


Was this useful?YesNo