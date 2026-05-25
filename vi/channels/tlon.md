---
title: Tlon
source_url: https://docs.openclaw.ai/vi/channels/tlon
scraped_at: 2026-05-25
---

Tlon là trình nhắn tin phi tập trung được xây dựng trên Urbit. OpenClaw kết nối với Urbit ship của bạn và có thể phản hồi DM cũng như tin nhắn trò chuyện nhóm. Theo mặc định, phản hồi trong nhóm yêu cầu nhắc đến bằng @ và có thể được hạn chế thêm qua danh sách cho phép.

Trạng thái: Plugin đi kèm. DM, nhắc đến trong nhóm, phản hồi trong luồng, định dạng văn bản phong phú và tải ảnh lên đều được hỗ trợ. Phản ứng và cuộc thăm dò chưa được hỗ trợ.

## Plugin đi kèm

Tlon được phát hành dưới dạng Plugin đi kèm trong các bản phát hành OpenClaw hiện tại, vì vậy các bản dựng đóng gói thông thường không cần cài đặt riêng.

Nếu bạn đang dùng bản dựng cũ hơn hoặc bản cài đặt tùy chỉnh loại trừ Tlon, hãy cài đặt một gói npm hiện tại:

Cài đặt qua CLI (npm registry):

bashCopy code
[code]
    openclaw plugins install @openclaw/tlon
[/code]

Dùng gói không kèm phiên bản để theo dõi thẻ phát hành chính thức hiện tại. Chỉ ghim một phiên bản chính xác khi bạn cần bản cài đặt có thể tái lập.

Bản checkout cục bộ (khi chạy từ git repo):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/tlon-plugin
[/code]

Chi tiết: [Plugins](</vi/tools/plugin>)

## Thiết lập

  1. Đảm bảo Plugin Tlon có sẵn. 
     * Các bản phát hành OpenClaw đóng gói hiện tại đã đi kèm Plugin này.
     * Các bản cài đặt cũ hơn/tùy chỉnh có thể thêm thủ công bằng các lệnh ở trên.
  2. Lấy URL ship và mã đăng nhập của bạn.
  3. Cấu hình `channels.tlon`.
  4. Khởi động lại Gateway.
  5. DM bot hoặc nhắc đến bot trong kênh nhóm.


Cấu hình tối thiểu (một tài khoản):

json5Copy code
[code]
    {  channels: {    tlon: {      enabled: true,      ship: "~sampel-palnet",      url: "https://your-ship-host",      code: "lidlut-tabwed-pillex-ridrup",      ownerShip: "~your-main-ship", // recommended: your ship, always allowed    },  },}
[/code]

## Ship riêng tư/LAN

Theo mặc định, OpenClaw chặn hostname và dải IP riêng tư/nội bộ để bảo vệ khỏi SSRF. Nếu ship của bạn đang chạy trên mạng riêng tư (localhost, IP LAN hoặc hostname nội bộ), bạn phải bật rõ ràng:

json5Copy code
[code]
    {  channels: {    tlon: {      url: "http://localhost:8080",      allowPrivateNetwork: true,    },  },}
[/code]

Điều này áp dụng cho các URL như:

  * `http://localhost:8080`
  * `http://192.168.x.x:8080`
  * `http://my-ship.local:8080`


⚠️ Chỉ bật tùy chọn này nếu bạn tin tưởng mạng cục bộ của mình. Thiết lập này vô hiệu hóa các biện pháp bảo vệ SSRF cho các yêu cầu tới URL ship của bạn.

## Kênh nhóm

Tự động khám phá được bật theo mặc định. Bạn cũng có thể ghim kênh thủ công:

json5Copy code
[code]
    {  channels: {    tlon: {      groupChannels: ["chat/~host-ship/general", "chat/~host-ship/support"],    },  },}
[/code]

Tắt tự động khám phá:

json5Copy code
[code]
    {  channels: {    tlon: {      autoDiscoverChannels: false,    },  },}
[/code]

## Kiểm soát truy cập

Danh sách cho phép DM (trống = không cho phép DM, dùng `ownerShip` cho luồng phê duyệt):

json5Copy code
[code]
    {  channels: {    tlon: {      dmAllowlist: ["~zod", "~nec"],    },  },}
[/code]

Ủy quyền nhóm (mặc định bị hạn chế):

json5Copy code
[code]
    {  channels: {    tlon: {      defaultAuthorizedShips: ["~zod"],      authorization: {        channelRules: {          "chat/~host-ship/general": {            mode: "restricted",            allowedShips: ["~zod", "~nec"],          },          "chat/~host-ship/announcements": {            mode: "open",          },        },      },    },  },}
[/code]

## Hệ thống chủ sở hữu và phê duyệt

Đặt một owner ship để nhận yêu cầu phê duyệt khi người dùng chưa được ủy quyền cố gắng tương tác:

json5Copy code
[code]
    {  channels: {    tlon: {      ownerShip: "~your-main-ship",    },  },}
[/code]

Owner ship được **tự động ủy quyền ở mọi nơi** — lời mời DM được tự động chấp nhận và tin nhắn kênh luôn được phép. Bạn không cần thêm owner vào `dmAllowlist` hoặc `defaultAuthorizedShips`.

Khi được đặt, owner nhận thông báo DM cho:

  * Yêu cầu DM từ các ship không có trong danh sách cho phép
  * Lượt nhắc đến trong các kênh chưa được ủy quyền
  * Yêu cầu mời nhóm


## Thiết lập tự động chấp nhận

Tự động chấp nhận lời mời DM (cho các ship trong dmAllowlist):

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptDmInvites: true,    },  },}
[/code]

Tự động chấp nhận lời mời nhóm từ các ship đáng tin cậy:

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptGroupInvites: true,      groupInviteAllowlist: ["~zod"],    },  },}
[/code]

