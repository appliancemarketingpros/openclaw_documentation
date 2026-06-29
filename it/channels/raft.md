---
title: Raft
source_url: https://docs.openclaw.ai/it/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Il supporto Raft collega un agente OpenClaw a un agente esterno Raft tramite la CLI Raft locale. Raft invia segnali di risveglio autenticati al Gateway. L'agente quindi usa la CLI Raft per controllare e inviare messaggi.

## Installazione

Raft è un Plugin esterno ufficiale. Installalo sull'host del Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Dettagli: [Plugin](</it/tools/plugin>)

## Prerequisiti

  * Un workspace Raft con un agente esterno.
  * La CLI Raft installata sullo stesso host del Gateway OpenClaw.
  * Un profilo della CLI Raft che ha già effettuato l'accesso ed è associato a quell'agente esterno.


Il Plugin non memorizza le credenziali Raft. La CLI Raft conserva tale autenticazione nel proprio profilo.

## Configurazione

Imposta il profilo nella configurazione:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Per l'account predefinito, puoi invece impostare `RAFT_PROFILE` nell'ambiente del Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Usa un account con nome quando un Gateway si collega a più di un agente esterno Raft:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Il flusso di configurazione interattiva registra lo stesso profilo:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Come funziona

Quando il Gateway si avvia, il Plugin:

  1. Apre un endpoint HTTP di risveglio solo loopback su una porta effimera.
  2. Avvia `raft --profile <profile> agent bridge` con quell'endpoint e un token per processo.
  3. Accetta solo segnali di risveglio autenticati, senza contenuto e con un'identità di replay dal bridge locale.
  4. Richiede uno tra `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` o `id`.
  5. Deduplica le consegne di risveglio recenti ritentate in base all'id evento del bridge, anche tra riavvii del Gateway.
  6. Restituisce una sessione runtime stabile per il bridge corrente e un batch di svuotamento attività vuoto per il protocollo della CLI Raft.
  7. Avvia un turno serializzato dell'agente OpenClaw per ogni risveglio accettato.


Il bridge gestisce i nuovi tentativi di consegna e le riconnessioni di Raft. Il turno OpenClaw riceve solo una notifica di risveglio, non una copia del corpo del messaggio Raft. Usa la CLI per leggere i messaggi in sospeso e per inviare la propria risposta:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Verifica

Controlla che OpenClaw riesca a trovare la CLI e abbia un profilo configurato:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Poi invia un messaggio all'agente esterno Raft. Il log del Gateway dovrebbe mostrare l'avvio del bridge Raft, seguito da un risveglio in ingresso. L'agente dovrebbe usare il profilo Raft configurato per controllare i messaggi in sospeso.

## Risoluzione dei problemi

La CLI Raft è mancante

Installa la CLI Raft sull'host del Gateway e rendi `raft` disponibile nel `PATH` del servizio. Verificala con `raft --help`, quindi riavvia il Gateway.

Il bridge termina immediatamente

Verifica che il profilo configurato abbia effettuato l'accesso e appartenga all'agente esterno Raft previsto. Esegui direttamente `raft --profile <profile> agent bridge` per vedere la diagnostica della CLI.

Arriva un risveglio ma non viene inviata alcuna risposta Raft

Questo è previsto quando l'agente non invoca la CLI Raft. Il bridge di risveglio non trasporta corpi dei messaggi né risposte finali automatiche. Controlla la policy degli strumenti dell'agente e assicurati che possa eseguire `raft --profile <profile> message check` e `message send`.

## Riferimenti

  * [Raft](<https://raft.build/>)
  * [Documentazione Raft](<https://docs.raft.build/welcome/>)
  * [Integrazione Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue