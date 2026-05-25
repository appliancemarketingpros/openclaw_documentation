---
title: Integra
source_url: https://docs.openclaw.ai/it/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Onboarding guidato completo per la configurazione del Gateway locale o remoto. Usalo quando vuoi che OpenClaw ti accompagni attraverso autenticazione del modello, workspace, gateway, canali, Skills e stato di salute in un unico flusso.

## Guide correlate

[**Hub di onboarding CLI** Guida dettagliata del flusso CLI interattivo. ](</it/start/wizard>) [**Panoramica dell'onboarding** Come si integra l'onboarding di OpenClaw. ](</it/start/onboarding-overview>) [**Riferimento per la configurazione CLI** Output, componenti interni e comportamento per ogni passaggio. ](</it/start/wizard-cli-reference>) [**Automazione CLI** Flag non interattivi e configurazioni tramite script. ](</it/start/wizard-cli-automation>) [**Onboarding dell'app macOS** Flusso di onboarding per l'app nella barra dei menu di macOS. ](</it/start/onboarding>)

## Esempi

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` usa provider di migrazione di proprietà dei plugin, come Hermes. Viene eseguito solo su una configurazione OpenClaw nuova; se sono presenti configurazione, credenziali, sessioni o file di memoria/identità del workspace esistenti, reimposta o scegli una configurazione nuova prima di importare.

`--modern` avvia l'anteprima dell'onboarding conversazionale Crestodian. Senza `--modern`, `openclaw onboard` mantiene il flusso di onboarding classico.

Per destinazioni `ws://` in testo normale su reti private (solo reti attendibili), imposta `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` nell'ambiente del processo di onboarding. Non esiste un equivalente `openclaw.json` per questo break-glass del trasporto lato client.

Provider personalizzato non interattivo:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` è facoltativo in modalità non interattiva. Se omesso, l'onboarding controlla `CUSTOM_API_KEY`. OpenClaw contrassegna automaticamente gli ID comuni dei modelli vision come compatibili con le immagini. Passa `--custom-image-input` per ID vision personalizzati sconosciuti, oppure `--custom-text-input` per forzare metadati solo testo.

LM Studio supporta anche un flag chiave specifico del provider in modalità non interattiva:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Ollama non interattivo:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` predefinisce `http://127.0.0.1:11434`. `--custom-model-id` è facoltativo; se omesso, l'onboarding usa i valori predefiniti suggeriti da Ollama. Anche gli ID dei modelli cloud come `kimi-k2.5:cloud` funzionano qui.

Archivia le chiavi del provider come riferimenti invece che in testo normale:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

