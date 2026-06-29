---
title: Tassonomia di maturità
source_url: https://docs.openclaw.ai/it/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Tassonomia della maturità

il modello dietro la scorecard

Superfici > categorie > capacità > evidenze.

50 superfici raggruppate in 4 famiglie, con ogni categoria collegata alla documentazione canonica e agli ID di copertura QA.

Sfoglia le aree di prodotto / Apri la tassonomia dettagliata / [Visualizza i punteggi](</it/maturity/scorecard>)

## Come leggere questa pagina

Una superficie è un'area di prodotto come il runtime Gateway, Discord o l'app macOS. Ogni superficie contiene categorie e ogni categoria contiene i controlli a livello di capacità coperti dagli scenari QA. Usa la scorecard per la valutazione a livello di rilascio; usa questa pagina per esaminare il modello sottostante.

## Livelli di maturità

M0PianificatoLa direzione è nota, ma non esiste alcun percorso utente supportato.Promozione: esistono issue di progettazione, proprietario e superficie di destinazione.

M1SperimentaleImplementato con limitazioni, flag, build da sorgente o flussi riservati ai maintainer.Promozione: il maintainer può eseguire lo scenario dal main corrente.

M2AlphaGli utenti reali possono provarlo, ma sono previste modifiche non compatibili e UX incompleta.Promozione: configurazione documentata, test di base, limitazioni note e almeno una prova in ambiente reale.

M3BetaEsiste un percorso pubblico e il workflow principale è utilizzabile con limitazioni circoscritte.Promozione: documentazione di installazione/aggiornamento, test di regressione, runbook di supporto e prova dello scenario riuscita nell'ambiente previsto.

M4StabilePercorso consigliato per gli utenti normali. Gli errori vengono trattati come regressioni.Promozione: gate di rilascio, percorso doctor/risoluzione dei problemi, documentazione ampia e prove ripetute nel mondo reale.

M5ClawesomeRifinito, piacevole, ben strumentato e competitivo con il miglior workflow comparabile.Promozione: Stabile più superamento della scorecard utente con utenti rappresentativi.

## Aree di prodotto

### Core

CLI M4Stabile7 aree - 90% completo Runtime Gateway M4Stabile13 aree - 89% completo Runtime agente M3Beta9 aree - 79% completo Sessione, memoria e motore di contesto M3Beta9 aree - 79% completo Framework dei canali M3Beta8 aree - 79% completo Osservabilità M3Beta5 aree - 79% completo App Web Gateway M3Beta6 aree - 79% completo Plugin M3Beta9 aree - 79% completo Sicurezza, autenticazione, abbinamento e segreti M3Beta6 aree - 79% completo Automazione: Cron, hook, attività, polling M3Beta6 aree - 79% completo Comprensione e generazione dei media M2Alpha6 aree - 68% completo Voce e conversazione in tempo reale M2Alpha6 aree - 68% completo TUI M2Alpha5 aree - 66% completo ClawHub M2Alpha4 aree - 62% completo OpenClaw App SDK M2Alpha6 aree - 53% completo

### Piattaforma

host Gateway Linux M4Stabile5 aree - 89% completo host Gateway macOS M4Stabile7 aree - 88% completo hosting Docker e Podman M3Beta4 aree - 79% completo Windows tramite WSL2 M3Beta6 aree - 79% completo Raspberry Pi e piccoli dispositivi Linux M3Beta4 aree - 79% completo app complementare macOS M3Beta8 aree - 78% completo app Android M2Alpha7 aree - 66% completo Windows nativo M2Alpha4 aree - completato al 66% Hosting Kubernetes M2Alpha4 aree - completato al 61% App iOS M1Sperimentale8 aree - completato al 44% Percorso di installazione Nix M1Sperimentale5 aree - completato al 44% Superfici companion watchOS M1Sperimentale5 aree - completato al 44% App companion Linux M0Pianificato5 aree - completato al 21% App companion Windows nativa M0Pianificato5 aree - completato al 21%

### Canale

Discord M4Stabile6 aree - completato all'87% Telegram M3Beta5 aree - completato al 78% Slack M3Beta5 aree - completato al 78% iMessage e BlueBubbles M3Beta5 aree - completato al 78% WhatsApp M3Beta5 aree - completato al 78% Matrix M2Alpha6 aree - completato al 67% Google Chat M2Alpha5 aree - completato al 66% Microsoft Teams M2Alpha5 aree - completato al 66% Signal M2Alpha5 aree - completato al 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canali regionali M2Alpha4 aree - completato al 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 aree - completato al 54% Canale di chiamata vocale M1Sperimentale5 aree - completato al 44%

### Provider e strumento

Automazione del browser, exec e strumenti sandbox M3Beta3 aree - completato al 79% Percorso provider OpenAI e Codex M3Beta5 aree - completato al 79% Strumenti di ricerca web M3Beta4 aree - completato al 79% Percorso provider Anthropic M3Beta5 aree - completato al 78% Percorso provider Google M3Beta5 aree - completato al 78% Percorso provider OpenRouter M3Beta4 aree - completato al 78% Strumenti di generazione di immagini, video e musica M2Alpha5 aree - completato al 68% Provider di modelli locali: Ollama, vLLM, SGLang, LM Studio M2Alpha5 aree - completato al 68% Provider ospitati a coda lunga M2Alpha3 aree - completato al 68%

## Dettagli

### Core

CLI - M4 Stabile - 7 aree

I normali percorsi di configurazione e riparazione sono documentati nella documentazione di installazione, CLI e Gateway. I percorsi Windows specifici della piattaforma sono tracciati nelle righe Windows tramite WSL2 e Windows nativo.

Copertura Sperimentale - 4%Qualità Stabile - 83%Completezza Stabile - 90%Parziale - 6

Configurazione CLI 6 funzionalità / supportate da LTS

Sperimentale17%

Stabile89%

Stabile90%

[Indice](</it/install>), [Programma di installazione](</it/install/installer>), [Node](</it/install/node>), [Aggiornamento](</it/install/updating>)

Onboarding e configurazione dell'autenticazione 5 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Onboard](</it/cli/onboard>), [Configure](</it/cli/configure>), [Panoramica sull'onboarding](</it/start/onboarding-overview>)

Configurazione di Plugin e canali 5 funzionalità

Sperimentale0%

Beta75%

Stabile89%

[Onboard](</it/cli/onboard>), [Plugin](</it/cli/plugins>), [Canali](</it/cli/channels>)

Gestione del servizio Gateway 5 funzionalità / supportate da LTS

Sperimentale14%

Stabile87%

Stabile90%

[Gateway](</it/cli/gateway>), [Aggiornamento](</it/install/updating>), [Risoluzione dei problemi](</it/gateway/troubleshooting>)

Osservabilità CLI 5 funzionalità / supportate da LTS

Sperimentale0%

Stabile89%

Stabile90%

[Stato](</it/cli/status>), [Salute](</it/cli/health>), [Log](</it/cli/logs>), [Diagnostica](</it/gateway/diagnostics>)

Doctor 10 funzionalità / supportate da LTS

Sperimentale0%

Stabile89%

Stabile90%

[Doctor](</it/cli/doctor>), [Doctor](</it/gateway/doctor>), [Segreti](</it/gateway/secrets>), [Risoluzione dei problemi](</it/gateway/troubleshooting>)

Aggiornamenti e upgrade 5 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Aggiornamento](</it/install/updating>), [Update](</it/cli/update>), [Risoluzione dei problemi](</it/gateway/troubleshooting>)

Runtime Gateway - M4 Stabile - 13 aree

L'architettura di base, l'autenticazione, l'abbinamento, la documentazione del protocollo, la documentazione del demone e i runbook CLI sono ampi e aggiornati.

Copertura sperimentale - 6%Qualità stabile - 81%Completezza stabile - 89%Parziale - 12

Approvazioni ed esecuzione remota 6 funzionalità / con supporto LTS

Sperimentale0%

Beta75%

Stabile89%

[Protocollo](</it/gateway/protocol>), [Indice](</it/gateway/security>)

API HTTP 4 funzionalità / con supporto LTS

Sperimentale25%

Stabile90%

Stabile90%

[Indice](</it/gateway>), [API HTTP Openai](</it/gateway/openai-http-api>), [API HTTP Openresponses](</it/gateway/openresponses-http-api>), [API HTTP di invocazione degli strumenti](</it/gateway/tools-invoke-http-api>), [Hook](</it/automation/hooks>), [Indice](</it/web>)

Superficie web ospitata 4 funzionalità / con supporto LTS

Sperimentale0%

Stabile89%

Stabile90%

[Indice](</it/gateway>), [Architettura](</it/concepts/architecture>), [UI di controllo](</it/web/control-ui>), [Webchat](</it/web/webchat>), [Canvas](</it/refactor/canvas>)

API RPC ed eventi del Gateway 20 funzionalità / con supporto LTS

Sperimentale9%

Stabile90%

Stabile90%

[Protocollo](</it/gateway/protocol>), [Indice](</it/gateway>), [Architettura](</it/concepts/architecture>)

Autenticazione e abbinamento dispositivo 10 funzionalità / con supporto LTS

Sperimentale0%

Beta75%

Stabile89%

[Protocollo](</it/gateway/protocol>), [Abbinamento](</it/gateway/pairing>), [Indice](</it/gateway/security>)

Accesso e rilevamento di rete 6 funzionalità / con supporto LTS

Sperimentale0%

Beta75%

Stabile89%

[Indice](</it/gateway>), [Rilevamento](</it/gateway/discovery>), [Protocollo](</it/gateway/protocol>)

Nodi e funzionalità remote 8 funzionalità

Sperimentale0%

Beta75%

Stabile89%

[Protocollo](</it/gateway/protocol>), [Architettura](</it/concepts/architecture>), [Indice](</it/nodes>)

Integrità, diagnostica e riparazione 7 funzionalità / con supporto LTS

Sperimentale0%

Beta75%

Stabile89%

[Indice](</it/gateway>), [Diagnostica](</it/gateway/diagnostics>), [Doctor](</it/gateway/doctor>)

Compatibilità del protocollo 7 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Protocollo](</it/gateway/protocol>), [Architettura](</it/concepts/architecture>), [Typebox](</it/concepts/typebox>), [Protocollo bridge](</it/gateway/bridge-protocol>)

Ruoli e autorizzazioni 5 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Protocollo](</it/gateway/protocol>), [Indice](</it/gateway/security>)

Ciclo di vita del Gateway 7 funzionalità / supportate da LTS

Sperimentale33%

Stabile90%

Stabile90%

[Indice](</it/gateway>), [Architettura](</it/concepts/architecture>)

Controlli di sicurezza 6 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Indice](</it/gateway/security>), [Protocollo](</it/gateway/protocol>), [Individuazione](</it/gateway/discovery>)

Connessione WebSocket 8 funzionalità / supportate da LTS

Sperimentale13%

Stabile90%

Stabile90%

[Protocollo](</it/gateway/protocol>), [Architettura](</it/concepts/architecture>)

Runtime dell'agente - M3 Beta - 9 aree

