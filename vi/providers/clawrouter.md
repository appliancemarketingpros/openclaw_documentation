---
title: ClawRouter
source_url: https://docs.openclaw.ai/vi/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter cung cấp cho OpenClaw một khóa có phạm vi theo chính sách cho nhiều nhà cung cấp mô hình thượng nguồn. Plugin đi kèm chỉ phát hiện các mô hình được phép cho khóa đó, định tuyến từng mô hình qua giao thức đã khai báo của nó, và báo cáo ngân sách cùng mức sử dụng tổng hợp của khóa trên các bề mặt sử dụng của OpenClaw.

Bạn không cài đặt hoặc xác thực từng Plugin nhà cung cấp thượng nguồn trên máy chủ OpenClaw. Thông tin xác thực thượng nguồn và chuyển tiếp theo từng nhà cung cấp vẫn nằm trong ClawRouter. OpenClaw chỉ cần Plugin `@openclaw/clawrouter` đi kèm và một thông tin xác thực ClawRouter đã được cấp.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `clawrouter`  
Gói | `@openclaw/clawrouter`  
Xác thực | `CLAWROUTER_API_KEY`  
URL mặc định | `https://clawrouter.openclaw.ai`  
Danh mục mô hình | Phạm vi theo thông tin xác thực qua `/v1/catalog`  
Hạn mức | Ngân sách hằng tháng và mức sử dụng qua `/v1/usage`  
  
## Bắt đầu

* ### Lấy thông tin xác thực có phạm vi

Hãy yêu cầu quản trị viên ClawRouter cấp thông tin xác thực có chính sách bao gồm các nhà cung cấp, mô hình và ngân sách hằng tháng mà bạn nên dùng. Thông tin xác thực chỉ được hiển thị một lần khi được cấp.

* ### Cấu hình OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

Plugin được đi kèm với OpenClaw. Nếu cấu hình của bạn đặt `plugins.allow`, hãy thêm `clawrouter` vào danh sách đó trước khi bật Plugin. Đối với triển khai tùy chỉnh, đặt `models.providers.clawrouter.baseUrl` thành nguồn gốc ClawRouter; mặc định là `https://clawrouter.openclaw.ai`.

* ### Liệt kê các mô hình được cấp quyền

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

Dùng chính xác các tham chiếu mô hình được trả về như đã hiển thị. Chúng giữ lại không gian tên thượng nguồn, chẳng hạn như `clawrouter/openai/...`, `clawrouter/anthropic/...`, hoặc `clawrouter/google/...`. Nếu `agents.defaults.models` là danh sách cho phép trong cấu hình của bạn, hãy thêm từng tham chiếu ClawRouter đã chọn vào đó.

* ### Chọn một mô hình

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

Bạn cũng có thể chọn một mô hình được trả về cho một lần chạy bằng `openclaw agent --model clawrouter/<provider>/<model> --message "..."`.

## Phát hiện mô hình

`GET /v1/catalog` là nguồn chân lý. OpenClaw không phát hành một danh sách mô hình ClawRouter cố định thứ hai. Một mô hình được cấu hình trong ClawRouter sẽ xuất hiện khi:

  * chính sách của thông tin xác thực cấp quyền cho nhà cung cấp của mô hình đó;
  * kết nối nhà cung cấp đã được bật và sẵn sàng;
  * mô hình trong danh mục quảng bá một năng lực LLM được hỗ trợ; và
  * danh mục công bố một hợp đồng truyền tải được Plugin hỗ trợ.


Vì vậy, việc thêm một mô hình khác vào nhà cung cấp ClawRouter được hỗ trợ không yêu cầu bản phát hành OpenClaw hoặc Plugin nhà cung cấp khác. Lần làm mới danh mục tiếp theo sẽ phát hiện mô hình đó. Một mô hình cần giao thức truyền dây mới cần được hỗ trợ trong Plugin ClawRouter trước khi OpenClaw quảng bá nó.

## Giao thức và Plugin nhà cung cấp

Bạn không cần cài đặt Plugin xác thực của mọi công ty thượng nguồn. ClawRouter sở hữu thông tin xác thực thượng nguồn; danh mục của nó cho OpenClaw biết nên dùng phương thức truyền tải nào. Plugin hỗ trợ:

