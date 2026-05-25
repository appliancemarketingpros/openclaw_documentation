---
title: CLI-Referenz
source_url: https://docs.openclaw.ai/de/cli
scraped_at: 2026-05-25
---

`openclaw` ist der zentrale CLI-Einstiegspunkt. Jeder Kernbefehl hat entweder eine eigene Referenzseite oder ist bei dem Befehl dokumentiert, für den er ein Alias ist; dieser Index listet die Befehle, die globalen Flags und die Regeln für die Ausgabegestaltung auf, die in der gesamten CLI gelten.

Verwenden Sie die Einrichtungsbefehle je nach Zweck:

  * `openclaw setup` erstellt die Basiskonfiguration und den Workspace, ohne den vollständigen geführten Onboarding-Ablauf zu durchlaufen.
  * `openclaw onboard` ist der vollständige geführte Erststartpfad für Gateway, Modellauthentifizierung, Workspace, Kanäle, Skills und Zustand.
  * `openclaw configure` ändert gezielt Teile einer bestehenden Einrichtung, etwa Modellauthentifizierung, Gateway, Kanäle, Plugins oder Skills.
  * `openclaw channels add` konfiguriert Kanalkonten, nachdem die Basis vorhanden ist; führen Sie den Befehl ohne Flags für eine geführte Kanaleinrichtung oder mit kanalspezifischen Flags für Skripte aus.


## Befehlsseiten

Bereich | Befehle  
---|---  
Einrichtung und Onboarding | [`crestodian`](</de/cli/crestodian>) · [`setup`](</de/cli/setup>) · [`onboard`](</de/cli/onboard>) · [`configure`](</de/cli/configure>) · [`config`](</de/cli/config>) · [`completion`](</de/cli/completion>) · [`doctor`](</de/cli/doctor>) · [`dashboard`](</de/cli/dashboard>)  
Zurücksetzen und Deinstallation | [`backup`](</de/cli/backup>) · [`reset`](</de/cli/reset>) · [`uninstall`](</de/cli/uninstall>) · [`update`](</de/cli/update>)  
Messaging und Agenten | [`message`](</de/cli/message>) · [`agent`](</de/cli/agent>) · [`agents`](</de/cli/agents>) · [`acp`](</de/cli/acp>) · [`mcp`](</de/cli/mcp>)  
Zustand und Sitzungen | [`status`](</de/cli/status>) · [`health`](</de/cli/health>) · [`sessions`](</de/cli/sessions>)  
Gateway und Logs | [`gateway`](</de/cli/gateway>) · [`logs`](</de/cli/logs>) · [`system`](</de/cli/system>)  
Modelle und Inferenz | [`models`](</de/cli/models>) · [`infer`](</de/cli/infer>) · `capability` (Alias für [`infer`](</de/cli/infer>)) · [`memory`](</de/cli/memory>) · [`commitments`](</de/cli/commitments>) · [`wiki`](</de/cli/wiki>)  
Netzwerk und Nodes | [`directory`](</de/cli/directory>) · [`nodes`](</de/cli/nodes>) · [`devices`](</de/cli/devices>) · [`node`](</de/cli/node>)  
Laufzeit und Sandbox | [`approvals`](</de/cli/approvals>) · `exec-policy` (siehe [`approvals`](</de/cli/approvals>)) · [`sandbox`](</de/cli/sandbox>) · [`tui`](</de/cli/tui>) · `chat`/`terminal` (Aliasse für [`tui --local`](</de/cli/tui>)) · [`browser`](</de/cli/browser>)  
Automatisierung | [`cron`](</de/cli/cron>) · [`tasks`](</de/cli/tasks>) · [`hooks`](</de/cli/hooks>) · [`webhooks`](</de/cli/webhooks>)  
Discovery und Dokumentation | [`dns`](</de/cli/dns>) · [`docs`](</de/cli/docs>)  
Pairing und Kanäle | [`pairing`](</de/cli/pairing>) · [`qr`](</de/cli/qr>) · [`channels`](</de/cli/channels>)  
Sicherheit und Plugins | [`security`](</de/cli/security>) · [`secrets`](</de/cli/secrets>) · [`skills`](</de/cli/skills>) · [`plugins`](</de/cli/plugins>) · [`proxy`](</de/cli/proxy>)  
Legacy-Aliasse | [`daemon`](</de/cli/daemon>) (Gateway-Dienst) · [`clawbot`](</de/cli/clawbot>) (Namespace)  
Plugins (optional) | [`path`](</de/cli/path>) · [`voicecall`](</de/cli/voicecall>) (falls installiert)  
  
## Globale Flags

Flag | Zweck  
---|---  
`--dev` | Isoliert den Zustand unter `~/.openclaw-dev` und verschiebt Standardports  
`--profile <name>` | Isoliert den Zustand unter `~/.openclaw-<name>`  
`--container <name>` | Wählt einen benannten Container für die Ausführung aus  
`--no-color` | Deaktiviert ANSI-Farben (`NO_COLOR=1` wird ebenfalls berücksichtigt)  
`--update` | Kurzform für [`openclaw update`](</de/cli/update>) (nur Quellinstallationen)  
`-V`, `--version`, `-v` | Gibt die Version aus und beendet das Programm  
  
## Ausgabemodi

  * ANSI-Farben und Fortschrittsanzeigen werden nur in TTY-Sitzungen gerendert.
  * OSC-8-Hyperlinks werden als anklickbare Links gerendert, sofern unterstützt; andernfalls fällt die CLI auf einfache URLs zurück.
  * `--json` (und `--plain`, sofern unterstützt) deaktiviert die Gestaltung für saubere Ausgabe.
  * Lang laufende Befehle zeigen eine Fortschrittsanzeige an (OSC 9;4, sofern unterstützt).


Verbindliche Quelle für die Palette: `src/terminal/palette.ts`.

## Befehlsbaum

Vollständiger Befehlsbaum CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins können zusätzliche Befehle auf oberster Ebene hinzufügen (zum Beispiel `openclaw voicecall`).

## Chat-Slash-Befehle

Chat-Nachrichten unterstützen `/...`-Befehle. Siehe [Slash-Befehle](</de/tools/slash-commands>).

Highlights:

  * `/status` — schnelle Diagnose.
  * `/trace` — sitzungsbezogene Plugin-Trace-/Debug-Zeilen.
  * `/config` — persistierte Konfigurationsänderungen.
  * `/debug` — reine Laufzeit-Konfigurationsüberschreibungen (Speicher, nicht Datenträger; erfordert `commands.debug: true`).


## Nutzungsverfolgung

`openclaw status --usage` und die Control-UI zeigen Provider-Nutzung und Kontingente an, wenn OAuth-/API-Zugangsdaten verfügbar sind. Die Daten stammen direkt aus den Provider-Nutzungsendpunkten und werden auf `X% left` normalisiert. Provider mit aktuellen Nutzungsfenstern: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi und [z.ai](<http://z.ai>).

Weitere Informationen finden Sie unter [Nutzungsverfolgung](</de/concepts/usage-tracking>).

## Verwandte Themen

  * [Slash-Befehle](</de/tools/slash-commands>)
  * [Konfiguration](</de/gateway/configuration>)
  * [Umgebung](</de/help/environment>)


Was this useful?YesNo