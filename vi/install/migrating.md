---
title: Hướng dẫn di chuyển
source_url: https://docs.openclaw.ai/vi/install/migrating
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ ba lộ trình di chuyển: nhập từ một hệ thống agent khác, chuyển một bản cài đặt hiện có sang máy mới, và nâng cấp Plugin tại chỗ.

## Nhập từ một hệ thống agent khác

Dùng các nhà cung cấp di chuyển đi kèm để đưa hướng dẫn, máy chủ MCP, Skills, cấu hình mô hình và (tùy chọn) khóa API vào OpenClaw. Kế hoạch được xem trước trước khi có bất kỳ thay đổi nào, thông tin bí mật được che trong báo cáo, và thao tác áp dụng được hỗ trợ bằng bản sao lưu đã xác minh.

[**Di chuyển từ Claude** Nhập trạng thái Claude Code và Claude Desktop, bao gồm `CLAUDE.md`, máy chủ MCP, Skills và lệnh dự án. ](</vi/install/migrating-claude>) [**Di chuyển từ Hermes** Nhập cấu hình Hermes, nhà cung cấp, máy chủ MCP, bộ nhớ, Skills và các khóa `.env` được hỗ trợ. ](</vi/install/migrating-hermes>)

Điểm vào CLI là [`openclaw migrate`](</vi/cli/migrate>). Quy trình thiết lập ban đầu cũng có thể đề xuất di chuyển khi phát hiện một nguồn đã biết (`openclaw onboard --flow import`).

## Chuyển OpenClaw sang máy mới

Sao chép **thư mục trạng thái** (`~/.openclaw/` theo mặc định) và **không gian làm việc** của bạn để giữ lại:

  * **Cấu hình** — `openclaw.json` và toàn bộ cài đặt Gateway.
  * **Xác thực** — `auth-profiles.json` theo từng agent (khóa API cùng OAuth), cộng với mọi trạng thái kênh hoặc nhà cung cấp trong `credentials/`.
  * **Phiên** — lịch sử hội thoại và trạng thái agent.
  * **Trạng thái kênh** — đăng nhập WhatsApp, phiên Telegram và các trạng thái tương tự.
  * **Tệp trong không gian làm việc** — `MEMORY.md`, `USER.md`, Skills và prompt.


### Các bước di chuyển

* ### Dừng Gateway và sao lưu

Trên máy **cũ** , dừng Gateway để tệp không thay đổi trong lúc sao chép, rồi tạo bản lưu trữ:

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

Nếu bạn dùng nhiều hồ sơ (ví dụ `~/.openclaw-work`), hãy lưu trữ từng hồ sơ riêng.

* ### Cài đặt OpenClaw trên máy mới

[Cài đặt](</vi/install>) CLI (và Node nếu cần) trên máy mới. Không sao nếu quy trình thiết lập ban đầu tạo một `~/.openclaw/` mới. Bạn sẽ ghi đè nó ở bước tiếp theo.

* ### Sao chép thư mục trạng thái và không gian làm việc

Chuyển bản lưu trữ qua `scp`, `rsync -a` hoặc ổ đĩa ngoài, rồi giải nén:

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

Đảm bảo các thư mục ẩn đã được bao gồm và quyền sở hữu tệp khớp với người dùng sẽ chạy Gateway.

* ### Chạy doctor và xác minh

Trên máy mới, chạy [Doctor](</vi/gateway/doctor>) để áp dụng các di chuyển cấu hình và sửa chữa dịch vụ:

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

Nếu Telegram hoặc Discord dùng phương án dự phòng biến môi trường mặc định (`TELEGRAM_BOT_TOKEN` hoặc `DISCORD_BOT_TOKEN`), hãy xác minh tệp `.env` trong thư mục trạng thái đã di chuyển có chứa các khóa đó mà không in giá trị bí mật:

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` cũng cảnh báo khi một tài khoản Telegram hoặc Discord mặc định đang bật không có token đã cấu hình và biến môi trường tương ứng không khả dụng với tiến trình doctor.

### Lỗi thường gặp

Không khớp hồ sơ hoặc thư mục trạng thái

Nếu Gateway cũ dùng `--profile` hoặc `OPENCLAW_STATE_DIR` còn Gateway mới thì không, các kênh sẽ có vẻ như đã đăng xuất và phiên sẽ trống. Khởi chạy Gateway với **cùng** hồ sơ hoặc thư mục trạng thái mà bạn đã di chuyển, rồi chạy lại `openclaw doctor`.

Chỉ sao chép openclaw.json

Chỉ riêng tệp cấu hình là chưa đủ. Hồ sơ xác thực mô hình nằm trong `agents/<agentId>/agent/auth-profiles.json`, còn trạng thái kênh và nhà cung cấp nằm trong `credentials/`. Luôn di chuyển **toàn bộ** thư mục trạng thái.

Quyền và quyền sở hữu

Nếu bạn sao chép với quyền root hoặc đổi người dùng, Gateway có thể không đọc được thông tin xác thực. Hãy đảm bảo thư mục trạng thái và không gian làm việc thuộc sở hữu của người dùng chạy Gateway.

Chế độ từ xa

Nếu UI của bạn trỏ tới một Gateway **từ xa** , máy chủ từ xa sở hữu phiên và không gian làm việc. Hãy di chuyển chính máy chủ Gateway, không phải laptop cục bộ của bạn. Xem [FAQ](</vi/help/faq#where-things-live-on-disk>).

Thông tin bí mật trong bản sao lưu

Thư mục trạng thái chứa hồ sơ xác thực, thông tin xác thực kênh và trạng thái nhà cung cấp khác. Lưu trữ bản sao lưu dưới dạng mã hóa, tránh các kênh truyền không an toàn, và xoay vòng khóa nếu bạn nghi ngờ đã bị lộ.

### Danh sách kiểm tra xác minh

Trên máy mới, xác nhận:

  * [ ] `openclaw status` cho thấy Gateway đang chạy.
  * [ ] Các kênh vẫn được kết nối (không cần ghép nối lại).
  * [ ] Bảng điều khiển mở được và hiển thị các phiên hiện có.
  * [ ] Tệp trong không gian làm việc (bộ nhớ, cấu hình) hiện diện.


## Nâng cấp Plugin tại chỗ

Nâng cấp Plugin tại chỗ giữ nguyên cùng id Plugin và khóa cấu hình nhưng có thể chuyển trạng thái trên đĩa vào cấu trúc hiện tại. Hướng dẫn nâng cấp theo từng Plugin nằm cùng với các kênh của chúng:

  * [Di chuyển Matrix](</vi/channels/matrix-migration>): giới hạn khôi phục trạng thái mã hóa, hành vi chụp nhanh tự động và lệnh khôi phục thủ công.


## Liên quan

  * [`openclaw migrate`](</vi/cli/migrate>): tham chiếu CLI cho nhập liên hệ thống.
  * [Tổng quan cài đặt](</vi/install>): tất cả phương thức cài đặt.
  * [Doctor](</vi/gateway/doctor>): kiểm tra tình trạng sau di chuyển.
  * [Gỡ cài đặt](</vi/install/uninstall>): gỡ OpenClaw sạch sẽ.


Was this useful?YesNo