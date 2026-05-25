---
title: Attività LLM
source_url: https://docs.openclaw.ai/it/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` è uno **strumento Plugin opzionale** che esegue un'attività LLM solo JSON e restituisce un output strutturato (facoltativamente validato rispetto a JSON Schema).

È ideale per motori di workflow come Lobster: puoi aggiungere un singolo passaggio LLM senza scrivere codice OpenClaw personalizzato per ogni workflow.

## Abilita il Plugin

  1. Abilita il Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Consenti lo strumento opzionale:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Usa `tools.allow` solo quando vuoi la modalità allowlist restrittiva.

## Configurazione (opzionale)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` è una allowlist di stringhe `provider/model`. Se impostata, qualsiasi richiesta fuori dall'elenco viene rifiutata.

## Parametri dello strumento

  * `prompt` (stringa, obbligatorio)
  * `input` (qualsiasi, opzionale)
  * `schema` (oggetto, JSON Schema opzionale)
  * `provider` (stringa, opzionale)
  * `model` (stringa, opzionale)
  * `thinking` (stringa, opzionale)
  * `authProfileId` (stringa, opzionale)
  * `temperature` (numero, opzionale)
  * `maxTokens` (numero, opzionale)
  * `timeoutMs` (numero, opzionale)


`thinking` accetta i preset di ragionamento standard di OpenClaw, come `low` o `medium`.

## Risultato

Restituisce `details.json` contenente il JSON analizzato (e lo valida rispetto a `schema` quando fornito).

## Esempio: passaggio di workflow Lobster

### Limitazione importante

L'esempio seguente presume che la **CLI Lobster standalone** sia in esecuzione in un ambiente in cui `openclaw.invoke` ha già l'URL del Gateway e il contesto di autenticazione corretti.

Per il runner Lobster **incorporato** incluso in OpenClaw, questo pattern di CLI annidata **non è attualmente affidabile** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Finché Lobster incorporato non avrà un bridge supportato per questo flusso, preferisci una delle seguenti opzioni:

  * chiamate dirette allo strumento `llm-task` fuori da Lobster, oppure
  * passaggi Lobster che non dipendono da chiamate `openclaw.invoke` annidate.


Esempio di CLI Lobster standalone:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Note sulla sicurezza

  * Lo strumento è **solo JSON** e istruisce il modello a produrre solo JSON (nessun blocco di codice, nessun commento).
  * Nessuno strumento viene esposto al modello per questa esecuzione.
  * Tratta l'output come non attendibile, a meno che tu non lo validi con `schema`.
  * Inserisci le approvazioni prima di qualsiasi passaggio con effetti collaterali (send, post, exec).


## Correlati

  * [Livelli di ragionamento](</it/tools/thinking>)
  * [Sub-agenti](</it/tools/subagents>)
  * [Comandi slash](</it/tools/slash-commands>)


Was this useful?YesNo