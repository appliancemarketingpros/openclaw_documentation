---
title: LongCat
source_url: https://docs.openclaw.ai/it/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) fornisce un'API ospitata per LongCat-2.0, un modello di ragionamento progettato per la programmazione e i carichi di lavoro agentici. OpenClaw fornisce il plugin `longcat` ufficiale per l'endpoint compatibile con OpenAI di LongCat.

Proprietà | Valore  
---|---  
Fornitore | `longcat`  
Autenticazione | `LONGCAT_API_KEY`  
API | Chat Completions compatibile con OpenAI  
URL di base | `https://api.longcat.chat/openai`  
Modello | `longcat/LongCat-2.0`  
Contesto | 1.048.576 token  
Output massimo | 131.072 token  
Input | Testo  
  
## Installare il plugin

Installa il pacchetto ufficiale, quindi riavvia il Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Guida introduttiva

* ### Creare una chiave API

Accedi alla [piattaforma API LongCat](<https://longcat.chat/platform/>) e crea una chiave nella pagina [Chiavi API](<https://longcat.chat/platform/api_keys>).

* ### Eseguire la configurazione iniziale

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Verificare il modello

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

La configurazione iniziale aggiunge il catalogo ospitato e seleziona `longcat/LongCat-2.0` quando non è già configurato alcun modello principale.

### Configurazione non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Comportamento del ragionamento

LongCat offre un controllo binario del ragionamento. OpenClaw associa i livelli di ragionamento abilitati a `thinking: { type: "enabled" }` e `/think off` a `thinking: { type: "disabled" }`. Attualmente LongCat non documenta `reasoning_effort`, pertanto OpenClaw non lo invia.

LongCat restituisce il ragionamento in `reasoning_content`. OpenClaw conserva questo campo quando riproduce i turni delle chiamate agli strumenti dell'assistente, affinché le sessioni agentiche multi-turno mantengano il formato dei messaggi previsto dal fornitore.

## Prezzi

Il catalogo integrato utilizza i prezzi di listino a consumo di LongCat, espressi in USD per milione di token: 0,75 $ per l'input non memorizzato nella cache, 0,015 $ per l'input memorizzato nella cache e 2,95 $ per l'output. LongCat può offrire sconti temporanei; la [pagina dei prezzi](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) e i tuoi dati di fatturazione sono le fonti autorevoli.

## LongCat-2.0 in hosting autonomo

Il fornitore `longcat` è destinato all'API ospitata di LongCat. Per i pesi aperti disponibili su [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), esegui il modello tramite un runtime compatibile con OpenAI e utilizza invece il fornitore [vLLM](</it/providers/vllm>) o [SGLang](</it/providers/sglang>) già disponibile in OpenClaw.

Mantieni l'identificatore esatto del modello usato dal runtime nel catalogo del fornitore in hosting autonomo; non instradare una distribuzione locale tramite `longcat/LongCat-2.0`.

## Risoluzione dei problemi

La chiave funziona in una shell ma non nel Gateway

I processi Gateway gestiti dal demone non ereditano tutte le variabili della shell interattiva. Inserisci `LONGCAT_API_KEY` in `~/.openclaw/.env`, configurala tramite la configurazione iniziale oppure usa un riferimento a un segreto approvato.

Le richieste non riescono con 402 o 429

`402` indica che l'account non dispone di una quota di token sufficiente. `429` indica che la chiave API ha raggiunto un limite di frequenza. Controlla l'[utilizzo di LongCat](<https://longcat.chat/platform/usage>) e riprova le richieste soggette al limite di frequenza dopo l'intervallo di attesa del fornitore.

Il modello non viene visualizzato

Esegui `openclaw plugins list` e verifica che il plugin `longcat` sia abilitato, quindi esegui `openclaw models list --provider longcat`.

## Contenuti correlati

[**Fornitori di modelli** Configurazione dei fornitori, riferimenti ai modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Documentazione dell'API LongCat** Endpoint dell'API ospitata, autenticazione, limiti ed esempi. ](<https://longcat.chat/platform/docs/>) [**Scheda del modello LongCat-2.0** Architettura, indicazioni per la distribuzione e dettagli del modello. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Segreti** Archivia le credenziali del fornitore senza incorporare testo non cifrato nella configurazione. ](</it/gateway/secrets>)

Was this useful?YesNo

Open issue