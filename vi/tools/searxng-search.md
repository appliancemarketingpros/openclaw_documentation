---
title: Tìm kiếm SearXNG
source_url: https://docs.openclaw.ai/vi/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ [SearXNG](<https://docs.searxng.org/>) làm nhà cung cấp `web_search` **tự lưu trữ, không cần khóa**. SearXNG là một công cụ siêu tìm kiếm mã nguồn mở tổng hợp kết quả từ Google, Bing, DuckDuckGo và các nguồn khác.

Ưu điểm:

  * **Miễn phí và không giới hạn** \-- không cần khóa API hoặc gói đăng ký thương mại
  * **Quyền riêng tư / air-gap** \-- truy vấn không bao giờ rời khỏi mạng của bạn
  * **Hoạt động ở mọi nơi** \-- không có hạn chế khu vực trên các API tìm kiếm thương mại


## Thiết lập

* ### Run a SearXNG instance

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Hoặc dùng bất kỳ bản triển khai SearXNG hiện có nào mà bạn có quyền truy cập. Xem [tài liệu SearXNG](<https://docs.searxng.org/>) để thiết lập cho môi trường sản xuất.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Hoặc đặt biến môi trường và để tính năng tự động phát hiện tìm thấy nó:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Cấu hình

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Cài đặt cấp Plugin cho phiên bản SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Trường `baseUrl` cũng chấp nhận các đối tượng SecretRef.

Quy tắc truyền tải:

  * `https://` hoạt động cho các máy chủ SearXNG công khai hoặc riêng tư
  * `http://` chỉ được chấp nhận cho các máy chủ mạng riêng đáng tin cậy hoặc loopback
  * máy chủ SearXNG công khai phải dùng `https://`
  * máy chủ riêng tư/nội bộ dùng bộ bảo vệ mạng tự lưu trữ; máy chủ `https://` công khai vẫn ở bộ bảo vệ tìm kiếm web nghiêm ngặt và không thể chuyển hướng đến địa chỉ riêng tư


## Biến môi trường

Đặt `SEARXNG_BASE_URL` làm phương án thay thế cho cấu hình:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Khi `SEARXNG_BASE_URL` được đặt và không có nhà cung cấp rõ ràng nào được cấu hình, tính năng tự động phát hiện sẽ tự động chọn SearXNG (ở mức ưu tiên thấp nhất -- bất kỳ nhà cung cấp dựa trên API nào có khóa sẽ thắng trước).

## Tham chiếu cấu hình Plugin

Trường | Mô tả  
---|---  
`baseUrl` | URL cơ sở của phiên bản SearXNG của bạn (bắt buộc)  
`categories` | Các danh mục phân tách bằng dấu phẩy như `general`, `news` hoặc `science`  
`language` | Mã ngôn ngữ cho kết quả như `en`, `de` hoặc `fr`  
  
## Ghi chú

  * **JSON API** \-- dùng endpoint `format=json` gốc của SearXNG, không phải quét HTML
  * **URL kết quả hình ảnh** \-- kết quả danh mục hình ảnh bao gồm `img_src` khi SearXNG trả về URL hình ảnh trực tiếp
  * **Không cần khóa API** \-- hoạt động ngay với bất kỳ phiên bản SearXNG nào
  * **Xác thực URL cơ sở** \-- `baseUrl` phải là URL `http://` hoặc `https://` hợp lệ; máy chủ công khai phải dùng `https://`
  * **Bộ bảo vệ mạng** \-- các endpoint SearXNG riêng tư/nội bộ chọn tham gia quyền truy cập mạng riêng; các endpoint SearXNG `https://` công khai giữ cơ chế bảo vệ SSRF nghiêm ngặt
  * **Thứ tự tự động phát hiện** \-- SearXNG được kiểm tra cuối cùng (thứ tự 200) trong tự động phát hiện. Các nhà cung cấp dựa trên API có khóa đã cấu hình chạy trước, sau đó là DuckDuckGo (thứ tự 100), rồi Ollama Web Search (thứ tự 110)
  * **Tự lưu trữ** \-- bạn kiểm soát phiên bản, truy vấn và các công cụ tìm kiếm upstream
  * **Danh mục** mặc định là `general` khi chưa được cấu hình
  * **Dự phòng danh mục** \-- nếu một yêu cầu danh mục không phải `general` thành công nhưng trả về không có kết quả nào, OpenClaw thử lại cùng truy vấn một lần với `general` trước khi trả về tập kết quả rỗng


## Liên quan

  * [Tổng quan Web Search](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [DuckDuckGo Search](</vi/tools/duckduckgo-search>) \-- một phương án dự phòng khác không cần khóa
  * [Brave Search](</vi/tools/brave-search>) \-- kết quả có cấu trúc với bậc miễn phí


Was this useful?YesNo