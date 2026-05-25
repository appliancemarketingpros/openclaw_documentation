---
title: Azure Speech
source_url: https://docs.openclaw.ai/vi/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech là nhà cung cấp chuyển văn bản thành giọng nói của Azure AI Speech. Trong OpenClaw, mặc định nhà cung cấp này tổng hợp âm thanh trả lời gửi đi dưới dạng MP3, Ogg/Opus gốc cho ghi chú thoại, và âm thanh mulaw 8 kHz cho các kênh điện thoại như Voice Call.

OpenClaw sử dụng trực tiếp Azure Speech REST API với SSML và gửi định dạng đầu ra do nhà cung cấp sở hữu thông qua `X-Microsoft-OutputFormat`.

Chi tiết | Giá trị  
---|---  
Trang web | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Tài liệu | [REST chuyển văn bản thành giọng nói của Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Xác thực | `AZURE_SPEECH_KEY` cộng với `AZURE_SPEECH_REGION`  
Giọng mặc định | `en-US-JennyNeural`  
Đầu ra tệp mặc định | `audio-24khz-48kbitrate-mono-mp3`  
Tệp ghi chú thoại mặc định | `ogg-24khz-16bit-mono-opus`  
  
## Bắt đầu

* ### Tạo tài nguyên Azure Speech

Trong cổng Azure, tạo một tài nguyên Speech. Sao chép **KEY 1** từ Resource Management > Keys and Endpoint, và sao chép vị trí tài nguyên chẳng hạn như `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Chọn Azure Speech trong messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Gửi tin nhắn

Gửi một câu trả lời qua bất kỳ kênh nào đã kết nối. OpenClaw tổng hợp âm thanh bằng Azure Speech và phân phối MP3 cho âm thanh tiêu chuẩn, hoặc Ogg/Opus khi kênh yêu cầu một ghi chú thoại.

## Tùy chọn cấu hình

Tùy chọn | Đường dẫn | Mô tả  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Khóa tài nguyên Azure Speech. Dự phòng sang `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, hoặc `SPEECH_KEY`.  
`region` | `messages.tts.providers.azure-speech.region` | Vùng tài nguyên Azure Speech. Dự phòng sang `AZURE_SPEECH_REGION` hoặc `SPEECH_REGION`.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Ghi đè tùy chọn cho điểm cuối/URL cơ sở của Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Ghi đè tùy chọn cho URL cơ sở của Azure Speech.  
`voice` | `messages.tts.providers.azure-speech.voice` | ShortName của giọng Azure (mặc định `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | Mã ngôn ngữ SSML (mặc định `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Định dạng đầu ra tệp âm thanh (mặc định `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Định dạng đầu ra ghi chú thoại (mặc định `ogg-24khz-16bit-mono-opus`).  
  
## Ghi chú

Xác thực

Azure Speech sử dụng khóa tài nguyên Speech, không phải khóa Azure OpenAI. Khóa này được gửi dưới dạng `Ocp-Apim-Subscription-Key`; OpenClaw suy ra `https://<region>.tts.speech.microsoft.com` từ `region` trừ khi bạn cung cấp `endpoint` hoặc `baseUrl`.

Tên giọng

Sử dụng giá trị `ShortName` của giọng Azure Speech, ví dụ `en-US-JennyNeural`. Nhà cung cấp đi kèm có thể liệt kê các giọng qua cùng tài nguyên Speech và lọc các giọng được đánh dấu là không còn được khuyến nghị hoặc đã ngừng dùng.

Đầu ra âm thanh

Azure chấp nhận các định dạng đầu ra như `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus`, và `riff-24khz-16bit-mono-pcm`. OpenClaw yêu cầu Ogg/Opus cho các đích `voice-note` để các kênh có thể gửi bong bóng thoại gốc mà không cần chuyển đổi MP3 bổ sung.

Bí danh

`azure` được chấp nhận làm bí danh nhà cung cấp cho các PR hiện có và cấu hình người dùng, nhưng cấu hình mới nên dùng `azure-speech` để tránh nhầm lẫn với các nhà cung cấp mô hình Azure OpenAI.

## Liên quan

[**Chuyển văn bản thành giọng nói** Tổng quan về TTS, nhà cung cấp, và cấu hình `messages.tts`. ](</vi/tools/tts>) [**Cấu hình** Tham chiếu cấu hình đầy đủ, bao gồm các cài đặt `messages.tts`. ](</vi/gateway/configuration>) [**Nhà cung cấp** Tất cả các nhà cung cấp OpenClaw đi kèm. ](</vi/providers>) [**Khắc phục sự cố** Các vấn đề thường gặp và các bước gỡ lỗi. ](</vi/help/troubleshooting>)

Was this useful?YesNo