---
title: GCP
source_url: https://docs.openclaw.ai/vi/install/gcp
scraped_at: 2026-05-25
---

Chạy một OpenClaw Gateway lâu dài trên VM GCP Compute Engine bằng Docker, với trạng thái bền vững, các binary được tích hợp sẵn và hành vi khởi động lại an toàn.

Nếu bạn muốn "OpenClaw 24/7 với ~$5-12/tháng", đây là một thiết lập đáng tin cậy trên Google Cloud. Giá thay đổi theo loại máy và khu vực; hãy chọn VM nhỏ nhất phù hợp với workload của bạn và nâng cấp nếu gặp OOM.

## Chúng ta đang làm gì (nói đơn giản)?

  * Tạo một dự án GCP và bật thanh toán
  * Tạo một VM Compute Engine
  * Cài đặt Docker (runtime ứng dụng cô lập)
  * Khởi động OpenClaw Gateway trong Docker
  * Lưu bền vững `~/.openclaw` \+ `~/.openclaw/workspace` trên host (tồn tại sau khi khởi động lại/rebuild)
  * Truy cập Control UI từ laptop của bạn qua SSH tunnel


Trạng thái `~/.openclaw` được mount đó bao gồm `openclaw.json`, từng agent `agents/<agentId>/agent/auth-profiles.json`, và `.env`.

Gateway có thể được truy cập qua:

  * Chuyển tiếp cổng SSH từ laptop của bạn
  * Mở cổng trực tiếp nếu bạn tự quản lý firewall và token


Hướng dẫn này dùng Debian trên GCP Compute Engine. Ubuntu cũng hoạt động; hãy ánh xạ package tương ứng. Để xem luồng Docker chung, xem [Docker](</vi/install/docker>).

* * *

## Lộ trình nhanh (operator có kinh nghiệm)

  1. Tạo dự án GCP + bật Compute Engine API
  2. Tạo VM Compute Engine (e2-small, Debian 12, 20GB)
  3. SSH vào VM
  4. Cài đặt Docker
  5. Clone repository OpenClaw
  6. Tạo các thư mục host bền vững
  7. Cấu hình `.env` và `docker-compose.yml`
  8. Tích hợp các binary cần thiết, build và khởi chạy


* * *

## Bạn cần gì

  * Tài khoản GCP (đủ điều kiện free tier cho e2-micro)
  * Đã cài đặt gcloud CLI (hoặc dùng Cloud Console)
  * Quyền truy cập SSH từ laptop của bạn
  * Quen cơ bản với SSH + sao chép/dán
  * ~20-30 phút
  * Docker và Docker Compose
  * Thông tin xác thực model
  * Thông tin xác thực provider tùy chọn 
    * Mã QR WhatsApp
    * Token bot Telegram
    * Gmail OAuth


* * *

* ### Cài đặt gcloud CLI (hoặc dùng Console)

**Tùy chọn A: gcloud CLI** (khuyến nghị cho tự động hóa)

Cài đặt từ <https://cloud.google.com/sdk/docs/install>

Khởi tạo và xác thực:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Tùy chọn B: Cloud Console**

Tất cả các bước có thể thực hiện qua UI web tại <https://console.cloud.google.com>

* ### Tạo một dự án GCP

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Bật thanh toán tại <https://console.cloud.google.com/billing> (bắt buộc cho Compute Engine).

Bật Compute Engine API:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. Vào IAM & Admin > Create Project
  2. Đặt tên và tạo
  3. Bật thanh toán cho dự án
  4. Điều hướng đến APIs & Services > Enable APIs > tìm "Compute Engine API" > Enable


* ### Tạo VM

**Loại máy:**

