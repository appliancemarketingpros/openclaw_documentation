---
title: Rimozione di BlueBubbles e percorso imsg per iMessage
source_url: https://docs.openclaw.ai/it/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Rimozione di BlueBubbles e percorso iMessage tramite imsg

OpenClaw non distribuisce più il canale BlueBubbles. Il supporto iMessage ora passa attraverso il plugin `imessage` incluso, che avvia [`imsg`](<https://github.com/steipete/imsg>) localmente o tramite un wrapper SSH e comunica in JSON-RPC su stdin/stdout.

Se la tua configurazione contiene ancora `channels.bluebubbles`, migrala a `channels.imessage`. Il vecchio URL della documentazione `/channels/bluebubbles` reindirizza a [Provenienza da BlueBubbles](</it/channels/imessage-from-bluebubbles>), che contiene la tabella completa di traduzione della configurazione e la checklist di cutover.

## Cosa è cambiato

  * Nel percorso iMessage supportato da OpenClaw non ci sono server HTTP BlueBubbles, route webhook, password REST o runtime del plugin BlueBubbles.
  * OpenClaw legge e osserva Messages tramite `imsg` sul Mac in cui Messages.app ha effettuato l’accesso.
  * Invio, ricezione, cronologia e media di base usano le normali superfici `imsg` e i permessi macOS.
  * Azioni avanzate come risposte in thread, tapback, modifica, annullamento dell’invio, effetti, conferme di lettura, indicatori di digitazione e gestione dei gruppi richiedono `imsg launch` con il bridge API privato disponibile.
  * I Gateway Linux e Windows possono ancora usare iMessage impostando `channels.imessage.cliPath` su un wrapper SSH che esegue `imsg` sul Mac con accesso effettuato.


## Cosa fare

  1. Installa e verifica `imsg` sul Mac con Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Concedi i permessi Accesso completo al disco e Automazione al contesto di processo che esegue `imsg` e OpenClaw.

  3. Traduci la vecchia configurazione:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Riavvia il Gateway e verifica:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Testa DM, gruppi, allegati e qualsiasi azione API privata da cui dipendi prima di eliminare il vecchio server BlueBubbles.


## Note di migrazione

  * `channels.bluebubbles.serverUrl` e `channels.bluebubbles.password` non hanno equivalenti iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, radici degli allegati, limiti di dimensione dei media, chunking e toggle delle azioni hanno equivalenti iMessage.
  * `channels.imessage.includeAttachments` è ancora disattivato per impostazione predefinita. Impostalo esplicitamente se prevedi che foto, memo vocali, video o file in ingresso raggiungano l’agente.
  * Con `groupPolicy: "allowlist"`, copia il vecchio blocco `groups`, inclusa qualsiasi voce wildcard `"*"`. Le allowlist dei mittenti dei gruppi e il registro dei gruppi sono gate separati.
  * I binding ACP che corrispondevano a `channel: "bluebubbles"` devono essere modificati in `channel: "imessage"`.
  * Le vecchie chiavi di sessione BlueBubbles non diventano chiavi di sessione iMessage. Le approvazioni di abbinamento vengono trasferite per handle, ma la cronologia delle conversazioni sotto le chiavi di sessione BlueBubbles no.


## Vedi anche

  * [Provenienza da BlueBubbles](</it/channels/imessage-from-bluebubbles>)
  * [iMessage](</it/channels/imessage>)
  * [Riferimento di configurazione - iMessage](</it/gateway/config-channels#imessage>)


Was this useful?YesNo