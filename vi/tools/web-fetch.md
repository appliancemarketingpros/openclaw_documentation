---
title: Tìm nạp web
source_url: https://docs.openclaw.ai/vi/tools/web-fetch
scraped_at: 2026-05-25
---

Công cụ `web_fetch` thực hiện HTTP GET thuần túy và trích xuất nội dung dễ đọc (HTML sang markdown hoặc văn bản). Công cụ này **không** thực thi JavaScript.

Đối với các trang dùng nhiều JS hoặc trang được bảo vệ bằng đăng nhập, hãy dùng [Web Browser](</vi/tools/browser>) thay thế.

## Bắt đầu nhanh

`web_fetch` được **bật theo mặc định** \-- không cần cấu hình. Agent có thể gọi ngay:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Tham số công cụ

URL cần tìm nạp. Chỉ hỗ trợ `http(s)`.

Định dạng đầu ra sau khi trích xuất nội dung chính.

Cắt ngắn đầu ra xuống số ký tự này.

## Cách hoạt động

* ### Fetch

Gửi HTTP GET với User-Agent giống Chrome và header `Accept-Language`. Chặn tên máy chủ riêng tư/nội bộ và kiểm tra lại chuyển hướng.

* ### Extract

Chạy Readability (trích xuất nội dung chính) trên phản hồi HTML.

* ### Fallback (optional)

Nếu Readability thất bại và Firecrawl đã được cấu hình, thử lại thông qua API Firecrawl với chế độ vượt qua bot.

* ### Cache

Kết quả được lưu vào bộ nhớ đệm trong 15 phút (có thể cấu hình) để giảm việc tìm nạp lặp lại cùng một URL.

## Cấu hình

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Dự phòng Firecrawl

Nếu trích xuất Readability thất bại, `web_fetch` có thể chuyển sang [Firecrawl](</vi/tools/firecrawl>) để vượt qua bot và trích xuất tốt hơn:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` hỗ trợ các đối tượng SecretRef. Cấu hình `tools.web.fetch.firecrawl.*` cũ được `openclaw doctor --fix` tự động di chuyển.

Hành vi runtime hiện tại:

  * `tools.web.fetch.provider` chọn rõ ràng nhà cung cấp dự phòng cho việc tìm nạp.
  * Nếu bỏ qua `provider`, OpenClaw tự động phát hiện nhà cung cấp web-fetch sẵn sàng đầu tiên từ các thông tin xác thực khả dụng. `web_fetch` không sandbox có thể dùng các Plugin đã cài đặt khai báo `contracts.webFetchProviders` và đăng ký một nhà cung cấp khớp tại runtime. Hiện nay nhà cung cấp đi kèm là Firecrawl.
  * Các lệnh gọi `web_fetch` trong sandbox vẫn chỉ giới hạn ở các nhà cung cấp đi kèm.
  * Nếu Readability bị tắt, `web_fetch` bỏ qua thẳng tới phương án dự phòng của nhà cung cấp đã chọn. Nếu không có nhà cung cấp nào khả dụng, nó thất bại đóng.


## Proxy env tin cậy

Nếu triển khai của bạn yêu cầu `web_fetch` đi qua một proxy HTTP(S) outbound tin cậy, hãy đặt `tools.web.fetch.useTrustedEnvProxy: true`.

Ở chế độ này, OpenClaw vẫn áp dụng kiểm tra SSRF dựa trên tên máy chủ trước khi gửi yêu cầu, nhưng cho phép proxy phân giải DNS thay vì ghim DNS cục bộ. Chỉ bật tùy chọn này khi proxy do operator kiểm soát và thực thi chính sách outbound sau khi phân giải DNS.

## Giới hạn và an toàn

  * `maxChars` bị giới hạn theo `tools.web.fetch.maxCharsCap`
  * Nội dung phản hồi bị giới hạn ở `maxResponseBytes` trước khi phân tích; phản hồi quá lớn sẽ bị cắt ngắn kèm cảnh báo
  * Tên máy chủ riêng tư/nội bộ bị chặn
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` và `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` là các tùy chọn tham gia hẹp cho các ngăn xếp proxy IP giả tin cậy; hãy để chúng chưa đặt trừ khi proxy của bạn sở hữu các dải tổng hợp đó và thực thi chính sách đích riêng của nó
  * Chuyển hướng được kiểm tra và giới hạn bởi `maxRedirects`
  * `useTrustedEnvProxy` là tùy chọn tham gia rõ ràng và chỉ nên được bật cho các proxy do operator kiểm soát vẫn thực thi chính sách outbound sau khi phân giải DNS
  * `web_fetch` hoạt động theo nỗ lực tối đa -- một số trang cần [Web Browser](</vi/tools/browser>)


## Hồ sơ công cụ

Nếu bạn dùng hồ sơ công cụ hoặc allowlist, hãy thêm `web_fetch` hoặc `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Liên quan

  * [Web Search](</vi/tools/web>) \-- tìm kiếm web bằng nhiều nhà cung cấp
  * [Web Browser](</vi/tools/browser>) \-- tự động hóa trình duyệt đầy đủ cho các trang dùng nhiều JS
  * [Firecrawl](</vi/tools/firecrawl>) \-- công cụ tìm kiếm và scrape của Firecrawl


Was this useful?YesNo