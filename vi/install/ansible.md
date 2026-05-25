---
title: Ansible
source_url: https://docs.openclaw.ai/vi/install/ansible
scraped_at: 2026-05-25
---

Triển khai OpenClaw lên máy chủ production bằng **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- trình cài đặt tự động với kiến trúc ưu tiên bảo mật.

## Điều kiện tiên quyết

Yêu cầu | Chi tiết  
---|---  
**OS** | Debian 11+ hoặc Ubuntu 20.04+  
**Truy cập** | Quyền root hoặc sudo  
**Mạng** | Kết nối Internet để cài đặt gói  
**Ansible** | 2.14+ (được cài tự động bởi script khởi động nhanh)  
  
## Bạn nhận được gì

  * **Bảo mật ưu tiên tường lửa** \-- UFW + cách ly Docker (chỉ SSH + Tailscale có thể truy cập)
  * **Tailscale VPN** \-- truy cập từ xa an toàn mà không công khai dịch vụ
  * **Docker** \-- container sandbox cách ly, chỉ bind vào localhost
  * **Phòng thủ nhiều lớp** \-- kiến trúc bảo mật 4 lớp
  * **Tích hợp Systemd** \-- tự động khởi động khi boot với hardening
  * **Thiết lập bằng một lệnh** \-- triển khai hoàn tất trong vài phút


## Khởi động nhanh

Cài đặt bằng một lệnh:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Những gì được cài đặt

Playbook Ansible cài đặt và cấu hình:

  1. **Tailscale** \-- VPN mesh để truy cập từ xa an toàn
  2. **Tường lửa UFW** \-- chỉ các cổng SSH + Tailscale
  3. **Docker CE + Compose V2** \-- cho backend sandbox agent mặc định
  4. **Node.js 24 + pnpm** \-- các phụ thuộc runtime (Node 22 LTS, hiện là `22.16+`, vẫn được hỗ trợ)
  5. **OpenClaw** \-- chạy trên host, không container hóa
  6. **Dịch vụ Systemd** \-- tự động khởi động với hardening bảo mật


## Thiết lập sau cài đặt

* ### Chuyển sang người dùng openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Chạy trình hướng dẫn onboarding

Script sau cài đặt hướng dẫn bạn cấu hình các cài đặt OpenClaw.

* ### Kết nối nhà cung cấp nhắn tin

Đăng nhập vào WhatsApp, Telegram, Discord hoặc Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Xác minh cài đặt

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Kết nối với Tailscale

Tham gia VPN mesh của bạn để truy cập từ xa an toàn.

### Lệnh nhanh

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Kiến trúc bảo mật

Triển khai sử dụng mô hình phòng thủ 4 lớp:

  1. **Tường lửa (UFW)** \-- chỉ SSH (22) + Tailscale (41641/udp) được công khai
  2. **VPN (Tailscale)** \-- gateway chỉ truy cập được qua VPN mesh
  3. **Cách ly Docker** \-- chuỗi iptables DOCKER-USER ngăn lộ cổng ra bên ngoài
  4. **Hardening Systemd** \-- NoNewPrivileges, PrivateTmp, người dùng không đặc quyền


Để xác minh bề mặt tấn công bên ngoài của bạn:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Chỉ cổng 22 (SSH) nên mở. Tất cả dịch vụ khác (gateway, Docker) đều bị khóa.

Docker được cài cho sandbox agent (thực thi công cụ cách ly), không phải để chạy chính gateway. Xem [Sandbox và công cụ đa agent](</vi/tools/multi-agent-sandbox-tools>) để cấu hình sandbox.

## Cài đặt thủ công

Nếu bạn muốn kiểm soát thủ công thay vì dùng tự động hóa:

* ### Cài đặt điều kiện tiên quyết

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Clone repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Cài đặt collection Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Chạy playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Hoặc chạy trực tiếp rồi sau đó tự thực thi script thiết lập:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Cập nhật

Trình cài đặt Ansible thiết lập OpenClaw để cập nhật thủ công. Xem [Cập nhật](</vi/install/updating>) để biết quy trình cập nhật chuẩn.

Để chạy lại playbook Ansible (ví dụ, cho các thay đổi cấu hình):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Quy trình này có tính idempotent và an toàn khi chạy nhiều lần.

## Khắc phục sự cố

Tường lửa chặn kết nối của tôi

  * Trước tiên hãy đảm bảo bạn có thể truy cập qua Tailscale VPN
  * Truy cập SSH (cổng 22) luôn được cho phép
  * Gateway chỉ truy cập được qua Tailscale theo thiết kế

Dịch vụ không khởi động bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Sự cố sandbox Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Đăng nhập nhà cung cấp thất bại

Đảm bảo bạn đang chạy với người dùng `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Cấu hình nâng cao

Để biết kiến trúc bảo mật chi tiết và cách khắc phục sự cố, hãy xem repo openclaw-ansible:

  * [Kiến trúc bảo mật](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Chi tiết kỹ thuật](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Hướng dẫn khắc phục sự cố](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Liên quan

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- hướng dẫn triển khai đầy đủ
  * [Docker](</vi/install/docker>) \-- thiết lập gateway container hóa
  * [Cách ly sandbox](</vi/gateway/sandboxing>) \-- cấu hình sandbox agent
  * [Sandbox và công cụ đa agent](</vi/tools/multi-agent-sandbox-tools>) \-- cách ly theo từng agent


Was this useful?YesNo