---
title: Di chuyển từ Hermes
source_url: https://docs.openclaw.ai/vi/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw nhập trạng thái Hermes thông qua một nhà cung cấp di chuyển được đóng gói kèm. Nhà cung cấp này xem trước mọi thứ trước khi thay đổi trạng thái, biên tập bí mật trong kế hoạch và báo cáo, đồng thời tạo một bản sao lưu đã xác minh trước khi áp dụng.

## Hai cách để nhập

### Trình hướng dẫn thiết lập ban đầu

Cách nhanh nhất. Trình hướng dẫn phát hiện Hermes tại `~/.hermes` và hiển thị bản xem trước trước khi áp dụng.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Hoặc trỏ tới một nguồn cụ thể:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Dùng `openclaw migrate` cho các lần chạy theo script hoặc có thể lặp lại. Xem [`openclaw migrate`](</vi/cli/migrate>) để biết tài liệu tham khảo đầy đủ.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Thêm `--from <path>` khi Hermes nằm ngoài `~/.hermes`.

## Những gì được nhập

Cấu hình mô hình

  * Lựa chọn mô hình mặc định từ `config.yaml` của Hermes.
  * Các nhà cung cấp mô hình đã cấu hình và endpoint tùy chỉnh tương thích với OpenAI từ `providers` và `custom_providers`.

Máy chủ MCP

Định nghĩa máy chủ MCP từ `mcp_servers` hoặc `mcp.servers`.

Tệp không gian làm việc

  * `SOUL.md` và `AGENTS.md` được sao chép vào không gian làm việc tác nhân OpenClaw.
  * `memories/MEMORY.md` và `memories/USER.md` được **nối thêm** vào các tệp bộ nhớ OpenClaw tương ứng thay vì ghi đè lên chúng.

Cấu hình bộ nhớ

Các mặc định cấu hình bộ nhớ cho bộ nhớ tệp OpenClaw. Các nhà cung cấp bộ nhớ bên ngoài như Honcho được ghi nhận dưới dạng mục lưu trữ hoặc mục cần xem xét thủ công để bạn có thể di chuyển chúng một cách có chủ đích.

Skills

Skills có tệp `SKILL.md` dưới `skills/<name>/` được sao chép, cùng với các giá trị cấu hình riêng cho từng Skill từ `skills.config`.

Khóa API (chọn tham gia)

Đặt `--include-secrets` để nhập các khóa `.env` được hỗ trợ: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Nếu không có cờ này, bí mật sẽ không bao giờ được sao chép.

## Những gì chỉ được lưu trữ

Nhà cung cấp sao chép các mục này vào thư mục báo cáo di chuyển để xem xét thủ công, nhưng **không** nạp chúng vào cấu hình hoặc thông tin xác thực OpenClaw đang hoạt động:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw từ chối tự động thực thi hoặc tin cậy trạng thái này vì định dạng và giả định tin cậy có thể lệch nhau giữa các hệ thống. Hãy di chuyển thủ công những gì bạn cần sau khi xem xét bản lưu trữ.

## Quy trình được khuyến nghị

* ### Xem trước kế hoạch

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Kế hoạch liệt kê mọi thứ sẽ thay đổi, bao gồm xung đột, mục bị bỏ qua và mọi mục nhạy cảm. Đầu ra kế hoạch biên tập các khóa lồng nhau trông giống bí mật.

* ### Áp dụng kèm sao lưu

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw tạo và xác minh một bản sao lưu trước khi áp dụng. Nếu bạn cần nhập khóa API, hãy thêm `--include-secrets`.

* ### Chạy doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</vi/gateway/doctor>) áp dụng lại mọi di chuyển cấu hình đang chờ và kiểm tra các vấn đề được đưa vào trong quá trình nhập.

* ### Khởi động lại và xác minh

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Xác nhận Gateway hoạt động ổn định và mô hình, bộ nhớ, cùng Skills đã nhập của bạn đã được nạp.

## Xử lý xung đột

Áp dụng sẽ từ chối tiếp tục khi kế hoạch báo cáo xung đột (một tệp hoặc giá trị cấu hình đã tồn tại tại đích).

Đối với bản cài đặt OpenClaw mới, xung đột là bất thường. Chúng thường xuất hiện khi bạn chạy lại quá trình nhập trên một thiết lập đã có chỉnh sửa của người dùng.

Nếu xung đột xuất hiện giữa quá trình áp dụng (ví dụ: một cuộc chạy đua ngoài dự kiến trên tệp cấu hình), Hermes đánh dấu các mục cấu hình phụ thuộc còn lại là `skipped` với lý do `blocked by earlier apply conflict` thay vì ghi chúng một phần. Báo cáo di chuyển ghi lại từng mục bị chặn để bạn có thể giải quyết xung đột gốc và chạy lại quá trình nhập.

## Bí mật

Bí mật không bao giờ được nhập theo mặc định.

  * Trước tiên hãy chạy `openclaw migrate apply hermes --yes` để nhập trạng thái không phải bí mật.
  * Nếu bạn cũng muốn sao chép các khóa `.env` được hỗ trợ sang, hãy chạy lại với `--include-secrets`.
  * Đối với thông tin xác thực do SecretRef quản lý, hãy cấu hình nguồn SecretRef sau khi quá trình nhập hoàn tất.


## Đầu ra JSON cho tự động hóa

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Với `--json` và không có `--yes`, lệnh áp dụng in kế hoạch và không thay đổi trạng thái. Đây là chế độ an toàn nhất cho CI và script dùng chung.

## Khắc phục sự cố

Áp dụng từ chối do xung đột

Kiểm tra đầu ra kế hoạch. Mỗi xung đột xác định đường dẫn nguồn và đích hiện có. Quyết định cho từng mục nên bỏ qua, chỉnh sửa đích, hay chạy lại với `--overwrite`.

Hermes nằm ngoài ~/.hermes

Truyền `--from /actual/path` (CLI) hoặc `--import-source /actual/path` (thiết lập ban đầu).

Thiết lập ban đầu từ chối nhập trên một thiết lập hiện có

Nhập qua thiết lập ban đầu yêu cầu một thiết lập mới. Hãy đặt lại trạng thái và thiết lập lại từ đầu, hoặc dùng trực tiếp `openclaw migrate apply hermes`, lệnh này hỗ trợ `--overwrite` và kiểm soát sao lưu rõ ràng.

Khóa API không được nhập

Bắt buộc có `--include-secrets`, và chỉ các khóa được liệt kê ở trên mới được nhận diện. Các biến khác trong `.env` bị bỏ qua.

## Liên quan

  * [`openclaw migrate`](</vi/cli/migrate>): tài liệu tham khảo CLI đầy đủ, hợp đồng Plugin và hình dạng JSON.
  * [Thiết lập ban đầu](</vi/cli/onboard>): luồng trình hướng dẫn và các cờ không tương tác.
  * [Di chuyển](</vi/install/migrating>): di chuyển một bản cài đặt OpenClaw giữa các máy.
  * [Doctor](</vi/gateway/doctor>): kiểm tra sức khỏe sau di chuyển.
  * [Không gian làm việc tác nhân](</vi/concepts/agent-workspace>): nơi đặt `SOUL.md`, `AGENTS.md` và các tệp bộ nhớ.


Was this useful?YesNo