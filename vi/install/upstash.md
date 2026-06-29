---
title: Hộp Upstash
source_url: https://docs.openclaw.ai/vi/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Chạy OpenClaw Gateway liên tục trên Upstash Box, một môi trường Linux được quản lý có hỗ trợ vòng đời keep-alive.

Dùng đường hầm SSH để truy cập bảng điều khiển. Không để lộ trực tiếp cổng Gateway ra internet công cộng.

## Điều kiện tiên quyết

  * Tài khoản Upstash
  * Upstash Box keep-alive
  * SSH client trên máy cục bộ của bạn


## Tạo Box

Tạo Box keep-alive trong Upstash Console. Ghi lại Box ID, chẳng hạn như `right-flamingo-14486`, và khóa API Box của bạn.

Upstash duy trì hướng dẫn Box OpenClaw hiện tại tại [Thiết lập OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Kết nối bằng đường hầm SSH

Chuyển tiếp cổng bảng điều khiển OpenClaw tới máy cục bộ của bạn. Dùng khóa API Box làm mật khẩu SSH khi được nhắc:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Các tùy chọn keepalive giúp giảm tình trạng đường hầm bị ngắt khi rảnh trong quá trình onboarding.

## Cài đặt OpenClaw

Bên trong Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Chạy onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Làm theo các lời nhắc. Sao chép URL bảng điều khiển và token khi onboarding hoàn tất.

## Khởi động Gateway

Cấu hình Gateway cho mạng Box và khởi động trong nền:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Khi đường hầm SSH đang hoạt động, mở URL bảng điều khiển cục bộ:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Tự động khởi động lại

Đặt lệnh này làm script khởi tạo Box để Gateway khởi động lại khi Box khởi động:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Khắc phục sự cố

Nếu SSH bị treo trong quá trình onboarding, hãy kết nối lại với cấu hình SSH sạch và keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Thao tác này bỏ qua các thiết lập `~/.ssh/config` cục bộ đã lỗi thời và giữ đường hầm hoạt động qua các khoảng thời gian mạng rảnh.

## Liên quan

  * [Truy cập từ xa](</vi/gateway/remote>)
  * [Bảo mật Gateway](</vi/gateway/security>)
  * [Cập nhật OpenClaw](</vi/install/updating>)


Was this useful?YesNo

Open issue