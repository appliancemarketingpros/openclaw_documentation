---
title: Không gian làm việc của tác tử
source_url: https://docs.openclaw.ai/vi/concepts/agent-workspace
scraped_at: 2026-05-25
---

Không gian làm việc là nhà của agent. Đây là thư mục làm việc duy nhất được dùng cho công cụ tệp và ngữ cảnh không gian làm việc. Hãy giữ riêng tư và xem nó như bộ nhớ.

Điều này tách biệt với `~/.openclaw/`, nơi lưu cấu hình, thông tin xác thực và phiên.

## Vị trí mặc định

  * Mặc định: `~/.openclaw/workspace`
  * Nếu `OPENCLAW_PROFILE` được đặt và không phải `"default"`, mặc định trở thành `~/.openclaw/workspace-<profile>`.
  * Ghi đè trong `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure`, hoặc `openclaw setup` sẽ tạo không gian làm việc và gieo các tệp khởi tạo nếu chúng bị thiếu.

Nếu bạn đã tự quản lý các tệp không gian làm việc, bạn có thể tắt việc tạo tệp khởi tạo:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Thư mục không gian làm việc bổ sung

Các bản cài đặt cũ hơn có thể đã tạo `~/openclaw`. Việc giữ nhiều thư mục không gian làm việc có thể gây nhầm lẫn về xác thực hoặc trôi lệch trạng thái, vì mỗi lần chỉ có một không gian làm việc đang hoạt động.

## Bản đồ tệp không gian làm việc

Đây là các tệp chuẩn mà OpenClaw mong đợi bên trong không gian làm việc:

AGENTS.md - operating instructions

Hướng dẫn vận hành cho agent và cách agent nên dùng bộ nhớ. Được tải khi bắt đầu mọi phiên. Đây là nơi phù hợp cho quy tắc, ưu tiên và chi tiết "cách hành xử".

SOUL.md - persona and tone

Chân dung, giọng điệu và ranh giới. Được tải trong mọi phiên. Hướng dẫn: [Hướng dẫn tính cách SOUL.md](</vi/concepts/soul>).

USER.md - who the user is

Người dùng là ai và nên xưng hô với họ như thế nào. Được tải trong mọi phiên.

IDENTITY.md - name, vibe, emoji

Tên, phong thái và emoji của agent. Được tạo/cập nhật trong nghi thức khởi tạo.

TOOLS.md - local tool conventions

Ghi chú về công cụ cục bộ và quy ước của bạn. Không kiểm soát tính khả dụng của công cụ; đây chỉ là hướng dẫn.

HEARTBEAT.md - heartbeat checklist

Danh sách kiểm tra nhỏ tùy chọn cho các lần chạy Heartbeat. Giữ ngắn để tránh tốn token.

BOOT.md - startup checklist

Danh sách kiểm tra khởi động tùy chọn được chạy tự động khi Gateway khởi động lại (khi [hook nội bộ](</vi/automation/hooks>) được bật). Giữ ngắn; dùng công cụ tin nhắn để gửi ra ngoài.

BOOTSTRAP.md - first-run ritual

Nghi thức chạy lần đầu một lần duy nhất. Chỉ được tạo cho một không gian làm việc hoàn toàn mới. Xóa nó sau khi nghi thức hoàn tất.

memory/YYYY-MM-DD.md - daily memory log

Nhật ký bộ nhớ hằng ngày (mỗi ngày một tệp). Nên đọc hôm nay + hôm qua khi bắt đầu phiên.

MEMORY.md - curated long-term memory (optional)

Bộ nhớ dài hạn được tuyển chọn: dữ kiện bền vững, tùy chọn, quyết định và tóm tắt ngắn. Giữ nhật ký chi tiết trong `memory/YYYY-MM-DD.md` để công cụ bộ nhớ có thể truy xuất theo yêu cầu mà không đưa chúng vào mọi prompt. Chỉ tải `MEMORY.md` trong phiên chính, riêng tư (không phải ngữ cảnh chia sẻ/nhóm). Xem [Bộ nhớ](</vi/concepts/memory>) để biết quy trình và việc xả bộ nhớ tự động.

