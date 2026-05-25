---
title: Tổng quan về nội dung đa phương tiện
source_url: https://docs.openclaw.ai/vi/tools/media-overview
scraped_at: 2026-05-25
---

OpenClaw tạo hình ảnh, video và nhạc, hiểu media gửi đến (hình ảnh, âm thanh, video), và đọc to phản hồi bằng chuyển văn bản thành giọng nói. Tất cả khả năng media đều được điều khiển bằng công cụ: agent quyết định khi nào dùng chúng dựa trên cuộc trò chuyện, và mỗi công cụ chỉ xuất hiện khi có ít nhất một nhà cung cấp nền được cấu hình.

Giọng nói trực tiếp dùng hợp đồng phiên Talk thay vì đường dẫn công cụ media một lần. Talk có ba chế độ: `realtime` gốc theo nhà cung cấp, `stt-tts` cục bộ hoặc phát trực tuyến, và `transcription` để thu giọng nói chỉ quan sát. Các chế độ đó dùng chung danh mục nhà cung cấp, phong bì sự kiện và ngữ nghĩa hủy với điện thoại, cuộc họp, thời gian thực trên trình duyệt, và máy khách nhấn-để-nói gốc.

## Khả năng

[**Tạo hình ảnh** Tạo và chỉnh sửa hình ảnh từ lời nhắc văn bản hoặc hình ảnh tham chiếu qua `image_generate`. Đồng bộ — hoàn tất ngay trong phản hồi. ](</vi/tools/image-generation>) [**Tạo video** Văn bản thành video, hình ảnh thành video, và video thành video qua `video_generate`. Bất đồng bộ — chạy trong nền và đăng kết quả khi sẵn sàng. ](</vi/tools/video-generation>) [**Tạo nhạc** Tạo nhạc hoặc bản âm thanh qua `music_generate`. Bất đồng bộ trên các nhà cung cấp dùng chung; đường dẫn quy trình ComfyUI chạy đồng bộ. ](</vi/tools/music-generation>) [**Chuyển văn bản thành giọng nói** Chuyển phản hồi gửi đi thành âm thanh nói qua công cụ `tts` cùng cấu hình `messages.tts`. Đồng bộ. ](</vi/tools/tts>) [**Hiểu media** Tóm tắt hình ảnh, âm thanh và video gửi đến bằng các nhà cung cấp mô hình có khả năng thị giác và các Plugin chuyên biệt về hiểu media. ](</vi/nodes/media-understanding>) [**Chuyển giọng nói thành văn bản** Chép lại tin nhắn thoại gửi đến thông qua STT theo lô hoặc các nhà cung cấp STT phát trực tuyến cho Cuộc gọi thoại. ](</vi/nodes/audio>)

## Ma trận khả năng nhà cung cấp

Nhà cung cấp | Hình ảnh | Video | Nhạc | TTS | STT | Giọng nói thời gian thực | Hiểu media  
---|---|---|---|---|---|---|---  
Alibaba |  | ✓ |  |  |  |  |   
BytePlus |  | ✓ |  |  |  |  |   
ComfyUI | ✓ | ✓ | ✓ |  |  |  |   
DeepInfra | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Deepgram |  |  |  |  | ✓ | ✓ |   
ElevenLabs |  |  |  | ✓ | ✓ |  |   
fal | ✓ | ✓ |  |  |  |  |   
Google | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓  
Gradium |  |  |  | ✓ |  |  |   
CLI cục bộ |  |  |  | ✓ |  |  |   
Microsoft |  |  |  | ✓ |  |  |   
MiniMax | ✓ | ✓ | ✓ | ✓ |  |  |   
Mistral |  |  |  |  | ✓ |  |   
OpenAI | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓  
OpenRouter | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Qwen |  | ✓ |  |  |  |  |   
Runway |  | ✓ |  |  |  |  |   
SenseAudio |  |  |  |  | ✓ |  |   
Together |  | ✓ |  |  |  |  |   
Vydra | ✓ | ✓ |  | ✓ |  |  |   
xAI | ✓ | ✓ |  | ✓ | ✓ |  | ✓  
Xiaomi MiMo | ✓ |  |  | ✓ |  |  | ✓  
  
## Bất đồng bộ so với đồng bộ

Khả năng | Chế độ | Lý do  
---|---|---  
Hình ảnh | Đồng bộ | Phản hồi của nhà cung cấp trả về trong vài giây; hoàn tất ngay trong phản hồi.  
Chuyển văn bản thành giọng nói | Đồng bộ | Phản hồi của nhà cung cấp trả về trong vài giây; được đính kèm vào âm thanh phản hồi.  
Video | Bất đồng bộ | Quá trình xử lý của nhà cung cấp mất 30 giây đến vài phút; hàng đợi chậm có thể chạy đến hết thời gian chờ đã cấu hình.  
Nhạc (dùng chung) | Bất đồng bộ | Cùng đặc điểm xử lý của nhà cung cấp như video.  
Nhạc (ComfyUI) | Đồng bộ | Quy trình cục bộ chạy ngay trên máy chủ ComfyUI đã cấu hình.  
  
Đối với công cụ bất đồng bộ, OpenClaw gửi yêu cầu đến nhà cung cấp, trả về id tác vụ ngay lập tức, và theo dõi công việc trong sổ cái tác vụ. Agent tiếp tục phản hồi các tin nhắn khác trong khi công việc chạy. Khi nhà cung cấp hoàn tất, OpenClaw đánh thức agent với các đường dẫn media đã tạo để agent có thể báo cho người dùng và, khi chính sách phân phối nguồn yêu cầu, chuyển tiếp kết quả qua công cụ nhắn tin. Đối với các tuyến nhóm/kênh chỉ dùng công cụ nhắn tin, OpenClaw coi việc thiếu bằng chứng phân phối bằng công cụ nhắn tin là một lần hoàn tất thất bại và gửi media dự phòng đã tạo trực tiếp đến kênh ban đầu.

## Chuyển giọng nói thành văn bản và Cuộc gọi thoại

Deepgram, DeepInfra, ElevenLabs, Mistral, OpenAI, OpenRouter, SenseAudio và xAI đều có thể chép lại âm thanh gửi đến thông qua đường dẫn `tools.media.audio` theo lô khi được cấu hình. Các Plugin kênh kiểm tra trước ghi chú thoại để gating theo mention hoặc phân tích lệnh sẽ đánh dấu tệp đính kèm đã chép lại trên ngữ cảnh gửi đến, để lượt hiểu media dùng chung tái sử dụng bản chép lại đó thay vì thực hiện lệnh gọi STT thứ hai cho cùng âm thanh.

Deepgram, ElevenLabs, Mistral, OpenAI và xAI cũng đăng ký các nhà cung cấp STT phát trực tuyến cho Cuộc gọi thoại, để âm thanh điện thoại trực tiếp có thể được chuyển tiếp đến nhà cung cấp đã chọn mà không cần chờ bản ghi hoàn tất.

Đối với cuộc trò chuyện trực tiếp với người dùng, hãy ưu tiên [chế độ Talk](</vi/nodes/talk>). Tệp đính kèm âm thanh theo lô vẫn nằm trên đường dẫn media; âm thanh thời gian thực trên trình duyệt, nhấn-để-nói gốc, điện thoại và cuộc họp nên dùng sự kiện Talk và các danh mục theo phạm vi phiên do Gateway trả về.

## Ánh xạ nhà cung cấp (cách nhà cung cấp tách theo các bề mặt)

Google

Các bề mặt hình ảnh, video, nhạc, TTS theo lô, giọng nói thời gian thực backend, và hiểu media.

OpenAI

Các bề mặt hình ảnh, video, TTS theo lô, STT theo lô, STT phát trực tuyến cho Cuộc gọi thoại, giọng nói thời gian thực backend, và nhúng bộ nhớ.

DeepInfra

Các bề mặt định tuyến chat/mô hình, tạo/chỉnh sửa hình ảnh, văn bản thành video, TTS theo lô, STT theo lô, hiểu media hình ảnh, và nhúng bộ nhớ. Các mô hình xếp hạng lại/phân loại/phát hiện đối tượng gốc của DeepInfra chưa được đăng ký cho đến khi OpenClaw có hợp đồng nhà cung cấp chuyên dụng cho các danh mục đó.

xAI

Hình ảnh, video, tìm kiếm, thực thi mã, TTS theo lô, STT theo lô, và STT phát trực tuyến cho Cuộc gọi thoại. Giọng nói thời gian thực của xAI là một khả năng upstream nhưng chưa được đăng ký trong OpenClaw cho đến khi hợp đồng giọng nói thời gian thực dùng chung có thể biểu diễn nó.

## Liên quan

  * [Tạo hình ảnh](</vi/tools/image-generation>)
  * [Tạo video](</vi/tools/video-generation>)
  * [Tạo nhạc](</vi/tools/music-generation>)
  * [Chuyển văn bản thành giọng nói](</vi/tools/tts>)
  * [Hiểu media](</vi/nodes/media-understanding>)
  * [Nút âm thanh](</vi/nodes/audio>)
  * [Chế độ Talk](</vi/nodes/talk>)


Was this useful?YesNo