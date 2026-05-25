---
title: Configurazione iniziale (CLI)
source_url: https://docs.openclaw.ai/it/start/wizard
scraped_at: 2026-05-25
---

L'onboarding da CLI è il modo **consigliato** per configurare OpenClaw su macOS, Linux o Windows (tramite WSL2; fortemente consigliato). Configura un Gateway locale o una connessione a un Gateway remoto, oltre a canali, Skills e impostazioni predefinite dello spazio di lavoro in un unico flusso guidato.

bashCopy code
[code]
    openclaw onboard
[/code]

Per riconfigurare in seguito:

bashCopy code
[code]
    openclaw configureopenclaw agents add <name>
[/code]

## QuickStart vs Avanzata

L'onboarding inizia con **QuickStart** (impostazioni predefinite) vs **Avanzata** (controllo completo).

### QuickStart (impostazioni predefinite)

  * Gateway locale (loopback)
  * Spazio di lavoro predefinito (o spazio di lavoro esistente)
  * Porta del Gateway **18789**
  * Autenticazione del Gateway **Token** (generato automaticamente, anche su loopback)
  * Impostazione predefinita della policy degli strumenti per le nuove configurazioni locali: `tools.profile: "coding"` (il profilo esplicito esistente viene preservato)
  * Impostazione predefinita dell'isolamento DM: l'onboarding locale scrive `session.dmScope: "per-channel-peer"` quando non è impostato. Dettagli: [Riferimento configurazione CLI](</it/start/wizard-cli-reference#outputs-and-internals>)
  * Esposizione Tailscale **Disattivata**
  * I DM di Telegram + WhatsApp usano per impostazione predefinita una **allowlist** (ti verrà chiesto il tuo numero di telefono)


### Avanzata (controllo completo)

  * Espone ogni passaggio (modalità, spazio di lavoro, Gateway, canali, daemon, Skills).


## Cosa configura l'onboarding

La **modalità locale (predefinita)** ti guida attraverso questi passaggi:

  1. **Modello/Autenticazione** — scegli qualsiasi provider/flusso di autenticazione supportato (chiave API, OAuth o autenticazione manuale specifica del provider), incluso Custom Provider (compatibile con OpenAI, compatibile con Anthropic o rilevamento automatico Unknown). Scegli un modello predefinito. Nota di sicurezza: se questo agente eseguirà strumenti o elaborerà contenuti Webhook/hook, preferisci il modello di ultima generazione più potente disponibile e mantieni rigorosa la policy degli strumenti. I livelli più deboli/vecchi sono più facili da colpire con prompt injection. Per esecuzioni non interattive, `--secret-input-mode ref` memorizza nei profili di autenticazione riferimenti basati su env invece di valori di chiavi API in chiaro. Nella modalità non interattiva `ref`, la variabile env del provider deve essere impostata; passare flag con chiavi inline senza tale variabile env fallisce immediatamente. Nelle esecuzioni interattive, scegliere la modalità di riferimento segreto ti consente di puntare a una variabile di ambiente o a un riferimento provider configurato (`file` o `exec`), con una rapida convalida preliminare prima del salvataggio. Per Anthropic, onboarding/configure interattivo offre **Anthropic Claude CLI** come percorso locale preferito e **Anthropic API key** come percorso di produzione consigliato. Anthropic setup-token rimane inoltre disponibile come percorso di autenticazione tramite token supportato.
  2. **Spazio di lavoro** — Posizione per i file dell'agente (predefinita `~/.openclaw/workspace`). Inizializza i file bootstrap.
  3. **Gateway** — Porta, indirizzo di bind, modalità di autenticazione, esposizione Tailscale. In modalità token interattiva, scegli l'archiviazione predefinita del token in chiaro oppure opta per SecretRef. Percorso SecretRef del token non interattivo: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  4. **Canali** — canali chat integrati e inclusi come iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, QQ Bot, Signal, Slack, Telegram, WhatsApp e altri.
  5. **Daemon** — Installa un LaunchAgent (macOS), un'unità utente systemd (Linux/WSL2) o un'attività pianificata nativa di Windows con fallback sulla cartella Startup per utente. Se l'autenticazione tramite token richiede un token e `gateway.auth.token` è gestito da SecretRef, l'installazione del daemon lo convalida ma non persiste il token risolto nei metadati dell'ambiente del servizio supervisor. Se l'autenticazione tramite token richiede un token e il SecretRef del token configurato non è risolto, l'installazione del daemon viene bloccata con indicazioni pratiche. Se `gateway.auth.token` e `gateway.auth.password` sono entrambi configurati e `gateway.auth.mode` non è impostato, l'installazione del daemon viene bloccata finché la modalità non viene impostata esplicitamente.
  6. **Controllo di integrità** — Avvia il Gateway e verifica che sia in esecuzione.
  7. **Skills** — Installa Skills consigliate e dipendenze facoltative.


La **modalità remota** configura solo il client locale per connettersi a un Gateway altrove. **Non** installa né modifica nulla sull'host remoto.

## Aggiungere un altro agente

Usa `openclaw agents add <name>` per creare un agente separato con il proprio spazio di lavoro, le proprie sessioni e i propri profili di autenticazione. L'esecuzione senza `--workspace` avvia l'onboarding.

Cosa imposta:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Note:

  * Gli spazi di lavoro predefiniti seguono `~/.openclaw/workspace-<agentId>`.
  * Aggiungi `bindings` per instradare i messaggi in ingresso (l'onboarding può farlo).
  * Flag non interattivi: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Riferimento completo

Per analisi dettagliate passo per passo e output di configurazione, vedi [Riferimento configurazione CLI](</it/start/wizard-cli-reference>). Per esempi non interattivi, vedi [Automazione CLI](</it/start/wizard-cli-automation>). Per il riferimento tecnico più approfondito, inclusi i dettagli RPC, vedi [Riferimento onboarding](</it/reference/wizard>).

## Documenti correlati

  * Riferimento comandi CLI: [`openclaw onboard`](</it/cli/onboard>)
  * Panoramica onboarding: [Panoramica onboarding](</it/start/onboarding-overview>)
  * Onboarding app macOS: [Onboarding](</it/start/onboarding>)
  * Rituale di primo avvio dell'agente: [Bootstrap dell'agente](</it/start/bootstrapping>)


Was this useful?YesNo