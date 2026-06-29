---
title: Cohere
source_url: https://docs.openclaw.ai/it/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) fornisce inferenza compatibile con OpenAI tramite la sua API di compatibilità. OpenClaw include il provider Cohere durante la sua transizione all’esternalizzazione e lo pubblica anche come Plugin esterno ufficiale con il catalogo modelli Command A.

Proprietà | Valore  
---|---  
ID provider | `cohere`  
Plugin | incluso durante la transizione; pacchetto esterno ufficiale  
Variabile env di autenticazione | `COHERE_API_KEY`  
Flag di onboarding | `--auth-choice cohere-api-key`  
Flag CLI diretto | `--cohere-api-key <key>`  
API | compatibile con OpenAI (`openai-completions`)  
URL base | `https://api.cohere.ai/compatibility/v1`  
Modello predefinito | `cohere/command-a-03-2025`  
  
## Inizia

  1. Cohere è incluso nei pacchetti OpenClaw attuali. Se non è disponibile, installa il pacchetto esterno e riavvia il Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Crea una chiave API Cohere.
  3. Esegui l’onboarding:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Conferma che il catalogo sia disponibile:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Il modello predefinito viene impostato solo quando non è già configurato alcun modello principale.

## Configurazione solo tramite ambiente

Rendi `COHERE_API_KEY` disponibile al processo Gateway, quindi seleziona il modello Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Correlati

  * [Provider di modelli](</it/concepts/model-providers>)
  * [CLI dei modelli](</it/cli/models>)
  * [Directory dei provider](</it/providers>)


Was this useful?YesNo

Open issue