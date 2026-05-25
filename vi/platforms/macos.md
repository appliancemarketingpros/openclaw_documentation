---
title: Ứng dụng macOS
source_url: https://docs.openclaw.ai/vi/platforms/macos
scraped_at: 2026-05-25
---

Ứng dụng macOS là **ứng dụng đồng hành trên thanh menu** của OpenClaw. Ứng dụng sở hữu quyền, quản lý/gắn vào Gateway cục bộ (launchd hoặc thủ công), và cung cấp các năng lực macOS cho agent dưới dạng một Node.

## Chức năng

  * Hiển thị thông báo gốc và trạng thái trên thanh menu.
  * Sở hữu các lời nhắc TCC (Notifications, Accessibility, Screen Recording, Microphone, Speech Recognition, Automation/AppleScript).
  * Chạy hoặc kết nối với Gateway (cục bộ hoặc từ xa).
  * Cung cấp các công cụ chỉ có trên macOS (Canvas, Camera, Screen Recording, `system.run`).
  * Khởi động dịch vụ máy chủ Node cục bộ ở chế độ **từ xa** (launchd), và dừng dịch vụ đó ở chế độ **cục bộ**.
  * Tùy chọn lưu trữ **PeekabooBridge** cho tự động hóa UI.
  * Cài đặt CLI toàn cục (`openclaw`) theo yêu cầu qua npm, pnpm hoặc bun (ứng dụng ưu tiên npm, rồi pnpm, rồi bun; Node vẫn là runtime Gateway được khuyến nghị).


## Chế độ cục bộ và từ xa

  * **Cục bộ** (mặc định): ứng dụng gắn vào Gateway cục bộ đang chạy nếu có; nếu không, ứng dụng bật dịch vụ launchd qua `openclaw gateway install`.
  * **Từ xa** : ứng dụng kết nối tới Gateway qua SSH/Tailscale và không bao giờ khởi động tiến trình cục bộ. Ứng dụng khởi động **dịch vụ máy chủ Node** cục bộ để Gateway từ xa có thể truy cập máy Mac này. Ứng dụng không sinh Gateway dưới dạng tiến trình con. Khám phá Gateway hiện ưu tiên tên Tailscale MagicDNS hơn IP tailnet thô, nhờ đó ứng dụng Mac phục hồi đáng tin cậy hơn khi IP tailnet thay đổi.


## Điều khiển launchd

Ứng dụng quản lý một LaunchAgent theo người dùng có nhãn `ai.openclaw.gateway` (hoặc `ai.openclaw.<profile>` khi dùng `--profile`/`OPENCLAW_PROFILE`; `com.openclaw.*` cũ vẫn được dỡ tải).

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.gatewaylaunchctl bootout gui/$UID/ai.openclaw.gateway
[/code]

Thay nhãn bằng `ai.openclaw.<profile>` khi chạy một hồ sơ có tên.

Nếu LaunchAgent chưa được cài đặt, hãy bật nó từ ứng dụng hoặc chạy `openclaw gateway install`.

## Năng lực Node (mac)

