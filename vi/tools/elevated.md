---
title: Chế độ nâng quyền
source_url: https://docs.openclaw.ai/vi/tools/elevated
scraped_at: 2026-05-25
---

Khi một tác tử chạy bên trong môi trường cách ly, các lệnh `exec` của nó bị giới hạn trong môi trường cách ly. **Chế độ nâng quyền** cho phép tác tử thoát ra và chạy lệnh bên ngoài môi trường cách ly, với các cổng phê duyệt có thể cấu hình.

## Chỉ thị

Điều khiển chế độ nâng quyền theo từng phiên bằng các lệnh gạch chéo:

Chỉ thị | Tác dụng  
---|---  
`/elevated on` | Chạy bên ngoài môi trường cách ly trên đường dẫn máy chủ đã cấu hình, vẫn giữ phê duyệt  
`/elevated ask` | Giống như `on` (bí danh)  
`/elevated full` | Chạy bên ngoài môi trường cách ly trên đường dẫn máy chủ đã cấu hình và bỏ qua phê duyệt  
`/elevated off` | Quay lại thực thi bị giới hạn trong môi trường cách ly  
  
Cũng có sẵn dưới dạng `/elev on|off|ask|full`.

Gửi `/elevated` không có đối số để xem cấp hiện tại.

## Cách hoạt động

* ### Check availability

Chế độ nâng quyền phải được bật trong cấu hình và người gửi phải nằm trong danh sách cho phép:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Set the level

Gửi một tin nhắn chỉ gồm chỉ thị để đặt mặc định cho phiên:

CodeCopy code
[code]
    /elevated full
[/code]

Hoặc dùng trực tiếp trong dòng (chỉ áp dụng cho tin nhắn đó):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands run outside the sandbox

Khi chế độ nâng quyền đang hoạt động, các lệnh gọi `exec` rời khỏi môi trường cách ly. Máy chủ hiệu lực mặc định là `gateway`, hoặc `node` khi đích exec được cấu hình/phiên là `node`. Ở chế độ `full`, các phê duyệt exec bị bỏ qua. Ở chế độ `on`/`ask`, các quy tắc phê duyệt đã cấu hình vẫn được áp dụng.

## Thứ tự phân giải

  1. **Chỉ thị trực tiếp trong dòng** trên tin nhắn (chỉ áp dụng cho tin nhắn đó)
  2. **Ghi đè phiên** (được đặt bằng cách gửi một tin nhắn chỉ gồm chỉ thị)
  3. **Mặc định toàn cục** (`agents.defaults.elevatedDefault` trong cấu hình)


## Tính khả dụng và danh sách cho phép

  * **Cổng toàn cục** : `tools.elevated.enabled` (phải là `true`)
  * **Danh sách cho phép người gửi** : `tools.elevated.allowFrom` với danh sách theo từng kênh
  * **Cổng theo tác tử** : `agents.list[].tools.elevated.enabled` (chỉ có thể hạn chế thêm)
  * **Danh sách cho phép theo tác tử** : `agents.list[].tools.elevated.allowFrom` (người gửi phải khớp cả toàn cục + theo tác tử)
  * **Dự phòng Discord** : nếu `tools.elevated.allowFrom.discord` bị bỏ qua, `channels.discord.allowFrom` được dùng làm dự phòng
  * **Tất cả các cổng phải đạt** ; nếu không, chế độ nâng quyền được xem là không khả dụng


Định dạng mục trong danh sách cho phép:

Tiền tố | Khớp với  
---|---  
(không có) | ID người gửi, E.164, hoặc trường From  
`name:` | Tên hiển thị của người gửi  
`username:` | Tên người dùng của người gửi  
`tag:` | Thẻ của người gửi  
`id:`, `from:`, `e164:` | Nhắm mục tiêu danh tính rõ ràng  
  
## Chế độ nâng quyền không kiểm soát những gì

  * **Chính sách công cụ** : nếu `exec` bị chính sách công cụ từ chối, chế độ nâng quyền không thể ghi đè.
  * **Chính sách chọn máy chủ** : chế độ nâng quyền không biến `auto` thành một ghi đè tự do xuyên máy chủ. Nó dùng các quy tắc đích exec đã cấu hình/phiên, chỉ chọn `node` khi đích đã là `node`.
  * **Tách biệt với`/exec`**: chỉ thị `/exec` điều chỉnh mặc định exec theo từng phiên cho người gửi được ủy quyền và không yêu cầu chế độ nâng quyền.


## Liên quan

[**Exec tool** Thực thi lệnh shell từ tác tử. ](</vi/tools/exec>) [**Exec approvals** Hệ thống phê duyệt và danh sách cho phép cho `exec`. ](</vi/tools/exec-approvals>) [**Sandboxing** Cấu hình môi trường cách ly cấp Gateway. ](</vi/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Cách ba cổng kết hợp trong một lệnh gọi công cụ. ](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo