---
title: Tài liệu tham khảo CLI
source_url: https://docs.openclaw.ai/vi/cli
scraped_at: 2026-05-25
---

`openclaw` là điểm vào CLI chính. Mỗi lệnh lõi có một trang tham chiếu riêng hoặc được ghi tài liệu cùng với lệnh mà nó là bí danh; mục lục này liệt kê các lệnh, cờ toàn cục, và quy tắc kiểu hiển thị đầu ra áp dụng trên toàn CLI.

Dùng các lệnh thiết lập theo mục đích:

  * `openclaw setup` tạo cấu hình nền tảng và workspace mà không đi qua toàn bộ luồng hướng dẫn onboarding.
  * `openclaw onboard` là đường dẫn chạy lần đầu được hướng dẫn đầy đủ cho Gateway, xác thực mô hình, workspace, kênh, Skills, và tình trạng hệ thống.
  * `openclaw configure` thay đổi các phần được nhắm mục tiêu của một thiết lập hiện có, chẳng hạn như xác thực mô hình, Gateway, kênh, Plugin, hoặc Skills.
  * `openclaw channels add` cấu hình tài khoản kênh sau khi nền tảng đã tồn tại; chạy không có cờ để thiết lập kênh theo hướng dẫn hoặc dùng các cờ riêng theo kênh cho script.


## Trang lệnh

Khu vực | Lệnh  
---|---  
Thiết lập và onboarding | [`crestodian`](</vi/cli/crestodian>) · [`setup`](</vi/cli/setup>) · [`onboard`](</vi/cli/onboard>) · [`configure`](</vi/cli/configure>) · [`config`](</vi/cli/config>) · [`completion`](</vi/cli/completion>) · [`doctor`](</vi/cli/doctor>) · [`dashboard`](</vi/cli/dashboard>)  
Đặt lại và gỡ cài đặt | [`backup`](</vi/cli/backup>) · [`reset`](</vi/cli/reset>) · [`uninstall`](</vi/cli/uninstall>) · [`update`](</vi/cli/update>)  
Nhắn tin và agent | [`message`](</vi/cli/message>) · [`agent`](</vi/cli/agent>) · [`agents`](</vi/cli/agents>) · [`acp`](</vi/cli/acp>) · [`mcp`](</vi/cli/mcp>)  
Tình trạng và phiên | [`status`](</vi/cli/status>) · [`health`](</vi/cli/health>) · [`sessions`](</vi/cli/sessions>)  
Gateway và nhật ký | [`gateway`](</vi/cli/gateway>) · [`logs`](</vi/cli/logs>) · [`system`](</vi/cli/system>)  
Mô hình và suy luận | [`models`](</vi/cli/models>) · [`infer`](</vi/cli/infer>) · `capability` (bí danh của [`infer`](</vi/cli/infer>)) · [`memory`](</vi/cli/memory>) · [`commitments`](</vi/cli/commitments>) · [`wiki`](</vi/cli/wiki>)  
Mạng và nút | [`directory`](</vi/cli/directory>) · [`nodes`](</vi/cli/nodes>) · [`devices`](</vi/cli/devices>) · [`node`](</vi/cli/node>)  
Runtime và sandbox | [`approvals`](</vi/cli/approvals>) · `exec-policy` (xem [`approvals`](</vi/cli/approvals>)) · [`sandbox`](</vi/cli/sandbox>) · [`tui`](</vi/cli/tui>) · `chat`/`terminal` (bí danh của [`tui --local`](</vi/cli/tui>)) · [`browser`](</vi/cli/browser>)  
Tự động hóa | [`cron`](</vi/cli/cron>) · [`tasks`](</vi/cli/tasks>) · [`hooks`](</vi/cli/hooks>) · [`webhooks`](</vi/cli/webhooks>)  
Khám phá và tài liệu | [`dns`](</vi/cli/dns>) · [`docs`](</vi/cli/docs>)  
Ghép nối và kênh | [`pairing`](</vi/cli/pairing>) · [`qr`](</vi/cli/qr>) · [`channels`](</vi/cli/channels>)  
Bảo mật và Plugin | [`security`](</vi/cli/security>) · [`secrets`](</vi/cli/secrets>) · [`skills`](</vi/cli/skills>) · [`plugins`](</vi/cli/plugins>) · [`proxy`](</vi/cli/proxy>)  
Bí danh cũ | [`daemon`](</vi/cli/daemon>) (dịch vụ Gateway) · [`clawbot`](</vi/cli/clawbot>) (namespace)  
Plugin (tùy chọn) | [`path`](</vi/cli/path>) · [`voicecall`](</vi/cli/voicecall>) (nếu đã cài đặt)  
  
## Cờ toàn cục

Cờ | Mục đích  
---|---  
`--dev` | Cô lập trạng thái dưới `~/.openclaw-dev` và dịch chuyển các cổng mặc định  
`--profile <name>` | Cô lập trạng thái dưới `~/.openclaw-<name>`  
`--container <name>` | Nhắm tới một container đã đặt tên để thực thi  
`--no-color` | Tắt màu ANSI (`NO_COLOR=1` cũng được tôn trọng)  
`--update` | Viết tắt cho [`openclaw update`](</vi/cli/update>) (chỉ với cài đặt từ nguồn)  
`-V`, `--version`, `-v` | In phiên bản và thoát  
  
## Chế độ đầu ra

  * Màu ANSI và chỉ báo tiến trình chỉ hiển thị trong các phiên TTY.
  * Siêu liên kết OSC-8 hiển thị dưới dạng liên kết có thể nhấp ở nơi được hỗ trợ; nếu không, CLI sẽ quay về URL thuần.
  * `--json` (và `--plain` ở nơi được hỗ trợ) tắt kiểu hiển thị để có đầu ra sạch.
  * Các lệnh chạy lâu hiển thị chỉ báo tiến trình (OSC 9;4 khi được hỗ trợ).


Nguồn sự thật của bảng màu: `src/terminal/palette.ts`.

## Cây lệnh

Full command tree CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugin có thể thêm các lệnh cấp cao nhất bổ sung (ví dụ `openclaw voicecall`).

## Lệnh slash trong chat

Tin nhắn chat hỗ trợ các lệnh `/...`. Xem [lệnh slash](</vi/tools/slash-commands>).

Điểm nổi bật:

  * `/status` — chẩn đoán nhanh.
  * `/trace` — các dòng trace/gỡ lỗi Plugin trong phạm vi phiên.
  * `/config` — thay đổi cấu hình được lưu bền vững.
  * `/debug` — ghi đè cấu hình chỉ trong runtime (bộ nhớ, không phải đĩa; yêu cầu `commands.debug: true`).


## Theo dõi mức sử dụng

`openclaw status --usage` và Control UI hiển thị mức sử dụng/hạn mức của nhà cung cấp khi có thông tin xác thực OAuth/API. Dữ liệu đến trực tiếp từ các endpoint mức sử dụng của nhà cung cấp và được chuẩn hóa thành `X% left`. Các nhà cung cấp có cửa sổ mức sử dụng hiện tại: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi, và [z.ai](<http://z.ai>).

Xem [Theo dõi mức sử dụng](</vi/concepts/usage-tracking>) để biết chi tiết.

## Liên quan

  * [Lệnh slash](</vi/tools/slash-commands>)
  * [Cấu hình](</vi/gateway/configuration>)
  * [Môi trường](</vi/help/environment>)


Was this useful?YesNo