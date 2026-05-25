---
title: Référence CLI
source_url: https://docs.openclaw.ai/fr/cli
scraped_at: 2026-05-25
---

`openclaw` est le point d’entrée principal de la CLI. Chaque commande principale dispose soit d’une page de référence dédiée, soit d’une documentation avec la commande dont elle est l’alias ; cet index liste les commandes, les indicateurs globaux et les règles de style de sortie qui s’appliquent à toute la CLI.

Utilisez les commandes de configuration selon l’intention :

  * `openclaw setup` crée la configuration de base et l’espace de travail sans parcourir le flux complet d’intégration guidée.
  * `openclaw onboard` est le parcours complet guidé de première exécution pour le gateway, l’authentification des modèles, l’espace de travail, les canaux, les skills et l’état de santé.
  * `openclaw configure` modifie des parties ciblées d’une configuration existante, comme l’authentification des modèles, le gateway, les canaux, les plugins ou les skills.
  * `openclaw channels add` configure les comptes de canal une fois la configuration de base en place ; exécutez-la sans indicateurs pour une configuration guidée des canaux ou avec des indicateurs propres au canal pour les scripts.


## Pages de commandes

Zone | Commandes  
---|---  
Configuration et intégration | [`crestodian`](</fr/cli/crestodian>) · [`setup`](</fr/cli/setup>) · [`onboard`](</fr/cli/onboard>) · [`configure`](</fr/cli/configure>) · [`config`](</fr/cli/config>) · [`completion`](</fr/cli/completion>) · [`doctor`](</fr/cli/doctor>) · [`dashboard`](</fr/cli/dashboard>)  
Réinitialisation et désinstallation | [`backup`](</fr/cli/backup>) · [`reset`](</fr/cli/reset>) · [`uninstall`](</fr/cli/uninstall>) · [`update`](</fr/cli/update>)  
Messagerie et agents | [`message`](</fr/cli/message>) · [`agent`](</fr/cli/agent>) · [`agents`](</fr/cli/agents>) · [`acp`](</fr/cli/acp>) · [`mcp`](</fr/cli/mcp>)  
Santé et sessions | [`status`](</fr/cli/status>) · [`health`](</fr/cli/health>) · [`sessions`](</fr/cli/sessions>)  
Gateway et journaux | [`gateway`](</fr/cli/gateway>) · [`logs`](</fr/cli/logs>) · [`system`](</fr/cli/system>)  
Modèles et inférence | [`models`](</fr/cli/models>) · [`infer`](</fr/cli/infer>) · `capability` (alias de [`infer`](</fr/cli/infer>)) · [`memory`](</fr/cli/memory>) · [`commitments`](</fr/cli/commitments>) · [`wiki`](</fr/cli/wiki>)  
Réseau et nœuds | [`directory`](</fr/cli/directory>) · [`nodes`](</fr/cli/nodes>) · [`devices`](</fr/cli/devices>) · [`node`](</fr/cli/node>)  
Runtime et bac à sable | [`approvals`](</fr/cli/approvals>) · `exec-policy` (voir [`approvals`](</fr/cli/approvals>)) · [`sandbox`](</fr/cli/sandbox>) · [`tui`](</fr/cli/tui>) · `chat`/`terminal` (alias de [`tui --local`](</fr/cli/tui>)) · [`browser`](</fr/cli/browser>)  
Automatisation | [`cron`](</fr/cli/cron>) · [`tasks`](</fr/cli/tasks>) · [`hooks`](</fr/cli/hooks>) · [`webhooks`](</fr/cli/webhooks>)  
Découverte et documentation | [`dns`](</fr/cli/dns>) · [`docs`](</fr/cli/docs>)  
Appairage et canaux | [`pairing`](</fr/cli/pairing>) · [`qr`](</fr/cli/qr>) · [`channels`](</fr/cli/channels>)  
Sécurité et plugins | [`security`](</fr/cli/security>) · [`secrets`](</fr/cli/secrets>) · [`skills`](</fr/cli/skills>) · [`plugins`](</fr/cli/plugins>) · [`proxy`](</fr/cli/proxy>)  
Alias hérités | [`daemon`](</fr/cli/daemon>) (service gateway) · [`clawbot`](</fr/cli/clawbot>) (espace de noms)  
Plugins (facultatifs) | [`path`](</fr/cli/path>) · [`voicecall`](</fr/cli/voicecall>) (si installé)  
  
## Indicateurs globaux

Indicateur | Objectif  
---|---  
`--dev` | Isole l’état sous `~/.openclaw-dev` et décale les ports par défaut  
`--profile <name>` | Isole l’état sous `~/.openclaw-<name>`  
`--container <name>` | Cible un conteneur nommé pour l’exécution  
`--no-color` | Désactive les couleurs ANSI (`NO_COLOR=1` est aussi respecté)  
`--update` | Raccourci pour [`openclaw update`](</fr/cli/update>) (installations depuis les sources uniquement)  
`-V`, `--version`, `-v` | Affiche la version et quitte  
  
## Modes de sortie

  * Les couleurs ANSI et les indicateurs de progression ne s’affichent que dans les sessions TTY.
  * Les liens hypertexte OSC-8 s’affichent comme des liens cliquables lorsque c’est pris en charge ; sinon, la CLI revient à des URL simples.
  * `--json` (et `--plain` lorsque pris en charge) désactive le style pour une sortie propre.
  * Les commandes de longue durée affichent un indicateur de progression (OSC 9;4 lorsque pris en charge).


Source de vérité de la palette : `src/terminal/palette.ts`.

## Arborescence des commandes

Arborescence complète des commandes CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Les plugins peuvent ajouter des commandes supplémentaires de premier niveau (par exemple `openclaw voicecall`).

## Commandes slash du chat

Les messages de chat prennent en charge les commandes `/...`. Consultez les [commandes slash](</fr/tools/slash-commands>).

Points forts :

  * `/status` — diagnostics rapides.
  * `/trace` — lignes de trace/débogage du plugin limitées à la session.
  * `/config` — modifications de configuration persistées.
  * `/debug` — remplacements de configuration limités au runtime (mémoire, pas le disque ; nécessite `commands.debug: true`).


## Suivi de l’utilisation

`openclaw status --usage` et l’interface Control affichent l’utilisation/le quota des fournisseurs lorsque les identifiants OAuth/API sont disponibles. Les données proviennent directement des points de terminaison d’utilisation des fournisseurs et sont normalisées en `X% left`. Fournisseurs avec des fenêtres d’utilisation actuelles : Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi et [z.ai](<http://z.ai>).

Consultez le [suivi de l’utilisation](</fr/concepts/usage-tracking>) pour plus de détails.

## Connexe

  * [Commandes slash](</fr/tools/slash-commands>)
  * [Configuration](</fr/gateway/configuration>)
  * [Environnement](</fr/help/environment>)


Was this useful?YesNo