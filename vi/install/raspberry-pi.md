---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/vi/install/raspberry-pi
scraped_at: 2026-05-25
---

Chạy một OpenClaw Gateway bền bỉ, luôn bật trên Raspberry Pi. Vì Pi chỉ là gateway (các mô hình chạy trên đám mây qua API), ngay cả một Pi cấu hình vừa phải cũng xử lý khối lượng công việc tốt — chi phí phần cứng thường là **$35–80 một lần** , không có phí hằng tháng.

## Khả năng tương thích phần cứng

Mẫu Pi | RAM | Hoạt động? | Ghi chú  
---|---|---|---  
Pi 5 | 4/8 GB | Tốt nhất | Nhanh nhất, được khuyến nghị.  
Pi 4 | 4 GB | Tốt | Lựa chọn cân bằng cho hầu hết người dùng.  
Pi 4 | 2 GB | Được | Thêm swap.  
Pi 4 | 1 GB | Hạn chế | Có thể dùng với swap, cấu hình tối thiểu.  
Pi 3B+ | 1 GB | Chậm | Hoạt động nhưng ì ạch.  
Pi Zero 2 W | 512 MB | Không | Không được khuyến nghị.  
  
**Tối thiểu:** RAM 1 GB, 1 nhân, 500 MB dung lượng đĩa trống, hệ điều hành 64-bit. **Khuyến nghị:** RAM 2 GB trở lên, thẻ SD 16 GB trở lên (hoặc USB SSD), Ethernet.

## Điều kiện tiên quyết

  * Raspberry Pi 4 hoặc 5 với RAM 2 GB trở lên (khuyến nghị 4 GB)
  * Thẻ MicroSD (16 GB trở lên) hoặc USB SSD (hiệu năng tốt hơn)
  * Bộ nguồn Pi chính hãng
  * Kết nối mạng (Ethernet hoặc WiFi)
  * Raspberry Pi OS 64-bit (bắt buộc -- không dùng 32-bit)
  * Khoảng 30 phút


## Thiết lập

* ### Ghi hệ điều hành

Dùng **Raspberry Pi OS Lite (64-bit)** \-- không cần desktop cho máy chủ headless.

  1. Tải [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>).
  2. Chọn hệ điều hành: **Raspberry Pi OS Lite (64-bit)**.
  3. Trong hộp thoại cài đặt, cấu hình sẵn: 
     * Tên máy chủ: `gateway-host`
     * Bật SSH
     * Đặt tên người dùng và mật khẩu
     * Cấu hình WiFi (nếu không dùng Ethernet)
  4. Ghi vào thẻ SD hoặc ổ USB, cắm vào, rồi khởi động Pi.


* ### Kết nối qua SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Cập nhật hệ thống

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Cài đặt Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Thêm swap (quan trọng với 2 GB trở xuống)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### Cài đặt OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Làm theo trình hướng dẫn. Khóa API được khuyến nghị hơn OAuth cho thiết bị headless. Telegram là kênh dễ bắt đầu nhất.

* ### Xác minh

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Truy cập giao diện điều khiển

Trên máy tính của bạn, lấy URL bảng điều khiển từ Pi:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Sau đó tạo một SSH tunnel trong terminal khác:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Mở URL đã in trong trình duyệt cục bộ của bạn. Để truy cập từ xa luôn bật, xem [tích hợp Tailscale](</vi/gateway/tailscale>).

## Mẹo hiệu năng

**Dùng USB SSD** \-- Thẻ SD chậm và dễ hao mòn. USB SSD cải thiện hiệu năng đáng kể. Xem [hướng dẫn khởi động Pi từ USB](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>).

**Bật cache biên dịch module** \-- Tăng tốc các lần gọi CLI lặp lại trên máy chủ Pi công suất thấp hơn:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Giảm mức sử dụng bộ nhớ** \-- Với thiết lập headless, giải phóng bộ nhớ GPU và tắt các dịch vụ không dùng:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**systemd drop-in để khởi động lại ổn định** \-- Nếu Pi này chủ yếu chạy OpenClaw, thêm một service drop-in:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Sau đó chạy `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`. Trên Pi headless, cũng bật lingering một lần để dịch vụ người dùng vẫn sống sau khi đăng xuất: `sudo loginctl enable-linger "$(whoami)"`.

## Thiết lập mô hình được khuyến nghị

Vì Pi chỉ chạy gateway, hãy dùng các mô hình API được lưu trữ trên đám mây:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Không chạy LLM cục bộ trên Pi — ngay cả các mô hình nhỏ cũng quá chậm để hữu ích. Hãy để Claude hoặc GPT xử lý phần mô hình.

## Ghi chú về binary ARM

Hầu hết tính năng OpenClaw hoạt động trên ARM64 mà không cần thay đổi (Node.js, Telegram, WhatsApp/Baileys, Chromium). Các binary đôi khi thiếu bản dựng ARM thường là các công cụ CLI Go/Rust tùy chọn được phân phối bởi Skills. Xác minh trang phát hành của binary bị thiếu để tìm artifact `linux-arm64` / `aarch64` trước khi chuyển sang build từ mã nguồn.

## Tính bền bỉ và sao lưu

Trạng thái OpenClaw nằm trong:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` theo từng agent, trạng thái kênh/nhà cung cấp, phiên.
  * `~/.openclaw/workspace/` — workspace của agent ([SOUL.md](<http://SOUL.md>), bộ nhớ, artifact).


Các mục này vẫn tồn tại sau khi khởi động lại. Tạo snapshot di động bằng:

bashCopy code
[code]
    openclaw backup create
[/code]

Nếu bạn đặt các mục này trên SSD, cả hiệu năng lẫn tuổi thọ đều cải thiện so với thẻ SD.

## Khắc phục sự cố

**Hết bộ nhớ** \-- Xác minh swap đang hoạt động bằng `free -h`. Tắt các dịch vụ không dùng (`sudo systemctl disable cups bluetooth avahi-daemon`). Chỉ dùng mô hình dựa trên API.

**Hiệu năng chậm** \-- Dùng USB SSD thay vì thẻ SD. Kiểm tra tình trạng giảm tốc CPU bằng `vcgencmd get_throttled` (nên trả về `0x0`).

**Dịch vụ không khởi động** \-- Kiểm tra log bằng `journalctl --user -u openclaw-gateway.service --no-pager -n 100` và chạy `openclaw doctor --non-interactive`. Nếu đây là Pi headless, cũng xác minh lingering đã được bật: `sudo loginctl enable-linger "$(whoami)"`.

**Sự cố binary ARM** \-- Nếu một skill lỗi với "exec format error", kiểm tra xem binary có bản dựng ARM64 không. Xác minh kiến trúc bằng `uname -m` (nên hiển thị `aarch64`).

**WiFi rớt kết nối** \-- Tắt quản lý nguồn WiFi: `sudo iwconfig wlan0 power off`.

## Bước tiếp theo

  * [Kênh](</vi/channels>) \-- kết nối Telegram, WhatsApp, Discord và nhiều kênh khác
  * [Cấu hình Gateway](</vi/gateway/configuration>) \-- tất cả tùy chọn cấu hình
  * [Cập nhật](</vi/install/updating>) \-- giữ OpenClaw luôn cập nhật


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Máy chủ Linux](</vi/vps>)
  * [Nền tảng](</vi/platforms>)


Was this useful?YesNo