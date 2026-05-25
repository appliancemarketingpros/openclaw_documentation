---
title: Tác nhân
source_url: https://docs.openclaw.ai/vi/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

Quản lý các agent biệt lập (không gian làm việc + xác thực + định tuyến).

Liên quan:

  * [Định tuyến đa agent](</vi/concepts/multi-agent>)
  * [Không gian làm việc của agent](</vi/concepts/agent-workspace>)
  * [Cấu hình Skills](</vi/tools/skills-config>): cấu hình khả năng hiển thị của skill.


## Ví dụ

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Liên kết định tuyến

Dùng liên kết định tuyến để ghim lưu lượng kênh đi vào với một agent cụ thể.

Nếu bạn cũng muốn các skill hiển thị khác nhau cho từng agent, hãy cấu hình `agents.defaults.skills` và `agents.list[].skills` trong `openclaw.json`. Xem [Cấu hình Skills](</vi/tools/skills-config>) và [Tham chiếu cấu hình](</vi/gateway/config-agents#agents-defaults-skills>).

Liệt kê liên kết:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

Thêm liên kết:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

Nếu bạn bỏ qua `accountId` (`--bind <channel>`), OpenClaw sẽ phân giải giá trị này từ mặc định của kênh và các hook thiết lập Plugin khi có sẵn.

Nếu bạn bỏ qua `--agent` cho `bind` hoặc `unbind`, OpenClaw sẽ nhắm tới agent mặc định hiện tại.

### Hành vi phạm vi liên kết

  * Liên kết không có `accountId` chỉ khớp với tài khoản mặc định của kênh.
  * `accountId: "*"` là phương án dự phòng trên toàn kênh (mọi tài khoản) và kém cụ thể hơn một liên kết tài khoản tường minh.
  * Nếu cùng agent đã có một liên kết kênh khớp mà không có `accountId`, và sau đó bạn liên kết với một `accountId` tường minh hoặc đã được phân giải, OpenClaw sẽ nâng cấp liên kết hiện có đó tại chỗ thay vì thêm một bản trùng lặp.


Ví dụ:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

Sau khi nâng cấp, định tuyến cho liên kết đó được giới hạn trong phạm vi `telegram:ops`. Nếu bạn cũng muốn định tuyến tài khoản mặc định, hãy thêm tường minh (ví dụ `--bind telegram:default`).

Gỡ liên kết:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` chấp nhận `--all` hoặc một hay nhiều giá trị `--bind`, không chấp nhận cả hai cùng lúc.

## Bề mặt lệnh

### `agents`

Chạy `openclaw agents` mà không có lệnh con tương đương với `openclaw agents list`.

### `agents list`

Tùy chọn:

  * `--json`
  * `--bindings`: bao gồm đầy đủ quy tắc định tuyến, không chỉ số lượng/tóm tắt theo từng agent


### `agents add [name]`

Tùy chọn:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (có thể lặp lại)
  * `--non-interactive`
  * `--json`


Ghi chú:

  * Truyền bất kỳ cờ thêm tường minh nào sẽ chuyển lệnh sang đường dẫn không tương tác.
  * Chế độ không tương tác yêu cầu cả tên agent và `--workspace`.
  * `main` được dành riêng và không thể dùng làm id agent mới.
  * Ở chế độ tương tác, việc gieo dữ liệu xác thực chỉ sao chép các hồ sơ tĩnh có tính di động (`api_key` và `token` tĩnh theo mặc định). Các hồ sơ OAuth có refresh-token vẫn chỉ có sẵn bằng cách kế thừa đọc xuyên qua từ kho agent `main` thực. Nếu agent mặc định đã cấu hình không phải là `main`, hãy đăng nhập riêng cho các hồ sơ OAuth trên agent mới.


### `agents bindings`

Tùy chọn:

  * `--agent <id>`
  * `--json`


### `agents bind`

Tùy chọn:

  * `--agent <id>` (mặc định là agent mặc định hiện tại)
  * `--bind <channel[:accountId]>` (có thể lặp lại)
  * `--json`


### `agents unbind`

Tùy chọn:

  * `--agent <id>` (mặc định là agent mặc định hiện tại)
  * `--bind <channel[:accountId]>` (có thể lặp lại)
  * `--all`
  * `--json`


### `agents delete <id>`

Tùy chọn:

  * `--force`
  * `--json`


Ghi chú:

  * Không thể xóa `main`.
  * Nếu không có `--force`, cần xác nhận tương tác.
  * Các thư mục không gian làm việc, trạng thái agent và bản ghi phiên được chuyển vào Thùng rác, không bị xóa cứng.
  * Khi có thể kết nối tới Gateway, thao tác xóa được gửi qua Gateway để việc dọn dẹp cấu hình và kho phiên dùng cùng bộ ghi với lưu lượng thời gian chạy. Nếu không thể kết nối tới Gateway, CLI sẽ dự phòng về đường dẫn cục bộ ngoại tuyến.
  * Nếu không gian làm việc của một agent khác là cùng đường dẫn, nằm bên trong không gian làm việc này, hoặc chứa không gian làm việc này, không gian làm việc sẽ được giữ lại và `--json` báo cáo `workspaceRetained`, `workspaceRetainedReason`, và `workspaceSharedWith`.


## Tệp định danh

Mỗi không gian làm việc của agent có thể bao gồm một `IDENTITY.md` ở gốc không gian làm việc:

  * Đường dẫn ví dụ: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` đọc từ gốc không gian làm việc (hoặc một `--identity-file` tường minh)


Đường dẫn avatar được phân giải tương đối với gốc không gian làm việc.

## Thiết lập định danh

`set-identity` ghi các trường vào `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (đường dẫn tương đối với không gian làm việc, URL http(s), hoặc URI dữ liệu)


Tùy chọn:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


Ghi chú:

  * Có thể dùng `--agent` hoặc `--workspace` để chọn agent đích.
  * Nếu bạn dựa vào `--workspace` và nhiều agent dùng chung không gian làm việc đó, lệnh sẽ thất bại và yêu cầu bạn truyền `--agent`.
  * Khi không cung cấp trường định danh tường minh nào, lệnh sẽ đọc dữ liệu định danh từ `IDENTITY.md`.


Tải từ `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

Ghi đè các trường một cách tường minh:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Mẫu cấu hình:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Định tuyến đa agent](</vi/concepts/multi-agent>)
  * [Không gian làm việc của agent](</vi/concepts/agent-workspace>)


Was this useful?YesNo