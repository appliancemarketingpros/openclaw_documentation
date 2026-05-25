---
title: Tìm kiếm MiniMax
source_url: https://docs.openclaw.ai/vi/tools/minimax-search
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ MiniMax như một nhà cung cấp `web_search` thông qua API tìm kiếm MiniMax Token Plan. API này trả về kết quả tìm kiếm có cấu trúc với tiêu đề, URL, đoạn trích và truy vấn liên quan.

## Lấy thông tin xác thực Token Plan

* ### Create a key

Tạo hoặc sao chép khóa MiniMax Token Plan từ [MiniMax Platform](<https://platform.minimax.io/user-center/basic-information/interface-key>). Các thiết lập OAuth có thể dùng lại `MINIMAX_OAUTH_TOKEN` thay thế.

* ### Store the key

Đặt `MINIMAX_CODE_PLAN_KEY` trong môi trường Gateway, hoặc cấu hình qua:

bashCopy code
[code]
    openclaw configure --section web
[/code]

OpenClaw cũng chấp nhận `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` và `MINIMAX_API_KEY` làm bí danh env. `MINIMAX_API_KEY` nên trỏ tới thông tin xác thực Token Plan đã bật tìm kiếm; các khóa API mô hình MiniMax thông thường có thể không được endpoint tìm kiếm Token Plan chấp nhận.

## Cấu hình

json5Copy code
[code]
    {  plugins: {    entries: {      minimax: {        config: {          webSearch: {            apiKey: "sk-cp-...", // optional if a MiniMax Token Plan env var is set            region: "global", // or "cn"          },        },      },    },  },  tools: {    web: {      search: {        provider: "minimax",      },    },  },}
[/code]

**Phương án môi trường:** đặt `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` hoặc `MINIMAX_API_KEY` trong môi trường Gateway. Đối với một bản cài đặt gateway, đặt nó trong `~/.openclaw/.env`.

## Chọn khu vực

MiniMax Search sử dụng các endpoint sau:

  * Toàn cầu: `https://api.minimax.io/v1/coding_plan/search`
  * CN: `https://api.minimaxi.com/v1/coding_plan/search`


Nếu `plugins.entries.minimax.config.webSearch.region` chưa được đặt, OpenClaw phân giải khu vực theo thứ tự này:

  1. `tools.web.search.minimax.region` / `webSearch.region` do plugin sở hữu
  2. `MINIMAX_API_HOST`
  3. `models.providers.minimax.baseUrl`
  4. `models.providers.minimax-portal.baseUrl`


Điều đó có nghĩa là quy trình onboarding CN hoặc `MINIMAX_API_HOST=https://api.minimaxi.com/...` sẽ tự động giữ MiniMax Search trên máy chủ CN.

Ngay cả khi bạn đã xác thực MiniMax thông qua đường dẫn OAuth `minimax-portal`, tìm kiếm web vẫn đăng ký với provider id `minimax`; URL cơ sở của nhà cung cấp OAuth được dùng làm gợi ý khu vực để chọn máy chủ CN/toàn cầu, và `MINIMAX_OAUTH_TOKEN` có thể đáp ứng thông tin xác thực bearer cho MiniMax Search.

## Tham số được hỗ trợ

Tham số | Kiểu | Ràng buộc | Mô tả  
---|---|---|---  
`query` | string | bắt buộc | Chuỗi truy vấn tìm kiếm.  
`count` | integer | 1-10 | Số kết quả cần trả về. OpenClaw cắt ngắn danh sách trả về theo kích thước này.  
  
Các bộ lọc dành riêng cho nhà cung cấp hiện chưa được hỗ trợ.

## Liên quan

  * [Tổng quan Web Search](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [MiniMax](</vi/providers/minimax>) \-- thiết lập mô hình, hình ảnh, giọng nói và xác thực


Was this useful?YesNo