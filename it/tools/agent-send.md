---
title: Invio dell'agente
source_url: https://docs.openclaw.ai/it/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` esegue un singolo turno dell'agente dalla riga di comando senza richiedere un messaggio di chat in ingresso. Usalo per workflow con script, test e consegna programmatica.

## Avvio rapido

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Questo invia il messaggio tramite il Gateway e stampa la risposta.

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Flag

Flag | Descrizione  
---|---  
`--message \<text\>` | Messaggio da inviare (obbligatorio)  
`--to \<dest\>` | Deriva la chiave di sessione da una destinazione (telefono, id chat)  
`--agent \<id\>` | Indirizza un agente configurato (usa la sua sessione `main`)  
`--session-id \<id\>` | Riutilizza una sessione esistente per id  
`--local` | Forza il runtime incorporato locale (salta il Gateway)  
`--deliver` | Invia la risposta a un canale di chat  
`--channel \<name\>` | Canale di consegna (whatsapp, telegram, discord, slack, ecc.)  
`--reply-to \<target\>` | Override della destinazione di consegna  
`--reply-channel \<name\>` | Override del canale di consegna  
`--reply-account \<id\>` | Override dell'id account di consegna  
`--thinking \<level\>` | Imposta il livello di ragionamento per il profilo modello selezionato  
`--verbose \<on|full|off\>` | Imposta il livello di verbosità  
`--timeout \<seconds\>` | Override del timeout dell'agente  
`--json` | Restituisce JSON strutturato  
  
## Comportamento

  * Per impostazione predefinita, la CLI passa **tramite il Gateway**. Aggiungi `--local` per forzare il runtime incorporato sulla macchina corrente.
  * Se il Gateway non è raggiungibile, la CLI **ripiega** sull'esecuzione incorporata locale.
  * Selezione della sessione: `--to` deriva la chiave di sessione (i target di gruppo/canale preservano l'isolamento; le chat dirette convergono su `main`).
  * I flag di ragionamento e verbosità persistono nello store delle sessioni.
  * Output: testo normale per impostazione predefinita, oppure `--json` per payload + metadati strutturati.
  * Con `--json --deliver`, il JSON include lo stato di consegna per invii riusciti, soppressi, parziali e non riusciti. Vedi [stato di consegna JSON](</it/cli/agent#json-delivery-status>).


## Esempi

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Correlati

[**Agent CLI reference** Riferimento completo per flag e opzioni di `openclaw agent`. ](</it/cli/agent>) [**Sub-agents** Avvio di sotto-agenti in background. ](</it/tools/subagents>) [**Sessions** Come funzionano le chiavi di sessione e come `--to`, `--agent` e `--session-id` le risolvono. ](</it/concepts/session>) [**Slash commands** Catalogo dei comandi nativi usati nelle sessioni degli agenti. ](</it/tools/slash-commands>)

Was this useful?YesNo