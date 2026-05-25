---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/nl/platforms/mac/skills
scraped_at: 2026-05-25
---

De macOS-app toont OpenClaw Skills via de Gateway; hij parseert Skills niet lokaal.

## Gegevensbron

  * `skills.status` (Gateway) retourneert alle Skills plus geschiktheid en ontbrekende vereisten (inclusief blokkades via allowlists voor gebundelde Skills).
  * Vereisten worden afgeleid van `metadata.openclaw.requires` in elke `SKILL.md`.


## Installatieacties

  * `metadata.openclaw.install` definieert installatieopties (brew/node/go/uv).
  * De app roept `skills.install` aan om installatieprogramma's op de Gateway-host uit te voeren.
  * Ingebouwde `critical`-bevindingen voor gevaarlijke code blokkeren standaard `skills.install`; verdachte bevindingen geven nog steeds alleen een waarschuwing. De gevaarlijke override bestaat op het Gateway-verzoek, maar de standaard app-flow blijft fail-closed.
  * Als elke installatieoptie `download` is, toont de Gateway alle downloadkeuzes.
  * Anders kiest de Gateway één voorkeursinstallatieprogramma op basis van de huidige installatievoorkeuren en host-binaries: Homebrew eerst wanneer `skills.install.preferBrew` is ingeschakeld en `brew` bestaat, daarna `uv`, daarna de geconfigureerde node-manager uit `skills.install.nodeManager`, en daarna latere fallbacks zoals `go` of `download`.
  * Node-installatielabels weerspiegelen de geconfigureerde node-manager, inclusief `yarn`.


## Env-/API-sleutels

  * De app slaat sleutels op in `~/.openclaw/openclaw.json` onder `skills.entries.<skillKey>`.
  * `skills.update` patcht `enabled`, `apiKey` en `env`.


## Externe modus

  * Installatie- en configuratie-updates gebeuren op de Gateway-host (niet op de lokale Mac).


## Gerelateerd

  * [Skills](</nl/tools/skills>)
  * [macOS-app](</nl/platforms/macos>)


Was this useful?YesNo