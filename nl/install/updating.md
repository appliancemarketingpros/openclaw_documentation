---
title: Bijwerken
source_url: https://docs.openclaw.ai/nl/install/updating
scraped_at: 2026-05-25
---

Houd OpenClaw up-to-date.

## Aanbevolen: `openclaw update`

De snelste manier om te updaten. Het detecteert je installatietype (npm of git), haalt de nieuwste versie op, voert `openclaw doctor` uit en herstart de Gateway.

bashCopy code
[code]
    openclaw update
[/code]

Om van kanaal te wisselen of een specifieke versie te gebruiken:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --tag mainopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update` accepteert geen `--verbose`. Gebruik voor updatediagnostiek `--dry-run` om de geplande acties vooraf te bekijken, `--json` voor gestructureerde resultaten, of `openclaw update status --json` om de kanaal- en beschikbaarheidsstatus te controleren. Het installatieprogramma heeft een eigen `--verbose`-vlag, maar die vlag maakt geen deel uit van `openclaw update`.

`--channel beta` geeft de voorkeur aan beta, maar de runtime valt terug op stable/latest wanneer de beta-tag ontbreekt of ouder is dan de nieuwste stabiele release. Gebruik `--tag beta` als je de onbewerkte npm beta dist-tag wilt voor een eenmalige pakketupdate.

Voor beheerde Plugins is terugvallen vanaf het beta-kanaal een waarschuwing: de core-update kan nog steeds slagen terwijl een Plugin de vastgelegde standaard-/nieuwste release gebruikt omdat er geen Plugin-beta beschikbaar is.

Zie [Ontwikkelingskanalen](</nl/install/development-channels>) voor kanaalsemantiek.

## Wisselen tussen npm- en git-installaties

Gebruik kanalen wanneer je het installatietype wilt wijzigen. De updater behoudt je status, configuratie, referenties en werkruimte in `~/.openclaw`; hij wijzigt alleen welke OpenClaw-code-installatie de CLI en Gateway gebruiken.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Voer eerst uit met `--dry-run` om de exacte installatiemodus-wissel vooraf te bekijken:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

Het `dev`-kanaal zorgt voor een git-checkout, bouwt die en installeert de globale CLI vanuit die checkout. De `stable`\- en `beta`-kanalen gebruiken pakketinstallaties. Als de Gateway al is geïnstalleerd, vernieuwt `openclaw update` de servicemetadata en herstart deze, tenzij je `--no-restart` meegeeft.

## Alternatief: voer het installatieprogramma opnieuw uit

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

Voeg `--no-onboard` toe om onboarding over te slaan. Om via het installatieprogramma een specifiek installatietype af te dwingen, geef je `--install-method git --no-onboard` of `--install-method npm --no-onboard` mee.

Als `openclaw update` mislukt na de npm-pakketinstallatiefase, voer dan het installatieprogramma opnieuw uit. Het installatieprogramma roept de oude updater niet aan; het voert de globale pakketinstallatie rechtstreeks uit en kan een gedeeltelijk bijgewerkte npm-installatie herstellen.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Om het herstel vast te zetten op een specifieke versie of dist-tag, voeg je `--version` toe:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Alternatief: handmatig npm, pnpm of bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Geef de voorkeur aan `openclaw update` voor begeleide installaties, omdat dit de pakketwissel kan coördineren met de draaiende Gateway-service. Als je handmatig bijwerkt terwijl een beheerde Gateway draait, herstart de Gateway dan direct nadat de package manager klaar is, zodat het oude proces niet blijft draaien vanaf vervangen pakketbestanden.

Wanneer `openclaw update` een globale npm-installatie beheert, installeert het het doel eerst in een tijdelijke npm-prefix, verifieert het de verpakte `dist`-inventaris en wisselt het daarna de schone pakketstructuur naar de echte globale prefix. Dat voorkomt dat npm een nieuw pakket over verouderde bestanden uit het oude pakket heen legt. Als de installatieopdracht mislukt, probeert OpenClaw het één keer opnieuw met `--omit=optional`. Die nieuwe poging helpt hosts waar native optionele afhankelijkheden niet kunnen compileren, terwijl de oorspronkelijke fout zichtbaar blijft als de fallback ook mislukt.

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Geavanceerde npm-installatieonderwerpen

Alleen-lezen pakketstructuur

OpenClaw behandelt verpakte globale installaties tijdens runtime als alleen-lezen, zelfs wanneer de globale pakketdirectory schrijfbaar is voor de huidige gebruiker. Plugin-pakketinstallaties staan in npm-/git-roots die eigendom zijn van OpenClaw onder de gebruikersconfiguratiedirectory, en het starten van de Gateway wijzigt de OpenClaw-pakketstructuur niet.

Sommige Linux-npm-configuraties installeren globale pakketten onder root-eigendom-directory's zoals `/usr/lib/node_modules/openclaw`. OpenClaw ondersteunt die indeling omdat Plugin-installatie-/updateopdrachten buiten die globale pakketdirectory schrijven.

Versterkte systemd-units

Geef OpenClaw schrijftoegang tot de configuratie-/statusroots zodat expliciete Plugin-installaties, Plugin-updates en doctor-opschoning hun wijzigingen kunnen bewaren:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Schijfruimte-preflight

Voor pakketupdates en expliciete Plugin-installaties probeert OpenClaw een beste-inspanningscontrole van de schijfruimte voor het doelvolume. Weinig ruimte levert een waarschuwing op met het gecontroleerde pad, maar blokkeert de update niet omdat bestandssysteemquota, snapshots en netwerkvolumes na de controle kunnen veranderen. De daadwerkelijke installatie door de package manager en de verificatie na installatie blijven leidend.

## Auto-updater

De auto-updater staat standaard uit. Schakel deze in via `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Kanaal | Gedrag  
---|---  
`stable` | Wacht `stableDelayHours` en past dan toe met deterministische jitter over `stableJitterHours` (gespreide uitrol).  
`beta` | Controleert elke `betaCheckIntervalHours` (standaard: elk uur) en past direct toe.  
`dev` | Geen automatische toepassing. Gebruik `openclaw update` handmatig.  
  
