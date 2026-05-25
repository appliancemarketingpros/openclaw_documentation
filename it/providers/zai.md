---
title: Z.AI
source_url: https://docs.openclaw.ai/it/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) è la piattaforma API per i modelli **GLM**. Fornisce API REST per GLM e usa chiavi API per l'autenticazione. Crea la tua chiave API nella console [Z.AI](<http://Z.AI>). OpenClaw usa il provider `zai` con una chiave API [Z.AI](<http://Z.AI>).

  * Provider: `zai`
  * Autenticazione: `ZAI_API_KEY`
  * API: Chat Completions [Z.AI](<http://Z.AI>) (autenticazione Bearer)


## Per iniziare

### Endpoint rilevato automaticamente

**Ideale per:** la maggior parte degli utenti. OpenClaw rileva l'endpoint [Z.AI](<http://Z.AI>) corrispondente dalla chiave e applica automaticamente l'URL di base corretto.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verifica che il modello sia elencato

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Endpoint regionale esplicito

**Ideale per:** gli utenti che vogliono forzare uno specifico Coding Plan o una superficie API generale.

* ### Scegli l'opzione di onboarding corretta

bashCopy code
[code]
    # Coding Plan Global (consigliato per gli utenti di Coding Plan)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (regione Cina)openclaw onboard --auth-choice zai-coding-cn # API generaleopenclaw onboard --auth-choice zai-global # API generale CN (regione Cina)openclaw onboard --auth-choice zai-cn
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verifica che il modello sia elencato

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Catalogo integrato

OpenClaw distribuisce il catalogo del provider `zai` in bundle nel manifest del plugin, quindi l'elenco in sola lettura può mostrare le righe GLM note senza caricare il runtime del provider:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Il catalogo basato sul manifest attualmente include:

Riferimento modello | Note  
---|---  
`zai/glm-5.1` | Modello predefinito  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Configurazione avanzata

Risoluzione in avanti dei modelli GLM-5 sconosciuti

Gli id `glm-5*` sconosciuti continuano a risolversi in avanti sul percorso del provider in bundle sintetizzando metadati di proprietà del provider dal modello `glm-4.7` quando l'id corrisponde alla forma corrente della famiglia GLM-5.

Streaming delle chiamate agli strumenti

`tool_stream` è abilitato per impostazione predefinita per lo streaming delle chiamate agli strumenti [Z.AI](<http://Z.AI>). Per disabilitarlo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Ragionamento e ragionamento preservato

Il ragionamento [Z.AI](<http://Z.AI>) segue i controlli `/think` di OpenClaw. Con il ragionamento disattivato, OpenClaw invia `thinking: { type: "disabled" }` per evitare risposte che consumano il budget di output in `reasoning_content` prima del testo visibile.

Il ragionamento preservato è facoltativo perché [Z.AI](<http://Z.AI>) richiede che l'intero storico `reasoning_content` venga riprodotto, aumentando i token del prompt. Abilitalo per modello:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Quando è abilitato e il ragionamento è attivo, OpenClaw invia `thinking: { type: "enabled", clear_thinking: false }` e riproduce il precedente `reasoning_content` per la stessa trascrizione compatibile con OpenAI.

Gli utenti avanzati possono comunque sovrascrivere il payload esatto del provider con `params.extra_body.thinking`.

Comprensione delle immagini

Il plugin [Z.AI](<http://Z.AI>) in bundle registra la comprensione delle immagini.

Proprietà | Valore  
---|---  
Modello | `glm-4.6v`  
  
La comprensione delle immagini viene risolta automaticamente dall'autenticazione [Z.AI](<http://Z.AI>) configurata: non è necessaria alcuna configurazione aggiuntiva.

Dettagli di autenticazione

  * [Z.AI](<http://Z.AI>) usa l'autenticazione Bearer con la tua chiave API.
  * L'opzione di onboarding `zai-api-key` rileva automaticamente l'endpoint [Z.AI](<http://Z.AI>) corrispondente dal prefisso della chiave.
  * Usa le opzioni regionali esplicite (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) quando vuoi forzare una superficie API specifica.


## Correlati

[**Famiglia di modelli GLM** Panoramica della famiglia di modelli GLM. ](</it/providers/glm>) [**Selezione del modello** Scelta dei provider, dei riferimenti modello e del comportamento di failover. ](</it/concepts/model-providers>)

Was this useful?YesNo