Ứng dụng macOS tự trình bày như một Node. Các lệnh thường dùng:

  * Canvas: `canvas.present`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`, `canvas.a2ui.*`
  * Camera: `camera.snap`, `camera.clip`
  * Màn hình: `screen.snapshot`, `screen.record`
  * Hệ thống: `system.run`, `system.notify`


Node báo cáo một bản đồ `permissions` để agent có thể quyết định những gì được phép.

Dịch vụ Node + IPC ứng dụng:

  * Khi dịch vụ máy chủ Node headless đang chạy (chế độ từ xa), dịch vụ đó kết nối tới Gateway WS như một Node.
  * `system.run` thực thi trong ứng dụng macOS (ngữ cảnh UI/TCC) qua một socket Unix cục bộ; lời nhắc + đầu ra vẫn ở trong ứng dụng.


Sơ đồ (SCI):

CodeCopy code
[code]
    Gateway -> Node Service (WS)                 |  IPC (UDS + token + HMAC + TTL)                 v             Mac App (UI + TCC + system.run)
[/code]

## Phê duyệt thực thi (system.run)

`system.run` được kiểm soát bởi **Phê duyệt thực thi** trong ứng dụng macOS (Settings → Exec approvals). Bảo mật + hỏi + danh sách cho phép được lưu cục bộ trên máy Mac tại:

CodeCopy code
[code]
    ~/.openclaw/exec-approvals.json
[/code]

Ví dụ:

jsonCopy code
[code]
    {  "version": 1,  "defaults": {    "security": "deny",    "ask": "on-miss"  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "allowlist": [{ "pattern": "/opt/homebrew/bin/rg" }]    }  }}
[/code]

Ghi chú:

  * Các mục `allowlist` là mẫu glob cho đường dẫn nhị phân đã phân giải, hoặc tên lệnh trần cho các lệnh được gọi qua PATH.
  * Văn bản lệnh shell thô chứa cú pháp điều khiển hoặc mở rộng shell (`&&`, `||`, `;`, `|`, ```, `$`, `<`, `>`, `(`, `)`) được xử lý như một lần trượt danh sách cho phép và yêu cầu phê duyệt rõ ràng (hoặc đưa nhị phân shell vào danh sách cho phép).
  * Chọn "Luôn cho phép" trong lời nhắc sẽ thêm lệnh đó vào danh sách cho phép.
  * Các ghi đè môi trường của `system.run` được lọc (loại bỏ `PATH`, `DYLD_*`, `LD_*`, `NODE_OPTIONS`, `PYTHON*`, `PERL*`, `RUBYOPT`, `SHELLOPTS`, `PS4`) rồi được hợp nhất với môi trường của ứng dụng.
  * Với các trình bao bọc shell (`bash|sh|zsh ... -c/-lc`), các ghi đè môi trường theo phạm vi yêu cầu được rút gọn thành một danh sách cho phép nhỏ và rõ ràng (`TERM`, `LANG`, `LC_*`, `COLORTERM`, `NO_COLOR`, `FORCE_COLOR`).
  * Với các quyết định luôn cho phép trong chế độ danh sách cho phép, các trình bao bọc điều phối đã biết (`env`, `nice`, `nohup`, `stdbuf`, `timeout`) lưu bền vững đường dẫn thực thi bên trong thay vì đường dẫn trình bao bọc. Nếu việc gỡ bao bọc không an toàn, không có mục danh sách cho phép nào được tự động lưu bền vững.


## Liên kết sâu

Ứng dụng đăng ký lược đồ URL `openclaw://` cho các hành động cục bộ.

### `openclaw://agent`

Kích hoạt một yêu cầu Gateway `agent`. **OC_I18N_900004** Tham số truy vấn:

  * `message` (bắt buộc)
  * `sessionKey` (tùy chọn)
  * `thinking` (tùy chọn)
  * `deliver` / `to` / `channel` (tùy chọn)
  * `timeoutSeconds` (tùy chọn)
  * `key` (khóa chế độ không cần giám sát, tùy chọn)


An toàn:

  * Không có `key`, ứng dụng sẽ nhắc xác nhận.
  * Không có `key`, ứng dụng áp dụng giới hạn thông điệp ngắn cho lời nhắc xác nhận và bỏ qua `deliver` / `to` / `channel`.
  * Với `key` hợp lệ, lần chạy là không cần giám sát (dành cho tự động hóa cá nhân).


## Luồng thiết lập ban đầu (điển hình)

  1. Cài đặt và khởi chạy **OpenClaw.app**.
  2. Hoàn tất danh sách kiểm quyền (lời nhắc TCC).
  3. Đảm bảo chế độ **Cục bộ** đang hoạt động và Gateway đang chạy.
  4. Cài đặt CLI nếu bạn muốn truy cập qua terminal.


## Vị trí thư mục trạng thái (macOS)