skills/ - workspace skills (optional)

Skills dành riêng cho không gian làm việc. Vị trí Skills có độ ưu tiên cao nhất cho không gian làm việc đó. Ghi đè Skills agent của dự án, Skills agent cá nhân, Skills được quản lý, Skills đi kèm và `skills.load.extraDirs` khi trùng tên.

canvas/ - Canvas UI files (optional)

Các tệp giao diện Canvas cho hiển thị node (ví dụ `canvas/index.html`).

## Những gì KHÔNG nằm trong không gian làm việc

Những mục này nằm dưới `~/.openclaw/` và KHÔNG nên được commit vào repo không gian làm việc:

  * `~/.openclaw/openclaw.json` (cấu hình)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (hồ sơ xác thực mô hình: OAuth + khóa API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (tài khoản runtime Codex theo từng agent, cấu hình, Skills, Plugin và trạng thái luồng native)
  * `~/.openclaw/credentials/` (trạng thái kênh/nhà cung cấp cộng với dữ liệu nhập OAuth cũ)
  * `~/.openclaw/agents/<agentId>/sessions/` (bản ghi phiên + siêu dữ liệu)
  * `~/.openclaw/skills/` (Skills được quản lý)


Nếu bạn cần di chuyển phiên hoặc cấu hình, hãy sao chép chúng riêng và giữ chúng ngoài quản lý phiên bản.

## Sao lưu Git (khuyến nghị, riêng tư)

Hãy xem không gian làm việc như bộ nhớ riêng tư. Đặt nó trong một repo git **riêng tư** để có bản sao lưu và có thể khôi phục.

Chạy các bước này trên máy nơi Gateway chạy (đó là nơi không gian làm việc tồn tại).

* ### Initialize the repo

Nếu đã cài git, các không gian làm việc hoàn toàn mới sẽ được khởi tạo tự động. Nếu không gian làm việc này chưa phải repo, hãy chạy:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Add a private remote

### GitHub web UI

  1. Tạo một kho lưu trữ **riêng tư** mới trên GitHub.
  2. Không khởi tạo với README (tránh xung đột merge).
  3. Sao chép URL remote HTTPS.
  4. Thêm remote và push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. Tạo một kho lưu trữ **riêng tư** mới trên GitLab.
  2. Không khởi tạo với README (tránh xung đột merge).
  3. Sao chép URL remote HTTPS.
  4. Thêm remote và push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Ongoing updates

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Không commit bí mật

Mẫu `.gitignore` khởi đầu được đề xuất:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Di chuyển không gian làm việc sang máy mới

* ### Clone the repo

Clone repo vào đường dẫn mong muốn (mặc định `~/.openclaw/workspace`).

* ### Update config

Đặt `agents.defaults.workspace` thành đường dẫn đó trong `~/.openclaw/openclaw.json`.

* ### Seed missing files

Chạy `openclaw setup --workspace <path>` để gieo bất kỳ tệp nào bị thiếu.

* ### Copy sessions (optional)

Nếu bạn cần các phiên, hãy sao chép riêng `~/.openclaw/agents/<agentId>/sessions/` từ máy cũ.

## Ghi chú nâng cao

  * Định tuyến đa agent có thể dùng các không gian làm việc khác nhau cho từng agent. Xem [Định tuyến kênh](</vi/channels/channel-routing>) để biết cấu hình định tuyến.
  * Nếu `agents.defaults.sandbox` được bật, các phiên không phải phiên chính có thể dùng không gian làm việc sandbox theo từng phiên dưới `agents.defaults.sandbox.workspaceRoot`.


## Liên quan

  * [Heartbeat](</vi/gateway/heartbeat>) \- tệp không gian làm việc [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</vi/gateway/sandboxing>) \- truy cập không gian làm việc trong môi trường sandbox
  * [Phiên](</vi/concepts/session>) \- đường dẫn lưu trữ phiên
  * [Lệnh thường trực](</vi/automation/standing-orders>) \- hướng dẫn liên tục trong các tệp không gian làm việc


Was this useful?YesNo