---
title: NVIDIA
source_url: https://docs.openclaw.ai/vi/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA cung cấp một API tương thích với OpenAI tại `https://integrate.api.nvidia.com/v1` cho các mô hình mở miễn phí. Xác thực bằng khóa API từ [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Bắt đầu

* ### Lấy khóa API của bạn

Tạo khóa API tại [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Xuất khóa và chạy quy trình onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Đặt một mô hình NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Để thiết lập không tương tác, bạn cũng có thể truyền khóa trực tiếp:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Danh mục tích hợp sẵn

Tham chiếu mô hình | Tên | Ngữ cảnh | Đầu ra tối đa  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Cấu hình nâng cao

Hành vi tự động bật

Nhà cung cấp sẽ tự động bật khi biến môi trường `NVIDIA_API_KEY` được đặt. Không cần cấu hình nhà cung cấp rõ ràng ngoài khóa.

Danh mục và giá

Danh mục đi kèm là tĩnh. Chi phí mặc định là `0` trong mã nguồn vì NVIDIA hiện cung cấp quyền truy cập API miễn phí cho các mô hình được liệt kê.

Endpoint tương thích với OpenAI

NVIDIA sử dụng endpoint completions `/v1` tiêu chuẩn. Mọi công cụ tương thích với OpenAI sẽ hoạt động ngay với URL cơ sở của NVIDIA.

Phản hồi chậm từ nhà cung cấp tùy chỉnh

Một số mô hình tùy chỉnh do NVIDIA lưu trữ có thể mất nhiều thời gian hơn bộ theo dõi trạng thái nhàn rỗi mặc định của mô hình trước khi phát ra đoạn phản hồi đầu tiên. Với các mục nhà cung cấp NVIDIA tùy chỉnh, hãy tăng thời gian chờ của nhà cung cấp thay vì tăng thời gian chờ runtime của toàn bộ agent:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Liên quan

[**Lựa chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Tham chiếu cấu hình đầy đủ cho agent, mô hình và nhà cung cấp. ](</vi/gateway/configuration-reference>)

Was this useful?YesNo