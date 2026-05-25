---
title: Tìm kiếm Perplexity
source_url: https://docs.openclaw.ai/vi/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ Perplexity Search API làm nhà cung cấp `web_search`. API này trả về kết quả có cấu trúc với các trường `title`, `url` và `snippet`.

Để tương thích, OpenClaw cũng hỗ trợ các thiết lập Perplexity Sonar/OpenRouter cũ. Nếu bạn dùng `OPENROUTER_API_KEY`, khóa `sk-or-...` trong `plugins.entries.perplexity.config.webSearch.apiKey`, hoặc đặt `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, nhà cung cấp sẽ chuyển sang đường dẫn chat-completions và trả về câu trả lời do AI tổng hợp kèm trích dẫn thay vì kết quả Search API có cấu trúc.

## Lấy khóa Perplexity API

  1. Tạo tài khoản Perplexity tại [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Tạo khóa API trong bảng điều khiển
  3. Lưu khóa trong cấu hình hoặc đặt `PERPLEXITY_API_KEY` trong môi trường Gateway.


## Tương thích OpenRouter

Nếu bạn đã dùng OpenRouter cho Perplexity Sonar, hãy giữ `provider: "perplexity"` và đặt `OPENROUTER_API_KEY` trong môi trường Gateway, hoặc lưu khóa `sk-or-...` trong `plugins.entries.perplexity.config.webSearch.apiKey`.

Điều khiển tương thích tùy chọn:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Ví dụ cấu hình

### Perplexity Search API gốc

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Tương thích OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Nơi đặt khóa

**Qua cấu hình:** chạy `openclaw configure --section web`. Lệnh này lưu khóa trong `~/.openclaw/openclaw.json` dưới `plugins.entries.perplexity.config.webSearch.apiKey`. Trường đó cũng chấp nhận các đối tượng SecretRef.

**Qua môi trường:** đặt `PERPLEXITY_API_KEY` hoặc `OPENROUTER_API_KEY` trong môi trường tiến trình Gateway. Với bản cài đặt gateway, đặt khóa trong `~/.openclaw/.env` (hoặc môi trường dịch vụ của bạn). Xem [Biến môi trường](</vi/help/faq#env-vars-and-env-loading>).

Nếu `provider: "perplexity"` được cấu hình và SecretRef của khóa Perplexity không phân giải được mà không có dự phòng env, quá trình khởi động/tải lại sẽ thất bại ngay.

## Tham số công cụ

Các tham số này áp dụng cho đường dẫn Perplexity Search API gốc.

Truy vấn tìm kiếm.

Số lượng kết quả cần trả về (1-10).

Mã quốc gia ISO gồm 2 chữ cái (ví dụ: `US`, `DE`).

Mã ngôn ngữ ISO 639-1 (ví dụ: `en`, `de`, `fr`).

Bộ lọc thời gian - `day` là 24 giờ.

Chỉ các kết quả được xuất bản sau ngày này (`YYYY-MM-DD`).

Chỉ các kết quả được xuất bản trước ngày này (`YYYY-MM-DD`).

Mảng danh sách cho phép/từ chối miền (tối đa 20).

Tổng ngân sách nội dung (tối đa 1000000).

Giới hạn token trên mỗi trang.

Đối với đường dẫn tương thích Sonar/OpenRouter cũ:

  * `query`, `count` và `freshness` được chấp nhận
  * `count` chỉ để tương thích ở đó; phản hồi vẫn là một câu trả lời được tổng hợp kèm trích dẫn thay vì danh sách N kết quả
  * Các bộ lọc chỉ dành cho Search API như `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` và `max_tokens_per_page` trả về lỗi rõ ràng


**Ví dụ:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Quy tắc bộ lọc miền

  * Tối đa 20 miền cho mỗi bộ lọc
  * Không thể trộn danh sách cho phép và danh sách từ chối trong cùng một yêu cầu
  * Dùng tiền tố `-` cho các mục danh sách từ chối (ví dụ: `["-reddit.com"]`)


## Ghi chú

  * Perplexity Search API trả về kết quả tìm kiếm web có cấu trúc (`title`, `url`, `snippet`)
  * OpenRouter hoặc `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` rõ ràng sẽ chuyển Perplexity trở lại Sonar chat completions để tương thích
  * Tương thích Sonar/OpenRouter trả về một câu trả lời được tổng hợp kèm trích dẫn, không phải các hàng kết quả có cấu trúc
  * Kết quả được lưu vào bộ nhớ đệm trong 15 phút theo mặc định (có thể cấu hình qua `cacheTtlMinutes`)


## Liên quan

[**Web search overview** Tất cả nhà cung cấp và quy tắc tự động phát hiện. ](</vi/tools/web>) [**Brave search** Kết quả có cấu trúc với bộ lọc quốc gia và ngôn ngữ. ](</vi/tools/brave-search>) [**Exa search** Tìm kiếm neural với trích xuất nội dung. ](</vi/tools/exa-search>) [**Perplexity Search API docs** Hướng dẫn bắt đầu nhanh và tài liệu tham khảo chính thức của Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo