---
title: Venice AI
source_url: https://docs.openclaw.ai/it/providers/venice
scraped_at: 2026-05-25
---

Venice AI offre **inferenza IA orientata alla privacy** con supporto per modelli non censurati e accesso ai principali modelli proprietari tramite il loro proxy anonimizzato. Tutta l'inferenza è privata per impostazione predefinita: nessun addestramento sui tuoi dati, nessuna registrazione.

## Perché Venice in OpenClaw

  * **Inferenza privata** per modelli open source (nessuna registrazione).
  * **Modelli non censurati** quando ne hai bisogno.
  * **Accesso anonimizzato** a modelli proprietari (Opus/GPT/Gemini) quando la qualità è importante.
  * Endpoint `/v1` compatibili con OpenAI.


## Modalità di privacy

Venice offre due livelli di privacy: comprenderli è fondamentale per scegliere il modello:

Modalità | Descrizione | Modelli  
---|---|---  
**Privata** | Completamente privata. Prompt/risposte **non vengono mai archiviati o registrati**. Effimera. | Llama, Qwen, DeepSeek, Kimi, MiniMax, Venice Uncensored, ecc.  
**Anonimizzata** | Instradata tramite proxy attraverso Venice con i metadati rimossi. Il fornitore sottostante (OpenAI, Anthropic, Google, xAI) vede richieste anonimizzate. | Claude, GPT, Gemini, Grok  
  
## Funzionalità

  * **Orientato alla privacy** : scegli tra modalità "privata" (completamente privata) e "anonimizzata" (tramite proxy)
  * **Modelli non censurati** : accesso a modelli senza restrizioni sui contenuti
  * **Accesso ai principali modelli** : usa Claude, GPT, Gemini e Grok tramite il proxy anonimizzato di Venice
  * **API compatibile con OpenAI** : endpoint `/v1` standard per una facile integrazione
  * **Streaming** : supportato su tutti i modelli
  * **Chiamata di funzioni** : supportata su modelli selezionati (controlla le capacità del modello)
  * **Visione** : supportata sui modelli con capacità di visione
  * **Nessun limite di frequenza rigido** : potrebbe essere applicata una limitazione per uso corretto in caso di utilizzo estremo


## Per iniziare

* ### Ottieni la tua chiave API

  1. Registrati su [venice.ai](<https://venice.ai>)
  2. Vai a **Impostazioni > Chiavi API > Crea nuova chiave**
  3. Copia la tua chiave API (formato: `vapi_xxxxxxxxxxxx`)


* ### Configura OpenClaw

Scegli il metodo di configurazione preferito:

### Interattiva (consigliata)

bashCopy code
[code]
    openclaw onboard --auth-choice venice-api-key
[/code]

Questo:

  1. Richiederà la tua chiave API (oppure userà `VENICE_API_KEY` esistente)
  2. Mostrerà tutti i modelli Venice disponibili
  3. Ti consentirà di scegliere il modello predefinito
  4. Configurerà automaticamente il provider


### Variabile d'ambiente

bashCopy code
[code]
    export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
[/code]

### Non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice venice-api-key \  --venice-api-key "vapi_xxxxxxxxxxxx"
[/code]

* ### Verifica la configurazione

bashCopy code
[code]
    openclaw agent --model venice/kimi-k2-5 --message "Hello, are you working?"
[/code]

## Selezione del modello

Dopo la configurazione, OpenClaw mostra tutti i modelli Venice disponibili. Scegli in base alle tue esigenze:

  * **Modello predefinito** : `venice/kimi-k2-5` per un solido ragionamento privato con supporto alla visione.
  * **Opzione ad alta capacità** : `venice/claude-opus-4-6` per il percorso Venice anonimizzato più potente.
  * **Privacy** : scegli modelli "privati" per un'inferenza completamente privata.
  * **Capacità** : scegli modelli "anonimizzati" per accedere a Claude, GPT, Gemini tramite il proxy di Venice.


Cambia il modello predefinito in qualsiasi momento:

bashCopy code
[code]
    openclaw models set venice/kimi-k2-5openclaw models set venice/claude-opus-4-6
[/code]

Elenca tutti i modelli disponibili:

bashCopy code
[code]
    openclaw models list --all --provider venice
[/code]

Puoi anche eseguire `openclaw configure`, selezionare **Modello/autenticazione** e scegliere **Venice AI**.

## Comportamento di riproduzione di DeepSeek V4

Se Venice espone modelli DeepSeek V4 come `venice/deepseek-v4-pro` o `venice/deepseek-v4-flash`, OpenClaw inserisce il segnaposto di riproduzione `reasoning_content` richiesto da DeepSeek V4 nei messaggi dell'assistente quando il proxy lo omette. Venice rifiuta il controllo nativo di primo livello `thinking` di DeepSeek, quindi OpenClaw mantiene quella correzione di riproduzione specifica del provider separata dai controlli di ragionamento del provider DeepSeek nativo.

## Catalogo integrato (41 in totale)

Modelli privati (26) — completamente privati, nessuna registrazione ID modello | Nome | Contesto | Funzionalità  
---|---|---|---  
`kimi-k2-5` | Kimi K2.5 | 256k | Predefinito, ragionamento, visione  
`kimi-k2-thinking` | Kimi K2 Thinking | 256k | Ragionamento  
`llama-3.3-70b` | Llama 3.3 70B | 128k | Generale  
`llama-3.2-3b` | Llama 3.2 3B | 128k | Generale  
`hermes-3-llama-3.1-405b` | Hermes 3 Llama 3.1 405B | 128k | Generale, strumenti disabilitati  
`qwen3-235b-a22b-thinking-2507` | Qwen3 235B Thinking | 128k | Ragionamento  
`qwen3-235b-a22b-instruct-2507` | Qwen3 235B Instruct | 128k | Generale  
`qwen3-coder-480b-a35b-instruct` | Qwen3 Coder 480B | 256k | Programmazione  
`qwen3-coder-480b-a35b-instruct-turbo` | Qwen3 Coder 480B Turbo | 256k | Programmazione  
`qwen3-5-35b-a3b` | Qwen3.5 35B A3B | 256k | Ragionamento, visione  
`qwen3-next-80b` | Qwen3 Next 80B | 256k | Generale  
`qwen3-vl-235b-a22b` | Qwen3 VL 235B (Vision) | 256k | Visione  
`qwen3-4b` | Venice Small (Qwen3 4B) | 32k | Veloce, ragionamento  
`deepseek-v3.2` | DeepSeek V3.2 | 160k | Ragionamento, strumenti disabilitati  
`venice-uncensored` | Venice Uncensored (Dolphin-Mistral) | 32k | Non censurato, strumenti disabilitati  
`mistral-31-24b` | Venice Medium (Mistral) | 128k | Visione  
`google-gemma-3-27b-it` | Google Gemma 3 27B Instruct | 198k | Visione  
`openai-gpt-oss-120b` | OpenAI GPT OSS 120B | 128k | Generale  
`nvidia-nemotron-3-nano-30b-a3b` | NVIDIA Nemotron 3 Nano 30B | 128k | Generale  
`olafangensan-glm-4.7-flash-heretic` | GLM 4.7 Flash Heretic | 128k | Ragionamento  
`zai-org-glm-4.6` | GLM 4.6 | 198k | Generale  
`zai-org-glm-4.7` | GLM 4.7 | 198k | Ragionamento  
`zai-org-glm-4.7-flash` | GLM 4.7 Flash | 128k | Ragionamento  
`zai-org-glm-5` | GLM 5 | 198k | Ragionamento  
`minimax-m21` | MiniMax M2.1 | 198k | Ragionamento  
`minimax-m25` | MiniMax M2.5 | 198k | Ragionamento  
Modelli anonimizzati (15) — tramite proxy Venice ID modello | Nome | Contesto | Funzionalità  
---|---|---|---  
`claude-opus-4-6` | Claude Opus 4.6 (tramite Venice) | 1M | Ragionamento, visione  
`claude-opus-4-5` | Claude Opus 4.5 (tramite Venice) | 198k | Ragionamento, visione  
`claude-sonnet-4-6` | Claude Sonnet 4.6 (tramite Venice) | 1M | Ragionamento, visione  
`claude-sonnet-4-5` | Claude Sonnet 4.5 (tramite Venice) | 198k | Ragionamento, visione  
`openai-gpt-54` | GPT-5.4 (tramite Venice) | 1M | Ragionamento, visione  
`openai-gpt-53-codex` | GPT-5.3 Codex (tramite Venice) | 400k | Ragionamento, visione, programmazione  
`openai-gpt-52` | GPT-5.2 (tramite Venice) | 256k | Ragionamento  
`openai-gpt-52-codex` | GPT-5.2 Codex (tramite Venice) | 256k | Ragionamento, visione, programmazione  
`openai-gpt-4o-2024-11-20` | GPT-4o (tramite Venice) | 128k | Visione  
`openai-gpt-4o-mini-2024-07-18` | GPT-4o Mini (tramite Venice) | 128k | Visione  
`gemini-3-1-pro-preview` | Gemini 3.1 Pro (tramite Venice) | 1M | Ragionamento, visione  
`gemini-3-pro-preview` | Gemini 3 Pro (tramite Venice) | 198k | Ragionamento, visione  
`gemini-3-flash-preview` | Gemini 3 Flash (tramite Venice) | 256k | Ragionamento, visione  
`grok-41-fast` | Grok 4.1 Fast (tramite Venice) | 1M | Ragionamento, visione  
`grok-code-fast-1` | Grok Code Fast 1 (tramite Venice) | 256k | Ragionamento, programmazione  
  
## Rilevamento dei modelli

OpenClaw include un catalogo iniziale Venice basato su manifest per l'elenco dei modelli in sola lettura. L'aggiornamento a runtime può comunque rilevare i modelli dall'API Venice e ripiega sul catalogo del manifest se l'API non è raggiungibile.

L'endpoint `/models` è pubblico (non serve autenticazione per l'elenco), ma l'inferenza richiede una chiave API valida.

## Streaming e supporto degli strumenti

Funzionalità | Supporto  
---|---  
**Streaming** | Tutti i modelli  
**Chiamata di funzioni** | La maggior parte dei modelli (controlla `supportsFunctionCalling` nell'API)  
**Visione/Immagini** | Modelli contrassegnati con la funzionalità "Visione"  
**Modalità JSON** | Supportata tramite `response_format`  
  
## Prezzi

Venice usa un sistema basato su crediti. Consulta [venice.ai/pricing](<https://venice.ai/pricing>) per le tariffe attuali:

  * **Modelli privati** : in genere hanno un costo inferiore
  * **Modelli anonimizzati** : simili ai prezzi dell'API diretta + una piccola commissione Venice


### Venice (anonimizzata) vs API diretta

Aspetto | Venice (anonimizzata) | API diretta  
---|---|---  
**Privacy** | Metadati rimossi, anonimizzati | Account collegato  
**Latenza** | +10-50 ms (proxy) | Diretta  
**Funzionalità** | La maggior parte delle funzionalità supportata | Funzionalità complete  
**Fatturazione** | Crediti Venice | Fatturazione del provider  
  
## Esempi di utilizzo

bashCopy code
[code]
    # Use the default private modelopenclaw agent --model venice/kimi-k2-5 --message "Quick health check" # Use Claude Opus via Venice (anonymized)openclaw agent --model venice/claude-opus-4-6 --message "Summarize this task" # Use uncensored modelopenclaw agent --model venice/venice-uncensored --message "Draft options" # Use vision model with imageopenclaw agent --model venice/qwen3-vl-235b-a22b --message "Review attached image" # Use coding modelopenclaw agent --model venice/qwen3-coder-480b-a35b-instruct --message "Refactor this function"
[/code]

## Risoluzione dei problemi

API key not recognized bashCopy code
[code]
    echo $VENICE_API_KEYopenclaw models list | grep venice
[/code]

Assicurati che la chiave inizi con `vapi_`.

Model not available

Il catalogo dei modelli Venice si aggiorna dinamicamente. Esegui `openclaw models list` per vedere i modelli attualmente disponibili. Alcuni modelli potrebbero essere temporaneamente offline.

Connection issues

L'API Venice si trova su `https://api.venice.ai/api/v1`. Assicurati che la tua rete consenta connessioni HTTPS.

## Configurazione avanzata

Config file example json5Copy code
[code]
    {  env: { VENICE_API_KEY: "vapi_..." },  agents: { defaults: { model: { primary: "venice/kimi-k2-5" } } },  models: {    mode: "merge",    providers: {      venice: {        baseUrl: "https://api.venice.ai/api/v1",        apiKey: "${VENICE_API_KEY}",        api: "openai-completions",        models: [          {            id: "kimi-k2-5",            name: "Kimi K2.5",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Correlati

[**Model selection** Scelta dei provider, riferimenti ai modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Venice AI** Homepage Venice AI e registrazione dell'account. ](<https://venice.ai>) [**API documentation** Riferimento dell'API Venice e documentazione per sviluppatori. ](<https://docs.venice.ai>) [**Pricing** Tariffe e piani attuali dei crediti Venice. ](<https://venice.ai/pricing>)

Was this useful?YesNo