De Gateway logt ook een updatehint bij het opstarten (uitschakelen met `update.checkOnStart: false`). Voor downgrade of incidentherstel stel je `OPENCLAW_NO_AUTO_UPDATE=1` in de Gateway-omgeving in om automatische toepassingen te blokkeren, zelfs wanneer `update.auto.enabled` is geconfigureerd. Updatehints bij het opstarten kunnen nog steeds worden uitgevoerd, tenzij `update.checkOnStart` ook is uitgeschakeld.

Pakketmanager-updates die via de live Gateway-control-plane-handler worden aangevraagd forceren na de pakketwissel een niet-uitgestelde updateherstart zonder cooldown. Dat voorkomt dat een oud proces in het geheugen lang genoeg blijft bestaan om chunks lazy te laden uit een pakketstructuur die al is vervangen. Shell `openclaw update` blijft het aanbevolen pad voor begeleide installaties, omdat het de service rondom de update kan stoppen en herstarten.

## Na het updaten

### Voer doctor uit

bashCopy code
[code]
    openclaw doctor
[/code]

Migreert configuratie, controleert DM-beleid en controleert de gezondheid van de Gateway. Details: [Doctor](</nl/gateway/doctor>)

### Herstart de Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Verifieer

bashCopy code
[code]
    openclaw health
[/code]

## Rollback

### Zet een versie vast (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Zet een commit vast (bron)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

Om terug te keren naar de nieuwste versie: `git checkout main && git pull`.

## Als je vastloopt

  * Voer `openclaw doctor` opnieuw uit en lees de uitvoer zorgvuldig.
  * Voor `openclaw update --channel dev` op broncheckouts bootstrapt de updater `pnpm` automatisch wanneer dat nodig is. Als je een pnpm-/corepack-bootstrapfout ziet, installeer `pnpm` dan handmatig (of schakel `corepack` opnieuw in) en voer de update opnieuw uit.
  * Controleer: [Probleemoplossing](</nl/gateway/troubleshooting>)
  * Vraag het in Discord: <https://discord.gg/clawd>


## Gerelateerd

  * [Installatieoverzicht](</nl/install>): alle installatiemethoden.
  * [Doctor](</nl/gateway/doctor>): gezondheidscontroles na updates.
  * [Migreren](</nl/install/migrating>): migratiehandleidingen voor hoofdversies.


Was this useful?YesNo