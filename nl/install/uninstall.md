---
title: De-installeren
source_url: https://docs.openclaw.ai/nl/install/uninstall
scraped_at: 2026-05-25
---

Twee paden:

  * **Eenvoudig pad** als `openclaw` nog is geïnstalleerd.
  * **Handmatige serviceverwijdering** als de CLI weg is maar de service nog draait.


## Eenvoudig pad (CLI nog geïnstalleerd)

Aanbevolen: gebruik het ingebouwde verwijderprogramma:

bashCopy code
[code]
    openclaw uninstall
[/code]

Niet-interactief (automatisering / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Handmatige stappen (zelfde resultaat):

  1. Stop de Gateway-service:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Verwijder de Gateway-service (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Verwijder status + configuratie:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Als je `OPENCLAW_CONFIG_PATH` hebt ingesteld op een aangepaste locatie buiten de statusmap, verwijder dat bestand dan ook.

  4. Verwijder je werkruimte (optioneel, verwijdert agentbestanden):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Verwijder de CLI-installatie (kies degene die je hebt gebruikt):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Als je de macOS-app hebt geïnstalleerd:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Opmerkingen:

  * Als je profielen hebt gebruikt (`--profile` / `OPENCLAW_PROFILE`), herhaal stap 3 voor elke statusmap (standaardwaarden zijn `~/.openclaw-<profile>`).
  * In externe modus staat de statusmap op de **Gateway-host** , dus voer stap 1-4 daar ook uit.


## Handmatige serviceverwijdering (CLI niet geïnstalleerd)

Gebruik dit als de Gateway-service blijft draaien maar `openclaw` ontbreekt.

### macOS (launchd)

Het standaardlabel is `ai.openclaw.gateway` (of `ai.openclaw.<profile>`; legacy `com.openclaw.*` kan nog bestaan):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Als je een profiel hebt gebruikt, vervang dan het label en de plist-naam door `ai.openclaw.<profile>`. Verwijder eventuele legacy `com.openclaw.*`-plists als die aanwezig zijn.

### Linux (systemd-gebruikerseenheid)

De standaardnaam van de eenheid is `openclaw-gateway.service` (of `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

De standaardtaaknaam is `OpenClaw Gateway` (of `OpenClaw Gateway (<profile>)`). Het taakscript staat onder je statusmap.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Als je een profiel hebt gebruikt, verwijder dan de bijbehorende taaknaam en `~\.openclaw-<profile>\gateway.cmd`.

## Normale installatie versus source-checkout

### Normale installatie ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Als je `https://openclaw.ai/install.sh` of `install.ps1` hebt gebruikt, is de CLI geïnstalleerd met `npm install -g openclaw@latest`. Verwijder deze met `npm rm -g openclaw` (of `pnpm remove -g` / `bun remove -g` als je op die manier hebt geïnstalleerd).

### Source-checkout (git clone)

Als je vanuit een repo-checkout draait (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Verwijder de Gateway-service **voordat** je de repo verwijdert (gebruik het eenvoudige pad hierboven of handmatige serviceverwijdering).
  2. Verwijder de repo-map.
  3. Verwijder status + werkruimte zoals hierboven getoond.


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Migratiehandleiding](</nl/install/migrating>)


Was this useful?YesNo