Tuyến danh mục | Phương thức truyền tải OpenClaw  
---|---  
Chat tương thích OpenAI | `openai-completions`  
Responses tương thích OpenAI | `openai-responses`  
Tin nhắn Anthropic gốc | `anthropic-messages`  
Truyền phát Google Gemini gốc | `google-generative-ai`  
  
Plugin cũng áp dụng các chính sách phát lại và lược đồ công cụ tương ứng cho những nhóm đó. Các hàng danh mục dùng định dạng yêu cầu/luồng khác được cố ý không quảng bá là mô hình văn bản OpenClaw. Hãy chuẩn hóa các nhà cung cấp đó thành một trong các hợp đồng được hỗ trợ trong ClawRouter thay vì gửi một payload không tương thích.

## Hạn mức và mức sử dụng

Phản hồi `/v1/usage` của ClawRouter cung cấp dữ liệu cho các bề mặt mức sử dụng nhà cung cấp thông thường của OpenClaw. `/status` và trạng thái dashboard liên quan hiển thị cửa sổ ngân sách hằng tháng khi khóa có giới hạn, cùng tổng số yêu cầu, token và chi tiêu. Các khóa không đo lường vẫn hiển thị mức sử dụng tổng hợp mà không có cửa sổ phần trăm.

Tra cứu hạn mức dùng cùng khóa có phạm vi như phát hiện mô hình. Tra cứu hạn mức thất bại không chặn việc thực thi mô hình.

Kiểm tra snapshot trực tiếp bằng:

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

Snapshot nhà cung cấp tương tự có sẵn cho `/status` trong chat và giao diện mức sử dụng của OpenClaw. Ngân sách áp dụng cho toàn chính sách, nên các yêu cầu do một client khác thực hiện bằng cùng chính sách ClawRouter có thể thay đổi phần trăm còn lại.

## Khắc phục sự cố

Triệu chứng | Kiểm tra  
---|---  
Không có mô hình ClawRouter | Xác nhận Plugin đã được bật và được `plugins.allow` cho phép, sau đó kiểm tra thông tin xác thực còn hoạt động và cấp quyền cho ít nhất một nhà cung cấp sẵn sàng.  
Thiếu một mô hình ClawRouter đã cấu hình | Kiểm tra năng lực và định dạng tuyến của mô hình đó trong `/v1/catalog`. Các hợp đồng truyền tải không được hỗ trợ được cố ý lọc ra.  
`Unknown model: clawrouter/...` | Thêm tham chiếu danh mục chính xác vào `agents.defaults.models` khi bản đồ cấu hình đó đang được dùng làm danh sách cho phép.  
`401` hoặc `403` từ danh mục hoặc mức sử dụng | Cấp lại hoặc đặt lại phạm vi thông tin xác thực ClawRouter; OpenClaw không dự phòng sang khóa nhà cung cấp thượng nguồn.  
Lệnh gọi mô hình thất bại sau khi phát hiện | Kiểm tra kết nối nhà cung cấp và tình trạng thượng nguồn trong ClawRouter, sau đó thử lại khi trạng thái sẵn sàng của nó phục hồi.  
Mức sử dụng có tổng số nhưng không có phần trăm | Chính sách không được đo lường; thêm ngân sách hằng tháng trong ClawRouter để hiển thị cửa sổ phần trăm.  
  
## Hành vi bảo mật

  * Phát hiện danh mục có phạm vi theo khóa proxy đã cấu hình và được lưu vào cache theo từng khóa.
  * Khóa proxy chỉ được gắn khi điều phối yêu cầu; nó không được lưu trong siêu dữ liệu mô hình.
  * ID mô hình Anthropic và Gemini gốc chỉ được viết lại thành ID thượng nguồn của chúng khi điều phối.
  * Các hàng danh mục không được hỗ trợ hoặc không được cấp quyền sẽ fail closed và không thể chọn.


## Liên quan

[**Nhà cung cấp mô hình** Cấu hình nhà cung cấp và lựa chọn mô hình. ](</vi/concepts/model-providers>) [**Theo dõi mức sử dụng** Các bề mặt mức sử dụng và trạng thái của OpenClaw. ](</vi/concepts/usage-tracking>)

Was this useful?YesNo

Open issue