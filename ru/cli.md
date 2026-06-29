---
title: Справочник CLI
source_url: https://docs.openclaw.ai/ru/cli
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw` — основная точка входа CLI. Для каждой базовой команды есть либо отдельная справочная страница, либо она документирована вместе с командой, для которой является псевдонимом; этот индекс перечисляет команды, глобальные флаги и правила оформления вывода, которые применяются во всем CLI.

Используйте команды настройки по назначению:

  * `openclaw setup` создает базовую конфигурацию и рабочую область без прохождения полного управляемого процесса первичной настройки.
  * `openclaw onboard` — полный управляемый путь первого запуска для Gateway, аутентификации модели, рабочей области, каналов, Skills и проверки состояния.
  * `openclaw configure` изменяет отдельные части существующей настройки, например аутентификацию модели, Gateway, каналы, плагины или Skills.
  * `openclaw channels add` настраивает учетные записи каналов после создания базовой конфигурации; запускайте ее без флагов для управляемой настройки канала или с флагами конкретного канала для скриптов.


## Страницы команд

Область | Команды  
---|---  
Настройка и онбординг | [`crestodian`](</ru/cli/crestodian>) · [`setup`](</ru/cli/setup>) · [`onboard`](</ru/cli/onboard>) · [`configure`](</ru/cli/configure>) · [`config`](</ru/cli/config>) · [`completion`](</ru/cli/completion>) · [`doctor`](</ru/cli/doctor>) · [`dashboard`](</ru/cli/dashboard>)  
Сброс и удаление | [`backup`](</ru/cli/backup>) · [`reset`](</ru/cli/reset>) · [`uninstall`](</ru/cli/uninstall>) · [`update`](</ru/cli/update>)  
Сообщения и агенты | [`message`](</ru/cli/message>) · [`agent`](</ru/cli/agent>) · [`agents`](</ru/cli/agents>) · [`acp`](</ru/cli/acp>) · [`mcp`](</ru/cli/mcp>)  
Состояние и сеансы | [`status`](</ru/cli/status>) · [`health`](</ru/cli/health>) · [`sessions`](</ru/cli/sessions>)  
Gateway и журналы | [`gateway`](</ru/cli/gateway>) · [`logs`](</ru/cli/logs>) · [`system`](</ru/cli/system>)  
Модели и инференс | [`models`](</ru/cli/models>) · [`infer`](</ru/cli/infer>) · `capability` (псевдоним для [`infer`](</ru/cli/infer>)) · [`memory`](</ru/cli/memory>) · [`commitments`](</ru/cli/commitments>) · [`wiki`](</ru/cli/wiki>)  
Сеть и узлы | [`directory`](</ru/cli/directory>) · [`nodes`](</ru/cli/nodes>) · [`devices`](</ru/cli/devices>) · [`node`](</ru/cli/node>)  
Runtime и песочница | [`approvals`](</ru/cli/approvals>) · `exec-policy` (см. [`approvals`](</ru/cli/approvals>)) · [`sandbox`](</ru/cli/sandbox>) · [`tui`](</ru/cli/tui>) · `chat`/`terminal` (псевдонимы для [`tui --local`](</ru/cli/tui>)) · [`browser`](</ru/cli/browser>)  
Автоматизация | [`cron`](</ru/cli/cron>) · [`tasks`](</ru/cli/tasks>) · [`hooks`](</ru/cli/hooks>) · [`webhooks`](</ru/cli/webhooks>) · [`transcripts`](</ru/cli/transcripts>)  
Обнаружение и документация | [`dns`](</ru/cli/dns>) · [`docs`](</ru/cli/docs>)  
Сопряжение и каналы | [`pairing`](</ru/cli/pairing>) · [`qr`](</ru/cli/qr>) · [`channels`](</ru/cli/channels>)  
Безопасность и плагины | [`security`](</ru/cli/security>) · [`secrets`](</ru/cli/secrets>) · [`skills`](</ru/cli/skills>) · [`plugins`](</ru/cli/plugins>) · [`proxy`](</ru/cli/proxy>)  
Устаревшие псевдонимы | [`daemon`](</ru/cli/daemon>) (служба Gateway) · [`clawbot`](</ru/cli/clawbot>) (пространство имен)  
Плагины (необязательно) | [`path`](</ru/cli/path>) · [`policy`](</ru/cli/policy>) · [`voicecall`](</ru/cli/voicecall>) · [`workboard`](</ru/cli/workboard>) (если установлен)  
  
## Глобальные флаги

Флаг | Назначение  
---|---  
`--dev` | Изолировать состояние в `~/.openclaw-dev` и сдвинуть порты по умолчанию  
`--profile <name>` | Изолировать состояние в `~/.openclaw-<name>`  
`--container <name>` | Выбрать именованный контейнер для выполнения  
`--no-color` | Отключить ANSI-цвета (`NO_COLOR=1` также учитывается)  
`--update` | Сокращение для [`openclaw update`](</ru/cli/update>) (только установки из исходников)  
`-V`, `--version`, `-v` | Вывести версию и завершить работу  
  
## Режимы вывода

  * ANSI-цвета и индикаторы прогресса отображаются только в TTY-сеансах.
  * Гиперссылки OSC-8 отображаются как кликабельные ссылки там, где это поддерживается; в остальных случаях CLI возвращается к обычным URL.
  * `--json` (и `--plain`, где поддерживается) отключает оформление для чистого вывода.
  * Длительные команды показывают индикатор прогресса (OSC 9;4, если поддерживается).


Единый источник палитры: `src/terminal/palette.ts`.

## Дерево команд

Полное дерево команд CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listworkboard  list  create  show  dispatchmemory  status  index  searchtranscripts  list  show  pathpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Плагины могут добавлять дополнительные команды верхнего уровня, например [`openclaw workboard`](</ru/cli/workboard>) или `openclaw voicecall`.

## Slash-команды чата

Сообщения чата поддерживают команды `/...`. См. [slash-команды](</ru/tools/slash-commands>).

Основное:

  * `/status` — быстрая диагностика.
  * `/trace` — строки трассировки и отладки плагина в рамках сеанса.
  * `/config` — сохраненные изменения конфигурации.
  * `/debug` — переопределения конфигурации только для runtime (в памяти, не на диске; требуется `commands.debug: true`).


## Отслеживание использования

`openclaw status --usage` и Control UI показывают использование/квоту провайдера, когда доступны учетные данные OAuth/API. Данные поступают напрямую из конечных точек использования провайдера и нормализуются в формат `X% left`. Провайдеры с текущими окнами использования: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi и z.ai.

Подробнее см. в разделе [Отслеживание использования](</ru/concepts/usage-tracking>).

## Связанные разделы

  * [Slash-команды](</ru/tools/slash-commands>)
  * [Конфигурация](</ru/gateway/configuration>)
  * [Окружение](</ru/help/environment>)


Was this useful?YesNo

Open issue