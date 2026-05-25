---
title: Together AI
source_url: https://docs.openclaw.ai/it/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) fornisce accesso ai principali modelli open-source, inclusi Llama, DeepSeek, Kimi e altri, tramite un'API unificata.

Proprietà | Valore  
---|---  
Provider | `together`  
Auth | `TOGETHER_API_KEY`  
API | compatibile con OpenAI  
URL base | `https://api.together.xyz/v1`  
  
## Per iniziare

* ### Ottieni una chiave API

Crea una chiave API su [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Esempio non interattivo

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Catalogo integrato

OpenClaw include questo catalogo Together in bundle:

Riferimento modello | Nome | Input | Contesto | Note  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | testo, immagine | 262,144 | Modello predefinito; reasoning abilitato  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | testo | 202,752 | Modello di testo general-purpose  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | testo | 131,072 | Modello di istruzioni veloce  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | testo, immagine | 10,000,000 | Multimodale  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | testo, immagine | 20,000,000 | Multimodale  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | testo | 131,072 | Modello di testo generale  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | testo | 131,072 | Modello di reasoning  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | testo | 262,144 | Modello di testo Kimi secondario  
  
## Generazione video

Il Plugin `together` in bundle registra anche la generazione video tramite lo strumento condiviso `video_generate`.

Proprietà | Valore  
---|---  
Modello video predefinito | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modalità | text-to-video, riferimento con immagine singola  
Parametri supportati | `aspectRatio`, `resolution`  
  
Per usare Together come provider video predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Nota sull'ambiente

Se il Gateway viene eseguito come daemon (launchd/systemd), assicurati che `TOGETHER_API_KEY` sia disponibile per quel processo (ad esempio, in `~/.openclaw/.env` o tramite `env.shellEnv`).

Risoluzione dei problemi

  * Verifica che la tua chiave funzioni: `openclaw models list --provider together`
  * Se i modelli non vengono visualizzati, conferma che la chiave API sia impostata nell'ambiente corretto per il processo Gateway.
  * I riferimenti dei modelli usano la forma `together/<model-id>`.


## Correlati

[**Selezione del modello** Regole dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Generazione video** Parametri dello strumento condiviso di generazione video e selezione del provider. ](</it/tools/video-generation>) [**Riferimento di configurazione** Schema di configurazione completo, incluse le impostazioni dei provider. ](</it/gateway/configuration-reference>) [**Together AI** Dashboard, documentazione API e prezzi di Together AI. ](<https://together.ai>)

Was this useful?YesNo