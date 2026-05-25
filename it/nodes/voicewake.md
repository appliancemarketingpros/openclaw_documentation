---
title: Attivazione vocale
source_url: https://docs.openclaw.ai/it/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw tratta le **parole di attivazione come un unico elenco globale** gestito dal **Gateway**.

  * Non esistono **parole di attivazione personalizzate per nodo**.
  * **Qualsiasi interfaccia utente di nodo/app può modificare** l'elenco; le modifiche vengono mantenute dal Gateway e trasmesse a tutti.
  * macOS e iOS mantengono toggle locali per **abilitare/disabilitare Voice Wake** (UX locale + autorizzazioni diverse).
  * Android attualmente mantiene Voice Wake disattivato e usa un flusso microfono manuale nella scheda Voce.


## Archiviazione (host Gateway)

Le parole di attivazione sono archiviate sulla macchina del gateway in:

  * `~/.openclaw/settings/voicewake.json`


Forma:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Protocollo

### Metodi

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` con parametri `{ triggers: string[] }` → `{ triggers: string[] }`


Note:

  * I trigger vengono normalizzati (spazi rimossi, valori vuoti scartati). Gli elenchi vuoti ripristinano i valori predefiniti.
  * Per sicurezza vengono applicati limiti (numero/lunghezza massimi).


### Metodi di routing (trigger → destinazione)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` con parametri `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Forma di `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Le destinazioni delle route supportano esattamente una tra:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Eventi

  * payload `voicewake.changed` `{ triggers: string[] }`
  * payload `voicewake.routing.changed` `{ config: VoiceWakeRoutingConfig }`


Chi lo riceve:

  * Tutti i client WebSocket (app macOS, WebChat, ecc.)
  * Tutti i nodi connessi (iOS/Android), e anche alla connessione del nodo come push iniziale dello "stato corrente".


## Comportamento del client

### App macOS

  * Usa l'elenco globale per controllare i trigger di `VoiceWakeRuntime`.
  * La modifica di "Parole trigger" nelle impostazioni di Voice Wake chiama `voicewake.set` e poi si affida alla trasmissione per mantenere sincronizzati gli altri client.


### Nodo iOS

  * Usa l'elenco globale per il rilevamento dei trigger di `VoiceWakeManager`.
  * La modifica delle parole di attivazione nelle Impostazioni chiama `voicewake.set` (tramite il WS del Gateway) e mantiene reattivo anche il rilevamento locale delle parole di attivazione.


### Nodo Android

  * Voice Wake è attualmente disabilitato nel runtime/nelle Impostazioni di Android.
  * La voce Android usa l'acquisizione microfono manuale nella scheda Voce invece dei trigger con parole di attivazione.


## Correlati

  * [Modalità Talk](</it/nodes/talk>)
  * [Audio e note vocali](</it/nodes/audio>)
  * [Comprensione dei media](</it/nodes/media-understanding>)


Was this useful?YesNo