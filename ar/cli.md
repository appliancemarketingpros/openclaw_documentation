---
title: مرجع CLI
source_url: https://docs.openclaw.ai/ar/cli
scraped_at: 2026-05-25
---

`openclaw` هو نقطة الدخول الرئيسية لـ CLI. يحتوي كل أمر أساسي إما على صفحة مرجعية مخصصة أو يتم توثيقه مع الأمر الذي يكون اسمًا مستعارًا له؛ يسرد هذا الفهرس الأوامر، والأعلام العامة، وقواعد تنسيق الإخراج التي تنطبق عبر CLI.

استخدم أوامر الإعداد حسب الغرض:

  * ينشئ `openclaw setup` التكوين الأساسي ومساحة العمل دون المرور عبر مسار الإعداد الإرشادي الكامل.
  * يُعد `openclaw onboard` مسار التشغيل الأول الإرشادي الكامل لـ Gateway، ومصادقة النموذج، ومساحة العمل، والقنوات، وSkills، والصحة.
  * يغيّر `openclaw configure` أجزاء مستهدفة من إعداد موجود، مثل مصادقة النموذج، وGateway، والقنوات، وPlugin، أو Skills.
  * يكوّن `openclaw channels add` حسابات القنوات بعد وجود الأساس؛ شغّله دون أعلام لإعداد القنوات إرشاديًا أو مع أعلام خاصة بالقناة للسكربتات.


## صفحات الأوامر

المجال | الأوامر  
---|---  
الإعداد والتهيئة الإرشادية | [`crestodian`](</ar/cli/crestodian>) · [`setup`](</ar/cli/setup>) · [`onboard`](</ar/cli/onboard>) · [`configure`](</ar/cli/configure>) · [`config`](</ar/cli/config>) · [`completion`](</ar/cli/completion>) · [`doctor`](</ar/cli/doctor>) · [`dashboard`](</ar/cli/dashboard>)  
إعادة الضبط وإلغاء التثبيت | [`backup`](</ar/cli/backup>) · [`reset`](</ar/cli/reset>) · [`uninstall`](</ar/cli/uninstall>) · [`update`](</ar/cli/update>)  
المراسلة والوكلاء | [`message`](</ar/cli/message>) · [`agent`](</ar/cli/agent>) · [`agents`](</ar/cli/agents>) · [`acp`](</ar/cli/acp>) · [`mcp`](</ar/cli/mcp>)  
الصحة والجلسات | [`status`](</ar/cli/status>) · [`health`](</ar/cli/health>) · [`sessions`](</ar/cli/sessions>)  
Gateway والسجلات | [`gateway`](</ar/cli/gateway>) · [`logs`](</ar/cli/logs>) · [`system`](</ar/cli/system>)  
النماذج والاستدلال | [`models`](</ar/cli/models>) · [`infer`](</ar/cli/infer>) · `capability` (اسم مستعار لـ [`infer`](</ar/cli/infer>)) · [`memory`](</ar/cli/memory>) · [`commitments`](</ar/cli/commitments>) · [`wiki`](</ar/cli/wiki>)  
الشبكة والعُقد | [`directory`](</ar/cli/directory>) · [`nodes`](</ar/cli/nodes>) · [`devices`](</ar/cli/devices>) · [`node`](</ar/cli/node>)  
وقت التشغيل وبيئة العزل | [`approvals`](</ar/cli/approvals>) · `exec-policy` (انظر [`approvals`](</ar/cli/approvals>)) · [`sandbox`](</ar/cli/sandbox>) · [`tui`](</ar/cli/tui>) · `chat`/`terminal` (أسماء مستعارة لـ [`tui --local`](</ar/cli/tui>)) · [`browser`](</ar/cli/browser>)  
الأتمتة | [`cron`](</ar/cli/cron>) · [`tasks`](</ar/cli/tasks>) · [`hooks`](</ar/cli/hooks>) · [`webhooks`](</ar/cli/webhooks>)  
الاكتشاف والوثائق | [`dns`](</ar/cli/dns>) · [`docs`](</ar/cli/docs>)  
الاقتران والقنوات | [`pairing`](</ar/cli/pairing>) · [`qr`](</ar/cli/qr>) · [`channels`](</ar/cli/channels>)  
الأمان وPlugin | [`security`](</ar/cli/security>) · [`secrets`](</ar/cli/secrets>) · [`skills`](</ar/cli/skills>) · [`plugins`](</ar/cli/plugins>) · [`proxy`](</ar/cli/proxy>)  
الأسماء المستعارة القديمة | [`daemon`](</ar/cli/daemon>) (خدمة Gateway) · [`clawbot`](</ar/cli/clawbot>) (نطاق أسماء)  
Plugin (اختياري) | [`path`](</ar/cli/path>) · [`voicecall`](</ar/cli/voicecall>) (إذا كان مثبتًا)  
  
