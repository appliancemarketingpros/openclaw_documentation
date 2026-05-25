---
title: Thực thi mã
source_url: https://docs.openclaw.ai/vi/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` chạy phân tích Python từ xa trong sandbox trên Responses API của xAI. Công cụ này được đăng ký bởi Plugin `xai` được đóng gói kèm (theo hợp đồng `tools`) và gửi yêu cầu đến cùng endpoint `https://api.x.ai/v1/responses` được `x_search` sử dụng.

Thuộc tính | Giá trị  
---|---  
Tên công cụ | `code_execution`  
Plugin nhà cung cấp | `xai` (được đóng gói kèm, `enabledByDefault: true`)  
Xác thực | hồ sơ xác thực xAI, `XAI_API_KEY`, hoặc `plugins.entries.xai.config.webSearch.apiKey`  
Mô hình mặc định | `grok-4-1-fast`  
Thời gian chờ mặc định | 30 giây  
`maxTurns` mặc định | chưa đặt (xAI áp dụng giới hạn nội bộ riêng)  
  
Công cụ này khác với [`exec`](</vi/tools/exec>) cục bộ:

  * `exec` chạy lệnh shell trên máy của bạn hoặc Node đã ghép nối.
  * `code_execution` chạy Python trong sandbox từ xa của xAI.


Dùng `code_execution` cho:

  * Tính toán.
  * Lập bảng.
  * Thống kê nhanh.
  * Phân tích kiểu biểu đồ.
  * Phân tích dữ liệu do `x_search` hoặc `web_search` trả về.


**Không** dùng công cụ này khi bạn cần tệp cục bộ, shell của bạn, repo của bạn, hoặc thiết bị đã ghép nối. Hãy dùng [`exec`](</vi/tools/exec>) cho việc đó.

## Thiết lập

* ### Cung cấp khóa API xAI

Chạy `openclaw onboard --auth-choice xai-api-key` cho `code_execution` và `x_search`, hoặc đặt `XAI_API_KEY` / cấu hình khóa trong Plugin xAI khi bạn cũng muốn tìm kiếm web Grok dùng cùng thông tin xác thực:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Hoặc qua cấu hình:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Bật và tinh chỉnh code_execution

Công cụ này được kiểm soát bởi `plugins.entries.xai.config.codeExecution.enabled`. Mặc định là tắt.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Khởi động lại Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` xuất hiện trong danh sách công cụ của agent sau khi Plugin xAI đăng ký lại với `enabled: true`.

## Cách sử dụng

Hỏi một cách tự nhiên và nêu rõ ý định phân tích:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Công cụ nhận một tham số `task` duy nhất ở bên trong, nên agent nên gửi toàn bộ yêu cầu phân tích và mọi dữ liệu nội tuyến trong một prompt.

## Lỗi

Khi công cụ chạy mà không có xác thực, nó trả về lỗi `missing_xai_api_key` có cấu trúc, trỏ đến các tùy chọn hồ sơ xác thực, biến môi trường và cấu hình. Lỗi là JSON, không phải ngoại lệ được ném ra, nên agent có thể tự sửa:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Giới hạn

  * Đây là thực thi từ xa của xAI, không phải thực thi tiến trình cục bộ.
  * Xem kết quả là phân tích tạm thời, không phải một phiên notebook bền vững.
  * Đừng giả định có quyền truy cập tệp cục bộ hoặc workspace của bạn.
  * Đối với dữ liệu X mới, trước tiên hãy dùng [`x_search`](</vi/tools/web#x_search>) rồi chuyển kết quả vào `code_execution`.


## Liên quan

[**Công cụ Exec** Thực thi shell cục bộ trên máy của bạn hoặc Node đã ghép nối. ](</vi/tools/exec>) [**Phê duyệt Exec** Chính sách cho phép/từ chối đối với thực thi shell. ](</vi/tools/exec-approvals>) [**Công cụ web** `web_search`, `x_search`, và `web_fetch`. ](</vi/tools/web>) [**Nhà cung cấp xAI** Mô hình Grok, tìm kiếm web/X và cấu hình thực thi mã. ](</vi/providers/xai>)

Was this useful?YesNo