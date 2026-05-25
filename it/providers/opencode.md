---
title: OpenCode
source_url: https://docs.openclaw.ai/it/providers/opencode
scraped_at: 2026-05-25
---

OpenCode espone due cataloghi ospitati in OpenClaw:

Catalogo | Prefisso | Provider di runtime  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Entrambi i cataloghi usano la stessa chiave API OpenCode. OpenClaw mantiene separati gli id dei provider di runtime in modo che il routing upstream per modello resti corretto, ma onboarding e documentazione li trattano come un'unica configurazione OpenCode.

## Per iniziare

### Catalogo Zen

**Ideale per:** il proxy multimodello OpenCode curato (Claude, GPT, Gemini).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Imposta un modello Zen come predefinito

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Catalogo Go

**Ideale per:** la gamma OpenCode ospitata di Kimi, GLM e MiniMax.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Imposta un modello Go come predefinito

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Esempio di configurazione

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Cataloghi integrati

### Zen

Proprietà | Valore  
---|---  
Provider di runtime | `opencode`  
Modelli di esempio | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Proprietà | Valore  
---|---  
Provider di runtime | `opencode-go`  
Modelli di esempio | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Configurazione avanzata

Alias della chiave API

Anche `OPENCODE_ZEN_API_KEY` è supportata come alias di `OPENCODE_API_KEY`.

Credenziali condivise

Inserire una chiave OpenCode durante la configurazione memorizza le credenziali per entrambi i provider di runtime. Non è necessario eseguire l'onboarding di ciascun catalogo separatamente.

Fatturazione e dashboard

Accedi a OpenCode, aggiungi i dettagli di fatturazione e copia la tua chiave API. La fatturazione e la disponibilità del catalogo sono gestite dalla dashboard OpenCode.

Comportamento di replay Gemini

I riferimenti OpenCode basati su Gemini restano nel percorso proxy-Gemini, quindi OpenClaw mantiene lì la sanificazione della thought-signature Gemini senza abilitare la validazione di replay Gemini nativa né le riscritture bootstrap.

Comportamento di replay non-Gemini

I riferimenti OpenCode non-Gemini mantengono la policy minima di replay compatibile con OpenAI.

## Correlati

[**Selezione del modello** Scelta di provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento della configurazione** Riferimento completo della configurazione per agenti, modelli e provider. ](</it/gateway/configuration-reference>)

Was this useful?YesNo