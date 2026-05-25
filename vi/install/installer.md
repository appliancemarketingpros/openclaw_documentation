---
title: Cơ chế nội bộ của trình cài đặt
source_url: https://docs.openclaw.ai/vi/install/installer
scraped_at: 2026-05-25
---

OpenClaw cung cấp ba tập lệnh cài đặt, được phân phối từ `openclaw.ai`.

Tập lệnh | Nền tảng | Chức năng  
---|---|---  
`install.sh` | macOS / Linux / WSL | Cài đặt Node nếu cần, cài đặt OpenClaw qua npm (mặc định) hoặc git, và có thể chạy quy trình thiết lập ban đầu.  
`install-cli.sh` | macOS / Linux / WSL | Cài đặt Node + OpenClaw vào một tiền tố cục bộ (`~/.openclaw`) bằng chế độ npm hoặc git checkout. Không yêu cầu root.  
`install.ps1` | Windows (PowerShell) | Cài đặt Node nếu cần, cài đặt OpenClaw qua npm (mặc định) hoặc git, và có thể chạy quy trình thiết lập ban đầu.  
  
## Lệnh nhanh

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Luồng ([install.sh](<http://install.sh>))

* ### Detect OS

Hỗ trợ macOS và Linux (bao gồm WSL). Nếu phát hiện macOS, cài đặt Homebrew nếu còn thiếu.

* ### Ensure Node.js 24 by default

Kiểm tra phiên bản Node và cài đặt Node 24 nếu cần (Homebrew trên macOS, tập lệnh thiết lập NodeSource trên Linux apt/dnf/yum). OpenClaw vẫn hỗ trợ Node 22 LTS, hiện là `22.16+`, để tương thích.

* ### Ensure Git

Cài đặt Git nếu còn thiếu.

* ### Install OpenClaw

  * phương thức `npm` (mặc định): cài đặt npm toàn cục
  * phương thức `git`: sao chép/cập nhật repo, cài đặt phụ thuộc bằng pnpm, build, sau đó cài đặt wrapper tại `~/.local/bin/openclaw`


* ### Post-install tasks

  * Làm mới dịch vụ Gateway đã tải theo khả năng tốt nhất (`openclaw gateway install --force`, rồi khởi động lại)
  * Chạy `openclaw doctor --non-interactive` khi nâng cấp và cài đặt bằng git (theo khả năng tốt nhất)
  * Thử chạy quy trình thiết lập ban đầu khi phù hợp (có TTY, không tắt thiết lập ban đầu, và các kiểm tra bootstrap/cấu hình đạt)
  * Mặc định `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Phát hiện source checkout

Nếu chạy bên trong một checkout OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), tập lệnh sẽ đề xuất:

  * dùng checkout (`git`), hoặc
  * dùng cài đặt toàn cục (`npm`)


Nếu không có TTY và chưa đặt phương thức cài đặt, mặc định là `npm` và hiển thị cảnh báo.

Tập lệnh thoát với mã `2` khi chọn phương thức không hợp lệ hoặc giá trị `--install-method` không hợp lệ.

### Ví dụ ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference Cờ | Mô tả  
---|---  
`--install-method npm|git` | Chọn phương thức cài đặt (mặc định: `npm`). Bí danh: `--method`  
`--npm` | Lối tắt cho phương thức npm  
`--git` | Lối tắt cho phương thức git. Bí danh: `--github`  
`--version <version|dist-tag|spec>` | Phiên bản npm, dist-tag, hoặc package spec (mặc định: `latest`)  
`--beta` | Dùng beta dist-tag nếu có, nếu không thì quay về `latest`  
`--git-dir <path>` | Thư mục checkout (mặc định: `~/openclaw`). Bí danh: `--dir`  
`--no-git-update` | Bỏ qua `git pull` cho checkout hiện có  
`--no-prompt` | Tắt lời nhắc  
`--no-onboard` | Bỏ qua thiết lập ban đầu  
`--onboard` | Bật thiết lập ban đầu  
`--dry-run` | In các hành động mà không áp dụng thay đổi  
`--verbose` | Bật đầu ra gỡ lỗi (`set -x`, nhật ký npm mức notice)  
`--help` | Hiển thị cách dùng (`-h`)  
Environment variables reference Biến | Mô tả  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Phương thức cài đặt  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Phiên bản npm, dist-tag, hoặc package spec  
`OPENCLAW_BETA=0|1` | Dùng beta nếu có  
`OPENCLAW_GIT_DIR=<path>` | Thư mục checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Bật/tắt cập nhật git  
`OPENCLAW_NO_PROMPT=1` | Tắt lời nhắc  
`OPENCLAW_NO_ONBOARD=1` | Bỏ qua thiết lập ban đầu  
`OPENCLAW_DRY_RUN=1` | Chế độ chạy thử  
`OPENCLAW_VERBOSE=1` | Chế độ gỡ lỗi  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Mức nhật ký npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kiểm soát hành vi sharp/libvips (mặc định: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Luồng ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Tải xuống một tarball Node LTS được ghim và hỗ trợ (phiên bản được nhúng trong tập lệnh và cập nhật độc lập) vào `<prefix>/tools/node-v<version>` và xác minh SHA-256.

* ### Ensure Git

Nếu thiếu Git, thử cài đặt qua apt/dnf/yum trên Linux hoặc Homebrew trên macOS.

* ### Install OpenClaw under prefix

  * phương thức `npm` (mặc định): cài đặt dưới tiền tố bằng npm, rồi ghi wrapper vào `<prefix>/bin/openclaw`
  * phương thức `git`: sao chép/cập nhật một checkout (mặc định `~/openclaw`) và vẫn ghi wrapper vào `<prefix>/bin/openclaw`


* ### Refresh loaded gateway service

Nếu một dịch vụ Gateway đã được tải từ cùng tiền tố đó, tập lệnh sẽ chạy `openclaw gateway install --force`, rồi `openclaw gateway restart`, và thăm dò tình trạng Gateway theo khả năng tốt nhất.

### Ví dụ ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference Cờ | Mô tả  
---|---  
`--prefix <path>` | Tiền tố cài đặt (mặc định: `~/.openclaw`)  
`--install-method npm|git` | Chọn phương thức cài đặt (mặc định: `npm`). Bí danh: `--method`  
`--npm` | Lối tắt cho phương thức npm  
`--git`, `--github` | Lối tắt cho phương thức git  
`--git-dir <path>` | Thư mục Git checkout (mặc định: `~/openclaw`). Bí danh: `--dir`  
`--version <ver>` | Phiên bản OpenClaw hoặc dist-tag (mặc định: `latest`)  
`--node-version <ver>` | Phiên bản Node (mặc định: `22.22.0`)  
`--json` | Phát sự kiện NDJSON  
`--onboard` | Chạy `openclaw onboard` sau khi cài đặt  
`--no-onboard` | Bỏ qua thiết lập ban đầu (mặc định)  
`--set-npm-prefix` | Trên Linux, buộc tiền tố npm thành `~/.npm-global` nếu tiền tố hiện tại không ghi được  
`--help` | Hiển thị cách dùng (`-h`)  
Environment variables reference Biến | Mô tả  
---|---  
`OPENCLAW_PREFIX=<path>` | Tiền tố cài đặt  
`OPENCLAW_INSTALL_METHOD=git|npm` | Phương thức cài đặt  
`OPENCLAW_VERSION=<ver>` | Phiên bản OpenClaw hoặc dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Phiên bản Node  
`OPENCLAW_GIT_DIR=<path>` | Thư mục checkout Git cho cài đặt bằng git  
`OPENCLAW_GIT_UPDATE=0|1` | Bật/tắt cập nhật git cho các checkout hiện có  
`OPENCLAW_NO_ONBOARD=1` | Bỏ qua thiết lập ban đầu  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Mức nhật ký npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kiểm soát hành vi sharp/libvips (mặc định: `1`)  
  
* * *

## install.ps1

### Luồng (install.ps1)

* ### Đảm bảo môi trường PowerShell + Windows

Yêu cầu PowerShell 5+.

* ### Đảm bảo Node.js 24 theo mặc định

Nếu thiếu, thử cài đặt qua winget, sau đó Chocolatey, rồi Scoop. Node 22 LTS, hiện là `22.16+`, vẫn được hỗ trợ để tương thích.

* ### Cài đặt OpenClaw

  * Phương thức `npm` (mặc định): cài đặt npm toàn cục bằng `-Tag` đã chọn, chạy từ thư mục tạm của trình cài đặt có thể ghi để các shell được mở trong thư mục được bảo vệ như `C:\` vẫn hoạt động
  * Phương thức `git`: clone/cập nhật repo, cài đặt/build bằng pnpm, và cài đặt wrapper tại `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Tác vụ sau cài đặt

  * Thêm thư mục bin cần thiết vào PATH của người dùng khi có thể
  * Làm mới dịch vụ Gateway đã tải theo cách cố gắng tối đa (`openclaw gateway install --force`, rồi khởi động lại)
  * Chạy `openclaw doctor --non-interactive` khi nâng cấp và cài đặt bằng git (cố gắng tối đa)


* ### Xử lý lỗi

`iwr ... | iex` và cài đặt bằng scriptblock báo lỗi kết thúc mà không đóng phiên PowerShell hiện tại. Cài đặt trực tiếp bằng `powershell -File` / `pwsh -File` vẫn thoát với mã khác 0 cho tự động hóa.

### Ví dụ (install.ps1)

### Mặc định

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Cài đặt bằng git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main qua npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Thư mục git tùy chỉnh

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Chạy thử

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Vết gỡ lỗi

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Tham chiếu cờ Cờ | Mô tả  
---|---  
`-InstallMethod npm|git` | Phương thức cài đặt (mặc định: `npm`)  
`-Tag <tag|version|spec>` | dist-tag, phiên bản, hoặc đặc tả gói npm (mặc định: `latest`)  
`-GitDir <path>` | Thư mục checkout (mặc định: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Bỏ qua thiết lập ban đầu  
`-NoGitUpdate` | Bỏ qua `git pull`  
`-DryRun` | Chỉ in các hành động  
Tham chiếu biến môi trường Biến | Mô tả  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Phương thức cài đặt  
`OPENCLAW_GIT_DIR=<path>` | Thư mục checkout  
`OPENCLAW_NO_ONBOARD=1` | Bỏ qua thiết lập ban đầu  
`OPENCLAW_GIT_UPDATE=0` | Tắt git pull  
`OPENCLAW_DRY_RUN=1` | Chế độ chạy thử  
  
* * *

## CI và tự động hóa

Dùng cờ/biến môi trường không tương tác để các lần chạy có thể dự đoán.

### install.sh (npm không tương tác)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (git không tương tác)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (bỏ qua thiết lập ban đầu)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Khắc phục sự cố

Tại sao cần Git?

Git là bắt buộc cho phương thức cài đặt `git`. Với cài đặt bằng `npm`, Git vẫn được kiểm tra/cài đặt để tránh lỗi `spawn git ENOENT` khi các phụ thuộc dùng URL git.

Tại sao npm gặp EACCES trên Linux?

Một số thiết lập Linux trỏ tiền tố toàn cục của npm tới các đường dẫn do root sở hữu. `install.sh` có thể chuyển tiền tố sang `~/.npm-global` và thêm các export PATH vào tệp rc của shell (khi các tệp đó tồn tại).

Sự cố sharp/libvips

Các script mặc định đặt `SHARP_IGNORE_GLOBAL_LIBVIPS=1` để tránh việc sharp build dựa trên libvips hệ thống. Để ghi đè:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Cài đặt Git for Windows, mở lại PowerShell, chạy lại trình cài đặt.

Windows: "openclaw is not recognized"

Chạy `npm config get prefix` và thêm thư mục đó vào PATH của người dùng (không cần hậu tố `\bin` trên Windows), rồi mở lại PowerShell.

Windows: cách lấy đầu ra trình cài đặt chi tiết

`install.ps1` hiện không cung cấp công tắc `-Verbose`. Dùng truy vết PowerShell để chẩn đoán ở cấp script:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

không tìm thấy openclaw sau khi cài đặt

Thường là sự cố PATH. Xem [khắc phục sự cố Node.js](</vi/install/node#troubleshooting>).

## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Cập nhật](</vi/install/updating>)
  * [Gỡ cài đặt](</vi/install/uninstall>)


Was this useful?YesNo