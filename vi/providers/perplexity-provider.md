---
title: Perplexity
source_url: https://docs.openclaw.ai/vi/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity cung cấp khả năng tìm kiếm web thông qua Perplexity Search API hoặc Perplexity Sonar qua OpenRouter.

Thuộc tính | Giá trị  
---|---  
Loại | Nhà cung cấp tìm kiếm web (không phải nhà cung cấp mô hình)  
Xác thực | `PERPLEXITY_API_KEY` (trực tiếp) hoặc `OPENROUTER_API_KEY` (qua OpenRouter)  
Đường dẫn cấu hình | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Bắt đầu

* ### Đặt khóa API

Chạy luồng cấu hình tìm kiếm web tương tác:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Hoặc đặt khóa trực tiếp:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Bắt đầu tìm kiếm

Tác nhân sẽ tự động sử dụng Perplexity cho các lượt tìm kiếm web sau khi khóa được cấu hình. Không cần thêm bước nào.

## Chế độ tìm kiếm

Plugin tự động chọn phương thức truyền tải dựa trên tiền tố khóa API:

### API Perplexity gốc (pplx-)

Khi khóa của bạn bắt đầu bằng `pplx-`, OpenClaw sử dụng Perplexity Search API gốc. Phương thức truyền tải này trả về kết quả có cấu trúc và hỗ trợ bộ lọc tên miền, ngôn ngữ và ngày (xem các tùy chọn lọc bên dưới).

### OpenRouter / Sonar (sk-or-)

Khi khóa của bạn bắt đầu bằng `sk-or-`, OpenClaw định tuyến qua OpenRouter bằng mô hình Perplexity Sonar. Phương thức truyền tải này trả về câu trả lời do AI tổng hợp kèm trích dẫn.

Tiền tố khóa | Phương thức truyền tải | Tính năng  
---|---|---  
`pplx-` | Perplexity Search API gốc | Kết quả có cấu trúc, bộ lọc tên miền/ngôn ngữ/ngày  
`sk-or-` | OpenRouter (Sonar) | Câu trả lời do AI tổng hợp kèm trích dẫn  
  
## Lọc API gốc

Khi dùng Perplexity API gốc, lượt tìm kiếm hỗ trợ các bộ lọc sau:

Bộ lọc | Mô tả | Ví dụ  
---|---|---  
Quốc gia | Mã quốc gia gồm 2 chữ cái | `us`, `de`, `jp`  
Ngôn ngữ | Mã ngôn ngữ ISO 639-1 | `en`, `fr`, `zh`  
Khoảng ngày | Khoảng thời gian gần đây | `day`, `week`, `month`, `year`  
Bộ lọc tên miền | Danh sách cho phép hoặc danh sách chặn (tối đa 20 tên miền) | `example.com`  
Ngân sách nội dung | Giới hạn token cho mỗi phản hồi / mỗi trang | `max_tokens`, `max_tokens_per_page`  
  
## Cấu hình nâng cao

Biến môi trường cho tiến trình daemon

Nếu OpenClaw Gateway chạy như một daemon (launchd/systemd), hãy đảm bảo `PERPLEXITY_API_KEY` có sẵn cho tiến trình đó.

Thiết lập proxy OpenRouter

Nếu bạn muốn định tuyến tìm kiếm Perplexity qua OpenRouter, hãy đặt `OPENROUTER_API_KEY` (tiền tố `sk-or-`) thay vì khóa Perplexity gốc. OpenClaw sẽ phát hiện tiền tố và tự động chuyển sang phương thức truyền tải Sonar.

## Liên quan

[**Công cụ tìm kiếm Perplexity** Cách tác nhân gọi tìm kiếm Perplexity và diễn giải kết quả. ](</vi/tools/perplexity-search>) [**Tham chiếu cấu hình** Tham chiếu cấu hình đầy đủ bao gồm các mục nhập Plugin. ](</vi/gateway/configuration-reference>)

Was this useful?YesNo