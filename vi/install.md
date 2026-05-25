---
title: Cài đặt
source_url: https://docs.openclaw.ai/vi/install
scraped_at: 2026-05-25
---

## Yêu cầu hệ thống

  * **Node 24** (khuyến nghị) hoặc Node 22.16+ - tập lệnh cài đặt tự động xử lý việc này
  * **macOS, Linux, hoặc Windows** \- hỗ trợ cả Windows gốc và WSL2; WSL2 ổn định hơn. Xem [Windows](</vi/platforms/windows>).
  * `pnpm` chỉ cần thiết nếu bạn build từ mã nguồn


## Khuyến nghị: tập lệnh cài đặt

Cách cài đặt nhanh nhất. Nó phát hiện OS của bạn, cài đặt Node nếu cần, cài đặt OpenClaw, và khởi chạy quy trình thiết lập ban đầu.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Để cài đặt mà không chạy quy trình thiết lập ban đầu:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Để biết tất cả cờ và tùy chọn CI/tự động hóa, xem [nội bộ trình cài đặt](</vi/install/installer>).

## Phương thức cài đặt thay thế

### Trình cài đặt tiền tố cục bộ (`install-cli.sh`)

Dùng cách này khi bạn muốn giữ OpenClaw và Node dưới một tiền tố cục bộ như `~/.openclaw`, mà không phụ thuộc vào bản cài đặt Node toàn hệ thống:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Mặc định nó hỗ trợ cài đặt npm, cùng với cài đặt từ git-checkout theo cùng luồng tiền tố. Tài liệu tham khảo đầy đủ: [nội bộ trình cài đặt](</vi/install/installer#install-clish>).

Đã cài đặt rồi? Chuyển đổi giữa bản cài đặt package và git bằng `openclaw update --channel dev` và `openclaw update --channel stable`. Xem [Cập nhật](</vi/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm, hoặc bun

Nếu bạn đã tự quản lý Node:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Troubleshooting: sharp build errors (npm)

Nếu `sharp` lỗi do libvips được cài đặt toàn cục:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Từ mã nguồn

Dành cho người đóng góp hoặc bất kỳ ai muốn chạy từ một checkout cục bộ:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Hoặc bỏ qua bước link và dùng `pnpm openclaw ...` từ bên trong repo. Xem [Thiết lập](</vi/start/setup>) để biết đầy đủ các quy trình phát triển.

### Cài đặt từ GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Container và trình quản lý package

[**Docker** Triển khai dạng container hoặc headless. ](</vi/install/docker>) [**Podman** Giải pháp container không root thay thế Docker. ](</vi/install/podman>) [**Nix** Cài đặt khai báo qua Nix flake. ](</vi/install/nix>) [**Ansible** Cấp phát đội máy tự động. ](</vi/install/ansible>) [**Bun** Chỉ dùng CLI qua runtime Bun. ](</vi/install/bun>)

## Xác minh cài đặt

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Nếu bạn muốn khởi động được quản lý sau khi cài đặt:

  * macOS: LaunchAgent qua `openclaw onboard --install-daemon` hoặc `openclaw gateway install`
  * Linux/WSL2: dịch vụ systemd của người dùng qua cùng các lệnh
  * Windows gốc: Scheduled Task trước, với mục đăng nhập trong thư mục Startup theo từng người dùng làm phương án dự phòng nếu việc tạo task bị từ chối


## Lưu trữ và triển khai

Triển khai OpenClaw trên máy chủ đám mây hoặc VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii92aS9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Cập nhật, di chuyển, hoặc gỡ cài đặt [**Updating** Luôn cập nhật OpenClaw. ](</vi/install/updating>) [**Migrating** Chuyển sang máy mới. ](</vi/install/migrating>) [**Uninstall** Gỡ bỏ OpenClaw hoàn toàn. ](</vi/install/uninstall>) Khắc phục sự cố: không tìm thấy `openclaw` Nếu cài đặt thành công nhưng terminal của bạn không tìm thấy `openclaw`: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Nếu `$(npm prefix -g)/bin` không nằm trong `$PATH`, hãy thêm nó vào tệp khởi động shell của bạn (`~/.zshrc` hoặc `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Sau đó mở terminal mới. Xem [thiết lập Node](</vi/install/node>) để biết thêm chi tiết. ](</vi/install/northflank>) Was this useful?YesNo ](</vi/install/render>)](</vi/install/railway>)](</vi/install/azure>)](</vi/install/gcp>)](</vi/install/hetzner>)](</vi/install/kubernetes>)](</vi/install/docker-vm-runtime>)](</vi/vps>)