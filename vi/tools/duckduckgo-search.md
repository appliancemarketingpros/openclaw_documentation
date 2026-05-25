---
title: Tìm kiếm DuckDuckGo
source_url: https://docs.openclaw.ai/vi/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ DuckDuckGo làm nhà cung cấp `web_search` **không cần khóa**. Không cần khóa API hoặc tài khoản.

## Thiết lập

Không cần khóa API - chỉ cần đặt DuckDuckGo làm nhà cung cấp của bạn:

* ### Cấu hình

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Cấu hình

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Các cài đặt tùy chọn ở cấp Plugin cho vùng và SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Tham số công cụ

Truy vấn tìm kiếm.

Số kết quả trả về (1-10).

Mã vùng DuckDuckGo (ví dụ: `us-en`, `uk-en`, `de-de`).

Mức SafeSearch.

Vùng và SafeSearch cũng có thể được đặt trong cấu hình Plugin (xem ở trên) - các tham số công cụ ghi đè giá trị cấu hình cho từng truy vấn.

## Ghi chú

  * **Không cần khóa API** \- hoạt động ngay, không cần cấu hình
  * **Thử nghiệm** \- thu thập kết quả từ các trang tìm kiếm HTML không dùng JavaScript của DuckDuckGo, không phải API hoặc SDK chính thức
  * **Rủi ro thử thách bot** \- DuckDuckGo có thể phục vụ CAPTCHA hoặc chặn yêu cầu khi sử dụng nhiều hoặc tự động hóa
  * **Phân tích cú pháp HTML** \- kết quả phụ thuộc vào cấu trúc trang, có thể thay đổi mà không báo trước
  * **Thứ tự tự động phát hiện** \- DuckDuckGo là phương án dự phòng không cần khóa đầu tiên (thứ tự 100) trong tự động phát hiện. Các nhà cung cấp dựa trên API có khóa đã cấu hình sẽ chạy trước, sau đó là Ollama Web Search (thứ tự 110), rồi SearXNG (thứ tự 200)
  * **SafeSearch mặc định là moderate** khi chưa được cấu hình


## Liên quan

  * [Tổng quan Web Search](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [Brave Search](</vi/tools/brave-search>) \-- kết quả có cấu trúc với gói miễn phí
  * [Exa Search](</vi/tools/exa-search>) \-- tìm kiếm neural với trích xuất nội dung


Was this useful?YesNo