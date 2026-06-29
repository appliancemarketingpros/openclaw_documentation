---
title: Pacchetto di benchmark per agente personale
source_url: https://docs.openclaw.ai/it/concepts/personal-agent-benchmark-pack
scraped_at: 2026-06-29
---

AgentsFundamentals

Il Personal Agent Benchmark Pack è un piccolo pacchetto di scenari QA supportato da repo per workflow di assistente personale locale. Non è un benchmark generico per modelli e non richiede un nuovo runner. Il pacchetto riutilizza lo stack QA privato descritto in [Panoramica QA](</it/concepts/qa-e2e-automation>), il [canale QA](</it/channels/qa-channel>) sintetico e il catalogo YAML `qa/scenarios` esistente.

Il primo pacchetto è intenzionalmente ristretto:

  * promemoria personali fittizi tramite consegna Cron locale
  * routing fittizio di DM e risposte nei thread tramite `qa-channel`
  * richiamo fittizio delle preferenze dai file di memoria temporanei dell'area di lavoro QA
  * controlli fittizi di non eco dei segreti
  * prosecuzione sicura degli strumenti basata su lettura dopo un breve turno in stile approvazione
  * comportamento di arresto al rifiuto dell'approvazione per una richiesta sensibile di lettura locale
  * report dello stato delle attività basato su prove che mantiene separati in sospeso, bloccato e completato
  * artefatti diagnostici sicuri per la condivisione che mantengono uno stato utile omettendo i contenuti personali grezzi
  * affermazioni di completamento basate su prove che evitano falsi avanzamenti prima che esistano evidenze locali
  * recupero dagli errori che segnala lo stato parziale e mantiene chiari i confini dei tentativi


## Scenari

I metadati del pacchetto leggibili dalla macchina si trovano in `extensions/qa-lab/src/scenario-packs.ts`. Esegui il pacchetto con `--pack personal-agent`:

bashCopy code
[code]
    OPENCLAW_ENABLE_PRIVATE_QA_CLI=1 pnpm openclaw qa suite \  --provider-mode mock-openai \  --pack personal-agent \  --concurrency 1
[/code]

`--pack` è additivo con flag `--scenario` ripetuti. Gli scenari espliciti vengono eseguiti per primi, poi gli scenari del pacchetto vengono eseguiti nell'ordine di `QA_PERSONAL_AGENT_SCENARIO_IDS` con i duplicati rimossi.

Il pacchetto è progettato per `qa-channel` con `mock-openai` o un'altra lane di provider QA locale. Non deve essere indirizzato a servizi di chat live o ad account personali reali.

## Modello di privacy

Gli scenari usano solo utenti fittizi, preferenze fittizie, segreti fittizi e l' area di lavoro Gateway QA temporanea creata dalla suite. Non devono leggere o scrivere memoria, sessioni, credenziali, agenti di avvio, configurazioni globali o stato Gateway live di utenti reali di OpenClaw.

Gli artefatti restano nella directory degli artefatti della suite QA esistente e devono essere trattati come output di test. I controlli di redazione usano marcatori fittizi, quindi gli errori sono sicuri da ispezionare e segnalare nelle issue.

## Estensione del pacchetto

Aggiungi nuovi casi `.yaml` in `qa/scenarios/personal/`, poi aggiungi l'id dello scenario a `QA_PERSONAL_AGENT_SCENARIO_IDS`. Mantieni ogni caso piccolo, locale, deterministico in `mock-openai` e focalizzato su un comportamento di assistente personale.

Buoni candidati di follow-up:

  * controlli sull'esportazione della traiettoria redatta
  * controlli sui workflow dei Plugin solo locali


Evita di aggiungere un nuovo runner, Plugin, dipendenza, trasporto live o giudice del modello finché il catalogo degli scenari non avrà abbastanza casi stabili da giustificare quella superficie.

Was this useful?YesNo

Open issue