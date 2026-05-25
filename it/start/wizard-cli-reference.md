---
title: Riferimento alla configurazione della CLI
source_url: https://docs.openclaw.ai/it/start/wizard-cli-reference
scraped_at: 2026-05-25
---

Questa pagina è il riferimento completo per `openclaw onboard`. Per la guida breve, vedi [Onboarding (CLI)](</it/start/wizard>).

## Cosa fa la procedura guidata

La modalità locale (predefinita) ti guida attraverso:

  * Configurazione di modello e autenticazione (OAuth per abbonamento OpenAI Code, CLI o chiave API Anthropic Claude, più opzioni MiniMax, GLM, Ollama, Moonshot, StepFun e AI Gateway)
  * Posizione del workspace e file di bootstrap
  * Impostazioni del Gateway (porta, bind, autenticazione, Tailscale)
  * Canali e provider (Telegram, WhatsApp, Discord, Google Chat, Mattermost, Signal, iMessage e altri Plugin di canale inclusi)
  * Installazione del daemon (LaunchAgent, unità utente systemd o Scheduled Task nativo di Windows con fallback alla cartella Startup)
  * Controllo di integrità
  * Configurazione di Skills


La modalità remota configura questa macchina per connettersi a un Gateway altrove. Non installa né modifica nulla sull’host remoto.

## Dettagli del flusso locale

* ### Rilevamento della configurazione esistente

  * Se `~/.openclaw/openclaw.json` esiste, scegli Mantieni, Modifica o Reimposta.
  * Rieseguire la procedura guidata non elimina nulla a meno che tu non scelga esplicitamente Reimposta (o passi `--reset`).
  * CLI `--reset` usa come predefinito `config+creds+sessions`; usa `--reset-scope full` per rimuovere anche il workspace.
  * Se la configurazione non è valida o contiene chiavi legacy, la procedura guidata si interrompe e ti chiede di eseguire `openclaw doctor` prima di continuare.
  * La reimpostazione usa `trash` e offre questi ambiti: 
    * Solo configurazione
    * Configurazione + credenziali + sessioni
    * Reimpostazione completa (rimuove anche il workspace)


* ### Modello e autenticazione

  * La matrice completa delle opzioni è in Opzioni di autenticazione e modello.


* ### Workspace

  * Predefinito `~/.openclaw/workspace` (configurabile).
  * Inizializza i file del workspace necessari per il rituale di bootstrap al primo avvio.
  * Layout del workspace: [Workspace dell’agente](</it/concepts/agent-workspace>).


* ### Gateway

  * Chiede porta, bind, modalità di autenticazione ed esposizione Tailscale.
  * Consigliato: mantieni l’autenticazione con token abilitata anche per il loopback, così i client WS locali devono autenticarsi.
  * In modalità token, la configurazione interattiva offre: 
    * **Genera/memorizza token in testo semplice** (predefinito)
    * **Usa SecretRef** (opt-in)
  * In modalità password, la configurazione interattiva supporta anche l’archiviazione in testo semplice o SecretRef.
  * Percorso SecretRef token non interattivo: `--gateway-token-ref-env &lt;ENV_VAR&gt;`. 
    * Richiede una variabile env non vuota nell’ambiente del processo di onboarding.
    * Non può essere combinato con `--gateway-token`.
  * Disabilita l’autenticazione solo se ti fidi completamente di ogni processo locale.
  * I bind non loopback richiedono comunque l’autenticazione.


* ### Canali

  * [WhatsApp](</it/channels/whatsapp>): accesso QR opzionale
  * [Telegram](</it/channels/telegram>): token del bot
  * [Discord](</it/channels/discord>): token del bot
  * [Google Chat](</it/channels/googlechat>): JSON dell’account di servizio + audience del Webhook
  * [Mattermost](</it/channels/mattermost>): token del bot + URL di base
  * [Signal](</it/channels/signal>): installazione opzionale di `signal-cli` \+ configurazione dell’account
  * [iMessage](</it/channels/imessage>): percorso CLI `imsg` \+ accesso al DB di Messages; usa un wrapper SSH quando il Gateway viene eseguito fuori dal Mac
  * Sicurezza DM: l’impostazione predefinita è l’abbinamento. Il primo DM invia un codice; approva tramite `openclaw pairing approve <channel> <code>` oppure usa allowlist.


