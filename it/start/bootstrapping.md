---
title: Inizializzazione dell'agente
source_url: https://docs.openclaw.ai/it/start/bootstrapping
scraped_at: 2026-05-25
---

Il bootstrapping è il rituale di **primo avvio** che prepara l'area di lavoro di un agente e raccoglie i dettagli sull'identità. Avviene dopo l'onboarding, quando l'agente si avvia per la prima volta.

## Cosa fa il bootstrapping

Alla prima esecuzione dell'agente, OpenClaw esegue il bootstrap dell'area di lavoro (predefinita `~/.openclaw/workspace`):

  * Crea i file iniziali `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Esegue un breve rituale di domande e risposte (una domanda alla volta).
  * Scrive identità e preferenze in `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Rimuove `BOOTSTRAP.md` al termine, così viene eseguito una sola volta.


Per le esecuzioni con modelli incorporati/locali, OpenClaw mantiene `BOOTSTRAP.md` fuori dal contesto di sistema privilegiato. Nel primo avvio interattivo principale, passa comunque il contenuto del file nel prompt utente, così i modelli che non chiamano in modo affidabile lo strumento `read` possono completare il rituale. Se l'esecuzione corrente non può accedere in sicurezza all'area di lavoro, l'agente riceve una nota di bootstrap limitata invece di un saluto generico.

## Saltare il bootstrapping

Per saltarlo in un'area di lavoro già preconfigurata, esegui `openclaw onboard --skip-bootstrap`.

## Dove viene eseguito

Il bootstrapping viene sempre eseguito sull'**host del Gateway**. Se l'app macOS si connette a un Gateway remoto, l'area di lavoro e i file di bootstrapping si trovano su quella macchina remota.

## Documentazione correlata

  * Onboarding dell'app macOS: [Onboarding](</it/start/onboarding>)
  * Layout dell'area di lavoro: [Area di lavoro dell'agente](</it/concepts/agent-workspace>)


Was this useful?YesNo