Il loop principale, i modelli, l'instradamento dei provider e lo streaming degli strumenti sono elementi di prima classe, ma il comportamento dei provider cambia settimanalmente e richiede prove di scenario per ogni rilascio.

Copertura Experimental - 33%Qualità Beta - 78%Completezza Beta - 79%Parziale - 6

Esecuzione dei turni dell'agente 3 funzionalità / supportate da LTS

Sperimentale29%

Beta79%

Beta79%

[Loop dell'agente](</it/concepts/agent-loop>), [Agente](</it/cli/agent>), [Runtime degli agenti](</it/concepts/agent-runtimes>)

Runtime esterni e subagenti 4 funzionalità

Sperimentale30%

Beta79%

Beta79%

[Runtime degli agenti](</it/concepts/agent-runtimes>), [Anthropic](</it/providers/anthropic>), [Google](</it/providers/google>), [Subagenti](</it/tools/subagents>)

Esecuzione con provider ospitati 5 funzionalità / supportate da LTS

Sperimentale20%

Beta79%

Beta79%

[Openai](</it/providers/openai>), [Anthropic](</it/providers/anthropic>), [Google](</it/providers/google>), [Modelli](</it/concepts/models>)

Provider locali e self-hosted 5 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Ollama](</it/providers/ollama>), [Modelli](</it/concepts/models>), [Agente](</it/cli/agent>)

Selezione del modello e del runtime 4 funzionalità / supportate da LTS

Sperimentale25%

Beta79%

Beta79%

[Modelli](</it/concepts/models>), [Modelli](</it/cli/models>), [Openai](</it/providers/openai>), [Runtime degli agenti](</it/concepts/agent-runtimes>)

Autenticazione dei provider 10 funzionalità / supportate da LTS

Sperimentale24%

Beta79%

Beta79%

[Modelli](</it/concepts/models>), [Agente](</it/cli/agent>), [Modelli](</it/cli/models>), [Openai](</it/providers/openai>), [Anthropic](</it/providers/anthropic>), [Google](</it/providers/google>), [Subagenti](</it/tools/subagents>)

Streaming e avanzamento 2 funzionalità

Alpha56%

Beta79%

Beta79%

[Streaming](</it/concepts/streaming>), [Loop dell'agente](</it/concepts/agent-loop>)

Chiamate agli strumenti e gestione delle risposte 3 funzionalità / supportate da LTS

Alpha65%

Beta79%

Beta79%

[Loop dell'agente](</it/concepts/agent-loop>), [Ollama](</it/providers/ollama>)

Controlli di esecuzione degli strumenti 6 capacità / supportate da LTS

Alpha50%

Beta79%

Beta79%

[Sandbox vs criterio degli strumenti vs privilegi elevati](</it/gateway/sandbox-vs-tool-policy-vs-elevated>), [Loop dell'agente](</it/concepts/agent-loop>), [Subagenti](</it/tools/subagents>)

Sessione, memoria e motore di contesto - M3 Beta - 9 aree

Documentazione solida e implementazione attiva. La maturità dipende dalla durabilità delle trascrizioni, dalla qualità della Compaction e dalla parità tra client.

Copertura Sperimentale - 30%Qualità Beta - 77%Completezza Beta - 79%Parziale - 6

Gestione delle sessioni CLI e delle trascrizioni 2 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Sessione](</it/concepts/session>), [Compaction della gestione delle sessioni](</it/reference/session-management-compaction>), [Sessioni](</it/cli/sessions>)

Gestione dei token 3 funzionalità / con supporto LTS

Sperimentale20%

Beta79%

Beta79%

[Compaction](</it/concepts/compaction>), [Contesto](</it/concepts/context>), [Compaction della gestione delle sessioni](</it/reference/session-management-compaction>)

Motore di contesto 2 funzionalità / con supporto LTS

Alpha57%

Beta79%

Beta79%

[Contesto](</it/concepts/context>), [Motore di contesto](</it/concepts/context-engine>), [Harness del motore di contesto Codex](</it/plan/codex-context-engine-harness>)

Cronologia cross-client e parità delle sessioni 2 funzionalità

Sperimentale40%

Beta79%

Beta79%

[Chat web](</it/web/webchat>), [Android](</it/platforms/android>), [Routing dei canali](</it/channels/channel-routing>)

Diagnostica, manutenzione e ripristino 3 funzionalità

Sperimentale40%

Beta79%

Beta79%

[Diagnostica](</it/gateway/diagnostics>), [Compaction della gestione delle sessioni](</it/reference/session-management-compaction>), [Flag](</it/diagnostics/flags>)

Prompt e contesto di base 2 funzionalità / con supporto LTS

Sperimentale38%

Beta79%

Beta79%

[Contesto](</it/concepts/context>), [Igiene delle trascrizioni](</it/reference/transcript-hygiene>), [Discord](</it/channels/discord>)

Memoria 5 funzionalità

Sperimentale46%

Beta79%

Beta79%

[Configurazione della memoria](</it/reference/memory-config>), [Qmd della memoria](</it/concepts/memory-qmd>), [Memoria](</it/concepts/memory>), [Discord](</it/channels/discord>)

Routing delle sessioni 2 funzionalità / con supporto LTS

Sperimentale25%

Beta79%

Beta79%

[Sessione](</it/concepts/session>), [Routing dei canali](</it/channels/channel-routing>), [Discord](</it/channels/discord>)

Persistenza delle trascrizioni 2 funzionalità / supportate da LTS

Sperimentale0%

Alpha68%

Beta79%

[Compaction della gestione delle sessioni](</it/reference/session-management-compaction>), [Igiene delle trascrizioni](</it/reference/transcript-hygiene>)

Framework dei canali - M3 Beta - 8 aree

Molti canali condividono i contratti di consegna e routing del Gateway, ma il comportamento dei canali varia in base all'API upstream e ai vincoli delle policy dell'account.

Copertura sperimentale - 13%Qualità Beta - 76%Completezza Beta - 79%Parziale - 5

Comandi e approvazioni delle azioni dei canali 5 funzionalità

Sperimentale0%

Beta79%

Beta79%

[Gruppi](</it/channels/groups>), [Discord](</it/channels/discord>), [Google Chat](</it/channels/googlechat>), [Signal](</it/channels/signal>), [Matrix](</it/channels/matrix>)

Configurazione dei canali 5 funzionalità / con supporto LTS

Sperimentale14%

Beta79%

Beta79%

[Indice](</it/channels>), [Abbinamento](</it/channels/pairing>), [Risoluzione dei problemi](</it/channels/troubleshooting>), [Plugin di canale SDK](</it/plugins/sdk-channel-plugins>)

Comportamento dei thread di gruppo e delle stanze ambientali 5 funzionalità

Sperimentale36%

Beta79%

Beta79%

[Gruppi](</it/channels/groups>), [Messaggi di gruppo](</it/channels/group-messages>), [Eventi delle stanze ambientali](</it/channels/ambient-room-events>), [Gruppi di trasmissione](</it/channels/broadcast-groups>), [Discord](</it/channels/discord>)

Accesso in ingresso e gate di identità 5 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Gruppi di accesso](</it/channels/access-groups>), [Gruppi](</it/channels/groups>), [Discord](</it/channels/discord>), [LINE](</it/channels/line>)

Allegati multimediali e dati avanzati dei canali 4 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[LINE](</it/channels/line>), [Signal](</it/channels/signal>), [Google Chat](</it/channels/googlechat>), [Matrix](</it/channels/matrix>), [Discord](</it/channels/discord>)

Recapito in uscita e pipeline di risposta 4 funzionalità / con supporto LTS

Sperimentale38%

Beta79%

Beta79%

[Gruppi](</it/channels/groups>), [Eventi delle stanze ambientali](</it/channels/ambient-room-events>), [Discord](</it/channels/discord>), [Matrix](</it/channels/matrix>), [Canali di configurazione](</it/gateway/config-channels>)

Instradamento e recapito delle conversazioni 10 funzionalità / con supporto LTS

Sperimentale19%

Beta79%

Beta79%

[Instradamento dei canali](</it/channels/channel-routing>), [Gruppi](</it/channels/groups>), [Discord](</it/channels/discord>), [Matrix](</it/channels/matrix>), [Risoluzione dei problemi](</it/channels/troubleshooting>), [Riferimento di configurazione](</it/gateway/configuration-reference>)

Stato di salute e controlli operatore 4 funzionalità / con supporto LTS

Sperimentale0%

Beta79%

Beta79%

[Stato di salute](</it/gateway/health>), [Riferimento alla configurazione](</it/gateway/configuration-reference>), [Risoluzione dei problemi](</it/channels/troubleshooting>), [Discord](</it/channels/discord>)

Observability - M3 Beta - 5 areas

Esiste documentazione su OTel, Prometheus, logging e diagnostica. Serve una revisione pubblica della maturità su "cosa gli operatori dovrebbero controllare per primo".

Copertura sperimentale - 18%Qualità Beta - 75%Completezza Beta - 79%Parziale - 3

Integrità e riparazione 12 funzionalità / supportate da LTS

Sperimentale28%

Beta79%

Beta79%

[Integrità](</it/gateway/health>), [Telegram](</it/channels/telegram>), [Doctor](</it/cli/doctor>), [Doctor](</it/gateway/doctor>), [Sottopercorsi SDK](</it/plugins/sdk-subpaths>), [Integrità](</it/cli/health>), [Protocollo](</it/gateway/protocol>)

Registrazione 5 funzionalità / supportate da LTS

Sperimentale0%

Alpha68%

Beta79%

[Registrazione](</it/logging>), [Registrazione](</it/gateway/logging>), [Log](</it/cli/logs>)

Raccolta diagnostica 8 funzionalità

Sperimentale30%

Beta79%

Beta79%

[Diagnostica](</it/gateway/diagnostics>), [Integrità](</it/gateway/health>), [Harness Codex](</it/plugins/codex-harness>), [Protocollo](</it/gateway/protocol>)

Esportazione telemetria 13 funzionalità

Sperimentale33%

Beta79%

Beta79%

[Hook](</it/plugins/hooks>), [Opentelemetry](</it/gateway/opentelemetry>), [Registrazione](</it/logging>), [Sottopercorsi SDK](</it/plugins/sdk-subpaths>), [Diagnostica Otel](</it/plugins/reference/diagnostics-otel>), [Prometheus](</it/gateway/prometheus>), [Diagnostica Prometheus](</it/plugins/reference/diagnostics-prometheus>)

Diagnostica sessione 4 funzionalità / supportate da LTS

Sperimentale0%

Alpha68%

Beta79%

[Opentelemetry](</it/gateway/opentelemetry>), [Prometheus](</it/gateway/prometheus>), [Diagnostica](</it/gateway/diagnostics>), [Protocollo](</it/gateway/protocol>)

App web Gateway - M3 Beta - 6 aree

L'interfaccia utente web è documentata con flussi di pairing, chat, PWA, Talk, push e Gateway remoto. Promuovere dopo le scorecard cross-browser e mobile-PWA.

Copertura sperimentale - 4%Qualità Beta - 74%Completezza Beta - 79%Nessuno

Conversazione in tempo reale nel browser 5 capacità

Sperimentale0%

Alpha68%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Protocollo](</it/gateway/protocol>), [Conversazione](</it/nodes/talk>)

Accesso e attendibilità del browser 5 capacità

Sperimentale0%

Alpha68%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Dashboard](</it/web/dashboard>), [Tailscale](</it/gateway/tailscale>), [Remoto](</it/gateway/remote>)

Configurazione 5 capacità

Sperimentale0%

Alpha68%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Configurazione](</it/gateway/configuration>)

Interfaccia utente del browser 10 capacità

Sperimentale8%

Beta79%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Indice](</it/web>), [Dashboard](</it/web/dashboard>), [Protocollo](</it/gateway/protocol>)

Conversazioni WebChat 15 capacità

Sperimentale10%

Beta79%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Webchat](</it/web/webchat>), [Primi passi](</it/start/getting-started>), [Instradamento dei canali](</it/channels/channel-routing>), [Operazioni sicure sui file](</it/gateway/security/secure-file-operations>)

Console dell'operatore 10 capacità

Sperimentale8%

Beta79%

Beta79%

[Interfaccia di controllo](</it/web/control-ui>), [Integrità](</it/gateway/health>), [Protocollo](</it/gateway/protocol>), [Dashboard](</it/web/dashboard>)

Plugin - M3 Beta - 9 aree

Esistono documentazione ampia e solide prove di runtime interno per manifest, discovery, caricamento, architettura di provider/strumenti e confini di approvazione. Mantieni la riga in beta finché la prova dell'API SDK pubblica/dei sottopercorsi e della distribuzione esterna non sarà più solida.

Copertura Sperimentale - 12%Qualità Beta - 72%Completezza Beta - 79%Parziale - 7

Creazione e pacchettizzazione dei plugin 8 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Creazione di plugin](</it/plugins/building-plugins>), [Panoramica SDK](</it/plugins/sdk-overview>), [Punti di ingresso SDK](</it/plugins/sdk-entrypoints>), [Sottopercorsi SDK](</it/plugins/sdk-subpaths>), [Manifest](</it/plugins/manifest>), [Riferimento](</it/plugins/reference>)

Plugin in bundle 5 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Inventario dei plugin](</it/plugins/plugin-inventory>), [Plugin](</it/cli/plugins>), [Architettura interna](</it/plugins/architecture-internals>)

Plugin Canvas 6 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Canvas](</it/plugins/reference/canvas>), [Canvas](</it/refactor/canvas>), [Riferimento di configurazione](</it/gateway/configuration-reference>)

Installazione ed esecuzione dei plugin 6 funzionalità / con supporto LTS

Sperimentale35%

Beta79%

Beta79%

[Architettura](</it/plugins/architecture>), [Architettura interna](</it/plugins/architecture-internals>), [Plugin](</it/cli/plugins>)

Plugin di canale 5 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Plugin di canale SDK](</it/plugins/sdk-channel-plugins>), [Ingresso canale SDK](</it/plugins/sdk-channel-inbound>), [Uscita canale SDK](</it/plugins/sdk-channel-outbound>)

Plugin provider e strumenti 6 funzionalità / con supporto LTS

Sperimentale43%

Beta79%

Beta79%

[Plugin provider SDK](</it/plugins/sdk-provider-plugins>), [Plugin strumento](</it/plugins/tool-plugins>), [Aggiunta di funzionalità](</it/plugins/adding-capabilities>)

Approvazioni dei plugin 6 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Richieste di autorizzazione dei plugin](</it/plugins/plugin-permission-requests>), [Approvazioni exec](</it/tools/exec-approvals>), [Plugin di canale SDK](</it/plugins/sdk-channel-plugins>)

Pubblicazione dei plugin 6 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Plugin](</it/cli/plugins>), [Compatibilità](</it/plugins/compatibility>), [Pubblicazione](</it/clawhub/publishing>)

Test dei plugin 6 funzionalità

Sperimentale27%

Beta79%

Beta79%

[Test dell'Sdk](</it/plugins/sdk-testing>), [Configurazione dell'Sdk](</it/plugins/sdk-setup>), [Harness Codex](</it/plugins/codex-harness>)

Sicurezza, autenticazione, pairing e segreti - M3 Beta - 6 aree

Esistono buone superfici di documentazione e hardening. Promuovere dopo che esecuzioni regolari di scenari di upgrade e sicurezza dimostrano l'assenza di regressioni nella configurazione.

Copertura Sperimentale - 16%Qualità Beta - 72%Completezza Beta - 79%Parziale - 5

Policy di approvazione e protezioni degli strumenti 2 funzionalità / con supporto LTS

Alpha50%

Beta79%

Beta79%

[Approvazioni Exec](</it/tools/exec-approvals>), [Approvazioni](</it/cli/approvals>), [Richieste di autorizzazione Plugin](</it/plugins/plugin-permission-requests>), [Controlli di audit](</it/gateway/security/audit-checks>)

Autenticazione Gateway e accesso remoto 9 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Indice](</it/gateway/security>), [Runbook di esposizione](</it/gateway/security/exposure-runbook>), [Autenticazione proxy attendibile](</it/gateway/trusted-proxy-auth>), [Tailscale](</it/gateway/tailscale>), [Remoto](</it/gateway/remote>), [Riferimento di configurazione](</it/gateway/configuration-reference>), [Gateway](</it/cli/gateway>), [Doctor](</it/cli/doctor>), [UI di controllo](</it/web/control-ui>), [Controllo browser](</it/tools/browser-control>), [Controlli di audit](</it/gateway/security/audit-checks>)

Controllo dell'accesso ai canali 3 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Pairing](</it/channels/pairing>), [Telegram](</it/channels/telegram>), [Gruppi di accesso](</it/channels/access-groups>), [Controlli di audit](</it/gateway/security/audit-checks>)

Pairing di dispositivi e Node 11 funzionalità / con supporto LTS

Sperimentale0%

Alpha68%

Beta79%

[Protocollo](</it/gateway/protocol>), [Dispositivi](</it/cli/devices>), [Pairing](</it/channels/pairing>), [Pairing](</it/gateway/pairing>), [Ambiti operatore](</it/gateway/operator-scopes>), [UI di controllo](</it/web/control-ui>), [Webchat](</it/web/webchat>), [Approvazioni](</it/cli/approvals>)

Fiducia nei Plugin 2 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Manifest](</it/plugins/manifest>), [Richieste di autorizzazione Plugin](</it/plugins/plugin-permission-requests>), [Gestire i Plugin](</it/plugins/manage-plugins>), [Controlli di audit](</it/gateway/security/audit-checks>)

Igiene di credenziali e segreti 5 funzionalità / con supporto LTS

Sperimentale46%

Beta79%

Beta79%

[Autenticazione](</it/gateway/authentication>), [Modelli](</it/cli/models>), [Openai](</it/providers/openai>), [Oauth](</it/concepts/oauth>), [Segreti](</it/gateway/secrets>), [Segreti](</it/cli/secrets>), [Superficie credenziali Secretref](</it/reference/secretref-credential-surface>), [Controlli di audit](</it/gateway/security/audit-checks>)

Automazione: cron, hook, attività, polling - M3 Beta - 6 aree

Documentato e utilizzabile, ma la prova degli scenari dovrebbe coprire consegna non presidiata, nuovi tentativi e visibilità degli errori.

Copertura Sperimentale - 2%Qualità Beta - 72%Completezza Beta - 79%Nessuno

Processi Cron 15 capacità

Sperimentale0%

Beta79%

Beta79%

[Processi Cron](</it/automation/cron-jobs>), [Cron](</it/cli/cron>), [Protocollo](</it/gateway/protocol>), [Attività](</it/automation/tasks>), [Discord](</it/channels/discord>)

Ingresso eventi 15 capacità

Sperimentale0%

Alpha68%

Beta79%

[Telegram](</it/channels/telegram>), [Zalo](</it/channels/zalo>), [Risoluzione dei problemi](</it/channels/troubleshooting>), [iMessage da Bluebubbles](</it/channels/imessage-from-bluebubbles>), [Integrazione Gmail Pubsub](</it/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</it/automation/cron-jobs>), [Webhook](</it/cli/webhooks>), [Webhook](</it/automation/cron-jobs#webhooks>), [Webhook](</it/automation/cron-jobs>)

Hook di automazione 11 capacità

Sperimentale0%

Alpha68%

Beta79%

[Hook](</it/automation/hooks>), [Hook](</it/cli/hooks>), [Hook](</it/plugins/hooks>), [Richieste di autorizzazione Plugin](</it/plugins/plugin-permission-requests>), [Sottopercorsi SDK](</it/plugins/sdk-subpaths>)

Attività e flussi in background 10 capacità

Sperimentale0%

Alpha68%

Beta79%

[Attività](</it/automation/tasks>), [Indice](</it/automation>), [Attività](</it/cli/tasks>), [TaskFlow](</it/automation/taskflow>), [Runtime SDK](</it/plugins/sdk-runtime>)

Heartbeat 5 capacità

Sperimentale14%

Beta79%

Beta79%

[Indice](</it/automation>), [Heartbeat](</it/gateway/heartbeat>), [Impegni](</it/concepts/commitments>)

Controlli di polling 10 capacità

Sperimentale0%

Alpha68%

Beta79%

[Polling](</it/cli/message>), [Messaggio](</it/cli/message>), [Telegram](</it/channels/telegram>), [Microsoft Teams](</it/channels/msteams>), [Processo in background](</it/gateway/background-process>)

Comprensione e generazione dei contenuti multimediali - M2 Alpha - 6 aree

Esiste un'ampia superficie di capacità, ma la variabilità dei provider, i limiti dei file e la parità tra Node e app la rendono non ancora stabile.

Copertura Sperimentale - 2%Qualità Alpha - 64%Completezza Alpha - 68%Nessuno

Acquisizione e accesso ai media 8 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Panoramica media](</it/tools/media-overview>), [Comprensione dei media](</it/nodes/media-understanding>), [Operazioni sicure sui file](</it/gateway/security/secure-file-operations>), [Pdf](</it/tools/pdf>), [Generazione immagini](</it/tools/image-generation>), [Qr](</it/cli/qr>), [Line](</it/channels/line>), [Whatsapp](</it/channels/whatsapp>)

Gestione dei media dei canali 5 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Immagini](</it/nodes/images>), [Panoramica media](</it/tools/media-overview>), [Discord](</it/channels/discord>)

Configurazione dei media 1 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Panoramica media](</it/tools/media-overview>), [Generazione immagini](</it/tools/image-generation>), [Manifest](</it/plugins/manifest>), [Harness Codex](</it/plugins/codex-harness>)

Distribuzione text-to-speech 2 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Tts](</it/tools/tts>), [Panoramica media](</it/tools/media-overview>), [Discord](</it/channels/discord>)

Comprensione dei media 12 funzionalità

Sperimentale7%

Alpha69%

Alpha69%

[Audio](</it/nodes/audio>), [Comprensione dei media](</it/nodes/media-understanding>), [Panoramica media](</it/tools/media-overview>), [Whatsapp](</it/channels/whatsapp>), [Immagini](</it/nodes/images>), [Infer](</it/cli/infer>), [Pdf](</it/tools/pdf>)

Generazione di media 17 funzionalità

Sperimentale5%

Alpha69%

Alpha69%

[Generazione immagini](</it/tools/image-generation>), [Panoramica media](</it/tools/media-overview>), [Skills](</it/tools/skills>), [Generazione musicale](</it/tools/music-generation>), [Generazione video](</it/tools/video-generation>)

Voce e conversazione in tempo reale - M2 Alpha - 6 aree

Esistono più implementazioni tra Control UI, app e provider. Sono necessarie scorecard su latenza, modalità di errore e configurazione prima della beta.

Copertura Sperimentale - 0%Qualità Alpha - 61%Completezza Alpha - 68%Nessuno

Provider Talk 7 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Openai](</it/providers/openai>), [Google](</it/providers/google>), [Plugin provider SDK](</it/plugins/sdk-provider-plugins>), [Talk](</it/nodes/talk>), [Control UI](</it/web/control-ui>)

Sessioni Talk in tempo reale 11 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Talk](</it/nodes/talk>), [Control UI](</it/web/control-ui>)

Voce e trascrizione 5 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Talk](</it/nodes/talk>), [Openai](</it/providers/openai>), [Google](</it/providers/google>)

Talk nell'app nativa 4 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Talk](</it/nodes/talk>), [Voicewake](</it/platforms/mac/voicewake>)

Attivazione vocale e instradamento 4 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Voicewake](</it/nodes/voicewake>), [Voicewake](</it/platforms/mac/voicewake>), [Overlay vocale](</it/platforms/mac/voice-overlay>)

Osservabilità di Talk 5 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Control UI](</it/web/control-ui>), [Overlay vocale](</it/platforms/mac/voice-overlay>), [Talk](</it/nodes/talk>)

TUI - M2 Alpha - 5 aree

Presente nella documentazione e nel sorgente, ma meno visibile come workflow utente principale. Richiede una definizione esplicita degli scenari.

Copertura Sperimentale - 0%Qualità Alpha - 59%Completezza Alpha - 66%Nessuna

Modalità runtime 14 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Tui](</it/cli/tui>), [Tui](</it/web/tui>), [Indice](</it/cli>)

Input e comandi 8 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Tui](</it/web/tui>)

Gestione delle sessioni 3 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Tui](</it/web/tui>), [Sessioni](</it/cli/sessions>)

Esecuzione della shell locale 4 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Tui](</it/web/tui>), [Tui](</it/cli/tui>)

Rendering e sicurezza dell'output 4 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Tui](</it/web/tui>), [Qr](</it/cli/qr>), [Log](</it/cli/logs>), [Completamento](</it/cli/completion>)

ClawHub - M2 Alpha - 4 aree

Esistono documentazione pubblica e concetto di ecosistema. Servono scorecard per installazione, attendibilità, aggiornamento, rollback e compatibilità.

Copertura Sperimentale - 0%Qualità Alpha - 58%Completezza Alpha - 62%Nessuno

Pubblicazione 7 capacità

Sperimentale0%

Alpha54%

Alpha55%

[Pubblicazione](</it/clawhub/publishing>), [Creazione di Skills](</it/tools/creating-skills>), [Community](</it/plugins/community>)

Scoperta del catalogo 5 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Plugin](</it/tools/plugin>), [Plugin](</it/cli/plugins>), [Skills](</it/cli/skills>), [Skills](</it/tools/skills>), [Community](</it/plugins/community>)

Compatibilità e attendibilità 12 capacità

Sperimentale0%

Alpha55%

Alpha56%

[Plugin](</it/tools/plugin>), [Plugin](</it/cli/plugins>), [Compatibilità](</it/plugins/compatibility>), [Inventario dei Plugin](</it/plugins/plugin-inventory>), [Pubblicazione](</it/clawhub/publishing>), [Skills](</it/tools/skills>), [Configurazione di Skills](</it/tools/skills-config>)

Ciclo di vita e integrità dei Plugin 26 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Plugin](</it/tools/plugin>), [Plugin](</it/cli/plugins>), [Skills](</it/cli/skills>), [Skills](</it/tools/skills>), [Protocollo](</it/gateway/protocol>), [Bundle](</it/plugins/bundles>), [Risoluzione delle dipendenze](</it/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 aree

OpenClaw App SDK è un contratto distinto per app esterne, separato dal runtime Gateway e dal Plugin SDK. La valutazione attuale mostra un percorso `@openclaw/sdk` reale, con lacune relative a pacchettizzazione pubblica, scoperta automatica, approvazioni, helper e compatibilità.

Copertura sperimentale - 3%Qualità Alpha - 54%Completezza Alpha - 53%Nessuna

API client 4 capacità

Sperimentale0%

Alpha51%

Alpha50%

[Openclaw Sdk](</it/gateway/external-apps>), [Progettazione API Openclaw Sdk](</it/gateway/external-apps>)

Accesso al Gateway 5 capacità

Sperimentale0%

Alpha53%

Alpha54%

[Openclaw Sdk](</it/gateway/external-apps>), [Progettazione API Openclaw Sdk](</it/gateway/external-apps>), [Protocollo](</it/gateway/protocol>), [Indice](</it/gateway/security>)

Conversazioni dell'agente 6 capacità

Sperimentale0%

Alpha52%

Alpha52%

[Openclaw Sdk](</it/gateway/external-apps>), [Progettazione API Openclaw Sdk](</it/gateway/external-apps>), [Protocollo](</it/gateway/protocol>)

Eventi e approvazioni 5 capacità

Sperimentale0%

Alpha52%

Alpha52%

[Openclaw Sdk](</it/gateway/external-apps>), [Progettazione API Openclaw Sdk](</it/gateway/external-apps>), [Protocollo](</it/gateway/protocol>)

Helper per le risorse 5 capacità

Sperimentale17%

Alpha62%

Alpha53%

[Openclaw Sdk](</it/gateway/external-apps>), [Progettazione API Openclaw Sdk](</it/gateway/external-apps>)

Compatibilità 5 capacità

Sperimentale0%

Alpha54%

Alpha55%

[Progettazione API Openclaw Sdk](</it/gateway/external-apps>), [Typebox](</it/concepts/typebox>), [Protocollo](</it/gateway/protocol>)

### Piattaforma

Host Gateway Linux - M4 stabile - 5 aree

Il runtime Node è consigliato, il servizio utente systemd è documentato e le indicazioni per VPS/container sono ampie.

Copertura sperimentale - 0%Qualità beta - 75%Completezza stabile - 89%Parziale - 4

Configurazione e aggiornamenti dell'host 4 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Indice](</it/install>), [Aggiornamento](</it/install/updating>), [Linux](</it/platforms/linux>), [Indice](</it/platforms>)

Runtime Gateway e controllo del servizio 6 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Indice](</it/gateway>), [Gateway](</it/cli/gateway>), [Linux](</it/platforms/linux>), [Vps](</it/vps>)

Accesso remoto e sicurezza 6 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Remoto](</it/gateway/remote>), [Tailscale](</it/gateway/tailscale>), [Runbook di esposizione](</it/gateway/security/exposure-runbook>), [Autenticazione](</it/gateway/authentication>), [Segreti](</it/gateway/secrets>)

Diagnostica e riparazione 4 funzionalità / supportate da LTS

Sperimentale0%

Beta75%

Stabile89%

[Stato](</it/cli/status>), [Log](</it/cli/logs>), [Doctor](</it/cli/doctor>), [Diagnostica](</it/gateway/diagnostics>), [Indice](</it/gateway>)

Target di distribuzione 3 funzionalità

Sperimentale0%

Beta75%

Stabile89%

[Vps](</it/vps>), [Docker](</it/install/docker>), [Hetzner](</it/install/hetzner>), [Digitalocean](</it/install/digitalocean>), [Kubernetes](</it/install/kubernetes>), [Podman](</it/install/podman>)

host macOS Gateway - M4 stabile - 7 aree

Il percorso del servizio LaunchAgent, le modalità Gateway locale/remota, l'installazione della CLI e l'integrazione dell'app sono documentati.

Copertura sperimentale - 0%Qualità beta - 74%Completezza stabile - 88%Nessuno

Configurazione CLI 4 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Macos](</it/platforms/macos>), [Gateway in bundle](</it/platforms/mac/bundled-gateway>), [Programma di installazione](</it/install/installer>), [Node](</it/install/node>)

Integrazione del Gateway locale 9 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Macos](</it/platforms/macos>), [Gateway in bundle](</it/platforms/mac/bundled-gateway>), [Remoto](</it/platforms/mac/remote>), [Indice](</it/gateway>), [Gateway](</it/cli/gateway>), [Bonjour](</it/gateway/bonjour>)

Modalità Gateway remoto 5 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Remoto](</it/platforms/mac/remote>), [Remoto](</it/gateway/remote>), [Tailscale](</it/gateway/tailscale>)

Ciclo di vita del servizio Gateway 10 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Macos](</it/platforms/macos>), [Gateway in bundle](</it/platforms/mac/bundled-gateway>), [Gateway](</it/cli/gateway>), [Indice](</it/gateway>), [Aggiornamento](</it/cli/update>), [Aggiornamento](</it/install/updating>), [Disinstallazione](</it/install/uninstall>), [Risoluzione dei problemi](</it/gateway/troubleshooting>)

Diagnostica e osservabilità 4 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Gateway in bundle](</it/platforms/mac/bundled-gateway>), [Macos](</it/platforms/macos>), [Gateway](</it/cli/gateway>), [Doctor](</it/gateway/doctor>), [Risoluzione dei problemi](</it/gateway/troubleshooting>)

Autorizzazioni e funzionalità native 4 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Macos](</it/platforms/macos>), [Remoto](</it/platforms/mac/remote>)

Profili e isolamento 5 funzionalità

Sperimentale0%

Beta74%

Stabile88%

[Gateway multipli](</it/gateway/multiple-gateways>), [Indice](</it/gateway>), [Gateway](</it/cli/gateway>)

Hosting Docker e Podman - M3 Beta - 4 aree

La documentazione di installazione esiste e questi sono percorsi di distribuzione comuni. Promuovi dopo che gli smoke test ricorrenti di rilascio avranno acquisito il comportamento di aggiornamento e dei volumi.

Copertura Sperimentale - 7%Qualità Beta - 71%Completezza Beta - 79%Nessuno

Configurazione dei container 6 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Docker](</it/install/docker>), [Podman](</it/install/podman>)

Operazioni sui container 11 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Podman](</it/install/podman>), [Runtime VM Docker](</it/install/docker-vm-runtime>), [Docker](</it/install/docker>), [Hetzner](</it/install/hetzner>), [Hostinger](</it/install/hostinger>)

Rilascio e convalida delle immagini 5 funzionalità

Sperimentale29%

Beta79%

Beta79%

[Docker](</it/install/docker>), [Runtime VM Docker](</it/install/docker-vm-runtime>), [Convalida completa del rilascio](</it/reference/full-release-validation>)

Sandbox e strumenti per agenti 3 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Docker](</it/install/docker>), [Runtime VM Docker](</it/install/docker-vm-runtime>)

Windows via WSL2 - M3 Beta - 6 aree

Percorso Windows consigliato con indicazioni su systemd/servizio utente e documentazione della catena di avvio. Promuovere dopo scorecard ripetute di installazione/aggiornamento.

Copertura Sperimentale - 6%Qualità Alpha - 69%Completezza Beta - 79%Parziale - 5

Configurazione WSL 6 funzionalità / supportate da LTS

Sperimentale0%

Alfa67%

Beta79%

[Windows](</it/platforms/windows>), [Guida introduttiva](</it/start/getting-started>)

CLI 8 funzionalità / supportate da LTS

Sperimentale0%

Alfa67%

Beta79%

[Windows](</it/platforms/windows>), [Guida introduttiva](</it/start/getting-started>), [Aggiornamento](</it/install/updating>), [Onboarding](</it/cli/onboard>), [Doctor](</it/cli/doctor>), [Stato](</it/cli/status>), [Log](</it/cli/logs>)

Ciclo di vita del servizio Gateway 10 funzionalità / supportate da LTS

Sperimentale0%

Alfa67%

Beta79%

[Windows](</it/platforms/windows>), [Indice](</it/gateway>), [Doctor](</it/gateway/doctor>)

Accesso ed esposizione del Gateway 11 funzionalità / supportate da LTS

Sperimentale0%

Alfa67%

Beta79%

[Autenticazione](</it/gateway/authentication>), [Segreti](</it/gateway/secrets>), [Remoto](</it/gateway/remote>), [Runbook di esposizione](</it/gateway/security/exposure-runbook>), [Windows](</it/platforms/windows>)

Diagnostica e riparazione 6 funzionalità / supportate da LTS

Sperimentale38%

Beta79%

Beta79%

[Windows](</it/platforms/windows>), [Stato](</it/cli/status>), [Log](</it/cli/logs>), [Doctor](</it/cli/doctor>), [Doctor](</it/gateway/doctor>)

Browser e interfaccia utente di controllo 6 funzionalità

Sperimentale0%

Alfa67%

Beta79%

[Risoluzione dei problemi di CDP remoto del browser WSL2 Windows](</it/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Browser](</it/tools/browser>), [Interfaccia utente di controllo](</it/web/control-ui>)

Raspberry Pi e piccoli dispositivi Linux - M3 Beta - 4 aree

La documentazione della piattaforma esiste e il percorso Gateway è basato su Linux. Richiede una prova smoke di rilascio specifica per l'hardware per passare a un livello superiore.

Copertura Sperimentale - 0%Qualità Alfa - 67%Completezza Beta - 79%Nessuna

Configurazione e compatibilità 12 funzionalità

Sperimentale0%

Alfa67%

Beta79%

[Raspberry Pi](</it/install/raspberry-pi>), [Indice](</it/install>), [FAQ primo avvio](</it/help/faq-first-run>), [FAQ](</it/help/faq>), [Linux](</it/platforms/linux>), [Installer](</it/install/installer>)

Accesso remoto e autenticazione 9 funzionalità

Sperimentale0%

Alfa67%

Beta79%

[Raspberry Pi](</it/install/raspberry-pi>), [Autenticazione](</it/gateway/authentication>), [Segreti](</it/gateway/secrets>), [Associazione](</it/gateway/pairing>), [Dispositivi](</it/cli/devices>), [Remoto](</it/gateway/remote>), [Tailscale](</it/gateway/tailscale>)

Runtime del Gateway 10 funzionalità

Sperimentale0%

Alfa67%

Beta79%

[Indice](</it/gateway>), [Gateway](</it/cli/gateway>), [Raspberry Pi](</it/install/raspberry-pi>), [Linux](</it/platforms/linux>), [VPS](</it/vps>)

Prestazioni e diagnostica 5 funzionalità

Sperimentale0%

Alfa67%

Beta79%

[Raspberry Pi](</it/install/raspberry-pi>), [Linux](</it/platforms/linux>), [Integrità](</it/gateway/health>), [Diagnostica](</it/gateway/diagnostics>)

App complementare macOS - M3 Beta - 8 aree

Esistono un'app ricca per la barra dei menu, permessi, modalità Node, Canvas, attivazione vocale, WebChat e modalità remota. È ancora abbastanza in rapida evoluzione da evitare lo stato stabile.

Copertura Sperimentale - 0%Qualità Alfa - 66%Completezza Beta - 78%Nessuno

Canvas 4 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Canvas](</it/platforms/mac/canvas>), [Macos](</it/platforms/macos>), [Webchat](</it/web/webchat>)

Configurazione locale 7 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Gateway in bundle](</it/platforms/mac/bundled-gateway>), [Macos](</it/platforms/macos>), [Processo figlio](</it/platforms/mac/child-process>), [Configurazione di sviluppo](</it/platforms/mac/dev-setup>)

Stato e impostazioni 5 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Barra dei menu](</it/platforms/mac/menu-bar>), [Icona](</it/platforms/mac/icon>), [Macos](</it/platforms/macos>), [Integrità](</it/platforms/mac/health>), [Logging](</it/platforms/mac/logging>), [Remoto](</it/platforms/mac/remote>)

Funzionalità native 5 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Macos](</it/platforms/macos>), [Xpc](</it/platforms/mac/xpc>), [Autorizzazioni](</it/platforms/mac/permissions>), [Firma](</it/platforms/mac/signing>), [Peekaboo](</it/platforms/mac/peekaboo>)

Connessioni remote 3 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Remoto](</it/platforms/mac/remote>), [Macos](</it/platforms/macos>), [Remoto](</it/gateway/remote>)

Voce e Talk 3 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Voicewake](</it/platforms/mac/voicewake>), [Sovrapposizione vocale](</it/platforms/mac/voice-overlay>), [Talk](</it/nodes/talk>), [Macos](</it/platforms/macos>)

WebChat 3 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Webchat](</it/platforms/mac/webchat>), [Macos](</it/platforms/macos>), [Webchat](</it/web/webchat>)

WebChat remoto 5 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Webchat](</it/platforms/mac/webchat>), [Remoto](</it/gateway/remote>), [Remoto](</it/platforms/mac/remote>)

App Android - M2 Alpha - 7 aree

Il percorso pubblico su Google Play esiste, ma la documentazione dell'app descrive ancora la ricostruzione come estremamente alpha e richiama il lavoro di irrobustimento della release.

Copertura sperimentale - 0%Qualità alpha - 59%Completezza alpha - 66%Nessuna

Acquisizione multimediale 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>), [Fotocamera](</it/nodes/camera>)

Chat mobile 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>)

Configurazione connessione 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>), [Bonjour](</it/gateway/bonjour>), [Abbinamento](</it/gateway/pairing>)

Distribuzione 3 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>)

Impostazioni 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>)

Voce 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>), [Conversazione](</it/nodes/talk>)

Runtime dispositivo 2 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Android](</it/platforms/android>), [Risoluzione dei problemi](</it/nodes/troubleshooting>), [Protocollo](</it/gateway/protocol>)

Windows nativo - M2 Alpha - 4 aree

I flussi principali di CLI/Gateway funzionano, ma la documentazione consiglia ancora WSL2 per l'esperienza completa ed elenca le avvertenze native.

Copertura Sperimentale - 0%Qualità Alpha - 58%Completezza Alpha - 66%Parziale - 1

CLI 9 funzionalità / supportato da LTS

Sperimentale0%

Alpha54%

Alpha64%

[Indice](</it/install>), [Installer](</it/install/installer>), [Windows](</it/platforms/windows>), [Per iniziare](</it/start/getting-started>), [Onboard](</it/cli/onboard>)

Gestione del Gateway 11 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Windows](</it/platforms/windows>), [Indice](</it/gateway>), [Gateway](</it/cli/gateway>), [Doctor](</it/cli/doctor>)

Rete 4 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Windows](</it/platforms/windows>), [Indice](</it/gateway>), [Gateway](</it/cli/gateway>)

Aggiornamenti 4 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Aggiornamento](</it/install/updating>), [CI](</it/ci>)

Hosting Kubernetes - M2 Alpha - 4 aree

L'hosting Kubernetes è un percorso distinto di distribuzione cluster basato su Kustomize. La valutazione attuale mostra un percorso reale di distribuzione minimale con lacune relative a CI specifica per Kubernetes, pacchettizzazione di ingress/TLS/NetworkPolicy, backup/ripristino e rafforzamento dell'esposizione in produzione.

Copertura Sperimentale - 0%Qualità Alpha - 55%Completezza Alpha - 61%Nessuna

Configurazione della distribuzione 5 capacità

Sperimentale0%

Alpha55%

Alpha61%

[Kubernetes](</it/install/kubernetes>), [Indice](</it/install>)

Configurazione e segreti 5 capacità

Sperimentale0%

Alpha55%

Alpha61%

[Kubernetes](</it/install/kubernetes>), [Segreti](</it/gateway/secrets>), [Ambiente](</it/help/environment>)

Accesso ed esposizione 5 capacità

Sperimentale0%

Alpha55%

Alpha61%

[Kubernetes](</it/install/kubernetes>), [Autenticazione](</it/gateway/authentication>), [Remoto](</it/gateway/remote>), [Runbook dell'esposizione](</it/gateway/security/exposure-runbook>)

Ciclo di vita del cluster 5 capacità

Sperimentale0%

Alpha55%

Alpha61%

[Kubernetes](</it/install/kubernetes>), [Indice](</it/gateway>)

App iOS - M1 Sperimentale - 8 aree

Anteprima interna / super-alpha. Esistono flussi push supportati da TestFlight e relay, ma non ancora una distribuzione pubblica.

Copertura Sperimentale - 0%Qualità Sperimentale - 41%Completezza Sperimentale - 44%Nessuno

Media e condivisione 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Fotocamera](</it/nodes/camera>)

Canvas e schermo 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Canvas](</it/plugins/reference/canvas>)

Chat e sessioni 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Webchat](</it/web/webchat>), [Protocollo](</it/gateway/protocol>)

Configurazione e diagnostica del Gateway 7 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Abbinamento](</it/channels/pairing>)

Distribuzione 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>)

Comandi del dispositivo 2 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Protocollo](</it/gateway/protocol>)

Notifiche e background 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Configurazione](</it/gateway/configuration>)

Voce 1 capacità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>), [Talk](</it/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

Flusso di installazione opzionale. Richiede un impegno di supporto più chiaro prima della promozione ad alpha/beta.

Copertura sperimentale - 0%Qualità sperimentale - 41%Completezza sperimentale - 44%Nessuno

Passaggio dell'installazione 4 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Nix](</it/install/nix>), [Indice](</it/install>), [Directory della documentazione](</it/start/docs-directory>)

Ciclo di vita del Plugin 4 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Gestire i Plugin](</it/plugins/manage-plugins>), [Plugin](</it/tools/plugin>), [Nix](</it/install/nix>)

Attivazione ed esperienza utente dell'app 7 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Nix](</it/install/nix>)

Configurazione e stato 7 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Nix](</it/install/nix>), [Configurazione](</it/cli/setup>), [Ambiente](</it/help/environment>)

Runtime del servizio e protezioni 8 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Nix](</it/install/nix>), [Configurazione](</it/cli/setup>), [Doctor](</it/cli/doctor>), [Aggiornamento](</it/cli/update>)

Superfici companion watchOS - M1 Sperimentale - 5 aree

Il sorgente contiene superfici per app/estensione Watch; la documentazione pubblica non presenta ancora questa funzionalità per gli utenti.

Copertura Sperimentale - 0%Qualità Sperimentale - 41%Completezza Sperimentale - 44%Nessuna

Consegna e ripristino 7 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>)

Approvazioni Exec 3 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Approvazioni Exec](</it/tools/exec-approvals>), [iOS](</it/platforms/ios>)

Distribuzione e supporto 6 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>)

Notifiche e risposte 7 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>)

Interfaccia app Watch 3 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[iOS](</it/platforms/ios>)

App complementare Linux - M0 Pianificata - 5 aree

La documentazione indica che le app complementari native per Linux sono pianificate; Gateway è oggi il percorso Linux supportato.

Copertura sperimentale - 0%Qualità sperimentale - 19%Completezza sperimentale - 21%Nessuna

Distribuzione dell'app 3 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Linux](</it/platforms/linux>), [Indice](</it/platforms>), [Indice](</it/install>)

Connettività Gateway 4 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Linux](</it/platforms/linux>), [Indice](</it/gateway>), [Abbinamento](</it/gateway/pairing>), [Remoto](</it/gateway/remote>)

Chat e sessioni 3 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Linux](</it/platforms/linux>), [Protocollo](</it/gateway/protocol>), [Webchat](</it/web/webchat>)

Funzionalità desktop 9 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Linux](</it/platforms/linux>), [Approvazioni Exec](</it/tools/exec-approvals>), [Segreti](</it/gateway/secrets>), [Indice](</it/nodes>), [Exec](</it/tools/exec>), [Talk](</it/nodes/talk>), [Fotocamera](</it/nodes/camera>)

Stato e diagnostica 7 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Linux](</it/platforms/linux>), [Openclaw](</it/start/openclaw>), [Doctor](</it/gateway/doctor>)

App complementare nativa per Windows - M0 Pianificato - 5 aree

Solo pianificato.

Copertura Sperimentale - 0%Qualità Sperimentale - 19%Completezza Sperimentale - 21%Nessuno

Installazione e aggiornamenti 4 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Windows](</it/platforms/windows>), [Indice](</it/install>)

Connessione Gateway 3 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Windows](</it/platforms/windows>), [Indice](</it/gateway>), [Abbinamento](</it/gateway/pairing>), [Remoto](</it/gateway/remote>)

Sessioni di chat 2 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Windows](</it/platforms/windows>), [Protocollo](</it/gateway/protocol>)

Stato e riparazione 5 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Windows](</it/platforms/windows>), [Doctor](</it/gateway/doctor>), [Indice](</it/gateway>)

Strumenti desktop e autorizzazioni 10 funzionalità

Sperimentale0%

Sperimentale19%

Sperimentale21%

[Windows](</it/platforms/windows>), [Indice](</it/nodes>), [Exec](</it/tools/exec>), [Approvazioni Exec](</it/tools/exec-approvals>), [Indice](</it/gateway/security>)

### Canale

Discord - M4 Stabile - 6 aree

Documentazione approfondita e ampia copertura delle funzionalità. I percorsi voce/delega dovrebbero restare valutati separatamente come beta/alpha.

Copertura Sperimentale - 0%Qualità Beta - 73%Completezza Stabile - 87%Parziale - 4

Configurazione e operazioni dei canali 10 funzionalità / supportate LTS

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>), [Discord](</it/plugins/reference/discord>), [Fly](</it/install/fly>), [Comandi slash](</it/tools/slash-commands>), [Salute](</it/gateway/health>), [Canali](</it/cli/channels>), [Canali di configurazione](</it/gateway/config-channels>)

Accesso e identità 6 funzionalità / supportate LTS

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>), [Associazione](</it/channels/pairing>), [Gruppi di accesso](</it/channels/access-groups>), [Gruppi](</it/channels/groups>)

Instradamento e recapito delle conversazioni 12 funzionalità / supportate LTS

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>), [Instradamento dei canali](</it/channels/channel-routing>), [Gruppi](</it/channels/groups>), [Gruppi di accesso](</it/channels/access-groups>), [Agenti ACP](</it/tools/acp-agents>), [Subagenti](</it/tools/subagents>)

Contenuti multimediali e avanzati 1 funzionalità / supportate LTS

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>)

Controlli nativi e approvazioni 5 funzionalità

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>), [Comandi slash](</it/tools/slash-commands>)

Voce e chiamate in tempo reale 5 funzionalità

Sperimentale0%

Beta73%

Stabile87%

[Discord](</it/channels/discord>), [Openai](</it/providers/openai>), [Elevenlabs](</it/providers/elevenlabs>), [Automazione QA E2E](</it/concepts/qa-e2e-automation>), [Canali di configurazione](</it/gateway/config-channels>)

Telegram - M3 Beta - 5 aree

Il canale core è abbastanza maturo per l'uso regolare, ma la UX ad alta variabilità e i casi limite dei contenuti multimediali richiedono prove di scenario ricorrenti.

Copertura sperimentale - 0%Qualità Alpha - 68%Completezza Beta - 78%Completo - 5

Configurazione e operazioni del canale 10 funzionalità / supportate LTS

Sperimentale0%

Alpha66%

Beta78%

[Telegram](</it/channels/telegram>), [Configurazione dei canali](</it/gateway/config-channels>), [Canali](</it/cli/channels>)

Accesso e identità 10 funzionalità / supportate LTS

Sperimentale0%

Alpha66%

Beta78%

[Telegram](</it/channels/telegram>), [Abbinamento](</it/channels/pairing>), [Gruppi di accesso](</it/channels/access-groups>), [Gruppi](</it/channels/groups>), [Multi Agent](</it/concepts/multi-agent>)

Instradamento e recapito delle conversazioni 1 funzionalità / supportate LTS

Sperimentale0%

Alpha66%

Beta78%

[Telegram](</it/channels/telegram>), [Gruppi](</it/channels/groups>), [Multi Agent](</it/concepts/multi-agent>)

Contenuti multimediali e avanzati 1 funzionalità / supportate LTS

Sperimentale0%

Alpha66%

Beta78%

[Telegram](</it/channels/telegram>), [Posizione](</it/channels/location>)

Controlli e approvazioni nativi 9 funzionalità / supportate LTS

Sperimentale0%

Beta77%

Beta79%

[Telegram](</it/channels/telegram>), [Approvazioni exec](</it/tools/exec-approvals>), [Reazioni](</it/tools/reactions>)

Slack - M3 Beta - 5 aree

Documentazione del canale di prima classe e superficie di instradamento. Richiede scorecard per scenari di installazione/amministrazione dello spazio di lavoro.

Copertura Sperimentale - 0%Qualità Alpha - 66%Completezza Beta - 78%Completa - 5

Configurazione e operazioni del canale 10 funzionalità / supportate da LTS

Sperimentale0%

Alpha66%

Beta78%

[Slack](</it/channels/slack>), [Slack](</it/plugins/reference/slack>), [Segreti](</it/gateway/secrets>), [Automazione QA E2E](</it/concepts/qa-e2e-automation>), [Risoluzione dei problemi](</it/channels/troubleshooting>)

Accesso e identità 1 funzionalità / supportate da LTS

Sperimentale0%

Alpha66%

Beta78%

[Slack](</it/channels/slack>), [Associazione](</it/channels/pairing>)

Instradamento e recapito delle conversazioni 5 funzionalità / supportate da LTS

Sperimentale0%

Alpha66%

Beta78%

[Slack](</it/channels/slack>), [Protezione dai cicli dei bot](</it/channels/bot-loop-protection>), [Associazione](</it/channels/pairing>)

Media e contenuti avanzati 1 funzionalità / supportate da LTS

Sperimentale0%

Alpha66%

Beta78%

[Slack](</it/channels/slack>), [Automazione QA E2E](</it/concepts/qa-e2e-automation>)

Controlli e approvazioni nativi 8 funzionalità / supportate da LTS

Sperimentale0%

Alpha66%

Beta78%

[Slack](</it/channels/slack>), [Comandi slash](</it/tools/slash-commands>), [Approvazioni Exec](</it/tools/exec-approvals>)

iMessage e BlueBubbles - M3 Beta - 5 aree

iMessage supportato funziona tramite imsg su un host macOS Messages con accesso effettuato; le configurazioni BlueBubbles legacy richiedono una migrazione. Mantieni visibili le avvertenze su autorizzazioni macOS, wrapper SSH, SIP/API private e migrazione.

Copertura Sperimentale - 0%Qualità Alpha - 66%Completezza Beta - 78%Nessuno

Configurazione e operazioni del canale 11 capacità

Sperimentale0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</it/announcements/bluebubbles-imessage>), [Imessage da Bluebubbles](</it/channels/imessage-from-bluebubbles>), [Configura canali](</it/gateway/config-channels>), [Imessage](</it/channels/imessage>)

Accesso e identità 6 capacità

Sperimentale0%

Alpha66%

Beta78%

[Imessage](</it/channels/imessage>), [Imessage da Bluebubbles](</it/channels/imessage-from-bluebubbles>), [Configura canali](</it/gateway/config-channels>)

Instradamento e consegna delle conversazioni 4 capacità

Sperimentale0%

Alpha66%

Beta78%

[Imessage](</it/channels/imessage>)

Media e contenuti avanzati 7 capacità

Sperimentale0%

Alpha66%

Beta78%

[Imessage](</it/channels/imessage>), [Imessage da Bluebubbles](</it/channels/imessage-from-bluebubbles>), [Configura canali](</it/gateway/config-channels>)

Controlli e approvazioni nativi 3 capacità

Sperimentale0%

Alpha66%

Beta78%

[Imessage](</it/channels/imessage>)

WhatsApp - M3 Beta - 5 aree

Il percorso principale è importante e documentato; la volatilità upstream di Baileys/sessione lo mantiene sotto Stable.

Copertura Sperimentale - 0%Qualità Alpha - 66%Completezza Beta - 78%Nessuno

Configurazione e operazioni dei canali 5 funzionalità

Sperimentale0%

Alfa66%

Beta78%

[WhatsApp](</it/channels/whatsapp>), [Configurazione canali](</it/gateway/config-channels>), [WhatsApp](</it/plugins/reference/whatsapp>), [Automazione QA E2E](</it/concepts/qa-e2e-automation>), [Diagnostica](</it/gateway/doctor>)

Accesso e identità 7 funzionalità

Sperimentale0%

Alfa66%

Beta78%

[WhatsApp](</it/channels/whatsapp>), [Configurazione canali](</it/gateway/config-channels>), [Automazione QA E2E](</it/concepts/qa-e2e-automation>), [Abbinamento](</it/channels/pairing>)

Instradamento e recapito delle conversazioni 4 funzionalità

Sperimentale0%

Alfa66%

Beta78%

[WhatsApp](</it/channels/whatsapp>), [Messaggi di gruppo](</it/channels/group-messages>)

Media e contenuti avanzati 2 funzionalità

Sperimentale0%

Alfa66%

Beta78%

[WhatsApp](</it/channels/whatsapp>)

Controlli nativi e approvazioni 2 funzionalità

Sperimentale0%

Alfa66%

Beta78%

[WhatsApp](</it/channels/whatsapp>)

Matrix - M2 Alfa - 6 aree

Supportato tramite Plugin in bundle. Richiede scorecard per bridge, autenticazione e ciclo di vita delle stanze.

Copertura sperimentale - 0%Qualità alfa - 60%Completezza alfa - 67%Nessuno

Configurazione e operazioni del canale 5 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>), [Migrazione Matrix](</it/channels/matrix-migration>)

Accesso e identità 7 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>), [Gruppi](</it/channels/groups>), [Protezione dai loop dei bot](</it/channels/bot-loop-protection>)

Instradamento e consegna delle conversazioni 1 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>)

Media e contenuti avanzati 1 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>)

Controlli nativi e approvazioni 6 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>)

Crittografia e verifica 3 funzionalità

Sperimentale0%

Alpha60%

Alpha67%

[Matrix](</it/channels/matrix>), [Migrazione Matrix](</it/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 aree

Canale documentato, ma la configurazione aziendale/amministrativa aumenta il rischio di maturità.

Copertura Sperimentale - 0%Qualità Alpha - 59%Completezza Alpha - 66%Nessuna

Configurazione e operazioni dei canali 16 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Google Chat](</it/channels/googlechat>), [Google Chat](</it/plugins/reference/googlechat>), [Configurazione dei canali](</it/gateway/config-channels>), [Riferimento CLI della procedura guidata](</it/start/wizard-cli-reference>), [Segreti](</it/gateway/secrets>), [Superficie delle credenziali Secretref](</it/reference/secretref-credential-surface>), [Stato](</it/gateway/health>), [Inventario dei Plugin](</it/plugins/plugin-inventory>), [Indice](</it/channels>)

Accesso e identità 11 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Google Chat](</it/channels/googlechat>), [Associazione](</it/channels/pairing>), [Gruppi di accesso](</it/channels/access-groups>), [Configurazione dei canali](</it/gateway/config-channels>), [Protezione dai loop dei bot](</it/channels/bot-loop-protection>), [Instradamento dei canali](</it/channels/channel-routing>)

Instradamento e consegna delle conversazioni 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Google Chat](</it/channels/googlechat>), [Protezione dai loop dei bot](</it/channels/bot-loop-protection>), [Gruppi di accesso](</it/channels/access-groups>), [Instradamento dei canali](</it/channels/channel-routing>)

Contenuti multimediali e avanzati 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Google Chat](</it/channels/googlechat>), [Messaggio](</it/cli/message>), [Comprensione dei contenuti multimediali](</it/nodes/media-understanding>), [Superficie delle credenziali Secretref](</it/reference/secretref-credential-surface>)

Controlli e approvazioni nativi 16 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Google Chat](</it/channels/googlechat>), [Messaggio](</it/cli/message>), [Comprensione dei contenuti multimediali](</it/nodes/media-understanding>), [Superficie delle credenziali Secretref](</it/reference/secretref-credential-surface>), [Reazioni](</it/tools/reactions>), [Comandi slash](</it/tools/slash-commands>), [Configurazione degli agenti](</it/gateway/config-agents>), [Refactoring del ciclo di vita dei messaggi](</it/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 aree

I flussi di autenticazione/amministrazione aziendali richiedono prove di scenario esplicite.

Copertura Sperimentale - 0%Qualità Alpha - 59%Completezza Alpha - 66%Nessuno

Configurazione e operazioni dei canali 9 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Msteams](</it/channels/msteams>), [Msteams](</it/plugins/reference/msteams>), [Configurazione canali](</it/gateway/config-channels>), [Stato](</it/gateway/health>)

Accesso e identità 9 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Msteams](</it/channels/msteams>), [Associazione](</it/channels/pairing>), [Gruppi di accesso](</it/channels/access-groups>)

Instradamento e recapito delle conversazioni 5 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Msteams](</it/channels/msteams>), [Gruppi](</it/channels/groups>), [Instradamento canali](</it/channels/channel-routing>)

Contenuti multimediali e avanzati 5 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Msteams](</it/channels/msteams>)

Controlli nativi e approvazioni 5 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Msteams](</it/channels/msteams>), [Approvazioni exec avanzate](</it/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 aree

La documentazione dei canali supportati esiste; servono prove più solide di installazione e riconnessione.

Copertura sperimentale - 0%Qualità Alpha - 59%Completezza Alpha - 66%Nessuno

Configurazione e operazioni dei canali 7 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Signal](</it/channels/signal>), [Signal](</it/plugins/reference/signal>)

Accesso e identità 6 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Signal](</it/channels/signal>)

Instradamento e recapito delle conversazioni 1 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Signal](</it/channels/signal>)

Media e contenuti avanzati 7 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Signal](</it/channels/signal>)

Controlli nativi e approvazioni 3 funzionalità

Sperimentale0%

Alpha59%

Alpha66%

[Signal](</it/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canali regionali - M2 Alpha - 4 aree

Copertura regionale importante, ma il livello di supporto pubblico dovrebbe essere calibrato in base al tipo di account, all'approvazione upstream e alla prova del maintainer.

Copertura Sperimentale - 0%Qualità Alpha - 55%Completezza Alpha - 58%Nessuno

Configurazione e operazioni dei canali 6 capacità

Sperimentale0%

Alpha61%

Alpha68%

[Indice](</it/channels>), [Abbinamento](</it/channels/pairing>), [Feishu](</it/plugins/reference/feishu>), [Interni dell'architettura](</it/plugins/architecture-internals>)

Accesso e identità 1 capacità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Instradamento e recapito delle conversazioni 1 capacità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Media e contenuti avanzati 1 capacità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 areas

Esistono superfici supportate, ma la maturità probabilmente varia in base alla copertura dell'upstream e dei manutentori. Valutarle singolarmente in seguito.

Copertura Sperimentale - 0%Qualità Alpha - 53%Completezza Alpha - 54%Nessuno

Configurazione e operazioni del canale 1 funzionalità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Accesso e identità 1 funzionalità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Instradamento e recapito delle conversazioni 1 funzionalità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Contenuti multimediali e avanzati 1 funzionalità

Sperimentale0%

Alpha53%

Alpha54%

Nessuna documentazione collegata

Canale per chiamate vocali - M1 Sperimentale - 5 aree

Percorso opzionale/Plugin con comportamento complesso in tempo reale. Richiede una scorecard degli scenari prima della beta pubblica.

Copertura sperimentale - 0%Qualità sperimentale - 41%Completezza sperimentale - 44%Nessuno

Configurazione e operazioni dei canali 2 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Chiamata vocale](</it/cli/voicecall>), [Chiamata vocale](</it/plugins/voice-call>), [Protocollo](</it/gateway/protocol>)

Accesso e identità 1 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Chiamata vocale](</it/plugins/voice-call>), [Chiamata vocale](</it/cli/voicecall>)

Routing e recapito delle conversazioni 1 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Chiamata vocale](</it/plugins/voice-call>)

Media e contenuti avanzati 2 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Chiamata vocale](</it/plugins/voice-call>), [Inventario Plugin](</it/plugins/plugin-inventory>)

Voce e chiamate in tempo reale 2 funzionalità

Sperimentale0%

Sperimentale41%

Sperimentale44%

[Chiamata vocale](</it/plugins/voice-call>)

### Provider e strumenti

Automazione del browser, exec e strumenti sandbox - M3 Beta - 3 aree

Gli strumenti principali sono documentati, ma la sicurezza dell'host e l'esperienza utente dei permessi dovrebbero restare sotto revisione attiva nella scorecard.

Copertura sperimentale - 21%Qualità Beta - 75%Completezza Beta - 79%Parziale - 2

Automazione del browser 8 funzionalità

Sperimentale13%

Beta79%

Beta79%

[Controllo del browser](</it/tools/browser-control>), [Test](</it/help/testing>), [Browser](</it/tools/browser>), [Indice](</it/gateway/security>), [Controlli di audit](</it/gateway/security/audit-checks>)

Invocazione ed esecuzione degli strumenti 6 funzionalità / supportato da LTS

Alpha50%

Beta79%

Beta79%

[Exec](</it/tools/exec>), [Processo in background](</it/gateway/background-process>), [API HTTP di invocazione strumenti](</it/gateway/tools-invoke-http-api>), [Ambiti operatore](</it/gateway/operator-scopes>), [Protocollo](</it/gateway/protocol>), [Approvazioni Exec](</it/tools/exec-approvals>), [Approvazioni Exec avanzate](</it/tools/exec-approvals-advanced>), [Elevato](</it/tools/elevated>)

Sandbox e policy degli strumenti 6 funzionalità / supportato da LTS

Sperimentale0%

Alpha68%

Beta79%

[Sandboxing](</it/gateway/sandboxing>), [Sandbox rispetto a policy degli strumenti rispetto a elevato](</it/gateway/sandbox-vs-tool-policy-vs-elevated>), [Strumenti sandbox multi-agente](</it/tools/multi-agent-sandbox-tools>), [Riferimento harness Codex](</it/plugins/codex-harness-reference>), [Strumenti di configurazione](</it/gateway/config-tools>)

Percorso del provider OpenAI e Codex - M3 Beta - 5 aree

Documentazione approfondita, percorso OAuth/abbonamento, voce in tempo reale, immagini e comportamento di compatibilità. La variabilità dei provider impedisce di passare a Stable senza prova nella scorecard di rilascio.

Copertura Sperimentale - 26%Qualità Beta - 74%Completezza Beta - 79%Parziale - 3

Modello e autenticazione 6 funzionalità / con supporto LTS

Sperimentale44%

Beta79%

Beta79%

[Openai](</it/providers/openai>), [Codex Harness](</it/plugins/codex-harness>), [Modelli](</it/concepts/models>), [Oauth](</it/concepts/oauth>), [Riferimento di Codex Harness](</it/plugins/codex-harness-reference>), [Monitoraggio dell'autenticazione](</it/gateway/authentication>)

Compatibilità di risposte e strumenti 4 funzionalità / con supporto LTS

Sperimentale40%

Beta79%

Beta79%

[Openai](</it/providers/openai>), [API HTTP Openresponses](</it/gateway/openresponses-http-api>), [API HTTP Openai](</it/gateway/openai-http-api>), [Plugin nativi Codex](</it/plugins/codex-native-plugins>)

Harness Codex nativo 2 funzionalità / con supporto LTS

Sperimentale44%

Beta79%

Beta79%

[Codex Harness](</it/plugins/codex-harness>), [Runtime di Codex Harness](</it/plugins/codex-harness-runtime>), [Riferimento di Codex Harness](</it/plugins/codex-harness-reference>), [Plugin nativi Codex](</it/plugins/codex-native-plugins>)

Immagini e input multimodale 2 funzionalità

Sperimentale0%

Alpha67%

Beta79%

[Openai](</it/providers/openai>), [Generazione di immagini](</it/tools/image-generation>), [Immagini](</it/nodes/images>)

Voce e audio in tempo reale 2 funzionalità

Sperimentale0%

Alpha67%

Beta79%

[Openai](</it/providers/openai>), [Discord](</it/channels/discord>), [Chiamata vocale](</it/plugins/voice-call>)

Strumenti di ricerca web - M3 Beta - 4 aree

Esistono più provider e documentazione. Serve prova di quote/errori/SSRF per famiglia di provider.

Copertura Sperimentale - 9%Qualità Beta - 74%Completezza Beta - 79%Nessuna

Provider di ricerca 19 funzionalità

Sperimentale11%

Beta79%

Beta79%

[Web](</it/tools/web>), [Brave Search](</it/tools/brave-search>), [Tavily](</it/tools/tavily>), [Exa Search](</it/tools/exa-search>), [Firecrawl](</it/tools/firecrawl>), [Perplexity Search](</it/tools/perplexity-search>), [Duckduckgo Search](</it/tools/duckduckgo-search>), [Searxng Search](</it/tools/searxng-search>), [Gemini Search](</it/tools/gemini-search>), [Grok Search](</it/tools/grok-search>), [Kimi Search](</it/tools/kimi-search>), [Minimax Search](</it/tools/minimax-search>), [Ollama Search](</it/tools/ollama-search>), [Sottopercorsi SDK](</it/plugins/sdk-subpaths>), [Panoramica SDK](</it/plugins/sdk-overview>), [Manifesto](</it/plugins/manifest>)

Configurazione e diagnostica 9 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Web](</it/tools/web>), [Recupero Web](</it/tools/web-fetch>), [FAQ](</it/help/faq>), [Costi di utilizzo API](</it/reference/api-usage-costs>), [Brave Search](</it/tools/brave-search>), [Perplexity Search](</it/tools/perplexity-search>), [Tavily](</it/tools/tavily>), [Firecrawl](</it/tools/firecrawl>)

Sicurezza della rete 4 funzionalità

Sperimentale0%

Alpha68%

Beta79%

[Web](</it/tools/web>), [Recupero Web](</it/tools/web-fetch>), [Firecrawl](</it/tools/firecrawl>), [Searxng Search](</it/tools/searxng-search>)

Disponibilità e recupero degli strumenti 11 funzionalità

Sperimentale25%

Beta79%

Beta79%

[Strumenti di configurazione](</it/gateway/config-tools>), [Recupero Web](</it/tools/web-fetch>), [Web](</it/tools/web>), [FAQ](</it/help/faq>)

Percorso provider Anthropic - M3 Beta - 5 aree

Provider di modelli di prima classe. Richiede prove di scenario ricorrenti per auth/catalog/tool-call.

Copertura Sperimentale - 0%Qualità Beta - 71%Completezza Beta - 78%Nessuna

Autenticazione e ripristino dei provider 9 capacità

Sperimentale0%

Alpha66%

Beta78%

[Anthropic](</it/providers/anthropic>), [Doctor](</it/gateway/doctor>), [Esempi di configurazione](</it/gateway/configuration-examples>), [Risoluzione dei problemi](</it/gateway/troubleshooting>), [Prompt Caching](</it/reference/prompt-caching>)

Selezione di modello e runtime 10 capacità

Sperimentale0%

Beta78%

Beta79%

[Anthropic](</it/providers/anthropic>), [Configura agenti](</it/gateway/config-agents>), [Modelli](</it/concepts/models>), [Backend CLI](</it/gateway/cli-backends>)

Trasporto delle richieste e semantica dei turni 10 capacità

Sperimentale0%

Beta77%

Beta79%

[Anthropic](</it/providers/anthropic>), [Prompt Caching](</it/reference/prompt-caching>), [Risoluzione dei problemi](</it/gateway/troubleshooting>), [Backend CLI](</it/gateway/cli-backends>), [Provider di modelli](</it/concepts/model-providers>)

Cache dei prompt e contesto 5 capacità

Sperimentale0%

Alpha66%

Beta78%

[Anthropic](</it/providers/anthropic>), [Prompt Caching](</it/reference/prompt-caching>), [Risoluzione dei problemi](</it/gateway/troubleshooting>), [Heartbeat](</it/gateway/heartbeat>)

Input multimediali 4 capacità

Sperimentale0%

Alpha66%

Beta78%

[Anthropic](</it/providers/anthropic>), [Configura agenti](</it/gateway/config-agents>)

Percorso del provider Google - M3 Beta - 5 aree

Provider di prima classe con superfici per modelli e tempo reale. Richiede una valutazione separata Live/Talk.

Copertura Sperimentale - 0%Qualità Alpha - 66%Completezza Beta - 78%Nessuna

Configurazione del provider e credenziali 10 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Google](</it/providers/google>), [Provider di modelli](</it/concepts/model-providers>)

Instradamento dei modelli ed endpoint 10 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Google](</it/providers/google>), [Provider di modelli](</it/concepts/model-providers>), [Google](</it/plugins/reference/google>), [Ricerca Gemini](</it/tools/gemini-search>)

Runtime Gemini diretto 9 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Google](</it/providers/google>), [Provider di modelli](</it/concepts/model-providers>), [Domande frequenti sui modelli](</it/help/faq-models>), [Test live](</it/help/testing-live>)

Media, ricerca e tempo reale 10 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Google](</it/plugins/reference/google>), [Google](</it/providers/google>)

Caching dei prompt 5 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Caching dei prompt](</it/reference/prompt-caching>), [Google](</it/providers/google>), [Provider di modelli](</it/concepts/model-providers>), [Uso dei token](</it/reference/token-use>)

Percorso del provider OpenRouter - M3 Beta - 4 aree

Il percorso unificato del provider è documentato e utile, ma il comportamento specifico dei modelli varia.

Copertura Sperimentale - 0%Qualità Alpha - 66%Completezza Beta - 78%Nessuno

Configurazione e autenticazione dei provider 14 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Openrouter](</it/providers/openrouter>), [Provider di modelli](</it/concepts/model-providers>), [Configura](</it/cli/configure>), [Autenticazione](</it/gateway/authentication>), [Ambiente](</it/help/environment>), [Modelli](</it/cli/models>), [Modelli](</it/concepts/models>)

Runtime chat e normalizzazione 15 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Openrouter](</it/providers/openrouter>), [Provider di modelli](</it/concepts/model-providers>), [Memorizzazione nella cache dei prompt](</it/reference/prompt-caching>)

Ripristino e diagnostica dei provider 5 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Failover dei modelli](</it/concepts/model-failover>), [Openrouter](</it/providers/openrouter>), [Modelli](</it/cli/models>)

Generazione di media e sintesi vocale 7 funzionalità

Sperimentale0%

Alpha66%

Beta78%

[Openrouter](</it/providers/openrouter>), [Generazione di immagini](</it/tools/image-generation>), [Generazione di musica](</it/tools/music-generation>), [Panoramica dei media](</it/tools/media-overview>), [Generazione di video](</it/tools/video-generation>), [Tts](</it/tools/tts>)

Strumenti di generazione di immagini, video e musica - M2 Alpha - 5 aree

La funzionalità esiste tra i provider, ma qualità, latenza e compatibilità dei parametri variano troppo per la beta senza prove specifiche per provider.

Copertura Sperimentale - 0%Qualità Alpha - 61%Completezza Alpha - 68%Nessuna

Routing e individuazione dei media 4 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Config Agents](</it/gateway/config-agents>), [Generazione di immagini](</it/tools/image-generation>), [Generazione di video](</it/tools/video-generation>), [Generazione di musica](</it/tools/music-generation>)

Ciclo di vita e consegna delle attività 12 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Panoramica dei media](</it/tools/media-overview>), [Generazione di immagini](</it/tools/image-generation>), [Generazione di video](</it/tools/video-generation>), [Generazione di musica](</it/tools/music-generation>)

Generazione di immagini 9 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Generazione di immagini](</it/tools/image-generation>), [Infer](</it/cli/infer>), [Panoramica dei media](</it/tools/media-overview>)

Generazione di video 11 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Generazione di video](</it/tools/video-generation>), [Runway](</it/providers/runway>), [Pixverse](</it/providers/pixverse>), [Fal](</it/providers/fal>), [Openrouter](</it/providers/openrouter>)

Generazione di musica 6 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Generazione di musica](</it/tools/music-generation>)

Provider di modelli locali: Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 aree

Utile e documentato, ma la variabilità dell'ambiente è elevata.

Copertura Sperimentale - 0%Qualità Alpha - 61%Completezza Alpha - 68%Nessuno

Configurazione, ciclo di vita e diagnostica dei provider 12 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Modelli locali](</it/gateway/local-models>), [Lmstudio](</it/providers/lmstudio>), [Ollama](</it/providers/ollama>), [Vllm](</it/providers/vllm>), [Servizi per modelli locali](</it/gateway/local-model-services>), [Configurare gli agenti](</it/gateway/config-agents>), [Risoluzione dei problemi](</it/gateway/troubleshooting>), [Doctor](</it/gateway/doctor>)

Plugin provider nativi 10 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Ollama](</it/providers/ollama>), [Lmstudio](</it/providers/lmstudio>)

Compatibilità runtime compatibile con OpenAI 8 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Vllm](</it/providers/vllm>), [Sglang](</it/providers/sglang>), [Modelli locali](</it/gateway/local-models>), [Lmstudio](</it/providers/lmstudio>)

Memoria locale ed embedding 5 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Memoria](</it/concepts/memory>), [Doctor](</it/gateway/doctor>)

Sicurezza della rete e controlli dei prompt 2 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Indice](</it/gateway/security>), [Configurare gli strumenti](</it/gateway/config-tools>), [Modelli locali](</it/gateway/local-models>)

Provider ospitati long-tail - M2 Alpha - 3 aree

Esistono molte pagine di documentazione/riferimento; il punteggio dovrebbe essere generato dai metadati dei provider più la copertura smoke live.

Copertura Sperimentale - 0%Qualità Alpha - 61%Completezza Alpha - 68%Nessuna

Provider LLM ospitati 12 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Indice](</it/providers>), [Provider di modelli](</it/concepts/model-providers>), [Test live](</it/help/testing-live>), [Onboarding](</it/cli/onboard>)

Provider multimediali ospitati 8 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Manifest](</it/plugins/manifest>), [Test live](</it/help/testing-live>), [Indice](</it/providers>)

Operazioni dei provider 12 funzionalità

Sperimentale0%

Alpha61%

Alpha68%

[Indice](</it/providers>), [Provider di modelli](</it/concepts/model-providers>), [Manifest](</it/plugins/manifest>), [Test live](</it/help/testing-live>), [Modelli](</it/cli/models>)

Was this useful?YesNo

Open issue