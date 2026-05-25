---
title: Agentinitialisatie
source_url: https://docs.openclaw.ai/nl/start/bootstrapping
scraped_at: 2026-05-25
---

Bootstrapping is het **eerste-start** ritueel dat een agentworkspace voorbereidt en identiteitsgegevens verzamelt. Dit gebeurt na de onboarding, wanneer de agent voor het eerst start.

## Wat bootstrapping doet

Bij de eerste agentrun voert OpenClaw bootstrapping uit voor de workspace (standaard `~/.openclaw/workspace`):

  * Plaatst initiële versies van `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Voert een kort vraag-en-antwoordritueel uit (één vraag tegelijk).
  * Schrijft identiteit en voorkeuren naar `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Verwijdert `BOOTSTRAP.md` na afronding, zodat het slechts één keer wordt uitgevoerd.


Voor ingebedde/lokale modelruns houdt OpenClaw `BOOTSTRAP.md` buiten de bevoorrechte systeemcontext. Bij de primaire interactieve eerste run geeft het de bestandsinhoud nog steeds mee in de gebruikersprompt, zodat modellen die de `read`-tool niet betrouwbaar aanroepen het ritueel kunnen voltooien. Als de huidige run niet veilig toegang kan krijgen tot de workspace, krijgt de agent een beperkte bootstrapnotitie in plaats van een algemene begroeting.

## Bootstrapping overslaan

Voer `openclaw onboard --skip-bootstrap` uit om dit over te slaan voor een vooraf gevulde workspace.

## Waar het wordt uitgevoerd

Bootstrapping wordt altijd uitgevoerd op de **Gateway-host**. Als de macOS-app verbinding maakt met een externe Gateway, staan de workspace en bootstrappingbestanden op die externe machine.

## Gerelateerde documentatie

  * Onboarding van de macOS-app: [Onboarding](</nl/start/onboarding>)
  * Workspace-indeling: [Agentworkspace](</nl/concepts/agent-workspace>)


Was this useful?YesNo