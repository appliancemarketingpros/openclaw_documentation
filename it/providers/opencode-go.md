---
title: OpenCode Go
source_url: https://docs.openclaw.ai/it/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go è il catalogo Go all'interno di [OpenCode](</it/providers/opencode>). Usa la stessa `OPENCODE_API_KEY` del catalogo Zen, ma mantiene l'ID provider runtime `opencode-go` così che il routing upstream per modello resti corretto.

Proprietà | Valore  
---|---  
Provider runtime | `opencode-go`  
Autenticazione | `OPENCODE_API_KEY`  
Configurazione padre | [OpenCode](</it/providers/opencode>)  
  
## Catalogo integrato

OpenClaw ricava la maggior parte delle righe del catalogo Go dal registro dei modelli pi integrato e integra le righe upstream correnti mentre il registro si aggiorna. Esegui `openclaw models list --provider opencode-go` per l'elenco corrente dei modelli.

Il provider include:

Riferimento modello | Nome  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (limiti 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Per iniziare

### Interattivo

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
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

### Non interattivo

* ### Passa la chiave direttamente

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Esempio di configurazione

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Configurazione avanzata

Comportamento del routing

OpenClaw gestisce automaticamente il routing per modello quando il riferimento del modello usa `opencode-go/...`. Non è richiesta alcuna configurazione aggiuntiva del provider.

Convenzione dei riferimenti runtime

I riferimenti runtime restano espliciti: `opencode/...` per Zen, `opencode-go/...` per Go. Questo mantiene corretto il routing upstream per modello in entrambi i cataloghi.

Credenziali condivise

La stessa `OPENCODE_API_KEY` è usata sia dal catalogo Zen sia da quello Go. Inserendo la chiave durante la configurazione vengono archiviate le credenziali per entrambi i provider runtime.

## Correlati

[**OpenCode (padre)** Onboarding condiviso, panoramica del catalogo e note avanzate. ](</it/providers/opencode>) [**Selezione del modello** Scelta dei provider, riferimenti di modello e comportamento di failover. ](</it/concepts/model-providers>)

Was this useful?YesNo