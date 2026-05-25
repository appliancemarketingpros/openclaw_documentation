---
title: Gateway Kilo
source_url: https://docs.openclaw.ai/it/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway fornisce un'**API unificata** che instrada le richieste a molti modelli dietro un singolo endpoint e una chiave API. È compatibile con OpenAI, quindi la maggior parte degli SDK OpenAI funziona cambiando l'URL di base.

Proprietà | Valore  
---|---  
Fornitore | `kilocode`  
Autenticazione | `KILOCODE_API_KEY`  
API | Compatibile con OpenAI  
URL di base | `https://api.kilo.ai/api/gateway/`  
  
## Per iniziare

* ### Crea un account

Vai su [app.kilo.ai](<https://app.kilo.ai>), accedi o crea un account, quindi vai a Chiavi API e genera una nuova chiave.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Oppure imposta direttamente la variabile di ambiente:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Modello predefinito

Il modello predefinito è `kilocode/kilo/auto`, un modello di instradamento intelligente gestito dal fornitore e amministrato da Kilo Gateway.

## Catalogo integrato

OpenClaw rileva dinamicamente i modelli disponibili da Kilo Gateway all'avvio. Usa `/models kilocode` per vedere l'elenco completo dei modelli disponibili con il tuo account.

Qualsiasi modello disponibile sul Gateway può essere usato con il prefisso `kilocode/`:

Riferimento modello | Note  
---|---  
`kilocode/kilo/auto` | Predefinito — instradamento intelligente  
`kilocode/anthropic/claude-sonnet-4` | Anthropic tramite Kilo  
`kilocode/openai/gpt-5.5` | OpenAI tramite Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google tramite Kilo  
...e molti altri | Usa `/models kilocode` per elencarli tutti  
  
## Esempio di configurazione

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Trasporto e compatibilità

Kilo Gateway è documentato nel codice sorgente come compatibile con OpenRouter, quindi rimane sul percorso proxy compatibile con OpenAI invece di usare la modellazione nativa delle richieste OpenAI.

  * I riferimenti Kilo basati su Gemini rimangono sul percorso proxy-Gemini, quindi OpenClaw mantiene lì la sanitizzazione delle firme di pensiero Gemini senza abilitare la validazione della riproduzione Gemini nativa o le riscritture bootstrap.
  * Kilo Gateway usa internamente un token Bearer con la tua chiave API.

Wrapper di stream e ragionamento

Il wrapper di stream condiviso di Kilo aggiunge l'header dell'app del fornitore e normalizza i payload di ragionamento proxy per i riferimenti a modelli concreti supportati.

Risoluzione dei problemi

  * Se il rilevamento dei modelli non riesce all'avvio, OpenClaw ripiega sul catalogo statico incluso contenente `kilocode/kilo/auto`.
  * Conferma che la tua chiave API sia valida e che il tuo account Kilo abbia i modelli desiderati abilitati.
  * Quando il Gateway viene eseguito come daemon, assicurati che `KILOCODE_API_KEY` sia disponibile per quel processo (ad esempio in `~/.openclaw/.env` o tramite `env.shellEnv`).


## Correlati

[**Selezione del modello** Scelta dei fornitori, dei riferimenti modello e del comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento di configurazione** Riferimento completo della configurazione di OpenClaw. ](</it/gateway/configuration-reference>) [**Kilo Gateway** Dashboard, chiavi API e gestione dell'account di Kilo Gateway. ](<https://app.kilo.ai>)

Was this useful?YesNo