Loại | Thông số | Chi phí | Ghi chú  
---|---|---|---  
e2-medium | 2 vCPU, 4GB RAM | ~$25/tháng | Đáng tin cậy nhất cho build Docker cục bộ  
e2-small | 2 vCPU, 2GB RAM | ~$12/tháng | Mức tối thiểu khuyến nghị cho build Docker  
e2-micro | 2 vCPU (shared), 1GB RAM | Đủ điều kiện free tier | Thường thất bại với OOM khi build Docker (exit 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. Vào Compute Engine > VM instances > Create instance
  2. Tên: `openclaw-gateway`
  3. Khu vực: `us-central1`, Zone: `us-central1-a`
  4. Loại máy: `e2-small`
  5. Boot disk: Debian 12, 20GB
  6. Tạo


* ### SSH vào VM

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

Nhấp nút "SSH" bên cạnh VM của bạn trong dashboard Compute Engine.

Lưu ý: Việc lan truyền khóa SSH có thể mất 1-2 phút sau khi tạo VM. Nếu kết nối bị từ chối, hãy chờ rồi thử lại.

* ### Cài đặt Docker (trên VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Đăng xuất rồi đăng nhập lại để thay đổi nhóm có hiệu lực:

bashCopy code
[code]
    exit
[/code]

Sau đó SSH lại vào:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

Xác minh:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone repository OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Hướng dẫn này giả định bạn sẽ build image tùy chỉnh để đảm bảo binary được lưu bền vững.

* ### Tạo các thư mục host bền vững

Docker container là tạm thời. Mọi trạng thái tồn tại lâu dài phải nằm trên host.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Cấu hình biến môi trường

Tạo `.env` ở root của repository.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Đặt `OPENCLAW_GATEWAY_TOKEN` khi bạn muốn quản lý token Gateway ổn định thông qua `.env`; nếu không, hãy cấu hình `gateway.auth.token` trước khi dựa vào client qua các lần khởi động lại. Nếu không có nguồn nào tồn tại, OpenClaw dùng token chỉ trong runtime cho lần khởi động đó. Tạo mật khẩu keyring và dán vào `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Không commit tệp này.**

Tệp `.env` này dành cho env container/runtime như `OPENCLAW_GATEWAY_TOKEN`. Auth OAuth/API-key của provider đã lưu nằm trong `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` được mount.

* ### Cấu hình Docker Compose

Tạo hoặc cập nhật `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` chỉ để tiện bootstrap, không phải thay thế cho cấu hình gateway đúng cách. Vẫn cần đặt auth (`gateway.auth.token` hoặc mật khẩu) và dùng thiết lập bind an toàn cho deployment của bạn.

* ### Các bước runtime VM Docker dùng chung

Dùng hướng dẫn runtime dùng chung cho luồng host Docker phổ biến:

  * [Tích hợp các binary cần thiết vào image](</vi/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Build và khởi chạy](</vi/install/docker-vm-runtime#build-and-launch>)
  * [Những gì được lưu bền vững ở đâu](</vi/install/docker-vm-runtime#what-persists-where>)
  * [Cập nhật](</vi/install/docker-vm-runtime#updates>)


* ### Ghi chú khởi chạy riêng cho GCP

Trên GCP, nếu build thất bại với `Killed` hoặc `exit code 137` trong lúc chạy `pnpm install --frozen-lockfile`, VM đã hết bộ nhớ. Dùng tối thiểu `e2-small`, hoặc `e2-medium` để các lần build đầu tiên đáng tin cậy hơn.

Khi bind vào LAN (`OPENCLAW_GATEWAY_BIND=lan`), hãy cấu hình origin trình duyệt đáng tin cậy trước khi tiếp tục:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Nếu bạn đã đổi cổng gateway, thay `18789` bằng cổng đã cấu hình.

* ### Truy cập từ laptop của bạn

Tạo SSH tunnel để chuyển tiếp cổng Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Mở trong trình duyệt của bạn:

`http://127.0.0.1:18789/`

In lại liên kết dashboard sạch:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Nếu UI yêu cầu auth bằng shared-secret, hãy dán token hoặc mật khẩu đã cấu hình vào thiết lập Control UI. Luồng Docker này ghi token theo mặc định; nếu bạn chuyển cấu hình container sang auth bằng mật khẩu, hãy dùng mật khẩu đó thay thế.

Nếu Control UI hiển thị `unauthorized` hoặc `disconnected (1008): pairing required`, hãy phê duyệt thiết bị trình duyệt:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Cần lại tham chiếu về lưu bền vững và cập nhật dùng chung? Xem [Docker VM Runtime](</vi/install/docker-vm-runtime#what-persists-where>) và [các cập nhật Docker VM Runtime](</vi/install/docker-vm-runtime#updates>).

* * *

## Khắc phục sự cố

**Kết nối SSH bị từ chối**

Việc lan truyền khóa SSH có thể mất 1-2 phút sau khi tạo VM. Hãy chờ rồi thử lại.

**Sự cố OS Login**

Kiểm tra hồ sơ OS Login của bạn:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Đảm bảo tài khoản của bạn có các quyền IAM bắt buộc (Compute OS Login hoặc Compute OS Admin Login).

**Hết bộ nhớ (OOM)**

Nếu build Docker thất bại với `Killed` và `exit code 137`, VM đã bị OOM-killed. Nâng cấp lên e2-small (tối thiểu) hoặc e2-medium (khuyến nghị để build cục bộ đáng tin cậy):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Service account (thực hành bảo mật tốt nhất)

Đối với sử dụng cá nhân, tài khoản người dùng mặc định của bạn hoạt động tốt.

Đối với tự động hóa hoặc pipeline CI/CD, hãy tạo một service account chuyên dụng với quyền tối thiểu:

  1. Tạo một service account:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Cấp vai trò Compute Instance Admin (hoặc vai trò tùy chỉnh hẹp hơn):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Tránh dùng vai trò Owner cho tự động hóa. Hãy áp dụng nguyên tắc đặc quyền tối thiểu.

Xem <https://cloud.google.com/iam/docs/understanding-roles> để biết chi tiết về vai trò IAM.

* * *

## Các bước tiếp theo

  * Thiết lập các kênh nhắn tin: [Kênh](</vi/channels>)
  * Ghép nối thiết bị cục bộ làm nút: [Nút](</vi/nodes>)
  * Cấu hình Gateway: [Cấu hình Gateway](</vi/gateway/configuration>)


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Azure](</vi/install/azure>)
  * [Lưu trữ VPS](</vi/vps>)


Was this useful?YesNo