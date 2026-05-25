---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/it/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw include un plugin `alibaba` in bundle che registra un provider per la generazione video per i modelli Wan su Alibaba Model Studio (il nome internazionale di DashScope). Il plugin è abilitato per impostazione predefinita; devi solo impostare una chiave API.

Proprietà | Valore  
---|---  
ID provider | `alibaba`  
Plugin | in bundle, `enabledByDefault: true`  
Variabili env auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (vince la prima corrispondenza)  
Flag onboarding | `--auth-choice alibaba-model-studio-api-key`  
Flag CLI diretto | `--alibaba-model-studio-api-key <key>`  
Modello predefinito | `alibaba/wan2.6-t2v`  
URL base predefinito | `https://dashscope-intl.aliyuncs.com`  
  
## Per iniziare

* ### Imposta una chiave API

Usa l'onboarding per archiviare la chiave per il provider `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Oppure passa la chiave direttamente durante l'installazione/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Oppure esporta una qualsiasi delle variabili env accettate prima di avviare il Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Imposta un modello video predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verifica che il provider sia configurato

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

L'elenco dovrebbe includere tutti e cinque i modelli Wan inclusi in bundle. Se `MODELSTUDIO_API_KEY` non viene risolta, `openclaw models status --json` segnala la credenziale mancante in `auth.unusableProfiles`.

## Modelli Wan integrati

Riferimento modello | Modalità  
---|---  
`alibaba/wan2.6-t2v` | Testo-video (predefinito)  
`alibaba/wan2.6-i2v` | Immagine-video  
`alibaba/wan2.6-r2v` | Riferimento-video  
`alibaba/wan2.6-r2v-flash` | Riferimento-video (rapido)  
`alibaba/wan2.7-r2v` | Riferimento-video  
  
## Capacità e limiti

Il provider incluso in bundle rispecchia i limiti dell'API video Wan di DashScope. Tutte e tre le modalità condividono lo stesso conteggio video per richiesta e lo stesso limite di durata; cambia solo la forma dell'input.

Modalità | Video di output max | Immagini di input max | Video di input max | Durata max | Controlli supportati  
---|---|---|---|---|---  
Testo-video | 1 | n/a | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Immagine-video | 1 | 1 | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Riferimento-video | 1 | n/a | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Quando una richiesta omette `durationSeconds`, il provider invia il valore predefinito accettato da DashScope di **5 secondi**. Imposta esplicitamente `durationSeconds` nello [strumento di generazione video](</it/tools/video-generation>) per arrivare fino a 10 s.

## Configurazione avanzata

Sovrascrivi l'URL base di DashScope

Il provider usa per impostazione predefinita l'endpoint internazionale di DashScope. Per indirizzare l'endpoint della regione Cina, imposta:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Il provider rimuove le barre finali prima di costruire gli URL delle attività AIGC.

Priorità env auth

OpenClaw risolve la chiave API Alibaba dalle variabili di ambiente in quest'ordine, prendendo il primo valore non vuoto:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Le voci `auth.profiles` configurate (impostate tramite `openclaw models auth login`) sovrascrivono la risoluzione delle variabili env. Consulta [Profili auth nelle FAQ sui modelli](</it/help/faq-models#what-is-an-auth-profile>) per la rotazione dei profili, il cooldown e i meccanismi di sovrascrittura.

Relazione con il plugin Qwen

Entrambi i plugin inclusi in bundle comunicano con DashScope e accettano chiavi API sovrapposte. Usa:

  * gli ID `alibaba/wan*.*` per utilizzare il provider video Wan dedicato documentato in questa pagina.
  * gli ID `qwen/*` per chat, embedding e comprensione dei media Qwen (vedi [Qwen](</it/providers/qwen>)).


Impostare una sola volta `MODELSTUDIO_API_KEY` autentica entrambi i plugin perché l'elenco delle variabili env auth è intenzionalmente sovrapposto; non devi eseguire l'onboarding di ciascun plugin separatamente.

## Correlati

[**Generazione video** Parametri dello strumento video condiviso e selezione del provider. ](</it/tools/video-generation>) [**Qwen** Configurazione di chat, embedding e comprensione dei media Qwen con la stessa auth DashScope. ](</it/providers/qwen>) [**Riferimento di configurazione** Valori predefiniti agent e configurazione dei modelli. ](</it/gateway/config-agents#agent-defaults>) [**FAQ modelli** Profili auth, cambio di modello e risoluzione degli errori "no profile". ](</it/help/faq-models>)

Was this useful?YesNo