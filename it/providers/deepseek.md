---
title: DeepSeek
source_url: https://docs.openclaw.ai/it/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) fornisce potenti modelli di IA con un'API compatibile con OpenAI.

Proprietà | Valore  
---|---  
Provider | `deepseek`  
Autenticazione | `DEEPSEEK_API_KEY`  
API | compatibile con OpenAI  
URL di base | `https://api.deepseek.com`  
  
## Per iniziare

* ### Ottieni la tua chiave API

Crea una chiave API su [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Questo richiederà la tua chiave API e imposterà `deepseek/deepseek-v4-flash` come modello predefinito.

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Per esaminare il catalogo statico incluso senza richiedere un Gateway in esecuzione, usa:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Configurazione non interattiva

Per installazioni automatizzate o headless, passa direttamente tutti i flag:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalogo integrato

Rif. modello | Nome | Input | Contesto | Output max | Note  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | Modello predefinito; interfaccia V4 con supporto al ragionamento  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | Interfaccia V4 con supporto al ragionamento  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | Interfaccia DeepSeek V3.2 senza ragionamento  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | Interfaccia V3.2 con ragionamento abilitato  
  
## Ragionamento e strumenti

Le sessioni di ragionamento DeepSeek V4 hanno un contratto di riproduzione più rigoroso rispetto alla maggior parte dei provider compatibili con OpenAI: dopo che un turno con ragionamento abilitato usa strumenti, DeepSeek si aspetta che i messaggi assistant riprodotti da quel turno includano `reasoning_content` nelle richieste successive. OpenClaw gestisce questo nel Plugin DeepSeek, quindi il normale uso degli strumenti multi-turno funziona con `deepseek/deepseek-v4-flash` e `deepseek/deepseek-v4-pro`.

Se passi una sessione esistente da un altro provider compatibile con OpenAI a un modello DeepSeek V4, i turni precedenti di chiamata agli strumenti dell'assistant potrebbero non avere `reasoning_content` nativo di DeepSeek. OpenClaw compila quel campo mancante nei messaggi assistant riprodotti per le richieste di ragionamento DeepSeek V4, così il provider può accettare la cronologia senza richiedere `/new`.

Quando il ragionamento è disabilitato in OpenClaw (inclusa la selezione UI **Nessuno**), OpenClaw invia a DeepSeek `thinking: { type: "disabled" }` e rimuove `reasoning_content` riprodotto dalla cronologia in uscita. Questo mantiene le sessioni con ragionamento disabilitato sul percorso DeepSeek senza ragionamento.

Usa `deepseek/deepseek-v4-flash` per il percorso veloce predefinito. Usa `deepseek/deepseek-v4-pro` quando vuoi il modello V4 più potente e puoi accettare costi o latenza maggiori.

## Test live

La suite diretta dei modelli live include DeepSeek V4 nel set di modelli moderno. Per eseguire solo i controlli diretti dei modelli DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Quel controllo live verifica che entrambi i modelli V4 possano completare e che i turni successivi con ragionamento/strumenti preservino il payload di riproduzione richiesto da DeepSeek.

## Esempio di configurazione

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Correlati

[**Selezione del modello** Scelta di provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento della configurazione** Riferimento completo della configurazione per agenti, modelli e provider. ](</it/gateway/configuration-reference>)

Was this useful?YesNo