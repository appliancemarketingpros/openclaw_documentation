---
title: ข้อมูลอ้างอิง CLI
source_url: https://docs.openclaw.ai/th/cli
scraped_at: 2026-05-25
---

`openclaw` คือจุดเข้าใช้งานหลักของ CLI คำสั่งหลักแต่ละคำสั่งมีหน้าคู่มืออ้างอิงเฉพาะ หรือถูกจัดทำเอกสารไว้ร่วมกับคำสั่งที่เป็น alias ดัชนีนี้แสดงรายการคำสั่ง flag ส่วนกลาง และกฎการจัดรูปแบบเอาต์พุตที่ใช้ทั่วทั้ง CLI

ใช้คำสั่งตั้งค่าตามเจตนา:

  * `openclaw setup` สร้าง config และ workspace พื้นฐานโดยไม่ดำเนินผ่านขั้นตอน onboarding แบบมีคำแนะนำเต็มรูปแบบ
  * `openclaw onboard` คือเส้นทาง first-run แบบมีคำแนะนำเต็มรูปแบบสำหรับ gateway, การยืนยันตัวตนโมเดล, workspace, channels, skills และ health
  * `openclaw configure` เปลี่ยนส่วนที่กำหนดเป้าหมายไว้ของการตั้งค่าที่มีอยู่ เช่น การยืนยันตัวตนโมเดล, gateway, channels, plugins หรือ skills
  * `openclaw channels add` กำหนดค่าบัญชี channel หลังจากมีพื้นฐานแล้ว; รันโดยไม่มี flag สำหรับการตั้งค่า channel แบบมีคำแนะนำ หรือใช้ flag เฉพาะ channel สำหรับสคริปต์


## หน้าคำสั่ง

พื้นที่ | คำสั่ง  
---|---  
การตั้งค่าและ onboarding | [`crestodian`](</th/cli/crestodian>) · [`setup`](</th/cli/setup>) · [`onboard`](</th/cli/onboard>) · [`configure`](</th/cli/configure>) · [`config`](</th/cli/config>) · [`completion`](</th/cli/completion>) · [`doctor`](</th/cli/doctor>) · [`dashboard`](</th/cli/dashboard>)  
การรีเซ็ตและถอนการติดตั้ง | [`backup`](</th/cli/backup>) · [`reset`](</th/cli/reset>) · [`uninstall`](</th/cli/uninstall>) · [`update`](</th/cli/update>)  
การส่งข้อความและ agents | [`message`](</th/cli/message>) · [`agent`](</th/cli/agent>) · [`agents`](</th/cli/agents>) · [`acp`](</th/cli/acp>) · [`mcp`](</th/cli/mcp>)  
สถานะความพร้อมและ sessions | [`status`](</th/cli/status>) · [`health`](</th/cli/health>) · [`sessions`](</th/cli/sessions>)  
Gateway และ logs | [`gateway`](</th/cli/gateway>) · [`logs`](</th/cli/logs>) · [`system`](</th/cli/system>)  
โมเดลและ inference | [`models`](</th/cli/models>) · [`infer`](</th/cli/infer>) · `capability` (alias สำหรับ [`infer`](</th/cli/infer>)) · [`memory`](</th/cli/memory>) · [`commitments`](</th/cli/commitments>) · [`wiki`](</th/cli/wiki>)  
เครือข่ายและ nodes | [`directory`](</th/cli/directory>) · [`nodes`](</th/cli/nodes>) · [`devices`](</th/cli/devices>) · [`node`](</th/cli/node>)  
Runtime และ sandbox | [`approvals`](</th/cli/approvals>) · `exec-policy` (ดู [`approvals`](</th/cli/approvals>)) · [`sandbox`](</th/cli/sandbox>) · [`tui`](</th/cli/tui>) · `chat`/`terminal` (alias สำหรับ [`tui --local`](</th/cli/tui>)) · [`browser`](</th/cli/browser>)  
Automation | [`cron`](</th/cli/cron>) · [`tasks`](</th/cli/tasks>) · [`hooks`](</th/cli/hooks>) · [`webhooks`](</th/cli/webhooks>)  
Discovery และเอกสาร | [`dns`](</th/cli/dns>) · [`docs`](</th/cli/docs>)  
Pairing และ channels | [`pairing`](</th/cli/pairing>) · [`qr`](</th/cli/qr>) · [`channels`](</th/cli/channels>)  
ความปลอดภัยและ plugins | [`security`](</th/cli/security>) · [`secrets`](</th/cli/secrets>) · [`skills`](</th/cli/skills>) · [`plugins`](</th/cli/plugins>) · [`proxy`](</th/cli/proxy>)  
Alias เดิม | [`daemon`](</th/cli/daemon>) (บริการ gateway) · [`clawbot`](</th/cli/clawbot>) (namespace)  
Plugins (ไม่บังคับ) | [`path`](</th/cli/path>) · [`voicecall`](</th/cli/voicecall>) (หากติดตั้งแล้ว)  
  
