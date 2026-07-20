---
title: Hoạt động trên Discord
source_url: https://docs.openclaw.ai/vi/channels/discord-activities
scraped_at: 2026-07-20
---

ChannelsMainstream messaging

Discord Activities cho phép một agent đăng tiện ích HTML tương tác, độc lập vào kênh Discord hiện tại. Tin nhắn có nút **Open widget** ; khi nhấp vào, tiện ích sẽ được khởi chạy bên trong Discord.

Tính năng này mặc định bị tắt. OpenClaw chỉ đăng ký các tuyến HTTP của Activity, công cụ agent `show_widget` và trình xử lý nút khởi chạy khi có `channels.discord.activities` và phân giải được client secret. Bí danh `discord_widget` đã ngừng dùng vẫn được duy trì trong một bản phát hành.

## Điều kiện tiên quyết

  * một [bot Discord OpenClaw](</vi/channels/discord>) hiện có
  * một tên máy chủ HTTPS công khai có thể truy cập Gateway OpenClaw
  * quyền cấu hình Activities và OAuth2 cho ứng dụng Discord của bot


Có thể sử dụng bất kỳ reverse proxy hoặc tunnel HTTPS nào. Cloudflare Tunnel có tên cung cấp tên máy chủ ổn định mà không để lộ trực tiếp cổng Gateway.

yamlCopy code
[code]
    # ~/.cloudflared/config.ymltunnel: openclaw-discordcredentials-file: /home/you/.cloudflared/TUNNEL-ID.jsoningress:  - hostname: openclaw.example.com    service: http://127.0.0.1:18789  - service: http_status:404
[/code]

bashCopy code
[code]
    cloudflared tunnel logincloudflared tunnel create openclaw-discordcloudflared tunnel route dns openclaw-discord openclaw.example.comcloudflared tunnel run openclaw-discord
[/code]

Hãy giữ bật cơ chế xác thực Gateway thông thường. Chỉ tiền tố Activity là công khai, còn Plugin tự xác thực OAuth, tư cách thành viên của phiên bản Activity, liên kết kênh, phiên và các quyền truy cập tài liệu dùng một lần.

## Thiết lập

* ### Công khai Gateway qua HTTPS

Khởi động tunnel hoặc reverse proxy và xác minh rằng `https://openclaw.example.com/discord/activity/` truy cập được Gateway sau khi thêm cấu hình Activities. Thay tên máy chủ ví dụ bằng tên máy chủ của bạn.

* ### Bật Activities trong Discord

Mở ứng dụng bot hiện có trong [Discord Developer Portal](<https://discord.com/developers/applications>). Mở **Activities** , bật Activities và tạo ánh xạ URL:

  * tiền tố: `ROOT` (`/`)
  * đích: `openclaw.example.com/discord/activity`


Đích là tên máy chủ công khai cộng với `/discord/activity`, không có dấu gạch chéo ở cuối.

* ### Sao chép OAuth2 client secret

Mở **OAuth2** trong Developer Portal. Discord yêu cầu ít nhất một URI chuyển hướng, vì vậy hãy thêm một giá trị giữ chỗ cục bộ, chẳng hạn như địa chỉ loopback, nếu ứng dụng chưa có; Embedded App SDK xử lý luồng trả về của Activity. Sao chép hoặc đặt lại client secret của ứng dụng. Hãy coi đây là thông tin xác thực: không dán vào cuộc trò chuyện, nhật ký hoặc tệp cấu hình được commit.

* ### Cấu hình OpenClaw

Thêm một khối vào tài khoản Discord cần cung cấp tiện ích:

json5Copy code
[code]
    {  channels: {    discord: {      token: "${DISCORD_BOT_TOKEN}",      activities: {        clientSecret: "${DISCORD_CLIENT_SECRET}",        // Không bắt buộc. Mặc định là ID ứng dụng bot được xác định khi khởi động.        applicationId: "YOUR_DISCORD_APPLICATION_ID",      },    },  },}
[/code]

Có thể bỏ `clientSecret` khỏi khối khi `DISCORD_CLIENT_SECRET` đã được đặt. Bản thân khối này phải được giữ lại để thể hiện lựa chọn bật tính năng.

Các thiết lập quyền truy cập Discord thông thường vẫn tách biệt. Ví dụ: `allowFrom` vẫn kiểm soát ai có thể gửi tin nhắn trực tiếp cho agent; thiết lập này không kiểm soát ai có thể mở tiện ích đã được đăng trong một kênh.

* ### Khởi động lại và kiểm thử

Khởi động lại Gateway. Trong một cuộc trò chuyện Discord, yêu cầu agent hiển thị tiện ích tương tác. Agent gọi `show_widget`; nhấp vào **Open widget** trong tin nhắn đã đăng.

## Mô hình bảo mật

  * OAuth xác định người dùng Discord trước khi trả về siêu dữ liệu của tiện ích.
  * API Get Activity Instance của Discord phải xác nhận rằng người dùng OAuth có mặt trong phiên bản Activity hiện tại. Kênh của phiên bản phải khớp với kênh nơi tiện ích được đăng.
  * Mọi người được Discord cho phép vào kênh đó đều có thể mở các tiện ích của kênh. Để thu hẹp đối tượng, hãy sử dụng quyền kênh Discord. Danh sách cho phép đối với lệnh và tin nhắn trực tiếp của OpenClaw không cấp hoặc thu hồi quyền truy cập vào nội dung kênh đã đăng.
  * Phiên OAuth hết hạn sau 15 phút. Quyền truy cập tài liệu tiện ích hết hạn sau 60 giây và chỉ hoạt động một lần.
  * Tiện ích hết hạn sau bảy ngày và mỗi phiên bản Plugin Discord giữ lại tối đa 64 tiện ích.
  * HTML của tiện ích do agent của bạn tạo và cần được coi là nội dung đáng tin cậy. Không nhúng các bí mật mà bạn không muốn một tiện ích có lỗi làm lộ.
  * Tiện ích có thể điều hướng trong khung lồng nhau của chính nó. iframe `sandbox="allow-scripts"` chặn điều hướng cấp cao nhất, cửa sổ bật lên và quyền truy cập cùng nguồn, còn Chính sách bảo mật nội dung của iframe chặn các kết nối mạng và tài nguyên bên ngoài. Các biện pháp kiểm soát này là lớp phòng thủ bổ sung, không phải ranh giới bảo mật chống lại agent đã tạo tiện ích.
  * Khi Activities bị tắt, `/discord/activity` hoàn toàn không được đăng ký.


Shell Activity công khai và tuyến trao đổi token có thể được truy cập qua tunnel của bạn khi tính năng được bật. Chúng không để lộ HTML của tiện ích nếu không có phiên OAuth hợp lệ và quyền truy cập tài liệu dùng một lần.

## Khắc phục sự cố

### Activity hiển thị “Gateway offline”

  * xác nhận tunnel đang chạy và định tuyến đến cổng liên kết thực tế của Gateway
  * xác nhận đích trong Developer Portal có chứa `/discord/activity`
  * khởi động lại Gateway sau khi thay đổi cấu hình Discord hoặc OpenClaw
  * kiểm tra nhật ký Gateway để tìm cảnh báo một dòng về việc thiếu client secret của Activities


### Discord mở trang trống hoặc báo cáo `blocked:csp`

  * xác minh ánh xạ URL sử dụng `ROOT` và không thêm phân đoạn `/discord/activity` thứ hai
  * xác nhận shell, `shell.js` và mô-đun SDK đều được trả về qua proxy Discord
  * kiểm tra nhật ký Gateway để tìm các yêu cầu trong `/discord/activity/`


Các yêu cầu mạng của tiện ích bị chặn có chủ đích. Hãy nhúng trực tiếp toàn bộ CSS, JavaScript, hình ảnh và dữ liệu mà tiện ích cần.

### “Widget unavailable”

Khởi chạy nút từ kênh nơi agent đã đăng nút đó. OpenClaw theo dõi các lần khởi chạy ở phía máy chủ khi người dùng nhấp vào, vì vậy bản ghi khởi chạy mới có thể phân giải chính xác tiện ích ngay cả khi Discord bỏ qua hoặc làm hỏng ID tùy chỉnh của nút. Khi cả ID tùy chỉnh lẫn bản ghi khởi chạy đều không phân giải được, OpenClaw sẽ mở tiện ích còn hiệu lực được đăng gần đây nhất trong kênh đó. Các tiện ích cũ hơn vẫn có thể được truy cập qua những nút còn giữ ID tùy chỉnh của chúng.

### “You cannot launch Activities in this channel”

Discord không khởi chạy Activities từ các luồng bài đăng diễn đàn. OpenClaw có thể đăng tin nhắn tiện ích và nút tại đó, nhưng hãy khởi chạy Activity từ một kênh văn bản thông thường. Hạn chế này đến từ Discord, không phải OpenClaw.

Was this useful?YesNo

Open issue