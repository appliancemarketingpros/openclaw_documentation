---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/it/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot è l'assistente di codifica AI di GitHub. Fornisce accesso ai modelli Copilot per il tuo account e piano GitHub. OpenClaw può usare Copilot come provider di modelli in due modi diversi.

## Due modi per usare Copilot in OpenClaw

### Provider integrato (github-copilot)

Usa il flusso nativo di login tramite dispositivo per ottenere un token GitHub, quindi scambialo con token API Copilot quando OpenClaw viene eseguito. Questo è il percorso **predefinito** e più semplice perché non richiede VS Code.

* ### Esegui il comando di login

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Ti verrà chiesto di visitare un URL e inserire un codice monouso. Mantieni il terminale aperto fino al completamento.

* ### Imposta un modello predefinito

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Oppure nella configurazione:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Plugin Copilot Proxy (copilot-proxy)

Usa l'estensione VS Code **Copilot Proxy** come bridge locale. OpenClaw comunica con l'endpoint `/v1` del proxy e usa l'elenco di modelli che configuri lì.

## Flag facoltativi

Flag | Descrizione  
---|---  
`--yes` | Salta la richiesta di conferma  
`--set-default` | Applica anche il modello predefinito consigliato dal provider  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Onboarding non interattivo

Se hai già un token di accesso OAuth GitHub per Copilot, importalo durante la configurazione headless con `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Puoi anche omettere `--auth-choice`; passare `--github-copilot-token` deduce la scelta di autenticazione del provider GitHub Copilot. Se il flag viene omesso, l'onboarding ripiega su `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, quindi `GITHUB_TOKEN`. Usa `--secret-input-mode ref` con `COPILOT_GITHUB_TOKEN` impostato per archiviare un `tokenRef` basato su env invece di testo in chiaro in `auth-profiles.json`.

TTY interattivo richiesto

Il flusso di login tramite dispositivo richiede un TTY interattivo. Eseguilo direttamente in un terminale, non in uno script non interattivo o in una pipeline CI.

La disponibilità dei modelli dipende dal tuo piano

La disponibilità dei modelli Copilot dipende dal tuo piano GitHub. Se un modello viene rifiutato, prova un altro ID (ad esempio `github-copilot/gpt-4.1`).

Aggiornamento del catalogo live dall'API Copilot

Dopo che il percorso di autenticazione tramite login dispositivo (o variabile env) ha risolto un token GitHub, OpenClaw aggiorna il catalogo dei modelli on demand da `${baseUrl}/models` (lo stesso endpoint usato da VS Code Copilot), così il runtime tiene traccia dei diritti per account e delle finestre di contesto accurate senza modifiche al manifest. I nuovi modelli Copilot pubblicati diventano visibili senza un aggiornamento di OpenClaw e le finestre di contesto riflettono i limiti reali per modello (ad es. 400k per la serie gpt-5.x, 1M per le varianti interne `claude-opus-*-1m`).

Il catalogo statico incluso rimane il fallback visibile quando il discovery è disabilitato, l'utente non ha un profilo di autenticazione GitHub, lo scambio del token fallisce o la chiamata HTTPS a `/models` genera un errore. Per disattivarlo e affidarti interamente al catalogo statico del manifest (scenari offline / air-gapped):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Selezione del trasporto

Gli ID dei modelli Claude usano automaticamente il trasporto Anthropic Messages. I modelli GPT, o-series e Gemini mantengono il trasporto OpenAI Responses. OpenClaw seleziona il trasporto corretto in base al riferimento del modello.

Compatibilità delle richieste

OpenClaw invia header di richiesta in stile Copilot IDE sui trasporti Copilot, inclusi turni di follow-up per compaction integrata, risultati degli strumenti e immagini. Non abilita la continuazione Responses a livello di provider per Copilot a meno che quel comportamento non sia stato verificato rispetto all'API di Copilot.

Ordine di risoluzione delle variabili di ambiente

OpenClaw risolve l'autenticazione Copilot dalle variabili di ambiente nel seguente ordine di priorità:

Priorità | Variabile | Note  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Priorità massima, specifica di Copilot  
2 | `GH_TOKEN` | Token GitHub CLI (fallback)  
3 | `GITHUB_TOKEN` | Token GitHub standard (minima)  
  
Quando sono impostate più variabili, OpenClaw usa quella con la priorità più alta. Il flusso di login tramite dispositivo (`openclaw models auth login-github-copilot`) archivia il suo token nello store dei profili di autenticazione e ha precedenza su tutte le variabili di ambiente.

Archiviazione dei token

Il login archivia un token GitHub nello store dei profili di autenticazione e lo scambia con un token API Copilot quando OpenClaw viene eseguito. Non devi gestire il token manualmente.

## Embedding per la ricerca in memoria

GitHub Copilot può anche fungere da provider di embedding per [la ricerca in memoria](</it/concepts/memory-search>). Se hai un abbonamento Copilot e hai effettuato il login, OpenClaw può usarlo per gli embedding senza una chiave API separata.

### Rilevamento automatico

Quando `memorySearch.provider` è `"auto"` (il valore predefinito), GitHub Copilot viene provato con priorità 15 -- dopo gli embedding locali ma prima di OpenAI e di altri provider a pagamento. Se è disponibile un token GitHub, OpenClaw scopre i modelli di embedding disponibili dall'API Copilot e sceglie automaticamente il migliore.

### Configurazione esplicita

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Come funziona

  1. OpenClaw risolve il tuo token GitHub (da variabili env o profilo di autenticazione).
  2. Lo scambia con un token API Copilot di breve durata.
  3. Interroga l'endpoint `/models` di Copilot per scoprire i modelli di embedding disponibili.
  4. Sceglie il modello migliore (preferisce `text-embedding-3-small`).
  5. Invia le richieste di embedding all'endpoint `/embeddings` di Copilot.


La disponibilità dei modelli dipende dal tuo piano GitHub. Se non sono disponibili modelli di embedding, OpenClaw salta Copilot e prova il provider successivo.

## Correlati

[**Selezione dei modelli** Scelta dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**OAuth e autenticazione** Dettagli di autenticazione e regole di riutilizzo delle credenziali. ](</it/gateway/authentication>)

Was this useful?YesNo