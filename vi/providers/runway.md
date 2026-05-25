---
title: Đường băng
source_url: https://docs.openclaw.ai/vi/providers/runway
scraped_at: 2026-05-25
---

OpenClaw phát hành kèm một nhà cung cấp `runway` được đóng gói sẵn cho tạo video được lưu trữ. Plugin được bật theo mặc định và đăng ký nhà cung cấp `runway` với hợp đồng `videoGenerationProviders`.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `runway`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Biến môi trường xác thực | `RUNWAYML_API_SECRET` (chuẩn) hoặc `RUNWAY_API_KEY`  
Cờ onboarding | `--auth-choice runway-api-key`  
Cờ CLI trực tiếp | `--runway-api-key <key>`  
API | Tạo video dựa trên tác vụ của Runway (thăm dò `GET /v1/tasks/{id}`)  
Mô hình mặc định | `runway/gen4.5`  
  
## Bắt đầu

* ### Đặt khóa API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Đặt Runway làm nhà cung cấp video mặc định

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Tạo video

Yêu cầu agent tạo video. Runway sẽ được sử dụng tự động.

## Chế độ và mô hình được hỗ trợ

Nhà cung cấp này cung cấp bảy mô hình Runway được chia thành ba chế độ. Cùng một ID mô hình có thể phục vụ nhiều hơn một chế độ (ví dụ `gen4.5` hoạt động cho cả văn bản thành video và hình ảnh thành video).

Chế độ | Mô hình | Đầu vào tham chiếu  
---|---|---  
Văn bản thành video | `gen4.5` (mặc định), `veo3.1`, `veo3.1_fast`, `veo3` | Không có  
Hình ảnh thành video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 hình ảnh cục bộ hoặc từ xa  
Video thành video | `gen4_aleph` | 1 video cục bộ hoặc từ xa  
  
Tham chiếu hình ảnh và video cục bộ được hỗ trợ qua URI dữ liệu.

Tỷ lệ khung hình | Giá trị được phép  
---|---  
Văn bản thành video | `16:9`, `9:16`  
Chỉnh sửa hình ảnh và video | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Cấu hình

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Cấu hình nâng cao

Bí danh biến môi trường

OpenClaw nhận diện cả `RUNWAYML_API_SECRET` (chuẩn) và `RUNWAY_API_KEY`. Biến nào cũng sẽ xác thực nhà cung cấp Runway.

Thăm dò tác vụ

Runway sử dụng API dựa trên tác vụ. Sau khi gửi yêu cầu tạo, OpenClaw thăm dò `GET /v1/tasks/{id}` cho đến khi video sẵn sàng. Không cần cấu hình bổ sung cho hành vi thăm dò.

## Liên quan

[**Tạo video** Tham số công cụ dùng chung, lựa chọn nhà cung cấp và hành vi bất đồng bộ. ](</vi/tools/video-generation>) [**Tham chiếu cấu hình** Cài đặt mặc định của agent, bao gồm mô hình tạo video. ](</vi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo