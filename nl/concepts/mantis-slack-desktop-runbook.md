---
title: Mantis Slack-desktopdraaiboek
source_url: https://docs.openclaw.ai/nl/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-05-25
---

Mantis Slack desktop-QA is de real-UI-lane voor bugs van Slack-klasse die een Linux-desktop, VNC-redding, Slack Web, een echte OpenClaw gateway, screenshots, video's en een PR-bewijscommentaar nodig hebben.

Gebruik dit wanneer unit tests of de headless Slack live-lane de bug niet kunnen bewijzen.

## Opslagmodel

Mantis gebruikt drie verschillende opslaglagen:

  * Provider-image: eigendom van Crabbox en opgeslagen in het cloudprovideraccount. Deze bevat machinecapaciteiten zoals Chrome/Chromium, ffmpeg, scrot, Node/corepack/pnpm, native buildtools en lege cachemappen.
  * Warme lease-status: eigendom van de huidige operatorsessie. Deze kan een ingelogd browserprofiel, `/var/cache/crabbox/pnpm` en een voorbereide source checkout bevatten zolang de lease actief is.
  * Mantis-artefacten: eigendom van de OpenClaw-run. Ze staan onder `.artifacts/qa-e2e/mantis/...`, waarna GitHub Actions ze uploadt en de Mantis GitHub App inline bewijs op de PR plaatst.


Plaats nooit geheimen, browsercookies, Slack-inlogstatus, repository-checkouts, `node_modules` of `dist/` in een vooraf gebakken provider-image.

## GitHub-dispatch

Voer de workflow uit vanaf `main`:

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

Toegestane `candidate_ref`-waarden zijn bewust smal omdat de workflow live-referenties gebruikt: huidige `main`-afstamming, releasetags of een open PR-head van `openclaw/openclaw`.

De workflow schrijft:

  * geüpload artefact: `mantis-slack-desktop-smoke-<run-id>-<attempt>`;
  * inline PR-commentaar van de Mantis GitHub App;
  * `slack-desktop-smoke.png`;
  * `slack-desktop-smoke.mp4`;
  * `slack-desktop-smoke-preview.gif`;
  * `slack-desktop-smoke-change.mp4`;
  * `mantis-slack-desktop-smoke-summary.json`;
  * `mantis-slack-desktop-smoke-report.md`;
  * externe logs zoals `slack-desktop-command.log`, `openclaw-gateway.log`, `chrome.log` en `ffmpeg.log`.


Het PR-commentaar wordt ter plekke bijgewerkt via de verborgen `<!-- mantis-slack-desktop-smoke -->`-markering.

## Lokale CLI

Koud source-bewijs:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

Behoud de VM voor VNC-redding:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

Open VNC:

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

Hergebruik een warme lease:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

Gebruik `--hydrate-mode prehydrated` alleen wanneer de hergebruikte externe werkruimte al `node_modules` en een gebouwde `dist/` heeft. Mantis faalt gesloten als die ontbreken.

## Hydratatiemodi

Modus | Gebruik wanneer | Extern gedrag | Afweging  
---|---|---|---  
`source` | Normaal PR-bewijs, koude machines, CI | Voert `pnpm install --frozen-lockfile --prefer-offline` en `pnpm build` uit in de VM | Traagst, sterkste source-checkout-bewijs  
`prehydrated` | Je bewust een hergebruikte lease voorbereidde | Vereist bestaande `node_modules` en `dist/`; slaat install/build over | Snel, maar alleen geldig voor door de operator beheerde warme leases  
  
GitHub Actions bereidt de kandidaat-checkout altijd voor vóór de VM-run. De pnpm-store wordt gecachet op OS, Node-versie en lockfile. De VM-source-run gebruikt ook `/var/cache/crabbox/pnpm` wanneer aanwezig.

## Timinginterpretatie

`mantis-slack-desktop-smoke-report.md` bevat fasetimings:

  * `crabbox.warmup`: cloudprovider-boot, desktop-/browsergereedheid en SSH.
  * `crabbox.inspect`: opzoeken van lease-metadata.
  * `credentials.prepare`: verkrijgen van een Convex-referentielease.
  * `crabbox.remote_run`: synchronisatie, browserstart, OpenClaw install/build of hydratatievalidatie, Gateway-start, screenshot en video-opname.
  * `artifacts.copy`: rsync terug vanaf de VM.


`crabbox.remote_run` kan als `accepted` worden gemarkeerd wanneer Crabbox een niet-nul externe status teruggeeft nadat Mantis metadata heeft gekopieerd die bewijst dat de OpenClaw Gateway actief is en de setup is voltooid. Behandel `accepted` als geslaagd-met-uitleg, niet als een mislukt scenario.

Als de run traag is:

  * warmup domineert: bak vooraf of promoot een betere Crabbox provider-image;
  * remote_run domineert in `source`: gebruik een warme lease, verbeter hergebruik van de pnpm-store, of verplaats machinevereisten naar de provider-image;
  * remote_run domineert in `prehydrated`: de externe werkruimte was niet echt klaar, of de Gateway/browser/Slack-setup is traag;
  * artefactkopie domineert: inspecteer videogrootte en de inhoud van de artefactmap.


## Bewijschecklist

Een goed PR-commentaar moet tonen:

  * scenario-id en kandidaat-SHA;
  * GitHub Actions-run-URL;
  * artefact-URL;
  * inline screenshot;
  * inline geanimeerde preview wanneer beschikbaar;
  * volledige MP4- en ingekorte MP4-links;
  * pass/fail-status;
  * timingsamenvatting in het bijgevoegde rapport.


Commit geen screenshots of video's naar de repository. Bewaar ze in GitHub Actions-artefacten of het PR-commentaar.

## Foutafhandeling

Als de workflow faalt vóór de VM-run, inspecteer dan eerst de Actions-job. Typische oorzaken zijn een niet-vertrouwde `candidate_ref`, ontbrekende omgevingsgeheimen of een mislukte install/build van de kandidaat.

Als de VM-run faalt maar screenshots zijn teruggekopieerd, inspecteer:

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

Als de run de lease heeft behouden, open dan VNC met de `crabbox vnc ...`-opdracht uit het rapport. Stop de lease wanneer je klaar bent:

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

Als de Slack-login is verlopen, herstel die dan in VNC op een behouden lease en voer opnieuw uit met `--lease-id`. Bak dat browserprofiel niet in een provider-image.

## Gerelateerd

  * [QA-overzicht](</nl/concepts/qa-e2e-automation>)
  * [Slack-kanaal](</nl/channels/slack>)
  * [Testen](</nl/help/testing>)


Was this useful?YesNo