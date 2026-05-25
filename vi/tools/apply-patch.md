---
title: công cụ apply_patch
source_url: https://docs.openclaw.ai/vi/tools/apply-patch
scraped_at: 2026-05-25
---

Áp dụng thay đổi tệp bằng định dạng bản vá có cấu trúc. Cách này lý tưởng cho các chỉnh sửa nhiều tệp hoặc nhiều hunk khi một lệnh gọi `edit` duy nhất sẽ dễ hỏng.

Công cụ chấp nhận một chuỗi `input` duy nhất bao bọc một hoặc nhiều thao tác tệp:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Tham số

  * `input` (bắt buộc): Nội dung bản vá đầy đủ bao gồm `*** Begin Patch` và `*** End Patch`.


## Ghi chú

  * Đường dẫn bản vá hỗ trợ đường dẫn tương đối (từ thư mục workspace) và đường dẫn tuyệt đối.
  * `tools.exec.applyPatch.workspaceOnly` mặc định là `true` (giới hạn trong workspace). Chỉ đặt thành `false` nếu bạn cố ý muốn `apply_patch` ghi/xóa bên ngoài thư mục workspace.
  * Dùng `*** Move to:` trong một hunk `*** Update File:` để đổi tên tệp.
  * `*** End of File` đánh dấu một thao tác chèn chỉ EOF khi cần.
  * Có sẵn theo mặc định cho các mô hình OpenAI và OpenAI Codex. Đặt `tools.exec.applyPatch.enabled: false` để tắt.
  * Có thể tùy chọn giới hạn theo mô hình qua `tools.exec.applyPatch.allowModels`.
  * Cấu hình chỉ nằm dưới `tools.exec`.


## Ví dụ

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Liên quan

[**Diffs** Trình xem diff chỉ đọc để trình bày thay đổi. ](</vi/tools/diffs>) [**Exec tool** Thực thi lệnh shell từ agent. ](</vi/tools/exec>) [**Code execution** Phân tích Python từ xa trong sandbox với xAI. ](</vi/tools/code-execution>)

Was this useful?YesNo