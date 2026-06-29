---
title: Architectuur van de agentruntime
source_url: https://docs.openclaw.ai/nl/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw beheert de ingebouwde agentruntime rechtstreeks. De runtimecode staat onder `src/agents/`, model-/providerhelpers staan onder `src/llm/`, en Plugin-gerichte contracten worden beschikbaar gemaakt via `openclaw/plugin-sdk/*`-barrels.

## Runtimeindeling

  * `src/agents/embedded-agent-runner/`: ingebouwde agentpogingslus, providerstreamadapters, Compaction, modelselectie en sessiebedrading.
  * `src/agents/sessions/`: sessiepersistentie, laden van extensies, resourcedetectie, Skills, prompts, thema's en door TUI ondersteunde toolrenderers.
  * `packages/agent-core/`: herbruikbare agentkern, harness-typen op lager niveau, berichten, Compaction-helpers, prompttemplates en tool-/sessiecontracten.
  * `src/agents/runtime/`: OpenClaw-facade voor `@openclaw/agent-core` plus lokale proxyhulpprogramma's.
  * `src/agents/agent-tools*.ts`: door OpenClaw beheerde tooldefinities, schema's, beleid, adapters voor hooks voor/na, en ondersteuning voor hostbewerkingen.
  * `src/agents/agent-hooks/`: ingebouwde runtimehooks, zoals waarborgen voor Compaction en contextsnoei.
  * `src/llm/`: model-/providerregister, transporthelpers en providerspecifieke streamimplementaties.


## Grenzen

Core-code roept de ingebouwde runtime aan via OpenClaw-modules en SDK-barrels, niet via oude externe agentpakketten. Plugins gebruiken gedocumenteerde `openclaw/plugin-sdk/*`-entrypoints en importeren geen interne onderdelen uit `src/**`.

`@earendil-works/pi-tui` blijft een TUI-afhankelijkheid van derden. Het wordt gebruikt als toolkit voor terminalcomponenten door de lokale TUI en sessierenderers; het internaliseren ervan zou een afzonderlijke vendoring-inspanning zijn.

## Manifesten

Resourcepakketten declareren OpenClaw-resources in pakketmetadata:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

De pakketbeheerder ontdekt ook conventionele mappen `extensions/`, `skills/`, `prompts/` en `themes/`.

## Runtimeselectie

De standaard ingebouwde runtime-id is `openclaw`. Plugin-harnassen kunnen aanvullende runtime-id's registreren. `auto` selecteert een ondersteunend Plugin-harnas wanneer dat bestaat en gebruikt anders de ingebouwde OpenClaw-runtime.

## Gerelateerd

  * [Workflow voor de OpenClaw-agentruntime](</nl/openclaw-agent-runtime>)
  * [Agentruntimes](</nl/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue