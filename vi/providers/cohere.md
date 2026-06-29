---
title: Cohere
source_url: https://docs.openclaw.ai/vi/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) cung cấp suy luận tương thích với OpenAI thông qua API Tương thích. OpenClaw phân phối nhà cung cấp Cohere trong giai đoạn chuyển đổi tách ra bên ngoài và cũng phát hành nó dưới dạng Plugin bên ngoài chính thức với danh mục mô hình Command A.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `cohere`  
Plugin | được đóng gói kèm trong giai đoạn chuyển đổi; gói bên ngoài chính thức  
Biến môi trường xác thực | `COHERE_API_KEY`  
Cờ thiết lập ban đầu | `--auth-choice cohere-api-key`  
Cờ CLI trực tiếp | `--cohere-api-key <key>`  
API | tương thích với OpenAI (`openai-completions`)  
URL cơ sở | `https://api.cohere.ai/compatibility/v1`  
Mô hình mặc định | `cohere/command-a-03-2025`  
  
## Bắt đầu

  1. Cohere được bao gồm trong các gói OpenClaw hiện tại. Nếu không có sẵn, hãy cài đặt gói bên ngoài và khởi động lại Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Tạo khóa API Cohere.
  3. Chạy thiết lập ban đầu:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Xác nhận danh mục có sẵn:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Mô hình mặc định chỉ được đặt khi chưa có mô hình chính nào được cấu hình.

## Thiết lập chỉ bằng môi trường

Cung cấp `COHERE_API_KEY` cho tiến trình Gateway, sau đó chọn mô hình Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Liên quan

  * [Nhà cung cấp mô hình](</vi/concepts/model-providers>)
  * [CLI mô hình](</vi/cli/models>)
  * [Thư mục nhà cung cấp](</vi/providers>)


Was this useful?YesNo

Open issue