* ### Installazione del daemon

  * macOS: LaunchAgent 
    * Richiede una sessione utente con accesso effettuato; per headless, usa un LaunchDaemon personalizzato (non distribuito).
  * Linux e Windows tramite WSL2: unità utente systemd 
    * La procedura guidata tenta `loginctl enable-linger <user>` in modo che il Gateway resti attivo dopo il logout.
    * Potrebbe chiedere sudo (scrive in `/var/lib/systemd/linger`); prova prima senza sudo.
  * Windows nativo: prima Scheduled Task 
    * Se la creazione del task viene negata, OpenClaw ripiega su un elemento di accesso nella cartella Startup per utente e avvia subito il Gateway.
    * Scheduled Tasks restano preferiti perché forniscono uno stato del supervisore migliore.
  * Selezione runtime: Node (consigliato; richiesto per WhatsApp e Telegram). Bun non è consigliato.


* ### Controllo di integrità

  * Avvia il Gateway (se necessario) ed esegue `openclaw health`.
  * `openclaw status --deep` aggiunge la sonda di integrità live del Gateway all’output di stato, incluse le sonde dei canali quando supportate.


* ### Skills

  * Legge le Skills disponibili e controlla i requisiti.
  * Ti consente di scegliere il gestore Node: npm, pnpm o bun.
  * Installa dipendenze opzionali (alcune usano Homebrew su macOS).


* ### Fine

  * Riepilogo e passaggi successivi, incluse opzioni per app iOS, Android e macOS.


## Dettagli della modalità remota

La modalità remota configura questa macchina per connettersi a un Gateway altrove.

Cosa imposti:

  * URL del Gateway remoto (`ws://...`)
  * Token se l’autenticazione del Gateway remoto è richiesta (consigliato)


## Opzioni di autenticazione e modello

Chiave API Anthropic

Usa `ANTHROPIC_API_KEY` se presente o chiede una chiave, quindi la salva per l’uso del daemon.

Abbonamento OpenAI Code (OAuth)

Flusso browser; incolla `code#state`.

Imposta `agents.defaults.model` su `openai/gpt-5.5` tramite il runtime Codex quando il modello non è impostato o appartiene già alla famiglia OpenAI.

Abbonamento OpenAI Code (abbinamento dispositivo)

Flusso di abbinamento browser con un codice dispositivo di breve durata.

Imposta `agents.defaults.model` su `openai/gpt-5.5` tramite il runtime Codex quando il modello non è impostato o appartiene già alla famiglia OpenAI.

Chiave API OpenAI

Usa `OPENAI_API_KEY` se presente o chiede una chiave, quindi memorizza la credenziale nei profili di autenticazione.

Imposta `agents.defaults.model` su `openai/gpt-5.5` quando il modello non è impostato, è `openai/*` o `openai-codex/*`.

Chiave API xAI (Grok)

Chiede `XAI_API_KEY` e configura xAI come provider di modelli.

OpenCode

Chiede `OPENCODE_API_KEY` (o `OPENCODE_ZEN_API_KEY`) e ti consente di scegliere il catalogo Zen o Go. URL di configurazione: [opencode.ai/auth](<https://opencode.ai/auth>).

Chiave API (generica)

Memorizza la chiave per te.

Vercel AI Gateway

Chiede `AI_GATEWAY_API_KEY`. Maggiori dettagli: [Vercel AI Gateway](</it/providers/vercel-ai-gateway>).

Cloudflare AI Gateway

Chiede ID account, ID Gateway e `CLOUDFLARE_AI_GATEWAY_API_KEY`. Maggiori dettagli: [Cloudflare AI Gateway](</it/providers/cloudflare-ai-gateway>).

MiniMax

La configurazione viene scritta automaticamente. Il default hosted è `MiniMax-M2.7`; la configurazione con chiave API usa `minimax/...`, mentre la configurazione OAuth usa `minimax-portal/...`. Maggiori dettagli: [MiniMax](</it/providers/minimax>).

StepFun

La configurazione viene scritta automaticamente per StepFun standard o Step Plan su endpoint Cina o globali. Standard attualmente include `step-3.5-flash`, e Step Plan include anche `step-3.5-flash-2603`. Maggiori dettagli: [StepFun](</it/providers/stepfun>).

Synthetic (compatibile con Anthropic)

Chiede `SYNTHETIC_API_KEY`. Maggiori dettagli: [Synthetic](</it/providers/synthetic>).

Ollama (Cloud e modelli open locali)

Chiede prima `Cloud + Local`, `Cloud only` o `Local only`. `Cloud only` usa `OLLAMA_API_KEY` con `https://ollama.com`. Le modalità supportate da host chiedono l’URL di base (predefinito `http://127.0.0.1:11434`), rilevano i modelli disponibili e suggeriscono valori predefiniti. `Cloud + Local` controlla anche se quell’host Ollama ha effettuato l’accesso per l’accesso cloud. Maggiori dettagli: [Ollama](</it/providers/ollama>).

Moonshot e Kimi Coding

Le configurazioni Moonshot (Kimi K2) e Kimi Coding vengono scritte automaticamente. Maggiori dettagli: [Moonshot AI (Kimi + Kimi Coding)](</it/providers/moonshot>).

Provider personalizzato

Funziona con endpoint compatibili con OpenAI e compatibili con Anthropic.

L’onboarding interattivo supporta le stesse opzioni di archiviazione della chiave API degli altri flussi con chiave API del provider:

  * **Incolla ora la chiave API** (testo semplice)
  * **Usa riferimento a secret** (riferimento env o riferimento provider configurato, con convalida preflight)


Flag non interattivi:

  * `--auth-choice custom-api-key`
  * `--custom-base-url`
  * `--custom-model-id`
  * `--custom-api-key` (opzionale; fallback a `CUSTOM_API_KEY`)
  * `--custom-provider-id` (opzionale)
  * `--custom-compatibility <openai|anthropic>` (opzionale; predefinito `openai`)
  * `--custom-image-input` / `--custom-text-input` (opzionale; sovrascrive la capacità di input del modello dedotta)

Salta

Lascia l’autenticazione non configurata.

Comportamento del modello:

  * Scegli il modello predefinito dalle opzioni rilevate oppure inserisci provider e modello manualmente.
  * L’onboarding del provider personalizzato deduce il supporto immagini per gli ID modello comuni e chiede solo quando il nome del modello è sconosciuto.
  * Quando l’onboarding parte da una scelta di autenticazione del provider, il selettore di modello preferisce automaticamente quel provider. Per Volcengine e BytePlus, la stessa preferenza corrisponde anche alle rispettive varianti coding-plan (`volcengine-plan/*`, `byteplus-plan/*`).
  * Se quel filtro del provider preferito risultasse vuoto, il selettore ripiega sul catalogo completo invece di non mostrare alcun modello.
  * La procedura guidata esegue un controllo del modello e avvisa se il modello configurato è sconosciuto o manca l’autenticazione.


Percorsi di credenziali e profili:

  * Profili di autenticazione (chiavi API + OAuth): `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * Importazione OAuth legacy: `~/.openclaw/credentials/oauth.json`


Modalità di archiviazione delle credenziali:

  * Il comportamento predefinito dell’onboarding persiste le chiavi API come valori in testo semplice nei profili di autenticazione.
  * `--secret-input-mode ref` abilita la modalità riferimento invece dell’archiviazione della chiave in testo semplice. Nella configurazione interattiva, puoi scegliere: 
    * riferimento a variabile d’ambiente (per esempio `keyRef: { source: "env", provider: "default", id: "OPENAI_API_KEY" }`)
    * riferimento a provider configurato (`file` o `exec`) con alias provider + id
  * La modalità riferimento interattiva esegue una rapida convalida preflight prima del salvataggio. 
    * Riferimenti env: convalida il nome della variabile + valore non vuoto nell’ambiente di onboarding corrente.
    * Riferimenti provider: convalida la configurazione del provider e risolve l’id richiesto.
    * Se il preflight fallisce, l’onboarding mostra l’errore e ti consente di riprovare.
  * In modalità non interattiva, `--secret-input-mode ref` è supportata solo da env. 
    * Imposta la variabile env del provider nell’ambiente del processo di onboarding.
    * I flag di chiave inline (per esempio `--openai-api-key`) richiedono che quella variabile env sia impostata; altrimenti l’onboarding fallisce rapidamente.
    * Per provider personalizzati, la modalità non interattiva `ref` memorizza `models.providers.<id>.apiKey` come `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.
    * In quel caso di provider personalizzato, `--custom-api-key` richiede che `CUSTOM_API_KEY` sia impostata; altrimenti l’onboarding fallisce rapidamente.
  * Le credenziali di autenticazione del Gateway supportano scelte in testo semplice e SecretRef nella configurazione interattiva: 
    * Modalità token: **Genera/memorizza token in testo semplice** (predefinito) o **Usa SecretRef**.
    * Modalità password: testo semplice o SecretRef.
  * Percorso SecretRef token non interattivo: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  * Le configurazioni esistenti in testo semplice continuano a funzionare senza modifiche.


## Output e componenti interni

Campi tipici in `~/.openclaw/openclaw.json`:

  * `agents.defaults.workspace`
  * `agents.defaults.skipBootstrap` quando viene passato `--skip-bootstrap`
  * `agents.defaults.model` / `models.providers` (se viene scelto Minimax)
  * `tools.profile` (l'onboarding locale usa per impostazione predefinita `"coding"` quando non è impostato; i valori espliciti esistenti vengono conservati)
  * `gateway.*` (modalità, bind, autenticazione, Tailscale)
  * `session.dmScope` (l'onboarding locale lo imposta per impostazione predefinita su `per-channel-peer` quando non è impostato; i valori espliciti esistenti vengono conservati)
  * `channels.telegram.botToken`, `channels.discord.token`, `channels.matrix.*`, `channels.signal.*`, `channels.imessage.*`
  * Allowlist dei canali (Slack, Discord, Matrix, Microsoft Teams) quando aderisci durante i prompt (i nomi vengono risolti in ID quando possibile)
  * `skills.install.nodeManager`
    * Il flag `setup --node-manager` accetta `npm`, `pnpm` o `bun`.
    * La configurazione manuale può comunque impostare `skills.install.nodeManager: "yarn"` in seguito.
  * `wizard.lastRunAt`
  * `wizard.lastRunVersion`
  * `wizard.lastRunCommit`
  * `wizard.lastRunCommand`
  * `wizard.lastRunMode`


`openclaw agents add` scrive `agents.list[]` e `bindings` opzionali.

Le credenziali WhatsApp vanno in `~/.openclaw/credentials/whatsapp/<accountId>/`. Le sessioni sono archiviate in `~/.openclaw/agents/<agentId>/sessions/`.

RPC della procedura guidata Gateway:

  * `wizard.start`
  * `wizard.next`
  * `wizard.cancel`
  * `wizard.status`


I client (app macOS e UI di controllo) possono eseguire il rendering dei passaggi senza reimplementare la logica di onboarding.

Comportamento di configurazione di Signal:

  * Scarica l'asset di rilascio appropriato
  * Lo archivia in `~/.openclaw/tools/signal-cli/<version>/`
  * Scrive `channels.signal.cliPath` nella configurazione
  * Le build JVM richiedono Java 21
  * Le build native vengono usate quando disponibili
  * Windows usa WSL2 e segue il flusso Linux di signal-cli all'interno di WSL


## Documentazione correlata

  * Hub di onboarding: [Onboarding (CLI)](</it/start/wizard>)
  * Automazione e script: [Automazione CLI](</it/start/wizard-cli-automation>)
  * Riferimento dei comandi: [`openclaw onboard`](</it/cli/onboard>)


Was this useful?YesNo