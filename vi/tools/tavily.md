---
title: Tavily
source_url: https://docs.openclaw.ai/vi/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) là một API tìm kiếm được thiết kế cho các ứng dụng AI. OpenClaw cung cấp API này theo hai cách:

  * dưới dạng nhà cung cấp `web_search` cho công cụ tìm kiếm chung
  * dưới dạng các công cụ Plugin rõ ràng: `tavily_search` và `tavily_extract`


Tavily trả về kết quả có cấu trúc được tối ưu hóa để LLM sử dụng, với độ sâu tìm kiếm có thể cấu hình, lọc theo chủ đề, bộ lọc miền, tóm tắt câu trả lời do AI tạo và trích xuất nội dung từ URL (bao gồm cả các trang được render bằng JavaScript).

Thuộc tính | Giá trị  
---|---  
ID Plugin | `tavily`  
Xác thực | `TAVILY_API_KEY` hoặc cấu hình `apiKey`  
URL cơ sở | `https://api.tavily.com` (mặc định)  
Công cụ đi kèm | `tavily_search`, `tavily_extract`  
  
## Bắt đầu

* ### Get an API key

Tạo tài khoản Tavily tại [tavily.com](<https://tavily.com>), rồi tạo một khóa API trong bảng điều khiển.

* ### Configure the plugin and provider

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verify search runs

Kích hoạt một `web_search` từ bất kỳ agent nào, hoặc gọi trực tiếp `tavily_search`.

## Tham chiếu công cụ

### `tavily_search`

Dùng công cụ này khi bạn muốn các tùy chọn điều khiển tìm kiếm riêng của Tavily thay vì `web_search` chung.

Tham số | Kiểu | Ràng buộc / mặc định | Mô tả  
---|---|---|---  
`query` | string | bắt buộc | Chuỗi truy vấn tìm kiếm. Giữ dưới 400 ký tự.  
`search_depth` | enum | `basic` (mặc định), `advanced` | `advanced` chậm hơn nhưng có độ liên quan cao hơn.  
`topic` | enum | `general` (mặc định), `news`, `finance` | Lọc theo nhóm chủ đề.  
`max_results` | integer | 1-20 | Số lượng kết quả.  
`include_answer` | boolean | mặc định `false` | Bao gồm tóm tắt câu trả lời do AI của Tavily tạo.  
`time_range` | enum | `day`, `week`, `month`, `year` | Lọc kết quả theo độ mới.  
`include_domains` | string array | (không có) | Chỉ bao gồm kết quả từ các miền này.  
`exclude_domains` | string array | (không có) | Loại trừ kết quả từ các miền này.  
  
Đánh đổi về độ sâu tìm kiếm:

Độ sâu | Tốc độ | Độ liên quan | Phù hợp nhất cho  
---|---|---|---  
`basic` | Nhanh hơn | Cao | Truy vấn mục đích chung (mặc định).  
`advanced` | Chậm hơn | Cao nhất | Nghiên cứu chính xác và xác minh dữ kiện.  
  
### `tavily_extract`

Dùng công cụ này để trích xuất nội dung sạch từ một hoặc nhiều URL. Xử lý các trang được render bằng JavaScript và hỗ trợ chia đoạn tập trung theo truy vấn để trích xuất có mục tiêu.

Tham số | Kiểu | Ràng buộc / mặc định | Mô tả  
---|---|---|---  
`urls` | string array | bắt buộc, 1-20 | URL để trích xuất nội dung từ đó.  
`query` | string | (tùy chọn) | Xếp hạng lại các đoạn trích xuất theo mức liên quan đến truy vấn này.  
`extract_depth` | enum | `basic` (mặc định), `advanced` | Dùng `advanced` cho các trang nặng JS, SPA hoặc bảng động.  
`chunks_per_source` | integer | 1-5; **yêu cầu`query`** | Số đoạn trả về cho mỗi URL. Gây lỗi nếu đặt mà không có `query`.  
`include_images` | boolean | mặc định `false` | Bao gồm URL hình ảnh trong kết quả.  
  
Đánh đổi về độ sâu trích xuất:

Độ sâu | Khi nào nên dùng  
---|---  
`basic` | Trang đơn giản. Thử tùy chọn này trước.  
`advanced` | SPA được render bằng JS, nội dung động, bảng.  
  
## Chọn công cụ phù hợp

Nhu cầu | Công cụ  
---|---  
Tìm kiếm web nhanh, không cần tùy chọn đặc biệt | `web_search`  
Tìm kiếm với độ sâu, chủ đề, câu trả lời AI | `tavily_search`  
Trích xuất nội dung từ các URL cụ thể | `tavily_extract`  
  
## Cấu hình nâng cao

API key resolution order

Client Tavily tra cứu khóa API theo thứ tự sau:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (được phân giải thông qua SecretRefs).
  2. `TAVILY_API_KEY` từ môi trường Gateway.


`tavily_extract` báo lỗi thiết lập nếu không có mục nào trong hai mục trên.

Custom base URL

Ghi đè `plugins.entries.tavily.config.webSearch.baseUrl` nếu bạn đưa Tavily qua proxy. Giá trị mặc định là `https://api.tavily.com`.

`chunks_per_source` requires `query`

`tavily_extract` từ chối các lệnh gọi truyền `chunks_per_source` mà không có `query`. Tavily xếp hạng các đoạn theo mức liên quan của truy vấn, nên tham số này vô nghĩa nếu thiếu truy vấn.

## Liên quan

[**Web Search overview** Tất cả nhà cung cấp và quy tắc tự động phát hiện. ](</vi/tools/web>) [**Firecrawl** Tìm kiếm kết hợp scraping với trích xuất nội dung. ](</vi/tools/firecrawl>) [**Exa Search** Tìm kiếm neural với trích xuất nội dung. ](</vi/tools/exa-search>) [**Configuration** Schema cấu hình đầy đủ cho mục nhập Plugin và định tuyến công cụ. ](</vi/gateway/configuration>)

Was this useful?YesNo