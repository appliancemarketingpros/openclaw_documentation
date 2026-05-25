---
title: Máy ảo macOS
source_url: https://docs.openclaw.ai/vi/install/macos-vm
scraped_at: 2026-05-25
---

## Mặc định được khuyến nghị (hầu hết người dùng)

  * **VPS Linux nhỏ** cho Gateway luôn bật và chi phí thấp. Xem [lưu trữ VPS](</vi/vps>).
  * **Phần cứng chuyên dụng** (Mac mini hoặc máy Linux) nếu bạn muốn toàn quyền kiểm soát và **IP dân cư** cho tự động hóa trình duyệt. Nhiều trang chặn IP trung tâm dữ liệu, nên duyệt cục bộ thường hoạt động tốt hơn.
  * **Kết hợp:** giữ Gateway trên một VPS giá rẻ, và kết nối Mac của bạn làm **Node** khi bạn cần tự động hóa trình duyệt/UI. Xem [Node](</vi/nodes>) và [Gateway từ xa](</vi/gateway/remote>).


Dùng VM macOS khi bạn đặc biệt cần các khả năng chỉ có trên macOS như iMessage hoặc muốn cách ly nghiêm ngặt khỏi máy Mac dùng hằng ngày.

## Tùy chọn VM macOS

### VM cục bộ trên Apple Silicon Mac của bạn (Lume)

Chạy OpenClaw trong một VM macOS dạng sandbox trên Apple Silicon Mac hiện có của bạn bằng [Lume](<https://cua.ai/docs/lume>).

Cách này cho bạn:

  * Môi trường macOS đầy đủ trong trạng thái cách ly (máy chủ của bạn vẫn sạch)
  * Hỗ trợ iMessage qua `imsg` (đường dẫn cục bộ mặc định là không thể trên Linux/Windows)
  * Đặt lại tức thì bằng cách nhân bản VM
  * Không cần thêm phần cứng hoặc chi phí đám mây


### Nhà cung cấp Mac lưu trữ (đám mây)

Nếu bạn muốn macOS trên đám mây, các nhà cung cấp Mac lưu trữ cũng hoạt động:

  * [MacStadium](<https://www.macstadium.com/>) (Mac được lưu trữ)
  * Các nhà cung cấp Mac lưu trữ khác cũng hoạt động; làm theo tài liệu VM + SSH của họ


Khi đã có quyền truy cập SSH vào VM macOS, tiếp tục ở bước 6 bên dưới.

* * *

## Đường dẫn nhanh (Lume, người dùng có kinh nghiệm)

  1. Cài đặt Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. Hoàn tất Setup Assistant, bật Remote Login (SSH)
  4. `lume run openclaw --no-display`
  5. SSH vào, cài đặt OpenClaw, cấu hình các kênh
  6. Xong


* * *

## Bạn cần gì (Lume)

  * Apple Silicon Mac (M1/M2/M3/M4)
  * macOS Sequoia hoặc mới hơn trên máy chủ
  * Khoảng 60 GB dung lượng đĩa trống cho mỗi VM
  * Khoảng 20 phút


* * *

## 1) Cài đặt Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

Nếu `~/.local/bin` không có trong PATH của bạn:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

Xác minh:

bashCopy code
[code]
    lume --version
[/code]

Tài liệu: [Cài đặt Lume](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) Tạo VM macOS

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

Lệnh này tải macOS xuống và tạo VM. Một cửa sổ VNC sẽ tự động mở.

* * *

## 3) Hoàn tất Setup Assistant

Trong cửa sổ VNC:

  1. Chọn ngôn ngữ và khu vực
  2. Bỏ qua Apple ID (hoặc đăng nhập nếu sau này bạn muốn dùng iMessage)
  3. Tạo tài khoản người dùng (ghi nhớ tên người dùng và mật khẩu)
  4. Bỏ qua mọi tính năng tùy chọn


Sau khi thiết lập hoàn tất, bật SSH:

  1. Mở System Settings → General → Sharing
  2. Bật "Remote Login"


* * *

## 4) Lấy địa chỉ IP của VM

bashCopy code
[code]
    lume get openclaw
[/code]

Tìm địa chỉ IP (thường là `192.168.64.x`).

* * *

## 5) SSH vào VM

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

Thay `youruser` bằng tài khoản bạn đã tạo, và IP bằng IP của VM.

* * *

## 6) Cài đặt OpenClaw

Bên trong VM:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Làm theo các lời nhắc onboarding để thiết lập nhà cung cấp mô hình của bạn (Anthropic, OpenAI, v.v.).

* * *

## 7) Cấu hình kênh

Chỉnh sửa tệp cấu hình:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

Thêm các kênh của bạn:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

Sau đó đăng nhập vào WhatsApp (quét QR):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) Chạy VM không có giao diện hiển thị

Dừng VM và khởi động lại không có màn hình:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

VM chạy trong nền. Daemon của OpenClaw giữ cho gateway tiếp tục chạy.

Để kiểm tra trạng thái:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## Bổ sung: tích hợp iMessage

Đây là tính năng nổi bật nhất khi chạy trên macOS. Dùng [iMessage](</vi/channels/imessage>) với `imsg` để thêm Messages vào OpenClaw.

Bên trong VM:

  1. Đăng nhập vào Messages.
  2. Cài đặt `imsg`.
  3. Cấp quyền Full Disk Access và Automation cho tiến trình đang chạy OpenClaw/`imsg`.
  4. Xác minh hỗ trợ RPC bằng `imsg rpc --help`.


Thêm vào cấu hình OpenClaw của bạn:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

Khởi động lại gateway. Giờ đây tác nhân của bạn có thể gửi và nhận iMessage.

Chi tiết thiết lập đầy đủ: [kênh iMessage](</vi/channels/imessage>)

* * *

## Lưu một image chuẩn

Trước khi tùy chỉnh thêm, chụp nhanh trạng thái sạch của bạn:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

Đặt lại bất cứ lúc nào:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## Chạy 24/7

Giữ VM chạy bằng cách:

  * Luôn cắm nguồn cho Mac của bạn
  * Tắt chế độ ngủ trong System Settings → Energy Saver
  * Dùng `caffeinate` nếu cần


Để thật sự luôn bật, hãy cân nhắc một Mac mini chuyên dụng hoặc một VPS nhỏ. Xem [lưu trữ VPS](</vi/vps>).

* * *

## Khắc phục sự cố

Vấn đề | Giải pháp  
---|---  
Không thể SSH vào VM | Kiểm tra "Remote Login" đã được bật trong System Settings của VM  
IP của VM không hiển thị | Chờ VM khởi động hoàn toàn, chạy lại `lume get openclaw`  
Không tìm thấy lệnh Lume | Thêm `~/.local/bin` vào PATH của bạn  
QR WhatsApp không quét được | Đảm bảo bạn đã đăng nhập vào VM (không phải máy chủ) khi chạy `openclaw channels login`  
  
* * *

## Tài liệu liên quan

  * [lưu trữ VPS](</vi/vps>)
  * [Node](</vi/nodes>)
  * [Gateway từ xa](</vi/gateway/remote>)
  * [kênh iMessage](</vi/channels/imessage>)
  * [Lume Quickstart](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Tham chiếu CLI Lume](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [Thiết lập VM không cần giám sát](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (nâng cao)
  * [Sandboxing bằng Docker](</vi/install/docker>) (cách cách ly thay thế)


Was this useful?YesNo