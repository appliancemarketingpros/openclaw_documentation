---
title: Hugging Face (inference)
source_url: https://docs.openclaw.ai/it/providers/huggingface
scraped_at: 2026-05-25
---

[I provider Hugging Face Inference](<https://huggingface.co/docs/inference-providers>) offrono chat completions compatibili con OpenAI tramite una singola API router. Ottieni accesso a molti modelli (DeepSeek, Llama e altri) con un solo token. OpenClaw usa l'**endpoint compatibile con OpenAI** (solo chat completions); per text-to-image, embeddings o speech usa direttamente i [client HF inference](<https://huggingface.co/docs/api-inference/quicktour>).

  * Provider: `huggingface`
  * Auth: `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN` (token a granularità fine con **Make calls to Inference Providers**)
  * API: compatibile con OpenAI (`https://router.huggingface.co/v1`)
  * Billing: singolo token HF; i [prezzi](<https://huggingface.co/docs/inference-providers/pricing>) seguono le tariffe del provider con un free tier.


## Per iniziare

* ### Crea un token a granularità fine

Vai a [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) e crea un nuovo token a granularità fine.

* ### Esegui l'onboarding

Scegli **Hugging Face** nel menu a discesa del provider, poi inserisci la tua chiave API quando richiesto:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Seleziona un modello predefinito

Nel menu a discesa **Default Hugging Face model** , scegli il modello desiderato. L'elenco viene caricato dalla Inference API quando hai un token valido; altrimenti viene mostrato un elenco integrato. La tua scelta viene salvata come modello predefinito.

Puoi anche impostare o cambiare il modello predefinito successivamente nella configurazione:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Configurazione non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Questo imposterà `huggingface/deepseek-ai/DeepSeek-R1` come modello predefinito.

## ID modello

I riferimenti ai modelli usano la forma `huggingface/<org>/<model>` (ID in stile Hub). L'elenco qui sotto proviene da **GET** `https://router.huggingface.co/v1/models`; il tuo catalogo potrebbe includerne altri.

Model | Ref (prefix with `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Configurazione avanzata

Rilevamento dei modelli e menu a discesa dell'onboarding

OpenClaw rileva i modelli chiamando direttamente l'**endpoint Inference** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Facoltativo: invia `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` o `$HF_TOKEN` per l'elenco completo; alcuni endpoint restituiscono un sottoinsieme senza auth.) La risposta è in stile OpenAI `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Quando configuri una chiave API Hugging Face (tramite onboarding, `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN`), OpenClaw usa questa GET per rilevare i modelli di chat-completion disponibili. Durante la **configurazione interattiva** , dopo aver inserito il token vedi un menu a discesa **Default Hugging Face model** popolato da quell'elenco (oppure dal catalogo integrato se la richiesta fallisce). A runtime (per esempio all'avvio del Gateway), quando è presente una chiave, OpenClaw chiama di nuovo **GET** `https://router.huggingface.co/v1/models` per aggiornare il catalogo. L'elenco viene unito con un catalogo integrato (per metadati come finestra di contesto e costo). Se la richiesta fallisce o non è impostata alcuna chiave, viene usato solo il catalogo integrato.

Nomi dei modelli, alias e suffissi di policy

  * **Nome dall'API:** il nome visualizzato del modello viene **idrato da GET /v1/models** quando l'API restituisce `name`, `title` o `display_name`; altrimenti viene derivato dall'id del modello (per esempio `deepseek-ai/DeepSeek-R1` diventa "DeepSeek R1").
  * **Override del nome visualizzato:** puoi impostare un'etichetta personalizzata per modello nella configurazione così appare come vuoi nella CLI e nella UI:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Suffissi di policy:** la documentazione e gli helper Hugging Face inclusi in OpenClaw trattano attualmente questi due suffissi come varianti di policy integrate:

    * **`:fastest`** — throughput massimo.
    * **`:cheapest`** — costo minimo per token in uscita.

Puoi aggiungerli come voci separate in `models.providers.huggingface.models` oppure impostare `model.primary` con il suffisso. Puoi anche impostare l'ordine predefinito del provider in [Inference Provider settings](<https://hf.co/settings/inference-providers>) (senza suffisso = usa quell'ordine).

  * **Merge della configurazione:** le voci esistenti in `models.providers.huggingface.models` (per esempio in `models.json`) vengono mantenute quando la configurazione viene unita. Quindi qualsiasi `name`, `alias` o opzione del modello che imposti lì viene preservata.


Ambiente e configurazione del daemon

Se il Gateway gira come daemon (launchd/systemd), assicurati che `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN` sia disponibile per quel processo (per esempio in `~/.openclaw/.env` o tramite `env.shellEnv`).

Configurazione: DeepSeek R1 con fallback Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Configurazione: Qwen con varianti cheapest e fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Configurazione: DeepSeek + Llama + GPT-OSS con alias json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Configurazione: più Qwen e DeepSeek con suffissi di policy json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Correlati

[**Selezione del provider di modelli** Panoramica di tutti i provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>) [**Selezione del modello** Come scegliere e configurare i modelli. ](</it/concepts/models>) [**Documentazione Inference Providers** Documentazione ufficiale di Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Configurazione** Riferimento completo della configurazione. ](</it/gateway/configuration>)

Was this useful?YesNo