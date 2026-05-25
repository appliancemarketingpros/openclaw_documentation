---
title: DeepInfra
source_url: https://docs.openclaw.ai/vi/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra cung cấp một **API hợp nhất** định tuyến yêu cầu đến các mô hình nguồn mở và frontier phổ biến nhất phía sau một endpoint và khóa API duy nhất. API này tương thích với OpenAI, vì vậy hầu hết các SDK OpenAI đều hoạt động bằng cách chuyển URL cơ sở.

## Lấy khóa API

  1. Truy cập <https://deepinfra.com/>
  2. Đăng nhập hoặc tạo tài khoản
  3. Điều hướng đến Dashboard / Keys rồi tạo khóa API mới hoặc dùng khóa được tạo tự động


## Thiết lập CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Hoặc đặt biến môi trường:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Đoạn cấu hình

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Các bề mặt OpenClaw được hỗ trợ

Plugin đi kèm đăng ký tất cả các bề mặt DeepInfra khớp với các hợp đồng nhà cung cấp OpenClaw hiện tại:

Bề mặt | Mô hình mặc định | Cấu hình/công cụ OpenClaw  
---|---|---  
Chat / nhà cung cấp mô hình | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Tạo/chỉnh sửa hình ảnh | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Hiểu phương tiện | `moonshotai/Kimi-K2.5` cho hình ảnh | hiểu hình ảnh đầu vào  
Chuyển giọng nói thành văn bản | `openai/whisper-large-v3-turbo` | phiên âm âm thanh đầu vào  
Chuyển văn bản thành giọng nói | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Tạo video | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Embedding bộ nhớ | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra cũng cung cấp reranking, phân loại, phát hiện đối tượng và các loại mô hình native khác. OpenClaw hiện chưa có hợp đồng nhà cung cấp hạng nhất cho các danh mục đó, vì vậy Plugin này chưa đăng ký chúng.

## Các mô hình có sẵn

OpenClaw tự động phát hiện các mô hình DeepInfra có sẵn khi khởi động. Dùng `/models deepinfra` để xem danh sách đầy đủ các mô hình có sẵn.

Bất kỳ mô hình nào có trên [DeepInfra.com](<https://deepinfra.com/>) đều có thể được dùng với tiền tố `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...và nhiều mô hình khác
[/code]

## Ghi chú

  * Tham chiếu mô hình có dạng `deepinfra/<provider>/<model>` (ví dụ: `deepinfra/Qwen/Qwen3-Max`).
  * Mô hình mặc định: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * URL cơ sở: `https://api.deepinfra.com/v1/openai`
  * Tạo video native dùng `https://api.deepinfra.com/v1/inference/<model>`.


## Liên quan

  * [Nhà cung cấp mô hình](</vi/concepts/model-providers>)
  * [Tất cả nhà cung cấp](</vi/providers>)


Was this useful?YesNo