---
title: Tìm kiếm song song
source_url: https://docs.openclaw.ai/vi/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Plugin Parallel cung cấp hai nhà cung cấp `web_search` của [Parallel](<https://parallel.ai/>):

  * **Parallel Search (Miễn phí)** (`parallel-free`) -- [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) miễn phí của Parallel. Không yêu cầu tài khoản hoặc khóa API. Chọn rõ tùy chọn này khi bạn muốn đường dẫn tìm kiếm được Parallel lưu trữ và không cần khóa.
  * **Parallel Search** (`parallel`) -- Search API trả phí của Parallel. Yêu cầu `PARALLEL_API_KEY` và cung cấp giới hạn tốc độ cao hơn cùng khả năng tinh chỉnh mục tiêu.


Cả hai đều trả về các đoạn trích được xếp hạng, tối ưu cho LLM từ một chỉ mục web được xây dựng cho tác tử AI. Đặt `tools.web.search.provider` thành `parallel-free` hoặc `parallel` để chọn một tùy chọn một cách rõ ràng.

## Cài đặt Plugin

Cài đặt Plugin chính thức, sau đó khởi động lại Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## Khóa API (nhà cung cấp trả phí)

`parallel-free` không yêu cầu khóa API, nhưng vẫn phải được chọn làm nhà cung cấp được quản lý. Nhà cung cấp trả phí `parallel` cần một khóa API:

* ### Tạo tài khoản

Đăng ký tại [platform.parallel.ai](<https://platform.parallel.ai>) và tạo khóa API từ bảng điều khiển của bạn.

* ### Lưu khóa

Đặt `PARALLEL_API_KEY` trong môi trường Gateway, hoặc cấu hình qua:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Cấu hình

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Phương án thay thế bằng môi trường:** đặt `PARALLEL_API_KEY` trong môi trường Gateway. Đối với bản cài đặt gateway, đặt nó trong `~/.openclaw/.env`.

## Ghi đè URL cơ sở

Ghi đè URL cơ sở chỉ áp dụng cho nhà cung cấp trả phí `parallel`. Nhà cung cấp miễn phí `parallel-free` luôn dùng `https://search.parallel.ai/mcp`.

Đặt `plugins.entries.parallel.config.webSearch.baseUrl` khi các yêu cầu Parallel cần đi qua proxy tương thích hoặc endpoint Parallel thay thế (ví dụ: Cloudflare AI Gateway). OpenClaw chuẩn hóa các máy chủ trần bằng cách thêm `https://` ở đầu và thêm `/v1/search` trừ khi đường dẫn đã kết thúc bằng phần đó. Endpoint đã phân giải được đưa vào khóa bộ nhớ đệm tìm kiếm, nên kết quả từ các endpoint Parallel khác nhau sẽ không được chia sẻ.

## Tham số công cụ

OpenClaw hiển thị dạng tìm kiếm gốc của Parallel để mô hình có thể điền cả mục tiêu bằng ngôn ngữ tự nhiên và một vài truy vấn từ khóa ngắn — sự kết hợp mà Parallel [khuyến nghị](<https://docs.parallel.ai/search/best-practices>) để có kết quả tốt nhất.

Mô tả bằng ngôn ngữ tự nhiên về câu hỏi hoặc mục tiêu nền tảng (tối đa 5000 ký tự). Nên tự đầy đủ ngữ cảnh.

Các truy vấn tìm kiếm từ khóa ngắn gọn, mỗi truy vấn 3-6 từ (1-5 mục, tối đa 200 ký tự mỗi mục). Cung cấp 2-3 truy vấn đa dạng để có kết quả tốt nhất.

Số kết quả cần trả về (1-40).

ID phiên Parallel tùy chọn (tối đa 1000 ký tự trên `parallel`; Search MCP miễn phí `parallel-free` giới hạn ở 100). Truyền `sessionId` từ một kết quả Parallel trước đó trong các tìm kiếm tiếp theo thuộc cùng tác vụ để Parallel có thể nhóm các lệnh gọi liên quan và cải thiện kết quả sau đó. ID vượt quá giới hạn sẽ bị bỏ và một ID mới sẽ được tạo.

Mã định danh tùy chọn của mô hình thực hiện lệnh gọi (ví dụ: `claude-opus-4-7`, `gpt-5.5`). Cho phép Parallel điều chỉnh các thiết lập mặc định theo năng lực của mô hình. Truyền đúng slug mô hình đang hoạt động; không rút gọn thành bí danh họ mô hình.

## Ghi chú

  * Parallel xếp hạng và nén kết quả dựa trên mức độ hữu ích cho suy luận LLM, không phải tỷ lệ nhấp của con người; hãy kỳ vọng các đoạn trích dày đặc trong từng kết quả thay vì nội dung toàn trang
  * Các đoạn trích kết quả được trả về dưới dạng mảng `excerpts` và cũng được nối vào trường `description` để tương thích với hợp đồng `web_search` chung
  * Parallel trả về `session_id` trong mọi phản hồi; OpenClaw hiển thị nó dưới dạng `sessionId` trong payload công cụ để bên gọi có thể nhóm các tìm kiếm tiếp theo
  * `searchId`, `warnings`, và `usage` từ Parallel được chuyển tiếp khi có mặt
  * OpenClaw luôn chuyển tiếp số lượng kết quả đã phân giải đến Parallel dưới dạng `advanced_settings.max_results`. Đối số `count` của bên gọi được ưu tiên, sau đó là thiết lập cấp cao nhất `tools.web.search.maxResults`, nếu không thì dùng mặc định `web_search` chung của OpenClaw (5). Điều này giữ cho khối lượng kết quả nhất quán khi chuyển đổi giữa các nhà cung cấp; riêng Parallel mặc định là 10
  * Kết quả được lưu vào bộ nhớ đệm trong 15 phút theo mặc định (có thể cấu hình qua `cacheTtlMinutes`)
  * Nhà cung cấp miễn phí `parallel-free` chấp nhận cùng các tham số. Nó áp dụng `count` ở phía máy khách và tạo `session_id` cho mỗi lệnh gọi khi không được cung cấp.


## Liên quan

  * [Tổng quan Tìm kiếm web](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [Tìm kiếm Exa](</vi/tools/exa-search>) \-- tìm kiếm neural với trích xuất nội dung
  * [Tìm kiếm Perplexity](</vi/tools/perplexity-search>) \-- kết quả có cấu trúc với lọc miền


Was this useful?YesNo

Open issue