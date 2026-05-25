---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/vi/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

Thêm giao diện kênh WhatsApp để gửi và nhận tin nhắn OpenClaw.

## Phân phối

  * Gói: `@openclaw/whatsapp`
  * Phương thức cài đặt: npm; ClawHub


## Giao diện

channels: whatsapp

## Ghi chú cài đặt trên Windows

Trên Windows, Plugin WhatsApp cần Git có trong `PATH` trong quá trình cài đặt npm vì một trong các phụ thuộc Baileys/libsignal của nó được tải từ URL git. Cài đặt Git for Windows, sau đó khởi động lại shell và chạy lại lệnh cài đặt:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git cũng hoạt động nếu thư mục `bin` của nó có trong `PATH`.

## Tài liệu liên quan

  * [whatsapp](</vi/channels/whatsapp>)


Was this useful?YesNo