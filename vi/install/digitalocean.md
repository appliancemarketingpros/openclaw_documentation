---
title: DigitalOcean
source_url: https://docs.openclaw.ai/vi/install/digitalocean
scraped_at: 2026-05-25
---

Chạy OpenClaw Gateway bền bỉ trên DigitalOcean Droplet (~6 USD/tháng cho gói Basic 1 GB).

DigitalOcean là lộ trình VPS trả phí đơn giản nhất. Nếu bạn muốn các tùy chọn rẻ hơn hoặc miễn phí:

  * [Hetzner](</vi/install/hetzner>) — 3,79 €/tháng, nhiều lõi/RAM hơn trên mỗi đô la.
  * [Oracle Cloud](</vi/install/oracle>) — ARM Always Free (tối đa 4 OCPU, 24 GB RAM), nhưng đăng ký có thể khá khó khăn và chỉ hỗ trợ ARM.


## Điều kiện tiên quyết

  * Tài khoản DigitalOcean ([đăng ký](<https://cloud.digitalocean.com/registrations/new>))
  * Cặp khóa SSH (hoặc sẵn sàng dùng xác thực bằng mật khẩu)
  * Khoảng 20 phút


## Thiết lập

* ### Tạo một Droplet

  1. Đăng nhập vào [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Nhấp **Create > Droplets**.
  3. Chọn: 
     * **Khu vực:** Gần bạn nhất
     * **Ảnh:** Ubuntu 24.04 LTS
     * **Kích thước:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Xác thực:** Khóa SSH (khuyến nghị) hoặc mật khẩu
  4. Nhấp **Create Droplet** và ghi lại địa chỉ IP.


* ### Kết nối và cài đặt

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Chỉ dùng shell root cho bước khởi tạo hệ thống. Chạy các lệnh OpenClaw dưới người dùng không phải root `openclaw` để trạng thái nằm dưới `/home/openclaw/.openclaw/` và Gateway được cài đặt dưới dạng dịch vụ systemd của người dùng đó.

* ### Chạy quy trình hướng dẫn ban đầu

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Trình hướng dẫn sẽ dẫn bạn qua xác thực mô hình, thiết lập kênh, tạo token Gateway và cài đặt daemon (systemd).

* ### Thêm swap (khuyến nghị cho Droplet 1 GB)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Xác minh Gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Truy cập giao diện điều khiển

Theo mặc định, Gateway liên kết với loopback. Chọn một trong các tùy chọn sau.

**Tùy chọn A: Đường hầm SSH (đơn giản nhất)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Sau đó mở `http://localhost:18789`.

**Tùy chọn B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Sau đó mở `https://<magicdns>/` từ bất kỳ thiết bị nào trên tailnet của bạn.

Tailscale Serve xác thực giao diện điều khiển và lưu lượng WebSocket thông qua header nhận dạng tailnet, giả định rằng chính máy chủ Gateway là đáng tin cậy. Các endpoint HTTP API vẫn tuân theo chế độ xác thực bình thường của Gateway (token/mật khẩu). Để yêu cầu thông tin xác thực bí mật dùng chung rõ ràng qua Serve, hãy đặt `gateway.auth.allowTailscale: false` và dùng `gateway.auth.mode: "token"` hoặc `"password"`.

**Tùy chọn C: Liên kết tailnet (không dùng Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Sau đó mở `http://<tailscale-ip>:18789` (yêu cầu token).

## Tính bền bỉ và sao lưu

Trạng thái OpenClaw nằm dưới:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` theo từng agent, trạng thái kênh/nhà cung cấp và dữ liệu phiên.
  * `~/.openclaw/workspace/` — workspace của agent ([SOUL.md](<http://SOUL.md>), bộ nhớ, artifact).


Các dữ liệu này vẫn tồn tại sau khi Droplet khởi động lại. Để tạo snapshot có thể di chuyển:

bashCopy code
[code]
    openclaw backup create
[/code]

Snapshot của DigitalOcean sao lưu toàn bộ Droplet; `openclaw backup create` có thể di chuyển giữa các máy chủ.

## Mẹo cho RAM 1 GB

Droplet 6 USD chỉ có 1 GB RAM. Để mọi thứ chạy mượt:

  * Đảm bảo bước swap ở trên nằm trong `/etc/fstab` để nó tồn tại sau khi khởi động lại.
  * Ưu tiên các mô hình dựa trên API (Claude, GPT) thay vì mô hình cục bộ — suy luận LLM cục bộ không phù hợp với 1 GB.
  * Đặt `agents.defaults.model.primary` thành một mô hình nhỏ hơn nếu bạn gặp OOM trên prompt lớn.
  * Theo dõi bằng `free -h` và `htop`.


## Khắc phục sự cố

**Gateway không khởi động** \-- Chạy `openclaw doctor --non-interactive` và kiểm tra nhật ký bằng `journalctl --user -u openclaw-gateway.service -n 50`.

**Cổng đã được sử dụng** \-- Chạy `lsof -i :18789` để tìm tiến trình, rồi dừng tiến trình đó.

**Hết bộ nhớ** \-- Xác minh swap đang hoạt động bằng `free -h`. Nếu vẫn gặp OOM, hãy dùng các mô hình dựa trên API (Claude, GPT) thay vì mô hình cục bộ, hoặc nâng cấp lên Droplet 2 GB.

## Bước tiếp theo

  * [Kênh](</vi/channels>) \-- kết nối Telegram, WhatsApp, Discord và nhiều kênh khác
  * [Cấu hình Gateway](</vi/gateway/configuration>) \-- tất cả tùy chọn cấu hình
  * [Cập nhật](</vi/install/updating>) \-- giữ OpenClaw luôn cập nhật


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Fly.io](</vi/install/fly>)
  * [Hetzner](</vi/install/hetzner>)
  * [Lưu trữ VPS](</vi/vps>)


Was this useful?YesNo