---
title: Hetzner
source_url: https://docs.openclaw.ai/vi/install/hetzner
scraped_at: 2026-05-25
---

## Mục tiêu

Chạy một OpenClaw Gateway liên tục trên VPS Hetzner bằng Docker, với trạng thái bền vững, binary được tích hợp sẵn và hành vi khởi động lại an toàn.

Nếu bạn muốn "OpenClaw 24/7 với giá khoảng ~$5", đây là thiết lập đáng tin cậy đơn giản nhất. Giá Hetzner có thể thay đổi; hãy chọn VPS Debian/Ubuntu nhỏ nhất và nâng cấp nếu gặp OOM.

Nhắc lại mô hình bảo mật:

  * Các tác tử dùng chung trong công ty là phù hợp khi mọi người đều nằm trong cùng ranh giới tin cậy và runtime chỉ dùng cho công việc.
  * Giữ tách biệt nghiêm ngặt: VPS/runtime chuyên dụng + tài khoản chuyên dụng; không dùng hồ sơ Apple/Google/trình duyệt/trình quản lý mật khẩu cá nhân trên máy chủ đó.
  * Nếu người dùng có thể đối kháng với nhau, hãy tách theo gateway/máy chủ/người dùng OS.


Xem [Bảo mật](</vi/gateway/security>) và [Lưu trữ VPS](</vi/vps>).

## Chúng ta đang làm gì (nói đơn giản)?

  * Thuê một máy chủ Linux nhỏ (VPS Hetzner)
  * Cài đặt Docker (runtime ứng dụng được cô lập)
  * Khởi động OpenClaw Gateway trong Docker
  * Duy trì `~/.openclaw` \+ `~/.openclaw/workspace` trên máy chủ (tồn tại qua các lần khởi động lại/tạo lại)
  * Truy cập Giao diện điều khiển từ laptop của bạn qua đường hầm SSH


Trạng thái `~/.openclaw` được mount đó bao gồm `openclaw.json`, mỗi tác tử `agents/<agentId>/agent/auth-profiles.json`, và `.env`.

Có thể truy cập Gateway qua:

  * Chuyển tiếp cổng SSH từ laptop của bạn
  * Mở cổng trực tiếp nếu bạn tự quản lý tường lửa và token


Hướng dẫn này giả định bạn dùng Ubuntu hoặc Debian trên Hetzner.  
Nếu bạn dùng VPS Linux khác, hãy ánh xạ các gói tương ứng. Để biết quy trình Docker chung, xem [Docker](</vi/install/docker>).

* * *

## Lộ trình nhanh (người vận hành có kinh nghiệm)

  1. Cấp phát VPS Hetzner
  2. Cài đặt Docker
  3. Sao chép kho lưu trữ OpenClaw
  4. Tạo thư mục máy chủ bền vững
  5. Cấu hình `.env` và `docker-compose.yml`
  6. Tích hợp các binary bắt buộc vào image
  7. `docker compose up -d`
  8. Xác minh tính bền vững và quyền truy cập Gateway


* * *

## Bạn cần gì

  * VPS Hetzner có quyền root
  * Truy cập SSH từ laptop của bạn
  * Có kinh nghiệm cơ bản với SSH + sao chép/dán
  * Khoảng 20 phút
  * Docker và Docker Compose
  * Thông tin xác thực mô hình
  * Thông tin xác thực provider tùy chọn 
    * QR WhatsApp
    * Token bot Telegram
    * Gmail OAuth


* * *

* ### Cấp phát VPS

Tạo một VPS Ubuntu hoặc Debian trong Hetzner.

Kết nối bằng root:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Hướng dẫn này giả định VPS có trạng thái bền vững. Đừng coi nó là hạ tầng dùng một lần.

* ### Cài đặt Docker (trên VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Xác minh:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Sao chép kho lưu trữ OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Hướng dẫn này giả định bạn sẽ build một image tùy chỉnh để đảm bảo binary được duy trì.

* ### Tạo thư mục máy chủ bền vững

Container Docker là tạm thời. Mọi trạng thái dài hạn phải nằm trên máy chủ.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Cấu hình biến môi trường

