---
title: Cơ sở dữ liệu mẫu thiết bị
source_url: https://docs.openclaw.ai/vi/reference/device-models
scraped_at: 2026-05-25
---

Ứng dụng đồng hành macOS hiển thị tên mẫu thiết bị Apple thân thiện trong UI **Phiên bản** bằng cách ánh xạ định danh mẫu Apple (ví dụ: `iPad16,6`, `Mac16,6`) sang tên dễ đọc.

Ánh xạ này được đưa vào mã nguồn dưới dạng JSON tại:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Nguồn dữ liệu

Hiện chúng tôi đưa ánh xạ này vào mã nguồn từ kho lưu trữ được cấp phép MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Để giữ cho các bản dựng có tính xác định, các tệp JSON được ghim vào các commit upstream cụ thể (được ghi trong `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Cập nhật cơ sở dữ liệu

  1. Chọn các commit upstream mà bạn muốn ghim vào (một cho iOS, một cho macOS).
  2. Cập nhật các hash commit trong `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Tải lại các tệp JSON, được ghim vào các commit đó:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Đảm bảo `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` vẫn khớp với upstream (thay thế nếu giấy phép upstream thay đổi).
  5. Xác minh ứng dụng macOS dựng sạch sẽ (không có cảnh báo):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Liên quan

  * [Node](</vi/nodes>)
  * [Khắc phục sự cố Node](</vi/nodes/troubleshooting>)


Was this useful?YesNo