## الأعلام العامة

العلم | الغرض  
---|---  
`--dev` | يعزل الحالة ضمن `~/.openclaw-dev` ويغيّر المنافذ الافتراضية  
`--profile <name>` | يعزل الحالة ضمن `~/.openclaw-<name>`  
`--container <name>` | يستهدف حاوية مسماة للتنفيذ  
`--no-color` | يعطّل ألوان ANSI (يتم احترام `NO_COLOR=1` أيضًا)  
`--update` | اختصار لـ [`openclaw update`](</ar/cli/update>) (لتثبيتات المصدر فقط)  
`-V`, `--version`, `-v` | يطبع الإصدار ويخرج  
  
## أوضاع الإخراج

  * لا تُعرض ألوان ANSI ومؤشرات التقدم إلا في جلسات TTY.
  * تُعرض الروابط التشعبية OSC-8 كروابط قابلة للنقر حيثما كان ذلك مدعومًا؛ وإلا يعود CLI إلى عناوين URL عادية.
  * يعطّل `--json` (و`--plain` حيثما كان مدعومًا) التنسيق للحصول على إخراج نظيف.
  * تعرض الأوامر طويلة التشغيل مؤشر تقدم (OSC 9;4 عند دعمه).


مصدر الحقيقة للوحة الألوان: `src/terminal/palette.ts`.

## شجرة الأوامر

شجرة الأوامر الكاملة CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

يمكن أن تضيف Plugin أوامر علوية إضافية (على سبيل المثال `openclaw voicecall`).

## أوامر الشرطة المائلة في الدردشة

تدعم رسائل الدردشة أوامر `/...`. راجع [أوامر الشرطة المائلة](</ar/tools/slash-commands>).

أبرزها:

  * `/status` — تشخيصات سريعة.
  * `/trace` — أسطر تتبع/تصحيح أخطاء Plugin ضمن نطاق الجلسة.
  * `/config` — تغييرات تكوين محفوظة.
  * `/debug` — تجاوزات تكوين لوقت التشغيل فقط (في الذاكرة، لا على القرص؛ يتطلب `commands.debug: true`).


## تتبع الاستخدام

يعرض `openclaw status --usage` وواجهة التحكم استخدام/حصة المزوّد عندما تتوفر بيانات اعتماد OAuth/API. تأتي البيانات مباشرة من نقاط نهاية استخدام المزوّد وتتم تسويتها إلى `X% left`. المزوّدون ذوو نوافذ الاستخدام الحالية: Anthropic، GitHub Copilot، Gemini CLI، OpenAI Codex، MiniMax، Xiaomi، [وz.ai](<http://xn--z-uoc.ai>).

راجع [تتبع الاستخدام](</ar/concepts/usage-tracking>) للتفاصيل.

## ذات صلة

  * [أوامر الشرطة المائلة](</ar/tools/slash-commands>)
  * [التكوين](</ar/gateway/configuration>)
  * [البيئة](</ar/help/environment>)


Was this useful?YesNo