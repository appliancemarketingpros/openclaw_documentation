---
title: Định dạng Markdown
source_url: https://docs.openclaw.ai/vi/concepts/markdown-formatting
scraped_at: 2026-05-25
---

OpenClaw định dạng Markdown đầu ra bằng cách chuyển đổi nó thành một biểu diễn trung gian dùng chung (IR) trước khi kết xuất đầu ra dành riêng cho từng kênh. IR giữ nguyên văn bản nguồn trong khi mang theo các đoạn kiểu dáng/liên kết để việc chia đoạn và kết xuất có thể luôn nhất quán trên các kênh.

## Mục tiêu

  * **Tính nhất quán:** một bước phân tích cú pháp, nhiều bộ kết xuất.
  * **Chia đoạn an toàn:** chia văn bản trước khi kết xuất để định dạng nội tuyến không bao giờ bị đứt qua các đoạn.
  * **Phù hợp với kênh:** ánh xạ cùng một IR sang Slack mrkdwn, Telegram HTML và các phạm vi kiểu của Signal mà không phân tích lại Markdown.


## Quy trình

  1. **Phân tích Markdown - > IR**
     * IR là văn bản thuần cộng với các đoạn kiểu (bold/italic/strike/code/spoiler) và các đoạn liên kết.
     * Offset là đơn vị mã UTF-16 để các phạm vi kiểu của Signal khớp với API của nó.
     * Bảng chỉ được phân tích khi một kênh chọn chuyển đổi bảng.
  2. **Chia đoạn IR (ưu tiên định dạng)**
     * Việc chia đoạn diễn ra trên văn bản IR trước khi kết xuất.
     * Định dạng nội tuyến không bị chia qua các đoạn; các span được cắt theo từng đoạn.
  3. **Kết xuất theo từng kênh**
     * **Slack:** token mrkdwn (bold/italic/strike/code), liên kết dạng `<url|label>`.
     * **Telegram:** thẻ HTML (`<b>`, `<i>`, `<s>`, `<code>`, `<pre><code>`, `<a href>`).
     * **Signal:** văn bản thuần + phạm vi `text-style`; liên kết trở thành `label (url)` khi nhãn khác.


## Ví dụ IR

Markdown đầu vào:

markdownCopy code
[code]
    Hello **world** - see [docs](https://docs.openclaw.ai).
[/code]

IR (sơ đồ):

jsonCopy code
[code]
    {  "text": "Hello world - see docs.",  "styles": [{ "start": 6, "end": 11, "style": "bold" }],  "links": [{ "start": 19, "end": 23, "href": "https://docs.openclaw.ai" }]}
[/code]

## Nơi được sử dụng

  * Các adapter đầu ra của Slack, Telegram và Signal kết xuất từ IR.
  * Các kênh khác (WhatsApp, iMessage, Microsoft Teams, Discord) vẫn dùng văn bản thuần hoặc quy tắc định dạng riêng, với chuyển đổi bảng Markdown được áp dụng trước khi chia đoạn khi được bật.


## Xử lý bảng

Bảng Markdown không được hỗ trợ nhất quán trên các ứng dụng chat. Dùng `markdown.tables` để kiểm soát chuyển đổi theo từng kênh (và từng tài khoản).

  * `code`: kết xuất bảng dưới dạng khối mã (mặc định cho hầu hết kênh).
  * `bullets`: chuyển mỗi hàng thành các gạch đầu dòng (mặc định cho Matrix, Signal và WhatsApp).
  * `off`: tắt phân tích và chuyển đổi bảng; văn bản bảng thô được chuyển qua.


Khóa cấu hình:

yamlCopy code
[code]
    channels:  discord:    markdown:      tables: code    accounts:      work:        markdown:          tables: off
[/code]

## Quy tắc chia đoạn

  * Giới hạn đoạn đến từ adapter/cấu hình kênh và được áp dụng cho văn bản IR.
  * Hàng rào mã được giữ nguyên như một khối duy nhất kèm dấu xuống dòng cuối để các kênh kết xuất chính xác.
  * Tiền tố danh sách và tiền tố trích dẫn khối là một phần của văn bản IR, nên việc chia đoạn không cắt giữa tiền tố.
  * Kiểu nội tuyến (bold/italic/strike/inline-code/spoiler) không bao giờ bị chia qua các đoạn; bộ kết xuất mở lại kiểu bên trong từng đoạn.


Nếu bạn cần thêm thông tin về hành vi chia đoạn trên các kênh, xem [Streaming + chia đoạn](</vi/concepts/streaming>).

## Chính sách liên kết

  * **Slack:** `[label](url)` -> `<url|label>`; URL trần vẫn giữ nguyên. Autolink bị tắt trong quá trình phân tích để tránh liên kết kép.
  * **Telegram:** `[label](url)` -> `<a href="url">label</a>` (chế độ phân tích HTML).
  * **Signal:** `[label](url)` -> `label (url)` trừ khi nhãn khớp với URL.


## Nội dung ẩn

Dấu nội dung ẩn (`||spoiler||`) chỉ được phân tích cho Signal, nơi chúng ánh xạ tới các phạm vi kiểu SPOILER. Các kênh khác coi chúng là văn bản thuần.

## Cách thêm hoặc cập nhật bộ định dạng kênh

  1. **Phân tích một lần:** dùng helper dùng chung `markdownToIR(...)` với các tùy chọn phù hợp với kênh (autolink, kiểu tiêu đề, tiền tố trích dẫn khối).
  2. **Kết xuất:** triển khai bộ kết xuất với `renderMarkdownWithMarkers(...)` và một bản đồ marker kiểu (hoặc phạm vi kiểu Signal).
  3. **Chia đoạn:** gọi `chunkMarkdownIR(...)` trước khi kết xuất; kết xuất từng đoạn.
  4. **Nối adapter:** cập nhật adapter đầu ra của kênh để dùng bộ chia đoạn và bộ kết xuất mới.
  5. **Kiểm thử:** thêm hoặc cập nhật kiểm thử định dạng và kiểm thử gửi đầu ra nếu kênh dùng chia đoạn.


## Lỗi thường gặp

  * Token ngoặc nhọn của Slack (`<@U123>`, `<#C123>`, `<https://...>`) phải được giữ nguyên; escape HTML thô một cách an toàn.
  * Telegram HTML yêu cầu escape văn bản bên ngoài thẻ để tránh markup bị hỏng.
  * Phạm vi kiểu của Signal phụ thuộc vào offset UTF-16; không dùng offset điểm mã.
  * Giữ dấu xuống dòng cuối cho khối mã có hàng rào để marker đóng nằm trên dòng riêng của chúng.


## Liên quan

[**Streaming và chia đoạn** Hành vi streaming đầu ra, ranh giới đoạn và phân phối dành riêng cho từng kênh. ](</vi/concepts/streaming>) [**Lời nhắc hệ thống** Những gì mô hình thấy trước cuộc hội thoại, bao gồm cả các tệp workspace được chèn. ](</vi/concepts/system-prompt>)

Was this useful?YesNo