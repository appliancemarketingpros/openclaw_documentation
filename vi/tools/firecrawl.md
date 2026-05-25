---
title: Firecrawl
source_url: https://docs.openclaw.ai/vi/tools/firecrawl
scraped_at: 2026-05-25
---

OpenClaw có thể sử dụng **Firecrawl** theo ba cách:

  * làm nhà cung cấp `web_search`
  * làm các công cụ Plugin tường minh: `firecrawl_search` và `firecrawl_scrape`
  * làm bộ trích xuất dự phòng cho `web_fetch`


Đây là dịch vụ trích xuất/tìm kiếm được lưu trữ, hỗ trợ vượt qua bot và bộ nhớ đệm, giúp ích cho các trang dùng nhiều JS hoặc các trang chặn yêu cầu fetch HTTP thông thường.

## Lấy khóa API

  1. Tạo tài khoản Firecrawl và tạo khóa API.
  2. Lưu khóa đó trong cấu hình hoặc đặt `FIRECRAWL_API_KEY` trong môi trường Gateway.


## Cấu hình tìm kiếm Firecrawl

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "firecrawl",      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webSearch: {            apiKey: "FIRECRAWL_API_KEY_HERE",            baseUrl: "https://api.firecrawl.dev",          },        },      },    },  },}
[/code]

Ghi chú:

  * Chọn Firecrawl trong onboarding hoặc `openclaw configure --section web` sẽ tự động bật Plugin Firecrawl được đóng gói kèm.
  * `web_search` với Firecrawl hỗ trợ `query` và `count`.
  * Với các điều khiển riêng của Firecrawl như `sources`, `categories`, hoặc thu thập kết quả, hãy dùng `firecrawl_search`.
  * `baseUrl` mặc định là Firecrawl được lưu trữ tại `https://api.firecrawl.dev`. Chỉ cho phép ghi đè tự lưu trữ đối với các endpoint riêng tư/nội bộ; HTTP chỉ được chấp nhận cho các đích riêng tư đó.
  * `FIRECRAWL_BASE_URL` là giá trị env dự phòng dùng chung cho URL cơ sở của tìm kiếm và thu thập Firecrawl.


## Cấu hình thu thập Firecrawl + dự phòng web_fetch

json5Copy code
[code]
    {  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "FIRECRAWL_API_KEY_HERE",            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 172800000,            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

Ghi chú:

  * Các lần thử dự phòng Firecrawl chỉ chạy khi có khóa API (`plugins.entries.firecrawl.config.webFetch.apiKey` hoặc `FIRECRAWL_API_KEY`).
  * `maxAgeMs` kiểm soát độ cũ tối đa của kết quả đã lưu trong bộ nhớ đệm (ms). Mặc định là 2 ngày.
  * Cấu hình cũ `tools.web.fetch.firecrawl.*` được `openclaw doctor --fix` tự động di trú.
  * Các ghi đè URL thu thập/cơ sở của Firecrawl tuân theo cùng quy tắc được lưu trữ/riêng tư như tìm kiếm: lưu lượng công khai được lưu trữ dùng `https://api.firecrawl.dev`; các ghi đè tự lưu trữ phải phân giải tới endpoint riêng tư/nội bộ.
  * `firecrawl_scrape` từ chối các URL đích rõ ràng là riêng tư, loopback, metadata và không phải HTTP(S) trước khi chuyển tiếp chúng tới Firecrawl, khớp với hợp đồng an toàn đích của `web_fetch` cho các lệnh gọi thu thập Firecrawl tường minh.


`firecrawl_scrape` dùng lại cùng các thiết lập `plugins.entries.firecrawl.config.webFetch.*` và biến env.

### Firecrawl tự lưu trữ

Đặt `plugins.entries.firecrawl.config.webSearch.baseUrl`, `plugins.entries.firecrawl.config.webFetch.baseUrl`, hoặc `FIRECRAWL_BASE_URL` khi bạn tự chạy Firecrawl. OpenClaw chỉ chấp nhận `http://` cho các đích loopback, mạng riêng tư, `.local`, `.internal`, hoặc `.localhost`. Máy chủ tùy chỉnh công khai bị từ chối để khóa API Firecrawl không bị vô tình gửi tới endpoint tùy ý.

## Công cụ Plugin Firecrawl

### `firecrawl_search`

Dùng mục này khi bạn muốn các điều khiển tìm kiếm riêng của Firecrawl thay vì `web_search` chung.

Tham số cốt lõi:

  * `query`
  * `count`
  * `sources`
  * `categories`
  * `scrapeResults`
  * `timeoutSeconds`


### `firecrawl_scrape`

Dùng mục này cho các trang dùng nhiều JS hoặc được bảo vệ khỏi bot, nơi `web_fetch` thông thường hoạt động yếu.

Tham số cốt lõi:

  * `url`
  * `extractMode`
  * `maxChars`
  * `onlyMainContent`
  * `maxAgeMs`
  * `proxy`
  * `storeInCache`
  * `timeoutSeconds`


## Ẩn mình / vượt qua bot

Firecrawl cung cấp tham số **chế độ proxy** để vượt qua bot (`basic`, `stealth`, hoặc `auto`). OpenClaw luôn dùng `proxy: "auto"` cùng với `storeInCache: true` cho các yêu cầu Firecrawl. Nếu proxy bị bỏ qua, Firecrawl mặc định dùng `auto`. `auto` thử lại bằng proxy ẩn mình nếu lần thử cơ bản thất bại, điều này có thể dùng nhiều tín dụng hơn so với thu thập chỉ dùng cơ bản.

## Cách `web_fetch` dùng Firecrawl

Thứ tự trích xuất của `web_fetch`:

  1. Readability (cục bộ)
  2. Firecrawl (nếu được chọn hoặc tự động phát hiện là dự phòng web-fetch đang hoạt động)
  3. Dọn dẹp HTML cơ bản (dự phòng cuối cùng)


Nút chọn là `tools.web.fetch.provider`. Nếu bạn bỏ qua, OpenClaw tự động phát hiện nhà cung cấp web-fetch sẵn sàng đầu tiên từ các thông tin xác thực có sẵn. Hiện tại nhà cung cấp được đóng gói kèm là Firecrawl.

## Liên quan

  * [Tổng quan Web Search](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [Web Fetch](</vi/tools/web-fetch>) \-- công cụ web_fetch với dự phòng Firecrawl
  * [Tavily](</vi/tools/tavily>) \-- công cụ tìm kiếm + trích xuất


Was this useful?YesNo