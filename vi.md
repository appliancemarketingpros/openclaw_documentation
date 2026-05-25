---
title: OpenClaw
source_url: https://docs.openclaw.ai/vi
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"TẨY DA CHẾT! TẨY DA CHẾT!"_ — Có lẽ là một con tôm hùm không gian

**Gateway trên mọi hệ điều hành cho các AI agent trên Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, và nhiều nền tảng khác.**

Gửi một tin nhắn, nhận phản hồi từ agent ngay trong túi bạn. Chạy một Gateway trên các kênh tích hợp sẵn, các Plugin kênh đi kèm, WebChat, và các node di động.

[**Bắt đầu** Cài đặt OpenClaw và khởi chạy Gateway trong vài phút. ](</vi/start/getting-started>) [**Chạy quy trình thiết lập ban đầu** Thiết lập có hướng dẫn bằng `openclaw onboard` và các luồng ghép nối. ](</vi/start/wizard>) [**Mở Control UI** Khởi chạy dashboard trong trình duyệt cho chat, cấu hình, và phiên. ](</vi/web/control-ui>)

## OpenClaw là gì?

OpenClaw là một **Gateway tự lưu trữ** kết nối các ứng dụng chat và giao diện kênh yêu thích của bạn — các kênh tích hợp sẵn cùng các Plugin kênh đi kèm hoặc bên ngoài như Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo, và nhiều nền tảng khác — với các AI coding agent như Pi. Bạn chạy một tiến trình Gateway duy nhất trên máy của mình (hoặc một máy chủ), và nó trở thành cầu nối giữa các ứng dụng nhắn tin của bạn với một trợ lý AI luôn sẵn sàng.

**Dành cho ai?** Nhà phát triển và người dùng chuyên sâu muốn có một trợ lý AI cá nhân có thể nhắn tin từ bất cứ đâu — mà không phải từ bỏ quyền kiểm soát dữ liệu hoặc phụ thuộc vào dịch vụ được lưu trữ sẵn.

**Điểm khác biệt là gì?**

  * **Tự lưu trữ** : chạy trên phần cứng của bạn, theo quy tắc của bạn
  * **Đa kênh** : một Gateway phục vụ đồng thời các kênh tích hợp sẵn cùng các Plugin kênh đi kèm hoặc bên ngoài
  * **Hướng agent** : được xây dựng cho coding agent với khả năng dùng công cụ, phiên, bộ nhớ, và định tuyến đa agent
  * **Mã nguồn mở** : giấy phép MIT, do cộng đồng thúc đẩy


**Bạn cần gì?** Node 24 (khuyến nghị), hoặc Node 22 LTS (`22.16+`) để tương thích, một API key từ nhà cung cấp bạn chọn, và 5 phút. Để có chất lượng và bảo mật tốt nhất, hãy dùng model thế hệ mới nhất mạnh nhất hiện có.

## Cách hoạt động
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway là nguồn sự thật duy nhất cho phiên, định tuyến, và kết nối kênh.

## Khả năng chính

[**Gateway đa kênh** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat, và nhiều nền tảng khác với một tiến trình Gateway duy nhất. ](</vi/channels>) [**Kênh Plugin** Các Plugin đi kèm bổ sung Matrix, Nostr, Twitch, Zalo, và nhiều kênh khác trong các bản phát hành hiện tại thông thường. ](</vi/tools/plugin>) [**Định tuyến đa agent** Phiên tách biệt theo agent, workspace, hoặc người gửi. ](</vi/concepts/multi-agent>) [**Hỗ trợ phương tiện** Gửi và nhận hình ảnh, âm thanh, và tài liệu. ](</vi/nodes/images>) [**Web Control UI** Dashboard trong trình duyệt cho chat, cấu hình, phiên, và node. ](</vi/web/control-ui>) [**Node di động** Ghép nối các node iOS và Android cho Canvas, camera, và workflow hỗ trợ giọng nói. ](</vi/nodes>)

## Khởi động nhanh

* ### Cài đặt OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Thiết lập ban đầu và cài đặt dịch vụ

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chat

Mở Control UI trong trình duyệt của bạn và gửi một tin nhắn:

bashCopy code
[code]
    openclaw dashboard
[/code]

Hoặc kết nối một kênh ([Telegram](</vi/channels/telegram>) là nhanh nhất) và chat từ điện thoại của bạn.

Cần phần cài đặt đầy đủ và thiết lập dev? Xem [Bắt đầu](</vi/start/getting-started>).

## Dashboard

Mở Control UI trong trình duyệt sau khi Gateway khởi động.

  * Mặc định cục bộ: <http://127.0.0.1:18789/>
  * Truy cập từ xa: [Bề mặt web](</vi/web>) và [Tailscale](</vi/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Cấu hình (tùy chọn)

Cấu hình nằm tại `~/.openclaw/openclaw.json`.

  * Nếu bạn **không làm gì** , OpenClaw dùng binary Pi đi kèm ở chế độ RPC với phiên theo từng người gửi.
  * Nếu bạn muốn siết chặt quyền truy cập, hãy bắt đầu với `channels.whatsapp.allowFrom` và quy tắc nhắc tên (đối với nhóm).


Ví dụ:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Bắt đầu tại đây

[**Trung tâm tài liệu** Tất cả tài liệu và hướng dẫn, được sắp xếp theo trường hợp sử dụng. ](</vi/start/hubs>) [**Cấu hình** Thiết lập Gateway cốt lõi, token, và cấu hình nhà cung cấp. ](</vi/gateway/configuration>) [**Truy cập từ xa** Các mẫu truy cập SSH và tailnet. ](</vi/gateway/remote>) [**Kênh** Thiết lập riêng cho từng kênh cho Feishu, Microsoft Teams, WhatsApp, Telegram, Discord, và nhiều nền tảng khác. ](</vi/channels/telegram>) [**Node** Node iOS và Android với ghép nối, Canvas, camera, và thao tác thiết bị. ](</vi/nodes>) [**Trợ giúp** Điểm vào cho các cách khắc phục phổ biến và xử lý sự cố. ](</vi/help>)

## Tìm hiểu thêm

[**Danh sách tính năng đầy đủ** Khả năng đầy đủ về kênh, định tuyến, và phương tiện. ](</vi/concepts/features>) [**Định tuyến đa agent** Cô lập workspace và phiên theo từng agent. ](</vi/concepts/multi-agent>) [**Bảo mật** Token, danh sách cho phép, và kiểm soát an toàn. ](</vi/gateway/security>) [**Xử lý sự cố** Chẩn đoán Gateway và các lỗi thường gặp. ](</vi/gateway/troubleshooting>) [**Giới thiệu và ghi công** Nguồn gốc dự án, người đóng góp, và giấy phép. ](</vi/reference/credits>)

Was this useful?YesNo