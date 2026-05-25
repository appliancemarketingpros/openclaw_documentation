---
title: Gradium
source_url: https://docs.openclaw.ai/vi/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) là một nhà cung cấp chuyển văn bản thành giọng nói được đóng gói sẵn cho OpenClaw. Plugin có thể tạo các phản hồi âm thanh thông thường (WAV), đầu ra Opus tương thích với ghi chú thoại, và âm thanh u-law 8 kHz cho các bề mặt điện thoại.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `gradium`  
Xác thực | `GRADIUM_API_KEY` hoặc cấu hình `apiKey`  
URL cơ sở | `https://api.gradium.ai` (mặc định)  
Giọng mặc định | `Emma` (`YTpq7expH9539ERJ`)  
  
## Thiết lập

Tạo một khóa API Gradium, rồi cung cấp khóa đó cho OpenClaw bằng biến môi trường hoặc khóa cấu hình.

### Biến môi trường

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Khóa cấu hình

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin kiểm tra `apiKey` đã được phân giải trước và quay về biến môi trường `GRADIUM_API_KEY` nếu không có.

## Cấu hình

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Khóa | Kiểu | Mô tả  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Khóa API đã được phân giải. Hỗ trợ `${ENV}` và tham chiếu bí mật.  
`messages.tts.providers.gradium.baseUrl` | string | Ghi đè nguồn gốc API. Dấu gạch chéo ở cuối sẽ bị loại bỏ. Mặc định là `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | ID giọng mặc định được dùng khi không có ghi đè chỉ thị.  
  
Định dạng âm thanh đầu ra được runtime tự động chọn dựa trên bề mặt đích và không thể cấu hình từ `openclaw.json`. Xem Đầu ra bên dưới.

## Giọng nói

Tên | ID giọng  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Giọng mặc định: Emma.

### Ghi đè giọng theo từng tin nhắn

Khi chính sách giọng nói đang hoạt động cho phép ghi đè giọng, bạn có thể chuyển giọng trực tiếp bằng một token chỉ thị. Tất cả các token này đều phân giải thành cùng một ghi đè `voiceId`:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Nếu chính sách giọng nói tắt ghi đè giọng, chỉ thị sẽ được tiêu thụ nhưng bị bỏ qua.

## Đầu ra

Runtime chọn định dạng đầu ra từ bề mặt đích. Hiện tại nhà cung cấp không tổng hợp các định dạng khác.

Đích | Định dạng | Phần mở rộng tệp | Tần số lấy mẫu | Cờ tương thích với giọng nói  
---|---|---|---|---  
Âm thanh tiêu chuẩn | `wav` | `.wav` | nhà cung cấp | không  
Ghi chú thoại | `opus` | `.opus` | nhà cung cấp | có  
Điện thoại | `ulaw_8000` | không áp dụng | 8 kHz | không áp dụng  
  
## Thứ tự tự động chọn

Trong số các nhà cung cấp TTS đã cấu hình, thứ tự tự động chọn của Gradium là `30`. Xem [Chuyển văn bản thành giọng nói](</vi/tools/tts>) để biết cách OpenClaw chọn nhà cung cấp đang hoạt động khi `messages.tts.provider` không được ghim.

## Liên quan

  * [Chuyển văn bản thành giọng nói](</vi/tools/tts>)
  * [Tổng quan về phương tiện](</vi/tools/media-overview>)


Was this useful?YesNo