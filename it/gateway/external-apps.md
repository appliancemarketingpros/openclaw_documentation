---
title: Integrazioni Gateway per app esterne
source_url: https://docs.openclaw.ai/it/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Le app esterne dovrebbero comunicare con OpenClaw tramite il protocollo Gateway oggi. Usa Gateway WebSocket e i metodi RPC quando uno script, una dashboard, un job CI, un'estensione IDE o un altro processo vuole avviare esecuzioni di agenti, trasmettere eventi in streaming, attendere i risultati, annullare il lavoro o ispezionare le risorse Gateway.

## Cosa è disponibile oggi

Superficie | Stato | Usala per  
---|---|---  
[Protocollo Gateway](</it/gateway/protocol>) | Pronto | Trasporto WebSocket, handshake di connessione, ambiti auth, versionamento del protocollo ed eventi.  
[Riferimento RPC Gateway](</it/reference/rpc>) | Pronto | Metodi Gateway correnti per agenti, sessioni, attività, modelli, strumenti, artefatti e approvazioni.  
[`openclaw agent`](</it/cli/agent>) | Pronto | Integrazione con script una tantum quando invocare la CLI è sufficiente.  
[`openclaw message`](</it/cli/message>) | Pronto | Invio di messaggi o azioni di canale da script.  
  
L'albero sorgente contiene lavoro su pacchetti interni per una futura libreria client, ma questa non è una superficie di installazione pubblica. Considerala un dettaglio di implementazione in anteprima finché i pacchetti non saranno pubblicati e versionati.

## Percorso consigliato

  1. Esegui o individua un Gateway.
  2. Connettiti tramite il [protocollo Gateway](</it/gateway/protocol>).
  3. Chiama i metodi RPC documentati dal [riferimento RPC Gateway](</it/reference/rpc>).
  4. Blocca la versione di OpenClaw rispetto alla quale esegui i test.
  5. Ricontrolla il riferimento RPC quando aggiorni OpenClaw.


Per le esecuzioni di agenti, inizia con l'RPC `agent` e abbinalo a `agent.wait` quando ti serve un risultato terminale. Per uno stato di conversazione duraturo, usa i metodi `sessions.*`. Per le integrazioni UI, sottoscrivi gli eventi Gateway e renderizza solo le famiglie di eventi che la tua app comprende.

## Codice app rispetto a codice Plugin

Usa Gateway RPC quando il codice vive fuori da OpenClaw:

  * script Node che avviano o osservano esecuzioni di agenti
  * job CI che chiamano un Gateway
  * dashboard e pannelli di amministrazione
  * estensioni IDE
  * bridge esterni che non devono diventare Plugin di canale
  * test di integrazione con trasporti Gateway finti o reali


Usa il Plugin SDK quando il codice viene eseguito dentro OpenClaw:

  * Plugin provider
  * Plugin di canale
  * hook di strumento o del ciclo di vita
  * Plugin di harness agente
  * helper runtime attendibili


Le app esterne non dovrebbero importare `openclaw/plugin-sdk/*`; quei sottopercorsi sono per Plugin caricati da OpenClaw.

## Correlati

  * [Protocollo Gateway](</it/gateway/protocol>)
  * [Riferimento RPC Gateway](</it/reference/rpc>)
  * [Comando CLI agent](</it/cli/agent>)
  * [Comando CLI message](</it/cli/message>)
  * [Loop agente](</it/concepts/agent-loop>)
  * [Runtime agente](</it/concepts/agent-runtimes>)
  * [Sessioni](</it/concepts/session>)
  * [Attività in background](</it/automation/tasks>)
  * [Agenti ACP](</it/tools/acp-agents>)
  * [Panoramica Plugin SDK](</it/plugins/sdk-overview>)


Was this useful?YesNo

Open issue