Tránh đặt thư mục trạng thái OpenClaw của bạn trong iCloud hoặc các thư mục được đồng bộ đám mây khác. Các đường dẫn có đồng bộ hỗ trợ có thể thêm độ trễ và đôi khi gây ra các cuộc đua khóa tệp/đồng bộ cho phiên và thông tin xác thực.

Ưu tiên một đường dẫn trạng thái cục bộ không đồng bộ, chẳng hạn như: **OC_I18N_900005** Nếu `openclaw doctor` phát hiện trạng thái nằm dưới:

  * `~/Library/Mobile Documents/com~apple~CloudDocs/...`
  * `~/Library/CloudStorage/...`


nó sẽ cảnh báo và khuyến nghị chuyển về một đường dẫn cục bộ.

## Quy trình build và phát triển (gốc)

  * `cd apps/macos && swift build`
  * `swift run OpenClaw` (hoặc Xcode)
  * Đóng gói ứng dụng: `scripts/package-mac-app.sh`


## Gỡ lỗi kết nối Gateway (CLI macOS)

Dùng CLI gỡ lỗi để thực hiện cùng cơ chế bắt tay Gateway WebSocket và logic khám phá mà ứng dụng macOS dùng, mà không cần khởi chạy ứng dụng. **OC_I18N_900006** Tùy chọn kết nối:

  * `--url <ws://host:port>`: ghi đè cấu hình
  * `--mode <local|remote>`: phân giải từ cấu hình (mặc định: cấu hình hoặc cục bộ)
  * `--probe`: buộc kiểm tra sức khỏe mới
  * `--timeout <ms>`: thời gian chờ yêu cầu (mặc định: `15000`)
  * `--json`: đầu ra có cấu trúc để so sánh khác biệt


Tùy chọn khám phá:

  * `--include-local`: bao gồm các gateway vốn sẽ bị lọc là "cục bộ"
  * `--timeout <ms>`: cửa sổ khám phá tổng thể (mặc định: `2000`)
  * `--json`: đầu ra có cấu trúc để so sánh khác biệt


## Hệ thống kết nối từ xa (đường hầm SSH)

Khi ứng dụng macOS chạy ở chế độ **Từ xa** , nó mở một đường hầm SSH để các thành phần UI cục bộ có thể nói chuyện với Gateway từ xa như thể Gateway đó nằm trên localhost.

### Đường hầm điều khiển (cổng Gateway WebSocket)

  * **Mục đích:** kiểm tra sức khỏe, trạng thái, Web Chat, cấu hình và các lệnh gọi control-plane khác.
  * **Cổng cục bộ:** cổng Gateway (mặc định `18789`), luôn ổn định.
  * **Cổng từ xa:** cùng cổng Gateway trên máy chủ từ xa.
  * **Hành vi:** không có cổng cục bộ ngẫu nhiên; ứng dụng tái sử dụng một đường hầm khỏe mạnh hiện có hoặc khởi động lại nếu cần.
  * **Dạng SSH:** `ssh -N -L <local>:127.0.0.1:<remote>` với BatchMode + ExitOnForwardFailure + tùy chọn keepalive.
  * **Báo cáo IP:** đường hầm SSH dùng loopback, nên gateway sẽ thấy IP Node là `127.0.0.1`. Dùng phương thức vận chuyển **Direct (ws/wss)** nếu bạn muốn IP client thực xuất hiện (xem [truy cập từ xa macOS](</vi/platforms/mac/remote>)).


Để biết các bước thiết lập, xem [truy cập từ xa macOS](</vi/platforms/mac/remote>). Để biết chi tiết giao thức, xem [Giao thức Gateway](</vi/gateway/protocol>).

## Tài liệu liên quan

  * [Runbook Gateway](</vi/gateway>)
  * [Gateway (macOS)](</vi/platforms/mac/bundled-gateway>)
  * [Quyền macOS](</vi/platforms/mac/permissions>)
  * [Canvas](</vi/platforms/mac/canvas>)


Was this useful?YesNo