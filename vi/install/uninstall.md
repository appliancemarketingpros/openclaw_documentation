---
title: Gỡ cài đặt
source_url: https://docs.openclaw.ai/vi/install/uninstall
scraped_at: 2026-05-25
---

Hai cách:

  * **Cách dễ** nếu `openclaw` vẫn còn được cài đặt.
  * **Gỡ dịch vụ thủ công** nếu CLI đã mất nhưng dịch vụ vẫn đang chạy.


## Cách dễ (CLI vẫn còn được cài đặt)

Khuyến nghị: dùng trình gỡ cài đặt tích hợp sẵn:

bashCopy code
[code]
    openclaw uninstall
[/code]

Không tương tác (tự động hóa / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Các bước thủ công (cùng kết quả):

  1. Dừng dịch vụ Gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Gỡ cài đặt dịch vụ Gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Xóa trạng thái + cấu hình:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Nếu bạn đặt `OPENCLAW_CONFIG_PATH` thành một vị trí tùy chỉnh bên ngoài thư mục trạng thái, hãy xóa cả tệp đó.

  4. Xóa workspace của bạn (tùy chọn, xóa các tệp agent):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Gỡ bản cài đặt CLI (chọn cách bạn đã dùng):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Nếu bạn đã cài đặt ứng dụng macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Ghi chú:

  * Nếu bạn đã dùng hồ sơ (`--profile` / `OPENCLAW_PROFILE`), lặp lại bước 3 cho từng thư mục trạng thái (mặc định là `~/.openclaw-<profile>`).
  * Ở chế độ từ xa, thư mục trạng thái nằm trên **máy chủ Gateway** , vì vậy cũng chạy các bước 1-4 ở đó.


## Gỡ dịch vụ thủ công (CLI chưa được cài đặt)

Dùng cách này nếu dịch vụ Gateway vẫn tiếp tục chạy nhưng thiếu `openclaw`.

### macOS (launchd)

Nhãn mặc định là `ai.openclaw.gateway` (hoặc `ai.openclaw.<profile>`; `com.openclaw.*` cũ có thể vẫn tồn tại):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Nếu bạn đã dùng hồ sơ, hãy thay nhãn và tên plist bằng `ai.openclaw.<profile>`. Xóa mọi plist `com.openclaw.*` cũ nếu có.

### Linux (đơn vị người dùng systemd)

Tên đơn vị mặc định là `openclaw-gateway.service` (hoặc `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

Tên tác vụ mặc định là `OpenClaw Gateway` (hoặc `OpenClaw Gateway (<profile>)`). Tập lệnh tác vụ nằm trong thư mục trạng thái của bạn.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Nếu bạn đã dùng hồ sơ, hãy xóa tên tác vụ tương ứng và `~\.openclaw-<profile>\gateway.cmd`.

## Cài đặt thông thường và checkout mã nguồn

### Cài đặt thông thường ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Nếu bạn đã dùng `https://openclaw.ai/install.sh` hoặc `install.ps1`, CLI đã được cài đặt bằng `npm install -g openclaw@latest`. Gỡ bằng `npm rm -g openclaw` (hoặc `pnpm remove -g` / `bun remove -g` nếu bạn đã cài đặt theo cách đó).

### Checkout mã nguồn (git clone)

Nếu bạn chạy từ một bản checkout kho mã (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Gỡ cài đặt dịch vụ Gateway **trước khi** xóa kho mã (dùng cách dễ ở trên hoặc gỡ dịch vụ thủ công).
  2. Xóa thư mục kho mã.
  3. Xóa trạng thái + workspace như đã trình bày ở trên.


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Hướng dẫn di chuyển](</vi/install/migrating>)


Was this useful?YesNo