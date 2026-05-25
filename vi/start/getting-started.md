---
title: Bắt đầu
source_url: https://docs.openclaw.ai/vi/start/getting-started
scraped_at: 2026-05-25
---

Cài đặt OpenClaw, chạy quy trình thiết lập ban đầu và trò chuyện với trợ lý AI của bạn — tất cả chỉ trong khoảng 5 phút. Khi hoàn tất, bạn sẽ có một Gateway đang chạy, xác thực đã được cấu hình, và một phiên trò chuyện hoạt động.

## Bạn cần có

  * **Node.js** — khuyến nghị Node 24 (cũng hỗ trợ Node 22.16+)
  * **Khóa API** từ một nhà cung cấp mô hình (Anthropic, OpenAI, Google, v.v.) — quy trình thiết lập ban đầu sẽ yêu cầu bạn nhập


## Thiết lập nhanh

* ### Cài đặt OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Quy trình tập lệnh cài đặt](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Chạy quy trình thiết lập ban đầu

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Trình hướng dẫn sẽ dẫn bạn qua việc chọn nhà cung cấp mô hình, đặt khóa API, và cấu hình Gateway. Quá trình này mất khoảng 2 phút.

Xem [Thiết lập ban đầu (CLI)](</vi/start/wizard>) để biết tài liệu tham khảo đầy đủ.

* ### Xác minh Gateway đang chạy

bashCopy code
[code]
    openclaw gateway status
[/code]

Bạn sẽ thấy Gateway đang lắng nghe trên cổng 18789.

* ### Mở bảng điều khiển

bashCopy code
[code]
    openclaw dashboard
[/code]

Lệnh này mở Control UI trong trình duyệt của bạn. Nếu trang tải được, mọi thứ đang hoạt động.

* ### Gửi tin nhắn đầu tiên

Nhập một tin nhắn trong cuộc trò chuyện của Control UI và bạn sẽ nhận được phản hồi từ AI.

Thay vào đó muốn trò chuyện từ điện thoại? Kênh nhanh nhất để thiết lập là [Telegram](</vi/channels/telegram>) (chỉ cần mã thông báo bot). Xem [Kênh](</vi/channels>) để biết tất cả tùy chọn.

Nâng cao: gắn một bản dựng Control UI tùy chỉnh

Nếu bạn duy trì một bản dựng bảng điều khiển đã bản địa hóa hoặc tùy chỉnh, hãy trỏ `gateway.controlUi.root` đến một thư mục chứa các tài sản tĩnh đã dựng và `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Sau đó đặt:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Khởi động lại Gateway và mở lại bảng điều khiển:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Việc cần làm tiếp theo

[**Kết nối một kênh** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, và nhiều kênh khác. ](</vi/channels>) [**Ghép nối và an toàn** Kiểm soát ai có thể nhắn tin cho agent của bạn. ](</vi/channels/pairing>) [**Cấu hình Gateway** Mô hình, công cụ, sandbox, và cài đặt nâng cao. ](</vi/gateway/configuration>) [**Duyệt công cụ** Trình duyệt, exec, tìm kiếm web, Skills, và Plugin. ](</vi/tools>)

Nâng cao: biến môi trường

Nếu bạn chạy OpenClaw bằng tài khoản dịch vụ hoặc muốn dùng đường dẫn tùy chỉnh:

  * `OPENCLAW_HOME` — thư mục chính để phân giải đường dẫn nội bộ
  * `OPENCLAW_STATE_DIR` — ghi đè thư mục trạng thái
  * `OPENCLAW_CONFIG_PATH` — ghi đè đường dẫn tệp cấu hình


Tài liệu tham khảo đầy đủ: [Biến môi trường](</vi/help/environment>).

## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [Tổng quan kênh](</vi/channels>)
  * [Thiết lập](</vi/start/setup>)


Was this useful?YesNo