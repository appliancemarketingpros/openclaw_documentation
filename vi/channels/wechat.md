---
title: WeChat
source_url: https://docs.openclaw.ai/vi/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw kết nối với WeChat thông qua Plugin kênh bên ngoài `@tencent-weixin/openclaw-weixin` của Tencent.

Trạng thái: Plugin bên ngoài. Trò chuyện trực tiếp và phương tiện được hỗ trợ. Trò chuyện nhóm không được metadata năng lực Plugin hiện tại quảng bá.

## Cách đặt tên

  * **WeChat** là tên hiển thị với người dùng trong các tài liệu này.
  * **Weixin** là tên được gói của Tencent và id Plugin sử dụng.
  * `openclaw-weixin` là id kênh OpenClaw.
  * `@tencent-weixin/openclaw-weixin` là gói npm.


Dùng `openclaw-weixin` trong các lệnh CLI và đường dẫn cấu hình.

## Cách hoạt động

Mã WeChat không nằm trong repo lõi OpenClaw. OpenClaw cung cấp hợp đồng Plugin kênh chung, còn Plugin bên ngoài cung cấp runtime dành riêng cho WeChat:

  1. `openclaw plugins install` cài đặt `@tencent-weixin/openclaw-weixin`.
  2. Gateway phát hiện manifest Plugin và tải entrypoint của Plugin.
  3. Plugin đăng ký id kênh `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` bắt đầu đăng nhập bằng QR.
  5. Plugin lưu thông tin xác thực tài khoản trong thư mục trạng thái OpenClaw.
  6. Khi Gateway khởi động, Plugin khởi động trình giám sát Weixin cho từng tài khoản đã cấu hình.
  7. Tin nhắn WeChat đến được chuẩn hóa thông qua hợp đồng kênh, được định tuyến đến tác tử OpenClaw đã chọn, rồi được gửi lại qua đường dẫn gửi ra của Plugin.


Sự tách biệt đó rất quan trọng: lõi OpenClaw nên không phụ thuộc kênh. Đăng nhập WeChat, lệnh gọi API Tencent iLink, tải lên/tải xuống phương tiện, token ngữ cảnh và giám sát tài khoản đều thuộc trách nhiệm của Plugin bên ngoài.

## Cài đặt

Cài đặt nhanh:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Cài đặt thủ công:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Khởi động lại Gateway sau khi cài đặt:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Đăng nhập

Chạy đăng nhập bằng QR trên cùng máy đang chạy Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Quét mã QR bằng WeChat trên điện thoại của bạn và xác nhận đăng nhập. Plugin lưu token tài khoản cục bộ sau khi quét thành công.

Để thêm tài khoản WeChat khác, chạy lại cùng lệnh đăng nhập. Với nhiều tài khoản, hãy cô lập phiên tin nhắn trực tiếp theo tài khoản, kênh và người gửi:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Kiểm soát truy cập

Tin nhắn trực tiếp dùng mô hình ghép nối và danh sách cho phép OpenClaw thông thường cho Plugin kênh.

Phê duyệt người gửi mới:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Để xem đầy đủ mô hình kiểm soát truy cập, xem [Ghép nối](</vi/channels/pairing>).

## Tương thích

Plugin kiểm tra phiên bản OpenClaw của máy chủ khi khởi động.

Dòng Plugin | Phiên bản OpenClaw | Thẻ npm  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Nếu Plugin báo rằng phiên bản OpenClaw của bạn quá cũ, hãy cập nhật OpenClaw hoặc cài đặt dòng Plugin legacy:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Tiến trình sidecar

Plugin WeChat có thể chạy công việc trợ giúp bên cạnh Gateway trong khi giám sát API Tencent iLink. Trong issue #68451, đường dẫn trợ giúp đó làm lộ một lỗi trong cơ chế dọn dẹp Gateway cũ chung của OpenClaw: một tiến trình con có thể cố gắng dọn dẹp tiến trình Gateway cha, gây vòng lặp khởi động lại dưới các trình quản lý tiến trình như systemd.

Cơ chế dọn dẹp khi khởi động hiện tại của OpenClaw loại trừ tiến trình hiện tại và các tiến trình tổ tiên của nó, vì vậy một trình trợ giúp kênh không được giết Gateway đã khởi chạy nó. Bản sửa này là chung; đây không phải là đường dẫn dành riêng cho WeChat trong lõi.

## Khắc phục sự cố

Kiểm tra cài đặt và trạng thái:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Nếu kênh hiển thị là đã cài đặt nhưng không kết nối, hãy xác nhận rằng Plugin đã được bật rồi khởi động lại:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Nếu Gateway khởi động lại liên tục sau khi bật WeChat, hãy cập nhật cả OpenClaw và Plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Nếu khi khởi động báo rằng gói Plugin đã cài đặt `requires compiled runtime output for TypeScript entry`, gói npm đã được phát hành mà không có các tệp runtime JavaScript đã biên dịch mà OpenClaw cần. Hãy cập nhật/cài đặt lại sau khi nhà phát hành Plugin phát hành gói đã sửa, hoặc tạm thời tắt/gỡ cài đặt Plugin.

Tạm thời tắt:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Tài liệu liên quan

  * Tổng quan kênh: [Kênh trò chuyện](</vi/channels>)
  * Ghép nối: [Ghép nối](</vi/channels/pairing>)
  * Định tuyến kênh: [Định tuyến kênh](</vi/channels/channel-routing>)
  * Kiến trúc Plugin: [Kiến trúc Plugin](</vi/plugins/architecture>)
  * SDK Plugin kênh: [SDK Plugin kênh](</vi/plugins/sdk-channel-plugins>)
  * Gói bên ngoài: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo