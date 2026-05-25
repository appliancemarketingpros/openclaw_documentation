---
title: Thiết lập
source_url: https://docs.openclaw.ai/vi/start/setup
scraped_at: 2026-05-25
---

## Tóm tắt nhanh

Chọn quy trình thiết lập dựa trên tần suất bạn muốn cập nhật và việc bạn có muốn tự chạy Gateway hay không:

  * **Tùy chỉnh nằm ngoài repo:** giữ cấu hình và workspace của bạn trong `~/.openclaw/openclaw.json` và `~/.openclaw/workspace/` để các bản cập nhật repo không chạm vào chúng.
  * **Quy trình ổn định (khuyến nghị cho đa số người dùng):** cài đặt ứng dụng macOS và để ứng dụng chạy Gateway đi kèm.
  * **Quy trình bản mới nhất (dev):** tự chạy Gateway qua `pnpm gateway:watch`, rồi để ứng dụng macOS kết nối ở chế độ Cục bộ.


## Điều kiện tiên quyết (từ mã nguồn)

  * Khuyến nghị Node 24 (Node 22 LTS, hiện là `22.16+`, vẫn được hỗ trợ)
  * Bắt buộc có `pnpm` cho các checkout từ mã nguồn. OpenClaw tải các plugins đi kèm từ các gói pnpm workspace `extensions/*` ở chế độ dev, vì vậy `npm install` ở root không chuẩn bị đầy đủ cây mã nguồn.
  * Docker (tùy chọn; chỉ dùng cho thiết lập/e2e trong container - xem [Docker](</vi/install/docker>))


## Chiến lược tùy chỉnh (để cập nhật không gây rắc rối)

Nếu bạn muốn "100% tùy chỉnh theo mình" _và_ dễ cập nhật, hãy giữ phần tùy chỉnh trong:

  * **Cấu hình:** `~/.openclaw/openclaw.json` (JSON/kiểu JSON5)
  * **Workspace:** `~/.openclaw/workspace` (skills, prompts, memories; hãy biến nó thành repo git riêng tư)


Bootstrap một lần:

bashCopy code
[code]
    openclaw setup
[/code]

Từ bên trong repo này, dùng mục nhập CLI cục bộ:

bashCopy code
[code]
    openclaw setup
[/code]

Nếu bạn chưa có bản cài đặt toàn cục, hãy chạy qua `pnpm openclaw setup`.

## Chạy Gateway từ repo này

Sau `pnpm build`, bạn có thể chạy trực tiếp CLI đã đóng gói:

bashCopy code
[code]
    node openclaw.mjs gateway --port 18789 --verbose
[/code]

## Quy trình ổn định (ứng dụng macOS trước)

  1. Cài đặt + khởi chạy **OpenClaw.app** (thanh menu).
  2. Hoàn tất checklist onboarding/quyền (các lời nhắc TCC).
  3. Đảm bảo Gateway là **Cục bộ** và đang chạy (ứng dụng quản lý việc này).
  4. Liên kết các bề mặt (ví dụ: WhatsApp):

bashCopy code
[code]
    openclaw channels login
[/code]

  5. Kiểm tra nhanh:

bashCopy code
[code]
    openclaw health
[/code]

Nếu onboarding không khả dụng trong bản build của bạn:

  * Chạy `openclaw setup`, rồi `openclaw channels login`, rồi khởi động Gateway thủ công (`openclaw gateway`).


## Quy trình bản mới nhất (Gateway trong terminal)

Mục tiêu: làm việc trên TypeScript Gateway, có hot reload, giữ UI ứng dụng macOS được kết nối.

### 0) (Tùy chọn) Chạy cả ứng dụng macOS từ mã nguồn

Nếu bạn cũng muốn ứng dụng macOS ở bản mới nhất:

bashCopy code
[code]
    ./scripts/restart-mac.sh
[/code]

### 1) Khởi động dev Gateway

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

