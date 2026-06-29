---
title: Qwen OAuth / Cổng thông tin
source_url: https://docs.openclaw.ai/vi/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` là id nhà cung cấp Qwen Portal. Nó nhắm tới endpoint Qwen Portal và giữ cho các thiết lập Qwen OAuth / portal cũ hơn vẫn có thể được tham chiếu thông qua một id nhà cung cấp riêng biệt.

Dùng nhà cung cấp này khi bạn có token Qwen Portal hiện tại dành riêng cho `https://portal.qwen.ai/v1`, hoặc khi bạn đang di chuyển một thiết lập Qwen Portal / Qwen CLI cũ hơn và muốn giữ các thông tin xác thực đó tách biệt với nhà cung cấp Qwen Cloud chính tắc. Đây không phải là lựa chọn đầu tiên được khuyến nghị cho người dùng Qwen mới.

Với các thiết lập Qwen Cloud mới, hãy ưu tiên [Qwen](</vi/providers/qwen>) với endpoint Standard ModelStudio, trừ khi bạn có token Qwen Portal hiện tại.

## Thiết lập

Cung cấp token portal của bạn thông qua quy trình onboarding:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Hoặc đặt:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Mặc định

  * Nhà cung cấp: `qwen-oauth`
  * Bí danh: `qwen-portal`, `qwen-cli`
  * URL cơ sở: `https://portal.qwen.ai/v1`
  * Biến môi trường: `QWEN_API_KEY`
  * Kiểu API: tương thích OpenAI
  * Mô hình mặc định: `qwen-oauth/qwen3.5-plus`


## Điểm khác biệt so với Qwen

OpenClaw có hai id nhà cung cấp hướng tới Qwen:

Nhà cung cấp | Nhóm endpoint | Phù hợp nhất cho  
---|---|---  
`qwen` | Các endpoint Qwen Cloud / Alibaba DashScope và Coding Plan | Thiết lập khóa API mới, Standard trả theo mức dùng, Coding Plan, tính năng DashScope đa phương thức  
`qwen-oauth` | Endpoint Qwen Portal tại `portal.qwen.ai/v1` | Token Qwen Portal hiện có và thiết lập Qwen OAuth / CLI kế thừa  
  
Cả hai nhà cung cấp đều dùng dạng yêu cầu tương thích OpenAI, nhưng chúng là các bề mặt xác thực riêng biệt. Token được lưu cho `qwen-oauth` không nên được xem là khóa DashScope hoặc ModelStudio, và khóa DashScope mới nên dùng nhà cung cấp `qwen` chính tắc thay vào đó.

## Khi nào nên chọn Qwen OAuth / Portal

  * Bạn đã có token Qwen Portal đang hoạt động.
  * Bạn đang bảo toàn quy trình làm việc Qwen OAuth hoặc Qwen CLI kế thừa trong khi chuyển sang mô hình nhà cung cấp của OpenClaw.
  * Bạn cần kiểm tra khả năng tương thích riêng với endpoint Qwen Portal.


Chọn [Qwen](</vi/providers/qwen>) cho thiết lập mới, nhiều lựa chọn endpoint hơn, Standard ModelStudio, Coding Plan và toàn bộ danh mục Plugin Qwen.

## Mô hình

Danh mục Plugin Qwen khởi tạo giá trị mặc định cho Qwen Portal:

  * `qwen-oauth/qwen3.5-plus`


Tính khả dụng phụ thuộc vào tài khoản và token Qwen Portal hiện tại. Nếu tài khoản của bạn dùng khóa API ModelStudio / DashScope thay vào đó, hãy cấu hình nhà cung cấp `qwen` chính tắc:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Di chuyển

Các hồ sơ Qwen Portal OAuth kế thừa có thể không làm mới được. Nếu một hồ sơ portal ngừng hoạt động, hãy xác thực lại bằng token hiện tại hoặc chuyển sang nhà cung cấp Qwen Standard:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Standard global ModelStudio dùng:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Khắc phục sự cố

  * Lỗi làm mới Portal OAuth: các hồ sơ Qwen Portal OAuth kế thừa có thể không làm mới được. Chạy lại onboarding với token hiện tại.
  * Lỗi endpoint sai: xác nhận tham chiếu mô hình bắt đầu bằng `qwen-oauth/` khi dùng token portal. Chỉ dùng tham chiếu `qwen/` cho nhà cung cấp Qwen chính tắc.
  * Nhầm lẫn `QWEN_API_KEY`: cả hai trang Qwen đều nhắc tới biến môi trường này, nhưng onboarding lưu thông tin xác thực dưới id nhà cung cấp đã chọn. Hãy ưu tiên onboarding khi bạn giữ cả `qwen` và `qwen-oauth` khả dụng trên cùng một máy.


## Liên quan

  * [Qwen](</vi/providers/qwen>)
  * [Alibaba Model Studio](</vi/providers/alibaba>)
  * [Nhà cung cấp mô hình](</vi/concepts/model-providers>)
  * [Tất cả nhà cung cấp](</vi/providers>)


Was this useful?YesNo

Open issue