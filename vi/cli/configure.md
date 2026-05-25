---
title: Cấu hình
source_url: https://docs.openclaw.ai/vi/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Lời nhắc tương tác để thực hiện các thay đổi có mục tiêu cho một thiết lập hiện có: thông tin xác thực, thiết bị, mặc định của agent, Gateway, kênh, plugin, Skills và kiểm tra tình trạng.

Dùng `openclaw onboard` cho hành trình chạy lần đầu có hướng dẫn đầy đủ, `openclaw setup` chỉ cho cấu hình/không gian làm việc cơ sở, và `openclaw channels add` khi bạn chỉ cần thiết lập tài khoản kênh.

Khi configure bắt đầu từ một lựa chọn xác thực nhà cung cấp, các bộ chọn mô hình mặc định và danh sách cho phép sẽ tự động ưu tiên nhà cung cấp đó. Với các nhà cung cấp ghép cặp như Volcengine và BytePlus, cùng tùy chọn ưu tiên đó cũng khớp với các biến thể kế hoạch lập trình của họ (`volcengine-plan/*`, `byteplus-plan/*`). Nếu bộ lọc nhà cung cấp ưu tiên tạo ra một danh sách trống, configure sẽ quay lại danh mục không lọc thay vì hiển thị một bộ chọn trống.

Đối với tìm kiếm web, `openclaw configure --section web` cho phép bạn chọn một nhà cung cấp và cấu hình thông tin xác thực của nhà cung cấp đó. Một số nhà cung cấp cũng hiển thị các lời nhắc tiếp theo dành riêng cho nhà cung cấp:

  * **Grok** có thể cung cấp thiết lập `x_search` tùy chọn với cùng `XAI_API_KEY` và cho phép bạn chọn một mô hình `x_search`.
  * **Kimi** có thể hỏi vùng API Moonshot (`api.moonshot.ai` so với `api.moonshot.cn`) và mô hình tìm kiếm web Kimi mặc định.


Liên quan:

  * Tham chiếu cấu hình Gateway: [Cấu hình](</vi/gateway/configuration>)
  * CLI cấu hình: [Cấu hình](</vi/cli/config>)


## Tùy chọn

  * `--section <section>`: bộ lọc phần có thể lặp lại


Các phần khả dụng:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Ghi chú:

  * Việc chọn nơi Gateway chạy luôn cập nhật `gateway.mode`. Bạn có thể chọn "Tiếp tục" mà không chọn các phần khác nếu đó là tất cả những gì bạn cần.
  * Sau khi ghi cấu hình cục bộ, configure sẽ cài đặt các plugin có thể tải xuống đã chọn khi đường dẫn thiết lập được chọn yêu cầu chúng. Cấu hình gateway từ xa không cài đặt các gói plugin cục bộ.
  * Các dịch vụ hướng kênh (Slack/Discord/Matrix/Microsoft Teams) sẽ nhắc nhập danh sách cho phép kênh/phòng trong quá trình thiết lập. Bạn có thể nhập tên hoặc ID; trình hướng dẫn sẽ phân giải tên thành ID khi có thể.
  * Nếu bạn chạy bước cài đặt daemon, xác thực bằng token yêu cầu một token, và `gateway.auth.token` được quản lý bằng SecretRef, configure sẽ xác thực SecretRef nhưng không lưu các giá trị token văn bản thuần đã phân giải vào siêu dữ liệu môi trường dịch vụ supervisor.
  * Nếu xác thực bằng token yêu cầu một token và SecretRef token đã cấu hình chưa được phân giải, configure sẽ chặn cài đặt daemon với hướng dẫn khắc phục có thể thực hiện.
  * Nếu cả `gateway.auth.token` và `gateway.auth.password` đều được cấu hình và `gateway.auth.mode` chưa được đặt, configure sẽ chặn cài đặt daemon cho đến khi mode được đặt rõ ràng.


## Ví dụ

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Cấu hình](</vi/gateway/configuration>)


Was this useful?YesNo