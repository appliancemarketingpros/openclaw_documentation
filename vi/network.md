---
title: Mạng
source_url: https://docs.openclaw.ai/vi/network
scraped_at: 2026-05-25
---

Trung tâm này liên kết đến các tài liệu cốt lõi về cách OpenClaw kết nối, ghép đôi và bảo mật thiết bị trên localhost, LAN và tailnet.

## Mô hình cốt lõi

Hầu hết thao tác đi qua Gateway (`openclaw gateway`), một tiến trình chạy dài duy nhất sở hữu các kết nối kênh và mặt phẳng điều khiển WebSocket.

  * **Ưu tiên loopback** : Gateway WS mặc định là `ws://127.0.0.1:18789`. Các bind không phải loopback yêu cầu đường dẫn xác thực Gateway hợp lệ: xác thực token/mật khẩu bằng shared-secret, hoặc một triển khai `trusted-proxy` không phải loopback được cấu hình đúng.
  * **Một Gateway cho mỗi host** được khuyến nghị. Để cô lập, hãy chạy nhiều gateway với hồ sơ và cổng riêng biệt ([Nhiều Gateway](</vi/gateway/multiple-gateways>)).
  * **Máy chủ Canvas** được phục vụ trên cùng cổng với Gateway (`/__openclaw__/canvas/`, `/__openclaw__/a2ui/`), được bảo vệ bằng xác thực Gateway khi bind vượt ra ngoài loopback.
  * **Truy cập từ xa** thường là tunnel SSH hoặc Tailscale VPN ([Truy cập từ xa](</vi/gateway/remote>)).


Tài liệu tham khảo chính:

  * [Kiến trúc Gateway](</vi/concepts/architecture>)
  * [Giao thức Gateway](</vi/gateway/protocol>)
  * [Runbook Gateway](</vi/gateway>)
  * [Bề mặt web + chế độ bind](</vi/web>)


## Ghép đôi + danh tính

  * [Tổng quan ghép đôi (DM + node)](</vi/channels/pairing>)
  * [Ghép đôi node do Gateway sở hữu](</vi/gateway/pairing>)
  * [CLI thiết bị (ghép đôi + xoay vòng token)](</vi/cli/devices>)
  * [CLI ghép đôi (phê duyệt DM)](</vi/cli/pairing>)


Tin cậy cục bộ:

  * Các kết nối local loopback trực tiếp có thể được tự động phê duyệt để ghép đôi nhằm giữ trải nghiệm trên cùng host mượt mà.
  * OpenClaw cũng có một đường dẫn tự kết nối hẹp trong backend/container cục bộ cho các luồng trợ giúp shared-secret đáng tin cậy.
  * Các client tailnet và LAN, bao gồm cả bind tailnet trên cùng host, vẫn yêu cầu phê duyệt ghép đôi rõ ràng.


## Khám phá + phương thức truyền tải

  * [Khám phá và phương thức truyền tải](</vi/gateway/discovery>)
  * [Bonjour / mDNS](</vi/gateway/bonjour>)
  * [Truy cập từ xa (SSH)](</vi/gateway/remote>)
  * [Tailscale](</vi/gateway/tailscale>)


## Node + phương thức truyền tải

  * [Tổng quan node](</vi/nodes>)
  * [Giao thức bridge (node cũ, lịch sử)](</vi/gateway/bridge-protocol>)
  * [Runbook node: iOS](</vi/platforms/ios>)
  * [Runbook node: Android](</vi/platforms/android>)


## Bảo mật

  * [Tổng quan bảo mật](</vi/gateway/security>)
  * [Tham chiếu cấu hình Gateway](</vi/gateway/configuration>)
  * [Khắc phục sự cố](</vi/gateway/troubleshooting>)
  * [Doctor](</vi/gateway/doctor>)


## Liên quan

  * [Runbook Gateway](</vi/gateway>)
  * [Truy cập từ xa](</vi/gateway/remote>)


Was this useful?YesNo