---
title: SMS
source_url: https://docs.openclaw.ai/vi/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw có thể nhận và gửi SMS thông qua số điện thoại Twilio hoặc Messaging Service. Gateway đăng ký một tuyến webhook đến, mặc định xác thực chữ ký yêu cầu của Twilio, và gửi phản hồi trở lại qua Messages API của Twilio.

[**Ghép nối** Chính sách DM mặc định cho SMS là ghép nối. ](</vi/channels/pairing>) [**Bảo mật Gateway** Xem lại việc phơi bày webhook và các kiểm soát truy cập người gửi. ](</vi/gateway/security>) [**Khắc phục sự cố kênh** Chẩn đoán liên kênh và các playbook sửa chữa. ](</vi/channels/troubleshooting>)

## Trước khi bắt đầu

Bạn cần:

  * Plugin SMS chính thức được cài đặt bằng `openclaw plugins install @openclaw/sms`.
  * Một tài khoản Twilio có số điện thoại hỗ trợ SMS, hoặc một Twilio Messaging Service.
  * Twilio Account SID và Auth Token.
  * Một URL HTTPS công khai trỏ tới OpenClaw Gateway của bạn.
  * Một lựa chọn chính sách người gửi: `pairing` cho sử dụng riêng tư, `allowlist` cho các số điện thoại đã được phê duyệt trước, hoặc `open` chỉ cho truy cập SMS công khai có chủ đích.


Dùng một số Twilio cho cả SMS và Voice Call nếu số đó có cả hai khả năng. Cấu hình webhook SMS và webhook Voice riêng trong Twilio; trang này chỉ đề cập webhook SMS.

## Thiết lập nhanh

* ### Cài đặt Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Tạo hoặc chọn người gửi Twilio

Trong Twilio, mở **Phone Numbers > Manage > Active numbers** và chọn một số hỗ trợ SMS. Lưu:

  * Account SID, ví dụ `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Số điện thoại người gửi, ví dụ `+15551234567`


Nếu bạn dùng Messaging Service thay vì số người gửi cố định, hãy lưu Messaging Service SID, ví dụ `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Cấu hình kênh SMS

Lưu nội dung này dưới dạng `sms.patch.json5` và thay đổi các placeholder:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Áp dụng:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Trỏ Twilio tới webhook Gateway

Trong cài đặt số điện thoại Twilio, mở **Messaging** và đặt **A message comes in** thành:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Dùng HTTP `POST`. Đường dẫn cục bộ mặc định là `/webhooks/sms`; thay đổi `channels.sms.webhookPath` nếu bạn cần tuyến khác.

* ### Phơi bày đúng đường dẫn webhook SMS

URL công khai của bạn phải định tuyến đường dẫn SMS tới tiến trình Gateway. Nếu bạn dùng Tailscale Funnel để kiểm thử cục bộ, hãy phơi bày `/webhooks/sms` một cách rõ ràng:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Voice Call và SMS dùng các đường dẫn webhook riêng. Nếu cùng một số Twilio xử lý cả hai, hãy giữ cả hai tuyến được cấu hình trong Twilio và trong tunnel của bạn.

* ### Khởi động Gateway và phê duyệt người gửi đầu tiên

bashCopy code
[code]
    openclaw gateway
[/code]

Gửi một tin nhắn văn bản tới số Twilio. Tin nhắn đầu tiên tạo một yêu cầu ghép nối. Phê duyệt yêu cầu đó:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Mã ghép nối hết hạn sau 1 giờ.

## Ví dụ cấu hình

### Tệp cấu hình

Dùng thiết lập bằng tệp cấu hình khi bạn muốn định nghĩa kênh đi cùng cấu hình Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Biến môi trường

Dùng thiết lập env cho các triển khai một tài khoản, nơi bí mật đến từ môi trường máy chủ:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Sau đó bật kênh trong cấu hình:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` được chấp nhận làm bí danh cho `TWILIO_PHONE_NUMBER`. Dùng `TWILIO_MESSAGING_SERVICE_SID` thay cho người gửi dạng số điện thoại khi Twilio nên chọn người gửi từ Messaging Service.

### Auth token SecretRef

`authToken` có thể là SecretRef. Dùng cách này khi Gateway nên phân giải Twilio Auth Token từ runtime bí mật của OpenClaw thay vì lưu cấu hình dạng văn bản thuần:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Biến môi trường hoặc nhà cung cấp bí mật được tham chiếu phải hiển thị với runtime Gateway. Khởi động lại các tiến trình Gateway được quản lý sau khi thay đổi biến môi trường của máy chủ.

### Số riêng tư chỉ allowlist

Dùng `allowlist` khi chỉ các số điện thoại đã biết mới có thể trò chuyện với agent:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Người gửi Messaging Service

Dùng `messagingServiceSid` thay vì `fromNumber` khi Twilio nên chọn người gửi thông qua Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Nếu cả `fromNumber` và `messagingServiceSid` đều có mặt sau khi phân giải cấu hình và env, `fromNumber` sẽ được dùng.

### Mục tiêu gửi đi mặc định

Đặt `defaultTo` khi tự động hóa hoặc gửi do agent khởi tạo nên có đích mặc định nếu luồng gửi bỏ qua mục tiêu rõ ràng:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Kiểm soát truy cập

`channels.sms.dmPolicy` kiểm soát truy cập SMS trực tiếp:

  * `pairing` (mặc định)
  * `allowlist` (yêu cầu ít nhất một người gửi trong `allowFrom`)
  * `open` (yêu cầu `allowFrom` bao gồm `"*"`)
  * `disabled`


Các mục `allowFrom` nên là số điện thoại E.164 như `+15551234567`. Tiền tố `sms:` được chấp nhận và chuẩn hóa. Với trợ lý riêng tư, ưu tiên `dmPolicy: "allowlist"` cùng các số điện thoại rõ ràng.

## Gửi SMS

Mục tiêu SMS gửi đi dùng tiền tố dịch vụ `sms:` với kênh SMS được chọn:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Khi việc chọn kênh là ngầm định, `twilio-sms:+15551234567` chọn kênh này mà không chiếm quyền tiền tố dịch vụ `sms:` hiện có do kênh sở hữu, vốn được iMessage dùng.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

CLI yêu cầu `--target` rõ ràng. `defaultTo` dành cho các đường dẫn tự động hóa và gửi do agent khởi tạo, nơi mục tiêu có thể được phân giải từ cấu hình kênh.

Phản hồi của agent từ các cuộc trò chuyện SMS đến sẽ tự động quay lại người gửi thông qua người gửi Twilio đã cấu hình.

Đầu ra SMS là văn bản thuần. OpenClaw loại bỏ markdown, làm phẳng các khối mã có hàng rào, giữ các liên kết dễ đọc, và chia các phản hồi dài thành nhiều phần trước khi gửi chúng qua Twilio.

## Xác minh thiết lập

Sau khi Gateway khởi động:

  1. Xác nhận nhật ký Gateway hiển thị tuyến webhook SMS.
  2. Chạy một probe phía Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Gửi SMS tới số Twilio từ điện thoại của bạn.
  4. Chạy `openclaw pairing list sms`.
  5. Phê duyệt mã ghép nối bằng `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Gửi SMS khác và xác nhận agent phản hồi.


Để kiểm thử chỉ gửi đi, dùng:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### Kiểm thử đầu cuối từ macOS iMessage/SMS

Trên máy Mac có thể gửi SMS nhà mạng qua Messages, bạn có thể dùng `imsg` để điều khiển phía người gửi mà không cần chạm vào điện thoại:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Tin nhắn đầu tiên sẽ tạo một yêu cầu ghép nối. Tin nhắn thứ hai sẽ nhận phản hồi của agent qua Twilio.

## Bảo mật webhook

Theo mặc định, OpenClaw xác thực `X-Twilio-Signature` bằng `publicWebhookUrl` và `authToken`. Giữ `publicWebhookUrl` khớp từng byte với URL được cấu hình trong Twilio, bao gồm scheme, host, path và query string.

Chỉ cho kiểm thử tunnel cục bộ, bạn có thể đặt:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Không dùng xác thực chữ ký đã tắt trên Gateway công khai.

## Cấu hình nhiều tài khoản

Dùng `accounts` khi bạn vận hành nhiều hơn một số Twilio:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Mỗi tài khoản nên dùng một `webhookPath` riêng biệt.

## Khắc phục sự cố

### Twilio trả về 403 hoặc OpenClaw từ chối webhook

Kiểm tra rằng `publicWebhookUrl` khớp chính xác với URL được cấu hình trong Twilio, bao gồm scheme, host, path và query string. Twilio ký chuỗi URL công khai, vì vậy việc proxy ghi lại URL và tên máy chủ thay thế có thể làm hỏng xác thực chữ ký.

### Không có yêu cầu ghép nối nào xuất hiện

Kiểm tra URL và phương thức webhook **Messaging** của số Twilio. Nó phải trỏ tới URL webhook SMS và dùng `POST`. Cũng xác nhận Gateway có thể truy cập được từ Internet công khai hoặc qua tunnel của bạn.

Nếu nhật ký tin nhắn Twilio hiển thị lỗi `11200`, Twilio đã chấp nhận SMS đến nhưng không thể truy cập webhook của bạn. Kiểm tra:

  * Twilio **Messaging > A message comes in** trỏ tới `publicWebhookUrl`.
  * Phương thức là `POST`.
  * Tunnel hoặc reverse proxy phơi bày đúng `webhookPath`; với Tailscale Funnel, chạy `tailscale funnel status` và xác nhận `/webhooks/sms` được liệt kê.
  * `publicWebhookUrl` dùng cùng scheme, host, path và query string mà Twilio gửi, để xác thực chữ ký có thể tái tạo URL đã được ký.


### Gửi đi thất bại

Xác nhận `accountSid`, `authToken`, và `fromNumber` hoặc `messagingServiceSid` đã được phân giải. Nếu bạn dùng tài khoản Twilio dùng thử, số đích có thể cần được xác minh trong Twilio trước khi SMS gửi đi được gửi.

### Tin nhắn đến nhưng agent không trả lời

Kiểm tra `dmPolicy` và `allowFrom`. Với chính sách `pairing` mặc định, người gửi phải được phê duyệt trước khi các lượt tác nhân thông thường được xử lý.

Was this useful?YesNo

Open issue