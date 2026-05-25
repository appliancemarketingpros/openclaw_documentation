---
title: Arcee AI
source_url: https://docs.openclaw.ai/it/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) fornisce accesso alla famiglia Trinity di modelli a miscela di esperti tramite un'API compatibile con OpenAI. Tutti i modelli Trinity sono concessi in licenza Apache 2.0.

I modelli Arcee AI possono essere usati direttamente tramite la piattaforma Arcee o tramite [OpenRouter](</it/providers/openrouter>).

Proprietà | Valore  
---|---  
Provider | `arcee`  
Autenticazione | `ARCEEAI_API_KEY` (diretta) o `OPENROUTER_API_KEY` (tramite OpenRouter)  
API | Compatibile con OpenAI  
URL base | `https://api.arcee.ai/api/v1` (diretta) o `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Primi passi

### Diretta (piattaforma Arcee)

* ### Ottieni una chiave API

Crea una chiave API su [Arcee AI](<https://chat.arcee.ai/>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Tramite OpenRouter

* ### Ottieni una chiave API

Crea una chiave API su [OpenRouter](<https://openrouter.ai/keys>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Imposta un modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Gli stessi riferimenti ai modelli funzionano sia per le configurazioni dirette sia per quelle OpenRouter (ad esempio `arcee/trinity-large-thinking`).

## Configurazione non interattiva

### Diretta (piattaforma Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Tramite OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Catalogo integrato

OpenClaw attualmente distribuisce questo catalogo Arcee incluso:

Riferimento modello | Nome | Input | Contesto | Costo (input/output per 1M) | Note  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | Modello predefinito; ragionamento abilitato  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | Uso generico; 400B parametri, 13B attivi  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | Veloce e conveniente; chiamata di funzioni  
  
## Funzionalità supportate

Funzionalità | Supportata  
---|---  
Streaming | Sì  
Uso di strumenti / chiamata di funzioni | Sì (Trinity Mini, Trinity Large Preview)  
Output strutturato (modalità JSON e schema JSON) | Sì  
Extended thinking | Sì (Trinity Large Thinking; strumenti disabilitati)  
  
Nota sull'ambiente

Se il Gateway viene eseguito come daemon (launchd/systemd), assicurati che `ARCEEAI_API_KEY` (o `OPENROUTER_API_KEY`) sia disponibile per quel processo (ad esempio in `~/.openclaw/.env` o tramite `env.shellEnv`).

Routing OpenRouter

Quando usi i modelli Arcee tramite OpenRouter, si applicano gli stessi riferimenti ai modelli `arcee/*`. OpenClaw gestisce il routing in modo trasparente in base alla tua scelta di autenticazione. Consulta la [documentazione del provider OpenRouter](</it/providers/openrouter>) per i dettagli di configurazione specifici di OpenRouter.

## Correlati

[**OpenRouter** Accedi ai modelli Arcee e a molti altri tramite una singola chiave API. ](</it/providers/openrouter>) [**Selezione del modello** Scelta dei provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>)

Was this useful?YesNo