Tạo `.env` trong thư mục gốc của kho lưu trữ.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Đặt `OPENCLAW_GATEWAY_TOKEN` khi bạn muốn quản lý token gateway ổn định thông qua `.env`; nếu không, hãy cấu hình `gateway.auth.token` trước khi dựa vào client qua các lần khởi động lại. Nếu không có nguồn nào tồn tại, OpenClaw sử dụng token chỉ dành cho runtime trong lần khởi động đó. Tạo mật khẩu keyring và dán vào `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Không commit tệp này.**

Tệp `.env` này dành cho env của container/runtime như `OPENCLAW_GATEWAY_TOKEN`. Xác thực OAuth/API-key của provider đã lưu nằm trong `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` được mount.

* ### Cấu hình Docker Compose

Tạo hoặc cập nhật `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` chỉ nhằm tiện bootstrap, không phải là thay thế cho cấu hình gateway đúng cách. Vẫn hãy đặt xác thực (`gateway.auth.token` hoặc mật khẩu) và dùng thiết lập bind an toàn cho triển khai của bạn.

* ### Các bước runtime Docker VM dùng chung

Dùng hướng dẫn runtime dùng chung cho quy trình máy chủ Docker phổ biến:

  * [Tích hợp các binary bắt buộc vào image](</vi/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Build và khởi chạy](</vi/install/docker-vm-runtime#build-and-launch>)
  * [Những gì được duy trì ở đâu](</vi/install/docker-vm-runtime#what-persists-where>)
  * [Cập nhật](</vi/install/docker-vm-runtime#updates>)


* ### Truy cập riêng cho Hetzner

Sau các bước build và khởi chạy dùng chung, hoàn tất thiết lập sau để mở đường hầm:

**Điều kiện tiên quyết:** Đảm bảo cấu hình sshd của VPS cho phép chuyển tiếp TCP. Nếu bạn đã siết chặt cấu hình SSH, hãy kiểm tra `/etc/ssh/sshd_config` và đặt:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` cho phép chuyển tiếp cục bộ `ssh -L` từ laptop của bạn trong khi chặn chuyển tiếp từ xa từ máy chủ. Đặt thành `no` sẽ làm đường hầm thất bại với: `channel 3: open failed: administratively prohibited: open failed`

Sau khi xác nhận chuyển tiếp TCP đã được bật, khởi động lại dịch vụ SSH (`systemctl restart ssh`) và chạy đường hầm từ laptop của bạn:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Mở:

`http://127.0.0.1:18789/`

Dán shared secret đã cấu hình. Hướng dẫn này dùng token gateway theo mặc định; nếu bạn đã chuyển sang xác thực bằng mật khẩu, hãy dùng mật khẩu đó.

Bản đồ trạng thái dùng chung nằm trong [Runtime Docker VM](</vi/install/docker-vm-runtime#what-persists-where>).

## Hạ tầng dưới dạng mã (Terraform)

Đối với các nhóm ưu tiên quy trình infrastructure-as-code, một thiết lập Terraform do cộng đồng duy trì cung cấp:

  * Cấu hình Terraform dạng mô-đun với quản lý trạng thái từ xa
  * Cấp phát tự động qua cloud-init
  * Script triển khai (bootstrap, triển khai, sao lưu/khôi phục)
  * Gia cố bảo mật (tường lửa, UFW, chỉ truy cập SSH)
  * Cấu hình đường hầm SSH để truy cập gateway


**Kho lưu trữ:**

  * Hạ tầng: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Cấu hình Docker: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Cách tiếp cận này bổ sung cho thiết lập Docker ở trên bằng các triển khai có thể tái tạo, hạ tầng được kiểm soát phiên bản và khôi phục thảm họa tự động.

## Bước tiếp theo

  * Thiết lập kênh nhắn tin: [Kênh](</vi/channels>)
  * Cấu hình Gateway: [Cấu hình Gateway](</vi/gateway/configuration>)
  * Luôn cập nhật OpenClaw: [Cập nhật](</vi/install/updating>)


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Fly.io](</vi/install/fly>)
  * [Docker](</vi/install/docker>)
  * [Lưu trữ VPS](</vi/vps>)


Was this useful?YesNo