`autoAcceptGroupInvites` mặc định từ chối an toàn khi `groupInviteAllowlist` trống. Đặt danh sách cho phép thành các ship có lời mời nhóm cần được tự động chấp nhận.

## Mục tiêu gửi (CLI/Cron)

Dùng các mục tiêu này với `openclaw message send` hoặc gửi qua Cron:

  * DM: `~sampel-palnet` hoặc `dm/~sampel-palnet`
  * Nhóm: `chat/~host-ship/channel` hoặc `group:~host-ship/channel`


## Kỹ năng đi kèm

Plugin Tlon bao gồm một kỹ năng đi kèm ([`@tloncorp/tlon-skill`](<https://github.com/tloncorp/tlon-skill>)) cung cấp quyền truy cập CLI vào các thao tác Tlon:

  * **Liên hệ** : lấy/cập nhật hồ sơ, liệt kê liên hệ
  * **Kênh** : liệt kê, tạo, đăng tin nhắn, lấy lịch sử
  * **Nhóm** : liệt kê, tạo, quản lý thành viên
  * **DM** : gửi tin nhắn, phản ứng với tin nhắn
  * **Phản ứng** : thêm/xóa phản ứng emoji vào bài đăng và DM
  * **Thiết lập** : quản lý quyền Plugin qua lệnh slash


Kỹ năng này tự động có sẵn khi Plugin được cài đặt.

## Khả năng

Tính năng | Trạng thái  
---|---  
Tin nhắn trực tiếp | ✅ Được hỗ trợ  
Nhóm/kênh | ✅ Được hỗ trợ (mặc định yêu cầu nhắc đến)  
Luồng | ✅ Được hỗ trợ (tự động phản hồi trong luồng)  
Văn bản phong phú | ✅ Markdown được chuyển đổi sang định dạng Tlon  
Hình ảnh | ✅ Được tải lên bộ nhớ Tlon  
Phản ứng | ✅ Qua kỹ năng đi kèm  
Cuộc thăm dò | ❌ Chưa được hỗ trợ  
Lệnh gốc | ✅ Được hỗ trợ (mặc định chỉ owner)  
  
## Khắc phục sự cố

Chạy thang kiểm tra này trước:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctor
[/code]

Các lỗi thường gặp:

  * **DM bị bỏ qua** : người gửi không có trong `dmAllowlist` và chưa cấu hình `ownerShip` cho luồng phê duyệt.
  * **Tin nhắn nhóm bị bỏ qua** : kênh chưa được khám phá hoặc người gửi chưa được ủy quyền.
  * **Lỗi kết nối** : kiểm tra URL ship có thể truy cập được; bật `allowPrivateNetwork` cho ship cục bộ.
  * **Lỗi xác thực** : xác minh mã đăng nhập còn hiệu lực (mã sẽ luân phiên thay đổi).


## Tham chiếu cấu hình

Cấu hình đầy đủ: [Cấu hình](</vi/gateway/configuration>)

Tùy chọn nhà cung cấp:

  * `channels.tlon.enabled`: bật/tắt khởi động kênh.
  * `channels.tlon.ship`: tên Urbit ship của bot (ví dụ `~sampel-palnet`).
  * `channels.tlon.url`: URL ship (ví dụ `https://sampel-palnet.tlon.network`).
  * `channels.tlon.code`: mã đăng nhập ship.
  * `channels.tlon.allowPrivateNetwork`: cho phép URL localhost/LAN (bỏ qua SSRF).
  * `channels.tlon.ownerShip`: owner ship cho hệ thống phê duyệt (luôn được ủy quyền).
  * `channels.tlon.dmAllowlist`: các ship được phép DM (trống = không có).
  * `channels.tlon.autoAcceptDmInvites`: tự động chấp nhận DM từ các ship trong danh sách cho phép.
  * `channels.tlon.autoAcceptGroupInvites`: tự động chấp nhận lời mời nhóm từ các ship trong danh sách cho phép.
  * `channels.tlon.groupInviteAllowlist`: các ship có lời mời nhóm có thể được tự động chấp nhận.
  * `channels.tlon.autoDiscoverChannels`: tự động khám phá kênh nhóm (mặc định: true).
  * `channels.tlon.groupChannels`: các nest kênh được ghim thủ công.
  * `channels.tlon.defaultAuthorizedShips`: các ship được ủy quyền cho mọi kênh.
  * `channels.tlon.authorization.channelRules`: quy tắc xác thực theo từng kênh.
  * `channels.tlon.showModelSignature`: thêm tên mô hình vào tin nhắn.


## Ghi chú

  * Phản hồi nhóm yêu cầu nhắc đến (ví dụ `~your-bot-ship`) để phản hồi.
  * Phản hồi trong luồng: nếu tin nhắn đến nằm trong một luồng, OpenClaw phản hồi trong luồng.
  * Văn bản phong phú: định dạng Markdown (in đậm, in nghiêng, mã, tiêu đề, danh sách) được chuyển đổi sang định dạng gốc của Tlon.
  * Hình ảnh: URL được tải lên bộ nhớ Tlon và nhúng dưới dạng khối hình ảnh.


## Liên quan

  * [Tổng quan về kênh](</vi/channels>) — tất cả kênh được hỗ trợ
  * [Ghép nối](</vi/channels/pairing>) — xác thực DM và luồng ghép nối
  * [Nhóm](</vi/channels/groups>) — hành vi trò chuyện nhóm và cơ chế yêu cầu nhắc đến
  * [Định tuyến kênh](</vi/channels/channel-routing>) — định tuyến phiên cho tin nhắn
  * [Bảo mật](</vi/gateway/security>) — mô hình truy cập và gia cố


Was this useful?YesNo