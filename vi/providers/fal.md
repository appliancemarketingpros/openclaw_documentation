---
title: Fal
source_url: https://docs.openclaw.ai/vi/providers/fal
scraped_at: 2026-05-25
---

OpenClaw đi kèm một provider `fal` tích hợp sẵn cho tạo hình ảnh và video được lưu trữ.

Thuộc tính | Giá trị  
---|---  
Provider | `fal`  
Xác thực | `FAL_KEY` (chuẩn; `FAL_API_KEY` cũng hoạt động làm phương án dự phòng)  
API | endpoint mô hình fal  
  
## Bắt đầu

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Tạo hình ảnh

Provider tạo hình ảnh `fal` tích hợp sẵn mặc định dùng `fal/fal-ai/flux/dev`.

Khả năng | Giá trị  
---|---  
Số hình ảnh tối đa | 4 mỗi yêu cầu  
Chế độ chỉnh sửa | Flux: 1 hình ảnh tham chiếu; GPT Image 2: 10; Nano Banana 2: 14  
Ghi đè kích thước | Được hỗ trợ  
Tỷ lệ khung hình | Được hỗ trợ cho tạo mới và chỉnh sửa GPT Image 2/Nano Banana 2  
Độ phân giải | Được hỗ trợ  
Định dạng đầu ra | `png` hoặc `jpeg`  
  
Dùng `outputFormat: "png"` khi bạn muốn đầu ra PNG. fal không khai báo cơ chế điều khiển nền trong suốt rõ ràng trong OpenClaw, nên `background: "transparent"` được báo cáo là một ghi đè bị bỏ qua đối với các mô hình fal.

Để dùng fal làm provider hình ảnh mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Tạo video

Provider tạo video `fal` tích hợp sẵn mặc định dùng `fal/fal-ai/minimax/video-01-live`.

Khả năng | Giá trị  
---|---  
Chế độ | Văn bản thành video, tham chiếu một hình ảnh, tham chiếu Seedance thành video  
Runtime | Luồng gửi/trạng thái/kết quả dựa trên hàng đợi cho các tác vụ chạy lâu  
  
Available video models

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Chuyển tham chiếu thành video chấp nhận tối đa 9 hình ảnh, 3 video và 3 tham chiếu âm thanh thông qua các tham số `video_generate` dùng chung là `images`, `videos` và `audioRefs`, với tổng cộng tối đa 12 tệp tham chiếu.

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Liên quan

[**Image generation** Các tham số công cụ hình ảnh dùng chung và lựa chọn provider. ](</vi/tools/image-generation>) [**Video generation** Các tham số công cụ video dùng chung và lựa chọn provider. ](</vi/tools/video-generation>) [**Configuration reference** Mặc định của agent, bao gồm lựa chọn mô hình hình ảnh và video. ](</vi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo