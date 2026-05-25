---
title: Showcase
source_url: https://docs.openclaw.ai/it/start/showcase
scraped_at: 2026-05-25
---

I progetti OpenClaw non sono demo giocattolo. Le persone stanno realizzando loop di revisione PR, app mobili, automazione domestica, sistemi vocali, devtool e flussi di lavoro ricchi di memoria dai canali che già usano — build chat-native su Telegram, WhatsApp, Discord e terminali; automazione reale per prenotazioni, acquisti e supporto senza aspettare un'API; e integrazioni con il mondo fisico con stampanti, aspirapolvere, telecamere e sistemi domestici.

## Video

Inizia da qui se vuoi il percorso più breve da "che cos'è?" a "ok, ho capito."

[**Guida completa alla configurazione** VelvetShark, 28 minuti. Installa, completa l'onboarding e arriva a un primo assistente funzionante end-to-end. ](<https://www.youtube.com/watch?v=SaWSPZoPX34>) [**Showcase della community** Un passaggio più rapido attraverso progetti reali, superfici e flussi di lavoro costruiti attorno a OpenClaw. ](<https://www.youtube.com/watch?v=mMSKQvlmFuQ>) [**Progetti nel mondo reale** Esempi dalla community, dai loop di coding chat-native fino all'hardware e all'automazione personale. ](<https://www.youtube.com/watch?v=5kkIJNUGFho>)

## Appena arrivati da Discord

Elementi di spicco recenti tra coding, devtool, mobile e creazione di prodotti chat-native.

[**Da revisione PR a feedback su Telegram** **@bangnokia** • `review` `github` `telegram` OpenCode completa la modifica, apre una PR, OpenClaw rivede il diff e risponde su Telegram con suggerimenti più un chiaro verdetto di merge. ![Feedback di revisione PR di OpenClaw consegnato su Telegram](/assets/showcase/pr-review-telegram.jpg) ](<https://x.com/i/status/2010878524543131691>) [**Skill per cantina vini in pochi minuti** **@prades_maxime** • `skills` `local` `csv` Ha chiesto a "Robby" (@openclaw) una skill locale per la cantina vini. Richiede un CSV di esempio esportato e un percorso di archiviazione, poi costruisce e testa la skill (962 bottiglie nell'esempio). ![OpenClaw costruisce una skill locale per cantina vini da CSV](/assets/showcase/wine-cellar-skill.jpg) ](<https://x.com/i/status/2010916352454791216>) [**Pilota automatico della spesa Tesco** **@marchattonhere** • `automation` `browser` `shopping` Piano pasti settimanale, articoli abituali, prenotazione fascia di consegna, conferma ordine. Nessuna API, solo controllo del browser. ![Automazione della spesa Tesco via chat](/assets/showcase/tesco-shop.jpg) ](<https://x.com/i/status/2009724862470689131>) [**SNAG da screenshot a Markdown** **@am-will** • `devtools` `screenshots` `markdown` Tasto rapido su un'area dello schermo, vision di Gemini, Markdown istantaneo negli appunti. ![Strumento SNAG da screenshot a markdown](/assets/showcase/snag.png) ](<https://github.com/am-will/snag>) [**Agents UI** **@kitze** • `ui` `skills` `sync` App desktop per gestire Skills e comandi tra Agents, Claude, Codex e OpenClaw. ![App Agents UI](/assets/showcase/agents-ui.jpg) ](<https://releaseflow.net/kitze/agents-ui>) [**Messaggi vocali Telegram (papla.media)** **Community** • `voice` `tts` `telegram` Avvolge il TTS di papla.media e invia i risultati come messaggi vocali Telegram (senza autoplay fastidioso). ![Output di messaggio vocale Telegram da TTS](/assets/showcase/papla-tts.jpg) ](<https://papla.media/docs>) [**CodexMonitor** **@odrobnik** • `devtools` `codex` `brew` Helper installabile con Homebrew per elencare, ispezionare e osservare sessioni locali di OpenAI Codex (CLI + VS Code). ![CodexMonitor su ClawHub](/assets/showcase/codexmonitor.png) ](<https://clawhub.ai/odrobnik/codexmonitor>) [**Controllo stampante 3D Bambu** **@tobiasbischoff** • `hardware` `3d-printing` `skill` Controlla e risolve problemi delle stampanti BambuLab: stato, job, telecamera, AMS, calibrazione e altro. ![Skill Bambu CLI su ClawHub](/assets/showcase/bambu-cli.png) ](<https://clawhub.ai/tobiasbischoff/bambu-cli>) [**Trasporto di Vienna (Wiener Linien)** **@hjanuschka** • `travel` `transport` `skill` Partenze in tempo reale, interruzioni, stato degli ascensori e instradamento per il trasporto pubblico di Vienna. ![Skill Wiener Linien](/assets/showcase/wienerlinien.png) ](<https://clawhub.ai/hjanuschka/wienerlinien>) **Pasti scolastici ParentPay** **@George5562** • `automation` `browser` `parenting` Prenotazione automatizzata dei pasti scolastici nel Regno Unito tramite ParentPay. Usa coordinate del mouse per clic affidabili sulle celle della tabella. [**Upload R2 (Send Me My Files)** **@julianengel** • `files` `r2` `presigned-urls` Carica su Cloudflare R2/S3 e genera link di download presigned sicuri. Utile per istanze OpenClaw remote. ](<https://clawhub.ai/skills/r2-upload>) **App iOS via Telegram** **@coard** • `ios` `xcode` `testflight` Ha creato un'app iOS completa con mappe e registrazione vocale, distribuita su TestFlight interamente tramite chat Telegram. ![App iOS su TestFlight](/assets/showcase/ios-testflight.jpg) **Assistente salute Oura Ring** **@AS** • `health` `oura` `calendar` Assistente personale AI per la salute che integra dati Oura ring con calendario, appuntamenti e programma palestra. ![Assistente salute Oura ring](/assets/showcase/oura-health.png) [**Kev's Dream Team (14+ agenti)** **@adam91holt** • `multi-agent` `orchestration` Più di 14 agenti sotto un unico gateway con un orchestratore Opus 4.5 che delega a worker Codex. Vedi la [descrizione tecnica](<https://github.com/adam91holt/orchestrated-ai-articles>) e [Clawdspace](<https://github.com/adam91holt/clawdspace>) per il sandboxing degli agenti. ](<https://github.com/adam91holt/orchestrated-ai-articles>) [**Linear CLI** **@NessZerra** • `devtools` `linear` `cli` CLI per Linear che si integra con flussi di lavoro agentici (Claude Code, OpenClaw). Gestisci issue, progetti e workflow dal terminale. ](<https://github.com/Finesssee/linear-cli>) [**Beeper CLI** **@jules** • `messaging` `beeper` `cli` Leggi, invia e archivia messaggi tramite Beeper Desktop. Usa l'API MCP locale di Beeper così gli agenti possono gestire tutte le tue chat (iMessage, WhatsApp e altro) in un unico posto. ](<https://github.com/blqke/beepcli>)

## Automazione e flussi di lavoro

Pianificazione, controllo del browser, loop di supporto e il lato "fai il compito per me" del prodotto.

[**Controllo purificatore d'aria Winix** **@antonplex** • `automation` `hardware` `air-quality` Claude Code ha individuato e confermato i controlli del purificatore, poi OpenClaw prende il controllo per gestire la qualità dell'aria della stanza. ![Controllo del purificatore d'aria Winix tramite OpenClaw](/assets/showcase/winix-air-purifier.jpg) ](<https://x.com/antonplex/status/2010518442471006253>) [**Belle foto del cielo dalla telecamera** **@signalgaining** • `automation` `camera` `skill` Attivato da una telecamera sul tetto: chiedi a OpenClaw di scattare una foto del cielo ogni volta che appare bello. Ha progettato una skill e scattato la foto. ![Istantanea del cielo dalla telecamera sul tetto catturata da OpenClaw](/assets/showcase/roof-camera-sky.jpg) ](<https://x.com/signalgaining/status/2010523120604746151>) [**Scena di briefing mattutino visivo** **@buddyhadry** • `automation` `briefing` `telegram` Un prompt pianificato genera ogni mattina un'immagine di scena (meteo, attività, data, post o citazione preferita) tramite una persona OpenClaw. ](<https://x.com/buddyhadry/status/2010005331925954739>) [**Prenotazione campo da padel** **@joshp123** • `automation` `booking` `cli` Controllo disponibilità Playtomic più CLI di prenotazione. Non perdere mai più un campo libero. ![Screenshot di padel-cli](/assets/showcase/padel-screenshot.jpg) ](<https://github.com/joshp123/padel-cli>) **Acquisizione contabilità** **Community** • `automation` `email` `pdf` Raccoglie PDF dalle email, prepara i documenti per un consulente fiscale. Contabilità mensile in autopilota. [**Modalità sviluppatore dal divano** **@davekiss** • `telegram` `migration` `astro` Ha ricostruito un intero sito personale via Telegram mentre guardava Netflix — da Notion a Astro, 18 post migrati, DNS su Cloudflare. Non ha mai aperto un laptop. ](<https://davekiss.com>) **Agente per la ricerca di lavoro** **@attol8** • `automation` `api` `skill` Cerca annunci di lavoro, li confronta con parole chiave del CV e restituisce opportunità rilevanti con link. Creato in 30 minuti usando l'API JSearch. [**Costruttore di skill Jira** **@jdrhyne** • `jira` `skill` `devtools` OpenClaw si è collegato a Jira, poi ha generato una nuova skill al volo (prima che esistesse su ClawHub). ](<https://x.com/jdrhyne/status/2008336434827002232>) [**Skill Todoist via Telegram** **@iamsubhrajyoti** • `todoist` `skill` `telegram` Ha automatizzato attività Todoist e fatto generare a OpenClaw la skill direttamente nella chat Telegram. ](<https://x.com/iamsubhrajyoti/status/2009949389884920153>) **Analisi TradingView** **@bheem1798** • `finance` `browser` `automation` Accede a TradingView tramite automazione del browser, cattura screenshot dei grafici ed esegue analisi tecnica su richiesta. Nessuna API necessaria — solo controllo del browser. **Supporto automatico su Slack** **@henrymascot** • `slack` `automation` `support` Osserva un canale Slack aziendale, risponde in modo utile e inoltra notifiche a Telegram. Ha corretto autonomamente un bug di produzione in un'app distribuita senza che nessuno glielo chiedesse.

## Conoscenza e memory

Sistemi che indicizzano, cercano, ricordano e ragionano su conoscenza personale o di team.

[**xuezh apprendimento del cinese** **@joshp123** • `learning` `voice` `skill` Motore per l'apprendimento del cinese con feedback sulla pronuncia e flussi di studio tramite OpenClaw. ![Feedback sulla pronuncia di xuezh](/assets/showcase/xuezh-pronunciation.jpeg) ](<https://github.com/joshp123/xuezh>) **Vault di memory WhatsApp** **Community** • `memory` `transcription` `indexing` Importa esportazioni complete di WhatsApp, trascrive più di 1.000 note vocali, le confronta con i log git e produce report markdown collegati. [**Ricerca semantica Karakeep** **@jamesbrooksco** • `search` `vector` `bookmarks` Aggiunge ricerca vettoriale ai segnalibri Karakeep usando Qdrant più embedding OpenAI o Ollama. ](<https://github.com/jamesbrooksco/karakeep-semantic-search>) **Memory Inside-Out-2** **Community** • `memory` `beliefs` `self-model` Gestore di memory separato che trasforma i file di sessione in ricordi, poi in convinzioni, poi in un modello del sé in evoluzione.

## Voce e telefono

Punti di ingresso speech-first, bridge telefonici e flussi di lavoro ricchi di trascrizione.

[**Bridge telefonico Clawdia** **@alejandroOPI** • `voice` `vapi` `bridge` Bridge HTTP da assistente vocale Vapi a OpenClaw. Telefonate quasi in tempo reale con il tuo agente. ](<https://github.com/alejandroOPI/clawdia-bridge>) [**Trascrizione OpenRouter** **@obviyus** • `transcription` `multilingual` `skill` Trascrizione audio multilingue tramite OpenRouter (Gemini e altro). Disponibile su ClawHub. ](<https://clawhub.ai/obviyus/openrouter-transcribe>)

## Infrastruttura e distribuzione

Packaging, distribuzione e integrazioni che rendono OpenClaw più facile da eseguire ed estendere.

[**Add-on Home Assistant** **@ngutman** • `homeassistant` `docker` `raspberry-pi` Gateway OpenClaw in esecuzione su Home Assistant OS con supporto per tunnel SSH e stato persistente. ](<https://github.com/ngutman/openclaw-ha-addon>) [**Skill Home Assistant** **ClawHub** • `homeassistant` `skill` `automation` Controlla e automatizza i dispositivi Home Assistant tramite linguaggio naturale. ](<https://clawhub.ai/skills/homeassistant>) [**Packaging Nix** **@openclaw** • `nix` `packaging` `deployment` Configurazione OpenClaw in stile nix con tutto incluso per distribuzioni riproducibili. ](<https://github.com/openclaw/nix-openclaw>) [**Calendario CalDAV** **ClawHub** • `calendar` `caldav` `skill` Skill calendario che usa khal e vdirsyncer. Integrazione con calendario self-hosted. ](<https://clawhub.ai/skills/caldav-calendar>)

## Casa e hardware

Il lato fisico di OpenClaw: case, sensori, telecamere, aspirapolvere e altri dispositivi.

[**Automazione GoHome** **@joshp123** • `home` `nix` `grafana` Automazione domestica nativa Nix con OpenClaw come interfaccia, più dashboard Grafana. ![Dashboard Grafana di GoHome](/assets/showcase/gohome-grafana.png) ](<https://github.com/joshp123/gohome>) [**Aspirapolvere Roborock** **@joshp123** • `vacuum` `iot` `plugin` Controlla il tuo robot aspirapolvere Roborock tramite conversazione naturale. ![Stato di Roborock](/assets/showcase/roborock-screenshot.jpg) ](<https://github.com/joshp123/gohome/tree/main/plugins/roborock>)

## Progetti della community

Cose che sono cresciute oltre un singolo flusso di lavoro fino a diventare prodotti o ecosistemi più ampi.

[**Marketplace StarSwap** **Community** • `marketplace` `astronomy` `webapp` Marketplace completo di attrezzatura astronomica. Costruito con e attorno all'ecosistema OpenClaw. ](<https://star-swap.com/>)

## Invia il tuo progetto

* ### Condividilo

Pubblica in [#self-promotion su Discord](<https://discord.gg/clawd>) oppure [twitta a @openclaw](<https://x.com/openclaw>).

* ### Includi i dettagli

Dicci cosa fa, inserisci un link al repository o alla demo e condividi uno screenshot se ne hai uno.

* ### Ottieni visibilità

Aggiungeremo i progetti più interessanti a questa pagina.

## Correlati

  * [Getting started](</it/start/getting-started>)
  * [OpenClaw](</it/start/openclaw>)


Was this useful?YesNo