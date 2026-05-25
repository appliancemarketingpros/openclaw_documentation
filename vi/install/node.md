---
title: Node.js
source_url: https://docs.openclaw.ai/vi/install/node
scraped_at: 2026-05-25
---

OpenClaw yêu cầu **Node 22.16 trở lên**. **Node 24 là runtime mặc định và được khuyến nghị** cho các lượt cài đặt, CI và quy trình phát hành. Node 22 vẫn được hỗ trợ qua nhánh LTS đang hoạt động. [script cài đặt](</vi/install#alternative-install-methods>) sẽ tự động phát hiện và cài đặt Node - trang này dành cho khi bạn muốn tự thiết lập Node và đảm bảo mọi thứ được nối đúng cách (phiên bản, PATH, cài đặt toàn cục).

## Kiểm tra phiên bản của bạn

bashCopy code
[code]
    node -v
[/code]

Nếu lệnh này in ra `v24.x.x` trở lên, bạn đang dùng mặc định được khuyến nghị. Nếu lệnh này in ra `v22.16.x` trở lên, bạn đang dùng đường dẫn Node 22 LTS được hỗ trợ, nhưng chúng tôi vẫn khuyến nghị nâng cấp lên Node 24 khi thuận tiện. Nếu Node chưa được cài đặt hoặc phiên bản quá cũ, hãy chọn một phương thức cài đặt bên dưới.

## Cài đặt Node

### macOS

**Homebrew** (được khuyến nghị):

bashCopy code
[code]
    brew install node
[/code]

Hoặc tải trình cài đặt macOS từ [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Hoặc dùng trình quản lý phiên bản (xem bên dưới).

### Windows

**winget** (được khuyến nghị):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Hoặc tải trình cài đặt Windows từ [nodejs.org](<https://nodejs.org/>).

Sử dụng trình quản lý phiên bản (nvm, fnm, mise, asdf)

Trình quản lý phiên bản cho phép bạn dễ dàng chuyển đổi giữa các phiên bản Node. Các tùy chọn phổ biến:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- nhanh, đa nền tảng
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- được sử dụng rộng rãi trên macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- đa ngôn ngữ (Node, Python, Ruby, v.v.)


Ví dụ với fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Khắc phục sự cố

### `openclaw: command not found`

Điều này gần như luôn có nghĩa là thư mục bin toàn cục của npm không nằm trong PATH của bạn.

* ### Tìm tiền tố npm toàn cục của bạn

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Kiểm tra xem nó có nằm trong PATH của bạn không

bashCopy code
[code]
    echo "$PATH"
[/code]

Tìm `<npm-prefix>/bin` (macOS/Linux) hoặc `<npm-prefix>` (Windows) trong đầu ra.

* ### Thêm nó vào tệp khởi động shell của bạn

### macOS / Linux

Thêm vào `~/.zshrc` hoặc `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Sau đó mở một terminal mới (hoặc chạy `rehash` trong zsh / `hash -r` trong bash).

### Windows

Thêm đầu ra của `npm prefix -g` vào PATH hệ thống của bạn qua Settings → System → Environment Variables.

### Lỗi quyền trên `npm install -g` (Linux)

Nếu bạn thấy lỗi `EACCES`, hãy chuyển tiền tố toàn cục của npm sang một thư mục mà người dùng có quyền ghi:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Thêm dòng `export PATH=...` vào `~/.bashrc` hoặc `~/.zshrc` của bạn để đặt nó vĩnh viễn.

## Liên quan

  * [Tổng quan cài đặt](</vi/install>) \- tất cả phương thức cài đặt
  * [Cập nhật](</vi/install/updating>) \- giữ OpenClaw luôn cập nhật
  * [Bắt đầu](</vi/start/getting-started>) \- các bước đầu tiên sau khi cài đặt


Was this useful?YesNo