## Flag ส่วนกลาง

Flag | วัตถุประสงค์  
---|---  
`--dev` | แยกสถานะไว้ใต้ `~/.openclaw-dev` และเลื่อนพอร์ตเริ่มต้น  
`--profile <name>` | แยกสถานะไว้ใต้ `~/.openclaw-<name>`  
`--container <name>` | กำหนดเป้าหมาย container ที่มีชื่อสำหรับการดำเนินการ  
`--no-color` | ปิดใช้งานสี ANSI (`NO_COLOR=1` จะถูกเคารพด้วย)  
`--update` | รูปย่อของ [`openclaw update`](</th/cli/update>) (เฉพาะการติดตั้งจาก source เท่านั้น)  
`-V`, `--version`, `-v` | พิมพ์เวอร์ชันแล้วออก  
  
## โหมดเอาต์พุต

  * สี ANSI และตัวบ่งชี้ความคืบหน้าจะแสดงผลเฉพาะใน session แบบ TTY
  * ไฮเปอร์ลิงก์ OSC-8 จะแสดงผลเป็นลิงก์ที่คลิกได้ในที่ที่รองรับ มิฉะนั้น CLI จะถอยกลับไปใช้ URL แบบข้อความธรรมดา
  * `--json` (และ `--plain` ในที่ที่รองรับ) จะปิดการจัดรูปแบบเพื่อให้ได้เอาต์พุตที่สะอาด
  * คำสั่งที่รันนานจะแสดงตัวบ่งชี้ความคืบหน้า (OSC 9;4 เมื่อรองรับ)


แหล่งข้อมูลจริงของพาเลต: `src/terminal/palette.ts`

## ผังคำสั่ง

ผังคำสั่งแบบเต็ม CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins สามารถเพิ่มคำสั่งระดับบนสุดเพิ่มเติมได้ (ตัวอย่างเช่น `openclaw voicecall`)

## คำสั่ง slash ในแชต

ข้อความแชตรองรับคำสั่ง `/...` ดู [คำสั่ง slash](</th/tools/slash-commands>)

ไฮไลต์:

  * `/status` — การวินิจฉัยอย่างรวดเร็ว
  * `/trace` — บรรทัด trace/debug ของ plugin ที่จำกัดตาม session
  * `/config` — การเปลี่ยนแปลง config ที่บันทึกถาวร
  * `/debug` — การ override config เฉพาะ runtime (ในหน่วยความจำ ไม่ใช่บนดิสก์; ต้องใช้ `commands.debug: true`)


## การติดตามการใช้งาน

`openclaw status --usage` และ Control UI แสดงการใช้งาน/โควตาของ provider เมื่อมีข้อมูลประจำตัว OAuth/API ข้อมูลมาจาก endpoint การใช้งานของ provider โดยตรงและถูกทำให้เป็นมาตรฐานเป็น `X% left` Provider ที่มีหน้าต่างการใช้งานปัจจุบัน: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi และ [z.ai](<http://z.ai>)

ดูรายละเอียดที่ [การติดตามการใช้งาน](</th/concepts/usage-tracking>)

## ที่เกี่ยวข้อง

  * [คำสั่ง slash](</th/tools/slash-commands>)
  * [การกำหนดค่า](</th/gateway/configuration>)
  * [Environment](</th/help/environment>)


Was this useful?YesNo