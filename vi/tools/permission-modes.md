---
title: Chế độ quyền truy cập
source_url: https://docs.openclaw.ai/vi/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

Các chế độ quyền quyết định tác nhân có bao nhiêu thẩm quyền trước khi có thể chạy lệnh host, ghi tệp, hoặc yêu cầu harness backend cấp thêm quyền truy cập. Bắt đầu với `tools.exec.mode: "auto"` khi bạn muốn OpenClaw dùng danh sách cho phép trước, rồi đến tự động đánh giá gốc của Codex hoặc tuyến phê duyệt của con người cho các trường hợp không khớp.

## Mặc định được khuyến nghị

Dùng `auto` cho các tác nhân lập trình cần quyền truy cập host hữu ích mà không biến mọi trường hợp không khớp thành prompt cho con người:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

Sau đó xác minh chính sách hiệu lực:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

Ở chế độ `auto`, OpenClaw chạy trực tiếp các kết quả khớp danh sách cho phép mang tính xác định. Các trường hợp phê duyệt không khớp sẽ đi qua trình tự động đánh giá gốc của OpenClaw trước, rồi chuyển về tuyến phê duyệt của con người đã cấu hình khi cần.

## Chế độ host exec của OpenClaw

`tools.exec.mode` là bề mặt chính sách đã chuẩn hóa cho host `exec`.

Chế độ | Hành vi | Dùng khi  
---|---|---  
`deny` | Chặn host exec. | Không lệnh host nào được phép.  
`allowlist` | Chỉ chạy các lệnh trong danh sách cho phép. | Bạn có một tập lệnh đã biết là an toàn.  
`ask` | Chạy các kết quả khớp danh sách cho phép và hỏi khi không khớp. | Con người nên xem xét các lệnh mới.  
`auto` | Chạy các kết quả khớp danh sách cho phép, rồi dùng tự động đánh giá. | Phiên lập trình cần quyền truy cập thực tế có kiểm soát.  
`full` | Chạy host exec không cần prompt. | Host/phiên đáng tin cậy này nên bỏ qua các cổng phê duyệt.  
  
Để xem chính sách host exec đầy đủ, tệp phê duyệt cục bộ, schema danh sách cho phép, các binary an toàn, và hành vi chuyển tiếp, hãy xem [Phê duyệt exec](</vi/tools/exec-approvals>).

## Ánh xạ Codex Guardian

Đối với các phiên app-server Codex gốc, `tools.exec.mode: "auto"` ánh xạ tới phê duyệt do Codex Guardian đánh giá khi các yêu cầu Codex cục bộ cho phép. OpenClaw thường gửi:

Trường Codex | Giá trị điển hình  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
Ở chế độ `auto`, OpenClaw không giữ lại các ghi đè Codex cũ không an toàn như `approvalPolicy: "never"` hoặc `sandbox: "danger-full-access"`. Chỉ dùng `tools.exec.mode: "full"` khi bạn chủ ý muốn tư thế không cần phê duyệt.

Để biết cách thiết lập app-server, thứ tự xác thực, và chi tiết runtime Codex gốc, hãy xem [Harness Codex](</vi/plugins/codex-harness>).

## Quyền harness ACPX

Các phiên ACPX không tương tác, nên chúng không thể nhấp vào prompt quyền TTY. ACPX dùng các thiết lập cấp harness riêng dưới `plugins.entries.acpx.config`:

Thiết lập | Giá trị phổ biến | Ý nghĩa  
---|---|---  
`permissionMode` | `approve-reads` | Chỉ tự động phê duyệt thao tác đọc.  
`permissionMode` | `approve-all` | Tự động phê duyệt thao tác ghi và lệnh shell.  
`permissionMode` | `deny-all` | Từ chối mọi prompt quyền.  
`nonInteractivePermissions` | `fail` | Hủy khi cần có prompt.  
`nonInteractivePermissions` | `deny` | Từ chối prompt và tiếp tục khi có thể.  
  
Thiết lập quyền ACPX riêng với phê duyệt exec của OpenClaw:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

Dùng `approve-all` như lựa chọn khẩn cấp tương đương với một phiên harness không cần prompt của ACPX. Để biết chi tiết thiết lập và các chế độ lỗi, hãy xem [Thiết lập tác nhân ACP](</vi/tools/acp-agents-setup#permission-configuration>).

## Chọn một chế độ

Mục tiêu | Cấu hình  
---|---  
Chặn hoàn toàn các lệnh host | `tools.exec.mode: "deny"`  
Chỉ cho các lệnh đã biết là an toàn chạy | `tools.exec.mode: "allowlist"`  
Hỏi con người cho mọi dạng lệnh mới | `tools.exec.mode: "ask"`  
Dùng tự động đánh giá Codex/OpenClaw trước con người | `tools.exec.mode: "auto"`  
Bỏ qua hoàn toàn phê duyệt host exec | `tools.exec.mode: "full"` cộng với tệp phê duyệt host khớp  
Cho phiên ACPX không tương tác ghi/exec | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
Nếu một lệnh vẫn hiện prompt hoặc thất bại sau khi đổi chế độ, hãy kiểm tra cả hai lớp:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

Host exec dùng kết quả nghiêm ngặt hơn giữa cấu hình OpenClaw và tệp phê duyệt cục bộ của host. Quyền harness ACPX không nới lỏng phê duyệt host exec, và phê duyệt host exec không nới lỏng prompt harness ACPX.

## Liên quan

  * [Phê duyệt exec](</vi/tools/exec-approvals>)
  * [Phê duyệt exec - nâng cao](</vi/tools/exec-approvals-advanced>)
  * [Harness Codex](</vi/plugins/codex-harness>)
  * [Thiết lập tác nhân ACP](</vi/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue