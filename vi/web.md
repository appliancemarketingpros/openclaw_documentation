---
title: Trang web
source_url: https://docs.openclaw.ai/vi/web
scraped_at: 2026-05-25
---

Gateway phục vụ một **Giao diện điều khiển trên trình duyệt** nhỏ (Vite + Lit) từ cùng cổng với WebSocket của Gateway:

  * mặc định: `http://<host>:18789/`
  * với `gateway.tls.enabled: true`: `https://<host>:18789/`
  * tiền tố tùy chọn: đặt `gateway.controlUi.basePath` (ví dụ: `/openclaw`)


Các khả năng nằm trong [Giao diện điều khiển](</vi/web/control-ui>). Phần còn lại của trang này tập trung vào các chế độ liên kết, bảo mật và các bề mặt hướng web.

## Webhook

Khi `hooks.enabled=true`, Gateway cũng mở một điểm cuối Webhook nhỏ trên cùng máy chủ HTTP. Xem [cấu hình Gateway](</vi/gateway/configuration>) → `hooks` để biết auth + payload.

## Cấu hình (bật mặc định)

Giao diện điều khiển được **bật theo mặc định** khi có tài nguyên (`dist/control-ui`). Bạn có thể điều khiển nó qua cấu hình:

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath optional  },}
[/code]

## Truy cập Tailscale

### Serve tích hợp (khuyến nghị)

Giữ Gateway trên loopback và để Tailscale Serve proxy nó:

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

Sau đó khởi động gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Mở:

  * `https://<magicdns>/` (hoặc `gateway.controlUi.basePath` bạn đã cấu hình)


### Liên kết tailnet + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

Sau đó khởi động gateway (ví dụ không phải loopback này dùng auth token bí mật chia sẻ):

bashCopy code
[code]
    openclaw gateway
[/code]

Mở:

  * `http://<tailscale-ip>:18789/` (hoặc `gateway.controlUi.basePath` bạn đã cấu hình)


### Internet công khai (Funnel)

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // or OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## Ghi chú bảo mật

  * Auth Gateway là bắt buộc theo mặc định (token, mật khẩu, trusted-proxy hoặc các header nhận dạng Tailscale Serve khi được bật).
  * Các liên kết không phải loopback vẫn **yêu cầu** auth gateway. Trong thực tế, điều đó nghĩa là auth token/mật khẩu hoặc một proxy ngược nhận biết danh tính với `gateway.auth.mode: "trusted-proxy"`.
  * Trình hướng dẫn tạo auth bí mật chia sẻ theo mặc định và thường tạo một token gateway (ngay cả trên loopback).
  * Ở chế độ bí mật chia sẻ, UI gửi `connect.params.auth.token` hoặc `connect.params.auth.password`.
  * Khi `gateway.tls.enabled: true`, các helper dashboard cục bộ và trạng thái hiển thị URL dashboard `https://` và URL WebSocket `wss://`.
  * Trong các chế độ mang danh tính như Tailscale Serve hoặc `trusted-proxy`, thay vào đó kiểm tra auth WebSocket được thỏa mãn từ các header yêu cầu.
  * Đối với các triển khai Giao diện điều khiển không phải loopback, đặt `gateway.controlUi.allowedOrigins` một cách tường minh (origin đầy đủ). Nếu không có, khởi động gateway sẽ bị từ chối theo mặc định.
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` bật chế độ dự phòng origin theo header Host, nhưng đây là một hạ cấp bảo mật nguy hiểm.
  * Với Serve, các header nhận dạng Tailscale có thể thỏa mãn auth Giao diện điều khiển/WebSocket khi `gateway.auth.allowTailscale` là `true` (không cần token/mật khẩu). Các điểm cuối HTTP API không dùng các header nhận dạng Tailscale đó; thay vào đó chúng tuân theo chế độ auth HTTP bình thường của gateway. Đặt `gateway.auth.allowTailscale: false` để yêu cầu thông tin xác thực tường minh. Xem [Tailscale](</vi/gateway/tailscale>) và [Bảo mật](</vi/gateway/security>). Luồng không cần token này giả định máy chủ gateway là đáng tin cậy.
  * `gateway.tailscale.mode: "funnel"` yêu cầu `gateway.auth.mode: "password"` (mật khẩu chia sẻ).


## Xây dựng UI

Gateway phục vụ các tệp tĩnh từ `dist/control-ui`. Xây dựng chúng bằng:

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo