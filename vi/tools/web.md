---
title: Tìm kiếm trên web
source_url: https://docs.openclaw.ai/vi/tools/web
scraped_at: 2026-05-25
---

Công cụ `web_search` tìm kiếm trên web bằng provider đã cấu hình của bạn và trả về kết quả. Kết quả được lưu vào bộ nhớ đệm theo truy vấn trong 15 phút (có thể cấu hình).

OpenClaw cũng bao gồm `x_search` cho bài đăng trên X (trước đây là Twitter) và `web_fetch` để lấy URL nhẹ. Trong giai đoạn này, `web_fetch` vẫn chạy cục bộ trong khi `web_search` và `x_search` có thể dùng xAI Responses ở bên dưới.

## Bắt đầu nhanh

* ### Choose a provider

Chọn một provider và hoàn tất mọi thiết lập bắt buộc. Một số provider không cần khóa, trong khi các provider khác dùng khóa API. Xem các trang provider bên dưới để biết chi tiết.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web
[/code]

Thao tác này lưu provider và mọi thông tin xác thực cần thiết. Bạn cũng có thể đặt một biến môi trường (ví dụ `BRAVE_API_KEY`) và bỏ qua bước này đối với các provider dựa trên API.

* ### Use it

Agent giờ có thể gọi `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Với bài đăng X, dùng:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Chọn provider

[**Brave Search** Kết quả có cấu trúc kèm đoạn trích. Hỗ trợ chế độ `llm-context`, bộ lọc quốc gia/ngôn ngữ. Có gói miễn phí. ](</vi/tools/brave-search>) [**DuckDuckGo** Phương án dự phòng không cần khóa. Không cần khóa API. Tích hợp không chính thức dựa trên HTML. ](</vi/tools/duckduckgo-search>) [**Exa** Tìm kiếm neural + từ khóa với trích xuất nội dung (điểm nổi bật, văn bản, tóm tắt). ](</vi/tools/exa-search>) [**Firecrawl** Kết quả có cấu trúc. Phù hợp nhất khi dùng cùng `firecrawl_search` và `firecrawl_scrape` để trích xuất sâu. ](</vi/tools/firecrawl>) [**Gemini** Câu trả lời do AI tổng hợp kèm trích dẫn thông qua nền tảng Google Search. ](</vi/tools/gemini-search>) [**Grok** Câu trả lời do AI tổng hợp kèm trích dẫn thông qua nền tảng web của xAI. ](</vi/tools/grok-search>) [**Kimi** Câu trả lời do AI tổng hợp kèm trích dẫn thông qua tìm kiếm web Moonshot; các dự phòng chat không có nền tảng tham chiếu sẽ thất bại rõ ràng. ](</vi/tools/kimi-search>) [**MiniMax Search** Kết quả có cấu trúc thông qua API tìm kiếm MiniMax Token Plan. ](</vi/tools/minimax-search>) [**Ollama Web Search** Tìm kiếm thông qua máy chủ Ollama cục bộ đã đăng nhập hoặc API Ollama được lưu trữ. ](</vi/tools/ollama-search>) [**Perplexity** Kết quả có cấu trúc với các điều khiển trích xuất nội dung và lọc miền. ](</vi/tools/perplexity-search>) [**SearXNG** Meta-search tự lưu trữ. Không cần khóa API. Tổng hợp Google, Bing, DuckDuckGo và nhiều nguồn khác. ](</vi/tools/searxng-search>) [**Tavily** Kết quả có cấu trúc với độ sâu tìm kiếm, lọc chủ đề và `tavily_extract` để trích xuất URL. ](</vi/tools/tavily>)

### So sánh provider

Provider | Kiểu kết quả | Bộ lọc | Khóa API  
---|---|---|---  
[Brave](</vi/tools/brave-search>) | Đoạn trích có cấu trúc | Quốc gia, ngôn ngữ, thời gian, chế độ `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</vi/tools/duckduckgo-search>) | Đoạn trích có cấu trúc | \-- | Không có (không cần khóa)  
[Exa](</vi/tools/exa-search>) | Có cấu trúc + đã trích xuất | Chế độ neural/từ khóa, ngày, trích xuất nội dung | `EXA_API_KEY`  
[Firecrawl](</vi/tools/firecrawl>) | Đoạn trích có cấu trúc | Thông qua công cụ `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</vi/tools/gemini-search>) | Do AI tổng hợp + trích dẫn | \-- | `GEMINI_API_KEY`  
[Grok](</vi/tools/grok-search>) | Do AI tổng hợp + trích dẫn | \-- | `XAI_API_KEY`  
[Kimi](</vi/tools/kimi-search>) | Do AI tổng hợp + trích dẫn; thất bại với các dự phòng chat không có nền tảng tham chiếu | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</vi/tools/minimax-search>) | Đoạn trích có cấu trúc | Khu vực (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</vi/tools/ollama-search>) | Đoạn trích có cấu trúc | \-- | Không có với máy chủ cục bộ đã đăng nhập; `OLLAMA_API_KEY` cho tìm kiếm trực tiếp `https://ollama.com`  
[Perplexity](</vi/tools/perplexity-search>) | Đoạn trích có cấu trúc | Quốc gia, ngôn ngữ, thời gian, miền, giới hạn nội dung | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</vi/tools/searxng-search>) | Đoạn trích có cấu trúc | Danh mục, ngôn ngữ | Không có (tự lưu trữ)  
[Tavily](</vi/tools/tavily>) | Đoạn trích có cấu trúc | Thông qua công cụ `tavily_search` | `TAVILY_API_KEY`  
  
## Tự động phát hiện

## Tìm kiếm web OpenAI gốc

Các mô hình OpenAI Responses trực tiếp tự động dùng công cụ `web_search` được OpenAI lưu trữ khi tìm kiếm web OpenClaw được bật và không có provider được quản lý nào được ghim. Đây là hành vi do provider sở hữu trong Plugin OpenAI đi kèm và chỉ áp dụng cho lưu lượng API OpenAI gốc, không áp dụng cho URL cơ sở proxy tương thích OpenAI hoặc tuyến Azure. Đặt `tools.web.search.provider` thành một provider khác như `brave` để giữ công cụ `web_search` được quản lý cho các mô hình OpenAI, hoặc đặt `tools.web.search.enabled: false` để tắt cả tìm kiếm được quản lý lẫn tìm kiếm OpenAI gốc.

## Tìm kiếm web Codex gốc

Các mô hình hỗ trợ Codex có thể tùy chọn dùng công cụ `web_search` Responses gốc của provider thay cho hàm `web_search` được quản lý của OpenClaw.

  * Cấu hình dưới `tools.web.search.openaiCodex`
  * Chỉ kích hoạt cho các mô hình hỗ trợ Codex (`openai-codex/*` hoặc các provider dùng `api: "openai-codex-responses"`)
  * `web_search` được quản lý vẫn áp dụng cho các mô hình không phải Codex
  * `mode: "cached"` là cài đặt mặc định và được khuyến nghị
  * `tools.web.search.enabled: false` tắt cả tìm kiếm được quản lý lẫn tìm kiếm gốc

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Nếu tìm kiếm Codex gốc được bật nhưng mô hình hiện tại không hỗ trợ Codex, OpenClaw giữ hành vi `web_search` được quản lý bình thường.

## An toàn mạng

Các lệnh gọi provider `web_search` được quản lý dùng đường dẫn fetch được bảo vệ của OpenClaw. Với các máy chủ API provider đáng tin cậy, OpenClaw cho phép các câu trả lời DNS fake-IP của Surge, Clash và sing-box trong `198.18.0.0/15` và `fc00::/7` chỉ cho hostname của provider đó. Các đích private, local loopback, link-local và metadata khác vẫn bị chặn.

Cấp phép tự động này không áp dụng cho các URL `web_fetch` tùy ý. Với `web_fetch`, chỉ bật `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` và `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` một cách rõ ràng khi proxy đáng tin cậy của bạn sở hữu các dải tổng hợp đó.

## Thiết lập tìm kiếm web

Danh sách provider trong tài liệu và luồng thiết lập được sắp xếp theo bảng chữ cái. Tự động phát hiện giữ một thứ tự ưu tiên riêng.

Nếu không đặt `provider`, OpenClaw kiểm tra các provider theo thứ tự này và dùng provider đầu tiên đã sẵn sàng:

