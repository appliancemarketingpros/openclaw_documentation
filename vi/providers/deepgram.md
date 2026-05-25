---
title: Deepgram
source_url: https://docs.openclaw.ai/vi/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram là một API chuyển giọng nói thành văn bản. Trong OpenClaw, nó được dùng để phiên âm âm thanh/ghi chú thoại gửi đến thông qua `tools.media.audio` và cho STT phát trực tuyến của Voice Call thông qua `plugins.entries.voice-call.config.streaming`.

Đối với phiên âm theo lô, OpenClaw tải toàn bộ tệp âm thanh lên Deepgram và chèn bản phiên âm vào quy trình trả lời (`{{Transcript}}` \+ khối `[Audio]`). Đối với phát trực tuyến Voice Call, OpenClaw chuyển tiếp các khung G.711 u-law trực tiếp qua endpoint WebSocket `listen` của Deepgram và phát ra bản phiên âm một phần hoặc cuối cùng khi Deepgram trả về.

Chi tiết | Giá trị  
---|---  
Trang web | [deepgram.com](<https://deepgram.com>)  
Tài liệu | [developers.deepgram.com](<https://developers.deepgram.com>)  
Xác thực | `DEEPGRAM_API_KEY`  
Mô hình mặc định | `nova-3`  
  
## Bắt đầu

* ### Set your API key

Thêm khóa API Deepgram của bạn vào môi trường:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Send a voice note

Gửi một tin nhắn âm thanh qua bất kỳ kênh nào đã kết nối. OpenClaw phiên âm tin nhắn đó qua Deepgram và chèn bản phiên âm vào quy trình trả lời.

## Tùy chọn cấu hình

Tùy chọn | Đường dẫn | Mô tả  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID mô hình Deepgram (mặc định: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Gợi ý ngôn ngữ (tùy chọn)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Bật phát hiện ngôn ngữ (tùy chọn)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Bật dấu câu (tùy chọn)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Bật định dạng thông minh (tùy chọn)  
  
### With language hint

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### With Deepgram options

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT phát trực tuyến Voice Call

Plugin `deepgram` đi kèm cũng đăng ký một nhà cung cấp phiên âm thời gian thực cho Plugin Voice Call.

Thiết lập | Đường dẫn cấu hình | Mặc định  
---|---|---  
Khóa API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Dự phòng về `DEEPGRAM_API_KEY`  
Mô hình | `...deepgram.model` | `nova-3`  
Ngôn ngữ | `...deepgram.language` | (chưa đặt)  
Mã hóa | `...deepgram.encoding` | `mulaw`  
Tốc độ mẫu | `...deepgram.sampleRate` | `8000`  
Ngắt cuối đoạn | `...deepgram.endpointingMs` | `800`  
Kết quả tạm thời | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Ghi chú

Authentication

Xác thực tuân theo thứ tự xác thực nhà cung cấp tiêu chuẩn. `DEEPGRAM_API_KEY` là cách đơn giản nhất.

Proxy and custom endpoints

Ghi đè endpoint hoặc header bằng `tools.media.audio.baseUrl` và `tools.media.audio.headers` khi dùng proxy.

Output behavior

Đầu ra tuân theo cùng các quy tắc âm thanh như những nhà cung cấp khác (giới hạn kích thước, thời gian chờ, chèn bản phiên âm).

## Liên quan

[**Media tools** Tổng quan về quy trình xử lý âm thanh, hình ảnh và video. ](</vi/tools/media-overview>) [**Configuration** Tham chiếu cấu hình đầy đủ, bao gồm các thiết lập công cụ phương tiện. ](</vi/gateway/configuration>) [**Troubleshooting** Các sự cố thường gặp và bước gỡ lỗi. ](</vi/help/troubleshooting>) [**FAQ** Các câu hỏi thường gặp về thiết lập OpenClaw. ](</vi/help/faq>)

Was this useful?YesNo