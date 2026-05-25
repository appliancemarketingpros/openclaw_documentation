---
title: Gruppi di diffusione
source_url: https://docs.openclaw.ai/it/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Panoramica

I gruppi broadcast consentono a più agenti di elaborare e rispondere allo stesso messaggio simultaneamente. Questo ti permette di creare team di agenti specializzati che lavorano insieme in un singolo gruppo WhatsApp o DM — il tutto usando un solo numero di telefono.

Ambito attuale: **solo WhatsApp** (canale web).

I gruppi broadcast vengono valutati dopo le allowlist dei canali e le regole di attivazione dei gruppi. Nei gruppi WhatsApp, questo significa che i broadcast avvengono quando OpenClaw normalmente risponderebbe (per esempio: su menzione, a seconda delle impostazioni del gruppo).

## Casi d'uso

1\. Team di agenti specializzati

Distribuisci più agenti con responsabilità atomiche e mirate:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Ogni agente elabora lo stesso messaggio e fornisce la propria prospettiva specializzata.

2\. Supporto multilingue CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Flussi di garanzia della qualità CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Automazione delle attività CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Configurazione

### Configurazione di base

Aggiungi una sezione `broadcast` di primo livello (accanto a `bindings`). Le chiavi sono gli ID peer WhatsApp:

  * chat di gruppo: JID del gruppo (ad es. `120363403215116621@g.us`)
  * DM: numero di telefono E.164 (ad es. `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Risultato:** Quando OpenClaw risponderebbe in questa chat, eseguirà tutti e tre gli agenti.

### Strategia di elaborazione

Controlla come gli agenti elaborano i messaggi:

### parallel (predefinito)

Tutti gli agenti elaborano simultaneamente:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Gli agenti elaborano in ordine (uno attende che il precedente termini):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Esempio completo

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Come funziona

### Flusso dei messaggi

* ### Arriva un messaggio in ingresso

Arriva un messaggio di un gruppo WhatsApp o un DM.

* ### Controllo broadcast

Il sistema controlla se l'ID peer è in `broadcast`.

* ### Se è nell'elenco broadcast

  * Tutti gli agenti elencati elaborano il messaggio.
  * Ogni agente ha la propria chiave di sessione e un contesto isolato.
  * Gli agenti elaborano in parallelo (impostazione predefinita) o in sequenza.


* ### Se non è nell'elenco broadcast

Si applica il routing normale (primo binding corrispondente).

### Isolamento delle sessioni

Ogni agente in un gruppo broadcast mantiene completamente separati:

  * **Chiavi di sessione** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Cronologia della conversazione** (l'agente non vede i messaggi degli altri agenti)
  * **Workspace** (sandbox separati se configurati)
  * **Accesso agli strumenti** (liste allow/deny diverse)
  * **Memoria/contesto** ([IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), ecc. separati)
  * **Buffer del contesto di gruppo** (messaggi recenti del gruppo usati per il contesto) è condiviso per peer, quindi tutti gli agenti broadcast vedono lo stesso contesto quando vengono attivati


Questo consente a ogni agente di avere:

  * Personalità diverse
  * Accesso agli strumenti diverso (ad es. sola lettura vs lettura-scrittura)
  * Modelli diversi (ad es. opus vs sonnet)
  * Skills diverse installate


### Esempio: sessioni isolate

Nel gruppo `120363403215116621@g.us` con agenti `["alfred", "baerbel"]`:

### Contesto di Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Contesto di Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Best practice

1\. Mantieni gli agenti focalizzati

Progetta ogni agente con una singola responsabilità chiara:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Buono:** Ogni agente ha un solo compito. ❌ **Scarso:** Un agente generico "dev-helper".

2\. Usa nomi descrittivi

Rendi chiaro cosa fa ogni agente:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configura accessi diversi agli strumenti

Concedi agli agenti solo gli strumenti di cui hanno bisogno:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` è in sola lettura. `fixer` può leggere e scrivere.

4\. Monitora le prestazioni

Con molti agenti, considera:

  * L'uso di `"strategy": "parallel"` (predefinito) per la velocità
  * La limitazione dei gruppi broadcast a 5-10 agenti
  * L'uso di modelli più veloci per agenti più semplici

5\. Gestisci gli errori con eleganza

Gli agenti falliscono in modo indipendente. L'errore di un agente non blocca gli altri:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Compatibilità

### Provider

I gruppi broadcast attualmente funzionano con:

  * ✅ WhatsApp (implementato)
  * 🚧 Telegram (pianificato)
  * 🚧 Discord (pianificato)
  * 🚧 Slack (pianificato)


### Routing

I gruppi broadcast funzionano insieme al routing esistente:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Risponde solo alfred (routing normale).
  * `GROUP_B`: agent1 E agent2 rispondono (broadcast).


## Risoluzione dei problemi

Gli agenti non rispondono

**Controlla:**

  1. Gli ID degli agenti esistono in `agents.list`.
  2. Il formato dell'ID peer è corretto (ad es. `120363403215116621@g.us`).
  3. Gli agenti non sono in liste deny.


**Debug:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Risponde un solo agente

**Causa:** L'ID peer potrebbe essere in `bindings` ma non in `broadcast`.

**Correzione:** Aggiungilo alla configurazione broadcast o rimuovilo dai binding.

Problemi di prestazioni

Se è lento con molti agenti:

  * Riduci il numero di agenti per gruppo.
  * Usa modelli più leggeri (sonnet invece di opus).
  * Controlla il tempo di avvio del sandbox.


## Esempi

Esempio 1: Team di revisione del codice jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**L'utente invia:** Frammento di codice.

**Risposte:**

  * code-formatter: "Indentazione corretta e suggerimenti di tipo aggiunti"
  * security-scanner: "⚠️ Vulnerabilità di SQL injection alla riga 12"
  * test-coverage: "La copertura è al 45%, mancano test per i casi di errore"
  * docs-checker: "Docstring mancante per la funzione `process_data`"

Esempio 2: Supporto multilingue jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Riferimento API

### Schema di configurazione

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Campi

Come elaborare gli agenti. `parallel` esegue tutti gli agenti simultaneamente; `sequential` li esegue nell'ordine dell'array.

JID del gruppo WhatsApp, numero E.164 o altro ID peer. Il valore è l'array di ID agente che devono elaborare i messaggi.

## Limitazioni

  1. **Numero massimo di agenti:** Nessun limite rigido, ma 10+ agenti possono essere lenti.
  2. **Contesto condiviso:** Gli agenti non vedono le risposte degli altri (per progettazione).
  3. **Ordine dei messaggi:** Le risposte parallele possono arrivare in qualsiasi ordine.
  4. **Limiti di frequenza:** Tutti gli agenti contano ai fini dei limiti di frequenza di WhatsApp.


## Miglioramenti futuri

Funzionalità pianificate:

  * [ ] Modalità contesto condiviso (gli agenti vedono le risposte degli altri)
  * [ ] Coordinamento degli agenti (gli agenti possono segnalarsi a vicenda)
  * [ ] Selezione dinamica degli agenti (scegliere gli agenti in base al contenuto del messaggio)
  * [ ] Priorità degli agenti (alcuni agenti rispondono prima degli altri)


## Correlati

  * [Instradamento dei canali](</it/channels/channel-routing>)
  * [Gruppi](</it/channels/groups>)
  * [Strumenti sandbox multi-agente](</it/tools/multi-agent-sandbox-tools>)
  * [Associazione](</it/channels/pairing>)
  * [Gestione delle sessioni](</it/concepts/session>)


Was this useful?YesNo