---
title: Bijwerken
source_url: https://docs.openclaw.ai/nl/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Werk OpenClaw veilig bij en wissel tussen stable-/beta-/dev-kanalen.

Als je hebt geïnstalleerd via **npm/pnpm/bun** (globale installatie, zonder git-metadata), worden updates uitgevoerd via de package-manager-flow in [Bijwerken](</nl/install/updating>).

## Gebruik

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opties

  * `--no-restart`: sla het herstarten van de Gateway-service over na een geslaagde update. Package-manager-updates die de Gateway wel herstarten, verifiëren dat de herstarte service de verwachte bijgewerkte versie rapporteert voordat de opdracht slaagt.
  * `--channel <stable|beta|dev>`: stel het updatekanaal in (git + npm; opgeslagen in de configuratie).
  * `--tag <dist-tag|version|spec>`: overschrijf het package-doel alleen voor deze update. Voor package-installaties wordt `main` gekoppeld aan `github:openclaw/openclaw#main`.
  * `--dry-run`: toon een voorbeeld van geplande updateacties (kanaal/tag/doel/herstart-flow) zonder configuratie te schrijven, te installeren, Plugins te synchroniseren of te herstarten.
  * `--json`: druk machineleesbare `UpdateRunResult`-JSON af, inclusief `postUpdate.plugins.warnings` wanneer corrupte of niet-laadbare beheerde Plugins reparatie nodig hebben nadat de core-update is geslaagd, details over Plugin-terugval voor het betakanaal wanneer een Plugin geen betarelease heeft, en `postUpdate.plugins.integrityDrifts` wanneer drift in npm-Plugin-artefacten wordt gedetecteerd tijdens Plugin-synchronisatie na de update.
  * `--timeout <seconds>`: time-out per stap (standaard 1800 s).
  * `--yes`: sla bevestigingsprompts over (bijvoorbeeld bevestiging voor downgraden).


`openclaw update` heeft geen `--verbose`-vlag. Gebruik `--dry-run` om een voorbeeld te bekijken van de geplande kanaal-/tag-/installatie-/herstartacties, `--json` voor machineleesbare resultaten, en `openclaw update status --json` wanneer je alleen kanaal- en beschikbaarheidsdetails nodig hebt. Als je Gateway-logboeken rond een update debugt, zijn consoleverbosity en bestandslogniveau gescheiden: Gateway `--verbose` beïnvloedt terminal-/WebSocket-uitvoer, terwijl bestandslogboeken `logging.level: "debug"` of `"trace"` in de configuratie vereisen. Zie [Gateway-logboekregistratie](</nl/gateway/logging>).

## `update status`

Toon het actieve updatekanaal + git-tag/-branch/-SHA (voor source-checkouts), plus updatebeschikbaarheid.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opties:

  * `--json`: druk machineleesbare status-JSON af.
  * `--timeout <seconds>`: time-out voor controles (standaard 3 s).


## `update wizard`

Interactieve flow om een updatekanaal te kiezen en te bevestigen of de Gateway na het bijwerken moet worden herstart (standaard wordt herstart). Als je `dev` selecteert zonder git-checkout, wordt aangeboden er een te maken.

Opties:

  * `--timeout <seconds>`: time-out voor elke updatestap (standaard `1800`)


## Wat het doet

Wanneer je expliciet van kanaal wisselt (`--channel ...`), houdt OpenClaw ook de installatiemethode in lijn:

  * `dev` → zorgt voor een git-checkout (standaard: `~/openclaw`, overschrijfbaar met `OPENCLAW_GIT_DIR`), werkt deze bij en installeert de globale CLI vanuit die checkout.
  * `stable` → installeert vanuit npm met `latest`.
  * `beta` → geeft de voorkeur aan npm-dist-tag `beta`, maar valt terug op `latest` wanneer beta ontbreekt of ouder is dan de huidige stable-release.


De automatische updater van de Gateway-core (wanneer ingeschakeld via configuratie) start het CLI-updatepad buiten de live Gateway-requesthandler. Control-plane `update.run` package-manager-updates forceren een niet-uitgestelde updateherstart zonder cooldown na de package-wissel, omdat het oude Gateway-proces mogelijk nog chunks in het geheugen heeft die verwijzen naar bestanden die door het nieuwe package zijn verwijderd.

