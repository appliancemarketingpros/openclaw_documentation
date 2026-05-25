---
title: SenseAudio
source_url: https://docs.openclaw.ai/vi/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio có thể chép lại âm thanh đầu vào và tệp đính kèm ghi chú thoại thông qua pipeline `tools.media.audio` dùng chung của OpenClaw. OpenClaw gửi âm thanh multipart đến endpoint chép lời tương thích với OpenAI và chèn văn bản được trả về dưới dạng `{{Transcript}}` cùng một khối `[Audio]`.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `senseaudio`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Hợp đồng | `mediaUnderstandingProviders` (âm thanh)  
Biến môi trường xác thực | `SENSEAUDIO_API_KEY`  
Mô hình mặc định | `senseaudio-asr-pro-1.5-260319`  
URL mặc định | `https://api.senseaudio.cn/v1`  
Trang web | [senseaudio.cn](<https://senseaudio.cn>)  
Tài liệu | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Bắt đầu

* ### Set your API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Send a voice note

Gửi một tin nhắn âm thanh qua bất kỳ kênh nào đã kết nối. OpenClaw tải âm thanh lên SenseAudio và sử dụng bản chép lời trong pipeline trả lời.

## Tùy chọn

Tùy chọn | Đường dẫn | Mô tả  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID mô hình ASR của SenseAudio  
`language` | `tools.media.audio.models[].language` | Gợi ý ngôn ngữ tùy chọn  
`prompt` | `tools.media.audio.prompt` | Lời nhắc chép lời tùy chọn  
`baseUrl` | `tools.media.audio.baseUrl` hoặc mô hình | Ghi đè base tương thích với OpenAI  
`headers` | `tools.media.audio.request.headers` | Header yêu cầu bổ sung  
  
## Liên quan

  * [Hiểu phương tiện (âm thanh)](</vi/nodes/audio>)
  * [Nhà cung cấp mô hình](</vi/concepts/model-providers>)


Was this useful?YesNo