---
title: Quy ước về phần giữ chỗ bí mật
source_url: https://docs.openclaw.ai/vi/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Quy ước placeholder cho bí mật

Sử dụng placeholder mà con người có thể đọc được nhưng không giống bí mật thật.

## Kiểu khuyến nghị

  * Ưu tiên các giá trị mô tả như `example-openai-key-not-real` hoặc `example-discord-bot-token`.
  * Với đoạn mã shell, ưu tiên `${OPENAI_API_KEY}` thay vì chuỗi nội tuyến giống token.
  * Giữ ví dụ rõ ràng là giả và giới hạn theo mục đích (nhà cung cấp, kênh, loại xác thực).


## Tránh các mẫu này trong tài liệu

  * Văn bản header hoặc footer khóa riêng tư PEM nguyên văn.
  * Tiền tố giống thông tin xác thực đang hoạt động, ví dụ `sk-...`, `xoxb-...`, `AKIA...`.
  * Bearer token trông thực tế được sao chép từ nhật ký runtime.


## Ví dụ

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue