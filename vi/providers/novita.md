---
title: NovitaAI
source_url: https://docs.openclaw.ai/vi/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI là nhà cung cấp hạ tầng AI được lưu trữ với API mô hình tương thích OpenAI. Trong OpenClaw, đây là nhà cung cấp mô hình được đóng gói sẵn, nên id nhà cung cấp là `novita`, thông tin xác thực đi qua luồng xác thực mô hình thông thường, và tham chiếu mô hình có dạng như `novita/deepseek/deepseek-v3-0324`.

Dùng Novita khi bạn muốn truy cập được lưu trữ vào các tuyến mô hình trọng số mở và mô hình bên thứ ba mà không cần chạy máy chủ suy luận riêng. Danh mục được đóng gói sẵn tập trung vào các mô hình chat thực tế cho các lượt tác vụ của tác nhân, bao gồm các tuyến DeepSeek, Moonshot, MiniMax, GLM và Qwen do Novita cung cấp.

Nhà cung cấp này dùng endpoint tương thích OpenAI của Novita. OpenClaw xử lý việc đăng ký nhà cung cấp, xác thực, bí danh, chuẩn hóa tham chiếu mô hình và chọn URL cơ sở; Novita kiểm soát trạng thái sẵn có trực tiếp của mô hình, quyền tài khoản, giá và giới hạn tốc độ.

## Thiết lập

Tạo khóa API tại [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>), rồi chạy:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Hoặc đặt:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Mặc định

  * Nhà cung cấp: `novita`
  * Bí danh: `novita-ai`, `novitaai`
  * URL cơ sở: `https://api.novita.ai/openai/v1`
  * Biến môi trường: `NOVITA_API_KEY`
  * Mô hình mặc định: `novita/deepseek/deepseek-v3-0324`


## Khi nào nên chọn Novita

  * Bạn muốn truy cập mô hình trọng số mở được lưu trữ bằng API tương thích OpenAI.
  * Bạn muốn các tuyến thuộc họ DeepSeek, Kimi, MiniMax, GLM hoặc Qwen thông qua một tài khoản nhà cung cấp duy nhất.
  * Bạn muốn một đường dự phòng được lưu trữ khác bên cạnh OpenRouter, GMI, DeepInfra hoặc API trực tiếp của nhà cung cấp.
  * Bạn thích lưu trữ mô hình phía nhà cung cấp hơn là duy trì hạ tầng vLLM, SGLang, LM Studio hoặc Ollama.


Chọn nhà cung cấp trực tiếp của nhà cung cấp gốc khi bạn cần tham số yêu cầu gốc theo nhà cung cấp hoặc hợp đồng hỗ trợ. Chọn nhà cung cấp cục bộ khi mô hình phải chạy trên phần cứng của riêng bạn hoặc sau ranh giới mạng của riêng bạn.

## Mô hình

Danh mục được đóng gói sẵn khởi tạo các id tuyến NovitaAI thường có sẵn, bao gồm:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Danh mục này là điểm khởi đầu cho việc chọn mô hình trong OpenClaw. Tài khoản, khu vực của bạn hoặc danh mục hiện tại của Novita có thể thêm, xóa hoặc hạn chế các tuyến. Kiểm tra nhà cung cấp từ CLI trước khi đặt một mặc định dài hạn:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Khắc phục sự cố

  * `401` hoặc `403`: xác minh khóa trong trang quản lý khóa của Novita và chạy lại `openclaw onboard --auth-choice novita-api-key` nếu hồ sơ đã lưu đã cũ.
  * Lỗi mô hình không xác định: dùng đúng `novita/<route-id>` do `openclaw models list --provider novita` trả về.
  * Tuyến chậm hoặc lỗi: thử một tuyến mô hình Novita khác hoặc đặt Novita làm nhà cung cấp dự phòng cho các khối lượng công việc có thể chấp nhận độ dao động riêng theo nhà cung cấp.


## Liên quan

  * [Nhà cung cấp mô hình](</vi/concepts/model-providers>)
  * [Tất cả nhà cung cấp](</vi/providers>)


Was this useful?YesNo

Open issue