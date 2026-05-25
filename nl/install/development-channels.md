---
title: Releasekanalen
source_url: https://docs.openclaw.ai/nl/install/development-channels
scraped_at: 2026-05-25
---

OpenClaw levert drie updatekanalen:

  * **stable** : npm dist-tag `latest`. Aanbevolen voor de meeste gebruikers.
  * **beta** : npm dist-tag `beta` wanneer deze actueel is; als beta ontbreekt of ouder is dan de nieuwste stable-release, valt de updateflow terug op `latest`.
  * **dev** : bewegende kop van `main` (git). npm dist-tag: `dev` (wanneer gepubliceerd). De `main`-branch is bedoeld voor experimenten en actieve ontwikkeling. Deze kan onvolledige functies of breaking changes bevatten. Gebruik deze niet voor productie-Gateways.


We leveren stable-builds meestal eerst aan **beta** , testen ze daar en voeren daarna een expliciete promotiestap uit die de gecontroleerde build naar `latest` verplaatst zonder het versienummer te wijzigen. Maintainers kunnen indien nodig ook een stable-release rechtstreeks naar `latest` publiceren. Dist-tags zijn de bron van waarheid voor npm- installaties.

## Van kanaal wisselen

bashCopy code
[code]
    openclaw update --channel stableopenclaw update --channel betaopenclaw update --channel dev
[/code]

`--channel` slaat je keuze op in de configuratie (`update.channel`) en stemt de installatiemethode daarop af:

  * **`stable`** (pakketinstallaties): werkt bij via npm dist-tag `latest`.
  * **`beta`** (pakketinstallaties): geeft de voorkeur aan npm dist-tag `beta`, maar valt terug op `latest` wanneer `beta` ontbreekt of ouder is dan de huidige stable-tag.
  * **`stable`** (git-installaties): checkt de nieuwste stable git-tag uit.
  * **`beta`** (git-installaties): geeft de voorkeur aan de nieuwste beta git-tag, maar valt terug op de nieuwste stable git-tag wanneer beta ontbreekt of ouder is.
  * **`dev`** : zorgt voor een git-checkout (standaard `~/openclaw`, overschrijf met `OPENCLAW_GIT_DIR`), schakelt over naar `main`, rebaset op upstream, bouwt en installeert de globale CLI vanuit die checkout.


## Eenmalig een versie of tag targeten

Gebruik `--tag` om voor één update een specifieke dist-tag, versie of pakketspecificatie te targeten **zonder** je opgeslagen kanaal te wijzigen:

bashCopy code
[code]
    # Install a specific versionopenclaw update --tag 2026.4.1-beta.1 # Install from the beta dist-tag (one-off, does not persist)openclaw update --tag beta # Install from GitHub main branch (npm tarball)openclaw update --tag main # Install a specific npm package specopenclaw update --tag openclaw@2026.4.1-beta.1
[/code]

Opmerkingen:

  * `--tag` geldt alleen voor **pakketinstallaties (npm)**. Git-installaties negeren deze optie.
  * De tag wordt niet opgeslagen. Je volgende `openclaw update` gebruikt zoals gewoonlijk je geconfigureerde kanaal.
  * Downgradebeveiliging: als de doelversie ouder is dan je huidige versie, vraagt OpenClaw om bevestiging (sla over met `--yes`).
  * `--channel beta` is iets anders dan `--tag beta`: de kanaalflow kan terugvallen op stable/latest wanneer beta ontbreekt of ouder is, terwijl `--tag beta` de ruwe `beta`-dist-tag voor die ene uitvoering target.


## Dry run

Bekijk vooraf wat `openclaw update` zou doen zonder wijzigingen aan te brengen:

bashCopy code
[code]
    openclaw update --dry-runopenclaw update --channel beta --dry-runopenclaw update --tag 2026.4.1-beta.1 --dry-runopenclaw update --dry-run --json
[/code]

De dry run toont het effectieve kanaal, de doelversie, geplande acties en of bevestiging voor een downgrade vereist zou zijn.

## Plugins en kanalen

Wanneer je met `openclaw update` van kanaal wisselt, synchroniseert OpenClaw ook Plugin- bronnen:

  * `dev` geeft de voorkeur aan gebundelde Plugins uit de git-checkout.
  * `stable` en `beta` herstellen via npm geïnstalleerde Plugin-pakketten.
  * Via npm geïnstalleerde Plugins worden bijgewerkt nadat de core-update is voltooid.


## Huidige status controleren

bashCopy code
[code]
    openclaw update status
[/code]

Toont het actieve kanaal, installatietype (git of pakket), huidige versie en bron (configuratie, git-tag, git-branch of standaard).

## Best practices voor tagging

  * Tag releases waarop je git-checkouts wilt laten landen (`vYYYY.M.D` voor stable, `vYYYY.M.D-beta.N` voor beta).
  * `vYYYY.M.D.beta.N` wordt ook herkend voor compatibiliteit, maar geef de voorkeur aan `-beta.N`.
  * Legacy `vYYYY.M.D-<patch>`-tags worden nog steeds herkend als stable (niet-beta).
  * Houd tags immutable: verplaats of hergebruik een tag nooit.
  * npm dist-tags blijven de bron van waarheid voor npm-installaties: 
    * `latest` -> stable
    * `beta` -> kandidaat-build of beta-first stable-build
    * `dev` -> main-snapshot (optioneel)


## Beschikbaarheid van de macOS-app

Beta- en dev-builds bevatten mogelijk **geen** macOS-apprelease. Dat is prima:

  * De git-tag en npm dist-tag kunnen nog steeds worden gepubliceerd.
  * Vermeld "geen macOS-build voor deze beta" in release notes of changelog.


## Gerelateerd

  * [Bijwerken](</nl/install/updating>)
  * [Installer-internals](</nl/install/installer>)


Was this useful?YesNo