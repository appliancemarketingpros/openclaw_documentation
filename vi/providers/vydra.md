---
title: Vydra
source_url: https://docs.openclaw.ai/vi/providers/vydra
scraped_at: 2026-05-25
---

Plugin Vydra được đóng gói kèm bổ sung:

  * Tạo hình ảnh qua `vydra/grok-imagine`
  * Tạo video qua `vydra/veo3` và `vydra/kling`
  * Tổng hợp giọng nói qua tuyến TTS của Vydra dựa trên ElevenLabs


OpenClaw dùng cùng một `VYDRA_API_KEY` cho cả ba khả năng.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `vydra`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Biến môi trường xác thực | `VYDRA_API_KEY`  
Cờ onboarding | `--auth-choice vydra-api-key`  
Cờ CLI trực tiếp | `--vydra-api-key <key>`  
Hợp đồng | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL cơ sở | `https://www.vydra.ai/api/v1` (dùng máy chủ `www`)  
  
## Thiết lập

* ### Chạy onboarding tương tác

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Hoặc đặt trực tiếp biến môi trường:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Chọn một khả năng mặc định

Chọn một hoặc nhiều khả năng bên dưới (hình ảnh, video, hoặc giọng nói) và áp dụng cấu hình tương ứng.

## Khả năng

Tạo hình ảnh

Mô hình hình ảnh mặc định:

  * `vydra/grok-imagine`


Đặt mô hình đó làm nhà cung cấp hình ảnh mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Hỗ trợ được đóng gói kèm hiện tại chỉ là text-to-image. Các tuyến chỉnh sửa được Vydra lưu trữ yêu cầu URL hình ảnh từ xa, và OpenClaw chưa thêm cầu nối tải lên dành riêng cho Vydra trong Plugin được đóng gói kèm.

Tạo video

Các mô hình video đã đăng ký:

  * `vydra/veo3` cho text-to-video
  * `vydra/kling` cho image-to-video


Đặt Vydra làm nhà cung cấp video mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Ghi chú:

  * `vydra/veo3` được đóng gói kèm chỉ dưới dạng text-to-video.
  * `vydra/kling` hiện yêu cầu một tham chiếu URL hình ảnh từ xa. Tải lên tệp cục bộ bị từ chối ngay từ đầu.
  * Tuyến HTTP `kling` hiện tại của Vydra chưa nhất quán về việc nó yêu cầu `image_url` hay `video_url`; nhà cung cấp được đóng gói kèm ánh xạ cùng một URL hình ảnh từ xa vào cả hai trường.
  * Plugin được đóng gói kèm giữ cách tiếp cận thận trọng và không chuyển tiếp các nút điều chỉnh kiểu chưa được tài liệu hóa như tỷ lệ khung hình, độ phân giải, watermark, hoặc âm thanh được tạo.

Kiểm thử trực tiếp video

Phạm vi kiểm thử trực tiếp dành riêng cho nhà cung cấp:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Tệp trực tiếp Vydra được đóng gói kèm hiện bao gồm:

  * `vydra/veo3` text-to-video
  * `vydra/kling` image-to-video dùng một URL hình ảnh từ xa


Ghi đè fixture hình ảnh từ xa khi cần:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Tổng hợp giọng nói

Đặt Vydra làm nhà cung cấp giọng nói:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Mặc định:

  * Mô hình: `elevenlabs/tts`
  * ID giọng nói: `21m00Tcm4TlvDq8ikWAM`


Plugin được đóng gói kèm hiện cung cấp một giọng nói mặc định đã được xác nhận hoạt động tốt và trả về tệp âm thanh MP3.

## Liên quan

[**Thư mục nhà cung cấp** Duyệt tất cả nhà cung cấp hiện có. ](</vi/providers>) [**Tạo hình ảnh** Các tham số công cụ hình ảnh dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/image-generation>) [**Tạo video** Các tham số công cụ video dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/video-generation>) [**Tham chiếu cấu hình** Mặc định của agent và cấu hình mô hình. ](</vi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo