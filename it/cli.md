---
title: Riferimento CLI
source_url: https://docs.openclaw.ai/it/cli
scraped_at: 2026-05-25
---

`openclaw` è il punto di ingresso principale della CLI. Ogni comando core ha una pagina di riferimento dedicata oppure è documentato con il comando di cui è alias; questo indice elenca i comandi, i flag globali e le regole di stile dell'output che si applicano in tutta la CLI.

Usa i comandi di configurazione in base all'intento:

  * `openclaw setup` crea la configurazione di base e il workspace senza eseguire l'intero flusso di onboarding guidato.
  * `openclaw onboard` è il percorso completo guidato di primo avvio per Gateway, autenticazione del modello, workspace, canali, skills e stato di salute.
  * `openclaw configure` modifica parti mirate di una configurazione esistente, come autenticazione del modello, Gateway, canali, plugins o skills.
  * `openclaw channels add` configura gli account dei canali dopo che la base esiste; eseguilo senza flag per la configurazione guidata dei canali o con flag specifici del canale per gli script.


## Pagine dei comandi

Area | Comandi  
---|---  
Configurazione e onboarding | [`crestodian`](</it/cli/crestodian>) · [`setup`](</it/cli/setup>) · [`onboard`](</it/cli/onboard>) · [`configure`](</it/cli/configure>) · [`config`](</it/cli/config>) · [`completion`](</it/cli/completion>) · [`doctor`](</it/cli/doctor>) · [`dashboard`](</it/cli/dashboard>)  
Ripristino e disinstallazione | [`backup`](</it/cli/backup>) · [`reset`](</it/cli/reset>) · [`uninstall`](</it/cli/uninstall>) · [`update`](</it/cli/update>)  
Messaggistica e agenti | [`message`](</it/cli/message>) · [`agent`](</it/cli/agent>) · [`agents`](</it/cli/agents>) · [`acp`](</it/cli/acp>) · [`mcp`](</it/cli/mcp>)  
Stato di salute e sessioni | [`status`](</it/cli/status>) · [`health`](</it/cli/health>) · [`sessions`](</it/cli/sessions>)  
Gateway e log | [`gateway`](</it/cli/gateway>) · [`logs`](</it/cli/logs>) · [`system`](</it/cli/system>)  
Modelli e inferenza | [`models`](</it/cli/models>) · [`infer`](</it/cli/infer>) · `capability` (alias di [`infer`](</it/cli/infer>)) · [`memory`](</it/cli/memory>) · [`commitments`](</it/cli/commitments>) · [`wiki`](</it/cli/wiki>)  
Rete e nodi | [`directory`](</it/cli/directory>) · [`nodes`](</it/cli/nodes>) · [`devices`](</it/cli/devices>) · [`node`](</it/cli/node>)  
Runtime e sandbox | [`approvals`](</it/cli/approvals>) · `exec-policy` (vedi [`approvals`](</it/cli/approvals>)) · [`sandbox`](</it/cli/sandbox>) · [`tui`](</it/cli/tui>) · `chat`/`terminal` (alias di [`tui --local`](</it/cli/tui>)) · [`browser`](</it/cli/browser>)  
Automazione | [`cron`](</it/cli/cron>) · [`tasks`](</it/cli/tasks>) · [`hooks`](</it/cli/hooks>) · [`webhooks`](</it/cli/webhooks>)  
Individuazione e documentazione | [`dns`](</it/cli/dns>) · [`docs`](</it/cli/docs>)  
Abbinamento e canali | [`pairing`](</it/cli/pairing>) · [`qr`](</it/cli/qr>) · [`channels`](</it/cli/channels>)  
Sicurezza e plugins | [`security`](</it/cli/security>) · [`secrets`](</it/cli/secrets>) · [`skills`](</it/cli/skills>) · [`plugins`](</it/cli/plugins>) · [`proxy`](</it/cli/proxy>)  
Alias legacy | [`daemon`](</it/cli/daemon>) (servizio Gateway) · [`clawbot`](</it/cli/clawbot>) (namespace)  
Plugins (opzionali) | [`path`](</it/cli/path>) · [`voicecall`](</it/cli/voicecall>) (se installato)  
  
## Flag globali

Flag | Scopo  
---|---  
`--dev` | Isola lo stato in `~/.openclaw-dev` e sposta le porte predefinite  
`--profile <name>` | Isola lo stato in `~/.openclaw-<name>`  
`--container <name>` | Seleziona un container denominato per l'esecuzione  
`--no-color` | Disabilita i colori ANSI (`NO_COLOR=1` viene rispettato anche)  
`--update` | Abbreviazione per [`openclaw update`](</it/cli/update>) (solo installazioni da sorgente)  
`-V`, `--version`, `-v` | Stampa la versione ed esce  
  
## Modalità di output

  * I colori ANSI e gli indicatori di avanzamento vengono renderizzati solo nelle sessioni TTY.
  * I collegamenti ipertestuali OSC-8 vengono renderizzati come link cliccabili dove supportati; altrimenti la CLI ripiega su URL semplici.
  * `--json` (e `--plain` dove supportato) disabilita lo stile per un output pulito.
  * I comandi a esecuzione prolungata mostrano un indicatore di avanzamento (OSC 9;4 quando supportato).


Fonte autorevole della palette: `src/terminal/palette.ts`.

## Albero dei comandi

Albero completo dei comandi CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

I plugins possono aggiungere ulteriori comandi di primo livello (per esempio `openclaw voicecall`).

## Comandi slash della chat

I messaggi di chat supportano comandi `/...`. Vedi [comandi slash](</it/tools/slash-commands>).

In evidenza:

  * `/status` — diagnostica rapida.
  * `/trace` — righe di trace/debug del plugin limitate alla sessione.
  * `/config` — modifiche persistenti della configurazione.
  * `/debug` — override della configurazione solo a runtime (memoria, non disco; richiede `commands.debug: true`).


## Monitoraggio dell'utilizzo

`openclaw status --usage` e la UI di controllo espongono utilizzo/quota del provider quando sono disponibili credenziali OAuth/API. I dati provengono direttamente dagli endpoint di utilizzo del provider e vengono normalizzati in `X% left`. Provider con finestre di utilizzo attuali: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi e [z.ai](<http://z.ai>).

Vedi [Monitoraggio dell'utilizzo](</it/concepts/usage-tracking>) per i dettagli.

## Correlati

  * [Comandi slash](</it/tools/slash-commands>)
  * [Configurazione](</it/gateway/configuration>)
  * [Ambiente](</it/help/environment>)


Was this useful?YesNo