---
title: Architettura del runtime degli agenti
source_url: https://docs.openclaw.ai/it/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw possiede direttamente il runtime dell'agente integrato. Il codice del runtime si trova in `src/agents/`, gli helper per modelli/provider si trovano in `src/llm/` e i contratti rivolti ai plugin sono esposti tramite i barrel `openclaw/plugin-sdk/*`.

## Layout del runtime

  * `src/agents/embedded-agent-runner/`: loop dei tentativi dell'agente integrato, adattatori di stream dei provider, Compaction, selezione del modello e cablaggio della sessione.
  * `src/agents/sessions/`: persistenza delle sessioni, caricamento delle estensioni, rilevamento delle risorse, Skills, prompt, temi e renderer degli strumenti basati su TUI.
  * `packages/agent-core/`: core agente riutilizzabile, tipi di harness di livello inferiore, messaggi, helper di Compaction, template di prompt e contratti di strumenti/sessione.
  * `src/agents/runtime/`: facade OpenClaw per `@openclaw/agent-core` più utilità proxy locali.
  * `src/agents/agent-tools*.ts`: definizioni degli strumenti di proprietà di OpenClaw, schemi, policy, adattatori di hook prima/dopo e supporto alle modifiche sull'host.
  * `src/agents/agent-hooks/`: hook del runtime integrati come salvaguardie di Compaction e potatura del contesto.
  * `src/llm/`: registro di modelli/provider, helper di trasporto e implementazioni di stream specifiche dei provider.


## Confini

Il codice core chiama il runtime integrato tramite moduli OpenClaw e barrel SDK, non tramite vecchi pacchetti agente esterni. I Plugin usano gli entrypoint documentati `openclaw/plugin-sdk/*` e non importano elementi interni di `src/**`.

`@earendil-works/pi-tui` rimane una dipendenza TUI di terze parti. È usata come toolkit di componenti terminale dal TUI locale e dai renderer di sessione; internalizzarla sarebbe un intervento separato di vendoring.

## Manifest

I pacchetti di risorse dichiarano le risorse OpenClaw nei metadati del pacchetto:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

Il package manager rileva anche le directory convenzionali `extensions/`, `skills/`, `prompts/` e `themes/`.

## Selezione del runtime

L'id del runtime integrato predefinito è `openclaw`. Gli harness dei Plugin possono registrare ulteriori id di runtime. `auto` seleziona un harness Plugin compatibile quando ne esiste uno e altrimenti usa il runtime OpenClaw integrato.

## Correlati

  * [Workflow del runtime agente OpenClaw](</it/openclaw-agent-runtime>)
  * [Runtime agente](</it/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue