---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/it/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo è la piattaforma API per i modelli **MiMo**. OpenClaw include un Plugin `xiaomi` in bundle che registra sia un provider di chat compatibile con OpenAI sia un provider vocale (TTS) con la stessa `XIAOMI_API_KEY`.

Proprietà | Valore  
---|---  
ID provider | `xiaomi`  
Plugin | in bundle, `enabledByDefault: true`  
Variabile env auth | `XIAOMI_API_KEY`  
Flag di onboarding | `--auth-choice xiaomi-api-key`  
Flag CLI diretto | `--xiaomi-api-key <key>`  
Contratti | completamenti chat + `speechProviders`  
API | compatibile con OpenAI (`openai-completions`)  
URL di base | `https://api.xiaomimimo.com/v1`  
Modello predefinito | `xiaomi/mimo-v2-flash`  
TTS predefinito | `mimo-v2.5-tts`, voce `mimo_default`  
  
## Introduzione

* ### Ottieni una chiave API

Crea una chiave API nella [console Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Catalogo integrato

Riferimento modello | Input | Contesto | Output max | Reasoning | Note  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | testo | 262.144 | 8.192 | No | Modello predefinito  
`xiaomi/mimo-v2-pro` | testo | 1.048.576 | 32.000 | Sì | Contesto ampio  
`xiaomi/mimo-v2-omni` | testo, immagine | 262.144 | 32.000 | Sì | Multimodale  
  
## Sintesi vocale

Il Plugin `xiaomi` in bundle registra anche Xiaomi MiMo come provider vocale per `messages.tts`. Chiama il contratto TTS dei completamenti chat di Xiaomi con il testo come messaggio `assistant` e indicazioni di stile opzionali come messaggio `user`.

Proprietà | Valore  
---|---  
ID TTS | `xiaomi` (alias `mimo`)  
Auth | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` con `audio`  
Predefinito | `mimo-v2.5-tts`, voce `mimo_default`  
Output | MP3 per impostazione predefinita; WAV se configurato  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Le voci integrate supportate includono `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` e `Dean`. `mimo-v2-tts` è supportato per account MiMo TTS meno recenti; l'impostazione predefinita usa il modello TTS MiMo-V2.5 attuale. Per destinazioni di note vocali come Feishu e Telegram, OpenClaw transcodifica l'output Xiaomi in Opus a 48 kHz con `ffmpeg` prima della consegna.

## Esempio di configurazione

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Comportamento di inserimento automatico

Il provider `xiaomi` viene inserito automaticamente quando `XIAOMI_API_KEY` è impostata nel tuo ambiente o esiste un profilo di autenticazione. Non devi configurare manualmente il provider, a meno che tu non voglia sovrascrivere i metadati del modello o l'URL di base.

Dettagli dei modelli

  * **mimo-v2-flash** — leggero e veloce, ideale per attività di testo generiche. Nessun supporto per il reasoning.
  * **mimo-v2-pro** — supporta il reasoning con una finestra di contesto da 1M token per carichi di lavoro su documenti lunghi.
  * **mimo-v2-omni** — modello multimodale con reasoning abilitato che accetta input sia di testo sia di immagini.

Risoluzione dei problemi

  * Se i modelli non vengono visualizzati, conferma che `XIAOMI_API_KEY` sia impostata e valida.
  * Quando il Gateway viene eseguito come daemon, assicurati che la chiave sia disponibile per quel processo (per esempio in `~/.openclaw/.env` o tramite `env.shellEnv`).


## Correlati

[**Selezione del modello** Scelta dei provider, dei riferimenti modello e del comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento di configurazione** Riferimento completo della configurazione di OpenClaw. ](</it/gateway/configuration-reference>) [**Console Xiaomi MiMo** Dashboard Xiaomi MiMo e gestione delle chiavi API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo