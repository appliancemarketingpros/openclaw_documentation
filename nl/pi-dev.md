---
title: Pi-ontwikkelworkflow
source_url: https://docs.openclaw.ai/nl/pi-dev
scraped_at: 2026-05-25
---

Een verstandige workflow voor werken aan de Pi-integratie in OpenClaw.

## Typechecking en linting

  * Standaard lokale gate: `pnpm check`
  * Build-gate: `pnpm build` wanneer de wijziging build-output, packaging of lazy-loading/modulegrenzen kan beïnvloeden
  * Volledige landing-gate voor Pi-zware wijzigingen: `pnpm check && pnpm test`


## Pi-tests uitvoeren

Voer de Pi-gerichte testset rechtstreeks uit met Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Om de live provider-oefening mee te nemen:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Dit dekt de belangrijkste Pi-unit-suites:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Handmatig testen

Aanbevolen flow:

  * Voer de Gateway uit in dev-modus: 
    * `pnpm gateway:dev`
  * Trigger de agent rechtstreeks: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Gebruik de TUI voor interactieve debugging: 
    * `pnpm tui`


Vraag voor tool-callgedrag om een `read`\- of `exec`-actie, zodat je tool-streaming en payload-afhandeling kunt zien.

## Reset naar een schone lei

State staat onder de OpenClaw-state-directory. De standaard is `~/.openclaw`. Als `OPENCLAW_STATE_DIR` is ingesteld, gebruik dan in plaats daarvan die directory.

Om alles te resetten:

  * `openclaw.json` voor configuratie
  * `agents/<agentId>/agent/auth-profiles.json` voor model-authprofielen (API-sleutels + OAuth)
  * `credentials/` voor provider-/kanaalstate die nog buiten de auth-profielopslag staat
  * `agents/<agentId>/sessions/` voor agentsessiegeschiedenis
  * `agents/<agentId>/sessions/sessions.json` voor de sessie-index
  * `sessions/` als legacy-paden bestaan
  * `workspace/` als je een lege workspace wilt


Als je alleen sessies wilt resetten, verwijder dan `agents/<agentId>/sessions/` voor die agent. Als je auth wilt behouden, laat dan `agents/<agentId>/agent/auth-profiles.json` en eventuele providerstate onder `credentials/` staan.

## Verwijzingen

  * [Testen](</nl/help/testing>)
  * [Aan de slag](</nl/start/getting-started>)


## Gerelateerd

  * [Pi-integratiearchitectuur](</nl/pi>)


Was this useful?YesNo