---
title: CLI-referentie
source_url: https://docs.openclaw.ai/nl/cli
scraped_at: 2026-05-25
---

`openclaw` is het belangrijkste CLI-toegangspunt. Elke kernopdracht heeft een eigen referentiepagina of is gedocumenteerd bij de opdracht waarvoor deze een alias is; deze index vermeldt de opdrachten, de globale flags en de regels voor uitvoerstyling die voor de hele CLI gelden.

Gebruik de setup-opdrachten naar intentie:

  * `openclaw setup` maakt de basisconfiguratie en werkruimte aan zonder de volledige begeleide onboarding-flow te doorlopen.
  * `openclaw onboard` is het volledige begeleide pad voor de eerste uitvoering voor Gateway, modelauthenticatie, werkruimte, kanalen, Skills en gezondheid.
  * `openclaw configure` wijzigt gerichte onderdelen van een bestaande setup, zoals modelauthenticatie, Gateway, kanalen, plugins of Skills.
  * `openclaw channels add` configureert kanaalaccounts nadat de basis bestaat; voer dit zonder flags uit voor begeleide kanaalsetup of met kanaalspecifieke flags voor scripts.


## Opdrachtpagina's

Gebied | Opdrachten  
---|---  
Setup en onboarding | [`crestodian`](</nl/cli/crestodian>) · [`setup`](</nl/cli/setup>) · [`onboard`](</nl/cli/onboard>) · [`configure`](</nl/cli/configure>) · [`config`](</nl/cli/config>) · [`completion`](</nl/cli/completion>) · [`doctor`](</nl/cli/doctor>) · [`dashboard`](</nl/cli/dashboard>)  
Reset en verwijderen | [`backup`](</nl/cli/backup>) · [`reset`](</nl/cli/reset>) · [`uninstall`](</nl/cli/uninstall>) · [`update`](</nl/cli/update>)  
Berichten en agents | [`message`](</nl/cli/message>) · [`agent`](</nl/cli/agent>) · [`agents`](</nl/cli/agents>) · [`acp`](</nl/cli/acp>) · [`mcp`](</nl/cli/mcp>)  
Gezondheid en sessies | [`status`](</nl/cli/status>) · [`health`](</nl/cli/health>) · [`sessions`](</nl/cli/sessions>)  
Gateway en logs | [`gateway`](</nl/cli/gateway>) · [`logs`](</nl/cli/logs>) · [`system`](</nl/cli/system>)  
Modellen en inferentie | [`models`](</nl/cli/models>) · [`infer`](</nl/cli/infer>) · `capability` (alias voor [`infer`](</nl/cli/infer>)) · [`memory`](</nl/cli/memory>) · [`commitments`](</nl/cli/commitments>) · [`wiki`](</nl/cli/wiki>)  
Netwerk en nodes | [`directory`](</nl/cli/directory>) · [`nodes`](</nl/cli/nodes>) · [`devices`](</nl/cli/devices>) · [`node`](</nl/cli/node>)  
Runtime en sandbox | [`approvals`](</nl/cli/approvals>) · `exec-policy` (zie [`approvals`](</nl/cli/approvals>)) · [`sandbox`](</nl/cli/sandbox>) · [`tui`](</nl/cli/tui>) · `chat`/`terminal` (aliassen voor [`tui --local`](</nl/cli/tui>)) · [`browser`](</nl/cli/browser>)  
Automatisering | [`cron`](</nl/cli/cron>) · [`tasks`](</nl/cli/tasks>) · [`hooks`](</nl/cli/hooks>) · [`webhooks`](</nl/cli/webhooks>)  
Detectie en docs | [`dns`](</nl/cli/dns>) · [`docs`](</nl/cli/docs>)  
Koppelen en kanalen | [`pairing`](</nl/cli/pairing>) · [`qr`](</nl/cli/qr>) · [`channels`](</nl/cli/channels>)  
Beveiliging en plugins | [`security`](</nl/cli/security>) · [`secrets`](</nl/cli/secrets>) · [`skills`](</nl/cli/skills>) · [`plugins`](</nl/cli/plugins>) · [`proxy`](</nl/cli/proxy>)  
Verouderde aliassen | [`daemon`](</nl/cli/daemon>) (Gateway-service) · [`clawbot`](</nl/cli/clawbot>) (naamruimte)  
Plugins (optioneel) | [`path`](</nl/cli/path>) · [`voicecall`](</nl/cli/voicecall>) (indien geïnstalleerd)  
  
## Globale flags

Flag | Doel  
---|---  
`--dev` | Isoleer status onder `~/.openclaw-dev` en verschuif standaardpoorten  
`--profile <name>` | Isoleer status onder `~/.openclaw-<name>`  
`--container <name>` | Richt uitvoering op een benoemde container  
`--no-color` | Schakel ANSI-kleuren uit (`NO_COLOR=1` wordt ook gerespecteerd)  
`--update` | Afkorting voor [`openclaw update`](</nl/cli/update>) (alleen broninstallaties)  
`-V`, `--version`, `-v` | Druk de versie af en sluit af  
  
## Uitvoermodi

  * ANSI-kleuren en voortgangsindicatoren worden alleen in TTY-sessies weergegeven.
  * OSC-8-hyperlinks worden waar ondersteund als klikbare links weergegeven; anders valt de CLI terug op platte URL's.
  * `--json` (en `--plain` waar ondersteund) schakelt styling uit voor schone uitvoer.
  * Langlopende opdrachten tonen een voortgangsindicator (OSC 9;4 waar ondersteund).


Bron van waarheid voor het palet: `src/terminal/palette.ts`.

## Opdrachtboom

Volledige opdrachtboom CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins kunnen extra opdrachten op topniveau toevoegen (bijvoorbeeld `openclaw voicecall`).

## Slash-opdrachten voor chat

Chatberichten ondersteunen `/...`-opdrachten. Zie [slash-opdrachten](</nl/tools/slash-commands>).

Hoogtepunten:

  * `/status` — snelle diagnostiek.
  * `/trace` — plugin-trace/debugregels binnen het sessiebereik.
  * `/config` — blijvende configuratiewijzigingen.
  * `/debug` — configuratie-overschrijvingen alleen voor runtime (geheugen, niet schijf; vereist `commands.debug: true`).


## Gebruiksregistratie

`openclaw status --usage` en de Control UI tonen providergebruik/quota wanneer OAuth/API-referenties beschikbaar zijn. Gegevens komen rechtstreeks van provider-endpoints voor gebruik en worden genormaliseerd naar `X% left`. Providers met huidige gebruiksvensters: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi en [z.ai](<http://z.ai>).

Zie [Gebruiksregistratie](</nl/concepts/usage-tracking>) voor details.

## Gerelateerd

  * [Slash-opdrachten](</nl/tools/slash-commands>)
  * [Configuratie](</nl/gateway/configuration>)
  * [Omgeving](</nl/help/environment>)


Was this useful?YesNo