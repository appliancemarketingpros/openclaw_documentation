---
title: Modalità elevata
source_url: https://docs.openclaw.ai/it/tools/elevated
scraped_at: 2026-05-25
---

Quando un agent viene eseguito dentro una sandbox, i suoi comandi `exec` sono confinati all'ambiente sandbox. La **modalità elevata** consente all'agent di uscire ed eseguire invece comandi fuori dalla sandbox, con gate di approvazione configurabili.

## Direttive

Controlla la modalità elevata per sessione con comandi slash:

Direttiva | Cosa fa  
---|---  
`/elevated on` | Esegue fuori dalla sandbox sul percorso host configurato, mantenendo le approvazioni  
`/elevated ask` | Uguale a `on` (alias)  
`/elevated full` | Esegue fuori dalla sandbox sul percorso host configurato e salta le approvazioni  
`/elevated off` | Torna all'esecuzione confinata nella sandbox  
  
Disponibile anche come `/elev on|off|ask|full`.

Invia `/elevated` senza argomento per vedere il livello corrente.

## Come funziona

* ### Verifica la disponibilità

La modalità elevata deve essere abilitata nella configurazione e il mittente deve essere nell'allowlist:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Imposta il livello

Invia un messaggio contenente solo la direttiva per impostare il valore predefinito della sessione:

CodeCopy code
[code]
    /elevated full
[/code]

Oppure usala inline (si applica solo a quel messaggio):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### I comandi vengono eseguiti fuori dalla sandbox

Con la modalità elevata attiva, le chiamate `exec` escono dalla sandbox. L'host effettivo è `gateway` per impostazione predefinita, oppure `node` quando la destinazione exec configurata/di sessione è `node`. In modalità `full`, le approvazioni exec vengono saltate. In modalità `on`/`ask`, le regole di approvazione configurate continuano ad applicarsi.

## Ordine di risoluzione

  1. **Direttiva inline** nel messaggio (si applica solo a quel messaggio)
  2. **Override di sessione** (impostato inviando un messaggio contenente solo la direttiva)
  3. **Predefinito globale** (`agents.defaults.elevatedDefault` nella configurazione)


## Disponibilità e allowlist

  * **Gate globale** : `tools.elevated.enabled` (deve essere `true`)
  * **Allowlist mittente** : `tools.elevated.allowFrom` con elenchi per canale
  * **Gate per agent** : `agents.list[].tools.elevated.enabled` (può solo restringere ulteriormente)
  * **Allowlist per agent** : `agents.list[].tools.elevated.allowFrom` (il mittente deve corrispondere sia a quella globale sia a quella per agent)
  * **Fallback Discord** : se `tools.elevated.allowFrom.discord` viene omesso, `channels.discord.allowFrom` viene usato come fallback
  * **Tutti i gate devono passare** ; altrimenti la modalità elevata viene trattata come non disponibile


Formati delle voci allowlist:

Prefisso | Corrisponde a  
---|---  
(nessuno) | ID mittente, E.164 o campo From  
`name:` | Nome visualizzato del mittente  
`username:` | Nome utente del mittente  
`tag:` | Tag del mittente  
`id:`, `from:`, `e164:` | Targeting esplicito dell'identità  
  
## Cosa non controlla la modalità elevata

  * **Policy degli strumenti** : se `exec` viene negato dalla policy degli strumenti, la modalità elevata non può ignorarla.
  * **Policy di selezione dell'host** : la modalità elevata non trasforma `auto` in un override libero tra host. Usa le regole della destinazione exec configurata/di sessione, scegliendo `node` solo quando la destinazione è già `node`.
  * **Separata da`/exec`**: la direttiva `/exec` regola i valori predefiniti exec per sessione per i mittenti autorizzati e non richiede la modalità elevata.


## Correlati

[**Strumento exec** Esecuzione di comandi shell dall'agent. ](</it/tools/exec>) [**Approvazioni exec** Sistema di approvazioni e allowlist per `exec`. ](</it/tools/exec-approvals>) [**Sandboxing** Configurazione della sandbox a livello Gateway. ](</it/gateway/sandboxing>) [**Sandbox vs policy degli strumenti vs modalità elevata** Come i tre gate si combinano durante una chiamata strumento. ](</it/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo