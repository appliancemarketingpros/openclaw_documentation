---
title: Groq
source_url: https://docs.openclaw.ai/it/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) offre inferenza ultra-rapida su modelli a pesi aperti (Llama, Gemma, Kimi, Qwen, GPT OSS e altri) usando hardware LPU personalizzato. OpenClaw include un Plugin Groq in bundle che registra sia un provider di chat compatibile con OpenAI sia un provider di comprensione dei media audio.

Proprietà | Valore  
---|---  
ID provider | `groq`  
Plugin | in bundle, `enabledByDefault: true`  
Variabile env auth | `GROQ_API_KEY`  
Flag di onboarding | `--auth-choice groq-api-key`  
API | compatibile con OpenAI (`openai-completions`)  
URL di base | `https://api.groq.com/openai/v1`  
Trascrizione audio | `whisper-large-v3-turbo` (predefinito)  
Chat predefinita suggerita | `groq/llama-3.3-70b-versatile`  
  
## Introduzione

* ### Get an API key

Crea una chiave API su [console.groq.com/keys](<https://console.groq.com/keys>).

* ### Set the API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Env onlyCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Verify the catalog is reachable

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Esempio di file di configurazione

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Catalogo integrato

OpenClaw distribuisce un catalogo Groq basato su manifest con voci sia con ragionamento sia senza ragionamento. Esegui `openclaw models list --provider groq` per vedere le righe in bundle per la versione installata, oppure consulta [console.groq.com/docs/models](<https://console.groq.com/docs/models>) per l'elenco ufficiale di Groq.

Rif. modello | Nome | Ragionamento | Input | Contesto  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | no | testo | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | no | testo | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | no | testo + immagine | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | no | testo + immagine | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | no | testo | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | no | testo | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | no | testo | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | no | testo | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | no | testo | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | no | testo | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | sì | testo | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | sì | testo | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | sì | testo | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | sì | testo | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | sì | testo | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | sì | testo | 131,072  
`groq/groq/compound` | Compound | sì | testo | 131,072  
`groq/groq/compound-mini` | Compound Mini | sì | testo | 131,072  
  
## Modelli con ragionamento

OpenClaw mappa i livelli `/think` condivisi ai valori `reasoning_effort` specifici del modello di Groq:

  * Per `qwen/qwen3-32b`, il pensiero disabilitato invia `none` e il pensiero abilitato invia `default`.
  * Per i modelli di ragionamento GPT OSS di Groq (`openai/gpt-oss-*`), OpenClaw invia `low`, `medium` o `high` in base al livello `/think`. Il pensiero disabilitato omette `reasoning_effort` perché questi modelli non supportano un valore disabilitato.
  * DeepSeek R1 Distill, Qwen QwQ e Compound usano la superficie di ragionamento nativa di Groq; `/think` controlla la visibilità, ma il modello ragiona sempre.


Consulta [Modalità di pensiero](</it/tools/thinking>) per i livelli `/think` condivisi e per come OpenClaw li traduce per provider.

## Trascrizione audio

Il Plugin in bundle di Groq registra anche un **provider di comprensione dei media audio** , così i messaggi vocali possono essere trascritti tramite la superficie condivisa `tools.media.audio`.

Proprietà | Valore  
---|---  
Percorso config condiviso | `tools.media.audio`  
URL di base predefinito | `https://api.groq.com/openai/v1`  
Modello predefinito | `whisper-large-v3-turbo`  
Priorità automatica | 20  
Endpoint API | compatibile con OpenAI `/audio/transcriptions`  
  
Per rendere Groq il backend audio predefinito:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Environment availability for the daemon

Se il Gateway viene eseguito come servizio gestito (launchd, systemd, Docker), `GROQ_API_KEY` deve essere visibile a quel processo, non solo alla tua shell interattiva.

Custom Groq model ids

OpenClaw accetta qualsiasi ID modello Groq a runtime. Usa l'ID esatto mostrato da Groq e anteponi `groq/`. Il catalogo in bundle copre i casi comuni; gli ID non presenti nel catalogo ricadono sul modello predefinito compatibile con OpenAI.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Correlati

[**Model providers** Scelta dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Thinking modes** Livelli di impegno di ragionamento e interazione con la policy del provider. ](</it/tools/thinking>) [**Configuration reference** Schema di configurazione completo, incluse le impostazioni di provider e audio. ](</it/gateway/configuration-reference>) [**Groq Console** Dashboard Groq, documentazione API e prezzi. ](<https://console.groq.com>)

Was this useful?YesNo