Con `--secret-input-mode ref`, l'onboarding scrive riferimenti basati su variabili d'ambiente invece dei valori delle chiavi in testo normale. Per i provider basati su profili di autenticazione, questo scrive voci `keyRef`; per i provider personalizzati, questo scrive `models.providers.<id>.apiKey` come riferimento env (per esempio `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Contratto della modalità `ref` non interattiva:

  * Imposta la variabile d'ambiente del provider nell'ambiente del processo di onboarding (per esempio `OPENAI_API_KEY`).
  * Non passare flag chiave inline (per esempio `--openai-api-key`) a meno che quella variabile d'ambiente non sia anch'essa impostata.
  * Se viene passato un flag chiave inline senza la variabile d'ambiente richiesta, l'onboarding fallisce rapidamente con indicazioni.


Opzioni token del Gateway in modalità non interattiva:

  * `--gateway-auth token --gateway-token <token>` archivia un token in testo normale.
  * `--gateway-auth token --gateway-token-ref-env <name>` archivia `gateway.auth.token` come SecretRef env.
  * `--gateway-token` e `--gateway-token-ref-env` si escludono a vicenda.
  * `--gateway-token-ref-env` richiede una variabile d'ambiente non vuota nell'ambiente del processo di onboarding.
  * Con `--install-daemon`, quando l'autenticazione tramite token richiede un token, i token gateway gestiti da SecretRef vengono convalidati ma non salvati come testo normale risolto nei metadati dell'ambiente del servizio supervisor.
  * Con `--install-daemon`, se la modalità token richiede un token e il SecretRef del token configurato non è risolto, l'onboarding fallisce in modo chiuso con indicazioni di correzione.
  * Con `--install-daemon`, se sia `gateway.auth.token` sia `gateway.auth.password` sono configurati e `gateway.auth.mode` non è impostato, l'onboarding blocca l'installazione finché la modalità non viene impostata esplicitamente.
  * L'onboarding locale scrive `gateway.mode="local"` nella configurazione. Se in seguito in un file di configurazione manca `gateway.mode`, trattalo come una configurazione danneggiata o una modifica manuale incompleta, non come una scorciatoia valida per la modalità locale.
  * L'onboarding locale installa i plugin scaricabili selezionati quando il percorso di configurazione scelto li richiede.
  * L'onboarding remoto scrive solo le informazioni di connessione per il Gateway remoto e non installa pacchetti plugin locali.
  * `--allow-unconfigured` è una scappatoia separata del runtime del gateway. Non significa che l'onboarding possa omettere `gateway.mode`.


Esempio:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

Stato di salute del gateway locale non interattivo:

  * A meno che tu non passi `--skip-health`, l'onboarding attende che un gateway locale sia raggiungibile prima di terminare con successo.
  * `--install-daemon` avvia prima il percorso di installazione del gateway gestito. Senza di esso, devi avere già un gateway locale in esecuzione, per esempio `openclaw gateway run`.
  * Se in automazione vuoi solo scrivere configurazione/workspace/bootstrap, usa `--skip-health`.
  * Se gestisci direttamente i file del workspace, passa `--skip-bootstrap` per impostare `agents.defaults.skipBootstrap: true` e saltare la creazione di `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` e `BOOTSTRAP.md`.
  * Su Windows nativo, `--install-daemon` prova prima le Attività pianificate e, se la creazione dell'attività viene negata, ripiega su un elemento di login nella cartella Startup per utente.


Comportamento dell'onboarding interattivo con modalità riferimento:

  * Scegli **Usa riferimento segreto** quando richiesto.
  * Poi scegli una delle seguenti opzioni: 
    * Variabile d'ambiente
    * Provider di segreti configurato (`file` o `exec`)
  * L'onboarding esegue una convalida preflight rapida prima di salvare il riferimento. 
    * Se la convalida fallisce, l'onboarding mostra l'errore e ti consente di riprovare.


### Scelte di endpoint [Z.AI](<http://Z.AI>) non interattive

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Esempio Mistral non interattivo:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Note sul flusso

Tipi di flusso

  * `quickstart`: prompt minimi, genera automaticamente un token gateway.
  * `manual`: prompt completi per porta, bind e autenticazione (alias di `advanced`).
  * `import`: esegue un provider di migrazione rilevato, mostra un'anteprima del piano, quindi applica dopo la conferma.

Prefiltraggio dei provider

Quando una scelta di autenticazione implica un provider preferito, l'onboarding prefiltra i selettori del modello predefinito e della allowlist su quel provider. Per Volcengine e BytePlus, questo corrisponde anche alle varianti del coding plan (`volcengine-plan/*`, `byteplus-plan/*`).

Se il filtro del provider preferito non produce ancora modelli caricati, l'onboarding ripiega sul catalogo non filtrato invece di lasciare vuoto il selettore.

Follow-up della ricerca web

Alcuni provider di ricerca web attivano prompt di follow-up specifici del provider:

  * **Grok** può offrire la configurazione facoltativa di `x_search` con lo stesso `XAI_API_KEY` e una scelta di modello `x_search`.
  * **Kimi** può chiedere la regione dell'API Moonshot (`api.moonshot.ai` vs `api.moonshot.cn`) e il modello predefinito di ricerca web Kimi.

Altri comportamenti

  * Comportamento dell'ambito DM dell'onboarding locale: [Riferimento per la configurazione CLI](</it/start/wizard-cli-reference#outputs-and-internals>).
  * Prima chat più rapida: `openclaw dashboard` (UI di controllo, nessuna configurazione del canale).
  * Provider personalizzato: collega qualsiasi endpoint compatibile con OpenAI o Anthropic, inclusi provider ospitati non elencati. Usa Unknown per il rilevamento automatico.
  * Se viene rilevato lo stato Hermes, l'onboarding offre un flusso di migrazione. Usa [Migra](</it/cli/migrate>) per piani dry-run, modalità sovrascrittura, report e mappature esatte.


## Comandi di follow-up comuni

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Usa invece `openclaw setup` quando hai bisogno solo della configurazione/workspace di base. Usa `openclaw configure` in seguito per modifiche mirate e `openclaw channels add` per la configurazione solo dei canali.

Was this useful?YesNo