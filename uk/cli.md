---
title: Довідник CLI
source_url: https://docs.openclaw.ai/uk/cli
scraped_at: 2026-05-25
---

`openclaw` є основною точкою входу CLI. Кожна основна команда має або окрему довідкову сторінку, або документується разом із командою, псевдонімом якої вона є; цей індекс перелічує команди, глобальні прапорці та правила оформлення виводу, що застосовуються в усьому CLI.

Використовуйте команди налаштування відповідно до мети:

  * `openclaw setup` створює базову конфігурацію та робочий простір без проходження повного керованого сценарію початкового налаштування.
  * `openclaw onboard` — це повний керований шлях першого запуску для Gateway, авторизації моделей, робочого простору, каналів, Skills і стану системи.
  * `openclaw configure` змінює окремі частини наявного налаштування, як-от авторизацію моделей, Gateway, канали, plugins або Skills.
  * `openclaw channels add` налаштовує облікові записи каналів після створення бази; запустіть її без прапорців для керованого налаштування каналів або з прапорцями конкретного каналу для скриптів.


## Сторінки команд

Область | Команди  
---|---  
Налаштування та початкове налаштування | [`crestodian`](</uk/cli/crestodian>) · [`setup`](</uk/cli/setup>) · [`onboard`](</uk/cli/onboard>) · [`configure`](</uk/cli/configure>) · [`config`](</uk/cli/config>) · [`completion`](</uk/cli/completion>) · [`doctor`](</uk/cli/doctor>) · [`dashboard`](</uk/cli/dashboard>)  
Скидання та видалення | [`backup`](</uk/cli/backup>) · [`reset`](</uk/cli/reset>) · [`uninstall`](</uk/cli/uninstall>) · [`update`](</uk/cli/update>)  
Повідомлення та агенти | [`message`](</uk/cli/message>) · [`agent`](</uk/cli/agent>) · [`agents`](</uk/cli/agents>) · [`acp`](</uk/cli/acp>) · [`mcp`](</uk/cli/mcp>)  
Стан системи та сеанси | [`status`](</uk/cli/status>) · [`health`](</uk/cli/health>) · [`sessions`](</uk/cli/sessions>)  
Gateway і журнали | [`gateway`](</uk/cli/gateway>) · [`logs`](</uk/cli/logs>) · [`system`](</uk/cli/system>)  
Моделі та інференс | [`models`](</uk/cli/models>) · [`infer`](</uk/cli/infer>) · `capability` (псевдонім для [`infer`](</uk/cli/infer>)) · [`memory`](</uk/cli/memory>) · [`commitments`](</uk/cli/commitments>) · [`wiki`](</uk/cli/wiki>)  
Мережа та вузли | [`directory`](</uk/cli/directory>) · [`nodes`](</uk/cli/nodes>) · [`devices`](</uk/cli/devices>) · [`node`](</uk/cli/node>)  
Runtime і пісочниця | [`approvals`](</uk/cli/approvals>) · `exec-policy` (див. [`approvals`](</uk/cli/approvals>)) · [`sandbox`](</uk/cli/sandbox>) · [`tui`](</uk/cli/tui>) · `chat`/`terminal` (псевдоніми для [`tui --local`](</uk/cli/tui>)) · [`browser`](</uk/cli/browser>)  
Автоматизація | [`cron`](</uk/cli/cron>) · [`tasks`](</uk/cli/tasks>) · [`hooks`](</uk/cli/hooks>) · [`webhooks`](</uk/cli/webhooks>)  
Виявлення та документація | [`dns`](</uk/cli/dns>) · [`docs`](</uk/cli/docs>)  
Сполучення та канали | [`pairing`](</uk/cli/pairing>) · [`qr`](</uk/cli/qr>) · [`channels`](</uk/cli/channels>)  
Безпека та plugins | [`security`](</uk/cli/security>) · [`secrets`](</uk/cli/secrets>) · [`skills`](</uk/cli/skills>) · [`plugins`](</uk/cli/plugins>) · [`proxy`](</uk/cli/proxy>)  
Застарілі псевдоніми | [`daemon`](</uk/cli/daemon>) (служба Gateway) · [`clawbot`](</uk/cli/clawbot>) (простір імен)  
Plugins (необов’язково) | [`path`](</uk/cli/path>) · [`voicecall`](</uk/cli/voicecall>) (якщо встановлено)  
  
## Глобальні прапорці

Прапорець | Призначення  
---|---  
`--dev` | Ізолює стан у `~/.openclaw-dev` і зміщує стандартні порти  
`--profile <name>` | Ізолює стан у `~/.openclaw-<name>`  
`--container <name>` | Націлює виконання на іменований контейнер  
`--no-color` | Вимикає кольори ANSI (також враховується `NO_COLOR=1`)  
`--update` | Скорочення для [`openclaw update`](</uk/cli/update>) (лише встановлення з джерела)  
`-V`, `--version`, `-v` | Виводить версію та завершує роботу  
  
## Режими виводу

  * Кольори ANSI та індикатори прогресу відображаються лише в сеансах TTY.
  * Гіперпосилання OSC-8 відображаються як клікабельні посилання там, де це підтримується; інакше CLI повертається до звичайних URL.
  * `--json` (і `--plain`, де підтримується) вимикає оформлення для чистого виводу.
  * Довготривалі команди показують індикатор прогресу (OSC 9;4, якщо підтримується).


Джерело істини для палітри: `src/terminal/palette.ts`.

## Дерево команд

Повне дерево команд CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins можуть додавати додаткові команди верхнього рівня (наприклад, `openclaw voicecall`).

## Слеш-команди чату

Повідомлення чату підтримують команди `/...`. Див. [слеш-команди](</uk/tools/slash-commands>).

Основне:

  * `/status` — швидка діагностика.
  * `/trace` — рядки трасування/налагодження Plugin у межах сеансу.
  * `/config` — збережені зміни конфігурації.
  * `/debug` — перевизначення конфігурації лише для runtime (у пам’яті, не на диску; потребує `commands.debug: true`).


## Відстеження використання

`openclaw status --usage` і Control UI показують використання/квоту провайдера, коли доступні облікові дані OAuth/API. Дані надходять безпосередньо з кінцевих точок використання провайдера та нормалізуються до `X% left`. Провайдери з поточними вікнами використання: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi та [z.ai](<http://z.ai>).

Докладніше див. [відстеження використання](</uk/concepts/usage-tracking>).

## Пов’язане

  * [Слеш-команди](</uk/tools/slash-commands>)
  * [Конфігурація](</uk/gateway/configuration>)
  * [Середовище](</uk/help/environment>)


Was this useful?YesNo