Voor package-manager-installaties bepaalt `openclaw update` de doelversie van het package voordat de package manager wordt aangeroepen. Globale npm-installaties gebruiken een gestagede installatie: OpenClaw installeert het nieuwe package in een tijdelijke npm-prefix, verifieert daar de meegeleverde `dist`-inventaris, en wisselt vervolgens die schone package-tree naar de echte globale prefix. Als verificatie mislukt, worden doctor na de update, Plugin-synchronisatie en herstartwerk niet uitgevoerd vanuit de verdachte tree. Zelfs wanneer de geïnstalleerde versie al overeenkomt met het doel, ververst de opdracht de globale package-installatie en voert daarna Plugin-synchronisatie, een verversing van core-opdrachtvoltooiing en herstartwerk uit. Dit houdt meegeleverde sidecars en kanaalbeheerde Plugin-records in lijn met de geïnstalleerde OpenClaw-build, terwijl volledige herbouws van Plugin-opdrachtvoltooiing worden overgelaten aan expliciete `openclaw completion --write-state`-runs.

Wanneer een lokale beheerde Gateway-service is geïnstalleerd en herstarten is ingeschakeld, stoppen package-manager-updates de draaiende service voordat de package-tree wordt vervangen, verversen vervolgens de servicemetadata vanuit de bijgewerkte installatie, herstarten de service en verifiëren dat de herstarte Gateway de verwachte versie rapporteert voordat succes wordt gemeld. Op macOS verifieert de controle na de update ook dat de LaunchAgent is geladen/draait voor het actieve profiel en dat de geconfigureerde loopbackpoort gezond is. Als de plist is geïnstalleerd maar launchd deze niet superviseert, bootstrapt OpenClaw de LaunchAgent automatisch opnieuw en voert daarna de controles voor gezondheid/versie/kanaalgereedheid opnieuw uit. Een verse bootstrap laadt de RunAtLoad-job rechtstreeks, zodat updateherstel niet meteen `kickstart -k` uitvoert op de nieuw gestarte Gateway. Als de Gateway nog steeds niet gezond wordt, sluit de opdracht af met een niet-nulstatus en drukt het pad naar het herstartlogboek plus expliciete instructies voor herstarten, opnieuw installeren en package-rollback af. Met `--no-restart` wordt de package-vervanging nog steeds uitgevoerd, maar de beheerde service wordt niet gestopt of herstart, waardoor de draaiende Gateway oude code kan blijven gebruiken totdat je deze handmatig herstart.

## Git-checkout-flow

### Kanaalselectie

  * `stable`: checkout de nieuwste niet-beta-tag, bouw daarna en voer doctor uit.
  * `beta`: geef de voorkeur aan de nieuwste `-beta`-tag, maar val terug op de nieuwste stable-tag wanneer beta ontbreekt of ouder is.
  * `dev`: checkout `main`, haal daarna op en rebase.


### Updatestappen

* ### Verify clean worktree

Vereist geen niet-gecommitte wijzigingen.

* ### Switch channel

Wisselt naar het geselecteerde kanaal (tag of branch).

* ### Fetch upstream

Alleen dev.

* ### Preflight build (dev only)

Voert de TypeScript-build uit in een tijdelijke worktree. Als de tip mislukt, loopt deze tot 10 commits terug om de nieuwste bouwbare commit te vinden. Stel `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` in om tijdens deze preflight ook lint uit te voeren; lint draait in beperkte seriële modus, omdat updatehosts van gebruikers vaak kleiner zijn dan CI-runners.

* ### Rebase

Rebaset op de geselecteerde commit (alleen dev).

* ### Install dependencies

Gebruikt de package manager van de repo. Voor pnpm-checkouts bootstrapt de updater `pnpm` op aanvraag (eerst via `corepack`, daarna met een tijdelijke fallback `npm install pnpm@11`) in plaats van `npm run build` binnen een pnpm-workspace uit te voeren.

* ### Build Control UI

Bouwt de Gateway en de Control UI.

* ### Run doctor

`openclaw doctor` draait als laatste veilige updatecontrole.

* ### Sync plugins

Synchroniseert Plugins naar het actieve kanaal. Dev gebruikt gebundelde Plugins; stable en beta gebruiken npm. Werkt bijgehouden Plugin-installaties bij.

Op het beta-updatekanaal proberen bijgehouden npm- en ClawHub-Plugin-installaties die de standaard-/latest-lijn volgen eerst een Plugin-`@beta`-release. Als de Plugin geen betarelease heeft, valt OpenClaw terug op de vastgelegde standaard-/latest-specificatie en rapporteert dat als waarschuwing. Voor npm-Plugins valt OpenClaw ook terug wanneer het beta-package bestaat maar installatievalidatie mislukt. Deze waarschuwingen over Plugin-terugval laten de core-update niet mislukken. Exacte versies en expliciete tags worden niet herschreven.

## `--update`-afkorting

`openclaw --update` wordt herschreven naar `openclaw update` (handig voor shells en launcher-scripts).

## Gerelateerd

  * `openclaw doctor` (biedt aan eerst update uit te voeren op git-checkouts)
  * [Ontwikkelingskanalen](</nl/install/development-channels>)
  * [Bijwerken](</nl/install/updating>)
  * [CLI-referentie](</nl/cli>)


Was this useful?YesNo