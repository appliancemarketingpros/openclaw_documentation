---
title: Tài liệu
source_url: https://docs.openclaw.ai/vi/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Tìm kiếm chỉ mục tài liệu OpenClaw trực tiếp từ terminal. Lệnh này gọi endpoint tìm kiếm MCP của tài liệu công khai do Mintlify lưu trữ tại `https://docs.openclaw.ai/mcp.SearchOpenClaw` và hiển thị kết quả trong terminal của bạn.

## Cách dùng

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Đối số:

Đối số | Mô tả  
---|---  
`[query...]` | Truy vấn tìm kiếm dạng tự do. Truy vấn nhiều từ được nối bằng dấu cách và gửi như một truy vấn.  
  
## Ví dụ

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Khi không có truy vấn, `openclaw docs` in URL điểm vào tài liệu cùng một lệnh tìm kiếm mẫu thay vì chạy tìm kiếm.

## Cách hoạt động

`openclaw docs` gọi CLI `mcporter` để gọi công cụ tìm kiếm MCP của tài liệu, sau đó phân tích các khối `Title: / Link: / Content:` từ đầu ra của công cụ thành danh sách kết quả.

Để phân giải `mcporter`, OpenClaw kiểm tra theo thứ tự:

  1. `mcporter` trên `PATH` (được dùng trực tiếp nếu có).
  2. `pnpm dlx mcporter ...` nếu đã cài đặt `pnpm`.
  3. `npx -y mcporter ...` nếu đã cài đặt `npx`.


Nếu không có tùy chọn nào khả dụng, lệnh thất bại kèm gợi ý cài đặt `pnpm` (`npm install -g pnpm`).

Lệnh gọi tìm kiếm dùng thời gian chờ cố định 30 giây. Đoạn trích kết quả được rút gọn còn khoảng 220 ký tự cho mỗi mục.

## Đầu ra

Trong terminal hỗ trợ định dạng phong phú (TTY), kết quả hiển thị dưới dạng một tiêu đề, theo sau là danh sách gạch đầu dòng. Mỗi gạch đầu dòng hiển thị tiêu đề trang, URL tài liệu được liên kết và một đoạn trích ngắn ở dòng tiếp theo. Kết quả trống in "Không có kết quả.".

Trong đầu ra không hỗ trợ định dạng phong phú (được pipe, `--no-color`, script), cùng dữ liệu đó được hiển thị dưới dạng Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Mã thoát

Mã | Ý nghĩa  
---|---  
`0` | Tìm kiếm thành công (bao gồm cả phản hồi không có kết quả).  
`1` | Lệnh gọi công cụ MCP thất bại; stderr được in trực tiếp.  
  
## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Tài liệu trực tiếp](<https://docs.openclaw.ai>)


Was this useful?YesNo