Provider dựa trên API trước:

  1. **Brave** \-- `BRAVE_API_KEY` hoặc `plugins.entries.brave.config.webSearch.apiKey` (thứ tự 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` hoặc `plugins.entries.minimax.config.webSearch.apiKey` (thứ tự 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY`, hoặc `models.providers.google.apiKey` (thứ tự 20)
  4. **Grok** \-- `XAI_API_KEY` hoặc `plugins.entries.xai.config.webSearch.apiKey` (thứ tự 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` hoặc `plugins.entries.moonshot.config.webSearch.apiKey` (thứ tự 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` hoặc `plugins.entries.perplexity.config.webSearch.apiKey` (thứ tự 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` hoặc `plugins.entries.firecrawl.config.webSearch.apiKey` (thứ tự 60)
  8. **Exa** \-- `EXA_API_KEY` hoặc `plugins.entries.exa.config.webSearch.apiKey`; tùy chọn `plugins.entries.exa.config.webSearch.baseUrl` ghi đè endpoint Exa (thứ tự 65)
  9. **Tavily** \-- `TAVILY_API_KEY` hoặc `plugins.entries.tavily.config.webSearch.apiKey` (thứ tự 70)


Các phương án dự phòng không cần khóa sau đó:

  10. **DuckDuckGo** \-- phương án dự phòng HTML không cần khóa, không cần tài khoản hoặc khóa API (thứ tự 100)
  11. **Ollama Web Search** \-- phương án dự phòng không cần khóa thông qua máy chủ Ollama cục bộ đã cấu hình của bạn khi nó có thể truy cập và đã đăng nhập bằng `ollama signin`; có thể dùng lại xác thực bearer của provider Ollama khi máy chủ cần, và có thể gọi tìm kiếm trực tiếp `https://ollama.com` khi được cấu hình với `OLLAMA_API_KEY` (thứ tự 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` hoặc `plugins.entries.searxng.config.webSearch.baseUrl` (thứ tự 200)


Nếu không phát hiện provider nào, nó dự phòng về Brave (bạn sẽ nhận được lỗi thiếu khóa nhắc bạn cấu hình một khóa).

## Cấu hình

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Cấu hình dành riêng cho nhà cung cấp (khóa API, URL cơ sở, chế độ) nằm trong `plugins.entries.<plugin>.config.webSearch.*`. Gemini cũng có thể tái sử dụng `models.providers.google.apiKey` và `models.providers.google.baseUrl` làm phương án dự phòng có mức ưu tiên thấp hơn sau cấu hình web-search chuyên dụng của nó và `GEMINI_API_KEY`. Xem các trang nhà cung cấp để biết ví dụ.

`tools.web.search.provider` được xác thực dựa trên các ID nhà cung cấp web-search được khai báo bởi manifest của plugin đi kèm và đã cài đặt. Lỗi gõ sai như `"brvae"` sẽ khiến xác thực cấu hình thất bại thay vì âm thầm quay về tự động phát hiện. Nếu một nhà cung cấp đã cấu hình chỉ có bằng chứng plugin cũ, chẳng hạn như một khối `plugins.entries.<plugin>` còn sót lại sau khi gỡ cài đặt plugin bên thứ ba, OpenClaw giữ cho quá trình khởi động ổn định và báo cảnh báo để bạn có thể cài đặt lại plugin hoặc chạy `openclaw doctor --fix` để dọn cấu hình cũ.

Việc chọn nhà cung cấp dự phòng `web_fetch` là riêng biệt:

  * chọn bằng `tools.web.fetch.provider`
  * hoặc bỏ qua trường đó và để OpenClaw tự động phát hiện nhà cung cấp web-fetch sẵn sàng đầu tiên từ các thông tin xác thực hiện có
  * `web_fetch` không chạy trong sandbox có thể dùng các nhà cung cấp plugin đã cài đặt khai báo `contracts.webFetchProviders`; các lần fetch trong sandbox chỉ dùng nhà cung cấp đi kèm
  * hiện nay nhà cung cấp web-fetch đi kèm là Firecrawl, được cấu hình trong `plugins.entries.firecrawl.config.webFetch.*`


Khi bạn chọn **Kimi** trong `openclaw onboard` hoặc `openclaw configure --section web`, OpenClaw cũng có thể hỏi về:

  * khu vực API Moonshot (`https://api.moonshot.ai/v1` hoặc `https://api.moonshot.cn/v1`)
  * mô hình web-search Kimi mặc định (mặc định là `kimi-k2.6`)


Đối với `x_search`, cấu hình `plugins.entries.xai.config.xSearch.*`. Nó dùng cùng hồ sơ xác thực xAI như chat, hoặc thông tin xác thực web-search `XAI_API_KEY` / plugin được Grok web search sử dụng. Cấu hình cũ `tools.web.x_search.*` được `openclaw doctor --fix` tự động di trú. Khi bạn chọn Grok trong `openclaw onboard` hoặc `openclaw configure --section web`, OpenClaw cũng có thể cung cấp bước thiết lập `x_search` tùy chọn với cùng khóa. Đây là bước tiếp theo riêng bên trong luồng Grok, không phải lựa chọn nhà cung cấp web-search cấp cao nhất riêng. Nếu bạn chọn nhà cung cấp khác, OpenClaw sẽ không hiển thị lời nhắc `x_search`.

### Lưu trữ khóa API

### Tệp cấu hình

Chạy `openclaw configure --section web` hoặc đặt khóa trực tiếp:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Biến môi trường

Đặt biến môi trường của nhà cung cấp trong môi trường tiến trình Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Đối với bản cài đặt gateway, đặt biến đó trong `~/.openclaw/.env`. Xem [Biến môi trường](</vi/help/faq#env-vars-and-env-loading>).

## Tham số công cụ

Tham số | Mô tả  
---|---  
`query` | Truy vấn tìm kiếm (bắt buộc)  
`count` | Số kết quả trả về (1-10, mặc định: 5)  
`country` | Mã quốc gia ISO gồm 2 chữ cái (ví dụ: "US", "DE")  
`language` | Mã ngôn ngữ ISO 639-1 (ví dụ: "en", "de")  
`search_lang` | Mã ngôn ngữ tìm kiếm (chỉ Brave)  
`freshness` | Bộ lọc thời gian: `day`, `week`, `month`, hoặc `year`  
`date_after` | Kết quả sau ngày này (YYYY-MM-DD)  
`date_before` | Kết quả trước ngày này (YYYY-MM-DD)  
`ui_lang` | Mã ngôn ngữ UI (chỉ Brave)  
`domain_filter` | Mảng danh sách cho phép/chặn miền (chỉ Perplexity)  
`max_tokens` | Tổng ngân sách nội dung, mặc định 25000 (chỉ Perplexity)  
`max_tokens_per_page` | Giới hạn token mỗi trang, mặc định 2048 (chỉ Perplexity)  
  
## x_search

`x_search` truy vấn bài đăng X (trước đây là Twitter) bằng xAI và trả về câu trả lời do AI tổng hợp kèm trích dẫn. Nó chấp nhận truy vấn ngôn ngữ tự nhiên và các bộ lọc có cấu trúc tùy chọn. OpenClaw chỉ bật công cụ `x_search` xAI tích hợp trên yêu cầu phục vụ lời gọi công cụ này.

### Cấu hình x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` gửi POST đến `<baseUrl>/responses` khi `plugins.entries.xai.config.xSearch.baseUrl` được đặt. Nếu trường đó bị bỏ qua, nó quay về `plugins.entries.xai.config.webSearch.baseUrl`, rồi đến `tools.web.search.grok.baseUrl` cũ, và cuối cùng là endpoint xAI công khai.

### Tham số x_search

Tham số | Mô tả  
---|---  
`query` | Truy vấn tìm kiếm (bắt buộc)  
`allowed_x_handles` | Giới hạn kết quả ở các handle X cụ thể  
`excluded_x_handles` | Loại trừ các handle X cụ thể  
`from_date` | Chỉ bao gồm bài đăng vào hoặc sau ngày này (YYYY-MM-DD)  
`to_date` | Chỉ bao gồm bài đăng vào hoặc trước ngày này (YYYY-MM-DD)  
`enable_image_understanding` | Cho phép xAI kiểm tra hình ảnh đính kèm bài đăng khớp  
`enable_video_understanding` | Cho phép xAI kiểm tra video đính kèm bài đăng khớp  
  
### Ví dụ x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Ví dụ

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Hồ sơ công cụ

Nếu bạn dùng hồ sơ công cụ hoặc danh sách cho phép, hãy thêm `web_search`, `x_search`, hoặc `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Liên quan

  * [Web Fetch](</vi/tools/web-fetch>) \-- fetch một URL và trích xuất nội dung dễ đọc
  * [Web Browser](</vi/tools/browser>) \-- tự động hóa trình duyệt đầy đủ cho các site dùng nhiều JS
  * [Grok Search](</vi/tools/grok-search>) \-- Grok làm nhà cung cấp `web_search`
  * [Ollama Web Search](</vi/tools/ollama-search>) \-- tìm kiếm web không cần khóa thông qua máy chủ Ollama của bạn


Was this useful?YesNo