`gateway:watch` khởi động hoặc khởi động lại tiến trình theo dõi Gateway trong một phiên tmux có tên và tự động attach từ các terminal tương tác. Shell không tương tác sẽ vẫn detached và in `tmux attach -t openclaw-gateway-watch-main`; dùng `OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch` để giữ một lần chạy tương tác ở trạng thái detached, hoặc `pnpm gateway:watch:raw` cho chế độ theo dõi foreground. Watcher tải lại khi có thay đổi liên quan đến mã nguồn, cấu hình và metadata của plugin đi kèm. Nếu Gateway đang được theo dõi thoát trong lúc khởi động, `gateway:watch` sẽ chạy `openclaw doctor --fix --non-interactive` một lần rồi thử lại; đặt `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0` để tắt lượt sửa chữa chỉ dành cho dev đó. `pnpm openclaw setup` là bước khởi tạo cấu hình/workspace cục bộ một lần cho một checkout mới. `pnpm gateway:watch` không build lại `dist/control-ui`, vì vậy hãy chạy lại `pnpm ui:build` sau các thay đổi trong `ui/` hoặc dùng `pnpm ui:dev` khi phát triển Control UI.

### 2) Trỏ ứng dụng macOS tới Gateway đang chạy của bạn

Trong **OpenClaw.app** :

  * Chế độ kết nối: **Cục bộ** Ứng dụng sẽ attach vào gateway đang chạy trên cổng đã cấu hình.


### 3) Xác minh

  * Trạng thái Gateway trong ứng dụng nên hiển thị **"Đang dùng gateway hiện có …"**
  * Hoặc qua CLI:

bashCopy code
[code]
    openclaw health
[/code]

### Các lỗi thường gặp

  * **Sai cổng:** Gateway WS mặc định là `ws://127.0.0.1:18789`; giữ ứng dụng + CLI trên cùng một cổng.
  * **Nơi lưu trạng thái:**
    * Trạng thái channel/provider: `~/.openclaw/credentials/`
    * Hồ sơ xác thực model: `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
    * Phiên: `~/.openclaw/agents/<agentId>/sessions/`
    * Nhật ký: `/tmp/openclaw/`


## Bản đồ lưu trữ thông tin xác thực

Dùng phần này khi gỡ lỗi xác thực hoặc quyết định cần sao lưu gì:

  * **WhatsApp** : `~/.openclaw/credentials/whatsapp/<accountId>/creds.json`
  * **Telegram bot token** : config/env hoặc `channels.telegram.tokenFile` (chỉ file thông thường; symlink bị từ chối)
  * **Discord bot token** : config/env hoặc SecretRef (nhà cung cấp env/file/exec)
  * **Slack tokens** : config/env (`channels.slack.*`)
  * **Danh sách cho phép ghép nối** : 
    * `~/.openclaw/credentials/<channel>-allowFrom.json` (tài khoản mặc định)
    * `~/.openclaw/credentials/<channel>-<accountId>-allowFrom.json` (tài khoản không mặc định)
  * **Hồ sơ xác thực model** : `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * **Payload secrets dựa trên file (tùy chọn)** : `~/.openclaw/secrets.json`
  * **Nhập OAuth cũ** : `~/.openclaw/credentials/oauth.json` Chi tiết hơn: [Bảo mật](</vi/gateway/security#credential-storage-map>).


## Cập nhật (mà không phá hỏng thiết lập của bạn)

  * Giữ `~/.openclaw/workspace` và `~/.openclaw/` là "đồ của bạn"; đừng đưa prompts/cấu hình cá nhân vào repo `openclaw`.
  * Cập nhật mã nguồn: `git pull` \+ `pnpm install` \+ tiếp tục dùng `pnpm gateway:watch`.


## Linux (systemd user service)

Các bản cài đặt Linux dùng systemd **user** service. Theo mặc định, systemd dừng các user services khi đăng xuất/nhàn rỗi, làm Gateway bị tắt. Onboarding cố gắng bật lingering cho bạn (có thể nhắc sudo). Nếu nó vẫn đang tắt, hãy chạy:

bashCopy code
[code]
    sudo loginctl enable-linger $USER
[/code]

Đối với máy chủ luôn bật hoặc nhiều người dùng, hãy cân nhắc dùng **system** service thay vì user service (không cần lingering). Xem [Sổ tay vận hành Gateway](</vi/gateway>) để biết ghi chú về systemd.

## Tài liệu liên quan

  * [Sổ tay vận hành Gateway](</vi/gateway>) (flags, giám sát, cổng)
  * [Cấu hình Gateway](</vi/gateway/configuration>) (schema cấu hình + ví dụ)
  * [Discord](</vi/channels/discord>) và [Telegram](</vi/channels/telegram>) (thẻ trả lời + cài đặt replyToMode)
  * [Thiết lập trợ lý OpenClaw](</vi/start/openclaw>)
  * [Ứng dụng macOS](</vi/platforms/macos>) (vòng đời gateway)


Was this useful?YesNo